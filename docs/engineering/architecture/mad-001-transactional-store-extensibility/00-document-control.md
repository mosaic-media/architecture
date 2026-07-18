<!--
File: docs/engineering/architecture/mad-001-transactional-store-extensibility/00-document-control.md
Document: MAD-001
Status: Draft
-->

# Document Control

---

# Document Information

| Field | Value |
|-------|-------|
| Document | MAD-001 |
| Title | Transactional Store Extensibility |
| Status | Draft |
| Decision Status | Accepted |
| Owner | AdamNi-7080 |
| Audience | Platform, SDK and Module engineers |
| Classification | Architecture decision record |

`Status` and `Version` describe this record's own documentation maturity. `Decision Status` describes the decision it captures. The decision was accepted in an architecture working session; the specification it corrects, [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/index.md), remains `Draft` pending its own review.

---

# Authority

MAD-001 records a single accepted decision. It does not define architecture and it does not provide implementation guidance.

- The accepted architecture it depends upon is owned by [MAC-001 — Platform Architecture](../mac-001-platform-architecture/index.md).
- The contract shape it corrects is owned by [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/index.md).
- The extensibility principle it honours is owned by [MEG-006 — Module Platform](../../guides/meg-006-module-platform/index.md).

Per [MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/02-document-types.md), a decision record preserves reasoning and alternatives that must not live inside Canon or Engineering Guides. This record should remain effectively immutable; a later change of direction should be captured as a new decision rather than by rewriting this one.

---

# Affected Specifications

| Specification | Effect |
|---------------|--------|
| [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md) | Contract shape corrected; build sequence note added. Carries the decision. |
| [MEG-006 — Module Platform](../../guides/meg-006-module-platform/index.md) | Unchanged. Its extensibility principle is honoured, not altered. |
| [MAC-001 — Platform Architecture](../mac-001-platform-architecture/index.md) | Unchanged. Its capability-equality model is honoured, not altered. |
| [MIP-005 — Module Adapter Contract Protocol](../../protocols/mip-005-module-adapter-contract-protocol/index.md) | Unchanged. Its "modules use Platform-owned storage" rule is reinforced. |

---

# Required Reading

- [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md)
- [MEG-006 — Module Platform](../../guides/meg-006-module-platform/13-platform-guidelines.md)
- [MAC-001 — Platform Architecture](../mac-001-platform-architecture/03-capability-model.md)
- [MEG-004 — Hexagonal Architecture](../../guides/meg-004-hexagonal-architecture/04-driven-ports.md)
- [MIP-005 — Module Adapter Contract Protocol](../../protocols/mip-005-module-adapter-contract-protocol/index.md)
