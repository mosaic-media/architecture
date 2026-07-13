<!--
File: engineering/meg/MEG-003 Domain-Driven Design/07-value-objects.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Value Objects

> *A Value Object is defined entirely by what it is, not by who it is.*

---

# Purpose

Not every business concept requires identity.

Many concepts exist purely because of the information they represent.

Examples include:

- Duration
- Resolution
- Language
- Rating
- Position
- File Size

The business does not distinguish between two identical durations.

Nor does it care whether one language object was created before another.

These concepts are modelled as **Value Objects**.

This document defines how Value Objects should be designed and used throughout the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **If identity is irrelevant, model the concept as a Value Object.**

Value Objects exist because of their value.

Two Value Objects containing identical values represent exactly the same business concept.

Unlike Entities, they possess no lifecycle or identity.

---

# What Is A Value Object?

A Value Object is a business concept whose identity is irrelevant.

Examples include:

```
Duration
```

```
Resolution
```

```
Aspect Ratio
```

```
Language
```

```
Watch Position
```

Each represents a meaningful business concept.

None require identity.

---

# Value Defines Equality

Unlike Entities:

Value Objects are equal when all of their values are equal.

Example.

```
Duration

↓

01:30:00
```

equals

```
Duration

↓

01:30:00
```

There is no business distinction between them.

Creating another identical Value Object creates the same concept.

---

# No Identity

Value Objects MUST NOT possess business identity.

Poor.

```
ResolutionID
```

```
LanguageID
```

```
DurationID
```

These identifiers communicate nothing useful.

The value itself already defines the concept.

---

# Immutability

Value Objects SHOULD be immutable.

Changing:

```
Duration

↓

90 Minutes

↓

95 Minutes
```

does not modify the existing Value Object.

Instead:

```
Old Value Object

↓

New Value Object
```

Immutability greatly simplifies reasoning, testing and concurrent execution.

It also aligns naturally with Go's preference for immutable value semantics where practical.

---

# Behaviour

Value Objects may contain behaviour.

Example.

```go
duration.Add(other)
```

```go
position.Progress(total)
```

```go
resolution.IsHDR()
```

Behaviour should naturally belong with the concept.

Avoid reducing Value Objects to passive data containers.

---

# Rich Concepts

Prefer:

```
Watch Position
```

rather than:

```
int64
```

Prefer:

```
Media Duration
```

rather than:

```
time.Duration
```

The standard library type may still be used internally.

However, wrapping important business concepts inside explicit Value Objects communicates intent more clearly.

---

# Primitive Obsession

One of the most common modelling mistakes is representing business concepts using primitive types.

Poor.

```go
type Media struct {
    Duration int
}
```

Questions immediately arise.

Duration:

- Seconds?
- Milliseconds?
- Frames?

Instead.

```go
type Media struct {
    Duration Duration
}
```

The domain becomes significantly clearer.

