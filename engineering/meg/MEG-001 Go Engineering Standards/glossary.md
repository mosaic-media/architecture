<!--
File: engineering/meg/MEG-001 Go Engineering Standards/glossary.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Glossary

> *Engineering terminology should have one meaning throughout the Mosaic ecosystem.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Engineering Guidelines (MEG).

Where a term has a specific architectural meaning within Mosaic, that definition takes precedence over colloquial usage.

The purpose of this glossary is to ensure that engineers discuss architecture using a shared vocabulary.

---

# A

## Abstraction

A simplified representation of behaviour that intentionally hides implementation details.

Within Mosaic, abstractions exist to reduce coupling and improve maintainability.

Abstractions MUST justify their existence by simplifying the software.

---

## API

Application Programming Interface.

The public contract exposed by a package, service or application.

Within Mosaic, exported identifiers form part of a package's API.

---

## Architecture

The high-level organisation of software components, responsibilities and dependencies.

Architecture answers:

> *How is the system organised?*

Not:

> *How is a particular function implemented?*

---

## Architectural Boundary

A clear separation between responsibilities.

Examples include:

- Transport
- Domain
- Infrastructure
- Storage

Boundaries reduce coupling and improve maintainability.

---

# B

## Behaviour

The observable actions provided by a component.

Go interfaces describe behaviour rather than implementation.

---

## Business Logic

Rules that implement domain-specific behaviour.

Business logic SHOULD remain independent of:

- HTTP
- databases
- transport protocols
- infrastructure

---

## Boundary

A location where responsibility changes.

Examples include:

- HTTP → Service
- Service → Repository
- Repository → Database

Boundaries often translate data, errors or models.

---

# C

## Cancellation

The act of terminating ongoing work through `context.Context`.

All long-running Mosaic operations are expected to honour cancellation requests.

---

## Cohesion

The degree to which responsibilities within a package naturally belong together.

High cohesion is desirable.

---

## Composition

Building complex behaviour by combining smaller components.

Composition is the preferred architectural mechanism within Mosaic.

---

## Composition Root

The location where application dependencies are constructed.

Typically:

```
cmd/server/main.go
```

---

## Concurrency

Structuring software so multiple independent tasks can make progress.

Concurrency improves responsiveness.

It does not necessarily imply parallel execution.

---

## Coupling

The degree to which one component depends upon another.

Lower coupling generally produces more maintainable software.

---

# D

## Dependency

A component required by another component.

Dependencies should be:

- explicit
- constructor-injected
- visible

---

## Domain

The business concepts represented by the software.

Examples include:

- Library
- Playback
- Metadata
- User

The domain should remain independent of infrastructure.

---

# E

## Embedding

A Go language feature allowing one type to promote another type's methods.

Embedding is not inheritance.

Within Mosaic, embedding is used sparingly.

---

## Error Boundary

A point where errors are translated into a more meaningful representation.

Example:

```
SQL

↓

Repository

↓

Domain Error

↓

HTTP Response
```

---

# G

## Goroutine

A lightweight concurrent execution managed by the Go runtime.

Every goroutine within Mosaic must have:

- an owner
- cancellation
- lifecycle management

---

# I

## Infrastructure

Components responsible for interacting with external systems.

Examples include:

- databases
- caches
- message brokers
- blob storage

Infrastructure should remain isolated from business logic.

---

## Interface

A behavioural contract describing capabilities.

Interfaces belong to consumers.

They do not describe implementation.

---

# M

## Middleware

Behaviour executed before or after another component.

Examples include:

- authentication
- logging
- metrics
- tracing

Each middleware should own one responsibility.

---

## Mutation

Modification of existing state.

Mutable shared state requires explicit synchronisation.

---

# O

## Observability

The ability to understand system behaviour through:

- logs
- metrics
- traces
- health checks

Every production service should be observable.

---

# P

## Package

The primary architectural unit within Go.

Packages own responsibilities.

Types implement behaviour.

---

## Polymorphism

The ability for multiple implementations to satisfy the same interface.

Within Go, polymorphism is achieved through interfaces rather than inheritance.

---

## Public API

The exported behaviour exposed by a package.

Public APIs should remain small and stable.

---

# R

## Refactoring

Improving internal implementation without changing observable behaviour.

Refactoring should improve:

- readability
- maintainability
- simplicity

---

## Repository

A component responsible for persistence.

Repositories should not contain business logic.

---

# S

## Service

A component responsible for implementing business behaviour.

Services coordinate collaborators.

They do not own infrastructure.

---

## Single Responsibility

The principle that a component should have one reason to change.

This principle applies equally to:

- packages
- structs
- functions
- services

---

## State

The current condition of a component.

Mutable state should remain clearly owned.

---

## Strategy

An interchangeable implementation satisfying a common behaviour.

Strategies naturally emerge from Go interfaces.

---

# T

## Technical Debt

The long-term cost introduced by suboptimal engineering decisions.

Technical debt should be reduced continuously.

Not accumulated deliberately.

---

## Transport

The mechanism through which requests enter or leave an application.

Examples include:

- HTTP
- CLI
- WebSocket
- gRPC

Transport should remain separate from business logic.

---

# U

## Utility Package

A generic package lacking a clearly defined responsibility.

Examples include:

```
utils
```

```
common
```

```
helpers
```

Utility packages are prohibited within Mosaic.

---

# W

## Worker Pool

A bounded collection of goroutines processing queued work.

Worker pools provide predictable concurrency and resource usage.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| API | Application Programming Interface |
| CI | Continuous Integration |
| GC | Garbage Collector |
| HTTP | Hypertext Transfer Protocol |
| MEG | Mosaic Engineering Guidelines |
| MDL | Mosaic Design Language |
| MDS | Mosaic Design Specifications |
| SDK | Software Development Kit |
| SQL | Structured Query Language |
| SWR | Stale-While-Revalidate |

---

# Relationship to the MEG

This glossary supports every document within MEG-001.

Definitions should remain consistent across:

- engineering standards
- ADRs
- architecture specifications
- contributor documentation

Where terminology evolves, this glossary SHOULD be updated before introducing new definitions elsewhere.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`18-contributor-guidance.md`

**Next File**

`references.md`
