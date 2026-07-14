<!--
File: engineering/meg/MEG-008 Observability/10-debugging.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Debugging

> *Debugging should explain behaviour without changing it.*

---

# Purpose

Observability provides insight into the platform while it is operating.

Sometimes that insight is insufficient.

Operators and developers require controlled mechanisms for investigating:

- unexpected Runtime behaviour
- capability failures
- storage inconsistencies
- performance regressions
- dependency issues

This document defines the debugging architecture of the Mosaic platform.

Debugging should be:

- deterministic
- safe
- observable
- non-invasive

The platform should never require production code changes simply to understand production behaviour.

---

# Philosophy

Within Mosaic:

> **Debugging is an extension of observability, not a replacement for it.**

Good observability should answer most operational questions.

Debugging exists only for the remaining edge cases.

If debugging becomes routine:

The observability architecture should probably improve.

---

# Debugging Hierarchy

Debugging follows the Runtime Architecture.

```text
Platform

↓

Runtime

↓

Capabilities

↓

Storage

↓

Infrastructure
```

Every layer should expose safe debugging facilities.

No layer should require private implementation knowledge.

---

# Debugging Objectives

Debugging should allow operators to answer:

- Why did this capability fail?
- Why is this Runtime Service blocked?
- Why is this dependency unresolved?
- Why is startup slower today?
- Why was this event delayed?

without:

- modifying production code
- restarting the Runtime
- attaching unsafe debuggers

---

# Observability First

The preferred investigation order is:

```text
Health

↓

Metrics

↓

Logs

↓

Traces

↓

Diagnostics

↓

Debugging
```

Debugging should be the final operational tool.

Not the first.

---

# Runtime Debugging

The Runtime SHOULD expose:

- active workers
- execution queues
- dependency graph
- scheduler state
- active traces
- resource allocation

Operators should inspect Runtime behaviour without modifying it.

The Runtime should remain introspectable.

---

# Capability Debugging

Capabilities SHOULD expose:

- lifecycle state
- active operations
- configuration
- dependency status
- recent failures

Capabilities should not expose:

- private implementation
- internal algorithms
- sensitive business information

Debugging should reinforce architectural boundaries.

Not bypass them.

---

# Storage Debugging

Storage debugging SHOULD expose:

- active migrations
- repository activity
- cache rebuilds
- storage latency
- blob integrity
- archive validation

Storage debugging explains:

How information moves.

Not database internals.

---

# Read-Only Principle

Debugging interfaces SHOULD remain read-only.

Preferred.

```text
Inspect Worker Pool
```

Avoid.

```text
Modify Worker Pool
```

Diagnostics should explain Runtime behaviour.

They should not become operational control surfaces.

Administrative operations belong elsewhere.

---

# Runtime Snapshots

The Runtime SHOULD support snapshot debugging.

Example.

```text
Snapshot

↓

Workers

↓

Capabilities

↓

Storage

↓

Resources

↓

Configuration
```

Snapshots capture one architectural moment.

They should never pause Runtime execution.

---

# Trace Replay

Where practical, the Runtime MAY support trace replay.

Replay should reconstruct:

- execution path
- spans
- Runtime Events
- timing

Replay should never re-execute business behaviour.

Its purpose is explanation.

Not simulation.

---

# Failure Investigation

Failures should expose sufficient debugging context.

Examples include:

- trace identifier
- capability
- Runtime Service
- dependency chain
- storage operations

Operators should understand:

> **Why did this fail?**

rather than simply:

> **It failed.**

---

# Dependency Inspection

The Runtime SHOULD expose dependency debugging.

Example.

```text
Recommendations

↓

Waiting

↓

Metadata

↓

Unavailable
```

Dependency debugging should explain:

Why capabilities remain:

- inactive
- degraded
- unavailable

The dependency graph already contains this information.

Debugging simply exposes it.

---

# Worker Inspection

Worker debugging SHOULD expose:

- current Work Unit
- execution duration
- lifecycle
- cancellation state
- queue ownership

Worker inspection should never require attaching debuggers to goroutines.

---

# Scheduler Inspection

