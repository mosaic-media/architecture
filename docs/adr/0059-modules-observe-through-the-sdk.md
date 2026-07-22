# 59. Modules observe through the SDK

**Status:** Accepted (built)
**Date:** 2026-07-22

## Context

[ADR 0053](0053-telemetry-is-ambient-in-context.md)–[ADR 0058](0058-telemetry-storage-retention-and-expert-mode.md)
decide how the *Platform* observes itself. They say nothing about modules, and
modules are where a disproportionate share of the difficulty lives: a module is
an anti-corruption layer against a third-party system it does not control
([ADR 0051](0051-modules-as-anti-corruption-layers.md)), which is precisely the
code most likely to encounter a shape nobody predicted.

Today a module has exactly two ways to say anything: return an error, or print.
Both are in use, and the printing case shows the whole problem in one line —
`module-stremio-addons/capability.go` calls

```
log.Printf("stremio: meta %s/%s — identity=%q artwork=%q contributors=%v", …)
```

That line goes to the Platform's stdout from another repository. It is
unstructured, it carries no trace id, it is attributed to nothing, it cannot be
filtered or retained, and it interpolates source-derived values — an identity, an
artwork URL, a contributor list — directly into the message text where no
redaction class can reach them. It is a useful line written the only way that was
available, and it is exactly what
[ADR 0056](0056-redaction-classes-are-the-pii-boundary.md) exists to prevent,
happening across a repository boundary right now.

One property of the SDK decides the shape of the fix. **`github.com/mosaic-media/sdk`
has no dependencies at all** — its `go.mod` is a module line and a Go version,
nothing else. A third party compiles against the contract and against nothing
the Platform happens to have chosen. That is not an accident of a young module;
it is what makes the published surface a *contract* rather than a distribution of
the Platform's taste, and it is the property [ADR 0016](0016-published-contract-surface.md)'s
stop point protects.

## Decision

**The Platform owns the observability plane. The SDK declares a telemetry surface;
the Platform implements it. The SDK stays dependency-free.**

- **Ambient, exactly as in the Platform.** `v1.TelemetryFrom(ctx)` returns the
  handle. This mirrors [ADR 0053](0053-telemetry-is-ambient-in-context.md)
  deliberately, and it also happens to be the only option that scales: there are
  now seven provider roles plus `Import`, each with its own request type, and
  every one of them already takes a `context.Context`. A field on `ImportRequest`
  would cover one of eight.
- **A small interface, declared by the SDK, not re-exported from anywhere.**
  Levelled logging with redaction-classed fields, and `Span(ctx, name)` returning
  a child context and a `Span` with `SetAttributes`/`Fail`/`End`. That is what
  a module needs, which is not the same as what the Platform uses.

  *As built, the counter and histogram this record originally listed are
  **absent**.* The Platform has no metrics yet, and publishing a counter that
  silently discards is worse than publishing nothing: a module author would
  instrument against it and get no data with no indication why. They join the
  surface when the Platform can back them.
- **`v1.Field` mirrors the Platform's redaction classes** — `String`,
  `Sensitive`, `Secret`, `Identifier` — with the same fail-closed default.
  `Sensitive` and `Secret` drop their value at construction exactly as the
  Platform's do. **`Identifier` is the one asymmetry, discovered while
  building:** it must carry its value across, because only the Platform holds
  the install salt and that salt must never reach a module. The Platform
  digests it at the boundary. The
  containment property must cross the boundary or it does not exist: module text
  lands in the Platform's telemetry store and is rendered into an administrator's
  browser, and third-party code is exactly where an unclassified value is most
  likely to originate.
- **The Platform stamps attribution; the module cannot.** Module id, module
  version, trace and span context, and the invoking caller are set by the
  Platform at the invocation seam
  ([ADR 0055](0055-instrument-at-the-seams.md), seam 8). A module cannot claim
  Platform origin, cannot attribute a record to a different module, and cannot
  alter the trace it belongs to.
- **A module configures nothing.** No exporter, no endpoint, no sampling rate, no
  retention, no sink. It emits; the Platform decides where the record goes, how
  long it lives and who may read it. This is what "the Platform manages the
  observability platform" means in practice, and it is the difference between a
  hook and a delegation.
