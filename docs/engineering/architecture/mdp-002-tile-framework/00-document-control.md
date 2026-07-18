<!--
File: docs/engineering/architecture/mdp-002-tile-framework/00-document-control.md
Document: MDP-002
Status: Deferred
-->

# Document Control

> **Proposal status: Deferred and non-authoritative.** This specification preserves post-v1 research. It is not a Mosaic v1 requirement.

---

# Document Information

| Property | Value |
|----------|-------|
| Document | MDP-002 |
| Title | Tile Framework |
| Classification | Mosaic Design Proposal |
| Status | Deferred |
| Owner | AdamNi-7080 |
| Delivery Target | Unscheduled post-v1 research |

---

# Authority Boundary

MDP-002 proposes a behavioural Tile model. It does not define one.

Nothing in this document establishes an implementation requirement. The authoritative v1 definition of a Tile is a governed Container Component, owned by [MDS-008 — Component Library](../../../design/system/mds-008-component-library/02-component-taxonomy.md).

Per [MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/02-document-types.md), a proposal must not become permanent reference documentation. The material here is retained as research provenance rather than as a specification to build against.

---

# Provenance

This document was previously published as [MDS-007 — Tile Framework](../../../design/system/mds-007-tile-framework/index.md), an active Mosaic Design System specification.

It was deferred and folded into [MDP-001 — Adaptive Composition Runtime](../mdp-001-adaptive-composition-runtime/index.md), then separated into its own proposal so that the Tile model and the Composition Engine can be reviewed and reactivated independently.

The [MDS-007](../../../design/system/mds-007-tile-framework/index.md) identifier is retired and carries a Superseded record at [MDS-007](../../../design/system/mds-007-tile-framework/index.md).

---

# Governing Decisions

The deferral is governed by decisions recorded in [MDS-008](../../../design/system/mds-008-component-library/index.md) and accepted there:

| Decision | Effect |
|----------|--------|
| [ADR-204](../../../design/system/mds-008-component-library/12-adrs.md) | Mosaic v1 ships as a client-side component library driven by semantic SDUI. |
| [ADR-205](../../../design/system/mds-008-component-library/12-adrs.md) | The Adaptive Composition Runtime is deferred until after Mosaic v1. |

Chapter 12 preserves the earlier decision history from the [MDS-007](../../../design/system/mds-007-tile-framework/index.md) review. Those records describe the state of that earlier draft and do not make this proposal authoritative.

---

# Reactivation

This proposal returns to review only when evidence from production v1 interfaces justifies it. Reactivation is an architectural decision, not an editorial one, and requires a new decision record rather than an edit to this document.
