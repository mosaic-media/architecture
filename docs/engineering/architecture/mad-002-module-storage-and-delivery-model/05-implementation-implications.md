<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/05-implementation-implications.md
Document: MAD-002
Status: Draft
-->

# 05 — Implementation Implications

---

# For The Platform

- Own the storage authority end to end: schema, migrations, transactions, access policy and backup. Expose persistence to capabilities only through storage contracts.
- Design the shared schema to be content-agnostic so Modules map onto it. Treat that model's generality as a first-class requirement, not an afterthought.
- Define analytical processing as a port. Provide the PostgreSQL-backed adapter first; keep the port free of engine-specific assumptions so a second adapter can be added without touching callers.

---

# For The Supervisor

- Resolve Module delivery at build time. Essential Modules come from the Platform repository and are always included; community Modules are fetched from their own repositories per user selection.
- Compose the selected set into one Platform Binary and activate it as a Generation, per [MIP-006 — Generation Composition Protocol](../../protocols/mip-006-generation-composition-protocol/index.md). No Module is loaded at runtime.

---

# For Module Authors

- A Module is a normal Go library depending on the SDK. It persists through Platform-owned storage contracts and never defines its own tables, modifies Core Platform schema, or opens a parallel database, per [MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md).
- A new content type is new rows and attribute data against the content-agnostic model, not a schema change.
- A genuinely new data-owning domain is a Platform and SDK evolution request ([MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md)), not work to do inside the Module.
- Community and essential authorship are the same task. "Essential" affects only where the Module ships and whether it can be deselected.

---

# For The Platform Foundation Build

The first Platform build already treats PostgreSQL as an essential Module behind storage contracts ([MEG-015 §02](../../guides/meg-015-platform-foundation-implementation/02-repository-layout.md)) and resolves stores uniformly ([MEG-015 §03](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md), per [MAD-001](../mad-001-transactional-store-extensibility/index.md)). MAD-002 adds no new obligation to the foundation build beyond keeping analytical processing behind a port when that work begins; the reference capability remains non-media and storage-through-contracts.
