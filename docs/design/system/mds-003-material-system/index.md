<!--
File: docs/design/system/mds-003-material-system/index.md
Document: MDS-003
Status: Draft
Version: 0.1
-->

# MDS-003 — Material System

> *Materials are not textures. They are physical behaviours through which the user's entertainment becomes part of the interface.*

---

# Purpose

The Mosaic Design Language established:

- Why Mosaic exists.
- How it thinks.
- How it behaves.
- How understanding is organised.

The Design System has established:

- Design Tokens
- Colour Architecture

MDS-003 defines how those concepts become **physical interface materials**.

Unlike traditional design systems, Mosaic does not treat materials as decorative surfaces.

Materials are considered physical participants within the user's entertainment World.

They receive:

- Runtime Atmosphere
- Refraction
- Light
- Hierarchy
- Interaction

and transform those inputs into a coherent visual experience.

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

Material

↓

Typography

↓

Components
```

The Material System consumes:

- Design Tokens
- Semantic Colours
- Runtime Atmosphere

It produces:

- Physical Surfaces
- Acrylic Behaviour
- Refraction
- Depth
- Environmental Response

---

# Scope

This specification defines:

- Material Philosophy
- Material Hierarchy
- Canvas
- Acrylic
- Hero Material
- Overlay Material
- Refraction
- UV Mapping
- Light Transport
- Material Resolution
- Runtime Material Behaviour

This specification intentionally does **not** define:

- Typography
- Components
- Motion Curves
- Layout
- Interaction

Those systems consume Materials.

They do not define them.

---

# Core Question

MDS-003 exists to answer one question.

> **How should the interface physically exist?**

Not:

> How should it be coloured?

---

# Material Statement

Within Mosaic:

> **Materials communicate physical presence rather than visual decoration.**

Every material should answer:

- What is this?
- How does light interact with it?
- How does it relate to the user's entertainment?

before it answers:

- How does it look?

---

# Material Responsibilities

The Material System separates responsibilities into independent layers.

```text
Material Identity

↓

Light Behaviour

↓

Runtime Atmosphere

↓

Refraction

↓

Presentation
```

Each layer contributes one responsibility.

No layer duplicates another.

---

# Expected Outcome

After reading MDS-003 contributors should understand:

- why Mosaic uses Acrylic
- how Runtime Atmosphere interacts with materials
- how Refraction works
- how UV mapping supports adaptation
- how surfaces establish hierarchy
- how future rendering systems should implement these ideas

without discussing specific rendering technologies.

---

# Repository Structure

```text
design/

└── mds/

    └── MDS-003 Material System/

        README.md

        00-document-control.md

        01-material-philosophy.md

        02-material-hierarchy.md

        03-canvas.md

        04-acrylic.md

        05-hero-material.md

        06-overlay-material.md

        07-refraction.md

        08-uv-indexed-refraction.md

        09-light-transport.md

        10-runtime-material-resolution.md

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

Downstream specifications:

- MDS-004 Typography
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
