<!--
File: engineering/meg/MEG-003 Domain-Driven Design/11-domain-events.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Domain Events

> *A Domain Event records that something important happened within the business. It is created by the domain before it becomes a runtime event.*

---

# Purpose

Business behaviour changes business state.

Whenever an important business state transition occurs, the domain should record that fact.

These facts are known as **Domain Events**.

Domain Events represent significant moments within the business itself.

They exist independently of:

- event buses
- messaging systems
- transport protocols
- workers
- subscribers

This document defines how Domain Events are modelled within the Mosaic Domain Model and how they relate to the Reactive Runtime defined in MEG-002.

---

# Philosophy

Within Mosaic:

> **Business events originate in the domain. Runtime events transport them.**

This distinction is critical.

The domain determines:

> **What happened.**

The runtime determines:

> **How everyone else learns about it.**

The business owns facts.

The runtime owns communication.

---

# What Is A Domain Event?

A Domain Event represents an important business fact.

Examples include:

```
PlaybackCompleted
```

```
MediaImported
```

```
CollectionCreated
```

```
MetadataCorrected
```

Each represents a completed business transition.

Each becomes part of the domain's history.

---

# Domain Events Are Business Concepts

Domain Events belong entirely to the domain.

They should make sense even if:

- Go did not exist
- the runtime did not exist
- the application was rewritten tomorrow

Example.

```
PlaybackCompleted
```

is meaningful.

```
KafkaMessagePublished
```

is not.

Technology should never leak into the domain.

---

# Business Before Runtime

The lifecycle is intentionally separated.

```
Business Behaviour

↓

Aggregate State Changes

↓

Domain Event

↓

Runtime Event

↓

Subscribers
```

Notice:

The runtime appears **after** the domain.

The domain remains completely unaware of transport.

---

# Where Domain Events Come From

Domain Events originate from Aggregates.

Example.

```
PlaybackSession

↓

Complete()

↓

PlaybackCompleted
```

The Aggregate owns:

- business rules
- state transition
- business fact

Infrastructure merely transports the resulting event.

