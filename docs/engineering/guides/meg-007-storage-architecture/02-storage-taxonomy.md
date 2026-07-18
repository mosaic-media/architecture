<!--
File: docs/engineering/guides/meg-007-storage-architecture/02-storage-taxonomy.md
Document: MEG-007
Status: Draft
-->

# Storage Taxonomy

> *Not all information is equal. Before choosing storage, the platform must first understand what kind of information it is preserving.*

---

# Purpose

The previous chapter established the philosophy that:

> **Information determines storage.**

This chapter formalises that philosophy.

Before assigning a storage engine, every piece of information within Mosaic is classified according to its:

- ownership
- lifecycle
- consistency requirements
- access patterns
- recoverability

This classification forms the **Storage Taxonomy**.

Every subsequent storage decision derives from this taxonomy.

---

# Philosophy

Within Mosaic:

> **Every category of information belongs to exactly one storage class.**

Storage classes exist independently of storage technologies.

The Runtime first determines:

> **What kind of information is this?**

Only afterwards does it determine:

> **Where should it live?**

---

# Storage Classes

Every piece of information belongs to one of the following categories.

```mermaid
flowchart TD

N1["Business State"]
N2["Operational State"]
N3["Analytical State"]
N4["Binary Assets"]
N5["Derived Assets"]
N6["Archive Data"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Each category possesses distinct architectural characteristics.

---

# Business State

Business State represents information that defines the platform itself.

Examples include:

- users
- libraries
- collections
- playback progress
- capability configuration
- module configuration

Business State is:

- authoritative
- transactional
- durable
- recoverable

Loss of Business State represents permanent information loss.

---

# Operational State

Operational State exists only to support Runtime execution.

Examples include:

- worker allocation
- scheduler state
- queue depth
- execution state
- capability lifecycle
- runtime health

Operational State is:

- temporary
- reconstructable
- runtime owned

Most Operational State should disappear safely when the Runtime stops.

---

# Analytical State

Analytical State exists to support:

- reporting
- recommendations
- aggregation
- optimisation
- search

Examples include:

- viewing history analysis
- popularity metrics
- recommendation vectors
- media statistics
- usage trends

Analytical State is generally:

- append oriented
- scan heavy
- reproducible

Analytical workloads should remain logically separate from transactional workloads. That separation is a property of the analytical processing port, not of a specific engine: the state store satisfies it today, and a dedicated engine may satisfy it later without changing the taxonomy. See [15 — v2 Storage Architecture](15-v2-storage-architecture.md).

---

# Binary Assets

Binary Assets represent large opaque objects.

Examples include:

- artwork
- posters
- banners
- subtitles
- generated thumbnails
- screenshots

Binary Assets differ fundamentally from structured information.

They optimise for:

- retrieval
- streaming
- caching

rather than relational querying.

---

# Derived Assets

Derived Assets are reproducible outputs.

Examples include:

- artwork caches
- search indexes
- metadata caches
- preview images
- recommendation caches

Derived Assets should generally satisfy one principle.

```mermaid
flowchart TD

N1["Delete"]
N2["Rebuild"]

N1 --> N2
```

If regeneration is possible, permanent durability becomes less important.

---

# Archive Data

Archive Data represents long-lived portable information.

Examples include:

- MOS archives
- exported libraries
- capability packages
- backups

Archive Data should prioritise:

- portability
- compatibility
- integrity

rather than runtime performance.

---

# Storage Characteristics

Every category possesses characteristic behaviour.

| Storage Class | Authoritative | Durable | Rebuildable |
|----------------|--------------|----------|-------------|
| Business State | Yes | Yes | No |
| Operational State | No | Usually No | Yes |
| Analytical State | Usually No | Optional | Usually Yes |
| Binary Assets | Yes | Yes | Sometimes |
| Derived Assets | No | Optional | Yes |
| Archive Data | Yes | Yes | No |

This classification should remain stable regardless of storage technology.

---

# Ownership

Every storage category has exactly one owner.

Examples.

```mermaid
flowchart TD

