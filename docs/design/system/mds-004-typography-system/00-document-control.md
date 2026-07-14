<!--
File: docs/design/system/mds-004-typography-system/00-document-control.md
Document: MDS-004
Title: Typography System
Status: Draft
Version: 0.1
-->

# Document Control

---

# Document Information

| Property | Value |
|----------|-------|
| Document ID | MDS-004 |
| Title | Mosaic Design System — Typography System |
| Classification | Internal |
| Status | Draft |
| Version | 0.1 |
| Owner | Lead Design Systems Architect |
| Parent Specifications | MDL-001 → MDL-005, MDS-001, MDS-002, MDS-003 |
| Repository | `/design/mds/MDS-004 Typography System/` |

---

# Purpose

MDS-004 defines the Typography System used throughout Mosaic.

Typography is not treated as visual styling.

It is treated as the primary mechanism through which Mosaic communicates knowledge.

Where the Material System defines:

> How the interface physically exists.

Typography defines:

> How the interface speaks.

Its responsibility is to make information feel:

- calm
- intelligent
- effortless
- trustworthy
- editorial

The Typography System therefore becomes a fundamental part of the Companion.

---

# Authority

MDS-004 governs:

- Type hierarchy
- Editorial rhythm
- Reading behaviour
- Responsive typography
- Variable font behaviour
- Accessibility
- Runtime typography
- Cross-platform typography

This specification intentionally does **not** govern:

- Colour
- Materials
- Motion
- Components
- Layout

Those systems work alongside Typography.

---

# Relationship To MDS

Typography sits between Materials and Motion.

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
Motion --> Components
Components --> Presentation
```

Typography consumes:

- Composition
- Colour
- Materials

It communicates:

- hierarchy
- rhythm
- language
- understanding

---

# Design Intent

Many interface typography systems optimise for:

- density
- efficiency
- information throughput

Mosaic intentionally optimises for:

- comprehension
- calmness
- editorial quality
- companionship

Typography should encourage users to read naturally rather than process interfaces mechanically.

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

Typography builds upon every one of these systems.

It should never redefine them.

---

# Architectural Scope

The Typography System defines:

- editorial hierarchy
- reading rhythm
- semantic typography
- runtime scaling
- accessibility
- responsive typography

It intentionally avoids implementation-specific concerns such as:

- CSS font declarations
- Flutter TextTheme
- SwiftUI Font
- Compose Typography

Those are implementation artefacts generated from this architecture.

---

# Stability

Expected lifetime.

| Artefact | Expected Lifetime |
|----------|-------------------|
| Font Implementation | Months |
| Variable Font Support | Months |
| Font Family | Years |
| Typography Hierarchy | Years |
| Typography Philosophy | Decades |

Rendering technology may evolve.

Reading behaviour should remain recognisably Mosaic.

---

# Success Criteria

MDS-004 succeeds when:

- users instinctively know what to read first
- reading feels calm rather than mechanical
- typography supports Composition rather than competing with it
- long-form reading remains comfortable
- interfaces feel editorial rather than technical
- typography quietly disappears behind understanding

Users should remember:

- the story,
- the information,
- the entertainment.

They should rarely remember the typography itself.

---

# Review Status

**Status**

Draft

**Dependencies**

- MDL-001 → MDL-005
- MDS-001
- MDS-002
- MDS-003

**Supersedes**

None.

**Next File**

`01-typography-philosophy.md`
