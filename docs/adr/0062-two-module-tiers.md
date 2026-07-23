# 62. Two module tiers

**Status:** Proposed; the classification half is built (two core metadata
modules exist). The guarantee clause is refined by
[ADR 0072](0072-the-guaranteed-metadata-provider-needs-no-credential.md), which
finds that "no install step that can fail" and "no configuration that can be
omitted" are different properties and that the clause needs both.
**Date:** 2026-07-22

Amends [ADR 0002](0002-module-storage-and-delivery-model.md) §1 and §3, and
narrows [ADR 0007](0007-static-go-module-composition.md) to one of the two tiers.
The delivery change is [ADR 0063](0063-platform-binary-built-by-ci.md), the
boundary mechanism is [ADR 0064](0064-extension-module-boundary.md), and trust is
[ADR 0065](0065-module-distribution-and-trust.md). Nothing here is built.

## Context

Every module in Mosaic is a Go library statically linked into one binary. That is
[ADR 0007](0007-static-go-module-composition.md), and
[ADR 0002](0002-module-storage-and-delivery-model.md) §3 goes further: essential
and community modules "differ only in delivery… Architecture: Identical." That
symmetry was a deliberate anti-second-class-ecosystem stance, and it has been
proven twice — the Stremio and remote-playback modules are both their own
repositories importing only the SDK.

The symmetry does not survive contact with what the two kinds of module actually
need.

**The PostgreSQL module cannot be anywhere but in the address space.** It
participates in a `UnitOfWork` ([ADR 0014](0014-storage-authority-and-transaction-scope.md)),
and a transaction does not survive a serialization boundary. No amount of
protocol design makes an out-of-process store a peer of an in-process one; the
`Tx` type exists precisely so that state and outbox events commit together.

**Third-party code in one address space has three problems that are not about
security.** One dependency graph — a module that wants its own SQLite cache, or a
version of a library the Platform pins differently, cannot have it, and with an
ecosystem that is the normal case rather than the exception. One failure domain —
a panic in a third-party module takes the Platform with it, indistinguishable
from the Platform's own. One resource budget — there is no boundary at which to
measure that a module used too much memory, so there is nothing to enforce.

**And some modules are neither.** Playback does not join a transaction, so the
first argument does not apply to it. But Mosaic without playback is not a media
centre; a deployment that cannot play anything is not a degraded Mosaic, it is
not Mosaic. The same holds for metadata and search: a fresh install with no way
to identify or find content reads as broken
([ADR 0035](0035-metadata-as-required-capability.md) made that case already).
Whatever these are, they cannot be something a user might fail to install.

One tier cannot serve all three. This record splits it.

## Decision

**Mosaic has two module tiers. A module is a *core module* for one of exactly two
reasons, and an *extension module* otherwise.**

> **Coupling.** It must share the Platform's address space to do its job — it
> participates in a `UnitOfWork`, or it sits on a hot path where a round trip per
> call is a real cost.
>
> **Guarantee.** It backs a capability class Mosaic cannot function without, so
> at least one implementation must be present in every binary, with no install
> step that can fail.

Either reason is sufficient. Both imply the same delivery: **compiled into the
Platform binary, first-party, curated.** Everything else — every module whose
absence degrades Mosaic rather than negating it — is an extension module,
delivered as its own process.

| | Core module | Extension module |
|---|---|---|
| Reason it is one | Coupling, or guarantee | Neither applies |
| Delivery | Compiled into the binary by Mosaic's CI | Its own binary, installed |
| Process | The Platform's | Its own |
| Dependencies | Shared with the Platform and every other core module | Entirely its own |
| Authorship | First-party only | Anyone |
| Failure | Takes the Platform down | Degrades one capability |
| Examples | `postgres` (coupling), local and remote playback (guarantee), a default metadata provider (guarantee) | `module-stremio-addons` |

Three things follow that are worth stating outright rather than leaving to be
inferred.

**The second clause is a product judgement, and calling it a technical test would
be dishonest.** "Mosaic cannot function without playback" is not derivable from
the code; it is a statement about what Mosaic *is*. That is fine — it is exactly
the kind of thing an architecture record should decide — but it means the tier
boundary has a discretionary half, and adding to the core set is therefore a
deliberate decision each time rather than the application of a rule. The
coupling clause is mechanical; the guarantee clause is not.

