<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/01-context.md
Document: MAD-002
Status: Draft
Version: 0.1
-->

# 01 — Context

---

# Why This Record Exists

The module and storage model was correct in spirit across several documents but stated nowhere as one accepted whole:

- [MEG-006](../../guides/meg-006-module-platform/01-module-philosophy.md) established that Modules are ordinary Go libraries statically linked into a Platform Binary, composed at build time, with no runtime plugins.
- [MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md) required Modules to use Platform-owned storage contracts and prohibited parallel databases.
- [MEG-015 §03](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md) and [MAD-001](../mad-001-transactional-store-extensibility/index.md) made storage a port and store resolution uniform.
- [MEG-007 §15](../../guides/meg-007-storage-architecture/15-v2-storage-architecture.md) recorded a v2 storage design — one PostgreSQL store, a shared object graph, logical bounded contexts.

But [MAC-001](../mac-001-platform-architecture/index.md), the Canon that answers "what is Mosaic," did not state that Modules never own storage, did not describe how community and essential Modules differ, and [MEG-007](../../guides/meg-007-storage-architecture/index.md)'s earlier chapters still described a mandatory two-database (PostgreSQL and DuckDB) model that its own §15 had moved past.

---

# The Questions To Settle

1. **What is a Module, concretely?** A build artefact, a runtime plugin, a service? The answer governs isolation, delivery and the whole storage question.
2. **Do Modules own storage?** If a content Module (anime, manga, music) can define its own tables, the Platform fragments into many schemas and the "one consistency domain" of the v2 design collapses.
3. **What actually separates a community Module from an essential one?** If the difference is architectural, the two are not equals and the ecosystem is second-class. If it is only delivery, they are equals.
4. **Is analytical processing a second mandatory database?** [MEG-007](../../guides/meg-007-storage-architecture/index.md)'s earlier chapters mandated DuckDB alongside PostgreSQL. That fixes an engine count into the architecture rather than leaving it a capability the Platform can satisfy with one engine now and more later.

---

# Constraints From Existing Canon

- **No runtime plugins** ([MEG-006](../../guides/meg-006-module-platform/01-module-philosophy.md)). Whatever a Module is, it is compiled in, not loaded at runtime.
- **Built-in and Module-delivered capabilities are architectural equals** ([MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md)). Any delivery distinction must not become an architectural one.
- **Storage is a port; no store holds a private path** ([MAD-001](../mad-001-transactional-store-extensibility/index.md)). Any storage answer must keep engine choice behind a contract.
- **The Supervisor owns composition and Generations** ([MAC-001 §05](../mac-001-platform-architecture/05-architecture-principles.md), [MIP-006](../../protocols/mip-006-generation-composition-protocol/index.md)). Delivery of Modules is a Supervisor build-time concern, not a Platform runtime concern.
