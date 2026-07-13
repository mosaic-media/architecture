<!--
File: design/mds/MDS-002 Colour System/00-document-control.md
Document: MDS-002
Title: Colour System
Status: Draft
Version: 0.1
-->

# Document Control

---

# Document Information

| Property | Value |
|----------|-------|
| Document ID | MDS-002 |
| Title | Mosaic Design System — Colour System |
| Classification | Internal |
| Status | Draft |
| Version | 0.1 |
| Owner | Lead Design Systems Architect |
| Parent Specifications | MDL-001 → MDL-005, MDS-001 |
| Repository | `/design/mds/MDS-002 Colour System/` |

---

# Purpose

MDS-002 defines the Colour System used throughout the Mosaic Design System.

Unlike conventional colour systems, which primarily establish visual identity, the Mosaic Colour System has three independent responsibilities.

1. Preserve the Mosaic brand.
2. Communicate semantic meaning.
3. Reflect the user's current entertainment atmosphere.

These responsibilities intentionally remain independent.

The Colour System exists to support understanding.

It should never compete with the entertainment it presents.

---

# Authority

MDS-002 governs:

- Brand Palette
- Semantic Colour Mapping
- Runtime Atmosphere
- Artwork Colour Extraction
- Theme Architecture
- Colour Resolution
- Colour Accessibility
- Colour Adaptation

This specification intentionally does **not** govern:

- Materials
- Typography
- Components
- Motion
- Layout

Those systems consume colour.

They do not define it.

---

# Relationship To MDS

The Colour System extends the Design Token Architecture.

```mermaid
flowchart TD

Vision
Vision --> Principles
Principles --> MentalModel
MentalModel --> Interaction
Interaction --> Composition
Composition --> Tokens
Tokens --> Colour
Colour --> Material
Material --> Components
```

The Colour System consumes Semantic Tokens.

It never introduces new semantic meaning.

---

# Design Intent

The Colour System intentionally separates three independent ideas.

```text
Brand

↓

Meaning

↓

Atmosphere
```

This separation is fundamental.

Brand should never determine semantic meaning.

Artwork should never redefine the Mosaic brand.

Atmosphere should never weaken accessibility.

Each layer performs exactly one responsibility.

---

# Reader Expectations

Before reading this specification contributors should already understand:

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model
- MDS-001 Design Token Architecture

This document assumes the conceptual architecture has already been established.

Its responsibility is implementation.

---

# Architectural Scope

The Colour System defines:

- Brand Colour Architecture
- Semantic Colour Roles
- Adaptive Atmosphere
- Runtime Colour Behaviour
- Accessibility Rules
- Colour Resolution

It intentionally avoids discussing implementation frameworks such as:

- CSS
- Flutter
- SwiftUI
- Compose

Those are generated from the Colour System rather than defining it.

---

# Stability

Expected lifetime.

| Artefact | Expected Lifetime |
|----------|-------------------|
| Primitive Colour Values | Years |
| Brand Palette | Many Years |
| Semantic Colour Roles | Many Years |
| Runtime Colour Algorithms | Occasionally |
| Presentation Themes | Frequently |

Colour values may evolve.

Semantic meaning should remain significantly more stable.

---

# Success Criteria

MDS-002 succeeds when:

- screenshots are immediately recognisable as Mosaic
- artwork enhances rather than overwhelms the interface
- semantic meaning remains consistent across themes
- accessibility remains uncompromised
- runtime adaptation feels natural rather than decorative
- colour communicates understanding before aesthetics

Users should remember:

- their entertainment

and

- the feeling of Mosaic.

They should rarely notice the Colour System consciously.

---

# Review Status

**Status**

Draft

**Dependencies**

- MDL-001 → MDL-005
- MDS-001 Design Token Architecture

**Supersedes**

None.

**Next File**

`01-colour-philosophy.md`
