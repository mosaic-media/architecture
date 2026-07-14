<!--
File: docs/engineering/guides/meg-008-observability/03-metrics.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Metrics

> *Logs explain individual events. Metrics reveal long-term behaviour.*

---

# Purpose

Individual log entries answer questions about specific moments in time.

Metrics answer questions such as:

- Is the Runtime becoming slower?
- Are workers approaching capacity?
- Is storage growing unexpectedly?
- Which capability consumes the most resources?
- Has recommendation generation improved?

Metrics transform isolated observations into measurable behaviour over time.

Within Mosaic, metrics are the primary mechanism through which the health and evolution of the platform become visible.

---

# Philosophy

Within Mosaic:

> **Measure architecture, not implementation.**

Metrics should describe:

- Runtime behaviour
- capability behaviour
- storage behaviour
- platform behaviour

They should not describe:

- individual functions
- individual algorithms
- temporary implementation details

Metrics should survive implementation changes.

---

# Metrics Describe Trends

Unlike logs:

```
One Event

↓

One Log
```

Metrics describe:

```
Thousands Of Events

↓

One Trend
```

Example.

```
Worker Utilisation

↓

74%
```

The metric summarises Runtime behaviour over time.

Not one execution.

---

# Metric Ownership

Metrics follow architectural ownership.

Examples.

```
Worker Manager

↓

Worker Metrics
```

```
Scheduler

↓

Scheduling Metrics
```

```
Capability Registry

↓

Capability Metrics
```

Every Runtime component owns the metrics describing its responsibilities.

Ownership should remain explicit.

---

# Four Metric Types

The Runtime SHOULD primarily expose four metric categories.

```text
Counters
```

Monotonically increasing values.

```text
Gauges
```

Current state.

```text
Histograms
```

Distribution.

```text
Summaries
```

Statistical observations.

Each solves a different operational problem.

---

# Counters

Counters represent totals.

Examples include:

- capabilities activated
- workers created
- Runtime Events published
- storage migrations
- backup executions

Counters never decrease.

They describe historical activity.

---

# Gauges

Gauges describe current Runtime state.

Examples include:

- active workers
- queue depth
- connected clients
- loaded capabilities
- blob storage usage

Gauges change continuously.

They describe:

> **What is true right now?**

---

# Histograms

Histograms describe distributions.

Examples include:

- execution duration
- query latency
- activation time
- startup duration
- storage latency

Histograms answer:

> **How long does this usually take?**

rather than:

> **How long did one execution take?**

Histograms are particularly valuable because they preserve latency distributions rather than only averages.

---

# Summaries

Summaries provide statistical observations.

Examples include:

- average worker utilisation
- average startup time
- average recommendation latency

Summaries help operators understand platform behaviour at a glance.

They should complement, not replace, histograms.

---

# Runtime Metrics

The Runtime SHOULD expose metrics describing:

- startup
- shutdown
- scheduling
- execution
- workers
- resources
- dependency resolution

The Runtime already understands these concepts.

Metrics simply expose them.

---

# Capability Metrics

Every capability SHOULD expose metrics describing:

- execution count
- execution duration
- failures
- retries
- health

Capabilities should not expose Runtime implementation metrics.

Those belong to Runtime Services.

Capability metrics should describe business operations.

---

# Storage Metrics

Storage systems SHOULD expose:

- transaction latency
- query duration
- cache hit ratio
- blob utilisation
- rebuild duration
- migration progress

Storage metrics should describe storage behaviour.

Not SQL internals.

---

# Event Metrics

Runtime Events naturally produce metrics.

Examples include:

```
Events Published
```

```
Events Delivered
```

```
Events Failed
```

```
Events Retried
```

These metrics help operators understand Runtime throughput.

Not business correctness.

---

# Worker Metrics

The Worker Manager SHOULD expose:

- worker count
- active workers
- idle workers
- utilisation
- failures
- replacements

Worker metrics describe Runtime capacity.

They should remain independent of business capabilities.

---

# Scheduler Metrics

The Scheduler SHOULD expose:

