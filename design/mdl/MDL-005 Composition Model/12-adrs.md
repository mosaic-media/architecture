<!--
File: design/mdl/MDL-005 Composition Model/12-adrs.md
Document: MDL-005
Chapter: 12
Title: Architectural Decision Records
Status: Draft
Version: 0.1
-->

# Architectural Decision Records

---

# Purpose

The Architectural Decision Records (ADRs) contained within MDL-005 preserve the reasoning behind the Composition Model.

Where previous specifications established:

- Vision
- Principles
- Mental Model
- Interaction

MDL-005 establishes **how understanding is organised**.

These ADRs document why the Composition Model was designed the way it was, ensuring future contributors understand the architectural intent before proposing changes.

Composition is considered one of the defining architectural systems of Mosaic.

Its decisions should therefore remain traceable throughout the lifetime of the project.

---

# ADR Format

Every ADR follows the standard Mosaic structure.

```text
ADR Number

Status

Context

Decision

Consequences

Alternatives Considered

Related Specifications
```

Each ADR records exactly one significant compositional decision.

---

# ADR-071

## Title

Composition Organises Understanding Rather Than Interface

### Status

Accepted

### Context

Traditional interface frameworks typically organise interface components directly.

This tightly couples understanding with implementation.

### Decision

Composition becomes a conceptual layer that organises understanding before presentation exists.

### Consequences

Presentation technologies may evolve independently while preserving identical conceptual organisation.

---

# ADR-072

## Title

Hierarchy Emerges From Priority

### Status

Accepted

### Context

Many design systems assign hierarchy manually.

This frequently produces inconsistent experiences.

### Decision

Hierarchy becomes a direct consequence of Priority.

Priority itself emerges from:

- Focus
- Context
- Relationships

### Consequences

Hierarchy naturally adapts as the user's World evolves.

No manual hierarchy management should normally be required.

---

# ADR-073

## Title

Hero Is An Emergent Concept

### Status

Accepted

### Context

Traditional interfaces frequently hardcode hero regions.

This weakens adaptability.

### Decision

The Hero becomes the highest-priority Expression within the current Composition.

### Consequences

Heroes evolve naturally.

They are never manually assigned.

Different clients remain conceptually identical despite differing visual implementations.

---

# ADR-074

## Title

Anchors Preserve Orientation

### Status

Accepted

### Context

Highly adaptive interfaces frequently become disorientating.

Founder workshops repeatedly identified the need for behavioural stability.

### Decision

Stable Anchors become first-class compositional concepts.

Anchors preserve orientation while surrounding information adapts.

### Consequences

Adaptive compositions remain understandable even as they evolve continuously.

---

# ADR-075

## Title

Density Is Behavioural Rather Than Visual

### Status

Accepted

### Context

Density is traditionally treated as spacing or compact mode.

This tightly couples understanding with presentation.

### Decision

Density becomes a conceptual property describing how much understanding should be communicated.

Presentation determines how density is expressed.

### Consequences

Rich and sparse compositions remain consistent across every supported platform.

---

# ADR-076

## Title

Composition Is Solved Rather Than Authored

### Status

Accepted

### Context

Static layouts cannot effectively represent continuously changing Worlds.

Founder workshops consistently favoured adaptive understanding over static screens.

### Decision

Composition becomes the output of a conceptual solving process.

The Composition Solver determines:

- hierarchy
- priority
- grouping
- Hero
- Expressions

### Consequences

Future runtime systems remain adaptive while preserving one coherent compositional language.

---

# ADR-077

## Title

Plugins Contribute Knowledge Rather Than Layout

### Status

Accepted

### Context

Allowing extensions to generate interface fragments inevitably fragments product identity.

### Decision

Plugins contribute:

- Information
- Relationships

The platform remains solely responsible for:

- Composition
- Priority
- Hierarchy
- Expressions

### Consequences

Every extension inherits the same compositional language.

The ecosystem scales without creating competing interface paradigms.

---

# ADR-078

## Title

Composition Is Device Independent

### Status

Accepted

### Context

Users increasingly consume entertainment across multiple devices.

Maintaining separate composition models would fragment understanding.

### Decision

Composition becomes device independent.

Only Presentation adapts.

### Consequences

Users experience one consistent World regardless of device.

---

# ADR-079

## Title

Breathing Space Is A Compositional Concept

### Status

Accepted

### Context

Whitespace is traditionally considered a visual concern.

Founder workshops consistently described empty space as supporting understanding rather than aesthetics.

### Decision

Breathing Space becomes part of Composition rather than visual styling.

### Consequences

Future Material Systems and Layout Engines should preserve conceptual rhythm before optimising visual density.

---

# ADR Relationships

```mermaid
flowchart TD

ADR071["Understanding"]

ADR072["Priority"]

ADR073["Hero"]

ADR074["Anchors"]

ADR075["Density"]

ADR076["Solver"]

ADR077["Plugins"]

ADR078["Device Independence"]

ADR079["Breathing Space"]

ADR071 --> ADR072

ADR072 --> ADR073

ADR072 --> ADR075

ADR073 --> ADR074

ADR075 --> ADR079

ADR074 --> ADR076

ADR076 --> ADR077

ADR076 --> ADR078
```

Every compositional decision reinforces the same objective.

Understanding before presentation.

---

# Future ADRs

Future Composition ADRs are expected to formalise:

- Composition Scoring
- Relationship Weighting
- Expression Selection
- Runtime Adaptation
- Multi-User Composition
- Shared Composition
- Predictive Composition
- Accessibility Composition

These intentionally remain outside MDL-005 Version 0.1.

---

# ADR Governance

Composition ADRs should change only when:

- repeated user research demonstrates misunderstanding,
- behavioural evolution requires conceptual refinement,
- the Mental Model changes,
- multiple specifications repeatedly conflict.

Presentation concerns should never trigger changes to the Composition Model.

---

# Summary

The ADRs within MDL-005 define one of the most distinctive architectural characteristics of Mosaic.

Rather than arranging interface...

Mosaic arranges understanding.

Every future implementation should preserve this distinction.

Doing so allows the platform to evolve visually while remaining conceptually stable for years to come.

---

# Review Status

**Status**

Draft

**Next File**

`13-contributor-guidance.md`
