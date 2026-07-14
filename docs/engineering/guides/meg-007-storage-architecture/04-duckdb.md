<!--
File: docs/engineering/guides/meg-007-storage-architecture/04-duckdb.md
Document: MEG-007
Status: Draft
Version: 0.1
-->

# DuckDB

> *DuckDB is not the memory of the business. It is the memory of understanding.*

---

# Purpose

Transactional databases excel at:

- inserts
- updates
- point lookups
- consistency

They perform considerably less well at:

- analytical scans
- aggregations
- recommendation generation
- trend analysis
- metadata correlation

These workloads require a different architecture.

Within Mosaic, DuckDB provides a specialised analytical engine responsible for processing information rather than owning it.

DuckDB exists to answer questions.

Not preserve business truth.

---

# Philosophy

Within Mosaic:

> **DuckDB stores analytical truth. PostgreSQL stores business truth.**

This distinction is fundamental.

PostgreSQL answers:

> **What happened?**

DuckDB answers:

> **What does it mean?**

The two databases cooperate.

Neither replaces the other.

---

# Why DuckDB?

DuckDB was selected because it provides:

- columnar storage
- vectorised execution
- extremely fast analytical queries
- embedded deployment
- SQL compatibility
- low operational overhead

These characteristics make it exceptionally well suited to:

- recommendation engines
- metadata correlation
- reporting
- search optimisation
- behavioural analysis

DuckDB is intentionally **not** a transactional database.

---

# Storage Responsibility

DuckDB owns:

- analytical datasets
- recommendation inputs
- reporting datasets
- metadata relationships
- search optimisation
- usage analytics

It intentionally does **not** own:

- users
- playback progress
- collections
- configuration
- permissions

Those remain transactional business state.

---

# Analytical Source Of Truth

DuckDB may become authoritative for analytical information.

Examples include:

```
Recommendation Vectors
```

```
Similarity Scores
```

```
Popularity Rankings
```

```
Content Correlations
```

These values are analytical outputs.

They are not business entities.

If necessary, they can be regenerated.

---

# Business Separation

DuckDB should never become the authoritative store for business entities.

Poor.

```
DuckDB

↓

Playback Progress
```

Preferred.

```
PostgreSQL

↓

Playback Progress

↓

DuckDB

↓

Viewing Statistics
```

Business ownership remains unchanged.

DuckDB consumes information.

It does not own it.

---

# Read-Optimised Design

DuckDB should optimise for:

- sequential scans
- aggregation
- filtering
- grouping
- joins across large datasets

It should not optimise for:

- transactional updates
- high-frequency writes
- business concurrency

Every storage engine should embrace its natural strengths.

---

# Data Ingestion

DuckDB receives information from:

- Runtime Events
- PostgreSQL snapshots
- capability exports
- metadata imports

Typical flow.

```
Business Event

↓

Analytical Pipeline

↓

DuckDB
```

Capabilities should never write directly into analytical tables as part of transactional workflows.

The Runtime should separate transactional persistence from analytical ingestion.

---

# Metadata Correlation

One of DuckDB's primary responsibilities is metadata correlation.

Examples include:

```
TMDB

↓

AniList

↓

TVDB

↓

IMDb

↓

Internal IDs
```

Large cross-provider mapping datasets are naturally analytical.

They benefit from DuckDB's execution model far more than a transactional database.

This follows the architectural direction explored in the earlier embedded hybrid-database design, where large metadata mapping datasets were intentionally separated from transactional state. NullAnimeException_ Master Specification & Roadmap....pdf

---

# Recommendation Engine

Recommendation generation naturally belongs within DuckDB.

Example.

```
Viewing History

↓

Similarity Analysis

↓

Recommendation Scores
```

The resulting recommendations become:

```
Derived Data
```

If recommendation data is lost:

The Runtime regenerates it.

No business correctness is affected.

---

# Search Optimisation

