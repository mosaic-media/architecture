<!--
File: docs/engineering/guides/meg-008-observability/02-logging.md
Document: MEG-008
Status: Draft
Version: 0.4
-->

# Structured Logging

> *Logs should explain architectural events. They should never become a transcript of implementation.*

---

# Purpose

Logging is one of the oldest operational tools in software engineering.

Unfortunately, many systems treat logs as:

- debugging output
- print statements
- exception dumps
- developer notes

Mosaic intentionally rejects this approach.

Within the platform, logs exist to describe meaningful architectural events occurring throughout:

- Runtime
- Capabilities
- Storage
- Modules

Structured Logging provides the Runtime's chronological memory.

---

# Philosophy

Within Mosaic:

> **Logs describe significant architectural events, not every line of code executed.**

Every log entry should answer:

- What happened?
- Where did it happen?
- Why did it happen?
- What was affected?

If a log cannot answer one of those questions:

It probably should not exist.

---

# Structured Before Text

Logs MUST be structured.

Poor.

```text
Worker failed...
```

Preferred.

```json
{
  "event": "worker.failed",
  "worker": "worker-12",
  "reason": "timeout",
  "capability": "metadata"
}
```

Structure enables:

- filtering
- correlation
- indexing
- analysis

Free-form text should remain supplementary.

Not primary.

Structured logging has become the industry standard because machine-readable logs enable automated filtering, aggregation and correlation across large systems.

---

# Log Ownership

Logging follows architectural ownership.

Examples.

```mermaid
flowchart TD

N1["Scheduler"]
N2["Scheduling Logs"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Worker Manager"]
N2["Worker Logs"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Capability Registry"]
N2["Capability Logs"]

N1 --> N2
```

Every Runtime Service owns the logs describing its own behaviour.

Logging should never become centralised business knowledge.

---

# Architectural Events

Logs should describe:

- lifecycle transitions
- execution
- failures
- recovery
- storage changes
- capability activation

Examples.

```

Capability Activated
```

```

Worker Allocated
```

```

Storage Migration Completed
```

Implementation details generally belong elsewhere.

---

# Business Versus Operational Logs

Business behaviour and Runtime behaviour remain separate.

Business.

```

Playback Completed
```

Operational.

```

Playback Capability Activated
```

Business events describe the product.

Operational logs describe the platform.

The distinction should remain explicit.

---

# Log Levels

The Runtime SHOULD standardise log levels.

```text
TRACE
```

Detailed execution flow.

```text
DEBUG
```

Developer diagnostics.

```text
INFO
```

Normal Runtime behaviour.

```text
WARN
```

Unexpected but recoverable conditions.

```text
ERROR
```

Operation failed.

```text
FATAL
```

Runtime cannot continue.

Log levels should communicate operational severity.

Not developer emotion.

---

# Context

Every log SHOULD contain contextual information.

Examples include:

- capability
- Runtime Service
- worker
- trace identifier
- operation
- storage system

Context should eliminate ambiguity.

Logs without context quickly become operational noise.

---

# Correlation

Logs SHOULD include correlation identifiers.

Example.

```text
trace_id

request_id

capability_id
```

Operators should be able to reconstruct one logical operation across:

- Runtime
- Capabilities
- Storage

Correlation is one of the primary reasons structured logging exists.

---

# Runtime Logging

The Runtime SHOULD log:

- startup
- shutdown
- lifecycle
- worker allocation
- scheduling
- dependency resolution
- activation

Runtime logs explain platform behaviour.

They should not explain business behaviour.

---

# Capability Logging

Capabilities SHOULD log:

- lifecycle
- external communication
- meaningful business transitions
- recoverable failures

Capabilities SHOULD avoid:

- verbose implementation details
- internal algorithm tracing

Business behaviour should remain understandable.

Not overwhelming.

---

# Storage Logging

Storage systems SHOULD log:

- migrations
- backup
- restore
- corruption detection
- rebuilds
- cache invalidation

Storage logs should describe information lifecycle.

Not SQL execution.

---

# Event Logging

Every significant Runtime Event MAY produce one structured log.

Example.

```mermaid
flowchart TD

N1["CapabilityActivated"]
N2["Structured Log"]

N1 --> N2
```

The Runtime should avoid producing multiple unrelated logs for one architectural event.

One event.

One authoritative log.

---

# Error Logging

Errors SHOULD describe:

- operation
- component
- consequence
- recovery

Poor.

```text
Database failed.
```

Preferred.

```mermaid
flowchart TD

N1["Repository.Save"]
N2["PostgreSQL Timeout"]
N3["Retry Scheduled"]

N1 --> N2
N2 --> N3
```

Good logs explain failure.

Not merely report it.

---

# Recovery Logging

Recovery deserves explicit visibility.

Examples include:

- retry
- failover
- rebuild
- migration rollback

Operators should understand:

> **How did the platform recover?**

Recovery is often more operationally important than failure itself.

---

# Security

Logs MUST NOT expose:

- passwords
- tokens
- secrets
- personal information
- encryption keys

Sensitive information belongs in secure storage.

Never in operational telemetry.

---

# Performance

Logging should remain efficient.

Avoid:

- excessive allocation
- unnecessary formatting
- blocking I/O

Structured log construction should impose minimal Runtime overhead.

Observability should not become a performance bottleneck.

---

# Retention

Log retention SHOULD remain configurable.

Typical policies include:

- development
- production
- audit

Retention belongs to operations.

Not capabilities.

---

# Observability Integration

Logs complement:

- metrics
- traces
- diagnostics

Logs should never attempt to replace them.

Different operational questions require different telemetry.

---

# Testing

Structured logging SHOULD be testable.

Tests should verify:

- event emitted
- required fields present
- sensitive data omitted
- context included

Logging should remain predictable.

Not incidental.

---

# Anti-Patterns

The following practices are prohibited.

## Print Statements

Using:

```go
fmt.Println(...)
```

for Runtime logging.

---

## Unstructured Logs

Free-form text without machine-readable fields.

---

## Duplicate Logs

Multiple Runtime components logging the same event independently.

---

## Sensitive Information

Logging credentials or secrets.

---

## Business Spam

Logging every business operation indiscriminately.

---

## Stack Traces Everywhere

Treating every recoverable error as a fatal diagnostic event.

---

# Mosaic Guidelines

Within Mosaic:

- Logs MUST remain structured.
- Logging MUST follow architectural ownership.
- Context MUST accompany every significant event.
- Correlation identifiers SHOULD be propagated.
- Business and operational logs MUST remain distinct.
- Sensitive information MUST NOT be logged.
- Runtime logs SHOULD describe architecture.
- Capabilities SHOULD log meaningful business events.
- Logs SHOULD complement metrics and traces rather than replace them.

---

# Relationship to MEG

Observability Philosophy established:

> **Why the platform should be observable.**

Structured Logging now defines:

> **How the platform records meaningful operational events.**

The next chapter introduces **Metrics**, describing how Mosaic measures behaviour over time rather than individual occurrences.

---

# Summary

Logs are the Runtime's memory.

Not every thought.

Only the important ones.

Within Mosaic, every significant architectural event should produce one clear, structured and contextual record that explains:

- what happened
- where
- why

without requiring an operator to inspect the implementation.

Good logs make the architecture readable while the platform is running.