Martin Fowler refers to overuse of primitive types in place of richer domain concepts as **Primitive Obsession**, a common code smell. ([martinfowler.com](https://martinfowler.com/bliki/ValueObject.html))

---

# Validation

Value Objects SHOULD validate themselves during construction.

Example.

```go
duration := NewDuration(seconds)
```

Validation may include:

- non-negative values
- valid ranges
- supported formats

Invalid Value Objects should never exist.

Constructors should enforce correctness immediately.

---

# Side Effects

Value Objects MUST NOT have side effects.

They should never:

- publish events
- persist state
- call external systems
- modify repositories

They simply represent business concepts.

Their behaviour should remain deterministic.

---

# Ownership

Value Objects belong to the Entity or Aggregate that owns them.

Example.

```
Media

↓

Duration

↓

Resolution

↓

Language
```

The Value Objects have no independent lifecycle.

If the Media Entity disappears, so do its associated Value Objects.

---

# Persistence

Repositories persist Value Objects as part of their owning Entity or Aggregate.

Value Objects should never have independent repositories.

Poor.

```
ResolutionRepository
```

Unless Resolution has become a business concept with identity, this repository should not exist.

---

# Reuse

Value Objects should be reused whenever the same business concept appears.

Example.

```
Duration
```

should represent duration consistently throughout:

- Playback
- Metadata
- Library
- Video Analysis

The ubiquitous language should remain consistent.

---

# Value Object Composition

Value Objects may contain other Value Objects.

Example.

```
Video Format

↓

Resolution

↓

Frame Rate

↓

Aspect Ratio
```

This produces richer, more expressive models without introducing identity.

---

# Entities Use Value Objects

Entities should compose Value Objects.

Example.

```
Media

├── MediaID
├── Duration
├── Resolution
├── Language
└── Artwork
```

Notice:

Only one concept possesses identity.

Everything else represents value.

This naturally produces smaller, more focused Entities.

---

# Avoid Shared Mutable State

Because Value Objects are immutable, they may safely be shared.

Example.

```
English Language

↓

Media A

↓

Media B

↓

Media C
```

Sharing immutable values introduces no coupling.

Immutability greatly simplifies concurrent systems.

---

# Avoid Generic Types

Avoid modelling business concepts using:

```
string
```

```
int
```

```
bool
```

where richer concepts exist.

Instead of:

```go
Rating int
```

Prefer:

```go
Rating Rating
```

The additional type communicates business meaning.

The compiler also prevents accidental misuse.

---

# Business Language

Value Objects should reinforce the ubiquitous language.

Good.

```
WatchProgress
```

```
PlaybackPosition
```

```
ArtworkType
```

Poor.

```
ProgressDTO
```

```
PositionValue
```

```
ImageInfo
```

Names should communicate business concepts.

Not implementation.

---

# Evolution

Value Objects often become richer over time.

Initially.

```
Resolution

↓

Width

Height
```

Later.

```
Resolution

↓

Width

Height

Aspect Ratio

Orientation

HDR Support
```

Business understanding evolves.

Value Objects should evolve alongside it.

---

# What Is Not A Value Object?

The following are usually **not** Value Objects.

```
Media
```

```
User
```

```
Collection
```

```
Playback Session
```

These possess identity.

They are therefore Entities.

---

# Mosaic Examples

Examples of Value Objects within Mosaic include:

```
Duration
```

```
Resolution
```

```
AspectRatio
```

```
Language
```

```
PlaybackPosition
```

```
MediaRating
```

```
ArtworkType
```

```
FileHash
```

Each is recognised because of its value.

Not because of an independent identity.

---

# Anti-Patterns

The following practices are prohibited.

## Mutable Value Objects

Changing the internal state of an existing Value Object.

---

## Identity

Assigning identifiers to Value Objects.

---

## Primitive Obsession

Representing business concepts entirely using primitive types.

---

## Infrastructure Dependencies

Importing:

- SQL
- HTTP
- Logging
- Runtime

into Value Objects.

---

## Side Effects

Publishing events or modifying repositories.

---

## Independent Persistence

Persisting Value Objects independently from their owning Entity.

---

# Mosaic Guidelines

Within Mosaic:

- Value Objects MUST be defined by value.
- Value Objects SHOULD be immutable.
- Value Objects MUST NOT possess identity.
- Value Objects SHOULD validate themselves during construction.
- Value Objects MAY contain behaviour.
- Value Objects MUST remain infrastructure independent.
- Entities SHOULD compose Value Objects.
- Business concepts SHOULD be preferred over primitive types.

---

# Relationship to MEG

Entities answer:

> **Who is this?**

Value Objects answer:

> **What is this?**

Together they form the fundamental vocabulary of every rich domain model.

The next chapter introduces **Aggregates**, which define how multiple Entities and Value Objects collaborate while preserving business consistency.

---

# Summary

Value Objects are one of the simplest yet most powerful modelling tools within Domain-Driven Design.

By representing business concepts through immutable values rather than primitive types, the Mosaic domain becomes:

- more expressive
- more type-safe
- easier to understand
- easier to test
- naturally thread-safe

Most importantly, the software begins speaking the language of the business rather than the language of the implementation.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`06-entities.md`

**Next File**

`08-aggregates.md`
