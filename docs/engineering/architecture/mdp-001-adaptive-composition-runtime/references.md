<!--
File: docs/engineering/architecture/mdp-001-adaptive-composition-runtime/references.md
Document: MDP-001
Status: Draft
-->

# References

---

# Purpose

This document records the architectural influences and conceptual foundations that informed **MDP-001 — Adaptive Composition Runtime**.

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

## [MDL-001 — Mosaic Design Language Vision](../../../design/language/mdl-001-vision/index.md)

Provides:

- Companion philosophy
- Entertainment-first thinking
- Long-term product identity

The Composition Engine exists to continuously express the Companion rather than render isolated interfaces.

---

## [MDL-002 — Principles](../../../design/language/mdl-002-principles/index.md)

Provides:

- Behaviour Before Interface
- Context Before Prediction
- Calm Interfaces
- Every Feature Earns Its Place

The Composition Engine continuously applies these principles at runtime.

---

## [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/index.md)

Provides:

- World
- Focus
- Context
- Relationships
- Information

The Runtime World is the implementation of the Mental Model.

Everything within the Composition Engine begins here.

---

## [MDL-004 — Interaction Model](../../../design/language/mdl-004-interaction-model/index.md)

Provides:

- Behaviour
- Continuity
- Runtime evolution
- Interaction flow

Behaviour becomes the primary trigger for every runtime pipeline.

The Composition Engine never initiates behaviour.

It responds to it.

---

## [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md)

Provides:

- Hero
- Hierarchy
- Priority
- Density
- Anchors
- Expressions

The Composition Solver is the runtime implementation of the Composition Model.

---

## [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/index.md)

Provides:

- Runtime Resolution
- Semantic hierarchy
- Deterministic pipelines

The Composition Engine produces Presentation Models consumed by downstream Design System specifications.

---

## [MDS-002 — Colour System](../../../design/system/mds-002-colour-system/index.md)

Provides:

- Runtime Atmosphere
- Adaptive colour
- Semantic colour

The Composition Engine determines where Runtime Atmosphere should be expressed.

The Colour System determines how.

---

## [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md)

Provides:

- Material Hierarchy
- Refraction
- Runtime Material Resolution

The Composition Engine assigns Material Intent.

The Material System resolves physical behaviour.

---

## [MDS-004 — Typography System](../../../design/system/mds-004-typography-system/index.md)

Provides:

- Editorial Hierarchy
- Runtime Typography
- Reading Rhythm

Expressions communicate editorial intent.

Typography communicates it to the user.

---

## [MDS-005 — Motion System](../../../design/system/mds-005-motion-system/index.md)

Provides:

- Behavioural Motion
- Runtime Motion Resolution
- Behaviour Orchestration

The Composition Engine supplies behavioural understanding.

The Motion System communicates its evolution.

---

# Future Specifications

The following specifications directly depend upon MDP-001.

- [MDP-001 — Adaptive Composition Runtime](14-adaptive-tile-model.md)
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)

These specifications implement presentation.

They never redefine runtime understanding.

---

# Runtime Architecture

The Composition Engine intentionally follows a runtime-first architecture.

Conceptually.

```mermaid
flowchart TD

N1["Behaviour"]
N2["World"]
N3["Composition"]
N4["Presentation"]
N5["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
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

```mermaid
flowchart TD

N1["Runtime World"]
N2["Composition Solver"]
N3["Expressions"]
N4["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
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

```mermaid
flowchart TD

N1["Behaviour"]
N2["Composition"]
N3["Presentation"]
N4["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
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

```mermaid
flowchart TD

N1["World"]
N2["Behaviour"]
N3["Understanding"]
N4["Composition"]
N5["Presentation"]
N6["User"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Companion understands first.

The interface communicates second.

That ordering should remain fundamental throughout the lifetime of Mosaic.

---

# Normative References

Required reading before contributing to MDP-001.

- [MDL-001 — Mosaic Design Language Vision](../../../design/language/mdl-001-vision/index.md)
- [MDL-002 — Principles](../../../design/language/mdl-002-principles/index.md)
- [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../../../design/language/mdl-004-interaction-model/index.md)
- [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md)
- [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/index.md)
- [MDS-002 — Colour System](../../../design/system/mds-002-colour-system/index.md)
- [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md)
- [MDS-004 — Typography System](../../../design/system/mds-004-typography-system/index.md)
- [MDS-005 — Motion System](../../../design/system/mds-005-motion-system/index.md)

Together these specifications define the conceptual foundation of the Composition Engine.

---

# Informative References

Future contributors may also wish to review:

- [MDP-001 — Adaptive Composition Runtime](14-adaptive-tile-model.md)
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)

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

This concludes **MDP-001 — Adaptive Composition Runtime**.

The next specification in the Mosaic Design System is:

> **[MDP-001 — Adaptive Composition Runtime](14-adaptive-tile-model.md)**

Within MDP-001, the [Adaptive Tile Model](14-adaptive-tile-model.md) proposes how solved understanding could become reusable presentation primitives.

It formalises:

- Tile philosophy
- Expression-to-Tile mapping
- Tile lifecycle
- Adaptive Tile behaviour
- Tile composition
- Tile interaction
- Tile orchestration
- Runtime tile resolution
- Module tile integration

The Tile Framework bridges the final gap between the runtime intelligence of the Composition Engine and the visual Component Library, allowing Mosaic to construct interfaces that remain adaptive, behavioural and entirely driven by understanding rather than static layouts.
