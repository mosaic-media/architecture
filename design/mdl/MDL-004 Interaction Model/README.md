<!--
File: design/mdl/MDL-004 Interaction Model/README.md
Document: MDL-004
Status: Draft
Version: 0.1
-->

# MDL-004 — Interaction Model

> *Understanding explains the world. Interaction explains how the world changes.*

---

# Purpose

MDL-001 established **why** Mosaic exists.

MDL-002 established **how** design decisions are made.

MDL-003 established **how Mosaic understands the world**.

MDL-004 defines **how that world behaves over time**.

Where the Mental Model describes concepts, the Interaction Model describes behaviour.

It explains:

- how Focus changes
- how Context evolves
- how Composition adapts
- how movement communicates understanding
- how continuity is preserved
- how users travel through their World without leaving it

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

The Interaction Model assumes the concepts introduced by the Mental Model already exist.

Its responsibility is to define how those concepts evolve during interaction.

---

# Scope

This specification defines:

- Behaviour
- Continuity
- Focus transitions
- Context transitions
- Temporal interaction
- Adaptive composition
- User flow
- Interaction hierarchy

This specification intentionally does **not** define:

- Motion timing
- Animation curves
- Materials
- Components
- Typography
- Layout
- Rendering

Those concerns belong to MDS.

---

# Core Question

MDL-004 exists to answer one question.

> **How should Mosaic behave?**

Not:

> How should it look?

---

# Behaviour Statement

Users should never feel they have navigated between disconnected pages.

Instead they should feel that:

> **Their World has naturally reorganised itself around what now matters.**

Everything within this specification reinforces that single idea.

---

# Primary Behaviour Model

The Interaction Model introduces the following behavioural pipeline.

```
World

↓

Focus Change

↓

Context Update

↓

Composition Re-evaluation

↓

Expression Selection

↓

Presentation Update
```

Interaction is therefore defined as:

> **The continuous evolution of the user's World.**

---

# Expected Outcome

After reading MDL-004, contributors should understand:

- how Mosaic changes over time
- why movement exists
- why compositions evolve
- how continuity is preserved
- how interaction differs from navigation
- why adaptive behaviour exists

without discussing implementation.

---

# Repository Structure

```
design/

└── mdl/

    └── MDL-004 Interaction Model/

        README.md

        00-document-control.md

        01-what-is-an-interaction-model.md

        02-continuity.md

        03-focus-transitions.md

        04-context-transitions.md

        05-composition-evolution.md

        06-movement.md

        07-user-flow.md

        08-temporal-behaviour.md

        09-interaction-states.md

        10-user-vs-system-behaviour.md

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

Downstream specifications:

- MDL-005 Composition Model
- MDS-003 Composition Engine
- MDS-005 Motion System
- MDS-008 Component Library

---

# Review Status

**Status**

Draft

**Owner**

Lead Design Systems Architect

**Next File**

`00-document-control.md`