The Scheduler SHOULD expose:

- waiting schedules
- overdue schedules
- execution windows
- recurring schedules

Operators should understand scheduling behaviour independently from execution.

---

# Event Inspection

Runtime Event debugging SHOULD expose:

- publishers
- subscribers
- retries
- dead letters
- delivery latency

The Runtime already coordinates event delivery.

Debugging should reveal:

How events moved through the platform.

---

# Configuration Debugging

Debugging SHOULD expose:

- active configuration
- configuration source
- schema version
- validation status

Sensitive values MUST remain redacted.

Configuration debugging explains:

Why the Runtime behaves this way.

Not:

What secrets it contains.

---

# Safe Production Debugging

Production debugging SHOULD avoid:

- process suspension
- memory modification
- live code injection

Safe debugging preserves:

- Runtime stability
- business correctness
- platform integrity

Observability should remain the primary investigative mechanism.

---

# Debug Logging

Temporary debug logging SHOULD be unnecessary.

Instead:

Operators should enable:

- existing structured logs
- additional tracing
- increased telemetry detail

The platform should already contain the required instrumentation.

---

# Remote Debugging

Remote debugging SHOULD remain controlled.

Access should require:

- authentication
- authorisation
- auditing

Remote debugging capabilities belong to platform administration.

Not general Runtime execution.

Security requirements are defined in MEG-009.

---

# Support Bundles

The Runtime SHOULD support support bundle generation.

Example.

```text
Support Bundle

├── Runtime Snapshot

├── Health

├── Metrics

├── Logs

├── Traces

├── Configuration (Redacted)

└── Diagnostics
```

Support bundles should allow complex issues to be analysed without reproducing them.

---

# Explainability

Every debugging interface should answer:

> **Why?**

Examples.

Why is startup slow?

↓

Dependency graph.

Why is storage degraded?

↓

Storage diagnostics.

Why is playback delayed?

↓

Trace.

Debugging should explain architecture.

Not expose implementation.

---

# Performance

Debugging SHOULD remain lightweight until explicitly enabled.

The Runtime should avoid:

- expensive inspection
- deep memory analysis
- continuous diagnostic overhead

Observability remains always-on.

Advanced debugging should generally remain on-demand.

---

# Testing

Debugging interfaces SHOULD be tested.

Typical tests verify:

- Runtime snapshots
- dependency inspection
- worker inspection
- support bundle generation
- configuration redaction

Debugging should remain deterministic.

Operators should trust its output.

---

# Anti-Patterns

The following practices are prohibited.

## Production Print Statements

Adding temporary logging to production code.

---

## Runtime Modification

Changing Runtime behaviour during debugging.

---

## Hidden Debug APIs

Undocumented Runtime inspection interfaces.

---

## Sensitive Data

Exposing credentials through debugging tools.

---

## Implementation Debugging

Debugging individual helper functions rather than architectural responsibilities.

---

## Manual Investigation

Operators manually correlating Runtime state already known by the platform.

---

# Mosaic Guidelines

Within Mosaic:

- Debugging MUST remain read-only.
- Observability SHOULD answer most operational questions.
- Runtime snapshots SHOULD remain inexpensive.
- Dependency debugging SHOULD expose architectural relationships.
- Sensitive information MUST remain redacted.
- Production debugging MUST preserve Runtime stability.
- Support bundles SHOULD remain deterministic.
- Debugging SHOULD explain architecture rather than implementation.

---

# Relationship to MEG

Alerting answers:

> **When should humans investigate?**

Debugging answers:

> **How should humans investigate safely and effectively?**

The next chapter introduces **OpenTelemetry**, defining how Mosaic exports its logs, metrics and traces through open standards while preserving the architectural ownership established throughout this specification.

---

# Summary

Debugging should not require changing the platform.

Within Mosaic, the Runtime should already know:

- what exists
- what is executing
- what failed
- why it failed

Debugging simply exposes that knowledge in a safe, deterministic and architecturally meaningful way.

The best debugging session is the one where the platform already contains the answer before anyone opens an IDE.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`09-alerting.md`

**Next File**

`11-opentelemetry.md`
