<!--
File: docs/design/language/mdl-001-vision/glossary.md
Document: MDL-001
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines terminology specific to the Mosaic Design Language.

Many of these terms deliberately differ from traditional UI or design system vocabulary.

Future specifications should reference these definitions rather than redefining terminology.

Where a term is defined here, that definition takes precedence throughout the MDL and MDS.

Maintaining a controlled glossary helps ensure consistent communication between designers, engineers and contributors.  [oai_citation:0‡W3C](https://www.w3.org/WAI/WCAG22/Techniques/general/G62?utm_source=chatgpt.com)

---

# A

## Adaptive

The ability for an experience to reorganise itself in response to user context while preserving understanding.

Adaptive does **not** mean unpredictable.

---

## Atmosphere

The emotional tone of a composition.

Atmosphere is influenced primarily by entertainment artwork while remaining constrained by the Mosaic Material System.

Atmosphere never replaces brand identity.

---

# C

## Companion

The primary behavioural metaphor of Mosaic.

A companion quietly assists the user, provides useful context and then steps aside.

Mosaic should never behave like a salesperson, dashboard or recommendation engine.

---

## Composition

The current arrangement of information presented around a user's focus.

Unlike a page, a composition evolves over time.

Compositions reorganise.

Pages navigate.

---

## Context

The user's current activity.

Examples include:

- watching an episode
- reading a novel
- listening to an album

Context determines relevance.

Context never permanently restricts exploration.

---

# D

## Domain

A major category of entertainment.

Examples include:

- Television
- Anime
- Books
- Films
- Music

Domains may contain multiple compositions.

Moving within a domain should generally feel less disruptive than moving between domains.

---

# E

## Enhancement

Providing additional value that deepens an existing experience.

Examples include:

- next episode information
- soundtrack
- source material
- production notes

Enhancement differs from persuasion.

---

# F

## Focus

The entertainment currently deserving primary attention.

Every composition has one current focus.

Focus changes naturally over time.

Changing focus should cause the composition to evolve.

---

# I

## Immersion

The reduction of mental effort required to remain inside an entertainment experience.

Immersion is the primary optimisation target of the Mosaic Design Language.

---

## Information

A discrete piece of knowledge about the user's entertainment.

Examples include:

- watch progress
- chapter progress
- release date
- rating
- cast member

Future specifications may treat information as the primary architectural unit from which interfaces are composed.

---

# M

## Material

A visual surface used by Mosaic to communicate hierarchy.

Examples are defined within the Mosaic Design System.

Materials communicate structure.

Artwork communicates emotion.

---

## Mental Model

The conceptual understanding users develop about how Mosaic works.

The Mosaic mental model intentionally centres around:

World

↓

Focus

↓

Context

↓

Composition

rather than pages and navigation.

---

# P

## Persuasion

Attempting to redirect attention towards different entertainment.

Persuasion is intentionally outside the scope of the core Mosaic experience.

---

## Principle

A decision-making rule.

Principles are derived from the philosophy established within MDL-001.

They help contributors choose between competing solutions.

---

# R

## Relationship

A meaningful connection between pieces of entertainment or information.

Examples include:

- adaptation
- sequel
- soundtrack
- author
- cast
- franchise

Relationships provide context.

Future specifications are expected to formalise relationship modelling further.

---

# T

## Tile

The visual representation of information within a composition.

Tiles are not the information itself.

They are one possible expression of that information.

Tiles may adapt in:

- size
- emphasis
- placement

while preserving their identity.

---

## Trusted Companion

The intended personality of Mosaic.

Characteristics include:

- knowledgeable
- calm
- friendly
- sophisticated
- respectful

This metaphor should guide future design decisions.

---

# W

## World

The user's complete entertainment universe.

A world consists of:

- collections
- history
- interests
- relationships
- current focus

The interface should communicate the user's world rather than isolated libraries.

---

# Cross References

| Specification | Primary Terms |
|--------------|---------------|
| MDL-002 Principles | Context, Companion, Immersion |
| MDL-003 Mental Model | World, Focus, Composition |
| MDL-004 Interaction Model | Composition, Tile, Domain |
| MDL-005 Composition Model | Tile, Material, Relationship |
| MDS Specifications | Material, Atmosphere, Adaptive |

---

# Glossary Maintenance

This glossary is expected to evolve throughout the lifetime of Mosaic.

New terms should only be introduced when:

- existing terminology cannot accurately describe a concept
- the concept is expected to appear across multiple specifications
- the definition improves consistency

Terminology should remain stable once established.

Renaming core concepts should require a formal design review.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`