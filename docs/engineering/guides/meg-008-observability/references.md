<!--
File: docs/engineering/guides/meg-008-observability/references.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# References

> *Observability is not a monitoring tool. It is an architectural property emerging from well-defined ownership, clear boundaries and explicit execution.*

---

# Purpose

This document records the primary references that influenced the Observability Architecture described throughout MEG-008.

Rather than treating observability as a collection of tools, Mosaic approaches it as an architectural discipline built upon:

- Runtime ownership
- Capability ownership
- Storage ownership
- Structured telemetry
- Explainable execution

The references below informed the implementation techniques.

The architectural philosophy remains specific to Mosaic.

---

# Primary References

## OpenTelemetry

OpenTelemetry provides the primary telemetry standard adopted by Mosaic.

Relevant concepts include:

- distributed tracing
- metrics
- structured logging
- context propagation
- vendor neutrality

Within Mosaic:

OpenTelemetry transports telemetry.

The Runtime owns telemetry.

This separation preserves architectural independence from monitoring vendors.

**URL**

https://opentelemetry.io/

---

## OpenTelemetry Specification

Relevant concepts include:

- trace context
- semantic conventions
- metrics model
- log model
- resources

Mosaic intentionally adopts OpenTelemetry as an implementation standard rather than an architectural dependency.

---

# Distributed Tracing

Modern distributed tracing strongly influenced:

- Runtime trace propagation
- capability spans
- storage spans
- event propagation

Within Mosaic:

Tracing follows architectural ownership rather than implementation hierarchy.

The trace should describe:

The architecture.

Not individual helper functions.

---

# Structured Logging

The logging architecture follows established structured logging principles.

Relevant concepts include:

- machine-readable logs
- contextual metadata
- correlation identifiers
- immutable log events

Structured logging allows:

- filtering
- aggregation
- automation

while remaining considerably more useful than free-form logging.

---

# Metrics

Metric design was influenced by modern operational telemetry practices.

Relevant concepts include:

- counters
- gauges
- histograms
- summaries

Mosaic intentionally measures:

architectural responsibilities

rather than:

implementation details.

---

# Health Models

Health modelling draws upon long-established cloud-native operational practices.

Relevant concepts include:

- readiness
- liveness
- dependency health
- graceful degradation

Within Mosaic:

Health remains distinct from:

- alerts
- diagnostics
- traces

Each describes a different operational concern.

---

# Explainability

One of the strongest influences behind MEG-008 is the idea that:

A Runtime should explain itself.

This principle appears repeatedly throughout:

- Runtime Diagnostics
- dependency graphs
- capability inspection
- Runtime snapshots

Rather than relying upon source code or debugger sessions.

Explainability is treated as a core architectural responsibility.

---

# Domain-Driven Design

Eric Evans

Relevant concepts include:

- ownership
- bounded contexts
- ubiquitous language

Observability ownership intentionally follows the same ownership boundaries established within MEG-003.

Every capability owns its own telemetry.

---

# Hexagonal Architecture

Alistair Cockburn

Observability reinforces dependency direction.

The Domain remains independent of:

- logging frameworks
- telemetry exporters
- monitoring systems

Infrastructure adapts observability around the Domain rather than embedding telemetry into business logic.

---

# Runtime Architecture

MEG-005 strongly influences observability.

Examples include:

- Runtime Services
- Worker Manager
- Scheduler
- Execution Engine
- Capability Registry

Observability follows the Runtime Architecture rather than creating an independent operational model.

The Runtime explains itself through telemetry.

---

# Storage Architecture

MEG-007 influences storage observability.

Examples include:

- Business State
- Analytical State
- Binary Assets
- Derived Assets

Storage telemetry follows information ownership rather than database implementation.

This preserves the Storage Taxonomy even within operational tooling.

---

# Go References

The Observability Architecture intentionally embraces idiomatic Go.

Recommended references include:

## Effective Go

Topics include:

- interfaces
- composition
- package ownership

https://go.dev/doc/effective_go

---

## Go Context

Relevant concepts include:

- cancellation
- deadlines
- request propagation
- execution context

Context propagation naturally complements distributed tracing.

https://go.dev/blog/context

---

## Go Concurrency Patterns

Relevant concepts include:

- pipelines
- worker coordination
- cancellation

These patterns strongly influence Runtime tracing and execution telemetry.

https://go.dev/blog/pipelines

---

# Internal Mosaic Specifications

The following specifications complement MEG-008.

## Engineering

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Capability Runtime
- MEG-006 Extension Platform
- MEG-007 Storage Architecture

---

## Planned Engineering Specifications

- MEG-009 Security
- MEG-010 Performance Engineering
- MEG-011 Deployment Architecture
- MEG-012 API Architecture

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

# Observability Principles

The Observability Architecture established throughout MEG-008 intentionally builds upon several enduring principles.

These include:

- Architecture owns telemetry.
- Runtime ownership determines telemetry ownership.
- Logs describe architectural events.
- Metrics describe behavioural trends.
- Traces describe execution journeys.
- Health describes operational readiness.
- Diagnostics describe Runtime structure.
- OpenTelemetry transports telemetry.
- Observability should explain the platform rather than merely record it.
- Operators should understand architecture without reading implementation.

These principles should remain considerably more stable than the telemetry frameworks implementing them.

---

# Keeping References Current

Observability tooling continues to evolve rapidly.

Telemetry standards improve.

Tracing systems mature.

Operational practices change.

This reference list SHOULD therefore be reviewed periodically to ensure:

- guidance remains relevant
- obsolete practices are removed
- improved observability techniques are incorporated

The architectural philosophy should remain stable even as operational tooling evolves.

---

# Closing Statement

MEG-008 intentionally does not define dashboards.

Nor does it prescribe a particular monitoring vendor.

Instead, it defines an architectural philosophy in which:

- Runtime ownership
- capability ownership
- storage ownership

naturally produce:

- logs
- metrics
- traces
- health
- diagnostics

The result is a platform that continuously explains itself through the same architectural boundaries that govern its execution.

When architecture and observability become reflections of one another, operations becomes dramatically simpler.

The Runtime already knows what it is doing.

Observability simply allows everyone else to know it too.

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