This follows the classic DDD pattern where Aggregates raise Domain Events as part of enforcing business behaviour. ([martinfowler.com](https://martinfowler.com/eaaDev/DomainEvent.html))

---

# Domain Events Follow Behaviour

Domain Events should follow completed behaviour.

Correct.

```
Collection

↓

Add Media

↓

MediaAddedToCollection
```

Incorrect.

```
AddMediaRequested
```

The domain records facts.

Not requests.

---

# One Business Transition

Every Domain Event should represent exactly one business transition.

Good.

```
PlaybackPaused
```

Poor.

```
PlaybackPausedAndRecommendationUpdated
```

Recommendations belong to another context.

One business fact.

One Domain Event.

---

# Domain Events Are Immutable

Once raised, a Domain Event MUST NOT change.

Example.

```
PlaybackCompleted

↓

Immutable
```

If business understanding changes later:

```
PlaybackCorrected
```

becomes a new Domain Event.

History is additive.

Never rewritten.

---

# Domain Events Belong To The Aggregate

Only the Aggregate owning the business state should raise the Domain Event.

Example.

```
Library Aggregate

↓

MediaImported
```

Metadata should never raise:

```
MediaImported
```

Ownership follows business ownership.

Always.

---

# Domain Events Are Internal

One of the most important distinctions within Mosaic is:

```
Domain Event

≠

Runtime Event
```

The Domain Event exists inside the domain.

The Runtime Event exists outside it.

They frequently represent the same business fact.

They serve different architectural purposes.

---

# Runtime Transformation

Conceptually.

```
PlaybackCompleted

↓

Domain Event

↓

Runtime Adapter

↓

Runtime Event

↓

Event Bus
```

The runtime adapter transforms domain concepts into transport concepts.

The Aggregate remains completely unaware of the Event Bus.

This separation keeps the domain pure while allowing the runtime to evolve independently.

---

# Domain Events Should Be Small

Domain Events should contain only information describing the business fact.

Example.

```
PlaybackCompleted

↓

Playback ID

Media ID

User ID

Completed At
```

Avoid:

- retry counts
- trace identifiers
- routing information
- worker identifiers

Those belong to runtime infrastructure.

---

# Domain Events Trigger Nothing

A Domain Event should never know:

- who receives it
- whether anyone receives it
- what happens next

It simply records:

> **This happened.**

Everything afterwards belongs to the runtime.

---

# Domain Events Are Not Integration Events

The domain should not model:

```
WebhookSent
```

```
KafkaPublished
```

```
APIMessageSent
```

These describe infrastructure.

Not business.

Instead.

```
PlaybackCompleted
```

The runtime determines how that fact is communicated externally.

---

# Event Ordering

Domain Events follow business chronology.

Example.

```
PlaybackStarted

↓

PlaybackPaused

↓

PlaybackResumed

↓

PlaybackCompleted
```

The domain defines this sequence.

The runtime may deliver them differently.

Business chronology and delivery chronology remain separate concepts.

---

# Event Collection

Aggregates SHOULD collect Domain Events during business execution.

Conceptually.

```
PlaybackSession

↓

Complete()

↓

Raise Domain Event

↓

Commit

↓

Runtime Publishes
```

Events should not leave the Aggregate until business consistency has been established.

This naturally complements the transactional boundaries defined earlier.

---

# Domain Events And Transactions

Domain Events should only be published externally after successful persistence.

Example.

```
Aggregate Updated

↓

Commit Successful

↓

Publish Runtime Event
```

If persistence fails:

The Domain Event never leaves the Aggregate.

Business facts should never describe work that never became true.

---

# Testing

Domain Events make business behaviour easy to test.

Example.

```
Playback Complete

↓

PlaybackCompleted Raised
```

Tests should verify:

- correct event
- correct payload
- correct timing

Testing business events is often simpler than testing infrastructure side effects.

---

# Evolution

Domain Events evolve with business understanding.

Initially.

```
PlaybackCompleted
```

Later.

```
PlaybackCompleted

↓

CompletionSource

↓

CompletionReason
```

The business language evolves.

The event evolves with it.

The event should never become more technical.

---

# Mosaic Examples

Examples of Domain Events include:

```
MediaImported
```

```
PlaybackStarted
```

```
PlaybackPaused
```

```
PlaybackCompleted
```

```
CollectionCreated
```

```
CollectionRenamed
```

```
MetadataCorrected
```

```
RecommendationGenerated
```

Every one represents an important business fact.

---

# Anti-Patterns

The following practices are prohibited.

## Infrastructure Events

```
KafkaPublished
```

```
WebhookDelivered
```

---

## Commands

```
RefreshMetadata
```

```
GenerateArtwork
```

---

## Mutable Events

Changing an event after it has been raised.

---

## Runtime Dependencies

Aggregates importing:

- Event Bus
- Kafka
- NATS
- RabbitMQ

The domain should remain transport agnostic.

---

## Publishing Before Commit

Publishing events before business state becomes durable.

---

## Business Logic Inside Subscribers

Business behaviour should occur before the Domain Event exists.

Subscribers react.

They do not redefine history.

---

# Mosaic Guidelines

Within Mosaic:

- Domain Events MUST describe completed business facts.
- Domain Events MUST originate from Aggregates.
- Domain Events MUST be immutable.
- Domain Events MUST remain independent of runtime infrastructure.
- Domain Events MUST NOT describe transport behaviour.
- Runtime Events SHOULD be derived from Domain Events.
- Domain Events SHOULD remain small and business focused.
- Domain Events SHOULD only leave the domain after successful persistence.

---

# Relationship to MEG

MEG-002 introduced Runtime Events.

This chapter deliberately introduces an additional layer.

```
Aggregate

↓

Domain Event

↓

Runtime Translation

↓

Runtime Event

↓

Reactive Runtime
```

This separation is one of the most important architectural decisions within Mosaic.

It ensures:

- the business remains independent
- the runtime remains replaceable
- transport remains invisible to the domain

The domain owns meaning.

The runtime owns delivery.

---

# Summary

Domain Events represent the moments that matter to the business.

They are not messages.

They are not notifications.

They are not transport.

They are simply immutable records that:

> **Something important became true.**

Everything else, including retries, workers, event buses and subscribers, exists solely to communicate those business facts throughout the platform.

That distinction keeps the Mosaic Domain Model remarkably clean while allowing the Reactive Runtime to remain highly sophisticated.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`10-domain-services.md`

**Next File**

`12-repositories.md`
