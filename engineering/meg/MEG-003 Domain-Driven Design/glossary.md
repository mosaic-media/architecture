<!--
File: engineering/meg/MEG-003 Domain-Driven Design/glossary.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Glossary

> *A shared model requires a shared language. Every important business term should have one unambiguous meaning.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Domain-Driven Design specification.

The definitions contained within this document establish the canonical business vocabulary for:

- Architecture Specifications
- ADRs
- Source Code
- Documentation
- Extension SDKs
- Technical Discussions

Where a term has a specific meaning within the Mosaic Domain Model, that definition takes precedence over informal usage.

---

# A

## Aggregate

A consistency boundary consisting of:

- one Aggregate Root
- zero or more Entities
- zero or more Value Objects

An Aggregate protects business invariants.

It is persisted as a single unit.

---

## Aggregate Root

The public entry point into an Aggregate.

The Aggregate Root:

- owns business consistency
- protects invariants
- exposes business behaviour
- is the only externally accessible object within the Aggregate

Every Aggregate has exactly one Aggregate Root.

---

# B

## Bounded Context

A boundary within which a Domain Model remains valid.

Every Bounded Context owns:

- language
- business rules
- terminology
- ownership

Different contexts may legitimately model similar concepts differently.

---

## Business Rule

A rule describing valid business behaviour.

Business Rules belong inside the Domain Model.

They do not belong in:

- HTTP
- databases
- repositories
- infrastructure

---

# C

## Context Map

A description of the relationships between Bounded Contexts.

Context Maps identify:

- ownership
- dependency direction
- translation boundaries
- communication mechanisms

They describe architecture.

Not implementation.

---

## Core Domain

The part of the business providing Mosaic's primary competitive advantage.

Core Domains receive the greatest architectural investment.

---

# D

## Domain

The area of knowledge the software exists to model.

Within Mosaic:

```
Media Management
```

is the overall domain.

---

## Domain Event

An immutable record describing a completed business fact.

Domain Events originate inside the Domain Model.

They later become Runtime Events.

---

## Domain Model

The collection of concepts representing the business.

The Domain Model includes:

- Entities
- Value Objects
- Aggregates
- Domain Services
- Domain Events

It intentionally excludes infrastructure.

---

## Domain Service

Business behaviour that belongs to the Domain but belongs naturally to no individual Aggregate.

Domain Services are:

- stateless
- business focused
- behaviour oriented

---

# E

## Entity

A business concept defined by its identity.

Entities:

- possess stable identity
- evolve over time
- own behaviour

Changing state does not change identity.

---

# F

## Factory

A component responsible for constructing valid domain objects.

Factories ensure:

- invariants
- default state
- complete construction

Factories perform creation.

Not business behaviour.

---

# G

## Generic Domain

A supporting capability that does not differentiate the Mosaic platform.

Examples include:

- logging
- configuration
- scheduling

Generic Domains should usually leverage established solutions.

---

# I

## Identity

The stable characteristic that distinguishes one Entity from another.

Identity belongs to the business.

Not the database.

---

## Invariant

A business rule that must always remain true.

Aggregates exist primarily to protect invariants.

---

# P

## Published Language

A stable contract through which Bounded Contexts communicate.

Within Mosaic this is usually expressed through:

- Domain Events
- Runtime Events
- public interfaces

---

# R

## Repository

A persistence abstraction responsible for loading and saving Aggregate Roots.

Repositories hide storage implementation.

They expose business concepts.

---

# S

## Shared Kernel

A shared Domain Model used by multiple Bounded Contexts.

Within Mosaic this pattern is generally discouraged because it increases coupling.

Published contracts are preferred.

---

## Subdomain

A distinct business capability within the larger Domain.

Examples include:

- Playback
- Library
- Metadata
- Search

Each Subdomain owns one coherent area of business responsibility.

---

## Supporting Domain

A business capability that enables the Core Domain but does not define Mosaic's competitive advantage.

Examples include:

- Authentication
- Notifications
- Search

---

# U

## Ubiquitous Language

The shared vocabulary used by:

- engineers
- architects
- product owners
- documentation
- source code

Every business concept should have one canonical meaning within its Bounded Context.

---

# V

## Value Object

A business concept defined entirely by its value.

Value Objects:

- possess no identity
- should be immutable
- may contain behaviour
- reinforce the ubiquitous language

Examples include:

- Duration
- Resolution
- Language

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ACL | Anti-Corruption Layer |
| ADR | Architectural Decision Record |
| DDD | Domain-Driven Design |
| MEG | Mosaic Engineering Guidelines |
| MDS | Mosaic Design Specifications |
| MDL | Mosaic Design Language |
| UBL | Ubiquitous Language |

---

# Relationship to MEG-003

This glossary supports every document within the Domain-Driven Design specification.

Definitions should remain consistent across:

- Domain Models
- Architecture Specifications
- ADRs
- Runtime Specifications
- Extension SDKs
- Contributor Documentation

Whenever the ubiquitous language evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`17-contributor-guidance.md`

**Next File**

`references.md`
