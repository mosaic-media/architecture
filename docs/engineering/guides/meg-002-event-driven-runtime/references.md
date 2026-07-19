<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/references.md
Document: MEG-002
Status: Draft
-->

# References

> *The Mosaic Runtime is built upon established engineering principles, adapted to the unique requirements of an extensible, event-driven media platform.*

---

# Purpose

This document records the primary references that influenced the design of the Mosaic Event-Driven Runtime. MEG-002 intentionally combines ideas from:

- Event-Driven Architecture
- Distributed Systems
- Reactive Systems
- Go Runtime Design
- Domain-Driven Design
- Cloud Native Architecture

into a cohesive runtime model designed specifically for Mosaic. The purpose of these references is not to prescribe implementation, but to provide architectural context for the standards defined throughout MEG-002.

---

# Event-Driven Architecture

## Martin Fowler — Event-Driven Architecture

**Purpose**

Introduces the concepts of:

- Event Notification
- Event-Carried State Transfer
- Event Sourcing
- CQRS

Mosaic adopts the philosophy of autonomous components communicating through immutable facts while deliberately avoiding unnecessary complexity such as mandatory event sourcing.

**URL**

https://martinfowler.com/articles/201701-event-driven.html

---

## Enterprise Integration Patterns

**Authors**

Gregor Hohpe and Bobby Woolf.

**Topics**

- Message Channels
- Message Routing
- Dead Letter Queues
- Correlation
- Aggregation
- Retry
- Message Transformation

Many runtime concepts used within MEG-002 originate from these messaging patterns.

---

# Reactive Systems

## The Reactive Manifesto

**Purpose**

Defines the characteristics of reactive systems, which are:

- Responsive
- Resilient
- Elastic
- Message Driven

Although Mosaic is not a Reactive Streams implementation, these principles strongly influenced the runtime architecture.

**URL**

https://www.reactivemanifesto.org/

---

# Distributed Systems

## Designing Data-Intensive Applications

**Author**

Martin Kleppmann.

**Topics**

- Distributed coordination
- Event logs
- Consistency
- Replication
- Ordering
- Fault tolerance

This work heavily influenced:

- event versioning
- retries
- idempotency
- ordering philosophy
- replay

---

## Release It!

**Author**

Michael T. Nygard.

**Topics**

- Circuit Breakers
- Stability Patterns
- Bulkheads
- Operational resilience

Many runtime resilience strategies draw inspiration from this work.

---

# Go References

## Effective Go

The Go Team. Primary reference for concurrency, interfaces, composition and package design, available at https://go.dev/doc/effective_go

---

## Go Concurrency Patterns

The Go Team. Recommended reading for pipelines, cancellation and worker coordination, available at https://go.dev/blog/pipelines

---

## Context

The Go Team. Reference for cancellation, deadlines and request lifecycles, available at https://go.dev/blog/context

---

## Share Memory By Communicating

The Go Team. Reference for Go's concurrency philosophy, available at https://go.dev/blog/share-memory-by-communicating

---

# Messaging Patterns

## Idempotent Consumer

Chris Richardson. Reference describing safe event consumption under at-least-once delivery, available at https://microservices.io/post/microservices/patterns/2020/10/16/idempotent-consumer.html

---

## Transactional Outbox

Chris Richardson. Reference describing durable event publication after successful state transitions, available at https://microservices.io/patterns/data/transactional-outbox.html

---

# Observability

## OpenTelemetry

Reference implementation for traces, metrics, logs and correlation, available at https://opentelemetry.io/

---

## Prometheus

Recommended operational metrics model, available at https://prometheus.io/

---

# Cloud Native References

## Twelve-Factor App

Several operational principles remain applicable, examples of which include:

- configuration
- disposability
- logging
- processes

Not every principle is adopted directly, but many complement the runtime architecture. The reference is available at https://12factor.net/

---

# Internal Mosaic Specifications

The following specifications complement MEG-002.

## Foundation

- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)

---

## Engineering Specifications

- [MEG-003 — Domain-Driven Design](../meg-003-domain-driven-design/index.md)
- [MEG-004 — Hexagonal Architecture](../meg-004-hexagonal-architecture/index.md)
- [MEG-005 — Runtime Architecture](../meg-005-runtime-architecture/index.md)
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
- [MDS-008 — Component Library](../../../design/system/mds-008-component-library/index.md)

---

## Mosaic Design Proposals

- [MDP-001 — Adaptive Composition Runtime](../../architecture/mdp-001-adaptive-composition-runtime/index.md)
- [MDP-001 ch14 — Adaptive Tile Model](../../architecture/mdp-001-adaptive-composition-runtime/14-adaptive-tile-model.md)

---

# Runtime Principles

The runtime philosophy established throughout MEG-002 is intentionally built upon several enduring architectural principles. These include:

- Components own behaviour.
- Events describe facts.
- Runtime owns coordination.
- Time belongs to infrastructure.
- Failures are expected.
- Delivery is independent.
- Capabilities remain autonomous.
- Observability is built-in.
- Graceful degradation is preferred over catastrophic failure.
- Simplicity scales better than cleverness.

These principles should be considered more important than any individual implementation technique.

---

# Keeping References Current

Distributed systems continue to evolve, observability continues to evolve and Go continues to evolve. This reference list should therefore be reviewed periodically to ensure that:

- links remain valid
- recommendations remain relevant
- obsolete practices are removed
- better architectural references are incorporated

The architectural philosophy of the runtime should remain stable, even as implementation techniques improve.

---

# Closing Statement

MEG-002 intentionally does not attempt to invent a new event-driven architecture. Instead, it combines proven ideas from distributed systems, reactive architectures and Go engineering into a runtime specifically designed for the Mosaic platform. The resulting architecture emphasises:

- autonomy
- simplicity
- resilience
- observability
- extensibility

Every runtime capability should reinforce these properties. As the Mosaic ecosystem grows, the runtime should continue to feel predictable, understandable and remarkably boring, and that is not a criticism: for infrastructure, boring is one of the highest compliments an engineer can give.
