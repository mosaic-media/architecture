<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/15-backpressure.md
Document: MEG-002
Status: Draft
-->

# Backpressure

> *A healthy runtime knows when to slow down. An unhealthy runtime tries to do everything at once.*

---

# Purpose

The Mosaic Runtime is designed to operate continuously under varying workloads.

During normal operation, events flow smoothly through the platform.

However, temporary spikes are inevitable.

Examples include:

- importing a large media library
- installing a new module
- rebuilding metadata
- replaying historical events
- recovering after downtime

Without backpressure, these bursts can overwhelm:

- workers
- databases
- storage
- external APIs
- memory
- CPU

This document defines how the Mosaic Runtime controls workload to maintain predictable behaviour under load.

---

# Philosophy

Within Mosaic:

> **The runtime should slow work down before it breaks.**

Throughput is desirable.

Stability is mandatory.

When resources become constrained, the runtime should reduce intake rather than consume unlimited memory or spawn unlimited work.

---

# What Is Backpressure?

Backpressure is the mechanism through which the runtime communicates:

> **"I cannot safely accept more work right now."**

Rather than continuing to accept events indefinitely, the runtime intentionally limits throughput to protect overall system health.

Backpressure is a fundamental concept in reactive systems because it allows producers and consumers to operate at sustainable rates instead of overwhelming one another. ([reactivemanifesto.org](https://www.reactivemanifesto.org/))

---

# Why Backpressure Matters

Consider:

```mermaid
flowchart TD

N1["Library Scan"]
N2["50,000 media.imported Events"]
N3["Metadata"]
N4["Artwork"]
N5["Search"]
N6["Recommendations"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

If every event immediately creates work:

- memory usage grows
- queues expand indefinitely
- workers become saturated
- external providers become rate limited

Eventually:

The runtime becomes unstable.

Backpressure prevents this.

---

# Runtime Model

The runtime continuously balances:

```mermaid
flowchart TD

N1["Incoming Work"]
N2["Queues"]
N3["Workers"]
N4["Completed Work"]

N1 --> N2
N2 --> N3
N3 --> N4
```

If workers cannot keep pace:

Queues grow.

Eventually the runtime begins applying backpressure.

---

# Backpressure Principles

The runtime should always prefer:

```mermaid
flowchart TD

N1["Slow Processing"]
N2["Stable Runtime"]

N1 --> N2
```

Rather than:

```mermaid
flowchart TD

N1["Unlimited Throughput"]
N2["Resource Exhaustion"]

N1 --> N2
```

Graceful degradation is always preferable to catastrophic failure.

---

# Bounded Queues

Every runtime queue MUST have a maximum capacity.

```mermaid
flowchart TD

N1["Queue"]
N2["Maximum Size"]
N3["Backpressure"]

N1 --> N2
N2 --> N3
```

Unbounded queues are prohibited.

Unlimited buffering simply converts CPU pressure into memory pressure.

Eventually the runtime still fails.

---

# Queue Ownership

Each capability owns its own work queue.

Example.

```

Metadata Queue

Artwork Queue

Search Queue

Recommendation Queue
```

Independent queues prevent slow capabilities from blocking unrelated work.

Failure isolation remains intact.

---

# Worker Saturation

Suppose:

```mermaid
flowchart TD

N1["Metadata"]
N2["All Workers Busy"]

N1 --> N2
```

New work should queue.

If the queue becomes full:

Backpressure should be applied.

Workers should never grow without limit.

---

# Resource Protection

Backpressure protects:

- CPU
- memory
- database pools
- blob storage
- network connections
- external APIs

Protecting infrastructure is one of the runtime's primary responsibilities.

Business capabilities should remain unaware.

---

# Producer Behaviour

Publishers should never attempt to bypass runtime backpressure.

Poor.

```mermaid
flowchart TD

N1["Queue Full"]
N2["Retry Immediately"]
N3["Queue Full"]
N4["Retry Again"]

N1 --> N2
N2 --> N3
N3 --> N4
```

This amplifies overload.

Instead:

```mermaid
flowchart TD

N1["Runtime"]
N2["Signals Backpressure"]
N3["Retry Scheduled"]

N1 --> N2
N2 --> N3
```

The runtime controls recovery.

---

# Queue Growth

Queue depth should remain observable.

Typical lifecycle.

```mermaid
flowchart TD

N1["Empty"]
N2["Growing"]
N3["Healthy"]
N4["Near Capacity"]
N5["Backpressure"]
N6["Recovery"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The runtime should begin protecting itself before queues become completely full.

---

# Priority

Not all work is equally important.

Examples.

High Priority.

- Playback
- Authentication
- User interaction

Lower Priority.

- Metadata refresh
- Recommendation generation
- Analytics

The scheduler MAY prioritise critical work during sustained load.

Business correctness should always take precedence over convenience.

---

# Load Shedding

Some work may be safely discarded.

Examples include:

- duplicate refresh requests
- repeated health checks
- obsolete cache refreshes

Other work must never be discarded.

Examples include:

- playback progress
- authentication events
- library imports

The runtime should understand this distinction.

---

# Coalescing

Repeated equivalent work SHOULD be combined where practical.

Example.

Poor.

```mermaid
flowchart TD

N1["LibraryUpdated"]
N2["Refresh Cache"]
N3["LibraryUpdated"]
N4["Refresh Cache"]
N5["LibraryUpdated"]
N6["Refresh Cache"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Better.

```mermaid
flowchart TD

N1["LibraryUpdated"]
N2["Queue Refresh"]
N3["Additional Requests"]
N4["Single Refresh"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The runtime should avoid redundant work whenever correctness permits.

---

# Rate Limiting

External systems frequently impose rate limits.

Examples include:

- TMDB
- AniList
- Docker APIs
- Remote storage

Backpressure should naturally integrate with rate limiting.

Rather than failing continuously, the runtime should reduce throughput to sustainable levels.

---

# Module Isolation

Modules should never be capable of overwhelming the runtime.

Suppose:

```mermaid
flowchart TD

N1["Third-Party Module"]
N2["Produces Millions Of Events"]

N1 --> N2
```

The runtime should:

- isolate the module
- apply backpressure
- preserve platform functionality

Platform stability always takes precedence over module throughput.

---

# Recovery

Backpressure should be temporary.

```mermaid
flowchart TD

N1["Load Spike"]
N2["Backpressure"]
N3["Queues Drain"]
N4["Normal Operation"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Recovery should occur automatically.

Manual intervention should rarely be required.

---

# Metrics

The runtime SHOULD expose:

- queue depth
- worker utilisation
- rejected work
- deferred work
- queue wait time
- average processing latency

These metrics provide early warning of runtime stress.

Operators should identify overload before users experience degraded behaviour.

---

# Adaptive Scaling

Where supported, the runtime MAY increase worker capacity during sustained load.

However:

Scaling should remain bounded.

Unlimited worker creation simply moves the bottleneck elsewhere.

Scaling should complement backpressure.

Not replace it.

---

# Circuit Breakers

Backpressure integrates naturally with circuit breakers.

Suppose:

```

TMDB Offline
```

Instead of:

```

Retry

Retry

Retry

Retry
```

The runtime should:

```mermaid
flowchart TD

N1["Open Circuit"]
N2["Reduce Requests"]
N3["Recover Gradually"]

N1 --> N2
N2 --> N3
```

This protects both the runtime and external dependencies.

---

# Replay

Replay should respect normal backpressure.

Historical replay should never bypass:

- queues
- workers
- rate limits
- resource limits

Replay should appear identical to live processing from the runtime's perspective.

---

# Anti-Patterns

The following practices are prohibited.

## Unlimited Queues

```

Append Forever
```

---

## Unlimited Workers

```mermaid
flowchart TD

N1["Queue Full"]
N2["Create Worker"]
N3["Repeat Forever"]

N1 --> N2
N2 --> N3
```

---

## Busy Waiting

Workers repeatedly polling empty queues.

---

## Ignoring Resource Limits

Continuing to accept work after resource exhaustion.

---

## Module Starvation

Allowing one module to consume all runtime capacity.

---

## Immediate Retry During Overload

Retries should reduce pressure.

Not increase it.

---

# Mosaic Guidelines

Within Mosaic:

- Every queue MUST be bounded.
- Every worker pool MUST be bounded.
- The runtime MUST apply backpressure before resource exhaustion.
- Queue depth MUST remain observable.
- Modules MUST be isolated from one another.
- Recovery SHOULD occur automatically.
- Replay MUST respect runtime limits.
- High-priority work SHOULD remain responsive during overload.
- Stability MUST always take precedence over throughput.

---

# Relationship to the Runtime

Backpressure is the mechanism that keeps the Mosaic Runtime stable under unpredictable workloads.

Combined with:

- worker pools
- scheduling
- retries
- idempotency
- event isolation

it allows the platform to remain responsive even during significant operational stress.

Rather than treating overload as an exceptional condition, the runtime treats it as an expected characteristic of a long-running system.

This philosophy produces a platform that fails gracefully rather than catastrophically.

---

# Summary

The purpose of backpressure is not to process more work.

It is to process work sustainably.

Within Mosaic, backpressure ensures:

- predictable resource usage
- resilient modules
- protected infrastructure
- graceful degradation
- operational stability

The runtime should always prefer temporary slowdown over permanent failure.

That single principle keeps the platform healthy as it grows from a handful of capabilities to hundreds of independently developed modules.
