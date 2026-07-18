<!--
File: docs/design/language/mdl-002-principles/references.md
Document: MDL-002
Status: Draft
-->

# References

---

# Purpose

This document records the references, theories and external guidance that informed **MDL-002 — Principles**.

Unlike implementation specifications, MDL references are provided to explain the origin of ideas and to aid future contributors who wish to explore the reasoning in greater depth.

References should **inform** the design language.

They should never replace it.

MDL is intentionally opinionated.

Its authority comes from the philosophy established by Mosaic rather than any individual external source.

---

# Reading Strategy

Contributors should approach references in the following order.

1. MDL Specifications
2. MDS Specifications
3. Product Design
4. Design Systems
5. Human Factors
6. Software Architecture

The Mosaic Design Language itself always remains the primary source of truth.

---

# Internal References

## [MDL-001 — Mosaic Design Language Vision](../mdl-001-vision/index.md)

Defines:

- Product vision
- Product beliefs
- Design philosophy
- Governance

MDL-002 should always be interpreted as a practical module of [MDL-001](../mdl-001-vision/index.md) rather than an independent specification.

---

## Future MDL Specifications

The following specifications build directly upon MDL-002.

- [MDL-003 — Mental Model](../mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../mdl-004-interaction-model/index.md)
- [MDL-005 — Composition Model](../mdl-005-composition-model/index.md)

These specifications should reference principles rather than redefine them.

---

## Future MDS Specifications

The following engineering specifications are expected to implement MDL-002.

- [MDS-001 — Design Token Architecture](../../system/mds-001-design-token-architecture/index.md)
- [MDS-003 — Material System](../../system/mds-003-material-system/index.md)
- [MDP-001 — Adaptive Composition Runtime](../../../engineering/architecture/mdp-001-adaptive-composition-runtime/index.md)
- [MDS-005 — Motion System](../../system/mds-005-motion-system/index.md)
- [MDS-008 — Component Library](../../system/mds-008-component-library/index.md)

MDL explains **why**.

MDS explains **how**.

---

# Product Design

## Human-Centred Design

Referenced throughout MDL.

Particularly relevant concepts include:

- reducing cognitive effort
- user-centred decision making
- progressive disclosure
- contextual interaction

MDL extends these ideas through the concept of the entertainment companion.

---

## Calm Technology

Referenced primarily by:

- Principle 07
- Movement philosophy
- Attention management

Important concepts adopted include:

- peripheral awareness
- respectful attention
- technology disappearing once its work is complete

Mosaic intentionally applies these ideas to entertainment software rather than ubiquitous computing.

---

# Design Systems

The following systems influenced the structure of MDL rather than its philosophy.

## Apple Human Interface Guidelines

Influences:

- experience-first thinking
- restraint
- hierarchy
- consistency

Rejected:

- visual identity
- material language

---

## Material Design

Influences:

- documentation structure
- systematic thinking
- design token philosophy

Rejected:

- visual metaphor
- interaction philosophy

---

## Fluent Design

Influences:

- adaptive interfaces
- cross-device thinking
- long-term governance

---

## Atlassian Design System

Influences:

- documentation quality
- specification organisation
- engineering collaboration

---

## Carbon Design System

Influences:

- governance
- enterprise documentation
- design maturity

---

# Architecture

## Architectural Decision Records

Referenced for:

- recording rationale
- preserving historical context
- long-term maintainability

The ADR process is adopted throughout MDL because it encourages decisions to remain understandable long after implementation changes.

---

## Documentation As Code

MDL assumes documentation should be:

- version controlled
- peer reviewed
- traceable
- maintainable

Markdown is considered the canonical representation.

Generated PDFs are publication artefacts.

---

# Product Philosophy

The following recurring themes influenced MDL.

## Experience Before Interface

The interface exists to communicate experience.

It should never become the experience itself.

---

## Systems Before Features

Reusable systems create more coherent products than isolated features.

---

## Context Before Prediction

Current user intent provides a stronger design signal than speculative behavioural prediction.

---

## Enhancement Before Persuasion

Software should deepen existing experiences rather than redirect attention.

---

## Companion Over Platform

Software should behave like a trusted companion rather than an attention-seeking platform.

---

# Design Documentation

The overall documentation structure of MDL draws inspiration from mature design systems that separate:

- philosophy
- principles
- foundations
- components
- governance

rather than treating a design system as merely a component library.  [Magic Patterns](https://www.magicpatterns.com/blog/design-system-documentation)

---

# Specification Conventions

The following conventions apply across all MDL documents.

Markdown is the authoritative source.

Every specification should:

- define purpose
- establish scope
- reference related specifications
- remain implementation independent where practical
- introduce ADRs where significant decisions occur

Future specifications should reuse this structure unless there is a compelling reason not to.

---

# Future References

Future specifications are expected to introduce references relating to:

- Information Architecture
- Runtime Composition
- GraphQL UI
- Motion Design
- Accessibility
- Typography
- Material Systems
- Colour Science
- Human Perception
- Spatial Cognition

These references intentionally belong with the specifications that require them.

---

# Living Document

This reference list should remain concise.

A reference should only be added if it has materially influenced:

- a principle
- an ADR
- a governance decision
- the structure of MDL

MDL is not intended to become an academic bibliography.

It is a practical engineering and design reference for contributors to Mosaic.

---

# Completion

This concludes **MDL-002 — Principles**.

The next specification in the Mosaic Design Language is:

> **[MDL-003 — Mental Model](../mdl-003-mental-model/index.md)**

Where [MDL-001](../mdl-001-vision/index.md) explains **why** Mosaic exists and MDL-002 explains **how** decisions are made, [MDL-003](../mdl-003-mental-model/index.md) defines **how Mosaic thinks**.

It introduces the conceptual model that both users and contributors should internalise before considering implementation details.
