<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/02-ports.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# Ports

> *A Port defines what the Domain needs. It never defines how that need is fulfilled.*

---

# Purpose

The Domain must interact with the outside world.

Examples include:

- loading Aggregates
- publishing Domain Events
- reading metadata
- writing blob storage
- retrieving configuration
- querying external providers

However, the Domain should remain completely unaware of:

- PostgreSQL
- DuckDB
- TMDB
- Jellyfin
- Docker
- HTTP
- Filesystems

Ports solve this problem.

They define the contracts through which the Domain communicates with external systems without depending upon those systems.

---

# Philosophy

Within Mosaic:

> **The Domain owns every contract it depends upon.**

A Port represents a business capability.

It does **not** represent a technology.

Infrastructure implements Ports.

The Domain defines them.

This inversion of ownership is the defining characteristic of Hexagonal Architecture.

---

# What Is A Port?

A Port is an interface representing a business capability required by the Domain.

Examples include:

```
MediaRepository
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

Each Port answers one question.

> **What does the Domain require?**

Not:

> **How is it implemented?**

---

# Why Ports Exist

Without Ports:

```
Playback

↓

PostgreSQL

↓

SQL

↓

Database
```

The Domain now understands infrastructure.

Instead:

```
Playback

↓

PlaybackRepository

↓

PostgreSQL Adapter
```

The Domain understands only:

```
PlaybackRepository
```

Everything else becomes replaceable.

---

# The Domain Owns The Port

One of the most important principles of Hexagonal Architecture is:

```
Domain

↓

Defines Interface

↓

Infrastructure Implements
```

Not:

```
Infrastructure

↓

Defines Interface

↓

Domain Uses
```

Ownership always belongs to the Domain.

The business decides what it needs.

Infrastructure satisfies those needs.

---

# Ports Describe Behaviour

Ports should describe business behaviour.

Good.

```go
type PlaybackRepository interface {

    FindByID(...)

    Save(...)
}
```

Poor.

```go
type PostgreSQLRepository interface {

    ExecuteSQL(...)
}
```

The first describes business intent.

The second describes implementation.

Ports should never leak technology.

---

# Business Language

Port names should reinforce the ubiquitous language.

Good.

```
CollectionRepository
```

```
MetadataProvider
```

```
RecommendationEngine
```

Poor.

```
DatabaseAccess
```

```
StorageLayer
```

```
PersistenceManager
```

Business concepts should always dominate technical vocabulary.

---

# Ports Are Stable

Infrastructure changes frequently.

Ports should not.

Changing a Port affects:

- the Domain
- every Adapter
- every test
- every implementation

Ports therefore form part of the long-term architectural contract.

They should evolve deliberately.

---

# Ports Are Small

Ports SHOULD remain focused.

Good.

```go
type ArtworkProvider interface {

    Artwork(...)
}
```

Poor.

```go
type MediaPlatform interface {

    Import()

    Search()

    Playback()

    Metadata()

    Recommendations()

    Authentication()
}
```

Large Ports increase coupling.

Small Ports improve flexibility.

This aligns closely with Go's preference for small interfaces representing behaviour rather than broad capability sets. ([go.dev](https://go.dev/doc/effective_go?utm_source=chatgpt.com))

---

# Business First

A useful question when designing a Port is:

> **What would the business ask for?**

Not:

> **What can PostgreSQL provide?**

The Domain should remain entirely unaware of implementation constraints.

---

# Technology Neutral

Ports should never reference:

- SQL
- REST
- HTTP
- Kafka
- NATS
- Docker
- Redis

Poor.

```
SQLRepository
```

Good.

```
MediaRepository
```

Technology belongs behind the Port.

---

# Ports Are Intent

Ports communicate intent.

Example.

```
MetadataProvider
```

communicates:

> Retrieve metadata.

It says nothing about:

- TMDB
- AniList
- Local Cache
- Filesystem

Those become Adapter concerns.

---

# One Responsibility

Each Port SHOULD describe one responsibility.

Examples.

```
MetadataProvider
```

```
ArtworkStore
```

```
Clock
```

Avoid combining unrelated concepts.

Poor.

```
MediaInfrastructure
```

One Port should answer one business question.

---

# Domain Dependencies

Everything the Domain depends upon should enter through Ports.

Examples include:

- repositories
- providers
- storage
- time
- identity generation

This dramatically improves:

- testing
- replacement
- evolution

The Domain remains isolated.

---

# Input vs Output

Not all Ports are identical.

Some receive requests.

Others perform work on behalf of the Domain.

Hexagonal Architecture traditionally distinguishes these as:

- Driving Ports
- Driven Ports

The next two chapters explore this distinction.

---

# Ports Are Not Adapters

A common mistake is confusing:

```
Port
```

with

```
Adapter
```

Ports define contracts.

Adapters implement contracts.

The Port belongs to the Domain.

The Adapter belongs to Infrastructure.

The two should never be combined.

---

# Testing

Ports make testing straightforward.

Example.

```
PlaybackRepository

↓

Fake Repository
```

The Domain remains unaware that no real database exists.

Tests become:

- deterministic
- fast
- infrastructure independent

This is one of the primary practical benefits of Hexagonal Architecture.

---

# Port Evolution

Ports should evolve slowly.

Whenever a Port changes ask:

- Is the Domain changing?
- Or merely the infrastructure?

If only infrastructure changed:

The Port probably should not.

Ports should remain stable as technologies evolve.

---

# Mosaic Examples

Examples of Ports within Mosaic include:

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
BlobStore
```

```
IdentityGenerator
```

```
Clock
```

Every Port expresses a business dependency.

None express technology.

---

# Anti-Patterns

The following practices are prohibited.

## Technology Ports

```
PostgresRepository
```

```
RedisProvider
```

---

## Generic Ports

```
Storage
```

without business meaning.

---

## Large Ports

Interfaces representing unrelated capabilities.

---

## Infrastructure Dependencies

Ports importing:

- SQL
- HTTP
- Runtime
- Logging

---

## Shared Ownership

Infrastructure defining contracts consumed by the Domain.

The Domain owns the contract.

Always.

---

# Mosaic Guidelines

Within Mosaic:

- Ports MUST belong to the Domain.
- Ports MUST describe business behaviour.
- Ports MUST remain technology independent.
- Ports SHOULD remain small.
- Ports SHOULD reinforce the ubiquitous language.
- Infrastructure MUST implement Ports.
- Ports SHOULD evolve slowly.
- Business requirements MUST drive Port design.

---

# Relationship to MEG

Hexagonal Architecture revolves around one simple idea.

```
Domain

↓

Port

↓

Adapter

↓

Technology
```

Ports define the contracts.

Adapters satisfy them.

The next chapter introduces the first category of Ports:

**Driving Ports**, which define how the outside world requests business behaviour from the Domain.

---

# Summary

Ports are one of the most important concepts within Hexagonal Architecture.

They invert the traditional ownership of dependencies.

Instead of infrastructure telling the Domain how to behave:

The Domain tells infrastructure what it requires.

That inversion protects the business from technology and ensures the Domain remains the most stable part of the Mosaic platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`01-hexagonal-philosophy.md`

**Next File**

`03-driving-ports.md`
