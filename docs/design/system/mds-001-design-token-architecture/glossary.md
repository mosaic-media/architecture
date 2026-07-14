<!--
File: docs/design/system/mds-001-design-token-architecture/glossary.md
Document: MDS-001
Title: Glossary
Status: Draft
Version: 0.2
-->

# Glossary

---

# Purpose

This glossary defines the architectural terminology introduced by **MDS-001 — Design Token Architecture**.

Unlike previous MDL glossaries, this document focuses on implementation concepts rather than product concepts.

These definitions should be considered normative throughout every future MDS specification.

---

# C

## Composition Token

A token describing the compositional role of an element.

Composition Tokens communicate:

- hierarchy
- importance
- behavioural responsibility

They intentionally avoid communicating physical implementation.

Examples include:

- Hero
- Supporting
- Anchor
- Peripheral

---

## Component Token

A token consumed directly by a reusable interface component.

Component Tokens inherit semantic meaning rather than defining it.

They should rarely reference Primitive Tokens directly.

---

# I

## Inheritance

The architectural process through which one token derives meaning from another.

Inheritance should always flow downward through the token hierarchy.

Meaning accumulates.

Responsibilities remain separated.

---

# P

## Platform Token

A platform-specific implementation generated from resolved Runtime Tokens.

Examples include:

- CSS variables
- Flutter ThemeData
- SwiftUI Environment values
- Compose theme objects

Platform Tokens are generated artefacts.

They are not authored manually.

---

## Primitive Token

A token representing a measurable physical value.

Examples include:

- colour
- spacing
- blur
- elevation
- radius

Primitive Tokens intentionally contain no semantic meaning.

---

# R

## Resolution

The deterministic process through which a token becomes a concrete implementation value.

Resolution evaluates:

- Semantic meaning
- Composition
- Runtime inputs
- Accessibility
- Platform

before producing a renderable value.

---

## Runtime Token

A dynamically resolved token representing the current runtime environment.

Examples include:

- Atmosphere
- Device
- Accessibility
- Current Focus

Runtime Tokens never redefine semantic meaning.

They only refine implementation.

---

# S

## Semantic Token

A token representing design intent independently from implementation.

Examples include:

- Surface.Primary
- Text.Secondary
- Action.Primary
- Border.Subtle

Applications should consume Semantic Tokens rather than Primitive Tokens whenever possible.

---

# T

## Theme

A mapping between Semantic Tokens and Primitive Tokens.

Themes alter implementation.

They should never alter semantic intent.

---

## Token

The smallest implementation unit capable of expressing a design decision independently from implementation technology.

Tokens communicate intent before values.

---

## Token Hierarchy

The ordered architectural structure of the Design Token Architecture.

```
Primitive

↓

Semantic

↓

Composition

↓

Component

↓

Runtime

↓

Presentation
```

Each layer contributes one responsibility.

---

## Token Resolution

The runtime process responsible for converting abstract tokens into platform-specific implementation values.

Resolution should remain deterministic and invisible to application code.

---

## Token Drift

The gradual weakening of the Design Token Architecture through:

- duplicate semantics
- implementation leakage
- inconsistent naming
- incorrect layering

Token Drift is considered architectural debt.

---

## Token Debt

Accumulated architectural complexity caused by poor token design.

Examples include:

- duplicated tokens
- unnecessary aliases
- Primitive consumption
- undocumented Runtime Tokens

Token Debt should be reduced continuously.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| MDL-001 Vision | Product Philosophy |
| MDL-002 Principles | Design Intent |
| MDL-003 Mental Model | World, Information |
| MDL-004 Interaction Model | Behaviour |
| MDL-005 Composition Model | Hierarchy, Composition |
| MDS-002 Material System | Semantic Consumption |
| MDS-006 Composition Engine | Runtime Resolution |

---

# Terminology Rules

Future contributors should:

- describe meaning before values
- describe semantics before implementation
- consume higher-level tokens whenever practical
- avoid platform-specific terminology within architectural specifications

The Design Token Architecture should remain understandable independently from any implementation technology.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
