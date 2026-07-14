<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/references.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# References

> *Hexagonal Architecture is not a framework. It is a way of protecting business knowledge from technological change.*

---

# Purpose

This document records the primary references that informed the architectural principles established throughout MEG-004.

Hexagonal Architecture has existed for over two decades.

The Mosaic implementation builds upon those established ideas while adapting them to:

- Event-Driven Runtime
- Domain-Driven Design
- Go Engineering
- Extension-first architecture
- Long-lived software platforms

The purpose of these references is to explain the architectural lineage of the Mosaic platform rather than prescribe implementation.

---

# Primary References

## Hexagonal Architecture (Ports & Adapters)

**Author**

Alistair Cockburn

**Purpose**

The original paper introducing:

- Ports
- Adapters
- Technology independence
- Dependency inversion
- Testable architecture

This paper forms the primary architectural foundation of MEG-004.

The central architectural principle adopted by Mosaic is:

> **The application communicates through Ports while Adapters isolate external technologies.**  [oai_citation:0‡Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture?utm_source=chatgpt.com)

**URL**

https://alistair.cockburn.us/hexagonal-architecture/

---

## Hexagonal Architecture Explained

**Authors**

Alistair Cockburn

Juan Manuel Garrido de Paz

**Purpose**

A modern expansion of the original Ports & Adapters architecture including practical implementation guidance.

Recommended reading for contributors wishing to understand the evolution of Hexagonal Architecture beyond the original article.  [oai_citation:1‡Google Books](https://books.google.com/books/about/Hexagonal_Architecture_Explained.html?id=Eim20AEACAAJ&utm_source=chatgpt.com)

---

# Supporting Architecture References

## AWS Prescriptive Guidance

**Purpose**

Practical guidance for implementing Hexagonal Architecture within modern cloud-native systems.

Topics include:

- dependency isolation
- testability
- replaceable infrastructure
- technology independence

The AWS guidance aligns closely with Mosaic's goal of protecting the Domain from infrastructure concerns.  [oai_citation:2‡AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html?utm_source=chatgpt.com)

---

## Dependency Injection Principles, Practices and Patterns

**Author**

Mark Seemann

**Topics**

- Composition Root
- Dependency Injection
- Dependency Inversion
- object composition

This work strongly influenced:

- explicit composition
- avoidance of service locators
- avoiding dependency injection containers
- constructor injection

Many of the Composition Root principles in MEG-004 derive directly from this body of work.

---

# Domain-Driven Design References

## Domain-Driven Design

**Author**

Eric Evans

Referenced for:

- Bounded Contexts
- Aggregates
- Domain Services
- Repositories
- Domain independence

Although MEG-003 defines the Domain Model, Hexagonal Architecture exists largely to protect that model.

---

## Implementing Domain-Driven Design

**Author**

Vaughn Vernon

Referenced primarily for:

- Application Services
- Repositories
- Aggregate persistence
- Dependency boundaries

Many practical implementation recommendations adopted by Mosaic align with this work.

---

# Software Engineering References

## Clean Architecture

**Author**

Robert C. Martin

Referenced primarily for:

- dependency rule
- policy vs detail
- architectural boundaries

Although Clean Architecture and Hexagonal Architecture differ in presentation, they share the central idea that dependencies point toward business rules.

---

## The Pragmatic Programmer

**Authors**

Andrew Hunt

David Thomas

Referenced for:

- simplicity
- explicitness
- maintainability
- evolutionary design

Many contributor guidelines within the MEG reflect these engineering attitudes.

---

## Refactoring

**Author**

Martin Fowler

Referenced for:

- architectural evolution
- continuous improvement
- incremental design

Architecture should evolve gradually.

Not through wholesale rewrites.

---

# Go References

The Go language naturally complements Hexagonal Architecture.

Recommended references include:

## Effective Go

Topics include:

- interfaces
- package design
- composition
- dependency management

https://go.dev/doc/effective_go

---

## Go Code Review Comments

Topics include:

- interfaces
- package ownership
- naming
- architecture

https://go.dev/wiki/CodeReviewComments

---

## Go Blog

Recommended topics:

- interfaces
- composition
- testing
- dependency management

The implementation should remain idiomatic Go while preserving architectural principles.

---

# Reactive Runtime References

MEG-004 intentionally integrates with MEG-002.

Relevant references include:

- Event-Driven Architecture
- Reactive Systems
- OpenTelemetry
- Enterprise Integration Patterns

The Runtime remains outside the Hexagon.

It communicates with the Domain exclusively through Ports and Adapters.

---

# Internal Mosaic Specifications

The following specifications complement MEG-004.

## Engineering

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design

---

## Planned Engineering Specifications

- MEG-005 Extension Platform
- MEG-006 Runtime Architecture
- MEG-007 Storage Architecture
- MEG-008 Observability
- MEG-009 Security
- MEG-010 Performance Engineering

---

## Mosaic Design Language

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model

---

## Mosaic Design Specifications

- MDS-001 Design Token Architecture
- MDS-002 Colour System
- MDS-003 Material System
- MDS-004 Typography System
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-007 Tile Framework
- MDS-008 Component Library

---

# Architectural Principles

The Hexagonal Architecture established throughout MEG-004 intentionally builds upon several enduring principles.

These include:

- The Domain owns business behaviour.
- Dependencies always point inward.
- Infrastructure remains replaceable.
- Ports belong to the Domain.
- Adapters own technology.
- Composition is explicit.
- Technology is temporary.
- Business knowledge is permanent.
- Testing is a consequence of good architecture.
- Simplicity scales better than cleverness.

These principles should remain considerably more stable than the technologies implementing them.

---

# Keeping References Current

Software architecture continues to evolve.

Implementation techniques improve.

Frameworks come and go.

The references contained within this document SHOULD therefore be reviewed periodically to ensure:

- guidance remains relevant
- obsolete practices are removed
- better implementation advice is incorporated

The underlying architectural philosophy should remain stable even as implementation techniques evolve.

---

# Closing Statement

MEG-004 does not attempt to invent a new architecture.

Instead, it applies the proven principles of Hexagonal Architecture to a modern, event-driven, extension-first platform.

The resulting architecture intentionally emphasises:

- explicit dependencies
- replaceable infrastructure
- protected business logic
- long-term maintainability
- technology independence

Every future engineering specification builds upon these foundations.

Because in the long life of a software platform:

> **Technologies are temporary.**

> **The business is permanent.**

Architecture exists to ensure the second survives the first.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`glossary.md`

**Next File**

**End of Specification**
