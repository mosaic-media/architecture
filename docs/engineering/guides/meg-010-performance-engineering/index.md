<!--
File: docs/engineering/guides/meg-010-performance-engineering/index.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# MEG-010 — Performance Engineering

> *Performance is not an optimisation step. It is an architectural property that must be designed, measured and protected from the beginning.*

---

# Purpose

Previous engineering specifications established:

- how software is written
- how work executes
- how the business is modelled
- how the Domain is protected
- how the Runtime operates
- how the platform evolves
- how information is stored
- how the platform explains itself
- how the platform protects itself

MEG-010 answers the next architectural question.

> **How should Mosaic remain fast, responsive and efficient without compromising clarity or correctness?**

Performance is not simply a matter of faster code.

Within Mosaic, performance is shaped by:

- Runtime scheduling
- capability design
- repository behaviour
- storage selection
- event throughput
- memory ownership
- caching strategy
- deployment topology
- observability

Performance must therefore be treated as a cross-cutting architectural concern rather than a narrow implementation concern.

---

# Relationship to MEG

```text
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

Hexagonal Architecture

↓

MEG-005

↓

Capability Runtime

↓

MEG-006

↓

Extension Platform

↓

MEG-007

↓

Storage Architecture

↓

MEG-008

↓

Observability

↓

MEG-009

↓

Security Architecture

↓

MEG-010

↓

Performance Engineering
```

Previous specifications define:

> **How the platform behaves.**

MEG-010 defines:

> **How the platform stays efficient while behaving that way.**

---

# Scope

This specification defines:

- Performance philosophy
- Performance ownership
- Runtime performance
- Capability performance
- Repository performance
- Storage performance
- Event throughput
- Scheduling efficiency
- Memory behaviour
- Caching strategy
- Back-pressure
- Benchmarking
- Profiling
- Load testing
- Performance observability
- Performance guidelines

This specification intentionally does **not** define:

- business behaviour
- security policy
- storage implementation
- deployment infrastructure

Those concerns belong to previous or future MEG specifications.

---

# Core Question

MEG-010 exists to answer one question.

> **How should Mosaic remain performant while preserving the architecture already defined by the previous MEGs?**

---

# Performance Statement

Within Mosaic:

> **Performance is the measurable expression of good architecture.**

Performance should not be achieved by compromising:

- ownership
- boundaries
- trust
- observability
- correctness

The fastest system is not always the best system.

The best system is the one that remains fast enough while staying understandable, secure and maintainable.

---

# Performance Hierarchy

Performance intentionally follows the platform architecture.

```text
Platform

↓

Runtime

↓

Capabilities

↓

Repositories

↓

Storage

↓

Infrastructure
```

Every layer contributes to platform performance.

Every layer therefore owns its own performance responsibilities.

---

# Expected Outcome

After reading MEG-010 contributors should understand:

- how performance is owned
- how latency should be measured
- how throughput should be improved
- how memory should be managed
- how back-pressure should operate
- how storage selection affects speed
- how to benchmark the platform
- how to improve performance without weakening architecture

without turning the platform into a performance-driven mess. Humans do love creating those.

---

# Repository Structure

```text
engineering/

└── meg/

    └── MEG-010 Performance Engineering/

        README.md

        00-document-control.md

        01-performance-philosophy.md

        02-runtime-performance.md

        03-capability-performance.md

        04-repository-performance.md

        05-storage-performance.md

        06-event-throughput.md

        07-scheduling-efficiency.md

        08-memory-ownership.md

        09-caching-strategy.md

        10-back-pressure.md

        11-benchmarking.md

        12-profiling.md

        13-performance-guidelines.md

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
- MEG-004 Hexagonal Architecture
- MEG-005 Capability Runtime
- MEG-006 Extension Platform
- MEG-007 Storage Architecture
- MEG-008 Observability
- MEG-009 Security Architecture

Future companion specifications:

- MEG-011 Deployment Architecture
- MEG-012 API Architecture
- MEG-013 Event Architecture

---

# Design Goals

The Performance Architecture is intended to produce a platform that is:

- Fast
- Responsive
- Efficient
- Predictable
- Measurable
- Scalable
- Resource-conscious
- Operationally stable

Performance should emerge from architecture rather than being retrofitted onto it.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Next File**

`00-document-control.md`
