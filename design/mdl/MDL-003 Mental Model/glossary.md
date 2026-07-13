<!--
File: design/mdl/MDL-003 Mental Model/glossary.md
Document: MDL-003
Title: Glossary
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines the conceptual terminology introduced by **MDL-003 — Mental Model**.

Unlike implementation terminology, these definitions describe concepts that should remain stable regardless of:

- programming language
- frontend framework
- storage engine
- rendering technology
- client platform

Every future MDL and MDS specification should use these definitions consistently.

Terminology is considered part of the architecture of the Mosaic Design Language.

---

# C

## Composition

The intentional organisation of Information that communicates the user's current World with the least possible cognitive effort.

Composition determines:

- hierarchy
- emphasis
- grouping
- importance

Composition does **not** determine presentation.

---

## Context

The temporary circumstances surrounding the user's current Focus.

Context answers:

> Why does this matter now?

Context determines relevance.

Context changes continuously.

---

# D

## Domain

A major category of entertainment existing within a World.

Examples include:

- Television
- Anime
- Movies
- Books
- Music

Domains organise entertainment.

They do not fragment the World.

---

# E

## Expression

The conceptual communication pattern selected by the Composition.

Expressions are independent from components.

Examples include:

- Timeline
- Progress
- Hero Detail
- Metadata
- Notification

Expressions are later rendered through Presentation.

---

# F

## Focus

The entertainment experience currently deserving the user's primary attention.

Focus answers:

> What currently matters?

Every World normally possesses one primary Focus.

---

# I

## Information

A meaningful piece of knowledge describing the user's entertainment world.

Examples include:

- progress
- release date
- runtime
- author
- cast
- rating

Information exists independently from interface.

---

# M

## Mental Model

The conceptual explanation of how Mosaic understands the user's entertainment world.

The Mental Model intentionally hides implementation architecture from users.

---

# P

## Presentation

The physical rendering of an Expression using the capabilities of a specific platform.

Presentation includes:

- Tiles
- Materials
- Typography
- Motion
- Layout

Presentation should never redefine meaning.

---

# R

## Relationship

A meaningful connection between two or more pieces of Information.

Relationships transform information into understanding.

Examples include:

- adaptation
- sequel
- soundtrack
- author
- actor
- franchise

---

# W

## World

The highest-level concept within Mosaic.

A World represents the user's complete entertainment environment.

Everything else exists inside a World.

A World is not:

- a homepage
- a library
- a dashboard

It is the conceptual environment experienced by the user.

---

# Conceptual Hierarchy

The Mental Model is intentionally hierarchical.

```text
World

↓

Focus

↓

Context

↓

Information

↓

Relationships

↓

Composition

↓

Expressions

↓

Presentation
```

Every concept builds upon the one before it.

---

# Terminology Rules

Future contributors should:

- reuse existing concepts before introducing new ones.
- avoid implementation terminology within MDL.
- preserve conceptual consistency across all specifications.
- favour user language over engineering language.

Concepts should only be renamed through formal design review.

---

# Review Status

**Status**

Draft

**Next File**

`references.md`
