<!--
File: docs/engineering/guides/meg-008-observability/04-distributed-tracing.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Distributed Tracing

> *Logs describe what happened. Metrics describe how the platform behaves. Traces explain how one piece of work travelled through the entire system.*

---

# Purpose

Mosaic is an event-driven, capability-oriented platform.

A single user action may involve:

- HTTP
- Runtime
- Scheduler
- Execution Engine
- Worker Manager
- Capability
- Repository
- PostgreSQL
- DuckDB
- Blob Storage

Without tracing, operators see isolated events.

Tracing connects those events into one coherent execution story.

Distributed Tracing provides end-to-end visibility across every architectural boundary.

---

# Philosophy

Within Mosaic:

> **Every unit of work should produce one trace.**

A trace should describe:

- where work originated
- which Runtime Services participated
- which capabilities executed
- which storage systems were accessed
- where latency occurred
- where failures happened

The platform should explain one execution from beginning to end.

---

# What Is A Trace?

A trace is the complete execution journey of one logical operation.

Example.

```text
User Request

↓

Playback Capability

↓

Repository

↓

PostgreSQL

↓

PlaybackCompleted

↓

Runtime

↓

Recommendation Capability

↓

DuckDB

↓

Response
```

Although multiple Runtime components participate:

The operator sees one trace.

---

# Trace Hierarchy

Every trace consists of:

```text
Trace

↓

Spans

↓

Events
```

The Trace represents:

The entire journey.

A Span represents:

One architectural responsibility.

Events provide additional detail within spans.

---

# Trace Ownership

Trace ownership follows execution.

The component performing work owns the span describing that work.

Example.

```
Scheduler

↓

Scheduling Span
```

```
Execution Engine

↓

Execution Span
```

```
Repository

↓

Persistence Span
```

Each architectural component describes its own responsibility.

No component should describe another's.

---

# Trace Identity

Every trace MUST possess a globally unique identifier.

Example.

```text
trace_id
```

Every span belongs to exactly one trace.

Trace identity allows operators to correlate:

- logs
- metrics
- spans
- diagnostics

into one operational narrative.

---

# Span Identity

Every architectural operation SHOULD become one span.

Examples include:

```text
Capability Activation
```

```text
Repository Save
```

```text
Blob Fetch
```

```text
DuckDB Query
```

Spans should represent meaningful architectural work.

Not implementation details.

---

# Parent-Child Relationships

Spans naturally form a hierarchy.

```text
HTTP Request

↓

Playback Capability

↓

Repository

↓

PostgreSQL
```

Each child span explains work performed on behalf of its parent.

Hierarchy should follow execution.

Not package structure.

---

# Runtime Tracing

The Runtime SHOULD trace:

- startup
- shutdown
- scheduling
- execution
- worker allocation
- dependency resolution

Runtime traces explain:

How the platform executed work.

They do not explain business correctness.

---

# Capability Tracing

Capabilities SHOULD create spans describing:

- business operations
- external requests
- repository usage
- event publication

Capabilities should avoid tracing:

- helper methods
- internal algorithms
- implementation details

Tracing should remain architectural.

---

# Repository Tracing

Repositories SHOULD expose spans for:

- aggregate loading
- persistence
- transactions
- cache lookups

Repository spans describe:

Storage interaction.

Not SQL statements.

Storage implementation details remain hidden.

---

# Storage Tracing

Every storage engine SHOULD expose spans.

Examples include:

```text
PostgreSQL Query
```

```text
DuckDB Analysis
```

```text
Blob Download
```

Storage tracing should identify:

- latency
- retries
- failures

It should not expose business semantics.

---

# Runtime Events

Runtime Events naturally extend traces.

Example.

```text
PlaybackCompleted

↓

Runtime Event

↓

Recommendation Capability
```

The Trace should continue across the Runtime Event boundary.

Operators should perceive one logical execution.

Not multiple unrelated operations.

Trace context propagation across asynchronous messaging is one of the defining characteristics of distributed tracing systems because it preserves end-to-end visibility despite asynchronous execution.

---

# Trace Context

Every Runtime boundary SHOULD propagate:

- trace identifier
- parent span
- correlation metadata

