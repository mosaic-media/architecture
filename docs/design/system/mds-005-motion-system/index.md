<!--
File: docs/design/system/mds-005-motion-system/index.md
Document: MDS-005
Status: Draft
Version: 0.4
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
N11["Components"]
N12["Presentation"]

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

# Guiding Question

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

```mermaid
flowchart TD

N1["Behaviour"]
N2["Temporal Meaning"]
N3["Material Response"]
N4["Motion"]
N5["Presentation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
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

        references.md

        glossary.md
```

---

# Dependencies

Required reading:

- [MDL-001](../../language/mdl-001-vision/index.md) → [MDL-005](../../language/mdl-005-composition-model/index.md)
- [MDS-001 — Design Token Architecture](../mds-001-design-token-architecture/index.md)
- [MDS-002 — Colour System](../mds-002-colour-system/index.md)
- [MDS-003 — Material System](../mds-003-material-system/index.md)
- [MDS-004 — Typography System](../mds-004-typography-system/index.md)

Downstream specifications:

- [MDS-006 — Composition Engine](../mds-006-composition-engine/index.md)
- [MDS-007 — Tile Framework](../mds-007-tile-framework/index.md)
- [MDS-008 — Component Library](../mds-008-component-library/index.md)
