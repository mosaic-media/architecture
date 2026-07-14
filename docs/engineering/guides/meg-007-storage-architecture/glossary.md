<!--
File: docs/engineering/guides/meg-007-storage-architecture/glossary.md
Document: MEG-007
Status: Draft
Version: 0.1
-->

# Glossary

> *Storage Architecture succeeds when every engineer classifies information the same way before deciding where it should live.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Storage Architecture.

These definitions establish the canonical storage vocabulary for:

- Architecture Specifications
- Repository Design
- Runtime Documentation
- Storage Implementations
- Contributor Guides
- Operational Documentation

Where a term has a specific meaning within the Mosaic Storage Architecture, that definition takes precedence over informal usage.

---

# A

## Analytical State

Information derived from business activity for analysis, reporting or optimisation.

Examples include:

- recommendation vectors
- viewing statistics
- popularity rankings
- metadata correlations

Analytical State belongs primarily within DuckDB.

It is generally reproducible.

---

## Archive Data

Portable, durable information intended for long-term preservation.

Examples include:

- MOS Archives
- exported libraries
- migration packages

Archive Data should remain Runtime independent.

---

# B

## Binary Asset

Large opaque objects stored independently from structured information.

Examples include:

- posters
- fan art
- subtitles
- preview images

Binary Assets belong in Blob Storage.

---

## Blob

A single binary object stored inside Blob Storage.

Blobs are referenced through stable identifiers rather than physical storage paths.

---

## Blob Storage

The storage subsystem responsible for binary assets.

Blob Storage owns:

- persistence
- retrieval
- streaming

It does not own business meaning.

---

## Business State

Authoritative information representing the business itself.

Examples include:

- users
- libraries
- collections
- playback progress

Business State is primarily stored in PostgreSQL.

---

# C

## Cache

A storage mechanism preserving derived information solely for performance.

Caches should always satisfy one principle.

```
Delete

↓

Rebuild
```

Caches are never authoritative.

---

## Content Addressing

A storage strategy where object identity derives from object content.

Typically implemented using cryptographic hashes.

Content addressing enables:

- deduplication
- integrity verification
- immutable storage

---

# D

## Derived Asset

Information generated from authoritative information.

Examples include:

- search indexes
- thumbnails
- recommendation vectors
- metadata caches

Derived Assets should remain reproducible.

---

## DuckDB

The analytical storage engine used by Mosaic.

DuckDB stores:

- analytical datasets
- recommendation inputs
- metadata relationships

It intentionally does not store authoritative Business State.

---

# M

## Migration

The process of transforming stored information or storage structures while preserving business meaning.

Migrations evolve storage implementation.

Not information ownership.

---

## MOS Archive

A portable, Runtime-independent archive format preserving media knowledge.

MOS Archives are:

- durable
- versioned
- portable

They complement, but do not replace, PostgreSQL.

---

## MOS Cache

A high-performance cache storing derived media information.

MOS Cache exists to improve Runtime performance.

It should never become authoritative.

---

# O

## Operational State

Temporary Runtime information required to coordinate execution.

Examples include:

- worker state
- scheduler state
- queue depth
- execution state

Operational State belongs to the Runtime.

Not Business Storage.

---

# P

## Polyglot Persistence

An architectural strategy using multiple specialised storage engines rather than one general-purpose database.

Within Mosaic this includes:

- PostgreSQL
- DuckDB
- Blob Storage
- MOS Archive
- MOS Cache

Each storage engine owns one distinct responsibility.

---

## PostgreSQL

The authoritative transactional storage engine for Business State.

PostgreSQL provides:

- durability
- consistency
- transactional guarantees

It represents the permanent business memory of the platform.

---

# R

## Repository

A Domain-owned abstraction responsible for persisting business entities.

Repositories protect the Domain from storage implementation.

Repository interfaces belong to the Domain.

Implementations belong to Infrastructure.

---

## Rebuildable Data

Information that can always be regenerated from authoritative sources.

Examples include:

- caches
- analytical datasets
- search indexes

Rebuildable information generally should not be backed up.

---

## Recovery

The process of restoring authoritative information following storage failure.

Recovery should restore:

- Business State
- Archive Data

before rebuilding derived information.

---

# S

## Source of Truth

The authoritative location responsible for one category of information.

Every business concept should have exactly one source of truth.

Derived copies never become authoritative.

---

## Storage Class

A category of information used by the Storage Taxonomy.

Storage Classes include:

- Business State
- Operational State
- Analytical State
- Binary Assets
- Derived Assets
- Archive Data

Storage Classes remain independent of storage technologies.

---

## Storage Lifecycle

The progression of information through different storage systems during its lifetime.

Examples include:

- import
- enrichment
- caching
- archiving
- deletion

Storage Lifecycle follows information ownership.

---

## Storage Taxonomy

The classification system used by Mosaic to categorise information before selecting storage technologies.

The Storage Taxonomy forms the foundation of the entire Storage Architecture.

---

# T

## Transactional State

Business information requiring:

- strong consistency
- durability
- atomic updates

Transactional State generally belongs within PostgreSQL.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| MEG | Mosaic Engineering Guidelines |
| MOS | Mosaic Object Storage (archive/cache format) |
| SQL | Structured Query Language |
| WAL | Write-Ahead Log |

---

# Relationship to MEG-007

This glossary supports every document within the Storage Architecture specification.

Definitions should remain consistent across:

- Runtime documentation
- Repository implementations
- Migration documentation
- Backup procedures
- Architecture Specifications

Whenever storage terminology evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`14-contributor-guidance.md`

**Next File**

`references.md`
