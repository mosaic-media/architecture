<!--
File: docs/engineering/guides/meg-001-go-engineering-standards/references.md
Document: MEG-001
Status: Draft
-->

# References

> *Engineering standards should be grounded in established knowledge rather than individual opinion.*

---

# Purpose

The Mosaic Engineering Guidelines (MEG) build upon decades of software engineering experience.

This document records the primary references that informed the standards defined throughout MEG-001.

These references should be considered recommended reading for contributors wishing to deepen their understanding of Go and software architecture.

The MEG is intentionally opinionated.

However, those opinions are derived from established engineering principles rather than invented in isolation.

---

# Primary Go References

## Effective Go

**Publisher**

The Go Team

**Purpose**

The canonical guide to writing idiomatic Go.

**Topics**

- Language idioms
- Package design
- Interfaces
- Concurrency
- Error handling
- Naming
- Documentation

**URL**

https://go.dev/doc/effective_go

---

## Go Code Review Comments

**Publisher**

The Go Team

**Purpose**

Practical engineering guidance used by Go maintainers during code review.

**Topics**

- Package naming
- Error handling
- Context usage
- Interfaces
- Receiver design
- Comments
- Testing
- Style

**URL**

https://go.dev/wiki/CodeReviewComments

---

## Go Blog

**Publisher**

The Go Team

**Purpose**

Articles explaining language design, performance, concurrency and architecture.

Recommended topics include:

- Context
- Pipelines
- Profiling
- Error handling
- Memory
- Synchronisation

**URL**

https://go.dev/blog

---

## Go Package Documentation

**Publisher**

The Go Team

**Purpose**

Authoritative documentation for the Go standard library.

Examples include:

- context
- errors
- sync
- net/http
- slog
- testing

**URL**

https://pkg.go.dev

---

# Software Engineering References

## Clean Architecture

**Author**

Robert C. Martin

**Topics**

- Dependency direction
- Architectural boundaries
- Separation of concerns

---

## Clean Code

**Author**

Robert C. Martin

**Topics**

- Readability
- Naming
- Functions
- Refactoring

While several examples are Java-centric, many of the underlying engineering principles remain valuable.

Individual implementation patterns should always be adapted to idiomatic Go.

---

## Domain-Driven Design

**Author**

Eric Evans

**Topics**

- Domain modelling
- Ubiquitous language
- Bounded contexts
- Aggregates

The strategic concepts remain highly relevant.

Implementation techniques should follow Go idioms rather than object-oriented conventions.

---

## Refactoring

**Author**

Martin Fowler

**Topics**

- Incremental improvement
- Code smells
- Continuous evolution
- Technical debt reduction

This work strongly aligns with the Boy Scout Rule adopted throughout the MEG.

---

## The Pragmatic Programmer

**Authors**

Andrew Hunt

David Thomas

**Topics**

- Software craftsmanship
- Continuous improvement
- Engineering discipline

Many of the engineering attitudes reflected within the MEG originate from this work.

---

## Designing Data-Intensive Applications

**Author**

Martin Kleppmann

**Topics**

- Distributed systems
- Data consistency
- Event-driven systems
- Storage architecture
- Scalability

Strongly recommended reading for engineers working on distributed Mosaic services.

---

# Architecture References

The following architectural concepts influence the Mosaic ecosystem.

- Event-Driven Architecture
- Hexagonal Architecture
- Ports and Adapters
- CQRS (where appropriate)
- Stale-While-Revalidate
- Repository Pattern
- Worker Pool Pattern
- Pipeline Pattern

Mosaic intentionally adopts concepts rather than frameworks.

Architectural ideas should always be evaluated through the lens of simplicity and maintainability.

---

# Concurrency References

Recommended reading.

## Go Concurrency Patterns

The Go Team

Topics include:

- Pipelines
- Cancellation
- Fan-out
- Fan-in

https://go.dev/blog/pipelines

---

## Share Memory By Communicating

The Go Team

Introduces Go's concurrency philosophy.

https://go.dev/blog/share-memory-by-communicating

---

## The Context Package

The Go Team

Introduces structured cancellation throughout Go applications.

https://go.dev/blog/context

---

# Testing References

Recommended reading.

- Go Testing Package Documentation
- Go Fuzz Testing
- Go Race Detector
- Table Driven Tests

Useful URLs:

https://pkg.go.dev/testing

https://go.dev/doc/articles/race_detector

https://go.dev/wiki/TableDrivenTests

---

# Performance References

Recommended reading.

- Profiling Go Programs
- Escape Analysis
- Go Memory Model
- Performance Wiki

Useful URLs:

https://go.dev/blog/profiling-go-programs

https://go.dev/ref/mem

https://go.dev/wiki/Performance

---

# Logging & Observability

Recommended references.

- slog Package Documentation
- OpenTelemetry Specification
- Prometheus Best Practices

Observability should be considered an architectural concern rather than an operational afterthought.

---

# Internal References

The following Mosaic specifications complement MEG-001.

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

## Future Mosaic Architecture Specifications

Examples include:

- Event Architecture
- Storage Architecture
- Module SDK
- Authentication
- Metadata Platform
- Runtime Platform
- Observability
- Deployment Architecture

Together these specifications define the complete architectural blueprint for the Mosaic ecosystem.

---

# Keeping References Current

Engineering practices evolve.

Languages evolve.

Tooling evolves.

This document SHOULD be reviewed periodically to ensure referenced material remains:

- relevant
- accessible
- authoritative

Where better references become available, they should replace older material while preserving the engineering philosophy established throughout the MEG.

---

# Closing Statement

The Mosaic Engineering Guidelines do not exist to replace established software engineering knowledge.

They exist to curate, refine and adapt that knowledge into a consistent set of standards for the Mosaic platform.

Contributors are encouraged to understand not only **what** these standards require, but also **why** they exist.

Engineering judgement will always remain more valuable than memorising rules.