- **Quota, enforced per module.** Telemetry volume is bounded per invocation;
  over-quota records are dropped, and the exhaustion is recorded exactly once at
  the boundary rather than per dropped record — a module in a tight loop would
  otherwise turn the warning into the flood it exists to prevent. Per invocation
  rather than per interval, so a chatty module degrades its own call and nothing
  else. Third-party code must not be able to
  fill the telemetry store, stall a request, or drown another module's records.
- **A module that never mentions telemetry is still fully traced.** Its
  invocation is spanned at the seam, the `context.Context` it receives already
  carries trace context opaquely, the `*http.Client` the Platform hands it
  propagates that context on every outbound call
  ([ADR 0055](0055-instrument-at-the-seams.md), seam 9), and every call it makes
  back into `ContentService` re-reads it. Adopting the surface adds *detail*, not
  correctness — which is the property that makes it safe to leave optional.
- **`TelemetryFrom` on an unseeded context returns a working no-op**, so a module
  is testable and runnable standalone without the Platform, exactly as
  `capabilities/reference` and `test/sdkprobe` are today.

## Alternatives considered

**Have the SDK depend on the OpenTelemetry API.** *Rejected — and this reverses
an earlier recommendation made before the SDK's dependency graph was checked.*
OTel's API module is stable, Apache-2.0 and would give modules tracing with no
adapter, which is why it looks right. Three things rule it out. It destroys the
SDK's zero-dependency property and forces every third-party module to resolve
OTel at a version the Platform effectively pins. It hands modules the *configuration*
surface — a module could set its own sampler or exporter — which is precisely the
ownership this record places with the Platform. And it publishes an
implementation choice as a contract, so replacing OTel later would be a breaking
change to a surface third parties compile against, when it should be an internal
detail. The SDK already declares `ContentService` rather than exporting the
Platform's service type; this is the same discipline applied to telemetry.

**Let each module log wherever it likes.** *Rejected*, and it is the status quo.
It produces one sink per module with no correlation between them, no redaction
discipline, no retention, no access control, and no way for an administrator to
see a module's behaviour in the expert-mode surface.

**Pass a telemetry handle on `ImportRequest`.** *Rejected.* `ImportRequest` was
built to grow and this would fit it, but it covers one of eight entry points; the
seven provider roles would each need the same field added to their own request
type, and every future role would need to remember. Context is already universal.

**Have modules return diagnostics in their result types.** *Rejected.* It only
reports on calls that return, which excludes the two cases that matter most — a
call that hung and a call that panicked — and it forces every result type to
carry a telemetry channel it otherwise has no reason to know about.

## Consequences

- **A bug that crosses into a module stops being opaque.** This is the single
  largest practical gain in the whole telemetry thread, because the module
  boundary is also a repository boundary and it is where a trace currently ends.
- **The SDK bumped to `v0.13.0`** and modules adopt it at their own pace.
  Nothing breaks for a module that does not. `module-stremio-addons` `v0.17.0`
  is the first, converting the `log.Printf` quoted above.
- **The Platform now persists third-party-authored strings.** Redaction classes
  are the containment for personal data; separately, the expert-mode viewer must
  treat module-supplied text as untrusted content when rendering it — escaped,
  never interpreted — since it originates outside the trust boundary and is
  displayed to an administrator.
- **A module can lose telemetry to quota.** That is the correct failure
  direction, and the attributed drop counter is what keeps it from being silent —
  a module whose records are being dropped should be diagnosable, which requires
  the drop itself to be a record.
- **Moving modules out of process changes nothing here.** The surface is an
  interface the Platform implements, so an out-of-process module gets the same
  calls over a different transport. Had the SDK exported OTel, the wire format
  would have become part of the contract.
- **`log.Printf` in a module becomes a review failure**, the same way it is
  becoming one in the Platform. The boundary test cannot reach another
  repository, so this is a convention backed by the module template rather than
  by CI — an honest weaker guarantee.

## Implementation implications

`contracts/platform/v1/telemetry.go` in the SDK holds the `Telemetry` and
`Span` interfaces, `Field` with its constructors, `WithTelemetry`,
`TelemetryFrom` and the no-op.

The Platform implements it in **`internal/platform/app/module_telemetry.go`**,
not in `internal/platform/telemetry` as this record first said. The adapter has
to import the SDK, and `internal/platform/telemetry` is deliberately kept to the
standard library ([ADR 0053](0053-telemetry-is-ambient-in-context.md)); putting
it in `app` also places it beside `moduleSpan`, the seam that installs it, which
is the only place it is installed.
