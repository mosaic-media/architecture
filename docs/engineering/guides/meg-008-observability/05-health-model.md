<!--
File: engineering/meg/MEG-008 Observability/05-health-model.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Health Model

> *Health does not mean "nothing is wrong." Health means "this component can currently fulfil its architectural responsibility."*

---

# Purpose

A Runtime consists of many independently operating components.

Examples include:

- Runtime Kernel
- Scheduler
- Worker Manager
- Execution Engine
- Capability Registry
- Capabilities
- Storage Systems

Operators require a consistent mechanism for determining whether these components remain operational.

This mechanism is the **Health Model**.

Health exists to communicate operational readiness.

Not business correctness.

---

# Philosophy

Within Mosaic:

> **Health follows responsibility.**

Every Runtime component owns one responsibility.

Health answers one question.

> **Can this component currently perform that responsibility?**

Nothing more.

---

# Health Is Not Monitoring

Health is frequently confused with:

- logs
- metrics
- alerts

These are related.

They are not identical.

Examples.

Logs answer:

> **What happened?**

Metrics answer:

> **How is behaviour changing?**

Traces answer:

> **How did this execution flow?**

Health answers:

> **Can this component currently operate?**

Each solves a different operational problem.

---

# Health Hierarchy

Health follows the architecture.

```text
Platform

↓

Runtime

↓

Runtime Services

↓

Capabilities

↓

Storage
```

Every layer exposes health independently.

Platform health emerges from these individual assessments.

---

# Health States

Every Runtime component SHOULD expose one of the following states.

```text
Unknown
```

Component has not yet been evaluated.

```text
Starting
```

Initialisation is in progress.

```text
Ready
```

Prepared to accept work.

```text
Healthy
```

Operating normally.

```text
Degraded
```

Operating with reduced capability.

```text
Unavailable
```

Unable to fulfil its responsibility.

```text
Stopping
```

Participating in Runtime shutdown.

These states should remain consistent throughout the platform.

---

# Readiness

Readiness answers:

> **Can this component begin accepting work?**

Examples.

```
Scheduler

↓

Ready
```

```
Capability

↓

Ready
```

Readiness occurs before:

```
Healthy
```

A component may be:

Ready.

↓

Healthy.

or

Ready.

↓

Immediately Degraded.

The two concepts remain distinct.

---

# Liveness

Liveness answers:

> **Does this component still exist and respond?**

A live component is not necessarily healthy.

Example.

```
Metadata Capability

↓

Responding

↓

External API Offline
```

The capability is:

- live
- degraded

Liveness should not imply correctness.

---

# Health Ownership

Every Runtime component owns its own health.

Examples.

```
Scheduler

↓

Scheduling Health
```

```
Worker Manager

↓

Worker Health
```

```
Blob Storage

↓

Blob Health
```

No component should report the health of another.

Ownership should remain explicit.

---

# Runtime Health

The Runtime Kernel SHOULD aggregate Runtime health.

Typical Runtime Services include:

- Scheduler
- Worker Manager
- Execution Engine
- Resource Manager
- Capability Registry

Each reports independently.

The Kernel aggregates.

The Kernel should not invent health.

---

# Capability Health

Every capability SHOULD expose health.

Typical considerations include:

- configuration loaded
- dependencies satisfied
- external providers available
- internal processing operational

Capabilities determine their own operational readiness.

The Runtime reports it.

---

# Storage Health

Storage systems SHOULD expose independent health.

Examples.

```
PostgreSQL

↓

Healthy
```

```
DuckDB

↓

Healthy
```

```
Blob Storage

↓

Degraded
```

Storage failures should remain isolated.

Platform health should reflect those failures accurately.

---

# Dependency Awareness

Health naturally follows dependency relationships.

Example.

```text
Blob Storage

↓

Unavailable
```

↓

```text
Metadata Capability

↓

Degraded
```

↓

```text
Platform

↓

Degraded
```

The Runtime should derive health through the dependency graph rather than hard-coded rules.

This makes the health model naturally extensible.

---

# Health Propagation

Health propagates upward.

```text
Worker

↓

Worker Manager

↓

Runtime

↓

Platform
```

Propagation should remain deterministic.

The Runtime should explain:

> **Why is Platform Health degraded?**

Health should never become a black box.

---