- scheduled work
- delayed work
- missed schedules
- execution latency
- recurring schedules

Scheduling metrics answer:

> **Is the Runtime keeping time correctly?**

---

# Capability Registry Metrics

The Capability Registry SHOULD expose:

- registered capabilities
- active capabilities
- failed activations
- dependency failures
- version conflicts

Operators should understand platform composition continuously.

---

# Resource Metrics

The Resource Manager SHOULD expose:

- CPU usage
- memory usage
- worker utilisation
- queue capacity
- connection pools

Resource metrics should help answer:

> **Can the Runtime continue accepting work?**

---

# Label Strategy

Metrics SHOULD use stable labels.

Examples include:

```text
capability="metadata"
```

```text
storage="postgres"
```

```text
worker_pool="default"
```

Labels should remain:

- low cardinality
- stable
- predictable

Avoid high-cardinality labels such as:

- user IDs
- filenames
- request payloads

High-cardinality metrics become expensive to store and query while providing little operational value.

---

# Naming

Metric names SHOULD follow consistent naming conventions.

Examples.

```text
runtime_workers_active
```

```text
capability_activation_duration_seconds
```

```text
storage_blob_objects_total
```

Names should describe:

- owner
- subject
- measurement

Consistency improves discoverability.

---

# Units

Every metric SHOULD use explicit units.

Examples include:

- seconds
- bytes
- requests
- events
- workers

Units should never require interpretation.

The metric itself should communicate what is being measured.

---

# Metric Lifetime

Metrics exist only while meaningful.

Examples.

```
Worker Utilisation

↓

Runtime Lifetime
```

```
Migration Duration

↓

Migration Only
```

Metrics should disappear naturally when their architectural responsibility ends.

---

# Aggregation

Metrics SHOULD aggregate naturally.

Examples.

```
Worker

↓

Worker Pool

↓

Runtime
```

```
Capability

↓

Capability Group

↓

Platform
```

Aggregation should follow architectural ownership.

Not implementation hierarchy.

---

# Observability Integration

Metrics complement:

- logs
- traces
- diagnostics

Metrics answer:

> **Is something changing?**

Logs explain:

> **What changed?**

Traces explain:

> **How did it change?**

Each telemetry type exists because it answers a different operational question.

---

# Performance

Metric collection SHOULD remain inexpensive.

Avoid:

- allocating objects per measurement
- synchronous reporting
- expensive calculations

The Runtime should spend more time executing capabilities than measuring them.

Observability should remain proportional to operational value.

---

# Anti-Patterns

The following practices are prohibited.

## Business IDs

Using user IDs or media IDs as metric labels.

---

## Function Metrics

Publishing metrics for individual helper functions.

---

## Duplicate Metrics

Multiple Runtime Services publishing the same measurement.

---

## Missing Units

Publishing values without explicit measurement units.

---

## Metric Spam

Publishing every conceivable measurement regardless of operational usefulness.

---

## Hidden Ownership

Metrics whose owner cannot be identified.

---

# Mosaic Guidelines

Within Mosaic:

- Metrics MUST follow architectural ownership.
- Metrics SHOULD describe trends rather than events.
- Counters, gauges and histograms SHOULD be preferred.
- Labels MUST remain stable and low cardinality.
- Units MUST be explicit.
- Runtime and capability metrics MUST remain distinct.
- Storage metrics SHOULD describe storage behaviour.
- Metrics SHOULD complement logs and traces rather than replace them.

---

# Relationship to MEG

Structured Logging records:

> **Individual architectural events.**

Metrics describe:

> **Architectural behaviour over time.**

The next chapter introduces **Distributed Tracing**, describing how Mosaic follows one unit of work across Runtime Services, capabilities and storage systems from beginning to end.

---

# Summary

Metrics transform the platform from something that merely runs into something that can be measured.

Within Mosaic, every significant architectural component should expose metrics describing:

- capacity
- performance
- utilisation
- health
- behaviour

Because if the Runtime cannot measure itself over time, it cannot know whether it is improving or slowly drifting towards failure.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`02-logging.md`

**Next File**

`04-distributed-tracing.md`
