<!--
File: docs/engineering/guides/meg-003-domain-driven-design/references.md
Document: MEG-003
Status: Draft
-->

# References

> *The Mosaic Domain Model is built upon established principles of Domain-Driven Design, adapted for an event-driven, module-first platform.*

---

# Purpose

This document records the primary references that informed the Domain-Driven Design principles established throughout MEG-003.

The objective of these references is not to prescribe implementation.

Instead, they provide the theoretical and architectural foundations upon which the Mosaic Domain Model has been developed.

Where the MEG differs from traditional DDD guidance, it does so intentionally to support the unique requirements of the Mosaic platform.

---

# Primary References

## Domain-Driven Design

**Author**

Eric Evans

**Purpose**

The foundational work introducing:

- Ubiquitous Language
- Bounded Contexts
- Aggregates
- Entities
- Value Objects
- Domain Services
- Strategic Design
- Tactical Design

This work forms the conceptual foundation of MEG-003.

Although Mosaic adapts certain implementation details for an event-driven architecture, the underlying modelling philosophy remains strongly aligned.

---

## Domain-Driven Design Reference

**Author**

Eric Evans

**Purpose**

A concise summary of the fundamental principles introduced in Domain-Driven Design.

Recommended reading for all contributors.

**URL**

https://domainlanguage.com/ddd/reference/

---

## Implementing Domain-Driven Design

**Author**

Vaughn Vernon

**Purpose**

Expands practical implementation guidance including:

- Aggregate design
- Aggregate boundaries
- Repositories
- Factories
- Domain Events
- Bounded Contexts

Many tactical recommendations adopted within Mosaic align closely with this work.

---

## Effective Aggregate Design

**Author**

Vaughn Vernon

**Purpose**

A three-part series focusing specifically on:

- Aggregate sizing
- Consistency boundaries
- Aggregate relationships

This work significantly influenced the Aggregate guidance within MEG-003.

**URL**

https://dddcommunity.org/library/vernon_2011/

---

# Supporting References

## Martin Fowler

Martin Fowler's writings on Domain-Driven Design significantly influenced the modelling approach used throughout Mosaic.

Recommended topics include:

- Aggregates
- Value Objects
- Bounded Contexts
- Domain Events
- Anti-Corruption Layers

**URL**

https://martinfowler.com/

---

## Patterns of Enterprise Application Architecture

**Author**

Martin Fowler

Relevant concepts include:

- Repository
- Unit of Work
- Identity Map
- Data Mapper

Mosaic intentionally adopts some of these concepts while deliberately avoiding others where they introduce unnecessary complexity.

---

# Software Engineering References

## Clean Architecture

**Author**

Robert C. Martin

Referenced primarily for:

- dependency direction
- separation of concerns
- business independence

Implementation details within Mosaic differ where Domain-Driven Design provides more appropriate guidance.

---

## Refactoring

**Author**

Martin Fowler

Relevant for:

- evolving models
- improving terminology
- incremental architectural refinement

The Domain Model is expected to evolve continuously.

This work strongly supports that philosophy.

---

## The Pragmatic Programmer

**Authors**

Andrew Hunt

David Thomas

Referenced primarily for:

- continuous improvement
- engineering discipline
- incremental design

Many contributor guidelines throughout the MEG reflect the engineering mindset encouraged by this work.

---

# Event-Driven Architecture

Although MEG-003 focuses upon the Domain rather than the Runtime, Domain Events naturally integrate with the runtime architecture defined in [MEG-002](../meg-002-event-driven-runtime/index.md).

Recommended references include:

## Martin Fowler

Event-Driven Architecture

https://martinfowler.com/articles/201701-event-driven.html

---

## Enterprise Integration Patterns

Gregor Hohpe

Bobby Woolf

Useful concepts include:

- Message Channels
- Published Language
- Message Translation

These patterns complement Domain Events without influencing the Domain Model itself.

---

# Go References

The Domain Model intentionally remains implementation independent.

However, contributors are encouraged to understand how Go supports rich domain modelling.

Recommended references include:

## Effective Go

https://go.dev/doc/effective_go

---

## Go Code Review Comments

https://go.dev/wiki/CodeReviewComments

---

## Go Blog

Recommended topics:

- composition
- interfaces
- package design
- concurrency

Go implementation should always support the Domain Model.

Never define it.

---

# Internal Mosaic Specifications

The following specifications complement MEG-003.

## Engineering

- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)
- [MEG-002 — Event-Driven Runtime](../meg-002-event-driven-runtime/index.md)

---

## Planned Engineering Specifications

- [MEG-004 — Hexagonal Architecture](../meg-004-hexagonal-architecture/index.md)
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
- [MDP-001 — Adaptive Composition Runtime](../../architecture/mdp-001-adaptive-composition-runtime/index.md)
- [MDP-001 — Adaptive Composition Runtime](../../architecture/mdp-001-adaptive-composition-runtime/14-adaptive-tile-model.md)
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)

---

# Domain Principles

The Domain Model established throughout MEG-003 is intentionally built upon several enduring principles.

These include:

- Business before technology.
- Language before implementation.
- Behaviour before data.
- Identity before persistence.
- Consistency before convenience.
- Small Aggregates.
- Explicit ownership.
- Evolutionary modelling.
- Infrastructure independence.
- Rich domain behaviour.

These principles should remain stable even as implementation evolves.

---

# Keeping References Current

Domain modelling continues to evolve.

Software architecture continues to evolve.

The references contained within this document SHOULD therefore be reviewed periodically to ensure that:

- recommended material remains current
- obsolete guidance is removed
- new influential work is incorporated
- architectural thinking remains contemporary

The philosophy of the Domain Model should remain stable even as modelling techniques improve.

---

# Closing Statement

MEG-003 does not attempt to replace Domain-Driven Design.

Instead, it adapts proven modelling principles into an architecture specifically designed for the Mosaic platform.

The resulting Domain Model intentionally emphasises:

- business language
- explicit ownership
- evolutionary design
- autonomous capabilities
- clear consistency boundaries

Everything else within the platform exists to support these business concepts.

Because ultimately:

> **The business is the product.**

The software merely gives it form.