DuckDB may support search acceleration.

Examples include:

- popularity weighting
- ranking models
- recommendation scoring
- metadata filtering

The search index itself remains derived.

DuckDB should optimise search.

Not become the primary search engine.

---

# Reporting

Operational reporting naturally belongs within DuckDB.

Examples include:

- viewing statistics
- library growth
- media popularity
- storage utilisation
- extension usage

Reporting should never degrade transactional performance.

Separating reporting workloads preserves PostgreSQL for business operations.

---

# Materialised Views

DuckDB MAY maintain derived analytical views.

Examples include:

```
Top Movies

↓

Materialised View
```

```
Trending Anime

↓

Materialised View
```

These views improve analytical performance.

They should remain reproducible.

---

# Batch Processing

DuckDB is naturally suited to batch-oriented workloads.

Examples include:

- nightly recommendation rebuilds
- metadata normalisation
- analytics refresh
- reporting snapshots

Large analytical transformations should occur outside transactional workflows.

---

# Event Consumption

DuckDB should consume Runtime Events.

Example.

```
PlaybackCompleted

↓

Analytics Pipeline

↓

DuckDB
```

This preserves loose coupling between:

- business capabilities
- analytical processing

The Domain remains unaware of analytics.

---

# Refresh Strategy

Analytical datasets SHOULD be refreshable.

Typical strategies include:

- incremental updates
- scheduled rebuilds
- event-driven updates

The chosen strategy should depend upon:

- data freshness
- workload
- operational cost

Not implementation convenience.

---

# Durability

Analytical data may be durable.

However:

Durability should not imply authority.

If analytical data becomes inconsistent:

The platform should rebuild it from authoritative business information.

---

# Performance

DuckDB should optimise for:

- high-throughput reads
- vectorised execution
- analytical joins
- aggregation

Transactional latency should never influence DuckDB design.

The database exists for different work.

---

# Observability

DuckDB SHOULD expose:

- query latency
- ingestion rate
- analytical refresh duration
- storage growth
- rebuild progress

Operators should understand analytical health independently from transactional health.

---

# Anti-Patterns

The following practices are prohibited.

## Transactional Business State

Persisting authoritative business entities inside DuckDB.

---

## Capability Ownership

Capabilities treating DuckDB as their primary persistence store.

---

## High-Frequency Writes

Using DuckDB for transactional workloads.

---

## Shared Authority

Allowing PostgreSQL and DuckDB to become competing sources of truth.

---

## Business Logic

Executing business behaviour inside analytical queries.

---

## Irreplaceable Analytics

Creating analytical datasets that cannot be regenerated.

---

# Mosaic Guidelines

Within Mosaic:

- DuckDB MUST remain the analytical storage engine.
- Business State MUST remain outside DuckDB.
- DuckDB SHOULD consume Runtime events and derived datasets.
- Analytical outputs SHOULD remain reproducible.
- Recommendation engines SHOULD build upon DuckDB.
- Reporting SHOULD remain isolated from transactional persistence.
- DuckDB SHOULD optimise for analytical workloads.
- PostgreSQL and DuckDB MUST never compete as authoritative sources of business truth.

---

# Relationship to MEG

PostgreSQL preserves:

> **Business truth.**

DuckDB derives:

> **Business understanding.**

The next chapter introduces **Blob Storage**, defining how Mosaic stores large binary assets such as artwork, subtitles, previews and other media resources while keeping them independent from both transactional and analytical storage.

---

# Summary

DuckDB is the platform's analytical memory.

It remembers:

- relationships
- patterns
- statistics
- correlations

It intentionally does **not** remember:

- users
- collections
- playback state
- configuration

By separating analytical processing from transactional persistence, Mosaic gains the ability to perform sophisticated queries, recommendations and reporting without compromising the integrity or performance of the business systems that drive the platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`03-postgresql.md`

**Next File**

`05-blob-storage.md`
