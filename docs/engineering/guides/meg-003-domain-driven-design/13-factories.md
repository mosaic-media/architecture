<!--
File: docs/engineering/guides/meg-003-domain-driven-design/13-factories.md
Document: MEG-003
Status: Draft
Version: 0.4
-->

# Factories

> *Construction is not business behaviour. Complex creation should be hidden so the domain begins life in a valid state.*

---

# Purpose

Some domain objects are simple to construct.

Others are not.

Creating an Aggregate may require:

- multiple Entities
- several Value Objects
- validation
- business rules
- default state
- invariant enforcement

Embedding this logic inside constructors or Application Services quickly leads to duplicated and inconsistent creation logic.

Factories solve this problem.

They encapsulate complex object creation while ensuring every new domain object begins life in a valid business state.

---

# Philosophy

Within Mosaic:

> **Factories create valid domain objects. They do not perform business behaviour.**

Factories exist to solve one problem:

> **How should a complex business object be created correctly?**

They should not become:

- service layers
- repositories
- orchestrators
- builders
- workflow engines

Their responsibility begins and ends with construction.

---

# Why Factories Exist

Consider creating a new Library.

Requirements might include:

- unique identifier
- default settings
- root collection
- default permissions
- import configuration

Without a Factory:

```go
library := &Library{
    ...
}
```

The caller must know:

- every required field
- every default
- every invariant

This knowledge becomes duplicated throughout the application.

A Factory centralises that knowledge.

