<!--
File: docs/design/system/mds-004-typography-system/12-adrs.md
Document: MDS-004
Chapter: 12
Title: Architectural Decision Records
Status: Draft
Version: 0.1
-->

# Architectural Decision Records

---

# Purpose

The Architectural Decision Records (ADRs) contained within MDS-004 preserve the architectural reasoning behind the Mosaic Typography System.

Where previous specifications established:

- Design Tokens
- Colour
- Materials

MDS-004 establishes the editorial voice through which the Mosaic Companion communicates.

These ADRs explain why Mosaic deliberately treats typography as language rather than decoration.

Future contributors should understand these decisions before proposing changes to typography behaviour or hierarchy.

---

# ADR Format

Every Mosaic ADR follows the standard structure.

```text
ADR Number

Status

Context

Decision

Consequences

Alternatives Considered

Related Specifications
```

Each ADR records one significant architectural decision.

---

# ADR-125

## Title

Treat Typography As Editorial Architecture

### Status

Accepted

### Context

Many interface systems optimise typography for information density.

Founder workshops consistently described Mosaic as a Companion rather than a dashboard.

### Decision

Typography becomes editorial architecture rather than interface styling.

### Consequences

Reading becomes calmer, more natural and more immersive across every Mosaic client.

---

# ADR-126

## Title

Editorial Hierarchy Drives Typography

### Status

Accepted

### Context

Allowing typography to determine hierarchy creates inconsistent experiences.

### Decision

Composition defines hierarchy.

Typography expresses hierarchy.

### Consequences

Editorial consistency is preserved across every device and future redesign.

---

# ADR-127

## Title

Separate Editorial Roles From Font Sizes

### Status

Accepted

### Context

Pixel-based typography tightly couples application code to implementation.

### Decision

Applications consume editorial roles such as:

- Display
- Heading
- Section
- Body
- Supporting
- Caption

Runtime determines physical implementation.

### Consequences

Typography becomes platform independent and future proof.

---

# ADR-128

## Title

Runtime Typography Owns Adaptation

### Status

Accepted

### Context

Accessibility, viewing distance and device capabilities require adaptive typography.

### Decision

The Runtime Typography Resolver becomes solely responsible for runtime adaptation.

Applications remain unaware of implementation details.

### Consequences

Typography adapts continuously while preserving one editorial language.

---

# ADR-129

## Title

Reading Comfort Has Higher Priority Than Density

### Status

Accepted

### Context

Many media applications sacrifice reading comfort to display additional information.

### Decision

Reading comfort always takes precedence over interface density.

Composition should reduce information before typography becomes uncomfortable.

### Consequences

Long-form reading becomes significantly more enjoyable.

---

# ADR-130

## Title

Hero Typography Introduces Rather Than Advertises

### Status

Accepted

### Context

Traditional Hero typography frequently behaves like marketing.

Founder workshops consistently favoured calm editorial presentation.

### Decision

Hero Typography communicates confidence through restraint rather than spectacle.

### Consequences

Entertainment remains emotionally dominant while typography quietly establishes orientation.

---

# ADR-131

## Title

Accessibility Overrides Typography Aesthetics

### Status

Accepted

### Context

Decorative typography frequently reduces readability.

### Decision

Accessibility possesses higher authority than typographic styling.

### Consequences

Typography remains understandable regardless of:

- theme,
- device,
- accessibility settings,
- runtime adaptation.

---

# ADR-132

## Title

Variable Fonts Are An Implementation Detail

### Status

Accepted

### Context

Variable Fonts provide significant flexibility but should not influence editorial architecture.

### Decision

Variable Fonts remain entirely behind the Runtime Typography Resolver.

Applications consume editorial roles.

### Consequences

Future typography technologies may evolve without affecting application code.

---

# ADR-133

## Title

Extensions Inherit Typography

### Status

Accepted

### Context

Allowing extensions to introduce independent typographic systems fragments product identity.

### Decision

Extensions contribute editorial content.

The platform owns typography.

### Consequences

Community extensions inherit future typography improvements automatically.

---

# ADR Relationships

```mermaid
flowchart TD

ADR125["Editorial Architecture"]

ADR126["Hierarchy"]

ADR127["Editorial Roles"]

ADR128["Runtime"]

ADR129["Reading Comfort"]

ADR130["Hero"]

ADR131["Accessibility"]

ADR132["Variable Fonts"]

ADR133["Extensions"]

ADR125 --> ADR126
ADR126 --> ADR127
ADR127 --> ADR128
ADR128 --> ADR132
ADR129 --> ADR127
ADR130 --> ADR126
ADR131 --> ADR128
ADR128 --> ADR133
```

Together these decisions establish typography as the editorial voice of the Mosaic Companion.

---

# Future ADRs

Future Typography ADRs are expected to formalise:

- AI-assisted Reading Profiles
- Adaptive Reading Tempo
- Cross-Language Editorial Behaviour
- Dynamic Optical Scaling
- Immersive Reading Mode
- Television Typography Profiles
- Accessibility Reading Personas
- Editorial Voice Localisation

These intentionally remain outside the scope of MDS-004 Version 0.1.

---

# ADR Governance

Typography ADRs should change only when:

- editorial research identifies deficiencies,
- accessibility research requires refinement,
- runtime typography architecture evolves,
- the Design Language itself changes.

Rendering technology alone should never justify architectural changes.

Typography should remain recognisably Mosaic regardless of implementation.

---

# Summary

The ADRs contained within MDS-004 define the editorial identity of Mosaic.

Typography is not treated as decoration.

It is treated as language.

Every implementation should therefore preserve:

- calmness,
- hierarchy,
- reading rhythm,
- companionship,

while allowing rendering technology to evolve independently.

---

# Review Status

**Status**

Draft

**Next File**

`13-contributor-guidance.md`
