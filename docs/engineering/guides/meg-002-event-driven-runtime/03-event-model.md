<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/03-event-model.md
Document: MEG-002
Status: Draft
Version: 0.1
-->

# Event Model

> *Events are immutable records of facts that have already occurred. They describe reality. They do not request it.*

---

# Purpose

A consistent event model is fundamental to an event-driven platform.

If every capability invents its own event structure, naming conventions and lifecycle semantics, the runtime quickly becomes fragmented.

This document defines the canonical event model for the Mosaic Runtime.

Every event published within the platform MUST conform to these principles.

---

# Philosophy

Within Mosaic:

> **An event is an immutable fact describing a completed state transition.**

Events are historical records.

Once published they cannot be modified.

If reality changes, a **new event** is published.

History is additive.

Never rewritten.

---

# What Is An Event?

An event answers one question.

> **What happened?**

Examples include:

```
MediaImported
```

```
PlaybackStarted
```

```
MetadataUpdated
```

```
ExtensionInstalled
```

Each describes something that has already occurred.

Nothing more.

---

# Event Lifecycle

Every event progresses through the same lifecycle.

```
State Changes

↓

Event Created

↓

Published

↓

Delivered

↓

Processed

↓

Archived
```

Once published, an event becomes immutable.

Subscribers must treat every event as read-only.

---

# Events Follow State

Events MUST be published **after** business state changes.

Correct:

```
Persist Media

↓

Commit Transaction

↓

Publish MediaImported
```

Incorrect:

```
Publish MediaImported

↓

Persist Media
```

If persistence fails, no event should exist describing work that never actually happened.

Events describe reality.

Not intention.

---

# Events Are Immutable

Once an event has been published:

- payloads MUST NOT change
- timestamps MUST NOT change
- identifiers MUST NOT change
- metadata MUST NOT change

Corrections require a new event.

Example.

```
MetadataImported

↓

MetadataCorrected
```

Not:

```
Modify Existing Event
```

Immutability is one of the defining characteristics of event-driven systems because it preserves an accurate historical record and simplifies replay, auditing and debugging. ([martinfowler.com](https://martinfowler.com/eaaDev/EventNarrative.html))

---

# Event Structure

Every runtime event consists of two parts.

```
Envelope

↓

Payload
```

The envelope describes runtime behaviour.

The payload describes business behaviour.

This separation keeps runtime infrastructure independent from domain semantics.

---

# Event Envelope

Every event SHOULD contain standard runtime metadata.

```
Event ID

Event Name

Event Version

Occurred At

Correlation ID

Causation ID

Producer

Payload
```

These fields allow the runtime to:

- route events
- trace workflows
- correlate requests
- support replay
- diagnose failures

Future chapters define each field in detail.

---

# Event Payload

The payload contains business information only.

Example:

```
MediaImported

↓

Media ID

Library ID

Source

Imported At
```

The payload SHOULD NOT contain:

- retry counts
- worker IDs
- routing information
- subscriber metadata

Those belong to the runtime.

---

# Event Ownership

Every event has exactly one publisher.

Example.

```
Library

↓

MediaImported
```

Library owns the event because Library owns the state transition.

Other capabilities consume the event.

They do not redefine it.

Ownership should always be unambiguous.

---

# Event Identity

Every event MUST have a globally unique identifier.

This identifier represents:

> **This specific occurrence of a fact.**

Two identical payloads published at different times represent two different events.

Identity belongs to the occurrence.

Not the payload.

---

# Event Time

Every event records when the business fact occurred.

Not:

- when processing completed
- when subscribers received it
- when retries succeeded

The timestamp represents reality.

Not delivery.

This distinction becomes important during replay and diagnostics.

---

# Event Ordering

Events SHOULD be considered independent unless an explicit ordering guarantee exists.

Subscribers MUST NOT assume:

```
Event A

↓

Event B
```

will always be received in that order.

Ordering guarantees are discussed in a later chapter.

Subscribers should instead be resilient to delayed or repeated delivery.

---

# Event Granularity

Events should describe meaningful business transitions.

Good:

```
PlaybackCompleted
```

Poor:

```
SetBooleanFlag
```

Events should communicate concepts recognised by the business domain.

Not implementation details.

---

# Event Completeness

An event SHOULD contain sufficient information for subscribers to perform their work.

Subscribers SHOULD NOT immediately perform another query simply to understand the event.

Poor:

```
MediaImported

↓

Media ID Only

↓

Every Subscriber Queries Database
```

Better:

```
MediaImported

↓

Media ID

Library ID

Media Type

Source
```

Include enough context to minimise unnecessary coupling.

Avoid including entire domain models.

---

# Event Independence

Events should remain independent.

Example.

```
MediaImported
```

should not contain:

```
Next Event

Subscriber List

Processing Instructions
```

The publisher describes the fact.

The runtime decides delivery.

Subscribers decide behaviour.

Each concern remains separate.

---

# Event Size

Event payloads SHOULD remain compact.

Events are notifications.

Not object graphs.

Include:

- identifiers
- essential business context
- immutable business facts

Avoid:

- large binary data
- complete database records
- transient runtime state

Large artefacts should be referenced rather than embedded.

---

# Event Evolution

Events evolve through versioning.

Existing events MUST remain valid.

Breaking changes require:

- new event versions
- compatibility strategy
- migration plan

Events should remain stable over time.

Future chapters define versioning standards.

---

# Event Replay

The runtime SHOULD support replay where practical.

Replay enables:

- rebuilding projections
- recovering state
- diagnostics
- testing
- extension installation

Replay is only possible because events are immutable.

Subscribers should therefore remain deterministic.

---

# Event Processing

Every subscriber should process events according to the same model.

```
Receive

↓

Validate

↓

Execute

↓

Publish New Events
```

Subscribers should avoid:

- modifying received events
- mutating runtime metadata
- depending upon subscriber order

Each subscriber behaves independently.

---

# Event Chains

Events naturally create event chains.

Example.

```
MediaImported

↓

MetadataFetched

↓

ArtworkDownloaded

↓

LibraryIndexed

↓

RecommendationsUpdated
```

Each event represents a completed business transition.

No event predicts the future.

---

# Mosaic Guidelines

Within Mosaic:

- Events MUST describe completed facts.
- Events MUST be immutable.
- Events MUST be published after state changes.
- Every event MUST have a unique identifier.
- Event payloads SHOULD contain business information only.
- Runtime metadata MUST remain outside business payloads.
- Subscribers MUST treat events as read-only.
- New events MUST be published for new facts.

---

# Summary

The Mosaic Event Model deliberately separates:

- business facts
- runtime metadata
- delivery
- processing

This separation keeps events stable, replayable and understandable.

Every future runtime feature, including retries, observability, versioning and extension interoperability, depends upon a consistent event model.

The event model is therefore one of the foundational architectural contracts of the Mosaic Runtime.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`02-why-events.md`

**Next File**

`04-event-naming.md`
