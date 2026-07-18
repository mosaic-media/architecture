<!--
File: docs/engineering/architecture/mdp-002-tile-framework/glossary.md
Document: MDP-002
Status: Deferred
-->

# Glossary

---

# Purpose

This glossary defines the terms used by the deferred Tile model.

These definitions describe the proposal. Where a term is also used by an authoritative specification, that specification governs and is named in the entry.

---

# Tile

Within this proposal, a behavioural presentation primitive sitting between a solved Expression and a rendered Component. It carries identity and intent rather than implementation.

This is **not** the authoritative Mosaic definition. For Mosaic v1 a Tile is a governed Container Component, defined by [MDS-008 — Component Library](../../../design/system/mds-008-component-library/02-component-taxonomy.md).

---

# Tile Identity

The stable reference that allows a presented unit to survive layout, device and content change without being rebuilt.

---

# Tile Family

A classification grouping Tiles by behavioural purpose, such as Hero, Content, Timeline, Relationship, Action, Metadata, Collection, Navigation, Overlay and Utility.

---

# Expression Mapping

The proposed deterministic process converting a solved runtime Expression into a Tile identity.

---

# Tile Lifecycle

The proposed progression of a Tile through resolution, materialisation, activity, evolution, retirement and release.

---

# Tile Orchestration

The proposed coordination of every live Tile following a single behavioural change.

---

# Module Tile

A Tile produced from a Module-provided Expression, resolved through the same pipeline as a native one.

---

# Capacity-Sensitive Tile Viewport

The proposed model in which a Tile presents a whole number of items derived from available space rather than from a device category. The governing equation and its calibration caveat are preserved in [05 — Adaptive Tiles](05-adaptive-tiles.md).

---

# Expression

A behavioural statement produced by the runtime and consumed by presentation. Defined for this proposal by [MDP-001 — Adaptive Composition Runtime](../mdp-001-adaptive-composition-runtime/04-expression-resolution.md), and in the Design Language by [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/08-expressions.md).

---

# Component

The concrete rendering primitive that implements a resolved Tile. Owned by [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md).
