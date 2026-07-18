<!--
File: docs/engineering/guides/meg-007-storage-architecture/03-postgresql.md
Document: MEG-007
Status: Draft
-->

# PostgreSQL

> **v2 decision:** PostgreSQL is the single authoritative state store for Mosaic. Logical bounded contexts share the Platform database through scoped repositories; they do not create separate Module databases.

> *PostgreSQL is the permanent memory of the Mosaic platform. If the business cannot afford to lose it, it belongs here.*

---

# Purpose

Not every category of information requires transactional guarantees.

Business state does.

Examples include:

- users
- libraries
- collections
- playback progress
- capability configuration
- permissions
- module configuration

These concepts define the platform itself.

They require:

- durability
- consistency
- transactional integrity
- recoverability

Within Mosaic, PostgreSQL is the authoritative storage engine for transactional Business State.

---

# Philosophy

Within Mosaic:

> **PostgreSQL stores business truth.**

If information cannot be recreated from another source, it should generally live in PostgreSQL.

If information can be regenerated:

It probably belongs elsewhere.

---

# Why PostgreSQL?

PostgreSQL was selected because it provides:

- ACID transactions
- mature indexing
- strong consistency
- reliability
- replication
- backup tooling
- long-term stability

The Runtime depends upon these guarantees when persisting business state.

Analytical workloads, however, are intentionally delegated elsewhere.

---

# Storage Responsibility

PostgreSQL owns:

- business entities
- business relationships
- configuration
- transactional state

It intentionally does **not** own:

- analytics
- binary assets
- artwork
- search indexes
- Runtime state

Its responsibility is intentionally narrow.

---

# Source Of Truth

Within Mosaic:

PostgreSQL is the authoritative source of truth for Business State.

Examples include:

```

User
```

```

Library
```

```

Collection
```

```

Playback Progress
```

```

Capability Configuration
```

Other storage engines may derive information from PostgreSQL.

PostgreSQL remains authoritative.

---

# Business Ownership

Every Capability owns its own business data.

Example.

```mermaid
flowchart TD

N1["Playback"]
N2["Playback Tables"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Metadata"]
N2["Metadata Tables"]

N1 --> N2
```

Capabilities should never directly mutate another capability's business tables.

Cross-capability communication occurs through:

- Runtime Events
- Contracts

Never shared persistence.

This reinforces the ownership model established in [MEG-003](../meg-003-domain-driven-design/index.md).

---

# Repository Boundary

The Domain never interacts directly with PostgreSQL.

Conceptually.

```mermaid
flowchart TD

N1["Aggregate"]
N2["Repository"]
N3["PostgreSQL"]

N1 --> N2
N2 --> N3
```

Repositories translate:

- Aggregates
- Entities
- Value Objects

into relational persistence.

The Domain remains unaware of SQL.

---

# Transactional Consistency

PostgreSQL provides strong transactional guarantees.

Examples include:

```mermaid
flowchart TD

N1["Playback Progress Updated"]
N2["Commit"]
N3["Domain Event Published"]

N1 --> N2
N2 --> N3
```

Business correctness depends upon these guarantees.

The Runtime should never compromise transactional integrity for convenience.

---

# Table Ownership

Every table has exactly one owning capability.

Example.

```

playback_sessions
```

↓

Playback Capability.

```

libraries
```

↓

Library Capability.

```

collections
```

↓

Collection Capability.

Ownership should remain explicit.

No table should become shared infrastructure.

---

# Schema Design

Schemas SHOULD follow capability boundaries.

Example.

```text
playback.*

library.*

metadata.*

users.*
```

The schema should reinforce architectural ownership.

Not merely organisational preference.

---

# Foreign Keys

Foreign keys SHOULD remain inside capability boundaries.

Poor.

```mermaid
flowchart TD

N1["playback"]
N2["metadata"]
N3["foreign key"]

N1 --> N2
N2 --> N3
```

Preferred.

```mermaid
flowchart TD

N1["PlaybackCompleted"]
N2["Runtime Event"]
N3["Metadata Reacts"]

N1 --> N2
N2 --> N3
```

Business relationships should generally be maintained through capability interaction rather than cross-capability relational coupling.

---

# Indexing

