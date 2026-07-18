<!--
File: docs/engineering/guides/meg-007-storage-architecture/09-storage-lifecycle.md
Document: MEG-007
Status: Draft
-->

# Storage Lifecycle

> *Information changes throughout its lifetime. Storage should evolve with it rather than treating every piece of data as permanent.*

---

# Purpose

Information within Mosaic is not static.

Media is:

- discovered
- imported
- enriched
- consumed
- archived
- eventually removed

During that lifecycle, information naturally moves between storage systems.

Examples include:

- PostgreSQL
- DuckDB
- Blob Storage
- MOS Cache
- MOS Archives

The Storage Lifecycle defines how information flows between these systems while preserving:

- ownership
- consistency
- recoverability

---

# Philosophy

Within Mosaic:

> **Information should move because its lifecycle changes, not because its storage technology changes.**

Every storage transition should represent a meaningful change in the information itself.

Storage should follow information.

Never dictate it.

---

# Information Lifecycle

Every piece of information progresses through a common lifecycle.

```mermaid
flowchart TD

N1["Discovered"]
N2["Imported"]
N3["Enriched"]
N4["Active"]
N5["Referenced"]
N6["Archived"]
N7["Deleted"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Different storage systems participate at different stages.

---

# Discovery

Initially.

```mermaid
flowchart TD

N1["External Source"]
N2["Metadata"]
N3["Capability"]

N1 --> N2
N2 --> N3
```

At this stage:

Information may exist only:

- remotely
- temporarily
- in memory

No permanent persistence has yet occurred.

---

# Import

Import creates Business State.

Typical flow.

```mermaid
flowchart TD

N1["Media Source"]
N2["Repository"]
N3["PostgreSQL"]

N1 --> N2
N2 --> N3
```

Business information now becomes durable.

Import should establish:

- ownership
- identity
- relationships

Everything afterwards builds upon this foundation.

---

# Enrichment

Following import:

Additional information may be collected.

Examples include:

- metadata
- artwork
- provider mappings
- recommendations

Typical flow.

```mermaid
flowchart TD

