<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/index.md
Document: MEG-002
Status: Draft
Version: 0.3
-->

# MEG-002 — Event-Driven Runtime

> *Software should not ask what happened. It should be told.*

---

# Purpose

The Mosaic Runtime is built upon an event-driven architecture.

Rather than components communicating directly through tightly coupled service calls, the runtime is composed of autonomous capabilities that communicate through events.

This approach enables:

- Loose coupling
- High cohesion
- Horizontal scalability
- Module interoperability
- Background processing
- Reactive workflows
- Independent deployment
- Progressive capability growth

Unlike traditional request-driven architectures, the Mosaic Runtime treats events as the primary mechanism through which the platform coordinates work.

---

# Relationship to MEG

```
MEG-001

↓

Engineering Principles

↓

MEG-002

↓

Runtime Behaviour

↓

Modules

↓

Platform Features
```

MEG-001 defines **how software is engineered.**

MEG-002 defines **how software behaves once it is running.**

Together they establish the engineering foundation of the Mosaic platform.

---

# Scope

This specification defines:

- Event philosophy
- Runtime lifecycle
- Event contracts
- Event naming
- Event versioning
- Publishers
- Subscribers
- Event bus
- Worker lifecycle
- Scheduling
- Retry strategy
- Idempotency
- Event ordering
- Correlation IDs
- Backpressure
- Observability
- Runtime resilience

This specification intentionally does **not** define:

- Business domains
- HTTP APIs
- Storage architecture
- Module SDK
- Deployment
- Infrastructure

These concerns are defined by later MEG specifications.

---

# Guiding Question

MEG-002 exists to answer one question.

> **How should independently developed capabilities coordinate work within the Mosaic Runtime?**

---

# Runtime Statement

Within Mosaic:

> **Capabilities publish facts. Other capabilities decide whether they care.**

A capability should never need to know:

- who consumes an event
- how many consumers exist
- what work those consumers perform
- whether any consumer exists at all

This separation allows the platform to evolve without creating unnecessary coupling between capabilities.

---

# Runtime Hierarchy

The Mosaic Runtime intentionally separates event processing into conceptual layers.

```
Capability

↓

Domain Event

↓

Event Bus

↓

Subscribers

↓

Background Work

↓

State Change

↓

New Events
```

Every layer owns exactly one responsibility.

Future chapters define each layer in detail.

---

# Expected Outcome

After reading MEG-002 contributors should understand:

- why Mosaic is event-driven
- when events should be published
- how events are named
- how subscribers behave
- how retries work
- how failures are handled
- how background workers integrate with the runtime
- how independent modules cooperate without direct dependencies

without discussing any individual business domain.

---

# Repository Structure

```
engineering/

└── meg/

    └── MEG-002 Event-Driven Runtime/

        README.md

        00-document-control.md

        01-runtime-philosophy.md

        02-why-events.md

        03-event-model.md

        04-event-naming.md

        05-event-schema.md

        06-event-versioning.md

        07-event-bus.md

        08-publishers.md

        09-subscribers.md

        10-worker-lifecycle.md

        11-scheduling.md

        12-idempotency.md

        13-retry-strategy.md

        14-event-ordering.md

        15-backpressure.md

        16-correlation-and-observability.md

        17-runtime-shutdown.md

        18-adrs.md

        19-contributor-guidance.md

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MEG-001 Go Engineering Standards
- MDL-002 Principles
- MDL-003 Mental Model

Future companion specifications:

- MEG-003 Domain Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Module Platform
- MEG-006 Runtime Architecture

---

# Design Goals

The Event-Driven Runtime is intended to produce a platform that is:

- Reactive
- Decoupled
- Observable
- Resilient
- Extensible
- Scalable
- Testable
- Deterministic
- Fault tolerant

The runtime should encourage independent capability evolution while preserving architectural consistency across the entire Mosaic ecosystem.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Next File**

`00-document-control.md`
