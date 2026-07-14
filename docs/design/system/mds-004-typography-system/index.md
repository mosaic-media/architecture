<!--
File: docs/design/system/mds-004-typography-system/index.md
Document: MDS-004
Status: Draft
Version: 0.1
-->

# MDS-004 — Typography System

> *Typography is not decoration. It is the voice of the Companion.*

---

# Purpose

The Material System defines how Mosaic physically exists.

The Typography System defines how Mosaic speaks.

Unlike conventional interface typography systems, which primarily optimise for information density, the Mosaic Typography System is designed around companionship.

Typography should communicate:

- confidence
- calmness
- clarity
- editorial quality
- restraint

The objective is not simply readability.

It is effortless understanding.

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

Design Tokens

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
```

Typography consumes:

- Design Tokens
- Composition
- Material Hierarchy

It reinforces:

- hierarchy
- rhythm
- understanding
- atmosphere

---

# Scope

This specification defines:

- Typography Philosophy
- Reading Hierarchy
- Editorial Rhythm
- Type Scales
- Responsive Typography
- Hero Typography
- Reading Density
- Accessibility
- Typography Resolution
- Runtime Typography

This specification intentionally does **not** define:

- Components
- Motion
- Layout
- Colour
- Materials

Those systems work alongside Typography.

---

# Core Question

MDS-004 exists to answer one question.

> **How should language communicate understanding?**

Not:

> Which font should we use?

---

# Typography Statement

Within Mosaic:

> **Typography should disappear behind understanding.**

Users should remember:

- what they read

Not:

- how the type looked.

---

# Typography Responsibilities

Typography separates into several conceptual systems.

```text
Editorial Hierarchy

↓

Reading Rhythm

↓

Responsive Scaling

↓

Runtime Adaptation

↓

Presentation
```

Each layer contributes one responsibility.

---

# Expected Outcome

After reading MDS-004 contributors should understand:

- how Mosaic uses typography
- why editorial rhythm matters
- how typography supports Composition
- how responsive typography behaves
- how runtime adaptation works
- how accessibility influences type

without discussing specific font families or rendering engines.

---

# Repository Structure

```text
design/

└── mds/

    └── MDS-004 Typography System/

        README.md

        00-document-control.md

        01-typography-philosophy.md

        02-editorial-hierarchy.md

        03-type-scale.md

        04-reading-rhythm.md

        05-hero-typography.md

        06-responsive-typography.md

        07-accessibility.md

        08-runtime-resolution.md

        09-platform-typography.md

        10-variable-fonts.md

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

Downstream specifications:

- MDS-005 Motion System
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
