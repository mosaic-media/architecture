<!--
File: docs/engineering/guides/meg-007-storage-architecture/index.md
Document: MEG-007
Status: Draft
Version: 0.1
-->

# MEG-007 — Storage Architecture

> *Storage should preserve information. It should never dictate architecture.*

---

# Purpose

The previous engineering specifications established:

- how software is written
- how work executes
- how the business is modelled
- how the Domain is protected
- how the Runtime operates
- how the platform evolves

MEG-007 answers the next foundational question.

> **How should information be stored throughout the Mosaic platform?**

Unlike traditional media servers, Mosaic does not treat storage as a single filesystem.

Instead, it separates storage according to the nature of the information being stored.

Business state.

Operational state.

Metadata.

Media.

Artwork.

Search indexes.

Analytics.

Each has different performance characteristics, lifecycle requirements and consistency guarantees.

The Storage Architecture defines where those responsibilities belong.

---

# Relationship to MEG

```
MEG-001

↓

Engineering Standards

↓

MEG-002

↓

Reactive Runtime

↓

MEG-003

↓

Domain Model

↓

MEG-004

↓

Hexagonal Architecture

↓

MEG-005

↓

Capability Runtime

↓

MEG-006

↓

Extension Platform

↓

MEG-007

↓

Storage Architecture
```

Previous specifications define:

> **How the platform behaves.**

MEG-007 defines:

> **Where the platform remembers.**

---

# Scope

This specification defines:

- Storage philosophy
- Storage taxonomy
- Persistence boundaries
- PostgreSQL architecture
- DuckDB architecture
- Blob Storage architecture
- MOS archive format
- MOS cache format
- Repository implementations
- Search indexes
- Metadata persistence
- Artwork persistence
- Migration strategy
- Backup and restore
- Storage lifecycle

This specification intentionally does **not** define:

- Business behaviour
- Runtime execution
- Extension SDKs
- Deployment topology

Those concerns belong to previous or future MEG specifications.

---

# Core Question

MEG-007 exists to answer one question.

> **How should Mosaic persist information while remaining scalable, observable and independent of storage technology?**

---

# Storage Statement

Within Mosaic:

> **Storage is an implementation detail. Information architecture is not.**

Every storage technology exists because it is the best fit for a particular category of information.

No single database should become responsible for every problem.

The platform should choose storage according to:

- access patterns
- consistency requirements
- query characteristics
- lifecycle
- operational cost

rather than familiarity or convenience.

---

# Storage Hierarchy

The Mosaic platform intentionally separates storage into distinct layers.

```
Business Data

↓

Operational Data

↓

Analytical Data

↓

Media Assets

↓

Derived Assets
```

Implemented as:

```
PostgreSQL

↓

DuckDB

↓

Blob Storage

↓

MOS Archives

↓

MOS Cache
```

Each storage system owns one responsibility.

---

# Expected Outcome

After reading MEG-007 contributors should understand:

- why Mosaic uses multiple storage engines
- which information belongs in each storage system
- where repositories persist data
- how storage integrates with the Runtime
- how media and metadata remain independent
- how storage evolves without affecting the Domain

without discussing any specific business capability.

---

# Repository Structure

```text
engineering/

└── meg/

    └── MEG-007 Storage Architecture/

        README.md

        00-document-control.md

        01-storage-philosophy.md

        02-storage-taxonomy.md

        03-postgresql.md

        04-duckdb.md

        05-blob-storage.md

        06-mos-archives.md

        07-mos-cache.md

        08-repositories.md

        09-storage-lifecycle.md

        10-migrations.md

        11-backup-and-restore.md

        12-storage-guidelines.md

        13-adrs.md

        14-contributor-guidance.md

        glossary.md

        references.md
```

---

# Dependencies

Required reading:

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Capability Runtime Architecture
- MEG-006 Extension Platform

---

# Design Goals

The Storage Architecture is intended to produce a platform that is:

- Purpose-built
- Observable
- Performant
- Replaceable
- Scalable
- Recoverable
- Technology independent
- Operationally predictable

Every storage engine should own one clear responsibility and evolve independently of the others.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Next File**

`00-document-control.md`
