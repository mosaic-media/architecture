<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/04-consequences.md
Document: MAD-002
Status: Draft
Version: 0.1
-->

# 04 — Consequences

---

# What This Enables

- **One consistency domain.** State, events and analytical derivations share one Platform-owned store, so atomicity, backup and migration remain single concerns.
- **A genuine ecosystem.** A community Module is architecturally a first-class Platform capability. Publishing anime support is the same shape of work as the built-in PostgreSQL adapter.
- **Deferred engine decisions.** The Platform can ship on one database and add a second only when a measured analytical need appears, without re-architecting — the port absorbs the change.
- **Content growth without schema growth.** New media types are new rows against the content-agnostic model, so the schema does not accrete a table tree per media type.

---

# Accepted Costs

- **The Platform must own a genuinely content-agnostic schema.** If that model is not general enough, Modules are squeezed. Its design is therefore load-bearing — see the deferred follow-up below.
- **A community Module cannot solve a storage need the shared model does not support** by reaching for its own table. Such a need surfaces as a Platform and SDK evolution request, deliberately, rather than being absorbed silently inside a Module.
- **Analytical work is constrained to what the port exposes.** Until a second engine is added, analytical features live within PostgreSQL's reach; the port keeps that boundary explicit rather than hidden.

---

# Canon And Guide Changes

- [MAC-001 §04](../mac-001-platform-architecture/04-module-model.md) — Module Model gains the delivery-model distinction and the storage-ownership rule; [§01](../mac-001-platform-architecture/01-platform-model.md) lists analytical processing among the port-based infrastructure concerns.
- [MEG-007](../../guides/meg-007-storage-architecture/15-v2-storage-architecture.md) — reconciled to one Platform-owned store with a content-agnostic schema and an analytical processing port; the earlier mandatory-DuckDB chapters are reframed as an optional adapter behind that port.

---

# Deferred Follow-Ups

- **Canonising the content-agnostic object model in full.** The node/relation model is described at principle level in [MEG-007 §15](../../guides/meg-007-storage-architecture/15-v2-storage-architecture.md). Its complete table-level design (identity scheme, ordering, source bindings, orphan handling) is a further storage-architecture effort, not settled here.
- **Confirming bounded contexts against a single transaction scope.** The media-domain contexts must not read across each other's tables; the reading that one transaction spans the acting context's stores plus the shared outbox needs confirmation when those contexts are built (carried from [MAD-001 §04](../mad-001-transactional-store-extensibility/04-consequences.md)).
- **Provider union and priority routing.** How several Modules of the same capability cooperate (union or context priority) is routing owned by [MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md), distinct from this storage-and-delivery decision.