Indexes should optimise transactional workloads.

Examples include:

- primary keys
- foreign identifiers
- lookup fields
- uniqueness constraints

Large analytical indexes belong in DuckDB.

Not PostgreSQL.

Each storage engine should optimise for its own workload.

---

# Concurrency

PostgreSQL should support concurrent capability execution safely.

The Runtime may execute many capabilities simultaneously.

Transactional isolation ensures:

- consistency
- correctness
- durability

Capabilities should not implement their own concurrency control.

The database already provides it.

---

# Business Events

Successful transactions frequently produce Domain Events.

Typical flow.

```mermaid
flowchart TD

N1["Aggregate Updated"]
N2["Repository Save"]
N3["Commit"]
N4["Outbox/Event Publication"]
N5["Runtime Event"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

PostgreSQL persists the business state.

The Runtime coordinates event delivery afterwards.

This separation preserves both transactional integrity and Runtime independence.

---

# Configuration Storage

Capability configuration belongs in PostgreSQL.

Examples include:

- provider settings
- feature flags
- user preferences
- module configuration

Configuration should remain durable.

Capabilities consume configuration through the SDK rather than querying PostgreSQL directly.

---

# Identity

Business identities originate in the Domain.

PostgreSQL persists them.

Example.

```

LibraryID
```

↓

```

libraries.id
```

The database stores identity.

It does not create business identity.

Identity ownership remains inside the Domain Model.

---

# Migrations

Schema evolution occurs through managed migrations.

Every schema change should be:

- versioned
- reversible where practical
- reviewed
- observable

Capabilities should evolve their schemas independently wherever possible.

Migration strategy is defined later in this specification.

---

# Backup

Business State MUST be backed up.

Loss of PostgreSQL should not result in permanent business data loss.

Backup requirements include:

- users
- libraries
- playback
- configuration

Derived information should not influence backup strategy.

---

# Performance

PostgreSQL should optimise for:

- transactional writes
- indexed reads
- consistency
- durability

It should not become the platform's analytics engine.

Large aggregations should migrate into DuckDB.

Transactional and analytical workloads should remain separated.

This separation follows the same architectural direction that led to introducing a dedicated analytical database alongside transactional storage in earlier iterations of the project. NullAnimeException_ Master Specification & Roadmap....pdf

---

# Observability

PostgreSQL SHOULD expose:

- transaction latency
- connection pool usage
- slow queries
- lock contention
- migration state

Storage should remain operationally observable.

Operators should understand the health of transactional persistence.

---

# Anti-Patterns

The following practices are prohibited.

## Analytics

Running large analytical scans against transactional tables.

---

## Binary Storage

Storing artwork and media blobs inside PostgreSQL.

---

## Runtime State

Persisting worker state or scheduler state.

---

## Shared Tables

Multiple capabilities modifying the same business tables.

---

## Cross-Capability Foreign Keys

Creating direct relational coupling between independently evolving capabilities.

---

## Business Logic

Embedding business behaviour inside SQL procedures or triggers.

Business behaviour belongs inside the Domain.

---

# Mosaic Guidelines

Within Mosaic:

- PostgreSQL MUST remain the authoritative store for Business State.
- Business ownership MUST determine table ownership.
- Capabilities MUST communicate through contracts or events rather than shared persistence.
- The Domain MUST remain unaware of PostgreSQL.
- Repositories MUST mediate all persistence.
- PostgreSQL SHOULD optimise for transactional workloads.
- Analytical workloads SHOULD remain outside PostgreSQL.
- Business State MUST remain durable and recoverable.

---

# Relationship to MEG

The Storage Taxonomy identified:

> **Business State**

PostgreSQL now becomes the implementation responsible for preserving that information.

The next chapter introduces **DuckDB**, explaining why analytical information deserves its own specialised storage engine and how it complements PostgreSQL without replacing it.

---

# Summary

PostgreSQL is not the platform's database.

It is the platform's **transactional memory**.

Its responsibility is deliberately narrow:

Preserve business truth.

Everything else:

- analytics
- binary assets
- caches
- derived information

belongs elsewhere.

By resisting the temptation to store everything in one database, Mosaic preserves both architectural clarity and long-term scalability.
