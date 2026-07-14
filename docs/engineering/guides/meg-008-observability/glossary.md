<!--
File: engineering/meg/MEG-008 Observability/glossary.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Glossary

> *Observability succeeds when every engineer uses the same language to describe what the platform is doing.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Observability specification.

These definitions establish the canonical observability vocabulary for:

- Runtime documentation
- Operational tooling
- Architecture specifications
- SDK documentation
- Contributor guidance
- Support procedures

Where a term has a specific meaning within Mosaic, that definition takes precedence over informal usage.

---

# A

## Alert

An operational notification indicating that human intervention may be required.

Alerts are derived from:

- metrics
- health
- diagnostics
- traces

Alerts do **not** represent business events.

---

## Alert Correlation

The process of combining multiple related operational failures into one meaningful alert.

Alert correlation reduces operational noise while preserving architectural context.

---

# D

## Diagnostic

Read-only Runtime information describing the current architectural state of the platform.

Diagnostics expose:

- Runtime composition
- dependency graphs
- worker state
- capability state
- storage ownership

Diagnostics explain architecture.

They do not execute business behaviour.

---

## Distributed Trace

The complete execution journey of one logical operation across multiple Runtime components.

A distributed trace consists of:

- one Trace
- multiple Spans
- optional Events

---

# E

## Event

A significant occurrence recorded within a Trace.

Events provide additional detail inside a Span.

Events differ from:

- Runtime Events
- Domain Events

which represent architectural concepts elsewhere within the platform.

---

# H

## Health

The operational readiness of a Runtime component.

Examples include:

- Starting
- Ready
- Healthy
- Degraded
- Unavailable

Health answers:

> **Can this component currently fulfil its architectural responsibility?**

---

## Health Propagation

The process through which component health contributes to higher-level platform health.

Example.

```text
Blob Storage

↓

Metadata Capability

↓

Platform
```

Health follows dependency relationships.

---

# L

## Log

A structured record describing a significant architectural event.

Logs answer:

> **What happened?**

Logs remain distinct from:

- metrics
- traces
- diagnostics

---

# M

## Metric

A numerical observation describing Runtime behaviour over time.

Metrics answer:

> **How is the platform behaving?**

Metric types include:

- Counter
- Gauge
- Histogram
- Summary

---

# O

## Observability

The architectural capability allowing operators to understand:

- Runtime behaviour
- platform health
- execution
- storage
- capabilities

without modifying the platform.

Observability emerges naturally from well-defined architectural ownership.

---

## OpenTelemetry

A vendor-neutral telemetry transport standard.

Within Mosaic:

The Runtime owns telemetry.

OpenTelemetry exports telemetry.

It is implementation infrastructure.

Not observability architecture.

---

# P

## Performance Telemetry

Observability describing:

- latency
- throughput
- utilisation
- capacity

Performance telemetry measures architectural behaviour rather than implementation detail.

---

# R

## Readiness

The state indicating that a Runtime component is prepared to begin accepting work.

Readiness precedes:

Healthy.

A component may be:

Ready.

↓

Degraded.

The two concepts remain distinct.

---

## Runtime Diagnostics

The collection of Runtime inspection interfaces exposing:

- dependency graphs
- Runtime Services
- workers
- storage
- capabilities

Diagnostics remain read-only.

They explain Runtime structure.

---

# S

## Sampling

The process of exporting only a subset of traces.

Sampling reduces telemetry cost while preserving operational insight.

Sampling policy belongs to operations.

Not capabilities.

---

## Span

One architectural unit of work within a Trace.

Examples include:

- Capability Execution
- Repository Save
- Worker Allocation
- Blob Download

Every Span belongs to exactly one Trace.

---

## Structured Logging

Logging using machine-readable fields rather than free-form text.

Structured logging supports:

- filtering
- indexing
- correlation
- automation

It forms the foundation of Runtime logging within Mosaic.

---

# T

## Telemetry

Operational information produced by the platform.

Telemetry includes:

- logs
- metrics
- traces
- health

Telemetry belongs to the Runtime.

Monitoring systems consume it.

---

## Trace

The complete execution history of one logical operation.

A Trace consists of:

- Spans
- Events
- Context

Traces explain execution journeys across Runtime boundaries.

---

## Trace Context

Metadata propagated alongside execution.

Typically includes:

- trace identifier
- span identifier
- correlation metadata

Trace context allows distributed execution to remain observable.

---

# U

## Utilisation

A measurement describing current resource usage.

Examples include:

- worker utilisation
- CPU utilisation
- queue utilisation

Utilisation differs from:

Capacity.

A resource may be:

90% utilised.

while still possessing:

10% remaining capacity.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| API | Application Programming Interface |
| OTel | OpenTelemetry |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SDK | Software Development Kit |
| SLI | Service Level Indicator |
| SLO | Service Level Objective |
| SLA | Service Level Agreement |
| UUID | Universally Unique Identifier |

---

# Relationship to MEG-008

This glossary supports every document within the Observability specification.

Definitions should remain consistent across:

- Runtime documentation
- SDK documentation
- operational runbooks
- dashboard documentation
- Architecture Specifications

Whenever observability terminology evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`14-contributor-guidance.md`

**Next File**

`references.md`
