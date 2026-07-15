<!--
File: docs/design/system/mds-001-design-token-architecture/05-composition-inputs.md
Document: MDS-001
Chapter: 05
Title: Composition Inputs
Status: Draft
Version: 0.1
-->

# Composition Inputs

---

# Purpose

Composition determines the current role, hierarchy and spatial relationship of information.

Those decisions influence token resolution but are not Design Tokens.

---

# Authority

[MDS-006 — Composition Engine](../mds-006-composition-engine/index.md) owns Composition roles such as Hero, Anchor, Supporting, Peripheral, Overlay and Navigation.

MDS-001 owns only how those roles may influence token resolution.

This separation prevents a temporary role from becoming a permanent token namespace.

---

# Composition Resolution Input

For each resolved subject, the Composition Engine may supply:

| Input | Meaning |
|-------|---------|
| Role | Current hierarchical responsibility. |
| Priority | Relative preservation and emphasis order. |
| Relationships | Parent, peer, Focus and supporting relationships. |
| Constraints | Available extent and governed layout limits. |
| State | Entering, stable, leaving or displaced Composition state. |

The resolver uses this information to select an appropriate implementation of existing Semantic Tokens.

It must not mint tokens such as `Composition.Hero` or `Tile.Hero` dynamically.

---

# Role Does Not Equal Appearance

Hero describes importance rather than a fixed colour, size or Material.

The same Hero role may resolve differently for playback, reading, reduced motion or constrained rendering while remaining semantically dominant.

Composition therefore supplies context to the resolver.

It does not prescribe physical values.

---

# Domain Layout Extensions

Modules may extend the Composition vocabulary when the Platform does not provide a required domain layout, such as:

- calendar month view
- tournament bracket
- programme guide
- spatial media timeline

A Module-defined layout should provide:

1. domain invariants
2. valid presentation modes
3. adaptation permissions
4. priority and Focus rules
5. overflow behaviour

The Composition Engine selects and sizes the resulting Tiles.

The Module must not hard-code renderer geometry, Material physics or token values.

---

# Adaptive Selection

When a Module provides several valid presentation modes, the Composition Engine may select among them using:

- available space
- content volume
- current Focus
- accessibility requirements
- interaction context
- measured client capability and budget

Selection must preserve declared domain invariants.

It must not be based permanently on mobile, television, desktop or another device category.

---

# Component Boundary

Components receive resolved Composition and token state.

They do not decide whether they are Hero, Supporting or Peripheral and do not create component-specific token hierarchies.

Their responsibility is faithful rendering.

---

# Layout Consumption Modes

Mosaic supports two client layout modes that consume the same Design System.

| Mode | Responsibility |
|------|----------------|
| Adaptive Composition | The client mathematically resolves media-driven geometry from Composition, Focus, artwork, content and current constraints. |
| Authored Layout | Documentation, administration, dashboards and conventional application pages use CSS or native layout with public Semantic Tokens. |

Adaptive Composition remains the default for media experiences.

Authored Layout allows a Design System consumer to construct conventional structure without inventing spacing, typography, sizing or Material values.

The modes may coexist within one client.

For example, a mathematically composed media Hero may sit above an authored administration region.

---

# Geometry And Density

Composition owns the semantic constraints from which concrete Tile geometry is derived.

In Adaptive Composition, the client-side Adaptive Layout implementation calculates final location, size, padding, spacing and density using those constraints and private Platform primitives.

Modules provide content relationships, semantic priority, domain invariants and valid presentation modes.

They do not request final coordinates, Material radii or arbitrary Primitive values.

In Authored Layout, consumers may select public semantic relationships such as `Space.Group`, `Type.Body` and `Size.ReadingMeasure`.

The resolver maps those meanings to renderer-native values while retaining accessibility and capability adaptation.

Typography and accessibility provide readability and interaction constraints, while the client design runtime remains responsible for the final solution.

---

# Summary

Composition is a governed runtime input to token resolution.

It may reorganise importance and layout without extending or mutating the Design Token hierarchy.
