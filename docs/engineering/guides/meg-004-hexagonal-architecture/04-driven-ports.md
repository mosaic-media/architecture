<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/04-driven-ports.md
Document: MEG-004
Status: Draft
-->

# Driven Ports

> *Driven Ports describe the capabilities the Domain requires from the outside world. They never describe how those capabilities are implemented.*

---

# Purpose

Business behaviour frequently depends upon external capabilities.

Examples include:

- loading Aggregates
- persisting changes
- retrieving metadata
- storing artwork
- generating identifiers
- obtaining the current time

The Domain requires these capabilities.

It should not know how they are fulfilled.

Driven Ports define these requirements.

They represent the contracts through which the Domain requests services from infrastructure while remaining completely independent of implementation.

---

# Philosophy

Within Mosaic:

> **The Domain expresses needs. Infrastructure fulfils them.**

A Driven Port answers one question.

> **What capability does the Domain require?**

It never answers:

> **Which technology provides it?**

Implementation remains outside the Domain.

---

# What Is A Driven Port?

A Driven Port is an interface representing a capability required by the Domain.

Examples include:

```

LibraryRepository
```

```

MetadataProvider
```

```

ArtworkStore
```

```

Clock
```

```

IdentityGenerator
```

Each describes behaviour.

None describe technology.

---

# Why Driven Ports Exist

Without Driven Ports:

```mermaid
flowchart TD

N1["Playback"]
N2["PostgreSQL"]
N3["SQL"]
N4["Persistence"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The Domain now understands infrastructure.

Instead.

```mermaid
flowchart TD

N1["Playback"]
N2["PlaybackRepository"]
N3["PostgreSQL Adapter"]

N1 --> N2
N2 --> N3
```

Only the Adapter knows PostgreSQL exists.

The Domain remains infrastructure independent.

---

# Dependency Inversion

Driven Ports are the mechanism through which Dependency Inversion is achieved.

```mermaid
flowchart TD

N1["Domain"]
N2["Interface"]
N3["Infrastructure"]

N1 --> N2
N2 --> N3
```

Not:

```mermaid
flowchart TD

N1["Infrastructure"]
N2["Interface"]
N3["Domain"]

N1 --> N2
N2 --> N3
```

The Domain owns every dependency it requires.

Infrastructure adapts itself to satisfy those contracts.

---

# The Domain Defines Requirements

A Driven Port expresses a business requirement.

Example.

```

PlaybackRepository
```

The Domain requires:

```

Load Playback

Save Playback
```

It does **not** require:

```

SQL

Transactions

Indexes

Connection Pools
```

Those concerns belong entirely to infrastructure.

---

# Ports Describe Behaviour

Driven Ports should describe business behaviour.

Good.

```go
type MetadataProvider interface {

    Metadata(...)
}
```

Poor.

```go
type TMDBClient interface {

    GetMovie(...)
}
```

The first describes business intent.

The second exposes infrastructure.

---

# Business Language

Driven Ports should reinforce the ubiquitous language.

Good.

```

ArtworkStore
```

```

IdentityGenerator
```

```

RecommendationRepository
```

Poor.

```

BlobClient
```

```

DatabaseAccess
```

```

RedisCache
```

Technology names should never appear within the Domain.

---

# Multiple Implementations

One Driven Port may have many implementations.

Example.

```mermaid
flowchart TD

N1["MetadataProvider"]
N2["TMDB Adapter"]
N3["AniList Adapter"]
N4["Local Cache Adapter"]
N5["Test Adapter"]

N1 --> N2
N1 --> N3
N1 --> N4
N1 --> N5
```

The Domain remains unchanged.

Adapters become interchangeable.

This flexibility is one of the primary architectural benefits of Hexagonal Architecture.

---

# Repositories

Repositories are among the most common Driven Ports.

Example.

```mermaid
flowchart TD

N1["Playback Domain"]
N2["PlaybackRepository"]
N3["PostgreSQL"]

N1 --> N2
N2 --> N3
```

The Domain depends upon:

```

PlaybackRepository
```

Only.

Persistence remains completely replaceable.

---

# External Providers

External services should always appear behind Driven Ports.

Example.

```mermaid
flowchart TD

N1["Metadata Domain"]
N2["MetadataProvider"]
N3["TMDB"]

N1 --> N2
N2 --> N3
```

Later.

```mermaid
flowchart TD

N1["MetadataProvider"]
N2["AniList"]

N1 --> N2
```

The Domain does not change.

Only the Adapter changes.

---

# Time

Time is infrastructure.

Poor.

```go
time.Now()
```

inside the Domain.

Preferred.

```mermaid
flowchart TD

N1["Clock"]
N2["Current Time"]

N1 --> N2
```

The Domain requests:

```

