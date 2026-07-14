<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/11-runtime-boundary.md
Document: MEG-004
Status: Draft
Version: 0.4
-->

# Runtime Boundary

> *The Runtime executes the business. It is not the business.*

---

# Purpose

The Reactive Runtime introduced in [MEG-002](../meg-002-event-driven-runtime/index.md) is one of the most sophisticated parts of the Mosaic platform.

It manages:

- event delivery
- scheduling
- retries
- workers
- observability
- lifecycle

Despite this sophistication, the Runtime remains infrastructure.

The Domain must never become aware that it exists.

This document defines the architectural boundary separating the Domain Model from the Reactive Runtime.

---

# Philosophy

Within Mosaic:

> **The Runtime serves the Domain. The Domain never serves the Runtime.**

The Runtime exists because the Domain requires a mechanism for coordinating work.

The Domain does **not** exist because the Runtime provides one.

This distinction is one of the most important architectural boundaries in the entire platform.

---

# Two Independent Models

Mosaic intentionally maintains two independent models.

```mermaid
flowchart TD

N1["Business Model"]
N2["Domain"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Execution Model"]
N2["Reactive Runtime"]

N1 --> N2
```

The Business Model describes:

- media
- playback
- metadata
- libraries
- collections

The Execution Model describes:

- workers
- queues
- retries
- scheduling
- event delivery

Neither model should leak into the other.

---

# The Runtime Is Infrastructure

Within Hexagonal Architecture, the Runtime is simply another external system.

Conceptually.

```mermaid
flowchart TD

N1["HTTP"]
N2["Runtime"]
N3["Database"]
N4["Blob Storage"]
N5["External APIs"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

All exist outside the Domain.

All communicate through Ports and Adapters.

The Runtime receives no special architectural status simply because it is part of Mosaic.

---

# Business Behaviour

Business behaviour belongs exclusively to the Domain.

Examples include:

```

Playback Completed
```

```

Collection Created
```

```

Metadata Corrected
```

The Runtime neither understands nor evaluates these concepts.

It simply transports and coordinates the resulting events.

---

# Runtime Behaviour

The Runtime owns operational concerns.

Examples include:

```

Retry Scheduled
```

```

Worker Started
```

```

Backpressure Applied
```

```

Queue Drained
```

These are runtime concepts.

They are not business concepts.

The Domain should never reference them.

---

# Domain Events

The Domain raises Domain Events.

```mermaid
flowchart TD

N1["PlaybackSession"]
N2["Complete()"]
N3["PlaybackCompleted"]

N1 --> N2
N2 --> N3
```

At this point:

The Domain has finished its work.

It does not:

- publish messages
- schedule retries
- notify subscribers

Those responsibilities begin only after the Domain boundary.

---

# Runtime Translation

A Runtime Adapter bridges the two models.

```mermaid
flowchart TD

