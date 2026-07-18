<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/03-alternatives-considered.md
Document: MAD-002
Status: Draft
-->

# 03 — Alternatives Considered

---

# Module-Owned Storage

Let each Module define and own its own tables or database.

- **Cost:** the "one consistency domain" of the v2 design collapses into many schemas; atomicity across a Module's data and the shared outbox is no longer guaranteed; backup, migration and access policy fragment per Module.
- **Conflicts with:** [MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md)'s parallel-database prohibition and [MAD-001](../mad-001-transactional-store-extensibility/index.md)'s single transaction boundary.
- **Rejected.** Modules use Platform-owned storage; the schema is made content-agnostic so they do not need their own.

---

# Architectural Distinction Between Community And Essential Modules

Treat essential Modules as a privileged internal class with capabilities community Modules cannot have.

- **Cost:** breaks the [MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md) principle that built-in and Module-delivered capabilities are architectural equals; creates a second-class ecosystem and a private path, the exact drift [MAD-001](../mad-001-transactional-store-extensibility/index.md) removed for storage.
- **Rejected.** The distinction is delivery and selectability only; the architecture is identical.

---

# A Mandatory Second Analytical Database

Keep the earlier model where DuckDB is a required engine alongside PostgreSQL from day one.

- **Cost:** fixes an engine count into the architecture before the workload justifies it; adds an operational dependency, a second consistency boundary and a sync path for the Platform Foundation, which one PostgreSQL store handles.
- **Rejected in this form.** The analytical *capability* is mandated behind a port; the *engine count* is not. PostgreSQL satisfies the port now, and a second engine is added later only if needed — as an essential Module behind the same port, not a parallel authority.

---

# Runtime Plugin Loading

Load Modules dynamically at runtime instead of compiling them in.

- **Cost:** reintroduces a runtime boundary, a plugin ABI, and dynamic-loading failure modes; contradicts [MEG-006](../../guides/meg-006-module-platform/01-module-philosophy.md)'s static-composition philosophy and the deterministic-Generation model.
- **Rejected.** Modules are Go libraries the Supervisor compiles into the binary; delivery differences are resolved at build time, not runtime.
