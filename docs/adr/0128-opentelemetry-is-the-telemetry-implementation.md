# 128. OpenTelemetry is the telemetry implementation

**Status:** Built in part. The SDK's surface is backed by the OTel API, the Supervisor's telemetry is the OTel SDK with a file exporter and optional OTLP, and **all six modules are on it** — one line each, which is the evidence for this record's central claim that the authoring surface does not change. The module-facing half of the SDK's surface is guarded against naming an OTel type, so the implementation underneath stays replaceable. Not built: the Platform's own ~1,300 lines and its PostgreSQL store, so the module adapter still carries its own copy of the classification mapping rather than the SDK's `Encoder`. Consumers require the SDK at a **pseudo-version** — tag pushes are refused in the environment this was built in, and `go get sdk@<sha>` resolves an untagged commit as an ordinary require with no `replace`.
**Date:** 2026-08-09

Reverses the OpenTelemetry alternative that
[ADR 0059](0059-modules-observe-through-the-sdk.md) and
[ADR 0060](0060-the-supervisor-observes-independently.md) each rejected, and
with it the SDK's zero-dependency rule. Does **not** reverse ADR 0059's
decision — see the first bullet, which is the whole point of this record.

## Context

Mosaic has hand-written its own telemetry three times.

The Platform has ~1,300 lines of it — `Record`, `Field`, `Level`, `Sink`,
`Span`, `TraceContext`, a batching buffer, a file sink, a console sink, a
PostgreSQL store with partitioning and retention
([ADR 0053](0053-telemetry-is-ambient-in-context.md)–[ADR 0058](0058-telemetry-storage-retention-and-expert-mode.md)).
The SDK declares a second, smaller copy for modules to author against
(ADR 0059). The Supervisor has just written a third, because it may not import
the Platform's and there was nowhere else to get one (ADR 0060).

**The third one is what makes this a decision rather than a preference.** Its
record format is duplicated from the Platform's on purpose, and the record
that landed it says so in as many words: the two binaries must agree on a
serialisation format, nothing structurally holds them together, and the whole
guard is a test that names the JSON keys. That is a real hazard, honestly
mitigated, and it exists because Mosaic has no shared telemetry vocabulary that
both processes are allowed to import. A fourth process — an out-of-process
extension module (ADR 0077) — would need a fourth copy or a fourth exemption.

Each of the three rejections was locally correct on the facts available:

- ADR 0059 rejected the OTel API in the SDK to protect the SDK's
  zero-dependency property, to keep the *configuration* surface away from
  modules, and to avoid publishing an implementation choice as a contract.
- ADR 0060 rejected "ships the OTel SDK and exports over OTLP" because an
  exporter needs a running collector, and the Supervisor may assume nothing
  else is up.

What none of them weighed is the cost of the alternative compounding. Three
formats, three redaction implementations, three sets of sinks, and a growing
set of processes that must agree without a shared type — against an ecosystem
where every collector, every backend and every dashboard already speaks one
protocol Mosaic does not.

**Two facts about OpenTelemetry Go decide the shape**, and both were measured
rather than assumed:

| Module | Version | Modules pulled in |
|---|---|---|
| `go.opentelemetry.io/otel/trace` (API) | `v1.45.0` | 3 |
| `go.opentelemetry.io/otel/log` (API) | **`v0.21.0`** | 3 |
| `go.opentelemetry.io/otel/sdk/log` | `v0.21.0` | 12 |

The API modules are small — three modules, one of which is a hash function —
and OTel's own guidance is that a *library* imports the API and a *binary*
wires the SDK. That split maps onto Mosaic exactly: the published SDK and the
modules take the API, the Platform and the Supervisor take the SDK.

The logs API being `v0.21.0` is the sharpest fact here and it is stated rather
than buried: **Mosaic's telemetry is predominantly logging, and the logging half
of OpenTelemetry Go is not 1.0.** The tracing half is, and is covered by that
project's compatibility guarantee.

## Decision

**OpenTelemetry is Mosaic's telemetry implementation, in every process. The
SDK's authoring surface stays, and gains the OTel API as its first dependency.**

- **The authoring surface is unchanged and ADR 0059's decision stands.**
  `v1.TelemetryFrom(ctx)`, `v1.Telemetry`, `v1.Span` and classified `v1.Field`
  constructors keep their shapes and their semantics. What changes is what sits
  behind them: an OTel `log.Record` and an OTel span rather than a Mosaic
  `Record` and a Mosaic `Span`. **A module written against the SDK today needs
  no change beyond a version bump**, and neither do the Platform's 324
  classified field call sites. This is the difference between standardising the
  implementation and republishing it as the contract, and it is what makes the
  reversal narrow.
- **Redaction stays at construction, and it is the reason the surface stays.**
  ADR 0056's property is that a classified value is dropped *before* the Field
  exists, so it is never buffered, never queued and never in a heap dump. OTel's
  attribute model has no such notion — `log.String(k, v)` carries `v`. So a
  classified constructor produces an OTel attribute with the value already gone,
  and `Sensitive`, `Secret` and `Identifier` are exactly where they were. A
  redaction processor running at export would be a strictly weaker guarantee,
  because by then the value has already travelled.
