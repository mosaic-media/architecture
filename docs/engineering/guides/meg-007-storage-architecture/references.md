<!--
File: docs/engineering/guides/meg-007-storage-architecture/references.md
Document: MEG-007
Status: Draft
Version: 0.1
-->

# References

> *The Storage Architecture is built upon the principle that information should determine storage, not the other way around.*

---

# Purpose

This document records the primary references that informed the Storage Architecture established throughout MEG-007.

Unlike many storage architectures that begin with selecting a database, the Mosaic Storage Architecture begins by classifying information according to:

- ownership
- lifecycle
- access patterns
- consistency
- recoverability

Only then are storage technologies selected.

The purpose of these references is to document the architectural influences behind that philosophy.

---

# Primary References

## PostgreSQL

**Purpose**

PostgreSQL provides the transactional foundation for authoritative Business State.

Relevant characteristics include:

- ACID transactions
- strong consistency
- mature indexing
- long-term durability
- replication
- backup support

Within Mosaic, PostgreSQL is intentionally limited to transactional business information.

It is **not** the analytical engine.

---

## DuckDB

**Purpose**

DuckDB provides embedded analytical processing.

Relevant characteristics include:

- columnar storage
- vectorised execution
- embedded deployment
- analytical SQL
- persistent or in-memory operation

DuckDB is intentionally used for:

- recommendation generation
- metadata correlation
- reporting
- analytical processing

rather than transactional persistence.  [oai_citation:0‡DuckDB](https://duckdb.org/docs/current/connect/overview?utm_source=chatgpt.com)

---

# Polyglot Persistence

The Storage Architecture intentionally adopts **polyglot persistence**.

Relevant concepts include:

- workload-specific databases
- specialised storage engines
- explicit ownership
- separation of transactional and analytical workloads

The guiding architectural principle is:

> Use multiple specialised storage systems only when each solves a clearly different problem.

This is one of the defining architectural characteristics of Mosaic.

Research consistently identifies domain alignment and workload optimisation as the principal benefits of polyglot persistence, while also recognising the additional operational complexity it introduces.  [oai_citation:1‡arXiv](https://arxiv.org/abs/2204.05779?utm_source=chatgpt.com)

---

# Storage Engine Separation

A major influence upon this specification is the distinction between:

```
OLTP

↓

Transactional Databases
```

and

```
OLAP

↓

Analytical Databases
```

Within Mosaic this becomes:

```
PostgreSQL

↓

Business State
```

```
DuckDB

↓

Analytical State
```

Keeping these workloads independent allows each engine to optimise for its own responsibilities. DuckDB itself recommends persistent embedded storage for read-write workloads while focusing on analytical processing rather than replacing an OLTP database.  [oai_citation:2‡DuckDB](https://duckdb.org/faq?utm_source=chatgpt.com)

---

# Blob Storage

Blob Storage principles were influenced by long-established object storage concepts.

Relevant characteristics include:

- immutable objects
- streaming
- content addressing
- deduplication
- binary asset separation

Within Mosaic:

Binary assets remain separate from structured business information.

---

# Repository Pattern

The Repository guidance builds directly upon:

- Domain-Driven Design
- Hexagonal Architecture

Repositories protect:

- the Domain
- storage independence
- business language

Storage technologies remain infrastructure.

Repositories remain the architectural boundary.

---

# Information Lifecycle

MEG-007 intentionally models information rather than databases.

Relevant concepts include:

- information ownership
- lifecycle
- mutability
- recoverability
- derivation

The Storage Taxonomy forms the foundation of every later storage decision.

This philosophy intentionally precedes technology selection.

---

# Derived Information

The distinction between:

- authoritative information
- derived information

is central to the Storage Architecture.

Examples include:

Authoritative.

- users
- libraries
- playback progress

Derived.

- search indexes
- recommendations
- metadata caches

Derived information should remain reproducible.

Business information should remain protected.

---

# Backup Philosophy

Backup guidance follows established operational principles.

Information should be classified according to:

- business value
- recoverability
- regeneration cost

Rather than:

- storage engine

This allows:

- PostgreSQL backups
- archive preservation

while rebuilding:

- DuckDB
- MOS Cache

after recovery.

---

# DuckDB Integration

DuckDB is increasingly designed to integrate with transactional databases rather than replace them.

Relevant capabilities include:

- direct PostgreSQL integration
- analytical copies
- SQL interoperability

This architectural direction closely aligns with the separation adopted by Mosaic.  [oai_citation:3‡DuckDB](https://duckdb.org/docs/current/core_extensions/postgres/overview?utm_source=chatgpt.com)

---

# Go References

The Storage Architecture intentionally embraces idiomatic Go.

Recommended references include:

## Effective Go

Topics include:

- interfaces
- package ownership
- composition
- error handling

https://go.dev/doc/effective_go

---

## Go Code Review Comments

Topics include:

- interface ownership
- dependency management
- package boundaries

https://go.dev/wiki/CodeReviewComments

---

# Internal Mosaic Specifications

The following specifications complement MEG-007.

## Engineering

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Capability Runtime
- MEG-006 Extension Platform

---

## Planned Engineering Specifications

- MEG-008 Observability
- MEG-009 Security
- MEG-010 Performance Engineering
- MEG-011 Deployment Architecture
- MEG-012 API Architecture

---

## Mosaic Design Language

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model

---

## Mosaic Design Specifications

- MDS-001 Design Token Architecture
- MDS-002 Colour System
- MDS-003 Material System
- MDS-004 Typography System
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-007 Tile Framework
- MDS-008 Component Library

---

# Storage Principles

The Storage Architecture established throughout MEG-007 intentionally builds upon several enduring principles.

These include:

- Information determines storage.
- Business State remains authoritative.
- Derived information remains reproducible.
- Binary assets remain independent.
- Storage ownership remains explicit.
- Repositories protect the Domain.
- Storage technologies remain replaceable.
- Polyglot persistence exists only where workloads genuinely differ.
- Recovery restores business information before rebuilding derived information.

These principles should remain considerably more stable than the storage technologies implementing them.

---

# Keeping References Current

Storage technologies continue to evolve.

Analytical databases improve.

Object storage changes.

Operational practices mature.

This reference list SHOULD therefore be reviewed periodically to ensure:

- storage guidance remains relevant
- obsolete practices are removed
- improved architectural patterns are incorporated

The philosophy of information ownership should remain stable even as storage implementation evolves.

---

# Closing Statement

MEG-007 intentionally does not prescribe a single database architecture.

Instead, it classifies information first and assigns specialised storage technologies second.

The resulting Storage Architecture intentionally emphasises:

- explicit ownership
- transactional correctness
- analytical independence
- binary separation
- reproducible derived information
- long-term recoverability

Within Mosaic, storage exists to preserve information.

Everything else, databases, caches, object stores and archive formats, exists solely to serve that purpose.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`glossary.md`

**Next File**

**End of Specification**
