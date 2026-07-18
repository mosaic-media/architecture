<!--
File: docs/engineering/architecture/mad-001-transactional-store-extensibility/04-consequences.md
Document: MAD-001
Status: Draft
-->

# 04 — Consequences

---

# Accepted Costs

- **Rework.** Every `tx.Users()`-style call site across the thirteen built slices moves to uniform resolution. The change is contained to how stores are *obtained*, not what they do.
- **A new port surface.** `StorageAdapter` and the transaction scope become part of the candidate contract surface promoted into `contracts/platform/v1`.

# Preserved Properties

- **Type safety.** The typed accessor keeps call sites fully typed with no assertion.
- **Atomicity.** One transaction, one storage adapter — unchanged. No parallel database, satisfying [MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md) by construction.
- **Capability equality.** Core and capability stores are obtained identically; no store holds a private path into the transaction.

---

# Changes Carried In The Platform Foundation Guide

- **[§03 Platform Contracts](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md)** — closed `Tx` replaced with uniform, port-based resolution; a Storage Extensibility Boundary section added.
- **[§04 Application Boundaries](../../guides/meg-015-platform-foundation-implementation/04-application-boundaries.md)** — left unchanged. It was already written abstractly ("load state through contracts"), which confirmed the abstraction was right and only §03's concrete shape was wrong.
- **[§12 Build Sequence](../../guides/meg-015-platform-foundation-implementation/12-build-sequence.md)** — records that slice 13 was blocked on the contract shape and is unblocked by this decision.
- **[§00 Document Control](../../guides/meg-015-platform-foundation-implementation/00-document-control.md)** — maturity note records the correction.

---

# Related Sequencing Fix

Resolving this decision closed an adjacent sequencing gap in the [MEG-015 build sequence](../../guides/meg-015-platform-foundation-implementation/12-build-sequence.md): the reference capability was gated on building against `contracts/platform/v1`, yet that package was not populated until the following slice. Promoting the proven contracts — now including the storage port — into `contracts/platform/v1` became the first step of slice 13. This fix is minor and fully carried by that guide; it is noted here only because the two findings share a slice.

---

# Deferred Follow-Ups

These were identified during the decision and deliberately not resolved here.

## Provider union and priority routing

The motivating extensibility need for many capabilities is provider **union and context priority** — for example several search Modules (film, television, anime) all answering a query, or one taking priority by context. This is a routing concern, distinct from transactional storage, and is already owned by [MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md) (Multiple Providers, Provider Routing, Orchestration Policy, Capability Managers). The open work is only that the [MEG-015 reference-capability slice](../../guides/meg-015-platform-foundation-implementation/12-build-sequence.md) does not yet build a Capability Manager to demonstrate it. Tracked as a separate item; not part of this decision.

## Canonisation of the content-agnostic object model

The decision relies on the Platform owning a content-agnostic object model so Modules never own schema. A concrete object graph (a recursive node tree with a separate relation graph, engine-neutral identity and JSONB-style attributes) exists as a working architecture reference. Canonising it is a separate effort and its likely home is [MEG-007 — Storage Architecture](../../guides/meg-007-storage-architecture/index.md); it is out of scope for this record.

## Bounded contexts versus a single transaction scope

A media-domain design organises persistence into bounded contexts that do not read across into each other's tables and communicate through events. The consistent reading is that a single `WithinTx` scope spans the acting context's stores plus the shared outbox, which uniform resolution supports. This should be confirmed when the media contexts are built.
