<!--
File: design/mdl/MDL-003 Mental Model/01-what-is-a-mental-model.md
Document: MDL-003
Chapter: 01
Title: What Is A Mental Model?
Status: Draft
Version: 0.1
-->

# What Is A Mental Model?

---

# Purpose

Before defining the concepts that exist within Mosaic, contributors must first understand what a mental model is and why it matters.

The purpose of this chapter is to establish a shared understanding of the role the Mental Model plays within the Mosaic Design Language.

Without a common conceptual model, contributors naturally invent their own.

Those individual interpretations eventually become inconsistent interfaces, inconsistent APIs and inconsistent experiences.

The Mental Model exists to prevent that fragmentation.

---

# Definition

Within the Mosaic Design Language, a **Mental Model** is:

> **The conceptual explanation of how Mosaic understands the user's world.**

It is intentionally independent from:

- user interface
- implementation
- programming language
- framework
- database
- network protocol

The Mental Model defines concepts.

Implementation expresses those concepts.

---

# Why Mental Models Exist

Every user forms an internal explanation of how software works.

This explanation is rarely technically accurate.

It does not need to be.

It simply needs to be:

- consistent
- predictable
- understandable

People successfully use cars without understanding combustion engines.

People successfully use electricity without understanding electrical engineering.

Likewise, Mosaic users should successfully use the platform without understanding GraphQL, plugins or runtime composition.

They should understand only the concepts required to accomplish their goals.

Mental models are a recognised UX concept describing the internal explanation users construct to predict how a system behaves. Good products align the system model with the user's mental model to reduce confusion and cognitive effort. (Norman, *The Design of Everyday Things*.)

---

# System Model vs Mental Model

Every software product contains two models.

## System Model

The technical reality.

Examples include:

- GraphQL
- SQLite
- DuckDB
- WebSockets
- Plugins
- Composition Engine

The system model belongs to engineers.

---

## Mental Model

The conceptual reality.

Examples include:

- World
- Focus
- Context
- Relationships
- Progress
- Companion

The mental model belongs to users.

---

These models intentionally differ.

The purpose of design is to translate one into the other.

---

# A Bad Mental Model

Imagine a media application whose navigation is organised around:

```
Media

↓

Series

↓

Season

↓

Episode

↓

Playback
```

Internally this may accurately describe the database.

From the user's perspective it introduces unnecessary concepts.

The user is forced to understand software architecture rather than entertainment.

---

# A Better Mental Model

Mosaic instead proposes:

```
My World

↓

My Current Focus

↓

What Helps Me Right Now
```

This is significantly closer to how people naturally describe entertainment.

Notice that:

- databases disappear
- APIs disappear
- plugins disappear
- implementation disappears

Only meaningful concepts remain.

---

# Mental Models Are Not Navigation

A common mistake is assuming that the Mental Model describes interface layout.

It does not.

Navigation is one possible expression of the Mental Model.

So are:

- composition
- search
- recommendations
- playback
- administration
- notifications

Every part of Mosaic should reinforce the same conceptual understanding.

---

# Mental Models Are Stable

Implementation changes frequently.

Mental models should not.

Changing the Mental Model requires contributors to relearn how the product works.

This is one of the most expensive forms of design change.

Consequently:

- components may evolve
- composition may evolve
- rendering may evolve

The conceptual model should evolve only when significant evidence demonstrates that it no longer reflects the intended experience.

---

# The Cost Of Multiple Mental Models

Products often become inconsistent because different teams unknowingly build different conceptual models.

Examples include:

Search Team:

> Mosaic is a search application.

Playback Team:

> Mosaic is a media player.

Library Team:

> Mosaic is a database.

Plugin Team:

> Mosaic is an extension host.

Each statement is partially true.

None describes the complete product.

MDL-003 exists so every team begins from the same understanding.

---

# The Mosaic Mental Model

The conceptual model of Mosaic is intentionally human rather than technical.

The user does not experience:

```
Database

↓

API

↓

Renderer
```

They experience:

```
My World

↓

What I'm Enjoying

↓

What Helps Me Continue
```

Everything implemented by Mosaic should reinforce this understanding.

---

# The Test

A contributor should be capable of explaining Mosaic to a non-technical family member without mentioning:

- GraphQL
- APIs
- plugins
- databases
- servers
- rendering

If that explanation remains accurate...

The Mental Model is working.

---

# Relationship To The Remaining Specification

The remaining chapters progressively define the concepts that make up the Mosaic Mental Model.

Beginning with:

```
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

Every later chapter builds upon the previous one.

No concept should be understood in isolation.

---

# Summary

The Mental Model is the conceptual architecture of Mosaic.

It describes:

- what exists
- why it exists
- how those concepts relate

without describing how any of them are implemented.

Every interface, API and future extension should reinforce this same conceptual understanding.

---

# Review Status

**Status**

Draft

**Next File**

`02-the-world.md`
