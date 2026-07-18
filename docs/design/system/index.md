<!--
File: docs/design/system/index.md
Document: System
Status: Draft
-->

# System

Mosaic Design System specifications describe implementation-facing design primitives, runtime design infrastructure, and component behaviour.

## Design System in Brief

The Design System progressively transforms Design Language intent into rendered interface behaviour.

| Specification | In one sentence |
|---------------|-----------------|
| [MDS-001 — Design Token Architecture](mds-001-design-token-architecture/index.md) | Defines how design intent becomes machine-readable, semantic tokens. |
| [MDS-002 — Colour System](mds-002-colour-system/index.md) | Defines how colour communicates brand, meaning and runtime atmosphere. |
| [MDS-003 — Material System](mds-003-material-system/index.md) | Defines the visual materials through which Mosaic expresses depth and environment. |
| [MDS-004 — Typography System](mds-004-typography-system/index.md) | Defines typography as a consistent voice and information hierarchy. |
| [MDS-005 — Motion System](mds-005-motion-system/index.md) | Defines motion as the expression of behavioural continuity and change. |
| [MDS-008 — Component Library](mds-008-component-library/index.md) | Defines the v1 client-side Web component library and semantic SDUI rendering boundary. |

For Mosaic v1 implementation, read [MDS-001 — Design Token Architecture](mds-001-design-token-architecture/index.md) through [MDS-005 — Motion System](mds-005-motion-system/index.md) for Tokens, Colour, Materials, Typography and Motion, then use [MDS-008 — Component Library](mds-008-component-library/index.md) as the component and SDUI rendering authority.

The mathematical solver, adaptive Tile model and normalised spatial runtime are preserved outside the active Design System as the deferred [MDP-001 — Adaptive Composition Runtime](../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md).

For focused implementation work, start with the owning specification and follow its dependencies. The linked MDS specifications remain authoritative.