Current Time
```

The infrastructure determines how that time is obtained.

This improves both testing and determinism.

---

# Identity Generation

Identity generation should also occur through a Driven Port.

Example.

```mermaid
flowchart TD

N1["IdentityGenerator"]
N2["Generate LibraryID"]

N1 --> N2
```

The Domain requires:

```

Unique Identity
```

It does not require:

- UUID
- ULID
- Snowflake
- Database Sequence

Those are implementation choices.

---

# Storage

Storage technologies should never appear within the Domain.

Poor.

```

Blob Storage
```

Preferred.

```

ArtworkStore
```

The business requires artwork storage.

It does not care whether artwork is stored in:

- Blob Storage
- Filesystem
- Cloud Storage

The Adapter owns that decision.

---

# Ports Should Be Small

Driven Ports should remain narrowly focused.

Good.

```

ArtworkStore
```

Poor.

```

InfrastructureProvider
```

Each Port should represent one business capability.

Nothing more.

---

# Ports Are Stable

Infrastructure changes frequently.

Driven Ports should remain relatively stable.

Changing a Port forces changes throughout:

- Domain
- Adapters
- Tests

Changing an Adapter affects only infrastructure.

Stable Ports protect the Domain from implementation churn.

---

# Error Semantics

Driven Ports should communicate business failures.

Poor.

```

SQL Error
```

Preferred.

```

Media Not Found
```

The Adapter translates infrastructure failures.

The Domain receives business concepts.

This mirrors the repository guidance established in [MEG-003](../meg-003-domain-driven-design/index.md).

---

# Testing

Driven Ports make infrastructure easy to replace.

Example.

```mermaid
flowchart TD

N1["PlaybackRepository"]
N2["InMemoryRepository"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Clock"]
N2["FixedClock"]

N1 --> N2
```

```mermaid
flowchart TD

N1["MetadataProvider"]
N2["FakeProvider"]

N1 --> N2
```

The Domain can now be tested without external dependencies.

---

# Runtime Integration

The Reactive Runtime itself may satisfy Driven Ports.

Example.

```mermaid
flowchart TD

N1["Domain"]
N2["EventPublisher"]
N3["Runtime Adapter"]
N4["Event Bus"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Notice:

The Domain depends only upon the Port.

The Runtime implements it.

[MEG-002](../meg-002-event-driven-runtime/index.md) and MEG-004 therefore complement one another naturally.

---

# Anti-Corruption Layers

Driven Ports frequently terminate at Anti-Corruption Layers.

Example.

```mermaid
flowchart TD

N1["MetadataProvider"]
N2["TMDB Adapter"]
N3["TMDB API"]

N1 --> N2
N2 --> N3
```

Translation occurs entirely inside the Adapter.

The Domain never understands external terminology.

This preserves the purity of the Domain Model established in [MEG-003](../meg-003-domain-driven-design/index.md).

---

# Examples Within Mosaic

Examples of Driven Ports include:

```

LibraryRepository
```

```

PlaybackRepository
```

```

MetadataProvider
```

```

ArtworkStore
```

```

Clock
```

```

IdentityGenerator
```

```

BlobStore
```

Every Port expresses a business dependency.

None expose implementation.

---

# Anti-Patterns

The following practices are prohibited.

## Infrastructure Interfaces

```

TMDBClient
```

```

PostgresRepository
```

inside the Domain.

---

## Framework Dependencies

Ports importing:

- SQL
- HTTP
- Redis
- Docker

---

## Technology Language

Using implementation terminology rather than business terminology.

---

## Generic Infrastructure Ports

```

StorageProvider
```

without business meaning.

---

## Shared Infrastructure Contracts

Allowing infrastructure to define interfaces consumed by the Domain.

The Domain always owns its own contracts.

---

# Mosaic Guidelines

Within Mosaic:

- Driven Ports MUST belong to the Domain.
- Driven Ports MUST express business requirements.
- Driven Ports MUST remain technology independent.
- Infrastructure MUST implement Driven Ports.
- Ports SHOULD remain focused and cohesive.
- External systems MUST be hidden behind Adapters.
- Error semantics SHOULD remain business oriented.
- Driven Ports SHOULD evolve more slowly than infrastructure.

---

# Relationship to MEG

Driving Ports answer:

> **How does the outside world invoke the Domain?**

Driven Ports answer:

> **How does the Domain obtain capabilities from the outside world?**

Together they define every dependency crossing the boundary of the Hexagon.

The next chapter introduces **Adapters**, the infrastructure components that implement these contracts while keeping the Domain completely insulated from technology.

---

# Summary

Driven Ports are the Domain's expression of dependency.

They communicate:

- what the business requires
- not how it is implemented

By ensuring every external dependency passes through a Domain-owned contract, Mosaic protects its most valuable asset:

The business model itself.

Infrastructure remains free to evolve.

The Domain remains free to ignore it.
