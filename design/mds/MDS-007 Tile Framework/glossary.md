<!--
File: design/mds/MDS-007 Tile Framework/glossary.md
Document: MDS-007
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines the terminology introduced by **MDS-007 — Tile Framework**.

Unlike previous glossaries, these definitions describe the presentation abstraction layer that exists between runtime understanding and rendered components.

These definitions should remain stable regardless of:

- rendering technology,
- UI framework,
- platform,
- device.

Future specifications should reuse these definitions consistently.

---

# A

## Adaptive Tile

A Tile capable of altering its physical presentation while preserving behavioural identity.

Adaptive Tiles change:

- layout,
- density,
- interaction,
- presentation.

They never change:

- behaviour,
- meaning,
- runtime identity.

---

# C

## Collection Tile

A Tile representing an organised behavioural group of related content.

Examples include:

- Continue Watching,
- Library,
- Recently Added,
- Favourites.

Collections communicate organisation rather than hierarchy.

---

## Content Tile

A Tile representing an individual content object.

Examples include:

- film,
- episode,
- chapter,
- album,
- book.

Content Tiles become important through Runtime Hierarchy rather than Tile identity.

---

# E

## Expression Mapping

The deterministic process through which Expressions become Tile identities.

Expression Mapping preserves behavioural meaning while remaining independent from rendering technology.

---

## Extension Tile

A standard Mosaic Tile produced from an extension-provided Expression.

Extensions never define Tile behaviour directly.

The Tile Framework remains responsible for presentation.

---

# H

## Hero Tile

The Tile representing the current behavioural centre of the user's World.

Hero Tiles inherit:

- Hero Material,
- Hero Typography,
- Hero Motion.

Only one Hero Tile normally exists within a Composition.

---

# M

## Metadata Tile

A Tile communicating supporting information.

Examples include:

- runtime,
- codec,
- language,
- release year.

Metadata Tiles remain behaviourally quiet.

---

# O

## Overlay Tile

A temporary Tile supporting interaction.

Examples include:

- search,
- playback controls,
- command palettes,
- menus.

Overlay Tiles inherit Overlay Materials and Overlay Motion.

---

# P

## Presentation Primitive

A reusable behavioural presentation object independent from rendering implementation.

Within Mosaic, Tiles are presentation primitives.

Components are not.

---

# R

## Relationship Tile

A Tile communicating behavioural relationships.

Examples include:

- recommendations,
- cast,
- franchise,
- author.

Relationship Tiles encourage exploration while preserving the user's current World.

---

## Runtime Tile Resolution

The deterministic process that transforms behavioural Tile identities into fully resolved presentation objects.

Runtime Tile Resolution evaluates:

- Materials,
- Typography,
- Motion,
- Accessibility,
- Adaptive behaviour

before components are created.

---

# T

## Tile

A reusable behavioural presentation primitive representing one solved Expression.

Tiles communicate presentation.

They do not communicate rendering implementation.

---

## Tile Composition

The behavioural grouping of multiple Tiles into coherent presentation structures.

Tile Composition follows behavioural relationships rather than layout.

---

## Tile Framework

The architectural layer positioned between Expressions and Components.

The Tile Framework transforms runtime understanding into reusable presentation primitives.

---

## Tile Identity

The stable behavioural identity assigned to every Tile.

Examples include:

- Hero Tile,
- Timeline Tile,
- Metadata Tile.

Tile identity remains stable across:

- devices,
- platforms,
- rendering technologies.

---

## Tile Lifecycle

The behavioural evolution of a Tile through:

- resolution,
- activation,
- evolution,
- retirement,
- release.

Lifecycle follows behaviour.

Not rendering.

---

## Tile Orchestration

The coordinated runtime evolution of every active Tile.

Tile Orchestration ensures presentation evolves as one coherent behavioural experience.

---

## Tile Taxonomy

The canonical behavioural vocabulary of Tile families used throughout Mosaic.

Tile Taxonomy intentionally remains:

- compact,
- reusable,
- presentation independent.

---

## Timeline Tile

A Tile communicating temporal progression.

Examples include:

- playback progress,
- reading progress,
- listening position,
- queue position.

Timeline Tiles communicate continuity rather than raw numerical progress.

---

# U

## Utility Tile

A Tile communicating peripheral system information.

Examples include:

- diagnostics,
- synchronisation,
- storage,
- updates.

Utility Tiles should remain behaviourally secondary.

---

# Cross References

| Specification | Primary Concepts |
|---------------|------------------|
| MDL-001 Vision | Companion |
| MDL-002 Principles | Behaviour Before Interface |
| MDL-003 Mental Model | World |
| MDL-004 Interaction Model | Behaviour |
| MDL-005 Composition Model | Expressions |
| MDS-006 Composition Engine | Runtime World, Expressions, Presentation Model |

---

# Terminology Rules

Future contributors should:

- describe Expressions before Tiles,
- describe Tiles before Components,
- distinguish presentation from rendering,
- distinguish behavioural identity from layout,
- avoid implementation-specific terminology within architectural documentation.

Tile terminology should remain independent from UI frameworks.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
