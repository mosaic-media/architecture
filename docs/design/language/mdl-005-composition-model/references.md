<!--
File: docs/design/language/mdl-005-composition-model/references.md
Document: MDL-005
Title: References
Status: Draft
Version: 0.4
-->

# References

---

# Purpose

This document records the architectural influences, design philosophies and conceptual references that informed **MDL-005 — Composition Model**.

Unlike implementation documentation, these references explain *why* the Composition Model exists rather than *how* it should be implemented.

MDL intentionally draws inspiration from multiple disciplines.

The resulting Composition Model is unique to Mosaic.

---

# Reading Order

Contributors should approach references in the following order.

1. MDL Specifications
2. Information Architecture
3. Human Perception
4. Interaction Design
5. Systems Architecture
6. Implementation Specifications

The Mosaic Design Language always remains the authoritative source.

---

# Internal References

## [MDL-001 — Mosaic Design Language Vision](../mdl-001-vision/index.md)

Provides:

- Product vision
- Immersion
- Companion philosophy
- Long-term product objectives

Every Composition should reinforce the experience described within [MDL-001](../mdl-001-vision/index.md).

---

## [MDL-002 — Principles](../mdl-002-principles/index.md)

Provides:

- Context Before Prediction
- Content Leads
- Every Feature Earns Its Place
- Be A Companion

The Composition Model should be viewed as the practical application of these principles.

---

## [MDL-003 — Mental Model](../mdl-003-mental-model/index.md)

Provides:

- World
- Focus
- Context
- Information
- Relationships
- Expressions

MDL-005 organises these concepts.

It does not redefine them.

---

## [MDL-004 — Interaction Model](../mdl-004-interaction-model/index.md)

Provides:

- Continuity
- Behaviour
- Focus Transitions
- Context Evolution
- Movement

MDL-005 determines how these behavioural changes become understandable compositions.

---

# Future Specifications

The following specifications directly depend upon MDL-005.

- [MDS-001 — Design Token Architecture](../../system/mds-001-design-token-architecture/index.md)
- [MDS-003 — Material System](../../system/mds-003-material-system/index.md)
- [MDS-006 — Composition Engine](../../system/mds-006-composition-engine/index.md)
- [MDS-002 — Colour System](../../system/mds-002-colour-system/index.md)
- [MDS-007 — Tile Framework](../../system/mds-007-tile-framework/index.md)
- [MDS-008 — Component Library](../../system/mds-008-component-library/index.md)

These specifications should implement the Composition Model rather than reinterpret it.

---

# Information Architecture

The Composition Model draws heavily from the discipline of Information Architecture.

Primary influences include:

- understanding before interface
- hierarchy before layout
- conceptual grouping
- progressive disclosure
- information scent

Mosaic intentionally extends these ideas into a runtime composition system capable of continuously reorganising understanding.

---

# Human Perception

Several principles of human perception influenced the Composition Model.

Examples include:

- visual hierarchy
- progressive attention
- chunking
- spatial memory
- cognitive load reduction

These concepts influenced compositional thinking rather than visual styling.

---

# Editorial Design

Editorial design significantly influenced the Composition Model.

Editors continually decide:

- what deserves attention
- what supports understanding
- what should wait

Composition performs the same role.

Instead of organising articles...

It organises understanding.

This editorial mindset differentiates Mosaic from grid-based dashboard systems.

---

# Systems Thinking

The Composition Model intentionally adopts systems thinking.

Examples include:

- Hero emerging from Priority
- Hierarchy emerging from Relationships
- Density emerging from Context
- Expressions emerging from Composition

Nothing should exist in isolation.

Every compositional decision should emerge naturally from the concepts preceding it.

---

# Design Systems

The organisation of MDL-005 was informed by mature design systems that distinguish:

- conceptual hierarchy
- interaction
- implementation
- presentation

rather than treating layout as the primary architectural concern.

Mosaic intentionally extends this approach by introducing runtime composition.

---

# Software Architecture

Although MDL intentionally avoids implementation details, several architectural concepts influenced the Composition Model.

Examples include:

- Separation of Concerns
- Information-Driven Architecture
- Constraint Solving
- Event-Driven Systems
- Domain-Driven Design
- Documentation as Code

These concepts influenced documentation structure.

They do not prescribe implementation.

---

# Mosaic-Specific Influences

The Composition Model emerged directly from founder workshops.

Significant discoveries included:

- the World as the primary conceptual object
- Hero emerging from Priority
- Information before interface
- Relationships before navigation
- Expressions before presentation
- Composition solving rather than authored layouts
- Modules contributing understanding rather than interface

These discoveries collectively distinguish Mosaic from conventional media platforms.

---

# Relationship To The Platform

The broader Mosaic platform architecture introduces concepts such as:

- GraphQL
- Modules
- Runtime composition
- Adaptive presentation
- Information graphs

The Composition Model intentionally remains implementation independent while providing the conceptual framework that those systems should implement.

---

# Normative References

Required reading before contributing to MDL-005.

- [MDL-001 — Mosaic Design Language Vision](../mdl-001-vision/index.md)
- [MDL-002 — Principles](../mdl-002-principles/index.md)
- [MDL-003 — Mental Model](../mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../mdl-004-interaction-model/index.md)

---

# Informative References

Future contributors may also wish to review:

- [MDS-006 — Composition Engine](../../system/mds-006-composition-engine/index.md)
- [MDS-007 — Tile Framework](../../system/mds-007-tile-framework/index.md)
- [MDS-008 — Component Library](../../system/mds-008-component-library/index.md)
- [MDS-005 — Motion System](../../system/mds-005-motion-system/index.md)

These documents describe how the conceptual Composition Model becomes runtime behaviour.

---

# Living Document

This reference list should remain intentionally concise.

References should only be introduced when they materially influence:

- compositional architecture
- hierarchy
- behavioural organisation
- conceptual understanding

The purpose of this document is to preserve architectural context rather than become an exhaustive bibliography.

---

# Completion

This concludes **MDL-005 — Composition Model**.

With the completion of MDL-005, the conceptual layer of the Mosaic Design Language is now established.

The next specification begins the transition from philosophy into implementation:

> **[MDS-001 — Design Token Architecture](../../system/mds-001-design-token-architecture/index.md)**

From this point onwards the documentation shifts from answering:

- Why?
- How should we think?
- How should the platform behave?

to answering:

- How should these concepts be implemented?
- How should the runtime consume them?
- How should every Mosaic client express them consistently?

The remaining MDS specifications build directly upon the five MDL specifications and collectively form the implementation blueprint for the Mosaic platform.
