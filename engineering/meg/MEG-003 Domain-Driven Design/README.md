<!--
File: engineering/meg/MEG-003 Domain-Driven Design/README.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# MEG-003 — Domain-Driven Design

> *Software should model the business. The business should never model the software.*

---

# Purpose

As Mosaic grows, it will encompass many independent business capabilities.

Examples include:

- Libraries
- Metadata
- Playback
- Users
- Authentication
- Extensions
- Collections
- Recommendations
- Books
- Music
- Live TV

Attempting to model all of these concerns within a single unified object model would inevitably produce a tightly coupled, increasingly complex platform.

Domain-Driven Design (DDD) provides the architectural principles required to manage that complexity.

Unlike many implementations of DDD, Mosaic does **not** adopt Domain-Driven Design because it is fashionable.

It adopts DDD because it aligns naturally with:

- Event-Driven Runtime
- Extension-first architecture
- Hexagonal Architecture
- Autonomous capabilities
- Long-term platform evolution

---

# Relationship to MEG

```
MEG-001

↓

Engineering Standards

↓

MEG-002

↓

Reactive Runtime

↓

MEG-003

↓

Business Modelling

↓

MEG-004

↓

Hexagonal Architecture

↓

Implementation
```

MEG-001 explains **how software is written.**

MEG-002 explains **how software executes.**

MEG-003 explains **how the business itself is modelled.**

---

# Scope

This specification defines:

- Domain philosophy
- Ubiquitous language
- Subdomains
- Core domains
- Supporting domains
- Generic domains
- Bounded contexts
- Context maps
- Entities
- Value objects
- Aggregates
- Aggregate roots
- Domain services
- Domain events
- Repositories
- Factories
- Domain invariants

This specification intentionally does **not** define:

- Runtime behaviour
- Event delivery
- Worker execution
- Scheduling
- Transport protocols
- Storage implementation

Those concerns are defined by other MEG specifications.

---

# Core Question

MEG-003 exists to answer one question.

> **How should the Mosaic business domain be modelled so that complexity remains understandable as the platform grows?**

---

# Domain Statement

Within Mosaic:

> **Software should reflect the language of the business, not the language of the implementation.**

The domain model should describe:

- media
- libraries
- playback
- users
- metadata

It should **not** describe:

- controllers
- databases
- HTTP
- workers
- SQL

Business concepts should remain independent of technical concerns.

This is one of the central goals of Domain-Driven Design: creating a shared domain model expressed through a ubiquitous language understood by both domain experts and engineers.  [oai_citation:0‡Google Books](https://books.google.com/books/about/Domain_Driven_Design_Reference.html?id=ccRsBgAAQBAJ&utm_source=chatgpt.com)

---

# Domain Hierarchy

The Mosaic platform intentionally separates domain modelling into conceptual layers.

```
Business Domain

↓

Subdomains

↓

Bounded Contexts

↓

Aggregates

↓

Entities

↓

Value Objects

↓

Implementation
```

Each layer owns exactly one responsibility.

Future chapters define every layer in detail.

---

# Expected Outcome

After reading MEG-003 contributors should understand:

- why Mosaic uses Domain-Driven Design
- how bounded contexts are identified
- how aggregates enforce business invariants
- how entities differ from value objects
- where domain events originate
- how repositories interact with aggregates
- how capabilities align with business domains

without discussing runtime implementation or transport infrastructure.

---

# Repository Structure

```
engineering/

└── meg/

    └── MEG-003 Domain-Driven Design/

        README.md

        00-document-control.md

        01-domain-philosophy.md

        02-ubiquitous-language.md

        03-subdomains.md

        04-bounded-contexts.md

        05-context-maps.md

        06-entities.md

        07-value-objects.md

        08-aggregates.md

        09-aggregate-roots.md

        10-domain-services.md

        11-domain-events.md

        12-repositories.md

        13-factories.md

        14-domain-invariants.md

        15-modelling-guidelines.md

        16-adrs.md

        17-contributor-guidance.md

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MEG-001 Go Engineering Standards
- MEG-002 Event-Driven Runtime
- MDL-002 Principles
- MDL-003 Mental Model

Future companion specifications:

- MEG-004 Hexagonal Architecture
- MEG-005 Extension Platform
- MEG-006 Runtime Architecture

---

# Design Goals

The Domain Model is intended to produce software that is:

- Business focused
- Ubiquitous
- Cohesive
- Evolvable
- Loosely coupled
- Testable
- Expressive
- Independent of infrastructure

The model should become deeper as understanding improves.

It should never become more technical.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Next File**

`00-document-control.md`
