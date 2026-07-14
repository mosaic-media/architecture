<!--
File: docs/design/system/mds-001-design-token-architecture/references.md
Document: MDS-001
Title: References
Status: Draft
Version: 0.1
-->

# References

---

# Purpose

This document records the architectural influences, design theories and implementation concepts that informed **MDS-001 — Design Token Architecture**.

Unlike implementation documentation, these references exist to explain the architectural reasoning behind the Design Token Architecture rather than prescribe implementation details.

The Mosaic Design System intentionally synthesises established Design System practices with the adaptive, runtime-first philosophy established throughout the MDL specifications.

---

# Reading Order

Contributors should approach references in the following order.

1. MDL Specifications
2. Design Token Architecture
3. Design Systems
4. Runtime Design
5. Cross-Platform Architecture
6. Implementation Specifications

The Mosaic Design Language remains the authoritative source.

External references provide context rather than authority.

---

# Internal References

## MDL-001 — Vision

Provides:

- Product philosophy
- Immersion
- Companion model
- Long-term product identity

Every token should ultimately reinforce the experience defined by the Vision.

---

## MDL-002 — Principles

Provides:

- Design intent
- Behavioural priorities
- Design governance

Semantic Tokens should communicate these principles through implementation.

---

## MDL-003 — Mental Model

Provides:

- World
- Focus
- Context
- Information
- Relationships

Runtime Tokens are intentionally designed to adapt these concepts rather than replace them.

---

## MDL-004 — Interaction Model

Provides:

- Behaviour
- Continuity
- Adaptive evolution
- Interaction States

Runtime Tokens should reinforce behavioural consistency rather than introduce alternative interaction models.

---

## MDL-005 — Composition Model

Provides:

- Hero
- Hierarchy
- Priority
- Density
- Composition

Composition Tokens are the implementation of these conceptual ideas.

---

# Future Specifications

The following specifications depend directly upon MDS-001.

- MDS-002 Colour System
- MDS-003 Material System
- MDS-004 Typography
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-007 Tile Framework
- MDS-008 Component Library

These specifications should consume the architecture defined here rather than redefining it.

---

# Design Tokens

The architecture of MDS-001 draws inspiration from modern token systems that distinguish between:

- physical values
- semantic meaning
- implementation

Mosaic extends this approach by introducing:

- Composition Tokens
- Runtime Tokens

allowing the Design System to adapt continuously while preserving semantic stability.

---

# Runtime Design

Unlike traditional Design Systems, Mosaic assumes that:

- artwork changes
- Context changes
- Focus changes
- accessibility changes
- device capabilities change

The Design Token Architecture therefore treats runtime adaptation as a first-class architectural concern rather than an implementation detail.

---

# Cross-Platform Design

MDS intentionally separates:

```
Meaning

↓

Runtime

↓

Platform

↓

Rendering
```

This separation allows identical Design Tokens to generate implementations for:

- Web
- Flutter
- SwiftUI
- Jetpack Compose
- Future clients

without changing the architecture.

---

# Design Systems

The organisation of the Mosaic Design System was influenced by mature Design Systems that distinguish:

- Foundations
- Tokens
- Components
- Patterns
- Guidelines

Mosaic intentionally extends this model through:

- runtime adaptation
- composition solving
- artwork-driven atmosphere
- semantic hierarchy

These concepts distinguish Mosaic from traditional static Design Systems.

---

# Software Architecture

Several software architecture concepts influenced MDS-001.

Examples include:

- Separation of Concerns
- Layered Architecture
- Domain-Driven Design
- Documentation as Code
- Architecture Decision Records
- Platform Abstraction

These concepts informed documentation organisation rather than implementation technology.

---

# Mosaic-Specific Influences

The Design Token Architecture emerged directly from the preceding MDL specifications.

Key architectural discoveries include:

- Meaning should precede implementation.
- Components should consume intent rather than values.
- Runtime should adapt implementation rather than semantics.
- Composition should remain independent from presentation.
- Extensions should inherit the Design System rather than redefining it.

These ideas collectively define the Mosaic Design System.

---

# Relationship To The Runtime

Future runtime systems are expected to implement concepts such as:

- Atmosphere generation
- Adaptive materials
- Theme resolution
- Device adaptation
- Accessibility adaptation

MDS-001 intentionally defines the architectural boundaries within which those systems operate.

Implementation details belong to future specifications.

---

# Normative References

Required reading before contributing to MDS-001.

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model

These documents collectively define the conceptual foundation upon which the Design Token Architecture is built.

---

# Informative References

Future contributors may also wish to review:

- MDS-002 Colour System
- MDS-003 Material System
- MDS-006 Composition Engine
- MDS-008 Component Library

These specifications implement the token architecture defined within MDS-001.

---

# Living Document

This reference list should remain intentionally concise.

References should only be introduced when they materially influence:

- architectural layering
- runtime adaptation
- semantic modelling
- implementation boundaries

The purpose of this document is to preserve architectural reasoning rather than provide an exhaustive catalogue of design literature.

---

# Completion

This concludes **MDS-001 — Design Token Architecture**.

The next specification in the Mosaic Design System is:

> **MDS-002 — Colour System**

Where MDS-001 defines **how design intent becomes machine-readable**, MDS-002 defines **how colour communicates meaning**.

It formalises:

- the Mosaic brand palette
- semantic colour architecture
- adaptive atmosphere
- artwork-derived colour generation
- accessibility-aware colour resolution
- light and dark themes
- runtime colour synthesis

It is here that the distinctive visual identity of Mosaic begins to emerge from the architectural foundations established by the MDL and MDS specifications.
