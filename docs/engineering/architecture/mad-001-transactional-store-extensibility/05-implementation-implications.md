<!--
File: docs/engineering/architecture/mad-001-transactional-store-extensibility/05-implementation-implications.md
Document: MAD-001
Status: Draft
-->

# 05 — Implementation Implications

---

# For The Platform

- Replace named `Tx` accessors with a typed accessor over the transaction scope. In Go this is a package function over `Tx` rather than a method, because methods cannot take type parameters.
- Introduce a `StorageAdapter` port that provides the `UnitOfWork` and binds each resolved store to the live transaction. The built-in PostgreSQL module implements it; a future SQLite module is a drop-in.
- Migrate existing command handlers (slices 1–13) from `tx.Foo()` to uniform resolution. Behaviour is unchanged; only store acquisition changes.

The authoritative shape lives in [MEG-015 §03](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md). This record does not restate it.

---

# For The SDK

- Expose storage as **use** interfaces — read and write through Platform-owned stores. Do not expose schema creation, migration or table definition to Modules.
- Keep `contracts/platform/v1` the only public contract surface. The storage port and transaction scope belong on it once promoted; private Platform internals do not. Enforce with import checks until SDK generation exists, per [MEG-015 §02](../../guides/meg-015-platform-foundation-implementation/02-repository-layout.md).

---

# For Module Authors

- A Module persists through Platform-owned storage contracts. It does not create tables, modify Core Platform schema or open a parallel database, per [MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md).
- A new content type is new rows and new attribute data against the Platform's content-agnostic model — never a schema change authored by the Module.
- A Module that needs a genuinely new **data-owning domain**, rather than new data within the existing model, is proposing Platform and SDK evolution and should be treated as such, per [MAC-001 §03](../mac-001-platform-architecture/03-capability-model.md).

---

# Verification

The decision holds when the reference capability persists atomically with the outbox using only promoted contract packages and no private Platform imports, and when the built-in storage adapter can be substituted without changing a call site. Both are exercised by the [MEG-015 test gates](../../guides/meg-015-platform-foundation-implementation/11-test-gates.md) and the [build sequence](../../guides/meg-015-platform-foundation-implementation/12-build-sequence.md) stop point.
