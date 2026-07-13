<!--
File: engineering/meg/MEG-001 Go Engineering Standards/06-interfaces-and-abstraction.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Interfaces and Abstraction

> *Abstraction should remove complexity, not introduce it. Every interface should exist because it solves a real problem, not because another language would have required one.*

---

# Purpose

Interfaces are one of Go's most powerful language features.

They are also one of the most commonly misunderstood.

Engineers transitioning from object-oriented languages frequently overuse interfaces, introducing unnecessary abstraction layers that reduce readability without improving flexibility.

This document defines how interfaces and abstractions should be designed throughout the Mosaic ecosystem.

---

# Philosophy

Within Mosaic:

> **Concrete first. Abstract second. Interface last.**

An interface is not the starting point of a design.

It is the result of discovering common behaviour between independently useful implementations.

Abstraction should emerge naturally.

It should never be assumed.

---

# What Is An Interface?

An interface describes **behaviour**.

It does **not** describe:

- ownership
- implementation
- storage
- inheritance
- lifecycle

For example:

```go
type Publisher interface {
    Publish(ctx context.Context, event Event) error
}
```

The interface communicates one thing.

> Something can publish events.

It intentionally says nothing about:

- Kafka
- NATS
- RabbitMQ
- WebSockets
- Memory

That decision belongs to the implementation.

---

# Why Interfaces Exist

Interfaces exist to reduce coupling.

They allow one component to depend upon behaviour rather than implementation.

This enables:

- testing
- substitution
- modularity
- evolution

Interfaces should therefore be introduced only when they reduce coupling.

Adding an interface that nobody needs increases complexity.

---

# Start With Concrete Types

Every implementation should begin as a concrete type.

Example:

```go
type Service struct {
    repo *Repository
}
```

Do not begin here:

```go
type Service interface {
    Create(...)
    Delete(...)
    Update(...)
}
```

The interface has no consumers.

It communicates nothing.

It merely adds another file to maintain.

Concrete implementations are easier to understand.

Interfaces can always be extracted later.

---

# Interfaces Belong To The Consumer

One of the most important Go design principles is:

> **The consumer owns the interface.**

Example:

```
metadata

↓

library
```

If `library` only needs:

```go
Find(id string)
```

then `library` defines:

```go
type MetadataProvider interface {
    Find(ctx context.Context, id string) (*Media, error)
}
```

The metadata package simply satisfies it.

The metadata package does **not** need to know the interface exists.

This produces smaller, more focused abstractions and aligns with widely accepted Go design guidance. ([go.dev](https://go.dev/doc/effective_go?v=1&utm_source=chatgpt.com))

---

# Accept Interfaces

Functions SHOULD accept interfaces whenever behaviour is required.

Example:

```go
func NewLibraryService(
    repo Repository,
) *Service
```

The service depends on behaviour.

Not implementation.

This allows:

- production repositories
- in-memory repositories
- mock repositories
- future repositories

without changing the service.

---

# Return Concrete Types

Constructors SHOULD return concrete implementations.

Preferred:

```go
func NewService(...) *Service
```

Avoid:

```go
func NewService(...) Service
```

Returning concrete types allows future API evolution.

Callers remain free to define their own interfaces if required.

Returning interfaces unnecessarily restricts future development.

---

# Keep Interfaces Small

Interfaces SHOULD describe one responsibility.

Excellent:

```go
type Reader interface {
    Read([]byte) (int, error)
}
```

Good:

```go
type Publisher interface {
    Publish(context.Context, Event) error
}
```

Poor:

```go
type MediaService interface {

    Find()

    Update()

    Delete()

    Publish()

    Sync()

    Backup()

    Export()

    Import()

    Validate()
}
```

Large interfaces become difficult to implement, difficult to mock and difficult to understand.

---

# Interface Segregation

Consumers should depend only upon behaviour they require.

Instead of:

```text
Repository

↓

Everything
```

Prefer:

```
Finder

Writer

Publisher

Scheduler
```

Each consumer receives only the behaviour it needs.

---

# Avoid "Impl"

Avoid names such as:

```
RepositoryImpl
```

```
DefaultRepository
```

```
UserServiceImpl
```

These names usually indicate object-oriented thinking rather than Go thinking.

Instead:

```
Repository
```

```
Service
```

```
Store
```

```
Client
```

Implementation details should remain invisible.

---

# Avoid Premature Abstraction

Do not introduce interfaces because:

- "we might have another implementation"
- "Java does this"
- "everything should be testable"

Instead ask:

> Is there currently more than one consumer?

> Is this coupling causing a problem?

> Does an interface simplify the architecture?

If not:

Do not create one.

---

# When To Introduce An Interface

Interfaces become appropriate when:

- multiple packages depend upon the same behaviour
- testing genuinely benefits
- different implementations naturally exist
- infrastructure varies while behaviour remains stable

Examples include:

- storage providers
- event publishers
- authentication providers
- metadata providers
- external APIs

---

# Abstraction Smells

The following usually indicate unnecessary abstraction.

## Single Implementation

```
Repository

↓

RepositoryImpl
```

---

## Interface With One User

```
Service

↓

ServiceImpl

↓

One caller
```

---

## Mirror Interfaces

```
Every struct

↓

Matching interface
```

---

## Generic Interfaces

```
Manager
```

```
Provider
```

```
Processor
```

without clearly defined behaviour.

---

## Empty Interfaces

```
interface{}
```

or

```
any
```

used to avoid designing proper types.

Generics and `any` should communicate genuine flexibility.

They should never hide uncertainty.

---

# Prefer Behaviour Over Type

Poor:

```
Can this object become another subclass?
```

Better:

```
What behaviour does this consumer require?
```

This small change fundamentally alters software architecture.

Behaviour becomes modular.

Types remain simple.

---

# Mosaic Guidelines

Within Mosaic:

- Interfaces MUST represent behaviour.
- Interfaces SHOULD belong to consumers.
- Constructors SHOULD return concrete types.
- Functions SHOULD accept interfaces where appropriate.
- Interfaces SHOULD remain small.
- Interfaces SHOULD emerge naturally.
- Large "god interfaces" are prohibited.

If an interface cannot be explained in one sentence, it is probably too large.

---

# Summary

Interfaces are among Go's most elegant features.

Used well, they reduce coupling and improve flexibility.

Used poorly, they recreate the complexity of inheritance-based object-oriented systems.

Within Mosaic, abstraction is considered successful when:

- behaviour becomes easier to understand
- coupling decreases
- testing becomes simpler
- implementation details disappear

If abstraction increases complexity instead, it has failed.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`05-dependency-management.md`

**Next File**

`07-composition-and-polymorphism.md`
