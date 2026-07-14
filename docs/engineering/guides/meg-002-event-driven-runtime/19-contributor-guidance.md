<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/19-contributor-guidance.md
Document: MEG-002
Status: Draft
Version: 0.3
-->

# Contributor Guidance

> *The runtime belongs to the platform. Every contribution should strengthen its predictability, resilience and simplicity.*

---

# Purpose

The Mosaic Runtime is shared infrastructure.

Every capability, module and application depends upon it behaving consistently.

Unlike ordinary business code, runtime changes affect the entire ecosystem.

This document provides practical guidance for engineers contributing to the Event-Driven Runtime.

It explains how contributors should apply the architectural principles established throughout MEG-002.

---

# Philosophy

Within Mosaic:

> **Protect the runtime before extending it.**

New functionality should never compromise:

- determinism
- observability
- resilience
- compatibility
- simplicity

The runtime should evolve carefully.

Capabilities should evolve rapidly.

---

# Before Modifying The Runtime

Every contributor SHOULD understand:

- the runtime philosophy
- existing event contracts
- lifecycle semantics
- worker ownership
- retry behaviour
- scheduling model
- observability expectations

Runtime changes should never begin with implementation.

They should begin with understanding.

---

# Before Introducing A New Event

Ask:

- Does this describe a completed business fact?
- Does an equivalent event already exist?
- Which capability owns this event?
- Does this event belong in the business domain or the runtime?

Duplicate events should be avoided.

Business language should remain consistent.

---

# Before Creating A Runtime Event

Runtime events describe platform behaviour.

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

Business events describe domain behaviour.

Examples include:

```
playback.started
```

```
media.imported
```

Contributors should distinguish clearly between these two categories.

---

# Before Adding A Subscriber

Ask:

- Does this capability genuinely need the event?
- Can it remain independent?
- Is the subscriber idempotent?
- Does it own the resulting business state?

Subscribers should remain autonomous.

---

# Before Publishing An Event

Confirm:

- Business state has committed.
- Payload is complete.
- Metadata is correct.
- Event ownership is clear.
- Event naming follows MEG-002.
- The event represents a completed fact.

Events should never describe work that might happen.

Only work that has happened.

---

# Before Introducing Scheduling

Ask:

- Is this genuinely a scheduling concern?
- Does business logic own time?
- Should the runtime schedule this instead?

Business capabilities should request scheduling.

They should never implement it.

---

# Before Adding Retry Logic

Retry logic belongs to the runtime.

Contributors SHOULD NOT implement:

```go
for {

    err := process()

    if err == nil {
        break
    }

    time.Sleep(...)
}
```

Instead:

Return the failure.

Allow the runtime to determine retry behaviour.

---

# Before Creating A Worker

Ask:

- Can an existing worker pool execute this work?
- Does this require a new execution model?
- Who owns this worker?
- How does it stop?
- How is it observed?

Workers should never exist without explicit ownership.

---

# Before Changing Runtime Behaviour

The following changes SHOULD require architectural review.

- delivery guarantees
- lifecycle semantics
- retry strategy
- scheduling model
- shutdown behaviour
- event contracts
- runtime APIs

These changes affect every capability.

They should never be introduced casually.

---

# Before Merging

Every runtime contribution SHOULD satisfy the following checklist.

## Runtime Behaviour

- Event flow remains deterministic.
- Runtime remains business agnostic.
- Worker ownership remains clear.
- Scheduling remains centralised.

---

## Events

- Events describe facts.
- Event ownership is correct.
- Event naming follows MEG-002.
- Payloads remain immutable.

---

## Reliability

- Subscribers remain idempotent.
- Retries remain runtime managed.
- Shutdown remains graceful.
- Failure isolation remains intact.

---

## Observability

- Logs remain structured.
- Metrics updated where appropriate.
- Correlation preserved.
- Tracing unaffected.

---

## Documentation

- MEG updated if required.
- ADR created where appropriate.
- Event documentation updated.
- Examples remain correct.

Architecture documentation should evolve alongside runtime behaviour.

---

# Module Compatibility

Contributors should assume:

Third-party modules already exist.

Runtime changes should minimise:

- breaking changes
- behavioural surprises
- migration effort

The runtime is a platform contract.

Not merely an internal implementation.

---

# Runtime APIs

Public runtime APIs should remain:

- minimal
- explicit
- stable
- discoverable

Every exported runtime API becomes part of the long-term platform surface.

Expanding APIs is easy.

Removing them is not.

---

# Runtime Simplicity

When multiple implementations are possible, contributors SHOULD prefer the implementation that:

- introduces fewer concepts
- exposes fewer APIs
- requires less documentation
- remains easier to explain

Complexity should always justify itself.

---

# Review Mindset

Runtime reviews should focus upon:

- determinism
- compatibility
- ownership
- resilience
- observability
- architectural consistency

Performance should never come at the expense of runtime correctness.

---

# Runtime Testing

Contributors SHOULD validate:

- duplicate delivery
- retries
- shutdown
- replay
- worker cancellation
- scheduling
- event ordering
- module compatibility

The runtime should be tested under failure as thoroughly as under success.

---

# Learning The Runtime

New contributors SHOULD study MEG-002 in the following order.

```
Runtime Philosophy

↓

Event Model

↓

Event Bus

↓

Publishers

↓

Subscribers

↓

Workers

↓

Scheduling

↓

Idempotency

↓

Retries

↓

Shutdown

↓

Observability
```

Understanding the philosophy first makes implementation significantly easier to reason about.

---

# Engineering Culture

Runtime contributors should strive to:

- simplify existing behaviour
- improve documentation
- reduce coupling
- preserve compatibility
- question unnecessary complexity
- document architectural reasoning

The runtime should become simpler over time.

Not more complicated.

---

# Contributor Checklist

Before requesting review, confirm:

- [ ] The runtime remains business agnostic.
- [ ] Event contracts remain stable.
- [ ] Subscribers remain idempotent.
- [ ] Retry behaviour remains runtime owned.
- [ ] Scheduling remains centralised.
- [ ] Worker ownership is explicit.
- [ ] Shutdown remains graceful.
- [ ] Observability remains complete.
- [ ] Documentation has been updated.
- [ ] The runtime is simpler or clearer than before.

---

# Relationship to MEG-002

This document explains how contributors should apply the architectural principles established throughout the Event-Driven Runtime specification.

The previous chapters define:

> **How the runtime behaves.**

This chapter defines:

> **How engineers should evolve it.**

Protecting architectural consistency is a shared responsibility.

---

# Summary

The Event-Driven Runtime is one of the most stable components within the Mosaic platform.

Every capability depends upon it.

Every module trusts it.

Every contributor therefore shares responsibility for preserving its:

- simplicity
- predictability
- resilience
- compatibility
- observability

The best runtime contribution is often not the one that adds the most functionality.

It is the one that allows the platform to continue evolving without increasing architectural complexity.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`18-adrs.md`

**Next File**

`glossary.md`
