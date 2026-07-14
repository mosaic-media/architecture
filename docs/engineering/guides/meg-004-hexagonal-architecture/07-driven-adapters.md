<!--
File: docs/engineering/guides/meg-004-hexagonal-architecture/07-driven-adapters.md
Document: MEG-004
Status: Draft
Version: 0.1
-->

# Driven Adapters

> *Driven Adapters fulfil the Domain's requests by translating business intent into infrastructure operations.*

---

# Purpose

The Domain frequently requires capabilities that only infrastructure can provide.

Examples include:

- persisting Aggregates
- retrieving metadata
- storing artwork
- publishing runtime events
- generating identifiers
- obtaining the current time

The Domain expresses these requirements through Driven Ports.

Driven Adapters satisfy those requirements by implementing the corresponding Port using specific infrastructure technologies.

They form the boundary between the Domain and the external world.

---

# Philosophy

Within Mosaic:

> **Driven Adapters implement capabilities. They never define them.**

The Domain owns the contract.

The Driven Adapter owns the implementation.

This distinction allows infrastructure to evolve without requiring changes to the Domain Model.

---

# What Is A Driven Adapter?

A Driven Adapter is an infrastructure implementation of a Driven Port.

Conceptually.

```
Domain

↓

Driven Port

↓

Driven Adapter

↓

Technology
```

The Domain depends only upon the Port.

The Adapter depends upon the technology.

---

# Why Driven Adapters Exist

Without Driven Adapters:

```
Domain

↓

SQL

↓

Database
```

Business behaviour becomes tightly coupled to persistence.

Instead.

```
Domain

↓

PlaybackRepository

↓

PostgreSQL Adapter

↓

Database
```

Only the Adapter understands SQL.

The Domain remains completely independent.

---

# One Port

Every Driven Adapter implements one or more Driven Ports.

Example.

```
MetadataProvider

↓

TMDB Adapter
```

Later.

```
MetadataProvider

↓

AniList Adapter
```

The Domain remains unchanged.

Only the Adapter changes.

---

# Infrastructure Ownership

Driven Adapters own every technology-specific concern.

Examples include:

- SQL
- HTTP clients
- SDKs
- authentication tokens
- connection pools
- file systems
- blob storage
- serialization

None of these concepts belong inside the Domain.

---

# Repository Adapters

Repository implementations are Driven Adapters.

Example.

```
PlaybackRepository

↓

PostgreSQL Adapter
```

Responsibilities include:

- SQL generation
- transaction management
- persistence mapping
- Aggregate reconstruction

Business behaviour remains inside the Aggregate.

Persistence behaviour remains inside the Adapter.

---

# External Service Adapters

External services should always terminate at a Driven Adapter.

Example.

```
MetadataProvider

↓

TMDB Adapter

↓

TMDB API
```

The Adapter performs:

- authentication
- request construction
- retries (where appropriate)
- response mapping
- error translation

The Domain receives only business concepts.

---

# Runtime Adapters

The Reactive Runtime is also infrastructure.

Example.

```
Domain Event

↓

RuntimeEventPublisher

↓

Runtime Adapter

↓

Event Bus
```

The Domain remains unaware of:

- workers
- queues
- subscribers
- delivery guarantees

Those concepts belong entirely to the runtime.

---

# Translation

Driven Adapters translate:

```
Business Request

↓

Infrastructure Request
```

and later:

```
Infrastructure Response

↓

Business Result
```

Translation occurs entirely within the Adapter.

Neither the Domain nor the infrastructure should understand one another's models directly.

---

# Mapping

Driven Adapters frequently perform mapping.

Examples include:

```
Aggregate

↓

Database Row
```

```
Database Row

↓

Aggregate
```

```
TMDB Response

↓

Metadata Value Object
```

Mapping should remain symmetrical wherever practical.

Business models should never become persistence models.

---

# Error Translation

Infrastructure errors should never escape the Adapter.

Poor.

```
SQL Error

↓

Domain
```

Preferred.

```
SQL Error

↓

Adapter

↓

MediaNotFound
```

Likewise.

```
HTTP Timeout

↓

Adapter

↓

MetadataUnavailable
```

The Domain should reason about business failures.

Never infrastructure failures.

---

# Configuration

Configuration belongs to infrastructure.

Example.

```
TMDB API Key

↓

Adapter
```

The Domain should never receive:

- API keys
- connection strings
- endpoint URLs

Configuration remains an implementation concern.

