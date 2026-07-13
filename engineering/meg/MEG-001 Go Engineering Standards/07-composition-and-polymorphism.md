<!--
File: engineering/meg/MEG-001 Go Engineering Standards/07-composition-and-polymorphism.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Composition and Polymorphism

> *Composition builds systems. Polymorphism enables flexibility. They solve different problems and should never be confused.*

---

# Purpose

Go deliberately avoids classical inheritance.

Instead, it separates three concepts that inheritance traditionally combines:

- Code reuse
- Behavioural polymorphism
- Object hierarchy

Within Mosaic, these concerns are treated independently.

Composition is used for building systems.

Interfaces are used for polymorphism.

Embedding is used sparingly as a convenience.

This separation produces software that is easier to understand, easier to evolve and significantly less coupled than inheritance-based designs. Go's own documentation describes embedding as a mechanism for code reuse rather than subclassing.  [oai_citation:0‡Go](https://go.dev/doc/effective_go?utm_source=chatgpt.com)

---

# Philosophy

Within Mosaic:

> **Compose behaviour. Never inherit implementation.**

Complex systems should emerge from combining small, focused components.

No component should exist merely because another component "extends" it.

Instead, components collaborate.

---

# Three Different Concepts

One of the biggest misconceptions among engineers transitioning from Java is assuming composition, embedding and polymorphism are interchangeable.

They are not.

Each exists for a different purpose.

| Concept | Purpose |
|----------|---------|
| Composition | Build larger behaviour from smaller components |
| Embedding | Reduce delegation boilerplate |
| Interfaces | Enable behavioural polymorphism |

Keeping these concepts separate leads to significantly simpler software.

---

# Composition

Composition is the primary architectural mechanism within Mosaic.

Example:

```go
type LibraryService struct {
    metadata MetadataProvider
    events   Publisher
    cache     Cache
}
```

The service does not inherit functionality.

Instead, it collaborates with other components.

Each dependency owns its own responsibility.

The resulting service becomes easier to:

- understand
- replace
- test
- extend

---

# Think In Capabilities

Instead of asking:

> What should this object inherit?

Ask:

> What capabilities does this component require?

Example.

```
Playback Service

↓

Metadata Provider

↓

Transcoder

↓

Progress Store

↓

Event Publisher
```

Each capability remains independently replaceable.

No capability needs knowledge of the others.

---

# Composition Produces Better Boundaries

Inheritance often produces deep hierarchies.

```
Media

↓

Video

↓

Movie

↓

AnimeMovie
```

Responsibility becomes fragmented across multiple types.

Instead:

```
Movie

↓

Metadata

↓

Artwork

↓

Playback

↓

Progress
```

Each concern remains isolated.

Business concepts remain obvious.

---

# Embedding

Struct embedding is a language convenience.

It promotes methods from one type onto another.

Example:

```go
type Job struct {
    *log.Logger
}
```

The `Job` now exposes the logger's methods directly.

However:

The logger still exists as a field.

It has **not** become a superclass.

Embedding should therefore be viewed as syntactic convenience rather than inheritance.  [oai_citation:1‡Go](https://go.dev/doc/effective_go?utm_source=chatgpt.com)

---

# When To Embed

Embedding SHOULD only be used when:

- the embedded type is conceptually part of the containing type
- method promotion improves readability
- ownership remains obvious

Examples include:

- loggers
- mutexes
- reusable infrastructure helpers

Embedding should improve ergonomics.

Not architecture.

---

# When Not To Embed

Avoid embedding purely to imitate inheritance.

Poor:

```go
type UserService struct {
    BaseService
}
```

Questions immediately arise.

What is a BaseService?

Why does every service inherit it?

What behaviour does it actually own?

This pattern usually indicates an object-oriented design has been translated directly into Go.

Instead:

```go
type UserService struct {
    logger *slog.Logger
    events Publisher
}
```

Dependencies become explicit.

Responsibilities remain clear.

---

# Polymorphism

Polymorphism allows different implementations to satisfy the same behaviour.

Go achieves this through interfaces.

Example:

```go
type Storage interface {
    Save(context.Context, Media) error
}
```

Multiple implementations may exist.

```
Postgres

↓

Storage
```

```
DuckDB

↓

Storage
```

```
Memory

↓

Storage
```

The service does not care which implementation it receives.

It depends only upon behaviour.

---

# Behaviour Before Type

Within Mosaic, engineers should think:

> I need something that can publish events.

Not:

> I need a Kafka publisher.

The implementation becomes a deployment decision.

The behaviour remains constant.

---

# Composition Enables Polymorphism

Composition and interfaces work together.

```
Service

↓

Publisher Interface

↓

NATS Publisher
```

or

```
Service

↓

Publisher Interface

↓

Memory Publisher
```

The service remains unchanged.

Only composition changes.

This is one of Go's greatest strengths.

---

# Avoid Base Types

The following patterns SHOULD NOT exist.

```
BaseService
```

```
BaseRepository
```

```
AbstractHandler
```

```
AbstractProvider
```

These names rarely communicate genuine responsibilities.

Instead, they accumulate unrelated behaviour until they become impossible to reason about.

If multiple types genuinely require shared behaviour, extract a reusable component rather than inventing a base type.

---

# Favour Delegation

Suppose several services require metrics.

Avoid:

```text
BaseService

↓

Metrics

↓

Logging

↓

Tracing
```

Prefer:

```go
type Service struct {
    metrics Metrics
}
```

Delegation keeps ownership explicit.

Every dependency remains visible.

---

# Reuse Behaviour, Not Identity

Inheritance answers:

> "Is this an X?"

Composition answers:

> "Can this perform X?"

The second question usually produces better software.

Components become reusable because of what they do.

Not because of where they appear in a hierarchy.

---

# Mosaic Guidelines

Within Mosaic:

- Composition MUST be preferred over inheritance.
- Embedding SHOULD only be used where it improves ergonomics.
- Embedding MUST NOT be used to simulate inheritance.
- Shared behaviour SHOULD become reusable components.
- Interfaces provide polymorphism.
- Components collaborate through behaviour rather than hierarchy.
- Base classes and abstract classes are prohibited.

---

# Decision Checklist

Before embedding or introducing shared behaviour, ask:

1. Am I reducing duplication or creating hierarchy?
2. Would explicit composition be easier to understand?
3. Does embedding genuinely improve readability?
4. Does this introduce hidden behaviour?
5. Would another engineer immediately understand the relationship?

If the answer to any question introduces doubt, explicit composition should generally be preferred.

---

# Summary

Composition is the architectural foundation of Go.

Embedding is a convenience.

Interfaces enable polymorphism.

Each solves a different problem.

Keeping these concepts separate allows Mosaic to produce software that is modular, testable and resilient to change without inheriting the complexity traditionally associated with object-oriented inheritance.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`06-interfaces-and-abstraction.md`

**Next File**

`08-error-handling.md`