N1["Business State"]
N2["Capabilities"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Operational State"]
N2["Runtime"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Analytical State"]
N2["Analytics Capability"]

N1 --> N2
```

Ownership determines:

- mutation
- persistence
- recovery
- lifecycle

Shared ownership should be avoided.

---

# Consistency

Different storage classes require different consistency guarantees.

Business State.

```

Strong Consistency
```

Operational State.

```

Eventually Disposable
```

Derived Assets.

```

Rebuildable
```

Consistency should follow information requirements.

Not database capabilities.

---

# Lifetime

Storage categories differ dramatically in lifespan.

Operational.

```mermaid
flowchart TD

N1["Milliseconds"]
N2["Minutes"]

N1 --> N2
```

Business.

```

Years
```

Archives.

```

Potentially Forever
```

Storage technology should reflect expected lifetime.

---

# Access Patterns

Every storage class has different access characteristics.

Business State.

- frequent reads
- transactional writes

Operational State.

- constant mutation
- short lifetime

Analytical State.

- sequential scans
- aggregations

Binary Assets.

- streaming
- large reads

Derived Assets.

- cache lookups
- rebuilds

Storage architecture should optimise for these access patterns.

---

# Mutation

Different categories mutate differently.

Business State.

```

Continuous Updates
```

Operational State.

```

Constant Change
```

Archive Data.

```

Almost Never
```

Mutation characteristics should influence storage design.

---

# Recovery

Recovery differs by storage class.

Business State.

```

Restore Backup
```

Derived Assets.

```

Rebuild
```

Operational State.

```

Restart Runtime
```

The platform should avoid restoring information that is cheaper to regenerate.

---

# Replication

Only authoritative information generally requires replication.

Examples include:

- Business State
- Archive Data

Derived Assets typically do not.

Replication should follow business value.

Not storage implementation.

---

# Search

Search indexes belong to:

```

Derived Assets
```

Not:

```

Business State
```

Search should remain rebuildable.

The authoritative business information remains elsewhere.

---

# Caching

Caches are always:

```

Derived Assets
```

Caches should never become authoritative.

If cache loss damages business correctness:

The cache is storing the wrong information.

---

# Storage Independence

Storage categories should remain independent of implementation.

Example.

```mermaid
flowchart TD

N1["Business State"]
N2["PostgreSQL"]

N1 --> N2
```

Later.

```mermaid
flowchart TD

N1["Business State"]
N2["Alternative Database"]

N1 --> N2
```

The taxonomy remains unchanged.

Only implementation evolves.

---

# Capability Mapping

Capabilities own Business State.

Runtime owns Operational State.

Analytics owns Analytical State.

Blob Storage owns Binary Assets.

MOS archives own Archive Data.

Every category therefore has:

- one owner
- one architectural purpose

Technology simply implements that purpose.

---

# Anti-Patterns

The following practices are prohibited.

## Business State In Cache

Treating cached information as authoritative.

---

## Shared Ownership

Multiple storage systems acting as sources of truth.

---

## Analytics In Transactional Storage

Large analytical workloads degrading business transactions.

---

## Operational State Persistence

Persisting temporary Runtime state unnecessarily.

---

## Binary Objects In Relational Storage

Using transactional databases for large binary assets.

---

## Mixed Storage Classes

One storage engine becoming responsible for unrelated storage categories without architectural justification.

---

# Mosaic Guidelines

Within Mosaic:

- Every piece of information MUST belong to one storage class.
- Business State MUST remain authoritative.
- Operational State SHOULD remain ephemeral.
- Derived Assets SHOULD remain reproducible.
- Archive Data MUST remain portable.
- Storage ownership MUST remain explicit.
- Access patterns SHOULD influence storage selection.
- Storage taxonomy MUST remain independent of implementation technologies.

---

# Relationship to MEG

The Storage Philosophy established:

> **Why storage should follow information.**

The Storage Taxonomy now defines:

> **Which categories of information exist.**

The next chapter introduces **PostgreSQL**, defining why it is the authoritative store for transactional Business State and how it fits into the wider Storage Architecture.

---

# Summary

The Storage Taxonomy is the foundation of every persistence decision within Mosaic.

Before choosing:

- PostgreSQL
- an analytical processing engine
- Blob Storage
- MOS

the platform first asks:

> **What kind of information is this?**

That simple question prevents storage technologies from becoming architectural decisions.

Instead, architecture remains driven by information itself.