---

# Retry Behaviour

Driven Adapters may implement infrastructure retries when interacting with unreliable external systems.

Examples include:

- TMDB
- AniList
- Blob Storage

These retries differ from runtime event retries defined in MEG-002.

Infrastructure retries protect one operation.

Runtime retries protect business workflows.

The two should remain distinct.

---

# Resource Ownership

Driven Adapters own infrastructure resources.

Examples include:

- database connections
- HTTP clients
- blob clients
- caches
- SDK instances

The Domain should never manage resource lifecycles.

Construction and disposal belong to infrastructure.

---

# Composition Root

Driven Adapters are constructed within the Composition Root.

Example.

```
main()

↓

Create PostgreSQL

↓

Create Repository Adapter

↓

Inject Port

↓

Domain
```

The Domain should never instantiate its own Adapters.

---

# Testing

Driven Adapters should be tested independently from the Domain.

Typical tests verify:

- SQL mapping
- HTTP translation
- serialization
- authentication
- protocol compatibility

Domain tests should replace Adapters with simple test implementations.

This separation keeps business tests fast while still validating infrastructure behaviour.

---

# Technology Replacement

Replacing infrastructure should require replacing only the Adapter.

Example.

```
PostgreSQL

↓

CockroachDB
```

or

```
TMDB

↓

AniList
```

The Port remains unchanged.

The Domain remains unchanged.

Only the Adapter evolves.

This is one of the primary reasons Hexagonal Architecture scales well over time.

---

# Multiple Adapters

One Port may have multiple implementations simultaneously.

Example.

```
ArtworkStore

├── Local Filesystem

├── Blob Storage

├── Memory

└── Test
```

Selecting the implementation becomes a Composition Root decision.

Not a Domain decision.

---

# Anti-Corruption Layers

Every integration with an external system SHOULD terminate inside a Driven Adapter.

Example.

```
Jellyfin

↓

Jellyfin Adapter

↓

LibraryRepository
```

The Adapter translates:

- terminology
- identifiers
- lifecycle
- business concepts

External models should never leak into the Domain.

---

# Examples Within Mosaic

Examples of Driven Adapters include:

```
PostgreSQL Playback Repository
```

```
DuckDB Analytics Repository
```

```
TMDB Metadata Provider
```

```
AniList Metadata Provider
```

```
Blob Artwork Store
```

```
Filesystem Artwork Store
```

```
Runtime Event Publisher
```

Every Adapter owns implementation.

None own business behaviour.

---

# Anti-Patterns

The following practices are prohibited.

## Business Logic

Calculating recommendations inside a repository.

---

## Domain Models Leaking Out

Returning SQL rows directly to the Domain.

---

## Infrastructure Models Leaking In

Passing SDK objects into Aggregates.

---

## Shared Adapters

One Adapter implementing unrelated Ports.

---

## Framework Dependencies

Importing:

- HTTP
- SQL
- Docker

into Domain objects.

---

## Repository As Service

Repositories making business decisions rather than simply persisting Aggregates.

---

# Mosaic Guidelines

Within Mosaic:

- Driven Adapters MUST implement Driven Ports.
- Driven Adapters MUST own technology-specific code.
- Driven Adapters MUST translate infrastructure models into business models.
- Infrastructure errors MUST be translated into business concepts.
- Configuration MUST remain inside infrastructure.
- Domain objects MUST remain infrastructure independent.
- Driven Adapters SHOULD remain independently replaceable.
- Infrastructure changes SHOULD affect only Driven Adapters.

---

# Relationship to MEG

Driving Adapters bring business requests into the Domain.

Driven Adapters fulfil the Domain's external requirements.

Together they complete the Hexagonal Architecture.

```
External System

↓

Driving Adapter

↓

Driving Port

↓

Application

↓

Domain

↓

Driven Port

↓

Driven Adapter

↓

Infrastructure
```

Every dependency crossing the architectural boundary now passes through an explicit Port and Adapter.

Nothing crosses the boundary accidentally.

---

# Summary

Driven Adapters are where technology finally appears.

They isolate:

- databases
- APIs
- storage
- runtimes
- external services

from the Domain by translating business concepts into infrastructure operations and back again.

Within Mosaic, replacing an infrastructure technology should almost always mean replacing only a Driven Adapter.

If changing a database requires changing an Aggregate, the architectural boundary has been violated.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`06-driving-adapters.md`

**Next File**

`08-dependency-direction.md`
