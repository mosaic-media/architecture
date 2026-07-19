<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/index.md
Document: MEG-004
Status: Draft
-->

# MEG-004 — Hexagonal Architecture

> *The Domain should know nothing about the outside world. The outside world should adapt itself to the Domain.*

---

# Purpose

Mosaic is designed to evolve for many years, and over that time its databases, APIs, protocols, storage engines, modules and user interfaces will all change. The business the platform serves should remain stable throughout. Hexagonal Architecture provides the structural rules that let the Domain Model stay independent of every external technology.

Unlike traditional layered architectures, Hexagonal Architecture does not organise software around technical layers. It organises software around **dependencies**: everything outside the Domain adapts to it, and the Domain adapts to nothing.

---

# Relationship to MEG

```mermaid
flowchart TD

N1["MEG-001"]
N2["Engineering Standards"]
N3["MEG-002"]
N4["Reactive Runtime"]
N5["MEG-003"]
N6["Domain Model"]
N7["MEG-004"]
N8["Dependency Boundaries"]
N9["Infrastructure"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
N8 --> N9
```

Each guide answers a different question. [MEG-001](../meg-001-go-engineering-standards/index.md) defines **how software is written**, [MEG-002](../meg-002-event-driven-runtime/index.md) defines **how software executes** and [MEG-003](../meg-003-domain-driven-design/index.md) defines **what the business is**. MEG-004 defines **how the business is protected from technology.**

---

# Scope

This specification defines Hexagonal philosophy, Ports, Adapters, driving adapters, driven adapters, dependency inversion, the composition root, dependency direction, application services, infrastructure boundaries, external systems, runtime integration and testing boundaries.

It intentionally does **not** define business models, Domain behaviour, runtime semantics, storage implementation or deployment architecture. Those concerns are defined by other MEG specifications.

---

# Guiding Question

MEG-004 exists to answer one question.

> **How should the Mosaic Domain Model remain completely independent of infrastructure while still interacting with the outside world?**

---

# Architectural Statement

Within Mosaic:

> **The Domain owns the contracts. Infrastructure provides the implementations.**

Everything external to the Domain is replaceable; the Domain is not. It should therefore never depend upon PostgreSQL, DuckDB, HTTP, REST, GraphQL, WebSockets, Docker, Jellyfin, TMDB, Stremio, Trakt or Message Brokers. Those technologies adapt themselves to the Domain through Ports and Adapters instead.

Hexagonal Architecture (also known as Ports and Adapters) exists specifically to isolate business logic from external technologies through dependency inversion.  [AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

---

# Architectural Hierarchy

The Mosaic Architecture intentionally separates concerns into distinct conceptual layers.

```mermaid
flowchart TD

N1["Business Domain"]
N2["Application"]
N3["Ports"]
N4["Adapters"]
N5["External Systems"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Notice that dependencies flow **upwards** while knowledge flows **inwards**. Infrastructure never leaks into the Domain.

---

# Expected Outcome

After reading MEG-004 contributors should understand why Hexagonal Architecture exists, what Ports represent, what Adapters implement, how dependencies flow, how infrastructure integrates with the Domain, how runtime and domain remain independent, and how new technologies are introduced without modifying business logic — all without discussing any specific database, transport protocol or framework.

---

# Repository Structure

```text
docs/
└── engineering/guides/
    └── meg-004-hexagonal-architecture/
        index.md
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
        references.md
        glossary.md
```

---

# Dependencies

Required reading:

- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)
- [MEG-002 — Event-Driven Runtime](../meg-002-event-driven-runtime/index.md)
- [MEG-003 — Domain-Driven Design](../meg-003-domain-driven-design/index.md)

Future companion specifications:

- [MEG-006 — Module Platform](../meg-006-module-platform/index.md)
- [MEG-005 — Runtime Architecture](../meg-005-runtime-architecture/index.md)
- [MEG-007 — Storage Architecture](../meg-007-storage-architecture/index.md)

---

# Design Goals

The Hexagonal Architecture is intended to produce software that is technology independent, testable, evolvable, replaceable, decoupled, domain centric, explicit and maintainable. Above all, the architecture should ensure that changing infrastructure never requires changing the Domain Model.
