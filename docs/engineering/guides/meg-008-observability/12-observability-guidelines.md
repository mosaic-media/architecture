<!--
File: docs/engineering/guides/meg-008-observability/12-observability-guidelines.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Observability Guidelines

> *The easiest platform to operate is the one that explains itself continuously.*

---

# Purpose

The previous chapters established the architectural building blocks of Mosaic Observability:

- Logging
- Metrics
- Distributed Tracing
- Health
- Runtime Diagnostics
- Storage Observability
- Performance Telemetry
- Alerting
- Debugging
- OpenTelemetry

This document combines those concepts into practical engineering guidance.

Its purpose is to answer one question.

> **"How should engineers design observable software?"**

---

# Philosophy

Within Mosaic:

> **Every architectural responsibility should produce corresponding observability.**

Observability is not something added after implementation.

It emerges naturally from:

- ownership
- boundaries
- responsibilities

Well-structured architecture naturally produces well-structured telemetry.

---

# Start With Ownership

Before adding telemetry ask:

> **Who owns this responsibility?**

Examples.

```
Scheduler

↓

Scheduling Metrics
```

```
Worker Manager

↓

Worker Metrics
```

```
Blob Storage

↓

Blob Metrics
```

Telemetry ownership should always mirror architectural ownership.

---

# Observe Architecture

Prefer observing:

- Runtime Services
- Capabilities
- Storage Systems
- Repositories

Avoid observing:

- helper methods
- utility functions
- implementation details

Operators think in terms of architecture.

Telemetry should do the same.

---

# Logs

Before adding a log ask:

> **Is this an architectural event?**

Good.

```
Capability Activated
```

Poor.

```
Entered Function X
```

Logs should describe:

- meaningful transitions
- failures
- recoveries
- lifecycle events

Implementation noise should remain minimal.

---

# Metrics

Metrics should describe trends.

Examples include:

- worker utilisation
- startup duration
- storage growth
- capability latency

Avoid metrics for:

- temporary implementation state
- internal variables
- helper functions

Metrics should survive implementation refactoring.

---

# Traces

Create spans around:

- Runtime boundaries
- capability execution
- repository access
- storage operations

Avoid spans around:

- internal algorithms
- utility methods
- formatting code

Traces should explain:

Execution.

Not implementation.

---

# Health

Health should answer:

> **Can this component currently fulfil its responsibility?**

Avoid using health to communicate:

- business success
- user satisfaction
- implementation correctness

Health remains an operational concept.

---

# Diagnostics

Diagnostics should expose:

- Runtime composition
- dependency graphs
- worker state
- capability state
- storage ownership

Diagnostics should explain architecture.

They should never require reading implementation code.

---

# Performance

Before measuring performance ask:

> **Which architectural responsibility owns this latency?**

Measure:

- Scheduler
- Worker Manager
- Repository
- Storage

Not:

- helper methods
- loops
- utility classes

Performance ownership follows architecture.

---

# Alerts

Alerts should require:

Human judgement.

Avoid alerting for:

- retries
- expected recoveries
- transient failures

The Runtime should solve routine operational problems automatically.

Humans should become involved only when necessary.

---

# Correlation

Every significant Runtime operation SHOULD include:

- trace identifier
- capability identifier
- Runtime service
- operation

Correlation should be automatic.

Operators should never manually combine unrelated telemetry.

---

# Context

Telemetry SHOULD contain enough context to explain itself.

Useful context includes:

- capability
- Runtime Service
- storage engine
- operation
- lifecycle stage

Avoid:

- unnecessary payload data
- business objects
- user information

Context should improve understanding.

Not increase noise.

---

# Business Versus Operations

Maintain a clear distinction.

Business.

```
Playback Completed
```

Operations.

```
Playback Capability Activated
```

Capabilities own business telemetry.

Runtime Services own operational telemetry.

The distinction should remain visible everywhere.

---

# Consistency

Telemetry naming SHOULD remain consistent.

Examples.

```text
runtime.*

capability.*

storage.*
```

Consistency improves:

- discoverability
- dashboards
- alerting
- diagnostics

The platform should feel predictable.

---

# Design For Failure

Ask:

> **If this component fails, how will operators understand why?**

The answer should already exist through:

- logs
- traces
- health
- diagnostics

Failure should become observable naturally.

Not through emergency instrumentation.

---

# Design For Recovery

Recovery deserves telemetry.

Examples include:

- retries
- worker replacement
- cache rebuilds
- migration rollback

Recovery often explains more about platform resilience than failure itself.

Recovery should therefore remain observable.

---

# Design For Operators

Operators should answer questions without:

- source code
- debuggers
- production changes

Every new Runtime Service should expose enough telemetry for operators to understand its behaviour independently.

Architecture should explain itself.

---

# Privacy

Never expose:

- passwords
- secrets
- authentication tokens
- private user information

Observability should improve operational understanding.

Not compromise platform security.

---

# Performance Cost

Observability has a cost.

Before adding telemetry ask:

> **Will this information genuinely improve platform understanding?**

Avoid:

- duplicate metrics
- unnecessary logs
- excessive spans

Collect useful information.

Not merely more information.

---

# Testing

Every new Runtime component SHOULD test:

- logs
- metrics
- traces
- health
- diagnostics

Observability should become part of normal engineering.

Not an operational afterthought.

---

# Documentation

Every significant telemetry surface SHOULD be documented.

Examples include:

- metric names
- health states
- trace attributes
- diagnostic endpoints

Documentation should evolve alongside implementation.

Observability should remain discoverable.

---

# Review Checklist

Before requesting review confirm:

- [ ] Architectural ownership is obvious.
- [ ] Logs describe architectural events.
- [ ] Metrics describe trends.
- [ ] Traces cross Runtime boundaries.
- [ ] Health reflects responsibility.
- [ ] Diagnostics explain architecture.
- [ ] Sensitive information remains protected.
- [ ] Telemetry naming is consistent.
- [ ] Observability remains lightweight.

---

# Common Observability Mistakes

Avoid:

- implementation logging
- duplicate metrics
- missing trace propagation
- health without context
- architecture hidden behind dashboards
- alerts without action
- telemetry ownership ambiguity

These mistakes usually produce noise rather than operational understanding.

---

# Mosaic Guidelines

Within Mosaic:

- Observability MUST follow architectural ownership.
- Runtime and business telemetry MUST remain distinct.
- Logs SHOULD describe architectural events.
- Metrics SHOULD describe behaviour over time.
- Traces SHOULD describe execution journeys.
- Health SHOULD describe operational readiness.
- Diagnostics SHOULD explain Runtime structure.
- Observability SHOULD remain lightweight.
- Architecture SHOULD always be more visible than implementation.

---

# Relationship to MEG

This chapter completes the practical implementation guidance of MEG-008.

The remaining documents describe:

- architectural reasoning (ADRs)
- contributor expectations
- terminology
- references

Together, MEG-001 through MEG-008 now define:

- engineering
- execution
- business modelling
- architecture
- runtime
- platform evolution
- storage
- observability

Every remaining engineering specification builds upon these foundations.

---

# Summary

Good observability is not measured by how much telemetry exists.

It is measured by how quickly someone can understand the platform.

Within Mosaic, every Runtime component should naturally explain:

- what it owns
- what it is doing
- why it is behaving that way

without exposing unnecessary implementation detail.

When architecture and observability become reflections of one another, operating the platform becomes dramatically simpler.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`11-opentelemetry.md`

**Next File**

`13-adrs.md`
