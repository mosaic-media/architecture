<!--
File: docs/engineering/architecture/mad-001-transactional-store-extensibility/03-alternatives-considered.md
Document: MAD-001
Status: Draft
-->

# 03 — Alternatives Considered

---

# Evaluation Dimensions

Each option was weighed on four dimensions: **type safety** at capability call sites, **transaction atomicity** risk, **blast radius** on the thirteen already-built slices, and which document's **authority** it touches.

---

# Options

## a. Extension registry on `Tx`

A generic `Extension(key string) any` method that capabilities register into at startup; core accessors unchanged.

- Type safety: **lost at the call site** — `any` plus a cast, stringly-typed key, runtime failure if unregistered.
- Atomicity: preserved (same transaction).
- Blast radius: none — purely additive.
- Authority: [MEG-015 §03](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md); brushes the "generic infrastructure port" anti-pattern in [MEG-004 §04](../../guides/meg-004-hexagonal-architecture/04-driven-ports.md).
- **Rejected:** it is an access gate — a store must *ask permission* to join the transaction — which is exactly the ceremony the accepted principle removes.

## b. Generic transactional handle *(chosen)*

`WithinTx` yields a transaction scope; all stores, core included, are obtained through a typed accessor over that scope; named `Tx` methods removed.

- Type safety: preserved (typed accessor).
- Atomicity: preserved.
- Blast radius: **high** — every command handler in slices 1–13 moves off `tx.Foo()` onto uniform resolution.
- Authority: [MEG-015 §03](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md) and [§04](../../guides/meg-015-platform-foundation-implementation/04-application-boundaries.md); best-aligned with the capability equality of [MAC-001](../mac-001-platform-architecture/03-capability-model.md).
- **Chosen:** the only option that removes the private path instead of decorating it, and the static-composition model makes it free of any runtime bridge.

## c. Per-capability `UnitOfWork`

A capability gets its own `UnitOfWork` wrapping or sharing the underlying transaction.

- Type safety: preserved.
- Atomicity: **conditional.** Genuine only if it shares the identical underlying transaction handle. If it opens its own transaction it is a second commit that *appears* atomic but is not, and it trips [MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md)'s parallel-database prohibition. If it shares the handle, it still needs that handle to be handed over — exactly what the closed `Tx` refused — so it collapses into (a), (b) or (d) plus a wrapper.
- **Rejected:** on its own it either fails to deliver atomicity or does not solve the handover.

## d. Typed generic accessor with a build-time registry

`Store[T](tx)` resolving a registry of transaction-bound store constructors populated at static composition; core accessors may remain.

- Type safety: preserved (generics, no cast).
- Atomicity: preserved.
- Blast radius: none — additive; core accessors can stay.
- Authority: [MEG-015 §03](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md); consistent with build-time composition.
- **Folded into (b):** (d) is the resolution mechanism (b) uses. It was considered as a standalone half-measure that keeps core accessors privileged, but since the decision demotes PostgreSQL to a swappable storage module, the core accessors are removed rather than retained — the full (b) form.

## e. Accept the closed list

No structural change; treat each new store as deliberate Platform and SDK evolution.

- Type safety and atomicity: full.
- Blast radius: none now — but every future store edits Core Platform `Tx` and breaks capability equality.
- Authority: leans on [MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md) / [MEG-006 §13](../../guides/meg-006-module-platform/13-platform-guidelines.md) allowing Platform evolution for new capabilities.
- **Rejected:** it is the honest baseline for measuring cost, but it preserves the private path and degrades as capability count grows.

---

# Summary

| Option | Type safety | Atomicity | Blast radius (slices 1–13) | Outcome |
|--------|-------------|-----------|-----------------------------|---------|
| a. Extension registry | Lost at call site | Preserved | None | Rejected — access gate |
| b. Generic handle | Preserved | Preserved | High | **Chosen** |
| c. Per-capability UoW | Preserved | Conditional | Low–medium | Rejected — atomicity/handover |
| d. Typed registry | Preserved | Preserved | None | Folded into (b) |
| e. Accept closed list | Full | Full | None now | Rejected — preserves private path |
