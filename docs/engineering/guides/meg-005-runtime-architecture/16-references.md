<!--
File: engineering/meg/MEG-005 Runtime Architecture/16-references.md
Document: MEG-005
Status: Draft
Version: 0.1
-->

# References

> *The Mosaic Runtime is built upon proven operating system and software architecture principles, adapted into a capability-oriented execution platform.*

---

# Purpose

This document records the primary references that influenced the Runtime Architecture described throughout MEG-005.

Unlike previous specifications, MEG-005 draws inspiration from multiple engineering disciplines, including:

- Operating Systems
- Runtime Design
- Event-Driven Systems
- Hexagonal Architecture
- Domain-Driven Design
- Distributed Systems

The Runtime is intentionally not modelled after a traditional web framework.

Instead, it is modelled after a lightweight execution platform.

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

Within Mosaic:

- Runtime Kernel
- Runtime Services
- Capability Registry

all follow this philosophy.

The Kernel remains intentionally small while Runtime Services own specialised behaviour.

---

## Operating System Design

General operating system design principles influenced:

- worker management
- scheduling
- lifecycle
- resource ownership
- startup
- shutdown

The Runtime intentionally behaves more like a lightweight operating system than a conventional backend application.

---

# Event-Driven Systems

## Reactive Manifesto

The Runtime adopts many of the ideas described within the Reactive Manifesto.

Examples include:

- responsiveness
- resilience
- elasticity
- message-driven communication

The Runtime Architecture builds upon the execution semantics defined previously in MEG-002.

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

The Runtime itself remains infrastructure.

Its relationship with the Domain follows the Ports and Adapters principles established in MEG-004.

Runtime Services expose capabilities through contracts rather than direct implementation dependencies.  [oai_citation:0‡Wikipedia](https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29?utm_source=chatgpt.com)

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

Every Runtime executable assembles its object graph explicitly during startup.  [oai_citation:1‡blog.ploeh.dk](https://blog.ploeh.dk/2011/07/28/CompositionRoot/?utm_source=chatgpt.com)

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

The Runtime Architecture intentionally embraces idiomatic Go.

Recommended references include:

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

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture

---

## Planned Engineering Specifications

- MEG-006 Extension Platform
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

# Runtime Principles

The Runtime Architecture established throughout MEG-005 intentionally builds upon several enduring engineering principles.

These include:

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

Runtime engineering continues to evolve.

Scheduling improves.

Worker models evolve.

Resource management strategies change.

This reference list SHOULD therefore be reviewed periodically to ensure:

- architectural guidance remains relevant
- obsolete operational practices are removed
- better runtime techniques are incorporated

The Runtime philosophy should remain stable even as Runtime implementation continues to mature.

---

# Closing Statement

MEG-005 intentionally does not describe a traditional application framework.

Instead, it describes an execution platform specifically designed for Mosaic.

The resulting Runtime Architecture intentionally emphasises:

- capability execution
- explicit ownership
- operational simplicity
- modular Runtime Services
- deterministic lifecycle
- replaceable infrastructure

The Runtime exists for one purpose.

> **Provide a stable execution environment in which independently evolving capabilities can safely operate.**

The Runtime should quietly make the platform possible.

The platform itself should remain the focus.

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
