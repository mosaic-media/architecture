<!--
File: docs/design/language/mdl-002-principles/glossary.md
Document: MDL-002
Status: Draft
-->

# Glossary

---

# Purpose

This glossary defines terminology introduced by **MDL-002 Principles**.

Definitions contained within this document supplement the Platform foundation glossary established in **[MDL-001 — Mosaic Design Language Vision](../mdl-001-vision/index.md)**.

Where duplicate terms exist, the definition contained within the most specialised specification should take precedence for that specification only.

Terminology is considered part of the Mosaic Design Language.

Changing terminology changes how contributors think.

For this reason, terminology should evolve deliberately rather than organically. Design systems benefit from maintaining a shared vocabulary because consistent language leads to more consistent decision-making across design and engineering teams.  [Design System University](https://designsystem.university/glossary)

---

# A

## Anti-pattern

A solution that appears useful in isolation but consistently produces poorer outcomes when adopted repeatedly.

Anti-patterns exist to teach contributors what **not** to build.

Every principle should document its own anti-patterns.

---

# C

## Capability

A piece of functionality provided by either the Mosaic Platform foundation or a module.

Capabilities describe *what* the system can do.

They intentionally avoid describing *how* that capability is presented.

---

## Cognitive Cost

The amount of mental effort required to understand or operate part of the interface.

Every feature increases cognitive cost.

Good design ensures that the value introduced by a feature exceeds the additional cognitive effort required to use it.

---

## Companion

The primary behavioural metaphor for Mosaic.

A companion:

- understands context
- offers useful assistance
- respects attention
- remains trustworthy
- disappears when no longer needed

The companion is **not**:

- promotional
- persuasive
- attention seeking
- intrusive

---

## Context

The user's current entertainment activity.

Context is temporary.

Context changes naturally.

Context should never permanently define the user.

Context is considered a stronger design signal than behavioural prediction.

---

# D

## Decision Hierarchy

The ordered structure used to resolve design questions.

Within MDL:

```mermaid
flowchart TD

N1["Vision"]
N2["Beliefs"]
N3["Principles"]
N4["Mental Model"]
N5["Interaction"]
N6["Composition"]
N7["Implementation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Higher levels always possess greater authority.

---

## Design Debt

Long-term complexity introduced through inconsistent design decisions.

Examples include:

- duplicated concepts
- competing terminology
- inconsistent interaction models
- unnecessary exceptions

Design debt should be treated with the same seriousness as technical debt.

---

# E

## Enhancement

Information or functionality that deepens the user's existing entertainment experience.

Examples include:

- release information
- chapter progress
- related works
- soundtrack information

Enhancement strengthens current context.

---

# F

## Feature

A user-facing capability.

Within MDL, a feature is **not** automatically considered valuable.

Every feature must justify:

- user value
- cognitive cost
- long-term maintenance
- consistency

before becoming part of Mosaic.

---

# I

## Immersion

The reduction of mental effort required to remain focused upon entertainment.

Immersion is considered the primary optimisation target of Mosaic.

---

# P

## Persuasion

Behaviour intended to redirect attention towards unrelated entertainment.

Examples include:

- trending content
- promoted releases
- engagement feeds
- popularity rankings

Persuasion is intentionally outside the scope of the Platform foundation Mosaic experience.

---

## Platform

The stable collection of systems that support every Mosaic experience.

Examples include:

- authentication
- playback
- composition
- navigation
- accessibility
- module framework

The platform provides capability.

It should avoid solving highly specialised problems that naturally belong within modules.

---

## Principle

A durable decision-making rule.

Unlike implementation guidance, principles remain largely stable over time.

Principles explain **how** Mosaic chooses between competing solutions.

---

# R

## Review Question

A question used during design reviews to determine whether a proposal aligns with MDL.

Review questions intentionally reference principles rather than implementation details.

---

# S

## System

A reusable solution capable of supporting many future features.

Examples include:

- Composition Engine
- Progress System
- Navigation System

Systems are preferred over isolated feature implementations.

---

# T

## Technology Independence

The expectation that MDL remains valid regardless of implementation technology.

The design language should survive changes in:

- programming language
- rendering engine
- framework
- frontend architecture

---

## Traceability

The ability to explain why a design decision exists.

Every significant implementation should be traceable through:

Implementation

↓

MDS

↓

MDL Principles

↓

MDL Vision

Traceability is considered a quality attribute of the Mosaic Design Language.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| [MDL-001 — Mosaic Design Language Vision](../mdl-001-vision/index.md) | Vision, Beliefs, Companion |
| [MDL-003 — Mental Model](../mdl-003-mental-model/index.md) | World, Focus, Context |
| [MDL-004 — Interaction Model](../mdl-004-interaction-model/index.md) | Behaviour, Movement |
| [MDL-005 — Composition Model](../mdl-005-composition-model/index.md) | Composition, Hierarchy |
| MDS Specifications | Systems, Components, Tokens |

---

# Glossary Governance

New terminology should only be introduced when:

- an existing term cannot adequately describe a concept,
- the concept appears across multiple specifications,
- the new terminology simplifies future discussion.

Terminology should remain stable once established.

Renaming a foundational concept should require:

- Design Review
- ADR
- Specification update

This ensures contributors continue sharing a common language over the lifetime of the project.
