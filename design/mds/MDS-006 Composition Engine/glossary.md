<!--
File: design/mds/MDS-006 Composition Engine/glossary.md
Document: MDS-006
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines the terminology introduced by **MDS-006 — Composition Engine**.

Unlike previous glossaries, these definitions describe the runtime architecture responsible for constructing the user's World.

These terms intentionally remain independent from:

- UI frameworks,
- rendering engines,
- platforms,
- programming languages.

Future specifications should reuse these definitions consistently.

---

# A

## Adaptive Layout

The runtime process that projects one solved Composition into different presentation environments.

Adaptive Layout changes:

- spatial organisation,
- density,
- presentation.

It never changes:

- behaviour,
- hierarchy,
- understanding.

---

# B

## Behaviour Orchestration

The coordinated execution of every runtime subsystem following behavioural change.

Behaviour Orchestration ensures:

- Composition,
- Materials,
- Typography,
- Motion,

all evolve together.

---

# C

## Composition

The solved understanding of the user's current World.

Composition exists independently from:

- layouts,
- components,
- rendering.

---

## Composition Solver

The deterministic runtime system responsible for transforming the Runtime World into a solved Composition.

The Solver determines:

- hierarchy,
- priority,
- grouping,
- Expressions.

It never determines rendering.

---

# E

## Expression

A runtime representation of one conceptual responsibility.

Examples include:

- Hero
- Timeline
- Progress
- Relationships
- Actions

Expressions are presentation independent.

---

## Expression Resolution

The deterministic process that transforms solved Composition into reusable runtime Expressions.

Expression Resolution bridges runtime understanding and presentation.

---

# H

## Hierarchy Profile

A conceptual runtime artefact representing the resolved behavioural hierarchy of the current Composition.

Hierarchy Profiles improve:

- determinism,
- caching,
- incremental updates.

---

# P

## Presentation Model

The platform-independent runtime description consumed by rendering engines.

The Presentation Model contains:

- Expressions,
- Materials,
- Typography,
- Motion,
- Interaction metadata.

Components are generated afterwards.

---

# R

## Runtime World

The continuously evolving behavioural model representing the user's current reality.

The Runtime World is the single source of truth for:

- Focus,
- Context,
- Behaviour,
- Relationships.

Every runtime subsystem consumes it.

---

## Runtime Pipeline

A deterministic execution stage within the Composition Engine.

Pipelines transform:

Behaviour

↓

Understanding

↓

Presentation

Each pipeline owns one architectural responsibility.

---

## Runtime Snapshot

An immutable representation of the Runtime World used during one orchestration cycle.

Snapshots improve:

- replay,
- testing,
- caching,
- deterministic execution.

---

# S

## Solver

See **Composition Solver**.

Within Mosaic, "Solver" always refers to runtime understanding rather than layout computation.

---

# W

## World

The user's current behavioural reality.

A World contains:

- Focus,
- Context,
- Relationships,
- Behaviour,
- Information.

The Composition Engine continuously solves this World into understandable presentation.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| MDL-001 Vision | Companion |
| MDL-002 Principles | Behaviour First |
| MDL-003 Mental Model | World, Focus |
| MDL-004 Interaction Model | Behaviour |
| MDL-005 Composition Model | Hero, Hierarchy |
| MDS-001 Design Token Architecture | Runtime Resolution |
| MDS-002 Colour System | Runtime Atmosphere |
| MDS-003 Material System | Material Resolution |
| MDS-004 Typography System | Editorial Hierarchy |
| MDS-005 Motion System | Behavioural Motion |

---

# Terminology Rules

Future contributors should:

- describe Worlds before screens,
- describe behaviour before rendering,
- describe Expressions before components,
- distinguish Composition from presentation,
- avoid platform-specific terminology inside architectural specifications.

Runtime terminology should remain independent from implementation technology.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