**A third party can never be a core module.** Not as policy, but because both
clauses exclude it. Coupling requires sharing a dependency graph and a failure
domain, which is only tractable across a small curated set. Guarantee requires
being present in a binary Mosaic's CI builds, which only first-party code can be.
This is a real asymmetry with [ADR 0002](0002-module-storage-and-delivery-model.md)
§3 and it should not be smoothed over: a third-party module is a **first-class
extension module**, not a second-class core one, but the two tiers are not equals
and never can be.

**The tier is a delivery and coupling decision, not a contract decision.** Both
tiers implement the same SDK Go interfaces — `Capability`, the provider roles
([ADR 0027](0027-modules-as-typed-capability-providers.md)), `ContentService`,
`Telemetry` ([ADR 0059](0059-modules-observe-through-the-sdk.md)). A module does
not know which tier it is in, and moving one between tiers is a build change
rather than a rewrite. [ADR 0064](0064-extension-module-boundary.md) is how that
holds across a process.

## Alternatives considered

**Keep one tier, everything static
([ADR 0007](0007-static-go-module-composition.md)).** *Rejected.* It leaves
third-party code sharing a dependency graph and a failure domain with the
Platform, and it puts a Go toolchain in the install path
([ADR 0063](0063-platform-binary-built-by-ci.md) argues that half). ADR 0007's
rejection of module RPC — *paying a distributed-systems cost for a problem that
is not distributed* — remains correct for core modules, and this record keeps it
there. It is wrong for third-party code, where the boundary is the point rather
than the cost.

**One tier, everything out of process.** *Rejected.* The storage module cannot
be, and rebuilding transaction semantics over RPC to make PostgreSQL a peer of a
metadata addon is a large cost for no benefit.

**One tier, everything in process, with a curated-only ecosystem.** *Rejected.*
It solves the dependency and failure-domain problems by not having an ecosystem,
which forfeits the reason the SDK exists
([ADR 0008](0008-sdk-as-public-contract-language.md)): format coverage cannot be
built by one person.

**Make the coupling clause the only test.** *Rejected*, and this was the first
draft of this record. It is cleaner — a purely mechanical rule with no
discretion — but it classifies playback as an extension module, which means a
Mosaic install can be missing the thing that makes it a media centre because an
install step failed. The guarantee clause exists to make that impossible, and
its discretionary nature is the price.

**Three tiers, splitting first-party-bundled from first-party-optional.**
*Rejected as premature.* It may eventually be right — a first-party module that
is neither coupled nor guaranteed is really an extension module that happens to
be written by us, and that is already expressible. Adding a tier before one is
needed is inventing structure.

## Consequences

- **[ADR 0002](0002-module-storage-and-delivery-model.md) §1 and §3 are no longer
  true.** §1 ("a Module is a Go library compiled into the binary") holds for core
  modules only; §3's identical-architecture claim is contradicted outright. §2
  (modules do not own storage or schema) and §4 (analytical processing is a port)
  are **unchanged and still govern** — including for out-of-process modules, where
  [ADR 0064](0064-extension-module-boundary.md) restates the limit.
- **The core set must stay small, permanently.** Core modules share one dependency
  graph, one address space and one failure domain. That problem is not solved for
  them; it is moved to Mosaic's CI, where it is tractable only because the set is
  curated and closed.
- **`module-stremio-addons` is an extension module**, which is the stronger
  version of the proof [ADR 0020](0020-optional-module-composition.md) set out to
  make: built the third-party way, and now *deployed* the third-party way too.
- **`module-remote-playback` is a core module**, so it keeps its direct
  `require` in the Platform's `go.mod`. [ADR 0008](0008-sdk-as-public-contract-language.md)
  says the Platform must not depend on modules; for core modules that dependency
  is now accepted rather than bridged, because they are first-party
  infrastructure and pretending otherwise would be worse than admitting it.
- **The register of what is and is not core needs a home.** With a discretionary
  clause, "why is this core?" must have an answer written down per module, or the
  set will drift by accretion. The classification belongs beside the role-class
  table in [ADR 0063](0063-platform-binary-built-by-ci.md).

**Open.** Whether a first-party module that is neither coupled nor guaranteed
should be bundled anyway for convenience — the third-tier question above — is
deferred until one exists.