N1["PostgreSQL"]
N2["Metadata Capability"]
N3["DuckDB"]
N4["Blob Storage"]
N5["MOS Cache"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Business State remains authoritative.

Enrichment produces supporting information.

---

# Active State

During normal operation:

Information exists simultaneously across multiple storage systems.

Example.

```mermaid
flowchart TD

N1["PostgreSQL"]
N2["Business Truth"]

N1 --> N2
```

```mermaid
flowchart TD

N1["DuckDB"]
N2["Analytics"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Blob Storage"]
N2["Artwork"]

N1 --> N2
```

```mermaid
flowchart TD

N1["MOS Cache"]
N2["Resolved Metadata"]

N1 --> N2
```

Every storage system owns its own responsibility.

No duplication of authority occurs.

---

# Runtime Consumption

Capabilities consume information through repositories.

Typical flow.

```mermaid
flowchart TD

N1["Capability"]
N2["Repository"]
N3["PostgreSQL"]
N4["Blob Storage"]
N5["MOS Cache"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Storage remains invisible.

Capabilities consume business concepts.

Not storage technologies.

---

# Derived Information

Derived information appears after business information exists.

Examples include:

- search indexes
- recommendation vectors
- artwork manifests
- provider mappings

These datasets are created.

Never authored.

Their lifecycle depends entirely upon the authoritative information from which they originate.

---

# Cache Lifecycle

Cache follows its own lifecycle.

```mermaid
flowchart TD

N1["Generate"]
N2["Use"]
N3["Invalidate"]
N4["Delete"]
N5["Regenerate"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Notice:

Deletion is expected.

Business correctness should never depend upon cache persistence.

---

# Binary Lifecycle

Binary assets follow a distinct lifecycle.

```mermaid
flowchart TD

N1["Download"]
N2["Blob Storage"]
N3["Reference"]
N4["Cache"]
N5["Archive"]
N6["Delete"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Binary assets remain independent of:

- Runtime execution
- analytical processing

They simply become referenced resources.

---

# Analytical Lifecycle

Analytical information progresses differently.

```mermaid
flowchart TD

N1["Business Events"]
N2["DuckDB"]
N3["Aggregation"]
N4["Reports"]
N5["Recommendation Inputs"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Analytics evolve continuously.

They should never become authoritative.

---

# Archive Lifecycle

MOS Archives exist for long-term portability.

Typical lifecycle.

```mermaid
flowchart TD

N1["Business State"]
N2["Export"]
N3["MOS Archive"]
N4["Transport"]
N5["Import"]
N6["Business State"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The archive remains independent of:

- Runtime
- deployment
- storage implementation

Its purpose is preservation.

---

# Deletion

Deletion should follow ownership.

Examples.

Business entity deleted.

↓

Blob references removed.

↓

Derived caches invalidated.

↓

Analytical datasets rebuilt.

↓

Unused blobs collected.

Deletion should proceed from:

Authoritative.

↓

Derived.

Never the reverse.

---

# Garbage Collection

Derived information SHOULD be collected automatically.

Examples include:

- orphaned blobs
- expired caches
- obsolete search indexes
- unused previews

Business information should never be removed by garbage collection.

Only information that is safely reproducible.

---

# Migration

Storage migration should preserve lifecycle.

Example.

```mermaid
flowchart TD

N1["PostgreSQL"]
N2["New Version"]

N1 --> N2
```

Business State survives.

Likewise.

```mermaid
flowchart TD

N1["Blob Storage"]
N2["New Provider"]

N1 --> N2
```

Blob identity remains unchanged.

Lifecycle remains stable.

Implementation evolves.

---

# Backup

Backup priorities follow storage classes.

Highest priority.

- Business State
- Archive Data

Lower priority.

- Binary Assets (depending upon regeneration policy)

Lowest priority.

- Derived Assets
- MOS Cache

The platform should avoid backing up information that is cheaper to rebuild.

---

# Recovery

Recovery should mirror lifecycle.

```mermaid
flowchart TD

N1["Restore Business State"]
N2["Restore Archives"]
N3["Restore Blob References"]
N4["Rebuild DuckDB"]
N5["Rebuild MOS Cache"]
N6["Resume Runtime"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Recovery should never require restoring analytical or cached datasets.

The Runtime should regenerate them automatically.

---

# Storage Transitions

Transitions between storage systems should always be explicit.

Example.

```mermaid
flowchart TD

N1["Business Event"]
N2["Analytics Pipeline"]
N3["DuckDB"]

N1 --> N2
N2 --> N3
```

Rather than.

```mermaid
flowchart TD

N1["Database Trigger"]
N2["Hidden Write"]

N1 --> N2
```

Storage transitions should remain:

- observable
- deterministic
- reviewable

---

# Lifecycle Ownership

Every lifecycle transition has exactly one owner.

Examples.

Import.

↓

Repository.

Enrichment.

↓

Capability.

Analytics.

↓

Analytics Capability.

Archive.

↓

Export Service.

Ownership prevents duplicated persistence behaviour.

---

# Event-Driven Storage

Storage transitions SHOULD be event driven.

Example.

```mermaid
flowchart TD

N1["MediaImported"]
N2["Metadata Capability"]
N3["Blob Storage"]
N4["MOS Cache"]
N5["DuckDB"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Each capability reacts independently.

The Storage Architecture naturally complements the Runtime Architecture established in [MEG-002](../meg-002-event-driven-runtime/index.md) and [MEG-005](../meg-005-runtime-architecture/index.md).

---

# Observability

The Storage Lifecycle SHOULD expose:

- imports
- enrichments
- cache rebuilds
- archive exports
- garbage collection
- recovery

Operators should always understand:

> **Where is this information within its lifecycle?**

---

# Anti-Patterns

The following practices are prohibited.

## Cache Before Business

Generating derived information before Business State exists.

---

## Shared Lifecycle Ownership

Multiple capabilities managing the same storage transition.

---

## Permanent Cache

Treating MOS Cache as authoritative.

---

## Hidden Storage Writes

Storage transitions occurring without Runtime visibility.

---

## Analytics Before Import

Generating analytical datasets before business information exists.

---

## Archive As Database

Using MOS Archives as primary Runtime persistence.

---

# Mosaic Guidelines

Within Mosaic:

- Storage transitions MUST follow information lifecycle.
- Business State MUST precede derived information.
- Cache SHOULD remain disposable.
- Archives MUST remain portable.
- Analytics SHOULD remain reproducible.
- Storage transitions SHOULD remain event driven.
- Every lifecycle transition MUST have one owner.
- Recovery SHOULD rebuild derived storage automatically.

---

# Relationship to MEG

Repositories explain:

> **How the Domain persists information.**

The Storage Lifecycle explains:

> **How that information evolves across storage systems over time.**

The next chapter introduces **Migrations**, defining how storage schemas, archive formats and persistence technologies evolve while preserving long-term compatibility.

---

# Summary

Storage is not static.

Information moves.

It matures.

It becomes enriched.

It is archived.

Eventually it disappears.

Within Mosaic, every storage transition should reflect a genuine change in the information itself while preserving one constant principle:

> **Authoritative information leads. Derived information follows.**

That simple rule keeps the entire Storage Architecture predictable, recoverable and easy to evolve.
