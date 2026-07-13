<!--
File: engineering/meg/MEG-003 Domain-Driven Design/12-repositories.md
Document: MEG-003
Status: Draft
Version: 0.1
-->

# Repositories

> *A Repository gives the illusion that Aggregates simply exist. It hides persistence so the domain can remain focused on the business.*

---

# Purpose

Business logic should never concern itself with:

- SQL
- PostgreSQL
- DuckDB
- Blob Storage
- Redis
- Filesystems

The domain should ask only one question:

> **"Can I obtain this Aggregate?"**

Repositories answer that question.

They provide a collection-like abstraction over persistent storage while insulating the Domain Model from infrastructure concerns.

---

# Philosophy

Within Mosaic:

> **Repositories exist to persist Aggregates, not data.**

This distinction is fundamental.

Repositories do not manage:

- rows
- tables
- documents
- files

They manage:

- Aggregate Roots

Everything else is an implementation detail.

This reflects the classic DDD Repository pattern, whose purpose is to isolate the domain model from persistence concerns while presenting aggregates as though they were held in an in-memory collection.  [oai_citation:0‡O'Reilly Media](https://www.oreilly.com/library/view/implementing-domain-driven-design/9780133039900/ch12.html?utm_source=chatgpt.com)

---

# What Is A Repository?

A Repository provides the illusion that Aggregates are stored within an in-memory collection.

Conceptually.

```
Playback Repository

↓

Load Playback Session

↓

Modify Aggregate

↓

Save Aggregate
```

How that Aggregate is stored is irrelevant to the domain.

---

# Why Repositories Exist

Without Repositories:

```
Playback

↓

SQL

↓

Database

↓

Rows

↓

Business Logic
```

The business now understands infrastructure.

Instead:

```
Playback

↓

Repository

↓

Persistence
```

The Aggregate remains infrastructure agnostic.

---

# Repository Responsibilities

Repositories are responsible for:

- loading Aggregates
- saving Aggregates
- removing Aggregates
- querying Aggregate identity

Repositories are **not** responsible for:

- business rules
- validation
- orchestration
- transactions
- event publication

Business belongs to the domain.

Persistence belongs to infrastructure.

---

# One Repository Per Aggregate

Every Aggregate Root SHOULD have one Repository.

Example.

```
Playback Aggregate

↓

PlaybackRepository
```

```
Library Aggregate

↓

LibraryRepository
```

Not:

```
PlaybackPositionRepository
```

```
WatchProgressRepository
```

Repositories persist Aggregate boundaries.

Not implementation details.

This one-repository-per-aggregate-root approach is one of the core recommendations of DDD because repositories preserve aggregate consistency boundaries.  [oai_citation:1‡Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design?utm_source=chatgpt.com)

---

# Aggregate Roots Only

Repositories should load and save Aggregate Roots.

Poor.

```
PlaybackProgress

↓

Repository
```

Preferred.

```
PlaybackSession

↓

Repository
```

Internal Entities remain internal.

The Aggregate Root protects consistency.

---

# Collection Semantics

Repositories should feel like collections.

Examples.

```
Find()

Save()

Delete()

Exists()
```

They should not expose database operations.

Poor.

```
ExecuteSQL()
```

```
RunQuery()
```

```
UpdateRow()
```

These reveal persistence.

Not business behaviour.

---

# Domain Language

Repository APIs should speak the ubiquitous language.

Good.

```go
libraryRepository.FindByID(...)
```

```go
playbackRepository.Save(...)
```

Poor.

```go
database.Select(...)
```

```go
repository.Execute(...)
```

Names should communicate business intent.

---

# Repository Interfaces

Repository interfaces belong to the domain.

Implementations belong to infrastructure.

Example.

```
Domain

↓

PlaybackRepository Interface
```

```
Infrastructure

↓

PostgresPlaybackRepository
```

The Domain knows nothing about PostgreSQL.

Infrastructure knows everything.

This separation preserves persistence ignorance while allowing different infrastructure implementations.  [oai_citation:2‡Stack and System](https://stackandsystem.com/series/domain-driven-design/9-repositories-in-domain-driven-design?utm_source=chatgpt.com)

---

# Persistence Ignorance

Aggregates should remain completely unaware of persistence.

Poor.

```go
playback.Save()
```

Preferred.

```go
repository.Save(playback)
```

Persistence should always occur outside the Aggregate.

The domain models business.

Infrastructure models storage.

---

# Transactions

Repositories participate in transactions.

They do not own them.

Typical flow.

```
Load Aggregate

↓

Business Behaviour

↓

Save Aggregate
```

The Repository persists the Aggregate.

The Aggregate determines what changed.

---

# Queries

Repositories exist primarily for write models.

Complex reporting queries often belong elsewhere.

Example.

```
PlaybackRepository

↓

Playback Aggregate
```

versus.

```
Continue Watching View

↓

Read Model
```

Repositories should not become reporting engines.

This aligns naturally with CQRS where rich queries are separated from aggregate persistence.

---

# Avoid Generic Repositories

Poor.

```go
type Repository[T any]
```

While technically elegant, generic repositories frequently describe persistence rather than business behaviour.

Instead.

```
PlaybackRepository
```

```
LibraryRepository
```

```
CollectionRepository
```

Business language should always dominate technical abstraction.

---

# Repository Methods

Repositories SHOULD expose intention-revealing operations.

Examples.

```go
FindByID()
```

```go
FindBySource()
```

```go
Exists()
```

Avoid exposing generic database operations.

Repositories should describe business retrieval.

Not storage mechanics.

---

# Repository Scope

Repositories should remain small.

Poor.

```
PlaybackRepository

↓

Save

Find

Export

Metrics

Analytics

Search

Cache

Notifications
```

Better.

```
PlaybackRepository

↓

Load

Save

Delete
```

Business behaviour belongs elsewhere.

---

# Repositories Do Not Orchestrate

Poor.

```
Repository

↓

Load

↓

Modify Aggregate

↓

Publish Events

↓

Call API
```

Repositories should simply persist Aggregates.

Everything else belongs to:

- Aggregates
- Domain Services
- Application Services
- Runtime

---

# Multiple Storage Engines

One of Mosaic's defining architectural characteristics is multiple storage technologies.

Examples include:

- PostgreSQL
- DuckDB
- Blob Storage
- Filesystem
- MOS Files

The Domain should remain unaware of all of them.

Every implementation should satisfy the same Repository contract.

Changing persistence should never require changing business behaviour.

---

# Repository Lifetime

Repositories should remain lightweight.

They should not:

- cache business state
- maintain sessions
- own transactions
- retain Aggregate instances

Every call should remain explicit.

Repositories are gateways.

Not application state.

---

# Testing

Repositories should be replaceable during testing.

Example.

```
PlaybackRepository

↓

In-Memory Repository
```

Business tests should not require:

- PostgreSQL
- DuckDB
- Blob Storage

The domain should remain testable independently of infrastructure.

---

# Anti-Patterns

The following practices are prohibited.

## Generic Repository

```
Repository<T>
```

used for every Aggregate.

---

## Repository Per Entity

Repositories for child Entities.

---

## SQL In The Domain

```
SELECT ...
```

appearing within business logic.

---

## Business Logic In Repositories

Repositories deciding business behaviour.

---

## Returning Persistence Models

Repositories returning database rows rather than Aggregates.

---

## Cross-Aggregate Repositories

One Repository managing multiple unrelated Aggregate Roots.

---

# Mosaic Guidelines

Within Mosaic:

- Every Aggregate Root SHOULD have one Repository.
- Repositories MUST persist Aggregate Roots.
- Repository interfaces SHOULD belong to the Domain.
- Repository implementations MUST belong to Infrastructure.
- Repositories MUST speak the ubiquitous language.
- Repositories MUST remain persistence focused.
- Business behaviour MUST remain outside Repositories.
- The Domain MUST remain unaware of storage technologies.

---

# Relationship to MEG

Aggregates own consistency.

Aggregate Roots protect consistency.

Repositories preserve consistency.

The next chapter introduces **Factories**, which solve the complementary problem of constructing complex Aggregates in valid business states before they are ever persisted.

---

# Summary

Repositories are one of the most misunderstood patterns in Domain-Driven Design.

They are not database wrappers.

They are not DAOs.

They are not query builders.

Within Mosaic, they exist for one purpose:

> **Provide the domain with the illusion that Aggregates simply exist, while keeping every persistence concern outside the business model.**

When implemented correctly, changing PostgreSQL to another storage engine should require changes only within infrastructure.

The business should never notice.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`11-domain-events.md`

**Next File**

`13-factories.md`
