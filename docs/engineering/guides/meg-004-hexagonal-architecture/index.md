<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/index.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# MEG-004 — Hexagonal Architecture

> *The Domain should know nothing about the outside world. The outside world should adapt itself to the Domain.*

---

# Purpose

Mosaic is designed to evolve for many years.

During that time:

- databases will change
- APIs will change
- protocols will change
- storage engines will change
- extensions will change
- user interfaces will change

The business, however, should remain stable.

Hexagonal Architecture provides the structural rules that allow the Domain Model to remain independent of every external technology.

Unlike traditional layered architectures, Hexagonal Architecture does not organise software around technical layers.

Instead, it organises software around **dependencies**.

Everything outside the Domain adapts to it.

The Domain adapts to nothing.

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

Domain Model

↓

MEG-004

↓

Dependency Boundaries

↓

Infrastructure
```

MEG-001 defines **how software is written.**

MEG-002 defines **how software executes.**

MEG-003 defines **what the business is.**

MEG-004 defines **how the business is protected from technology.**

---

# Scope

This specification defines:

- Hexagonal philosophy
- Ports
- Adapters
- Driving adapters
- Driven adapters
- Dependency inversion
- Composition root
- Dependency direction
- Application services
- Infrastructure boundaries
- External systems
- Runtime integration
- Testing boundaries

This specification intentionally does **not** define:

- Business models
- Domain behaviour
- Runtime semantics
- Storage implementation
- Deployment architecture

Those concerns are defined by other MEG specifications.

---

# Core Question

MEG-004 exists to answer one question.

> **How should the Mosaic Domain Model remain completely independent of infrastructure while still interacting with the outside world?**

---

# Architectural Statement

Within Mosaic:

> **The Domain owns the contracts. Infrastructure provides the implementations.**

Everything external to the Domain is replaceable.

The Domain is not.

The Domain should never depend upon:

- PostgreSQL
- DuckDB
- HTTP
- REST
- GraphQL
- WebSockets
- Docker
- Jellyfin
- TMDB
- Stremio
- Trakt
- Message Brokers

Instead, those technologies adapt themselves to the Domain through Ports and Adapters.

Hexagonal Architecture (also known as Ports and Adapters) exists specifically to isolate business logic from external technologies through dependency inversion.  [oai_citation:0‡AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html?utm_source=chatgpt.com)

---

# Architectural Hierarchy

The Mosaic Architecture intentionally separates concerns into distinct conceptual layers.

```
Business Domain

↓

Application

↓

Ports

↓

Adapters

↓

External Systems
```

Notice:

Dependencies flow **upwards**.

Knowledge flows **inwards**.

Infrastructure never leaks into the Domain.

---

# Expected Outcome

After reading MEG-004 contributors should understand:

- why Hexagonal Architecture exists
- what Ports represent
- what Adapters implement
- how dependencies flow
- how infrastructure integrates with the Domain
- how runtime and domain remain independent
- how new technologies are introduced without modifying business logic

without discussing any specific database, transport protocol or framework.

---

# Repository Structure

```
engineering/

└── meg/

    └── MEG-004 Hexagonal Architecture/

        README.md

        00-document-control.md

        01-hexagonal-philosophy.md

        02-ports.md

        03-driving-ports.md

        04-driven-ports.md

        05-adapters.md

        06-driving-adapters.md

        07-driven-adapters.md

        08-dependency-direction.md

        09-composition-root.md

        10-application-services.md

        11-runtime-boundary.md

        12-testing-the-hexagon.md

        13-modelling-guidelines.md

        14-adrs.md

        15-contributor-guidance.md

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design

Future companion specifications:

- MEG-005 Extension Platform
- MEG-006 Runtime Architecture
- MEG-007 Storage Architecture

---

# Design Goals

The Hexagonal Architecture is intended to produce software that is:

- Technology independent
- Testable
- Evolvable
- Replaceable
- Decoupled
- Domain centric
- Explicit
- Maintainable

The architecture should ensure that changing infrastructure never requires changing the Domain Model.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Next File**

`00-document-control.md`
