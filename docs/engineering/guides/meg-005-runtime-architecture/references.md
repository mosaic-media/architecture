<!--
File: docs/engineering/guides/meg-005-runtime-architecture/references.md
Document: MEG-005
Status: Draft
-->

# References

> *The Mosaic Runtime is built upon proven operating system and software architecture principles, adapted into a capability-oriented execution platform.*

---

# Purpose

This document records the primary references that influenced the Runtime Architecture described throughout MEG-005. Unlike previous specifications, MEG-005 draws inspiration from multiple engineering disciplines, including:

- Operating Systems
- Runtime Design
- Event-Driven Systems
- Hexagonal Architecture
- Domain-Driven Design
- Distributed Systems

That breadth follows from the subject matter, because the Runtime is intentionally not modelled after a traditional web framework but after a lightweight execution platform.

---

# Runtime Architecture

## Microkernel Architecture

The Runtime Kernel is heavily influenced by microkernel operating system design.

Relevant concepts include:

- minimal kernel
- service isolation
- explicit ownership
- message-based coordination
- replaceable services

Within Mosaic the Runtime Kernel, the Runtime Services and the Capability Registry all follow this philosophy, which is why the Kernel remains intentionally small while Runtime Services own specialised behaviour.

---

## Operating System Design

General operating system design principles influenced:

- worker management
- scheduling
- lifecycle
- resource ownership
- startup
- shutdown

Those concerns are the ones an operating system solves rather than the ones an application solves, so the Runtime intentionally behaves more like a lightweight operating system than a conventional backend application.

---

# Event-Driven Systems

## Reactive Manifesto

The Runtime adopts many of the ideas described within the Reactive Manifesto.

Examples include:

- responsiveness
- resilience
- elasticity
- message-driven communication

The Runtime Architecture builds upon the execution semantics defined previously in [MEG-002](../meg-002-event-driven-runtime/index.md).

**URL**

https://www.reactivemanifesto.org/

---

## Enterprise Integration Patterns

**Authors**

Gregor Hohpe

Bobby Woolf

Relevant Runtime concepts include:

- message routing
- work dispatch
- retries
- dead-letter handling
- scheduling

The Runtime adapts these ideas while remaining capability oriented.

---

# Hexagonal Architecture

## Hexagonal Architecture

**Author**

Alistair Cockburn

The Runtime itself remains infrastructure, so its relationship with the Domain follows the Ports and Adapters principles established in [MEG-004](../meg-004-hexagonal-architecture/index.md). Runtime Services therefore expose capabilities through contracts rather than direct implementation dependencies.  [Wikipedia](https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29)

---

# Dependency Injection

## Composition Root

**Author**

Mark Seemann

The Runtime Composition Root follows the principles of:

- explicit composition
- dependency injection
- centralised construction
- constructor injection

Every Runtime executable assembles its object graph explicitly during startup.  [blog.ploeh.dk](https://blog.ploeh.dk/2011/07/28/CompositionRoot/)

---

# Distributed Systems

## Designing Data-Intensive Applications

**Author**

Martin Kleppmann

Relevant Runtime concepts include:

- coordination
- failure recovery
- consistency
- event ordering
- operational resilience

Although MEG-005 does not define distributed execution directly, many Runtime design principles were influenced by these ideas.

---

## Release It!

**Author**

Michael T. Nygard

Relevant concepts include:

- graceful degradation
- fault isolation
- operational resilience
- resource protection
- recovery

Many Runtime lifecycle decisions align closely with these operational principles.

---

# Go References

The Runtime Architecture intentionally embraces idiomatic Go, so the following references are recommended.

## Effective Go

Topics include:

- package ownership
- interfaces
- concurrency
- composition

https://go.dev/doc/effective_go

---

## Go Concurrency Patterns

The Go Team

Relevant Runtime concepts include:

- pipelines
- cancellation
- worker coordination
- context propagation

https://go.dev/blog/pipelines

---

## Context

The Go Team

Relevant Runtime concepts include:

- deadlines
- cancellation
- execution lifecycle

https://go.dev/blog/context

---

# Internal Mosaic Specifications

The following specifications complement MEG-005.

## Engineering

- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)
- [MEG-002 — Event-Driven Runtime](../meg-002-event-driven-runtime/index.md)
- [MEG-003 — Domain-Driven Design](../meg-003-domain-driven-design/index.md)
- [MEG-004 — Hexagonal Architecture](../meg-004-hexagonal-architecture/index.md)

---

## Planned Engineering Specifications

- [MEG-006 — Module Platform](../meg-006-module-platform/index.md)
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

# Runtime Principles

The Runtime Architecture established throughout MEG-005 intentionally builds upon several enduring engineering principles, which include:

- Execution belongs to the Runtime.
- Business belongs to capabilities.
- Dependencies remain explicit.
- Runtime Services own one responsibility.
- Resources have explicit ownership.
- Startup is deterministic.
- Shutdown is graceful.
- Runtime state remains operational.
- Runtime components remain replaceable.
- Capabilities grow the platform.
- The Runtime enables the platform.

These principles should remain significantly more stable than the implementation techniques used to realise them.

---

# Keeping References Current

Runtime engineering continues to evolve: scheduling improves, worker models evolve and resource management strategies change. This reference list should therefore be reviewed periodically to ensure:

- architectural guidance remains relevant
- obsolete operational practices are removed
- better runtime techniques are incorporated

The Runtime philosophy should remain stable even as Runtime implementation continues to mature.

---

# Closing Statement

MEG-005 intentionally does not describe a traditional application framework; it describes an execution platform specifically designed for Mosaic. The resulting Runtime Architecture therefore emphasises:

- capability execution
- explicit ownership
- operational simplicity
- modular Runtime Services
- deterministic lifecycle
- replaceable infrastructure

The Runtime exists for one purpose.

> **Provide a stable execution environment in which independently evolving capabilities can safely operate.**

The Runtime should quietly make the platform possible while the platform itself remains the focus.
