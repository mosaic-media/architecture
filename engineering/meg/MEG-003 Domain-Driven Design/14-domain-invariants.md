<!--
File: engineering/meg/MEG-003 Domain-Driven Design/14-domain-invariants.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Domain Invariants

> *Business rules are not suggestions. They define what it means for the domain to be correct.*

---

# Purpose

Every business domain contains rules that must always remain true.

Examples include:

- A playback position cannot exceed the media duration.
- A Collection cannot contain duplicate media.
- A User cannot own another user's Library.
- Watch progress cannot be negative.

These rules define the integrity of the business.

Domain-Driven Design refers to these rules as **Domain Invariants**.

This document defines how Domain Invariants should be identified, protected and enforced throughout the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Invalid business state should be impossible to represent.**

The responsibility of the Domain Model is not merely to process data.

Its responsibility is to prevent invalid business state from ever existing.

If an Aggregate can enter an invalid state, the model has failed.

---

# What Is A Domain Invariant?

A Domain Invariant is a business rule that must always be true.

Examples include:

```
Playback Progress

≤

Media Duration
```

```
Collection

↓

Unique Media
```

```
User

↓

Unique Username
```

The business assumes these rules are always satisfied.

The software should enforce them accordingly.

---

# Why Invariants Exist

Without invariants:

```
Playback

↓

Duration = 90 Minutes

↓

Progress = 120 Minutes
```

The system now contains impossible business state.

Every subsequent operation becomes more complicated because every consumer must now defend against invalid data.

Instead:

The invalid state should never be constructible.

---

# Business Rules

Only genuine business rules become invariants.

Examples.

Good.

```
Library Name Required
```

```
Playback Cannot Complete Before It Starts
```

Poor.

```
Maximum HTTP Connections
```

```
Database Timeout
```

Infrastructure rules belong elsewhere.

Invariants belong to the business.

---

# Invariants Belong To The Domain

Business rules should never be enforced solely by:

- controllers
- HTTP handlers
- repositories
- UI validation

Poor.

```
HTTP

↓

Validate

↓

Domain
```

Preferred.

```
Domain

↓

Validate

↓

Always Correct
```

Infrastructure may validate for convenience.

The Domain validates for correctness.

---

# Aggregate Responsibility

Aggregates own invariants.

Example.

```
PlaybackSession

↓

Advance()

↓

Validate Progress

↓

Apply Change
```

The Aggregate protects itself.

External callers should never be responsible for enforcing business rules.

---

# Entity Responsibility

Entities may also enforce local invariants.

Example.

```
Collection

↓

Rename()

↓

Name Cannot Be Empty
```

The Entity understands the rule because it owns the concept.

Business rules should live with the business object they describe.

---

# Value Objects

Value Objects frequently enforce invariants during construction.

Example.

```go
duration := NewDuration(seconds)
```

Possible rules:

- non-negative
- finite
- valid range

If construction fails:

The Value Object never exists.

This is preferable to creating invalid values and validating them later.

---

# Construction

Factories should also enforce invariants.

Poor.

```
Create Aggregate

↓

Validate Later
```

Preferred.

```
Validate

↓

Create Aggregate

↓

Always Valid
```

Every Aggregate should begin life in a valid business state.

Factories and constructors should enforce this from the outset.

---

# Protecting State

All state mutation should occur through business behaviour.

Poor.

```go
playback.Progress = progress
```

Preferred.

```go
playback.Advance(progress)
```

The Aggregate now controls:

- validation
- state transition
- invariant enforcement

Business correctness becomes automatic.

---

# Preventing Invalid State

The preferred strategy is prevention.

Not correction.

Poor.

```
Invalid State

↓

Fix Later
```

Preferred.

```
Reject Invalid Change
```

If invalid state never exists, downstream logic becomes dramatically simpler.

---

# Local Invariants

Some invariants exist entirely inside one Aggregate.

Example.

```
Collection

↓

Duplicate Media Prohibited
```

Only the Collection Aggregate needs to understand this rule.

No other capability participates.

These invariants should remain local.

---

# Cross-Aggregate Rules

Some business rules appear to span multiple Aggregates.

Example.

```
Library Storage Quota
```

```
Subscription Limits
```

These should rarely be enforced through distributed transactions.

Instead.

