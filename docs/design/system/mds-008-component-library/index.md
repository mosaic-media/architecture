<!--
File: docs/design/system/mds-008-component-library/index.md
Document: MDS-008
Status: Draft
-->

# MDS-008 — Component Library

> *Components do not decide. They faithfully render the decisions already made.*

---

# Purpose

Every previous specification has progressively transformed behavioural understanding into presentation.

The MDL established:

- Vision
- Principles
- Mental Model
- Interaction
- Composition

The MDS established:

- Design Tokens
- Colour
- Materials
- Typography
- Motion

MDS-008 defines the final architectural layer.

For Mosaic v1, it is also the primary Presentation implementation authority. The first release ships a client-side Web component library driven either by authored semantic HTML or by Platform SDUI.

The Component Library is responsible for physically implementing governed Mosaic presentation.

In v1, its client resolver consumes authored semantic HTML or Platform SDUI structure and content. It resolves those inputs into governed components, including Tile structural components.

In a later release, the deferred [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md) may supply adaptive placement decisions without changing the component contract.

Unlike traditional UI frameworks, Components possess almost no behavioural responsibility.

By the time a Component is created:

- Behaviour has been solved.
- Hierarchy has been solved.
- Materials have been solved.
- Typography has been solved.
- Motion has been solved.
- Interaction has been solved.
- Structural component intent has been resolved.

Components simply render.

---

# Relationship to Previous Specifications

```mermaid
flowchart TD

N1["Vision"]
N2["Principles"]
N3["Mental Model"]
N4["Interaction"]
N5["Composition"]
N6["Tokens"]
N7["Colour"]
N8["Materials"]
N9["Typography"]
N10["Motion"]
N11["Semantic Structure"]
N12["Component Library"]
N13["Rendering"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
N8 --> N9
N9 --> N10
N10 --> N11
N11 --> N12
N12 --> N13
```

The Component Library consumes:

- Semantic SDUI structure and content
- Authored semantic HTML
- Resolved semantic component intents
- Material Profiles
- Typography Profiles
- Motion Profiles
- Interaction Profiles

It produces:

- Platform Components
- Render Trees
- Accessible UI
- Client-specific renderers

---

# Scope

This specification defines:

- Component Philosophy
- Component Taxonomy
- Component Contracts
- Component Lifecycle
- Component Composition
- Tile Structural Components
- Rendering Architecture
- Client Renderers
- Runtime SDUI
- Mosaic v1 Web Component Library
- SDUI Structural Component Vocabulary
- Optional HTMX Web Adapter
- Refreshable Compiled SDUI
- SDUI Patch Stream
- Continuity Keys
- Recovery SDUI
- Platform Components
- Accessibility Contracts
- Runtime Rendering
- Component Optimisation

This specification intentionally does **not** define:

- Behaviour
- Hierarchy
- Runtime World
- Expressions
- Design Tokens

Adaptive Tile solving is deferred to [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md).

The Design Language and semantic structure already establish the problem to render.

The Component Library simply implements their decisions.

---

# Guiding Question

MDS-008 exists to answer one question.

> **How should semantic structure become concrete Mosaic interface implementations?**

Not:

> How should the application behave?

For recovery and onboarding states, this specification also defines how clients render the deliberately smaller Recovery SDUI vocabulary emitted by the Supervisor.

---

# Component Statement

Within Mosaic:

> **Components render. They never reason.**

This is the single most important architectural principle of the Component Library.

---

# Component Responsibilities

The Component Library separates implementation into several conceptual layers.

```mermaid
flowchart TD

N1["Resolved Tile"]
N2["Component Contract"]
N3["Platform Component"]
N4["Rendering"]
N5["Pixels"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Each layer contributes exactly one responsibility.

---

# Expected Outcome

After reading MDS-008 contributors should understand:

- why Components intentionally remain simple,
- how Component Contracts work,
- how Components remain platform independent,
- how rendering stays replaceable,
- how accessibility integrates,
- how runtime presentation becomes visible,
- how Recovery SDUI becomes safe diagnostic presentation,

without redefining behaviour or runtime architecture.

---

# Repository Structure

```text
design/

└── mds/

    └── MDS-008 Component Library/

        README.md

        00-document-control.md

        01-component-philosophy.md

        02-component-taxonomy.md

        03-component-contracts.md

        04-component-lifecycle.md

        05-component-composition.md

        06-rendering-architecture.md

        07-platform-components.md

        08-accessibility-contracts.md

        09-runtime-rendering.md

        10-component-optimisation.md

        11-governance.md

        12-adrs.md

        13-contributor-guidance.md

        references.md

        glossary.md
```

---

# Dependencies

Required reading:

- [MDL-001](../../language/mdl-001-vision/index.md) → [MDL-005](../../language/mdl-005-composition-model/index.md)
- [MDS-001 — Design Token Architecture](../mds-001-design-token-architecture/index.md) through [MDS-005 — Motion System](../mds-005-motion-system/index.md)

Downstream specifications:

There are currently no downstream Design System specifications.

Platform implementation guides may build upon this specification.
