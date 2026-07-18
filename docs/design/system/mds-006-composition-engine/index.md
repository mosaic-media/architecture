<!--
File: docs/design/system/mds-006-composition-engine/index.md
Document: MDS-006
Status: Superseded
-->

# MDS-006 — Composition Engine

> **Superseded.** This identifier no longer carries a specification. Its content moved, and this record exists so the identifier still resolves to an explanation rather than to nothing.

---

# Where This Content Went

MDS-006 — Composition Engine was an active Mosaic Design System specification. It was withdrawn from the Design System and its material split two ways.

| If you want | Read | Authority |
|-------------|------|-----------|
| The behaviour Mosaic implements today | [MDS-008 — Component Library](../mds-008-component-library/index.md) | Authoritative for v1 |
| The deferred research this specification contained | [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) | Non-authoritative, unscheduled |

Most readers want [MDS-008](../mds-008-component-library/index.md).

---

# Why

Mosaic v1 ships a client-side component library driven by semantic SDUI. The mathematical adaptive runtime this specification described requires calibration against real interfaces and was not made a v1 dependency.

The decisions are recorded in [MDS-008](../mds-008-component-library/index.md) and accepted:

- [ADR-204 — Ship Mosaic v1 As A Client-Side Component Library Driven By Semantic SDUI](../mds-008-component-library/12-adrs.md)
- [ADR-205 — Defer The Adaptive Composition Runtime Until After Mosaic v1](../mds-008-component-library/12-adrs.md)

---

# Identifier Status

The MDS-006 identifier is retired and will not be reused. Reissuing it would make existing references ambiguous.

Per [MDG-001 — Documentation Authority Guide](../../../engineering/documentation/mdg-001-documentation-authority-guide/08-document-lifecycle.md), a replaced document is not deleted: its status becomes Superseded, it names its replacement, and it stays available so the historical trail survives.
