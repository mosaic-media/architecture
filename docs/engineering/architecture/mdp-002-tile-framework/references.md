<!--
File: docs/engineering/architecture/mdp-002-tile-framework/references.md
Document: MDP-002
Status: Deferred
-->

# References

---

# Purpose

This chapter identifies the documents that govern, bound or complement the research preserved by MDP-002.

Because this proposal is non-authoritative, the references below matter in one direction: they tell a reader which document to trust instead of this one.

---

# Authoritative Documents

These specifications own material that MDP-002 discusses but does not define.

| Document | Owns |
|----------|------|
| [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md) | The v1 Tile as a governed Container Component, and the SDUI rendering boundary. |
| [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md) | Composition intent, hierarchy, priority, density and breathing space. |
| [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/index.md) | Expressions and presentation within the user's mental model. |
| [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md) | Materials and Acrylic assembly. |
| [MDS-005 — Motion System](../../../design/system/mds-005-motion-system/index.md) | Motion tokens and governed transitions. |
| [MAC-001 — Platform Architecture](../mac-001-platform-architecture/index.md) | Runtime ownership and the Platform boundary. |

---

# Related Proposals

- [MDP-001 — Adaptive Composition Runtime](../mdp-001-adaptive-composition-runtime/index.md) preserves the Composition Engine, solver and layout mathematics that this Tile model was designed to sit above. The two proposals were reviewed together and deferred together.

---

# Governing Decisions

- [ADR-204 and ADR-205](../../../design/system/mds-008-component-library/12-adrs.md), recorded in [MDS-008](../../../design/system/mds-008-component-library/index.md), establish the v1 component architecture and the deferral of the adaptive runtime.

---

# Superseded Identifier

- [MDS-007 — Tile Framework](../../../design/system/mds-007-tile-framework/index.md) is the retired Design System identifier this material was published under. It carries a Superseded record pointing here and to [MDS-008](../../../design/system/mds-008-component-library/index.md).

---

# Reference Maintenance

If this proposal returns to review, these references should be revisited first. A deferred proposal decays through its dependencies rather than through its own text: the documents above continue to evolve while this one does not.
