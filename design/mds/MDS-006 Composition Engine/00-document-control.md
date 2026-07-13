<!--
File: design/mds/MDS-006 Composition Engine/00-document-control.md
Document: MDS-006
Title: Composition Engine
Status: Draft
Version: 0.1
-->

# Document Control

---

# Document Information

| Property | Value |
|----------|-------|
| Document ID | MDS-006 |
| Title | Mosaic Design System — Composition Engine |
| Classification | Internal |
| Status | Draft |
| Version | 0.1 |
| Owner | Lead Runtime Architecture Team |
| Parent Specifications | MDL-001 → MDL-005, MDS-001 → MDS-005 |
| Repository | `/design/mds/MDS-006 Composition Engine/` |

---

# Purpose

MDS-006 defines the runtime architecture responsible for constructing the user's World.

Every previous specification described:

- what the platform believes,
- how it behaves,
- how it communicates.

The Composition Engine is responsible for turning those architectural concepts into a living experience.

Unlike conventional UI frameworks, which render predefined interface trees, the Composition Engine continuously solves:

- behavioural intent,
- hierarchy,
- expressions,
- presentation,

before a single component is rendered.

The Composition Engine is therefore the runtime embodiment of the Mosaic Design Language.

---

# Authority

MDS-006 governs:

- Runtime World construction
- Composition Solver implementation
- Expression Resolution
- Runtime Hierarchy
- Behaviour Orchestration
- Adaptive Layout Resolution
- Composition Pipelines
- Runtime Caching
- Multi-device Composition

This specification intentionally does **not** govern:

- rendering frameworks,
- GraphQL schemas,
- storage,
- transport,
- platform widgets.

Those systems provide capabilities.

The Composition Engine creates experience.

---

# Relationship To MDS

The Composition Engine consumes every conceptual system defined before it.

```mermaid
flowchart TD

Vision
Vision --> Principles
Principles --> MentalModel
MentalModel --> Interaction
Interaction --> Composition
Composition --> Tokens
Tokens --> Colour
Colour --> Materials
Materials --> Typography
Typography --> Motion
Motion --> CompositionEngine
CompositionEngine --> Presentation
```

Everything before the Composition Engine defines intent.

Everything after it implements presentation.

---

# Design Intent

Traditional applications typically follow:

```text
Data

↓

Screen

↓

Render
```

Mosaic intentionally follows:

```text
World

↓

Behaviour

↓

Composition

↓

Expressions

↓

Presentation

↓

Render
```

The distinction is fundamental.

Applications render components.

Mosaic constructs understanding.

---

# Reader Expectations

Before reading this specification contributors should already understand:

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

The Composition Engine assumes every conceptual decision has already been made.

Its responsibility is runtime orchestration.

---

# Architectural Scope

The Composition Engine defines:

- runtime solving
- behavioural orchestration
- expression selection
- hierarchy resolution
- adaptive composition
- presentation modelling

It intentionally avoids implementation technologies such as:

- Flutter Widgets
- React Components
- SwiftUI Views
- Compose Composables

These become consumers of the Presentation Model produced by the engine.

---

# Stability

Expected lifetime.

| Artefact | Expected Lifetime |
|----------|-------------------|
| UI Components | Months |
| Rendering Backends | Months |
| Runtime Optimisations | Years |
| Composition Engine Architecture | Years |
| Runtime Philosophy | Decades |

The engine implementation may evolve continuously.

Its conceptual model should remain remarkably stable.

---

# Success Criteria

MDS-006 succeeds when:

- every client constructs identical understanding
- behaviour consistently produces identical composition
- adaptive layouts preserve the user's World
- extensions integrate naturally
- rendering frameworks remain replaceable
- contributors think in runtime worlds rather than interface trees

Users should never feel that screens are loading.

They should simply feel that their World continuously evolves around them.

---

# Review Status

**Status**

Draft

**Dependencies**

- MDL-001 → MDL-005
- MDS-001 → MDS-005

**Supersedes**

None.

**Next File**

`01-composition-engine-philosophy.md`
