<!--
File: design/mds/MDS-006 Composition Engine/references.md
Document: MDS-006
Title: References
Status: Draft
Version: 0.1
-->

# References

---

# Purpose

This document records the architectural influences and conceptual foundations that informed **MDS-006 — Composition Engine**.

Unlike implementation documentation, these references explain *why* the Composition Engine exists rather than prescribing specific runtime technologies.

The Composition Engine intentionally combines ideas from:

- behavioural architecture,
- runtime systems,
- graph modelling,
- information architecture,
- reactive systems,
- deterministic execution,

into one coherent runtime capable of continuously constructing the user's World.

---

# Reading Order

Contributors should approach references in the following order.

1. MDL Specifications
2. Design Token Architecture
3. Colour System
4. Material System
5. Typography System
6. Motion System
7. Composition Engine
8. Platform Runtime

The Mosaic Design Language remains the primary architectural authority.

External implementation technologies exist only to realise this model.

---

# Internal References

## MDL-001 — Vision

Provides:

- Companion philosophy
- Entertainment-first thinking
- Long-term product identity

The Composition Engine exists to continuously express the Companion rather than render isolated interfaces.

---

## MDL-002 — Principles

Provides:

- Behaviour Before Interface
- Context Before Prediction
- Calm Interfaces
- Every Feature Earns Its Place

The Composition Engine continuously applies these principles at runtime.

---

## MDL-003 — Mental Model

Provides:

- World
- Focus
- Context
- Relationships
- Information

The Runtime World is the implementation of the Mental Model.

Everything within the Composition Engine begins here.

---

## MDL-004 — Interaction Model

Provides:

- Behaviour
- Continuity
- Runtime evolution
- Interaction flow

Behaviour becomes the primary trigger for every runtime pipeline.

The Composition Engine never initiates behaviour.

It responds to it.

---

## MDL-005 — Composition Model

Provides:

- Hero
- Hierarchy
- Priority
- Density
- Anchors
- Expressions

The Composition Solver is the runtime implementation of the Composition Model.

---

## MDS-001 — Design Token Architecture

Provides:

- Runtime Resolution
- Semantic hierarchy
- Deterministic pipelines

The Composition Engine produces Presentation Models consumed by downstream Design System specifications.

---

## MDS-002 — Colour System

Provides:

- Runtime Atmosphere
- Adaptive colour
- Semantic colour

The Composition Engine determines where Runtime Atmosphere should be expressed.

The Colour System determines how.

---

## MDS-003 — Material System

Provides:

- Material Hierarchy
- Refraction
- Runtime Material Resolution

The Composition Engine assigns Material Intent.

The Material System resolves physical behaviour.

---

## MDS-004 — Typography System

Provides:

- Editorial Hierarchy
- Runtime Typography
- Reading Rhythm

Expressions communicate editorial intent.

Typography communicates it to the user.

---

## MDS-005 — Motion System

Provides:

- Behavioural Motion
- Runtime Motion Resolution
- Behaviour Orchestration

The Composition Engine supplies behavioural understanding.

The Motion System communicates its evolution.

---

# Future Specifications

The following specifications directly depend upon MDS-006.

- MDS-007 Tile Framework
- MDS-008 Component Library

These specifications implement presentation.

They never redefine runtime understanding.

---

# Runtime Architecture

The Composition Engine intentionally follows a runtime-first architecture.

Conceptually.

```text
Behaviour

↓

World

↓

Composition

↓

Presentation

↓

Rendering
```

Traditional interface frameworks often reverse this ordering.

Mosaic deliberately does not.

---

# Behavioural Systems

One of the strongest influences behind the Composition Engine is behavioural architecture.

Rather than modelling:

- pages,
- routes,
- layouts,

the runtime models:

- behaviour,
- understanding,
- continuity,
- relationships.

Presentation naturally emerges afterwards.

---

# Information Architecture

The Composition Engine treats information as the primary architectural resource.

Examples include:

- Hero
- Relationships
- Progress
- Context
- Behaviour

Information exists before interface.

The runtime simply determines how it should be understood.

---

# Deterministic Execution

The Composition Engine intentionally assumes deterministic execution.

Identical Runtime Worlds should always produce identical:

- Composition
- Expressions
- Presentation Models

This assumption enables:

- replay,
- testing,
- caching,
- synchronisation,
- platform independence.

---

# Runtime Graphs

Future implementations may internally represent the Runtime World using graph-based models.

The graph itself is intentionally **not** part of the architectural contract.

The architectural contract remains:

```text
Runtime World

↓

Composition Solver

↓

Expressions

↓

Presentation
```

Graph technology is replaceable.

Behaviour is not.

---

# Reactive Systems

The Composition Engine intentionally behaves as a reactive runtime.

Behaviour changes.

↓

Runtime World updates.

↓

Composition evolves.

↓

Presentation evolves.

This differs significantly from request-driven interface architectures.

---

# Platform Independence

The Composition Engine intentionally separates:

```text
Behaviour

↓

Composition

↓

Presentation

↓

Rendering
```

Every client therefore shares identical behavioural understanding while remaining free to implement presentation using:

- Flutter
- React
- SwiftUI
- Compose
- Future runtime technologies

without altering the architecture.

---

# Mosaic-Specific Influences

The Composition Engine emerged directly from founder exploration.

Major architectural discoveries included:

- Interfaces should be solved rather than authored.
- Behaviour should own hierarchy.
- Expressions should separate understanding from components.
- Runtime should model Worlds rather than screens.
- Presentation should remain an implementation detail.

These discoveries collectively define the architectural identity of Mosaic.

---

# Relationship To The Companion

The Composition Engine represents the reasoning layer of the Companion.

Conceptually.

```text
World

↓

Behaviour

↓

Understanding

↓

Composition

↓

Presentation

↓

User
```

The Companion understands first.

The interface communicates second.

That ordering should remain fundamental throughout the lifetime of Mosaic.

---

# Normative References

Required reading before contributing to MDS-006.

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model
- MDS-001 Design Token Architecture
- MDS-002 Colour System
- MDS-003 Material System
- MDS-004 Typography System
- MDS-005 Motion System

Together these specifications define the conceptual foundation of the Composition Engine.

---

# Informative References

Future contributors may also wish to review:

- MDS-007 Tile Framework
- MDS-008 Component Library

These specifications describe how Expressions become reusable presentation primitives while preserving the runtime architecture established here.

---

# Living Document

This reference list should remain intentionally concise.

References should only be introduced when they materially influence:

- runtime behaviour,
- behavioural architecture,
- composition solving,
- implementation boundaries.

The objective is to preserve architectural reasoning rather than catalogue runtime technologies.

---

# Completion

This concludes **MDS-006 — Composition Engine**.

The next specification in the Mosaic Design System is:

> **MDS-007 — Tile Framework**

Where MDS-006 defines **how the user's World is solved**, MDS-007 defines **how that solved understanding becomes reusable presentation primitives**.

It formalises:

- Tile philosophy
- Expression-to-Tile mapping
- Tile lifecycle
- Adaptive Tile behaviour
- Tile composition
- Tile interaction
- Tile orchestration
- Runtime tile resolution
- Extension tile integration

The Tile Framework bridges the final gap between the runtime intelligence of the Composition Engine and the visual Component Library, allowing Mosaic to construct interfaces that remain adaptive, behavioural and entirely driven by understanding rather than static layouts.
