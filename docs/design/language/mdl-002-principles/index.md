<!--
File: docs/design/language/mdl-002-principles/index.md
Document: MDL-002
Status: Draft
Version: 0.1
-->

# MDL-002 — Principles

> *A design language without principles becomes a style guide.*

---

## Purpose

MDL-001 defines **why** Mosaic exists.

MDL-002 defines **how decisions are made**.

This specification establishes the principles that govern every future design, engineering and product decision within Mosaic.

Unlike implementation guidance, principles should remain relatively stable throughout the lifetime of the platform.

Whenever contributors disagree about a design decision, these principles should be used as the primary decision-making framework.

---

## Relationship to MDL-001

The hierarchy of the Mosaic Design Language is intentional.

```
Vision

↓

Beliefs

↓

Principles

↓

Mental Model

↓

Interaction Model

↓

Composition Model

↓

Design System

↓

Implementation
```

Every principle defined within this specification should be directly traceable back to the philosophy established by **MDL-001 Vision**.

Principles do not exist independently.

They are practical expressions of the Mosaic vision.

---

# Scope

This specification defines:

- Design principles
- Decision hierarchy
- Principle ownership
- Principle governance
- Principle application
- Design trade-offs

This specification intentionally does **not** define:

- Components
- Motion
- Colours
- Typography
- Materials
- Layouts
- Tokens

These belong to later MDL and MDS specifications.

---

# Structure

This specification contains:

- 00 Document Control
- 01 What Is A Principle?
- 02 Principle Hierarchy
- 03 Context Before Prediction
- 04 Enhancement Before Persuasion
- 05 Content Leads
- 06 Movement Preserves Understanding
- 07 Every Feature Earns Its Place
- 08 The Platform Enables
- 09 Respect The User's Flow
- 10 Be A Companion
- 11 Applying Principles
- 12 Governance
- 13 ADRs
- 14 Contributor Guidance
- 15 Review Checklist
- Glossary
- References

---

# The Seven Principles

The Mosaic Design Language is currently governed by seven core principles.

1. Context Before Prediction
2. Enhancement Before Persuasion
3. Content Leads
4. Movement Preserves Understanding
5. Every Feature Earns Its Place
6. The Platform Enables
7. Be A Companion

These principles intentionally describe behaviour rather than appearance.

A contributor should be able to apply them whether designing:

- a backend service
- a plugin
- a GraphQL schema
- a mobile client
- a television interface
- an administration page

---

# Design Philosophy

Every principle exists to answer a simple question:

> **When there are two good solutions, which one is more Mosaic?**

Without principles, design discussions become subjective.

With principles, contributors gain a common framework for evaluating proposals.

The objective is not agreement.

The objective is consistency.

---

# Dependencies

```
MDL-001 Vision

↓

MDL-002 Principles

↓

MDL-003 Mental Model

↓

MDL-004 Interaction Model

↓

MDL-005 Composition Model
```

MDL-002 is required reading before implementing any future MDL or MDS specification.

---

# Repository Structure

```
design/

└── mdl/

    └── MDL-002 Principles/

        README.md

        00-document-control.md

        01-what-is-a-principle.md

        02-principle-hierarchy.md

        03-context-before-prediction.md

        04-enhancement-before-persuasion.md

        05-content-leads.md

        06-movement-preserves-understanding.md

        07-every-feature-earns-its-place.md

        08-the-platform-enables.md

        09-respect-the-users-flow.md

        10-be-a-companion.md

        11-applying-principles.md

        12-governance.md

        13-adrs.md

        14-contributor-guidance.md

        15-design-review-checklist.md

        glossary.md

        references.md
```

---

# Review Status

**Status**

Draft

**Owner**

Lead Design Systems Architect

**Next File**

`00-document-control.md`
