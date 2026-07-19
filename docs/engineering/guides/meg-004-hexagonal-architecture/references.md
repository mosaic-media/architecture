<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/references.md
Document: MEG-004
Status: Draft
-->

# References

> *Hexagonal Architecture is not a framework. It is a way of protecting business knowledge from technological change.*

---

# Purpose

This document records the primary references that informed the architectural principles established throughout MEG-004. Hexagonal Architecture has existed for over two decades, and the Mosaic implementation builds upon those established ideas while adapting them to an Event-Driven Runtime, Domain-Driven Design, Go Engineering, Module-first architecture and long-lived software platforms.

These references explain the architectural lineage of the Mosaic platform rather than prescribe implementation.

---

# Primary References

## Hexagonal Architecture (Ports & Adapters)

**Author:** Alistair Cockburn

The original paper introducing Ports, Adapters, technology independence, dependency inversion and testable architecture. It forms the primary architectural foundation of MEG-004, and the central architectural principle adopted by Mosaic is:

> **The application communicates through Ports while Adapters isolate external technologies.**  [Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture)

**URL:** https://alistair.cockburn.us/hexagonal-architecture/

---

## Hexagonal Architecture Explained

**Authors:** Alistair Cockburn, Juan Manuel Garrido de Paz

A modern expansion of the original Ports & Adapters architecture including practical implementation guidance. Recommended reading for contributors wishing to understand the evolution of Hexagonal Architecture beyond the original article.  [Google Books](https://books.google.com/books/about/Hexagonal_Architecture_Explained.html?id=Eim20AEACAAJ)

---

# Supporting Architecture References

## AWS Prescriptive Guidance

Practical guidance for implementing Hexagonal Architecture within modern cloud-native systems, covering dependency isolation, testability, replaceable infrastructure and technology independence. The AWS guidance aligns closely with Mosaic's goal of protecting the Domain from infrastructure concerns.  [AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

---

## Dependency Injection Principles, Practices and Patterns

**Author:** Mark Seemann

Covers the Composition Root, Dependency Injection, Dependency Inversion and object composition. This work strongly influenced Mosaic's preference for explicit composition and constructor injection, and its avoidance of service locators and dependency injection containers. Many of the Composition Root principles in MEG-004 derive directly from it.

---

# Domain-Driven Design References

## Domain-Driven Design

**Author:** Eric Evans

Referenced for Bounded Contexts, Aggregates, Domain Services, Repositories and Domain independence. Although [MEG-003](../meg-003-domain-driven-design/index.md) defines the Domain Model, Hexagonal Architecture exists largely to protect that model.

---

## Implementing Domain-Driven Design

**Author:** Vaughn Vernon

Referenced primarily for Application Services, Repositories, Aggregate persistence and dependency boundaries. Many practical implementation recommendations adopted by Mosaic align with this work.

---

# Software Engineering References

## Clean Architecture

**Author:** Robert C. Martin

Referenced primarily for the dependency rule, policy versus detail, and architectural boundaries. Although Clean Architecture and Hexagonal Architecture differ in presentation, they share the central idea that dependencies point toward business rules.

---

## The Pragmatic Programmer

**Authors:** Andrew Hunt, David Thomas

Referenced for simplicity, explicitness, maintainability and evolutionary design. Many contributor guidelines within the MEG reflect these engineering attitudes.

---

## Refactoring

**Author:** Martin Fowler

Referenced for architectural evolution, continuous improvement and incremental design. Architecture should evolve gradually, not through wholesale rewrites.

---

# Go References

The Go language naturally complements Hexagonal Architecture. Recommended references include the following.

## Effective Go

Topics include interfaces, package design, composition and dependency management.

https://go.dev/doc/effective_go

---

## Go Code Review Comments

Topics include interfaces, package ownership, naming and architecture.

https://go.dev/wiki/CodeReviewComments

---

## Go Blog

Recommended topics are interfaces, composition, testing and dependency management. The implementation should remain idiomatic Go while preserving architectural principles.

---

# Reactive Runtime References

MEG-004 intentionally integrates with [MEG-002](../meg-002-event-driven-runtime/index.md). Relevant references include Event-Driven Architecture, Reactive Systems, OpenTelemetry and Enterprise Integration Patterns.

The Runtime remains outside the Hexagon and communicates with the Domain exclusively through Ports and Adapters.

---

# Internal Mosaic Specifications

The following specifications complement MEG-004.

## Engineering

- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)
- [MEG-002 — Event-Driven Runtime](../meg-002-event-driven-runtime/index.md)
- [MEG-003 — Domain-Driven Design](../meg-003-domain-driven-design/index.md)

---

## Planned Engineering Specifications

- [MEG-006 — Module Platform](../meg-006-module-platform/index.md)
- [MEG-005 — Runtime Architecture](../meg-005-runtime-architecture/index.md)
- [MEG-007 — Storage Architecture](../meg-007-storage-architecture/index.md)
- [MEG-008 — Observability](../meg-008-observability/index.md)
- [MEG-009 — Security Architecture](../meg-009-security-architecture/index.md)
- [MEG-010 — Performance Engineering](../meg-010-performance-engineering/index.md)

---

## Mosaic Design Language

- [MDL-001 — Mosaic Design Language Vision](../../../design/language/mdl-001-vision/index.md)
- [MDL-002 — Principles](../../../design/language/mdl-002-principles/index.md)
- [MDL-003 — Mental Model](../../../design/language/mdl-003-mental-model/index.md)
- [MDL-004 — Interaction Model](../../../design/language/mdl-004-interaction-model/index.md)
- [MDL-005 — Composition Model](../../../design/language/mdl-005-composition-model/index.md)

---

## Mosaic Design Specifications

- [MDS-001 — Design Token Architecture](../../../design/system/mds-001-design-token-architecture/index.md)
- [MDS-002 — Colour System](../../../design/system/mds-002-colour-system/index.md)
- [MDS-003 — Material System](../../../design/system/mds-003-material-system/index.md)
- [MDS-004 — Typography System](../../../design/system/mds-004-typography-system/index.md)
- [MDS-005 — Motion System](../../../design/system/mds-005-motion-system/index.md)
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)

---

## Mosaic Design Proposals

- [MDP-001 — Adaptive Composition Runtime](../../architecture/mdp-001-adaptive-composition-runtime/index.md)
- [MDP-001 ch14 — Adaptive Tile Model](../../architecture/mdp-001-adaptive-composition-runtime/14-adaptive-tile-model.md)

---

# Architectural Principles

The Hexagonal Architecture established throughout MEG-004 intentionally builds upon several enduring principles.

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

Software architecture continues to evolve: implementation techniques improve and frameworks come and go. The references in this document should therefore be reviewed periodically to ensure guidance remains relevant, obsolete practices are removed and better implementation advice is incorporated. The underlying architectural philosophy should remain stable even as implementation techniques evolve.

---

# Closing Statement

MEG-004 does not attempt to invent a new architecture. Instead, it applies the proven principles of Hexagonal Architecture to a modern, event-driven, module-first platform, emphasising explicit dependencies, replaceable infrastructure, protected business logic, long-term maintainability and technology independence. Every future engineering specification builds upon these foundations.

Because in the long life of a software platform:

> **Technologies are temporary.**

> **The business is permanent.**

Architecture exists to ensure the second survives the first.