```
Aggregate

↓

Domain Event

↓

Another Aggregate

↓

Eventually Consistent
```

Only rules requiring immediate consistency belong inside one Aggregate.

Everything else should generally become eventual consistency.

---

# Expressing Invariants

Good business behaviour makes invariants obvious.

Example.

Instead of:

```go
SetCompleted(true)
```

Prefer.

```go
Complete()
```

The Aggregate now decides whether completion is valid.

Intent-revealing methods naturally reinforce business rules.

---

# Validation Order

Business behaviour should generally follow this pattern.

```
Validate

↓

Modify State

↓

Raise Domain Event
```

If validation fails:

State does not change.

No Domain Event is raised.

Business history remains correct.

---

# Domain Events

Domain Events should only be raised after invariants have been satisfied.

Poor.

```
Raise Event

↓

Validation Fails
```

Preferred.

```
Validation

↓

State Change

↓

Raise Event
```

Events describe completed truth.

Not attempted operations.

---

# Persistence

Repositories should never repair broken Aggregates.

Poor.

```
Repository

↓

Fix Invalid Aggregate

↓

Save
```

If an Aggregate reaches persistence in an invalid state:

The bug already occurred.

Repositories persist correctness.

They do not create it.

---

# Infrastructure Validation

UI validation.

HTTP validation.

JSON validation.

These improve user experience.

They do **not** replace Domain validation.

Every business rule should still exist inside the Domain.

Never trust external validation alone.

---

# Testing Invariants

Every invariant SHOULD have dedicated tests.

Examples.

```
Progress Cannot Exceed Duration
```

```
Collection Rejects Duplicates
```

```
Empty Library Name Rejected
```

Tests should verify:

- valid behaviour
- invalid behaviour
- edge cases

Business correctness deserves explicit verification.

---

# Evolving Rules

Business rules change.

For example.

Initially.

```
Collection

↓

Maximum 100 Items
```

Later.

```
Unlimited Collections
```

The invariant changes.

The Domain evolves.

Implementation follows.

The model should evolve with business understanding.

---

# Common Mosaic Invariants

Examples include:

Playback.

- Progress ≥ 0
- Progress ≤ Duration
- Completed implies Progress = Duration

Library.

- Library has an owner.
- Root collection always exists.

Collection.

- Media references are unique.
- Name cannot be empty.

Metadata.

- Primary artwork always exists.
- Source provider recorded.

User.

- Identity immutable.
- Username unique.

These examples are illustrative rather than exhaustive.

---

# Anti-Patterns

The following practices are prohibited.

## Validation Only In Controllers

Business rules enforced exclusively by HTTP.

---

## Public Mutable State

Allowing callers to bypass business behaviour.

---

## Invalid Aggregates

Allowing construction before validation.

---

## Repository Repair

Repositories silently fixing broken business objects.

---

## Duplicate Validation

Implementing business rules independently in:

- UI
- HTTP
- Services
- Domain

The Domain remains authoritative.

---

## Business Rules In Infrastructure

Embedding business validation inside persistence or transport layers.

---

# Mosaic Guidelines

Within Mosaic:

- Every business invariant MUST be enforced by the Domain.
- Aggregates MUST protect Aggregate invariants.
- Value Objects SHOULD validate themselves.
- Factories MUST construct valid Aggregates.
- Invalid state MUST NOT be representable.
- Domain Events MUST only follow successful validation.
- Repositories MUST persist already-valid Aggregates.
- Infrastructure validation MUST complement, not replace, Domain validation.

---

# Relationship to MEG

Factories ensure Aggregates begin life correctly.

Invariants ensure they remain correct.

Together they guarantee:

```
Construction

↓

Valid Aggregate

↓

Business Behaviour

↓

Valid Aggregate

↓

Persistence
```

The next chapter introduces **Modelling Guidelines**, bringing together the concepts introduced throughout MEG-003 into practical modelling advice for engineers designing new business capabilities.

---

# Summary

Domain Invariants are the rules that define business correctness.

They are not optional.

They are not advisory.

They are the reason the Domain Model exists.

Within Mosaic, every Aggregate, Entity and Value Object should actively prevent invalid business state rather than attempting to repair it afterwards.

Correctness should be the natural outcome of the model itself.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`13-factories.md`

**Next File**

`15-modelling-guidelines.md`
