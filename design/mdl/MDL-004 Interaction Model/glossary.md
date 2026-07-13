<!--
File: design/mdl/MDL-004 Interaction Model/glossary.md
Document: MDL-004
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines the behavioural terminology introduced by **MDL-004 — Interaction Model**.

Unlike the glossary contained within **MDL-003**, which defines conceptual objects, this glossary defines behavioural concepts.

These terms should be used consistently throughout every future MDL and MDS specification.

Behavioural terminology is considered part of the Mosaic Design Language.

Changing terminology changes how contributors think about interaction.

---

# B

## Behaviour

The observable evolution of the user's World over time.

Behaviour exists independently from implementation.

Behaviour answers:

> **What should happen?**

Implementation answers:

> **How does it happen?**

---

## Behavioural Continuity

The preservation of understanding as the user's World changes.

Continuity is considered one of the primary objectives of the Interaction Model.

---

## Behavioural Weight

A conceptual measure of how significant an interaction is.

Weight is determined by conceptual change rather than visual change.

Example.

```
Episode

↓

Next Episode
```

Low weight.

```
Anime

↓

Books
```

High weight.

Behavioural weight influences future composition and motion systems.

---

# C

## Composition Evolution

The continuous refinement of a Composition as the user's World changes.

Unlike page replacement, Composition Evolution preserves continuity.

---

## Context Transition

A behavioural transition in which Context changes while Focus may remain the same.

Context Transitions are expected to occur significantly more frequently than Focus Transitions.

---

## Continuity

The preservation of user understanding throughout interaction.

Users should feel they remain inside one evolving World rather than repeatedly entering new interfaces.

---

# F

## Focus Transition

A behavioural transition where the user's primary attention changes from one subject to another.

Focus Transitions should preserve understanding rather than reset it.

---

# I

## Interaction

The behavioural evolution of the user's World in response to:

- user intent
- time
- information
- relationships

Interaction is not synonymous with animation or interface.

---

## Interaction Model

The behavioural architecture governing how concepts defined by the Mental Model evolve over time.

The Interaction Model intentionally remains independent from presentation.

---

## Interaction State

The current behavioural mode of the user's World.

Examples include:

- Watching
- Reading
- Exploring
- Continuing
- Managing

Interaction States describe behaviour rather than interface.

---

# L

## Local Evolution

Behavioural changes affecting only the relevant portion of the current Composition.

Local evolution preserves continuity by avoiding unnecessary global reorganisation.

---

# M

## Movement

The communication of behavioural change.

Movement exists to explain:

- continuity
- hierarchy
- progression
- understanding

Movement is not decoration.

---

# P

## Progressive Evolution

A behavioural strategy in which significant changes occur through multiple understandable transitions rather than abrupt replacement.

---

# T

## Temporal Behaviour

Behaviour driven by the passage of time rather than direct user interaction.

Examples include:

- episode releases
- scheduled events
- countdown completion
- background updates

Temporal Behaviour allows the World to evolve naturally while users are absent.

---

## Transitional State

A short-lived Interaction State existing only to support another state.

Examples include:

- Preparing Playback
- Searching
- Authenticating

Transitional States should never become destinations.

---

# U

## User Behaviour

Behaviour originating from user intention.

Examples include:

- Continue Watching
- Resume Reading
- Explore Cast

User Behaviour defines goals.

It does not define implementation.

---

# S

## System Behaviour

Behaviour performed internally by the platform in order to support User Behaviour.

Examples include:

- Composition recalculation
- Relationship updates
- Information processing

System Behaviour should remain largely invisible.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| MDL-001 Vision | Companion, Immersion |
| MDL-002 Principles | Behavioural Decision Making |
| MDL-003 Mental Model | World, Focus, Context |
| MDL-005 Composition Model | Composition Behaviour |
| MDS Motion System | Behaviour Communication |

---

# Terminology Rules

Future contributors should:

- describe behaviour before interface
- prefer conceptual terminology over implementation terminology
- avoid framework-specific language
- preserve behavioural consistency across specifications

Interaction terminology should remain stable throughout the lifetime of the Mosaic Design Language.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