N1["Aggregate"]
N2["Domain Event"]
N3["Runtime Adapter"]
N4["Runtime Event"]
N5["Event Bus"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Notice:

The Domain never imports:

- Event Bus
- Publisher
- Runtime

The Adapter performs the translation.

This keeps the Domain pure while allowing the Runtime to evolve independently.

---

# Subscribers

Runtime Subscribers are Driving Adapters.

Example.

```mermaid
flowchart TD

N1["Runtime Event"]
N2["Subscriber Adapter"]
N3["Driving Port"]
N4["Application Service"]
N5["Domain"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Domain remains unaware that:

- queues
- workers
- event buses

exist.

It simply receives another business request.

---

# Scheduling

Scheduling belongs entirely to the Runtime.

Poor.

```go
time.Sleep(...)
```

inside an Aggregate.

Preferred.

```mermaid
flowchart TD

N1["Domain"]
N2["Request Behaviour"]
N3["Runtime Scheduler"]
N4["Driving Adapter"]
N5["Domain"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Runtime owns time.

The Domain owns behaviour.

---

# Retries

Retries are Runtime concerns.

Suppose metadata retrieval fails.

```mermaid
flowchart TD

N1["Metadata Provider"]
N2["Failure"]
N3["Runtime Retry"]
N4["Later"]
N5["Driving Adapter"]
N6["Domain"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Domain simply executes business behaviour again.

It remains unaware that this execution resulted from a retry.

This separation keeps business behaviour deterministic while allowing the Runtime to implement sophisticated recovery strategies.  [AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

---

# Workers

Workers execute Application Services.

They do not execute Aggregates directly.

Conceptually.

```mermaid
flowchart TD

N1["Worker"]
N2["Driving Adapter"]
N3["Application Service"]
N4["Aggregate"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The Worker knows:

- scheduling
- cancellation
- retries

The Aggregate knows:

- business rules

Responsibilities remain completely separate.

---

# Cancellation

Runtime cancellation should never leak into business behaviour.

The Runtime decides:

```

Stop Processing
```

The Domain decides:

```

How To Leave Business State Consistent
```

Cancellation is operational.

Consistency is business.

---

# Observability

The Runtime owns:

- traces
- metrics
- queue depth
- worker utilisation
- retry counts

The Domain owns:

- business events
- business identities
- business outcomes

Operational telemetry should never pollute the Domain Model.

---

# Module Integration

Modules participate through the Runtime boundary.

Example.

```mermaid
flowchart TD

N1["Module"]
N2["Runtime Event"]
N3["Driving Adapter"]
N4["Driving Port"]
N5["Application"]
N6["Domain"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Domain cannot determine whether the caller is:

- Platform capabilities
- Module
- Scheduler
- HTTP

Every caller appears identical.

This greatly simplifies business modelling.

---

# Runtime Replacement

Imagine replacing the current Runtime.

```mermaid
flowchart TD

N1["Event Bus A"]
N2["Event Bus B"]

N1 --> N2
```

or

```mermaid
flowchart TD

N1["Worker Engine A"]
N2["Worker Engine B"]

N1 --> N2
```

The Domain should remain unchanged.

Only:

- Runtime Adapters
- Composition Root

require modification.

This is a direct consequence of respecting the Runtime boundary.

---

# Runtime Is Not An Application Service

A common mistake is allowing the Runtime to orchestrate business workflows.

Poor.

```mermaid
flowchart TD

N1["Runtime"]
N2["If PlaybackCompleted"]
N3["Generate Recommendations"]
N4["Update Statistics"]
N5["Refresh Metadata"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Runtime has now become part of the business.

Instead.

```mermaid
flowchart TD

N1["PlaybackCompleted"]
N2["Runtime Delivers"]
N3["Independent Subscribers"]

N1 --> N2
N2 --> N3
```

Business behaviour remains inside the Domain.

The Runtime merely coordinates execution.

---

# Runtime APIs

The Domain should never import runtime APIs.

Poor.

```go
runtime.Publish(...)
```

```go
runtime.Schedule(...)
```

Preferred.

```mermaid
flowchart TD

N1["Domain Event"]
N2["Runtime Adapter"]
N3["Runtime"]

N1 --> N2
N2 --> N3
```

The Runtime remains replaceable because the Domain does not depend upon its APIs.

---

# Testing

The Runtime boundary makes testing significantly easier.

Domain tests.

```mermaid
flowchart TD

N1["Application Service"]
N2["Aggregate"]
N3["Assertions"]

N1 --> N2
N2 --> N3
```

Runtime tests.

```mermaid
flowchart TD

N1["Worker"]
N2["Runtime Adapter"]
N3["Queues"]
N4["Retries"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Each model can be verified independently.

This separation dramatically reduces testing complexity.

---

# Anti-Patterns

The following practices are prohibited.

## Runtime Imports

Aggregates importing runtime packages.

---

## Event Bus Inside Domain

Publishing runtime events directly from business objects.

---

## Scheduling Inside Aggregates

Business objects managing timers.

---

## Worker-Aware Business Logic

Business behaviour depending upon worker identity or execution environment.

---

## Retry-Aware Aggregates

Aggregates changing behaviour because an operation is a retry.

Business correctness should remain independent of execution history.

---

## Runtime Orchestration

Runtime components deciding business workflows.

---

# Mosaic Guidelines

Within Mosaic:

- The Runtime MUST remain infrastructure.
- The Domain MUST remain unaware of the Runtime.
- Domain Events MUST cross the Runtime boundary through Adapters.
- Runtime Subscribers MUST invoke Driving Ports.
- Scheduling MUST remain outside the Domain.
- Retries MUST remain outside the Domain.
- Workers MUST execute Application Services rather than business rules.
- Operational telemetry MUST remain outside the Domain.
- Runtime behaviour MUST remain replaceable without modifying business logic.

---

# Relationship to MEG

This chapter completes the integration between:

- **[MEG-002](../meg-002-event-driven-runtime/index.md) — Reactive Runtime**
- **[MEG-003 — Domain-Driven Design](../meg-003-domain-driven-design/index.md)**
- **MEG-004 — Hexagonal Architecture**

Together they establish one of the most important architectural principles within Mosaic:

```mermaid
flowchart TD

N1["Domain"]
N2["Ports"]
N3["Adapters"]
N4["Reactive Runtime"]
N5["Infrastructure"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Each layer owns one responsibility.

None understand the implementation details of the next.

---

# Summary

The Runtime is an extraordinarily capable piece of infrastructure.

It schedules.

Retries.

Observes.

Coordinates.

Delivers.

The Domain does none of those things.

It simply models the business.

Maintaining this boundary ensures that the most valuable part of the platform, the business itself, remains protected from the inevitable evolution of the technologies that execute it.
