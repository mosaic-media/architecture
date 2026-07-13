<!--
File: design/mds/MDS-005 Motion System/README.md
Document: MDS-005
Status: Draft
Version: 0.1
-->

# MDS-005 — Motion System

> *Motion is not animation. Motion is the visible expression of understanding changing over time.*

---

# Purpose

The previous Mosaic Design System specifications established:

- Design Tokens
- Colour
- Materials
- Typography

These define what the interface is.

MDS-005 defines **how that interface changes**.

Unlike conventional motion systems, which primarily focus on visual transitions, the Mosaic Motion System exists to communicate behavioural continuity.

Motion should explain:

- what changed,
- why it changed,
- how it relates to the previous state.

The user should never perceive animation.

They should perceive understanding.

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

Components

↓

Presentation
```

The Motion System consumes:

- Interaction Model
- Composition
- Material System
- Typography

It communicates behavioural evolution over time.

---

# Scope

This specification defines:

- Motion Philosophy
- Motion Hierarchy
- Behavioural Motion
- Material Motion
- Refraction Motion
- Temporal Continuity
- Motion Curves
- Motion Accessibility
- Runtime Motion Resolution
- Platform Motion

This specification intentionally does **not** define:

- Components
- Layout
- Business Logic
- Interaction Behaviour

Those systems drive motion.

They do not define it.

---

# Core Question

MDS-005 exists to answer one question.

> **How should behavioural change become visible?**

Not:

> Which animation should play?

---

# Motion Statement

Within Mosaic:

> **Motion communicates understanding.**

If removing motion reduces understanding...

The motion belongs.

If removing motion changes only appearance...

The motion should be questioned.

---

# Motion Responsibilities

The Motion System separates motion into several conceptual layers.

```text
Behaviour

↓

Temporal Meaning

↓

Material Response

↓

Motion

↓

Presentation
```

Each layer contributes one responsibility.

Motion is therefore the consequence of behaviour rather than an isolated visual system.

---

# Expected Outcome

After reading MDS-005 contributors should understand:

- why Mosaic moves,
- how behaviour drives motion,
- how materials participate,
- how continuity is preserved,
- how accessibility affects motion,
- how runtime motion is resolved,

without discussing rendering technologies or animation frameworks.

---

# Repository Structure

```text
design/

└── mds/

    └── MDS-005 Motion System/

        README.md

        00-document-control.md

        01-motion-philosophy.md

        02-motion-hierarchy.md

        03-behavioural-motion.md

        04-material-motion.md

        05-refraction-motion.md

        06-temporal-continuity.md

        07-motion-curves.md

        08-accessibility.md

        09-runtime-motion-resolution.md

        10-platform-motion.md

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
- MDS-001 Design Token Architecture
- MDS-002 Colour System
- MDS-003 Material System
- MDS-004 Typography System

Downstream specifications:

- MDS-006 Composition Engine
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
