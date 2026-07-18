<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/glossary.md
Document: MEG-002
Status: Draft
-->

# Glossary

> *The runtime should speak one language. Every architectural term should have one meaning.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Event-Driven Runtime.

Runtime terminology should remain consistent across:

- Architecture Specifications
- ADRs
- Source Code
- Documentation
- Module SDKs
- Operational Guides

Where a term has a specific meaning within the Mosaic Runtime, that definition takes precedence over informal usage.

---

# A

## Acknowledgement (ACK)

Confirmation that a subscriber has successfully processed an event.

Acknowledgement informs the runtime that:

- the event does not require retry
- processing completed successfully

Acknowledgement does **not** imply that other subscribers have also completed successfully.

---

## At-Least-Once Delivery

The runtime guarantee that every published event will be delivered one or more times.

Duplicate delivery is therefore expected.

Subscribers must be idempotent.

---

# B

## Backpressure

The runtime mechanism that limits incoming work when processing capacity becomes constrained.

Backpressure protects:

- memory
- CPU
- worker pools
- external systems

It exists to preserve runtime stability.

---

## Business Event

An immutable fact describing a completed business state transition.

Examples include:

```

media.imported
```

```

PlaybackCompleted
```

Business events belong to capabilities.

Not the runtime.

---

# C

## Capability

A self-contained unit of business functionality.

Examples include:

- Library
- Metadata
- Playback
- Search

Capabilities:

- own business state
- publish events
- subscribe to events

Capabilities do not own runtime infrastructure.

---

## Causation ID

The identifier of the event that directly caused another event.

Causation expresses immediate parent-child relationships.

Unlike Correlation IDs, Causation IDs change throughout a workflow.

---

## Correlation ID

An identifier shared by all events participating in the same business workflow.

Correlation allows complete workflows to be reconstructed across many capabilities.

---

# D

## Dead Letter Queue (DLQ)

The destination for events that cannot be processed successfully after retry exhaustion.

Dead-letter events require investigation.

They should never disappear silently.

---

## Delivery

The runtime process of transporting an event from the Event Bus to a subscriber.

Delivery is owned entirely by the runtime.

---

# E

## Event

An immutable record describing a completed business fact.

Every event consists of:

- Runtime Envelope
- Business Payload

Events never describe intentions.

Only completed reality.

---

## Event Bus

The runtime component responsible for routing events between publishers and subscribers.

The Event Bus owns:

- routing
- delivery
- retries
- acknowledgements

It intentionally owns no business logic.

---

## Event Envelope

Runtime metadata surrounding every event.

Examples include:

- Event ID
- Version
- Correlation ID
- Producer

The envelope belongs to the runtime.

---

## Event Visibility

The contract classification of a Module event.

Public events are integration contracts.

Private events are implementation details.

---

## Event Payload

The immutable business information carried by an event.

Payloads describe business facts.

They never describe runtime behaviour.

---

# I

## Idempotency

The property whereby processing the same event multiple times produces the same final business state.

Idempotency is mandatory for every subscriber.

---

# O

## Occurred At

The timestamp recording when the business fact became true.

It represents business chronology.

Not delivery chronology.

---

# P

## Producer

The capability that published an event.

Every event has exactly one producer.

---

## Private Event

A Module-owned event that remains inside the Module's implementation boundary.

Other Modules should not subscribe to private events.

---

## Public Event

A Module-owned event that is part of the Module's documented integration contract.

Other Modules may subscribe to public events through manifest-declared subscriptions.

---

## Publisher

The runtime component responsible for introducing events into the Event Bus.

Publishers announce facts.

They never coordinate workflows.

---

# Q

## Queue

A bounded runtime structure holding work awaiting execution.

Every runtime queue has finite capacity.

Unlimited queues are prohibited.

---

# R

## Reactive Runtime

The runtime architecture through which autonomous capabilities cooperate by publishing and subscribing to immutable events.

The Reactive Runtime owns:

- coordination
- scheduling
- retries
- workers
- observability

Business capabilities own behaviour.

---

## Replay

The process of delivering historical events through the runtime again.

Replay enables:

- rebuilding projections
- diagnostics
- module installation
- recovery

Replay should produce identical business behaviour to live execution.

---

## Retry

A subsequent attempt to process a previously failed event.

Retries are owned by the runtime.

Business capabilities simply return failures.

---

## Runtime Event

An event describing platform behaviour rather than business behaviour.

Examples include:

```

WorkerStarted
```

```

RetryScheduled
```

```

BackpressureApplied
```

Runtime events belong to infrastructure.

---

# S

## Scheduler

The runtime component responsible for delayed and recurring execution.

Schedulers own:

- timers
- recurring jobs
- delayed retries

They never own business decisions.

---

## Subscriber

A capability that reacts to published events.

Subscribers:

- validate
- execute business behaviour
- publish further events

Subscribers remain autonomous.

---

# T

## Task

A unit of executable work performed by a worker.

Tasks originate from:

- events
- schedules
- retries
- runtime operations

Tasks are execution concepts.

Not business concepts.

---

## Trace

A complete execution path describing one workflow across the runtime.

Traces combine:

- Correlation IDs
- Causation IDs
- Timing
- Capability transitions

---

# W

## Worker

A runtime component responsible for executing tasks.

Workers own execution.

They do not own business behaviour.

---

## Worker Pool

A bounded collection of workers processing queued tasks.

Worker pools provide:

- controlled concurrency
- predictable resource usage
- operational visibility

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ACK | Acknowledgement |
| ADR | Architectural Decision Record |
| DLQ | Dead Letter Queue |
| EDA | Event-Driven Architecture |
| ID | Identifier |
| MEG | Mosaic Engineering Guidelines |
| SDK | Software Development Kit |
| SWR | Stale-While-Revalidate |

---

# Relationship to MEG-002

This glossary supports every document within the Event-Driven Runtime specification.

Definitions should remain consistent across:

- runtime implementation
- module SDKs
- architecture specifications
- operational tooling
- contributor documentation

Where runtime terminology evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.