- **A module still configures nothing.** It takes the OTel *API*, never the SDK
  and never a global provider, and it receives its logger and tracer through the
  context the Platform seeds. It cannot set a sampler, an exporter or an
  endpoint, which is the ownership ADR 0059 placed with the Platform and this
  record does not move.
- **The Platform wires the SDK and owns the pipeline.** The PostgreSQL store
  becomes an OTel log processor rather than a bespoke sink; the file sink becomes
  a file exporter; retention, partitioning and the expert-mode reader are
  unchanged, because they are about storage and access rather than about record
  production.
- **The Supervisor takes the SDK with a file exporter and no collector.** ADR
  0060's objection was to *OTLP* — an exporter needing something else to be
  alive — and it was right. A file exporter needs nothing. OTLP becomes a thing
  an operator may configure, off by default, and never a thing the Supervisor
  requires in order to record that a child would not start.
- **The duplicated record format goes away.** The Supervisor's hand-written
  entry, the test that pins its JSON keys, and the Platform's parallel definition
  are all replaced by one vocabulary both processes import. That was ADR 0060's
  named open question — "either the Supervisor imports a small shared package or
  it duplicates a struct definition" — and this is the shared package, sourced
  from outside Mosaic so neither process owns it.
- **The SDK's zero-dependency rule ends, and is replaced by a narrower one:**
  the SDK may depend on the OpenTelemetry **API** modules and nothing else. Not
  the SDK modules, not an exporter, not a collector client. The property being
  protected was never "zero" for its own sake — it was that a third party
  compiles against a contract rather than against the Platform's taste. A
  vendor-neutral, CNCF-governed API that the third party very likely already has
  in their build is a different thing from a Mosaic-flavoured one.

## Alternatives

**Replace the SDK's surface with OTel's outright**, so modules call
`otel.Tracer(…)` and `otel.Logger(…)` directly and `v1.Telemetry` is deleted.
*Rejected*, and it is the fuller reading of "standardise on OpenTelemetry", so
the reason matters. It gives up redaction at construction across the module
boundary, which is the exact containment ADR 0059 was written to establish and
the boundary where ADR 0056 says an unclassified value is most likely to
originate. It also hands modules the global provider, so a module could set a
sampler or an exporter — the configuration ownership ADR 0059 placed with the
Platform. And it would require changes in all six module repositories to buy
those losses. If the redaction property is later judged not worth the wrapper,
that is a new record; it is not this one.

**Keep the hand-written stack and share it as a fourth published module.**
*Rejected.* It is the smallest change and it solves only the duplication, not
the interoperability: a Mosaic-shaped record still reaches no collector, no
dashboard and no backend without an adapter somebody writes. It also creates a
module to version and keep in step across four consumers, which is the cost ADR
0060 declined to take on for one struct and which does not get cheaper at four.

**Adopt the trace API only, and leave logging hand-written.** *Rejected*, though
it is the one that survives the `v0.21.0` fact most comfortably. It leaves the
duplication exactly where it is, because the duplicated thing is the *log*
record, not the span — and it would put Mosaic in the position of shipping two
telemetry models in one process, correlated by hand.

**Wait for the logs API to reach 1.0.** *Rejected*, and this is the one to
revisit if the adoption goes badly. The cost of waiting is paid in the coin this
record exists to stop spending: every process added before then hand-writes a
fourth copy. And Mosaic's own release discipline already absorbs exactly this
shape of churn — [ADR 0127](0127-the-monitored-version-is-the-contract-not-the-artefact.md)
decided two days ago that the contract's *minor* is the breaking component
before 1.0, so an OTel logs API bump is an SDK minor bump, which is the cadence
the SDK already has.

## Consequences

- **The SDK acquires a dependency, and its `go.mod` stops being a module line
  and a Go version.** That is a genuine loss and the rule in every `CLAUDE.md`
  that states it must change rather than be quietly contradicted. A third-party
  module author now resolves OTel at a version Mosaic's SDK effectively floors.
- **A pre-1.0 API enters a published contract.** `go.opentelemetry.io/otel/log`
  makes no compatibility promise, so a breaking change there is a breaking change
  to what modules compile against. The mitigation is that the SDK's surface is a
  wrapper rather than a re-export: an OTel logs API break is absorbed inside the
  SDK for anything that does not change the shape of a levelled record with
  attributes, which is most of what could change.
- **Everything Mosaic emits becomes readable by tooling nobody has to write.**
  An operator can point a collector at it, and traces that today end at the
  expert-mode viewer can reach anything that speaks OTLP. This is the whole
  benefit and it is worth naming plainly.
- **The out-of-process module harness gets its telemetry for free.** ADR 0077's
  gRPC boundary currently has to carry the SDK's telemetry calls over the wire as
  Mosaic-shaped messages; OTel's context propagation and record model cross a
  process boundary as their ordinary business.
- **Three implementations become one, and the one is not Mosaic's.** That is
  the point, and it is also the risk being taken: a dependency that is not
  Mosaic's can move in directions Mosaic did not choose, and the answer will
  sometimes have to be a version floor rather than a fix.
- **The work is large and is not one slice.** The SDK's surface, the Platform's
  ~1,300 lines and its PostgreSQL store, the Supervisor's file, and a version
  bump in six module repositories. The order is forced: the SDK first, because
  every other repository compiles against its shape.