DDD factories exist specifically to separate object construction from object use while ensuring newly created Aggregates satisfy all invariants.  [O'Reilly Media](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/ch11lev1sec1.html)

---

# What Is A Factory?

A Factory is responsible for creating:

- Entities
- Aggregates
- occasionally Value Objects

in a valid business state.

A Factory does **not** own the resulting object.

Ownership transfers immediately to the caller.

---

# Construction Is Not Behaviour

Factories should create objects.

They should not perform business operations.

Good.

```

Create Library
```

Poor.

```mermaid
flowchart TD

N1["Create Library"]
N2["Import Media"]
N3["Generate Artwork"]
N4["Publish Events"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Creation and behaviour should remain separate.

---

# Valid From Birth

Factories SHOULD guarantee that every created object satisfies its business invariants.

Poor.

```go
library := &Library{}

library.Name = name

library.Owner = owner

library.Validate()
```

Preferred.

```go
library, err := NewLibrary(...)
```

Invalid objects should never exist, even temporarily.

---

# Aggregate Creation

Factories are most valuable when creating Aggregates.

Example.

```mermaid
flowchart TD

N1["Library Factory"]
N2["Library"]
N3["Default Collection"]
N4["Configuration"]
N5["Policies"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The caller receives a complete Aggregate.

Not a partially initialised object.

---

# Factory Or Constructor?

The simplest solution should always be preferred.

Use a constructor when:

- creation is straightforward
- invariants are simple
- dependencies are minimal

Example.

```go
NewDuration(...)
```

Use a Factory when:

- multiple objects must be assembled
- creation logic is complex
- business rules determine construction
- Aggregate assembly becomes non-trivial

Factories should emerge naturally.

Not automatically.

---

# Factory Methods

Many Aggregates naturally create their own internal objects.

Example.

```mermaid
flowchart TD

N1["Collection"]
N2["AddMedia()"]
N3["CollectionItem Created"]

N1 --> N2
N2 --> N3
```

The Aggregate Root itself acts as the Factory.

This is often preferable to introducing another type.

Only introduce a dedicated Factory when creation logic genuinely becomes complex.

Evans and Vernon both encourage using Aggregate methods as factories where the creation naturally belongs to the Aggregate itself.  [O'Reilly Media](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/ch11.html)

---

# Domain Language

Factory names should communicate business intent.

Good.

```

LibraryFactory
```

```

PlaybackFactory
```

```

CollectionFactory
```

Poor.

```

ObjectFactory
```

```

EntityBuilder
```

```

GenericFactory
```

Names should reinforce the ubiquitous language.

---

# Factory Responsibilities

Factories MAY:

- validate creation rules
- assemble child Entities
- construct Value Objects
- assign identities
- establish defaults

Factories MUST NOT:

- persist objects
- publish events
- start workflows
- access HTTP
- perform infrastructure operations

Their responsibility ends once construction completes.

---

# Factory Dependencies

Factories should depend only upon:

- domain concepts
- domain policies
- domain services

They should never depend directly upon:

- databases
- message buses
- HTTP
- file systems

Construction remains a domain concern.

Persistence does not.

---

# Identities

Factories frequently create identities.

Example.

```mermaid
flowchart TD

N1["LibraryFactory"]
N2["Generate LibraryID"]
N3["Create Aggregate"]

N1 --> N2
N2 --> N3
```

The mechanism used to generate the identifier is an implementation concern.

The resulting identity is a domain concept.

---

# Value Objects

Simple Value Objects rarely require Factories.

Usually:

```go
duration := NewDuration(...)
```

is entirely sufficient.

Dedicated Factories for simple immutable Value Objects generally introduce unnecessary complexity.

---

# Aggregate Integrity

Factories should create complete Aggregates.

Poor.

```mermaid
flowchart TD

N1["Library"]
N2["Missing Root Collection"]

N1 --> N2
```

Preferred.

```mermaid
flowchart TD

N1["Library"]
N2["Root Collection"]
N3["Configuration"]
N4["Ready"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The caller should never be responsible for "finishing" Aggregate construction.

---

# Application Services

Application Services frequently use Factories.

Example.

```mermaid
flowchart TD

N1["Command"]
N2["Application Service"]
N3["Library Factory"]
N4["Repository"]
N5["Runtime"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Notice:

The Application Service coordinates.

The Factory constructs.

The Repository persists.

Responsibilities remain distinct.

---

# Testing

Factories should be easy to test.

Typical tests verify:

- valid construction
- invariant enforcement
- default values
- invalid inputs

Factories should remain deterministic.

The same inputs should produce equivalent business objects.

---

# Evolution

Factories should evolve alongside the domain.

Initially.

```

NewLibrary(...)
```

Later.

```mermaid
flowchart TD

N1["LibraryFactory"]
N2["Policies"]
N3["Defaults"]
N4["Configuration"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Complexity should move into the Factory only when it genuinely exists.

Do not anticipate complexity prematurely.

---

# What Is Not A Factory?

The following are **not** Factories.

```

Repository
```

Repositories retrieve and persist.

---

```

Application Service
```

Coordinates use cases.

---

```

Domain Service
```

Models business behaviour.

---

```

Builder
```

Supports incremental object construction.

Factories produce complete domain objects.

---

# Mosaic Examples

Appropriate Factory responsibilities include:

```mermaid
flowchart TD

N1["LibraryFactory"]
N2["Create new Library Aggregate"]

N1 --> N2
```

```mermaid
flowchart TD

N1["CollectionFactory"]
N2["Create default Collection hierarchy"]

N1 --> N2
```

```mermaid
flowchart TD

N1["PlaybackFactory"]
N2["Create new Playback Session"]

N1 --> N2
```

```mermaid
flowchart TD

N1["ImportFactory"]
N2["Create Import Job Aggregate"]

N1 --> N2
```

Each creates a valid business object.

None execute business workflows.

---

# Anti-Patterns

The following practices are prohibited.

## Partially Constructed Aggregates

Returning objects that require additional setup before becoming valid.

---

## Factory As Service

Factories performing business operations after construction.

---

## Infrastructure Inside Factories

Factories executing SQL, HTTP or message publication.

---

## Generic Factory

```

ObjectFactory
```

creating unrelated domain concepts.

---

## Builders For Everything

Introducing Builder patterns where a simple constructor or Aggregate factory method is clearer.

---

# Mosaic Guidelines

Within Mosaic:

- Factories SHOULD create valid Aggregates.
- Factories SHOULD encapsulate complex construction.
- Factories MUST enforce creation invariants.
- Factories MUST remain infrastructure independent.
- Aggregate factory methods SHOULD be preferred where creation naturally belongs to the Aggregate.
- Constructors SHOULD be preferred for simple creation.
- Factories MUST NOT perform persistence.
- Factories MUST NOT publish events.

---

# Relationship to MEG

Repositories answer:

> **How do I retrieve and persist Aggregates?**

Factories answer:

> **How do I create Aggregates correctly?**

Together they define the beginning and end of an Aggregate's lifecycle.

The next chapter introduces **Domain Invariants**, the business rules that every Aggregate, Factory and Entity must protect throughout that lifecycle.

---

# Summary

Factories exist to protect one of the most important moments in a domain object's life:

> **Its creation.**

Within Mosaic, every Aggregate should begin life:

- complete
- valid
- consistent
- expressive

By encapsulating construction inside Factories, the domain remains focused on business concepts rather than construction mechanics, and every new object enters the system already satisfying the rules that define it.
