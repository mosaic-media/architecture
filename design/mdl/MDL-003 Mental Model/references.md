<!--
File: design/mdl/MDL-003 Mental Model/references.md
Document: MDL-003
Title: References
Status: Draft
Version: 0.1
-->

# References

---

# Purpose

This document records the references and architectural influences that informed **MDL-003 — Mental Model**.

Unlike implementation specifications, these references exist to explain conceptual thinking rather than prescribe implementation.

MDL intentionally synthesises ideas from:

- Human-Centred Design
- Cognitive Psychology
- Information Architecture
- Systems Thinking
- Knowledge Representation
- Software Architecture

The Mental Model itself remains an original architectural model created specifically for Mosaic.

---

# Reading Order

Future contributors should approach references in the following order.

1. MDL Specifications
2. Product Design
3. Human Factors
4. Information Architecture
5. Systems Architecture
6. Engineering References

The Mosaic Design Language always remains the authoritative source.

---

# Internal References

## MDL-001 — Vision

Defines:

- Why Mosaic exists
- Product philosophy
- Product beliefs
- Companion metaphor

MDL-003 should always be interpreted as an implementation-independent extension of the Vision.

---

## MDL-002 — Principles

Defines:

- Decision making
- Design principles
- Governance
- Design authority

Every concept introduced by MDL-003 should reinforce one or more MDL-002 principles.

---

## Future Specifications

The following specifications build directly upon the Mental Model.

- MDL-004 Interaction Model
- MDL-005 Composition Model

These specifications intentionally assume the concepts introduced by MDL-003.

They should extend them rather than redefine them.

---

## Future MDS Specifications

The following MDS specifications are expected to implement the Mental Model.

- MDS-001 Design Token Architecture
- MDS-003 Composition Engine
- MDS-007 Tile Framework
- MDS-008 Component Library
- MDS-011 Extension Design Specification

The Mental Model defines:

> What exists.

MDS defines:

> How those concepts become interface.

---

# Human-Centred Design

## Mental Models

Referenced throughout this specification.

Key concepts include:

- conceptual consistency
- user understanding
- predictable behaviour
- reducing cognitive effort

MDL extends these ideas by introducing a domain-specific conceptual architecture centred around entertainment rather than productivity software.

---

## Cognitive Load

Referenced throughout:

- World
- Focus
- Context
- Composition

Reducing unnecessary interpretation is considered a primary optimisation target.

Future Composition specifications are expected to expand upon these ideas.

---

# Information Architecture

The Mental Model intentionally draws inspiration from information architecture rather than traditional interface design.

Primary influences include:

- information before interface
- relationships before navigation
- concepts before components
- understanding before presentation

MDL intentionally extends these concepts into runtime composition.

---

# Knowledge Representation

MDL increasingly treats entertainment as structured knowledge rather than interface objects.

Key influences include:

- entities
- relationships
- semantic meaning
- graph thinking

These ideas are expected to mature significantly within future specifications.

MDL intentionally avoids prescribing implementation technologies for these concepts.

---

# Systems Thinking

The Mental Model intentionally adopts systems thinking rather than feature thinking.

Examples include:

- World instead of Homepage
- Composition instead of Layout
- Information instead of Widgets
- Relationships instead of Navigation

This approach encourages reusable conceptual systems rather than isolated interface features.

---

# Software Architecture

Although MDL intentionally avoids implementation details, the following architectural disciplines influenced its structure.

- Domain-Driven Design
- Event-Driven Systems
- Information Architecture
- Separation of Concerns
- Architecture Decision Records

These references informed documentation structure rather than product philosophy.

---

# Design Systems

The following design systems influenced the organisation of MDL.

## Apple Human Interface Guidelines

Influenced:

- philosophy-first thinking
- experience-first design
- restraint

Not adopted:

- visual language
- interaction model

---

## Material Design

Influenced:

- systematic documentation
- design token hierarchy

Not adopted:

- material metaphor
- interaction philosophy

---

## Fluent Design

Influenced:

- adaptive thinking
- cross-device consistency

Not adopted:

- visual identity

---

# Mosaic-Specific Influences

The Mental Model emerged directly from founder discovery workshops.

Major conceptual discoveries included:

- World
- Focus
- Context
- Information
- Relationships
- Composition
- Expressions

These concepts intentionally replaced earlier terminology centred around:

- pages
- widgets
- dashboards
- cards

This evolution represents one of the defining characteristics of the Mosaic Design Language.

---

# Normative References

The following specifications should be considered required reading before contributing to MDL-003.

- MDL-001 Vision
- MDL-002 Principles

Future specifications should reference MDL-003 rather than redefining its concepts.

---

# Informative References

Future contributors may also wish to review:

- MDS-003 Composition Engine
- MDS-007 Tile Framework
- MDS-011 Extension Design Specification

These documents provide implementation guidance for the conceptual architecture established here.

---

# Living Document

This reference list should remain concise.

References should only be added when they have materially influenced:

- conceptual architecture
- terminology
- governance
- design reasoning

The purpose of this document is to preserve architectural context rather than create an exhaustive bibliography.

---

# Completion

This concludes **MDL-003 — Mental Model**.

The next specification in the Mosaic Design Language is:

> **MDL-004 — Interaction Model**

Where MDL-003 defines **how Mosaic understands the world**, MDL-004 defines **how that world behaves over time**.

It formalises concepts including:

- continuity
- transitions
- adaptive behaviour
- composition evolution
- movement
- temporal interaction

MDL-004 transforms understanding into behaviour.