Capabilities should not manually propagate trace context.

The Runtime owns propagation.

The SDK exposes it.

---

# Parallel Execution

Parallel work creates sibling spans.

Example.

```text
Media Imported

├── Artwork Download

├── Metadata Resolution

└── Recommendation Update
```

Each executes independently.

All belong to the same trace.

Tracing should reveal concurrency naturally.

---

# Errors

Failures SHOULD appear inside spans.

Example.

```text
Blob Download

↓

Timeout

↓

Retry Scheduled
```

The trace should explain:

- what failed
- where
- how recovery proceeded

Operators should rarely require log inspection to understand failure flow.

---

# Timing

Every span SHOULD record:

- start time
- end time
- duration

Timing should reveal:

- bottlenecks
- blocking
- latency

Tracing exists primarily to explain execution flow.

Timing makes that explanation useful.

---

# Attributes

Spans SHOULD contain structured attributes.

Examples include:

```text
capability

runtime_service

storage

operation

result
```

Attributes should remain:

- stable
- meaningful
- low cardinality

Avoid user identifiers or rapidly changing values.

---

# Events

Spans MAY include events.

Examples.

```text
Retry Scheduled
```

```text
Worker Allocated
```

```text
Blob Cached
```

Events describe significant moments during span execution.

They should not replace structured logs.

---

# Sampling

Tracing every operation indefinitely may become expensive.

The Runtime SHOULD support configurable sampling.

Possible strategies include:

- always sample startup
- always sample failures
- probabilistic sampling for successful requests

Sampling policy belongs to operations.

Not capabilities.

---

# OpenTelemetry

The Runtime SHOULD expose tracing through OpenTelemetry.

OpenTelemetry provides:

- vendor neutrality
- standard context propagation
- ecosystem compatibility

The Runtime should produce architectural traces.

OpenTelemetry simply transports them.

Detailed OpenTelemetry integration is defined later in this specification.

---

# Performance

Tracing SHOULD remain lightweight.

Avoid:

- excessive span creation
- unnecessary allocations
- deep implementation tracing

Architectural spans generally provide considerably more operational value than implementation-level spans.

---

# Privacy

Traces MUST NOT contain:

- credentials
- secrets
- authentication tokens
- personal information

Business identifiers should be minimised wherever practical.

Tracing should improve understanding.

Not expose sensitive information.

---

# Testing

Tracing SHOULD be testable.

Typical tests verify:

- span creation
- parent-child relationships
- context propagation
- timing
- attributes

Tracing should remain deterministic.

Observability should not become accidental.

---

# Anti-Patterns

The following practices are prohibited.

## Function Tracing

Creating spans for every helper function.

---

## Broken Context

Failing to propagate trace context across Runtime Events.

---

## Duplicate Spans

Multiple components tracing identical architectural work.

---

## Business Data

Recording sensitive business information inside spans.

---

## Runtime Leakage

Capabilities manually interacting with tracing implementation.

---

## Missing Ownership

Spans without clear architectural ownership.

---

# Mosaic Guidelines

Within Mosaic:

- Every logical operation SHOULD produce one trace.
- Every Runtime responsibility SHOULD produce one span.
- Trace context MUST propagate across Runtime boundaries.
- Capabilities SHOULD create architectural spans.
- Storage SHOULD expose storage spans.
- Tracing MUST remain implementation independent.
- Sensitive information MUST NOT appear inside traces.
- Traces SHOULD complement logs and metrics rather than replace them.

---

# Relationship to MEG

Metrics describe:

> **How the platform behaves over time.**

Distributed Tracing explains:

> **How one operation travelled through the platform.**

The next chapter introduces **Health**, defining how Runtime Services, capabilities and storage systems communicate operational readiness independently from logs, metrics and traces.

---

# Summary

Tracing transforms isolated Runtime activity into one coherent execution narrative.

Within Mosaic, every trace should cross:

- Runtime
- Capabilities
- Storage

without interruption.

The result is a platform where operators can answer one of the most valuable operational questions:

> **Exactly how did this happen?**

without guessing, reproducing the problem or reading implementation code.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`03-metrics.md`

**Next File**

`05-health-model.md`