# Critical Versus Optional

Not every dependency has equal importance.

Required dependency.

```text
PostgreSQL

↓

Unavailable

↓

Platform Unavailable
```

Optional dependency.

```text
Recommendation Capability

↓

Unavailable

↓

Platform Healthy

↓

Capability Degraded
```

Capability manifests SHOULD identify whether dependencies are:

- required
- optional

The health model should respect that distinction.

---

# External Dependencies

Capabilities frequently depend upon external services.

Examples include:

- TMDB
- AniList
- Trakt

Loss of one external provider should normally produce:

```text
Capability

↓

Degraded
```

rather than:

```text
Platform

↓

Unavailable
```

External dependency failures should remain isolated wherever practical.

---

# Startup Health

During startup.

```text
Starting

↓

Ready

↓

Healthy
```

The Runtime should not report:

Healthy.

before startup completes.

Operators should distinguish:

"Starting"

from:

"Broken."

---

# Shutdown Health

During shutdown.

```text
Healthy

↓

Stopping

↓

Unavailable
```

Shutdown should be visible through the health model.

Components should stop accepting work before becoming unavailable.

---

# Health Checks

Health checks SHOULD remain lightweight.

Avoid:

- expensive queries
- large allocations
- deep diagnostics

Health determines operational readiness.

Diagnostics explain detailed behaviour.

These concerns should remain separate.

---

# Health Endpoints

The Runtime SHOULD expose:

```text
Platform Health
```

```text
Runtime Health
```

```text
Capability Health
```

```text
Storage Health
```

Operators should inspect the platform at multiple architectural levels.

One health endpoint is rarely sufficient.

---

# Health Metadata

Health responses SHOULD include:

- state
- timestamp
- component
- version
- dependencies
- reason

Example.

```json
{
  "component": "metadata",
  "status": "degraded",
  "reason": "tmdb unavailable"
}
```

Health should explain itself.

Not merely report status.

---

# Observability Integration

Health complements:

- logs
- metrics
- traces

Health identifies:

> **There is a problem.**

Tracing explains:

> **Where the problem occurred.**

Logs explain:

> **What happened.**

Metrics explain:

> **How long it has existed.**

Together they provide complete operational understanding.

---

# Performance

Health evaluation SHOULD remain inexpensive.

Health checks should not become one of the Runtime's largest workloads.

The Runtime should spend its resources executing capabilities.

Not evaluating itself.

---

# Testing

Health SHOULD be testable.

Typical tests verify:

- startup transitions
- dependency propagation
- degradation
- recovery
- shutdown

Health behaviour should remain deterministic.

Operators should trust health.

---

# Anti-Patterns

The following practices are prohibited.

## Boolean Health

Returning only:

```text
Healthy

↓

True
```

Health requires context.

---

## Business Health

Using business success to determine Runtime health.

---

## Hidden Dependencies

Health depending upon undocumented Runtime relationships.

---

## Expensive Health Checks

Running analytical queries or large storage scans.

---

## Shared Health Ownership

Multiple Runtime components reporting conflicting health.

---

## Permanent Healthy

Components reporting "Healthy" regardless of operational state.

---

# Mosaic Guidelines

Within Mosaic:

- Every Runtime component MUST expose health.
- Health MUST follow architectural ownership.
- Readiness and health MUST remain distinct.
- Health SHOULD propagate through dependency relationships.
- Optional dependencies SHOULD degrade capabilities rather than the platform.
- Health responses SHOULD explain their state.
- Health evaluation MUST remain lightweight.
- Health MUST complement logs, metrics and traces.

---

# Relationship to MEG

Distributed Tracing explains:

> **How work moved through the platform.**

The Health Model explains:

> **Whether the platform is currently capable of performing that work.**

The next chapter introduces **Runtime Diagnostics**, defining how Mosaic exposes its internal architecture, dependency graph and execution state for operators and developers.

---

# Summary

Health is not simply:

> **Working**

or

> **Broken**

Within Mosaic, health is an architectural property.

Every Runtime component knows:

- its responsibility
- its dependencies
- its operational state

The health model simply makes that knowledge visible.

When operators understand not only that something is unhealthy, but *why*, the platform has become genuinely observable.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`04-distributed-tracing.md`

**Next File**

`06-runtime-diagnostics.md`
