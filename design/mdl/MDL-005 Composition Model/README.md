<!--
File: design/mdl/MDL-005 Composition Model/README.md
Document: MDL-005
Status: Draft
Version: 0.1
-->

# MDL-005 — Composition Model

> *Interaction explains how the world changes. Composition explains how the world is understood.*

---

# Purpose

MDL-001 established **why** Mosaic exists.

MDL-002 established **how** decisions are made.

MDL-003 established **how Mosaic understands the user's world**.

MDL-004 established **how that world behaves**.

MDL-005 defines **how that world is organised into meaningful experiences**.

This specification introduces the Composition Model that transforms:

- World
- Focus
- Context
- Information
- Relationships

into coherent experiences that minimise cognitive effort.

Unlike traditional layout systems, Composition is not concerned with pixels.

It is concerned with meaning.

---

# Relationship to Previous Specifications

```
Vision

↓

Principles

↓

Mental Model

↓

Interaction Model

↓

Composition Model

↓

Design System

↓

Implementation
```

The Composition Model assumes:

- the World already exists,
- behaviour has already occurred,
- information has already been understood.

Its responsibility is to organise understanding.

---

# Scope

This specification defines:

- Composition
- Hierarchy
- Priority
- Anchors
- Hero
- Density
- Grouping
- Breathing Space
- Composition Solving
- Adaptive Composition

This specification intentionally does **not** define:

- Components
- Tiles
- Materials
- Motion curves
- Typography
- Colours
- Tokens

Those belong to MDS.

---

# Core Question

MDL-005 exists to answer one question.

> **How should understanding be organised?**

Not:

> Where should widgets go?

---

# Composition Statement

Users should never need to consciously search for what matters.

Composition should naturally communicate:

- what is important
- why it is important
- what changed
- what should happen next

without explanation.

---

# Primary Composition Pipeline

```
World

↓

Focus

↓

Context

↓

Information

↓

Relationships

↓

Priority

↓

Composition

↓

Expressions

↓

Presentation
```

Composition therefore sits between understanding and interface.

---

# Expected Outcome

After reading MDL-005 contributors should understand:

- how hierarchy emerges
- why hero regions exist
- how adaptive layouts work
- how plugins participate
- how compositions evolve
- how future layout engines should reason

without discussing implementation.

---

# Repository Structure

```
design/

└── mdl/

    └── MDL-005 Composition Model/

        README.md

        00-document-control.md

        01-what-is-a-composition.md

        02-hierarchy.md

        03-priority.md

        04-hero.md

        05-anchors.md

        06-adaptive-composition.md

        07-density.md

        08-breathing-space.md

        09-composition-solving.md

        10-device-independence.md

        11-governance.md

        12-adrs.md

        13-contributor-guidance.md

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model

Downstream specifications:

- MDS-003 Composition Engine
- MDS-005 Motion System
- MDS-007 Tile Framework
- MDS-008 Component Library

---

# Review Status

**Status**

Draft

**Owner**

Lead Design Systems Architect

**Next File**

`00-document-control.md`
