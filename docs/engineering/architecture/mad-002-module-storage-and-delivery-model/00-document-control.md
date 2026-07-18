<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/00-document-control.md
Document: MAD-002
Status: Draft
-->

# Document Control

---

# Document Information

| Field | Value |
|-------|-------|
| Document | MAD-002 |
| Title | Module Storage and Delivery Model |
| Status | Draft |
| Decision Status | Accepted |
| Owner | AdamNi-7080 |
| Audience | Platform, SDK, Supervisor and Module engineers |
| Classification | Architecture decision record |

`Status` and `Version` describe this record's own documentation maturity. `Decision Status` describes the decision it captures. The decision was accepted in an architecture working session as the approved way forward.

---

# Authority

MAD-002 records an accepted decision and its reasoning. It does not define architecture and it does not provide implementation guidance.

- The accepted module and storage architecture it makes Canon is owned by [MAC-001 — Platform Architecture](../mac-001-platform-architecture/index.md).
- The storage architecture that realises it is owned by [MEG-007 — Storage Architecture](../../guides/meg-007-storage-architecture/index.md).
- The module engineering practice it depends on is owned by [MEG-006 — Module Platform](../../guides/meg-006-module-platform/index.md).

Per [MDG-001 §02](../../documentation/mdg-001-documentation-authority-guide/02-document-types.md), a decision record preserves reasoning and alternatives that must not live inside Canon or Engineering Guides. This record should remain effectively immutable; a later change of direction should be a new decision rather than a rewrite of this one.

---

# Relationship To The Prior Decision

[MAD-001 — Transactional Store Extensibility](../mad-001-transactional-store-extensibility/index.md) established that storage is a port and stores are resolved uniformly, so no store holds a private path into the transaction boundary. MAD-002 generalises the same principle to the whole module and storage model: what that decision did for the transaction contract, MAD-002 states for delivery, schema ownership and analytical processing.

---

# Affected Specifications

| Specification | Effect |
|---------------|--------|
| [MAC-001 — Platform Architecture](../mac-001-platform-architecture/04-module-model.md) | Module Model gains the delivery-model distinction and the storage-ownership rule. Carries the decision as Canon. |
| [MEG-007 — Storage Architecture](../../guides/meg-007-storage-architecture/index.md) | Reconciled to one Platform-owned store with a content-agnostic schema and an analytical processing port. |
| [MEG-006 — Module Platform](../../guides/meg-006-module-platform/index.md) | Unchanged. Its build-time composition and no-runtime-plugin principles are honoured. |
| [MIP-005 — Module Adapter Contract Protocol](../../protocols/mip-005-module-adapter-contract-protocol/index.md) | Unchanged. Its "modules use Platform-owned storage" rule is reinforced. |

---

# Required Reading

- [MAC-001 — Platform Architecture](../mac-001-platform-architecture/04-module-model.md)
- [MEG-006 — Module Platform](../../guides/meg-006-module-platform/01-module-philosophy.md)
- [MEG-007 — Storage Architecture](../../guides/meg-007-storage-architecture/15-v2-storage-architecture.md)
- [MAD-001 — Transactional Store Extensibility](../mad-001-transactional-store-extensibility/index.md)
- [MIP-006 — Generation Composition Protocol](../../protocols/mip-006-generation-composition-protocol/index.md)
