<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/references.md
Document: MEG-002
Status: Draft
Version: 0.3
-->

# References

> *The Mosaic Runtime is built upon established engineering principles, adapted to the unique requirements of an extensible, event-driven media platform.*

---

# Purpose

This document records the primary references that influenced the design of the Mosaic Event-Driven Runtime.

MEG-002 intentionally combines ideas from:

- Event-Driven Architecture
- Distributed Systems
- Reactive Systems
- Go Runtime Design
- Domain-Driven Design
- Cloud Native Architecture

into a cohesive runtime model designed specifically for Mosaic.

The purpose of these references is not to prescribe implementation, but to provide architectural context for the standards defined throughout MEG-002.

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

Gregor Hohpe

Bobby Woolf

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

Defines the characteristics of reactive systems.

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

Martin Kleppmann

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

Michael T. Nygard

**Topics**

- Circuit Breakers
- Stability Patterns
- Bulkheads
- Operational resilience

Many runtime resilience strategies draw inspiration from this work.

---

# Go References

## Effective Go

The Go Team

Primary reference for:

- concurrency
- interfaces
- composition
- package design

https://go.dev/doc/effective_go

---

## Go Concurrency Patterns

The Go Team

Recommended reading for:

- pipelines
- cancellation
- worker coordination

https://go.dev/blog/pipelines

---

## Context

The Go Team

Reference for:

- cancellation
- deadlines
- request lifecycles

https://go.dev/blog/context

---

## Share Memory By Communicating

The Go Team

Reference for Go's concurrency philosophy.

https://go.dev/blog/share-memory-by-communicating

---

# Messaging Patterns

## Idempotent Consumer

Chris Richardson

Reference describing safe event consumption under at-least-once delivery.

https://microservices.io/post/microservices/patterns/2020/10/16/idempotent-consumer.html

---

## Transactional Outbox

Chris Richardson

Reference describing durable event publication after successful state transitions.

https://microservices.io/patterns/data/transactional-outbox.html

---

# Observability

## OpenTelemetry

Reference implementation for:

- traces
- metrics
- logs
- correlation

https://opentelemetry.io/

---

## Prometheus

Recommended operational metrics model.

https://prometheus.io/

---

# Cloud Native References

## Twelve-Factor App

Several operational principles remain applicable.

Examples include:

- configuration
- disposability
- logging
- processes

Not every principle is adopted directly.

However, many complement the runtime architecture.

https://12factor.net/

---

# Internal Mosaic Specifications

The following specifications complement MEG-002.

## Foundation

- MEG-001 Go Engineering Standards

---

## Planned Engineering Specifications

- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Module Platform
- MEG-006 Runtime Architecture
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

The runtime philosophy established throughout MEG-002 is intentionally built upon several enduring architectural principles.

These include:

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

Distributed systems continue to evolve.

Observability continues to evolve.

Go continues to evolve.

This reference list SHOULD therefore be reviewed periodically to ensure that:

- links remain valid
- recommendations remain relevant
- obsolete practices are removed
- better architectural references are incorporated

The architectural philosophy of the runtime should remain stable, even as implementation techniques improve.

---

# Closing Statement

MEG-002 intentionally does not attempt to invent a new event-driven architecture.

Instead, it combines proven ideas from distributed systems, reactive architectures and Go engineering into a runtime specifically designed for the Mosaic platform.

The resulting architecture emphasises:

- autonomy
- simplicity
- resilience
- observability
- extensibility

Every runtime capability should reinforce these properties.

As the Mosaic ecosystem grows, the runtime should continue to feel predictable, understandable and remarkably boring.

That is not a criticism.

For infrastructure, boring is one of the highest compliments an engineer can give.

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
