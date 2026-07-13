<!--
File: design/mds/MDS-002 Colour System/references.md
Document: MDS-002
Title: References
Status: Draft
Version: 0.1
-->

# References

---

# Purpose

This document records the architectural influences, design philosophies and implementation concepts that informed **MDS-002 — Colour System**.

Unlike implementation documentation, these references exist to explain the reasoning behind the Colour System rather than prescribe specific algorithms.

The Mosaic Colour System intentionally combines ideas from:

- visual design
- perception
- accessibility
- material design
- lighting
- runtime adaptation

into a single architectural model centred around entertainment rather than software.

---

# Reading Order

Contributors should approach references in the following order.

1. MDL Specifications
2. MDS Token Architecture
3. Colour System
4. Material System
5. Runtime Systems
6. Platform Implementations

The Mosaic Design Language remains the primary authority.

External references provide context.

---

# Internal References

## MDL-001 — Vision

Provides:

- Product identity
- Companion philosophy
- Immersion
- Entertainment-first thinking

Every colour decision should ultimately reinforce the experience described within the Vision.

---

## MDL-002 — Principles

Provides:

- Content Leads
- Context Before Prediction
- Be A Companion
- Movement Preserves Understanding

The Colour System should strengthen these principles.

It should never replace them.

---

## MDL-003 — Mental Model

Provides:

- World
- Focus
- Context
- Information

Runtime Atmosphere intentionally reflects the user's current World rather than arbitrary interface state.

---

## MDL-004 — Interaction Model

Provides:

- Behaviour
- Continuity
- Runtime evolution

Atmosphere should evolve with interaction rather than behaving like independent theme switching.

---

## MDL-005 — Composition Model

Provides:

- Hero
- Hierarchy
- Priority
- Density

Colour should reinforce Composition.

It should never redefine it.

---

## MDS-001 — Design Token Architecture

Provides:

- Primitive Tokens
- Semantic Tokens
- Runtime Tokens
- Resolution Pipeline

The Colour System implements this architecture.

It should not modify it.

---

# Future Specifications

The following specifications depend directly upon MDS-002.

- MDS-003 Material System
- MDS-004 Typography
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-007 Tile Framework
- MDS-008 Component Library

These specifications consume Semantic Colours and Runtime Atmosphere rather than creating independent colour systems.

---

# Colour Theory

The Mosaic Colour System intentionally distinguishes between:

- identity
- meaning
- emotion

Traditional colour theory often merges these responsibilities.

Mosaic deliberately separates them into:

```
Brand

↓

Semantic

↓

Atmosphere
```

This separation allows each system to evolve independently.

---

# Human Perception

The Colour System is influenced by several characteristics of human perception.

Examples include:

- simultaneous contrast
- colour adaptation
- luminance perception
- visual hierarchy
- peripheral awareness

Rather than using colour to attract attention, Mosaic primarily uses colour to support understanding and atmosphere.

---

# Environmental Lighting

One of the defining influences behind the Mosaic Colour System is environmental lighting.

Rather than treating artwork as a palette...

Mosaic treats artwork as a light source.

This philosophical distinction influences:

- Runtime Atmosphere
- Material System
- Refraction Engine
- Acrylic rendering

It is one of the defining characteristics of the Mosaic visual identity.

---

# Accessibility

Accessibility is considered a first-class architectural concern.

The Colour System intentionally assumes:

```
Accessibility

↓

Semantic Meaning

↓

Atmosphere

↓

Presentation
```

This ordering ensures that runtime adaptation never compromises readability.

Future implementations should validate accessibility continuously rather than treating it as a final review step.

---

# Runtime Design

Unlike traditional Design Systems, Mosaic assumes colour changes over time.

Examples include:

- artwork
- Focus
- Context
- playback
- accessibility
- user preference

The Colour System therefore treats runtime adaptation as an architectural responsibility rather than an implementation feature.

---

# Material Interaction

The Colour System intentionally stops at Materials.

Conceptually.

```text
Colour

↓

Atmosphere

↓

Materials

↓

Presentation
```

Materials determine:

- translucency
- diffusion
- glow
- refraction

Colour provides environmental influence.

This separation allows future Material Systems to evolve independently.

---

# Platform Independence

The Colour System intentionally avoids platform-specific implementation.

Every client should consume identical semantic meaning while generating implementation appropriate for:

- Web
- Flutter
- SwiftUI
- Compose
- Future platforms

The visual language should remain recognisable regardless of rendering technology.

---

# Mosaic-Specific Influences

The Colour System emerged directly from the architectural decisions made during Mosaic discovery.

Significant ideas include:

- artwork should illuminate rather than recolour the interface
- runtime atmosphere should remain subtle
- acrylic should behave like illuminated material rather than frosted glass
- colour should reinforce composition rather than replace it
- brand identity should remain recognisable regardless of current entertainment

These concepts distinguish Mosaic from existing entertainment platforms.

---

# Relationship To The Refraction System

The Runtime Atmosphere defined within MDS-002 intentionally provides one of the primary inputs into the Mosaic Refraction System.

Conceptually.

```text
Artwork

↓

Colour Extraction

↓

Runtime Atmosphere

↓

Material Refraction

↓

Presentation
```

This relationship will be formalised within the Material System specification.

The Colour System intentionally stops before physical rendering begins.

---

# Normative References

Required reading before contributing to MDS-002.

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model
- MDS-001 Design Token Architecture

Together these specifications define the conceptual foundation of the Colour System.

---

# Informative References

Future contributors may also wish to review:

- MDS-003 Material System
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-008 Component Library

These specifications describe how colour becomes a rendered experience.

---

# Living Document

This reference list should remain intentionally concise.

References should only be introduced when they materially influence:

- semantic architecture
- runtime atmosphere
- accessibility
- implementation boundaries

The purpose of this document is to preserve architectural reasoning rather than become an exhaustive bibliography.

---

# Completion

This concludes **MDS-002 — Colour System**.

The next specification in the Mosaic Design System is:

> **MDS-003 — Material System**

Where MDS-002 defines **how colour communicates meaning**, MDS-003 defines **how those colours physically exist within the Mosaic interface**.

It formalises:

- Acrylic
- Refraction
- Light transport
- UV-indexed atmosphere
- Material hierarchy
- Canvas
- Hero surfaces
- Overlay materials
- Adaptive translucency

This specification is expected to become one of the defining technical and visual documents of the entire Mosaic platform.
