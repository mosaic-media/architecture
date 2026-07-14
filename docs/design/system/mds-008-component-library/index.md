<!--
File: docs/design/system/mds-008-component-library/index.md
Document: MDS-008
Status: Draft
Version: 0.1
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
- Composition Engine
- Tile Framework

MDS-008 defines the final architectural layer.

The Component Library is responsible for physically implementing the behavioural presentation described by resolved Tiles.

Unlike traditional UI frameworks, Components possess almost no behavioural responsibility.

By the time a Component is created:

- Behaviour has been solved.
- Hierarchy has been solved.
- Materials have been solved.
- Typography has been solved.
- Motion has been solved.
- Interaction has been solved.
- Tiles have been solved.

Components simply render.

---

# Relationship to Previous Specifications

```text
Vision

↓

Principles

↓

Mental Model

↓

Interaction

↓

Composition

↓

Tokens

↓

Colour

↓

Materials

↓

Typography

↓

Motion

↓

Composition Engine

↓

Tile Framework

↓

Component Library

↓

Rendering
```

The Component Library consumes:

- Resolved Tiles
- Material Profiles
- Typography Profiles
- Motion Profiles
- Interaction Profiles

It produces:

- Platform Components
- Render Trees
- Accessible UI

---

# Scope

This specification defines:

- Component Philosophy
- Component Taxonomy
- Component Contracts
- Component Lifecycle
- Component Composition
- Rendering Architecture
- Platform Components
- Accessibility Contracts
- Runtime Rendering
- Component Optimisation

This specification intentionally does **not** define:

- Behaviour
- Hierarchy
- Runtime World
- Expressions
- Tiles
- Design Tokens

Those systems already solved the problem.

The Component Library simply implements their decisions.

---

# Core Question

MDS-008 exists to answer one question.

> **How should resolved Tiles become concrete user interface implementations?**

Not:

> How should the application behave?

---

# Component Statement

Within Mosaic:

> **Components render. They never reason.**

This is the single most important architectural principle of the Component Library.

---

# Component Responsibilities

The Component Library separates implementation into several conceptual layers.

```text
Resolved Tile

↓

Component Contract

↓

Platform Component

↓

Rendering

↓

Pixels
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

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MDL-001 → MDL-005
- MDS-001 → MDS-007

Downstream specifications:

There are currently no downstream Design System specifications.

Platform implementation guides may build upon this specification.

---

# Review Status

**Status**

Draft

**Owner**

Lead UI Platform Architecture Team

**Next File**

`00-document-control.md`
