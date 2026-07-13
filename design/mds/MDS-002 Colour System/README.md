<!--
File: design/mds/MDS-002 Colour System/README.md
Document: MDS-002
Status: Draft
Version: 0.1
-->

# MDS-002 — Colour System

> *Colour should communicate understanding before identity, and identity before decoration.*

---

# Purpose

MDS-001 established how design intent becomes machine-readable through the Design Token Architecture.

MDS-002 defines how colour expresses that intent.

Unlike conventional colour systems, the Mosaic Colour System is not centred around a brand palette.

Instead, it balances three independent responsibilities:

- Brand Identity
- Semantic Communication
- Runtime Atmosphere

These responsibilities intentionally remain separate.

The result is a colour system that is:

- recognisable
- adaptive
- accessible
- artwork-aware
- implementation independent

---

# Relationship to Previous Specifications

```
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

Colour System

↓

Material System

↓

Components
```

The Colour System implements the semantic architecture established by MDS-001.

It never replaces it.

---

# Scope

This specification defines:

- Brand Colours
- Semantic Colours
- Runtime Atmosphere
- Artwork Colour Extraction
- Adaptive Colour
- Theme Architecture
- Light Mode
- Dark Mode
- Accessibility
- Colour Resolution

This specification intentionally does **not** define:

- Materials
- Components
- Typography
- Motion
- Layout

Those specifications consume colour.

They do not define it.

---

# Core Question

MDS-002 exists to answer one question.

> **How should colour communicate meaning?**

Not:

> Which colours should we use?

---

# Colour Statement

Within Mosaic:

> **Colour communicates understanding first.**

Brand second.

Decoration last.

If colour ever becomes the primary source of understanding, accessibility has already failed.

---

# Colour Responsibilities

The Mosaic Colour System separates colour into three independent systems.

```
Brand

↓

Semantic

↓

Atmosphere
```

Each system exists for one purpose.

They intentionally do not overlap.

---

# Expected Outcome

After reading MDS-002 contributors should understand:

- how Mosaic uses colour
- how artwork influences the interface
- how runtime atmosphere works
- how accessibility is preserved
- how themes evolve
- how clients resolve colour consistently

without discussing implementation.

---

# Repository Structure

```
design/

└── mds/

    └── MDS-002 Colour System/

        README.md

        00-document-control.md

        01-colour-philosophy.md

        02-brand-colours.md

        03-semantic-colours.md

        04-runtime-atmosphere.md

        05-artwork-colour-extraction.md

        06-theme-architecture.md

        07-light-and-dark.md

        08-accessibility.md

        09-colour-resolution.md

        10-runtime-synthesis.md

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

Downstream specifications:

- MDS-003 Material System
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-008 Component Library

---

# Review Status

**Status**

Draft

**Owner**

Lead Design Systems Architect

**Next File**

`00-document-control.md`
