<!--
File: docs/engineering/guides/meg-007-storage-architecture/07-mos-cache.md
Document: MEG-007
Status: Draft
Version: 0.1
-->

# MOS Cache

> *The MOS archive preserves truth. The MOS cache preserves performance.*

---

# Purpose

Not every piece of information requires durable storage.

Many datasets exist solely to improve Runtime performance.

Examples include:

- resolved provider mappings
- artwork metadata
- metadata normalisation
- search indexes
- recommendation inputs
- playback manifests
- transcoding metadata

These datasets are:

- reproducible
- disposable
- performance oriented

Within Mosaic, this information is stored inside the **MOS Cache**.

Unlike the MOS Archive, the MOS Cache is intentionally ephemeral.

Its purpose is acceleration.

Not preservation.

---

# Philosophy

Within Mosaic:

> **If it can always be rebuilt, it should be cached rather than persisted.**

The MOS Cache exists only because rebuilding some information repeatedly is unnecessarily expensive.

Business correctness must never depend upon cache availability.

---

# What Is The MOS Cache?

The MOS Cache is a high-performance cache format storing derived media information.

Conceptually.

```text
MOS Cache

├── Resolved Metadata

├── Provider Mappings

├── Artwork Metadata

├── Search Indexes

├── Playback Metadata

└── Derived Runtime Data
```

Every entry represents information that can be regenerated.

---

# Why MOS Cache Exists

Without caching.

```text
Media

↓

TMDB

↓

AniList

↓

TVDB

↓

Normalise

↓

Runtime
```

Every request repeats identical work.

Instead.

```text
Media

↓

MOS Cache

↓

Runtime
```

Expensive work occurs once.

The Runtime consumes the cached result repeatedly.

---

# Cache Responsibility

MOS Cache owns:

- resolved metadata
- provider translation
- playback manifests
- artwork manifests
- search acceleration
- derived media information

It intentionally does **not** own:

- business entities
- Runtime state
- permissions
- users
- playback progress

Those remain authoritative elsewhere.

---

# Derived Information

Every MOS Cache entry MUST satisfy one requirement.

```
Delete

↓

Rebuild
```

If deletion would permanently lose information:

It does not belong in the cache.

The cache exists only for derived information.

---

# Relationship To MOS Archives

MOS Archive.

```text
Portable

↓

Durable

↓

Authoritative
```

MOS Cache.

```text
Local

↓

Ephemeral

↓

Derived
```

The two formats intentionally solve different problems.

They complement one another.

They should never replace one another.

---

# Cache Construction

Typical lifecycle.

```text
Business Information

↓

Metadata Resolution

↓

Normalisation

↓

MOS Cache

↓

Runtime Consumption
```

Cache generation should remain deterministic.

Identical inputs should produce functionally identical cache entries.

---

# Cache Identity

Every cache entry SHOULD possess a stable identity.

Examples include:

```text
Media ID
```

```text
Provider Mapping ID
```

```text
Artwork Manifest ID
```

Stable identifiers simplify:

- invalidation
- diagnostics
- rebuilding

Identity belongs to the cached object.

Not the storage implementation.

---

# Cache Granularity

Cache entries SHOULD remain small.

Preferred.

```text
One Media Object

↓

One Cache Entry
```

Avoid.

```text
Entire Library

↓

One Cache Entry
```

Fine-grained caches reduce:

- rebuild cost
- invalidation scope
- storage churn

---

# Provider Resolution

One of the MOS Cache's primary responsibilities is provider resolution.

Example.

```text
AniList

↓

TMDB

↓

TVDB

↓

IMDb

↓

Resolved Mapping
```

This avoids repeated metadata translation throughout the Runtime.

It also reflects one of the earliest architectural motivations for introducing a local metadata layer rather than repeatedly querying remote services. NullAnimeException_ Master Specification & Roadmap....pdf

---

# Artwork Resolution

Artwork metadata SHOULD be cached.

Examples include:

- selected artwork
- preferred language
- resolution
- dominant colours
- UV refraction maps

Notice:

The cache stores information **about** artwork.

Blob Storage stores the artwork itself.

Responsibilities remain separate.

---

# Playback Manifests

Streaming capabilities MAY cache resolved playback manifests.

Examples include:

- resolved streams
- subtitle selection
- audio defaults
- media capabilities

These manifests should remain disposable.

If upstream information changes:

The Runtime regenerates them.

---

# Search Acceleration

Search indexes naturally belong inside the MOS Cache.

Example.

```text
Metadata

↓

Search Index

↓

MOS Cache
```

Indexes remain:

- derived
- rebuildable
- disposable

Search correctness should never depend upon cache persistence.

---

# Recommendation Inputs

Recommendation engines MAY consume cached metadata.

Examples include:

- genre vectors
- tag vectors
- similarity inputs

The cache accelerates recommendation generation.

It does not own recommendation correctness.

DuckDB remains responsible for analytical processing.

---

# Cache Invalidation

Every cache entry MUST possess an invalidation strategy.

Examples include:

- metadata changed
- provider updated
- artwork replaced
- scheduled refresh
- manual refresh

Cache invalidation should remain explicit.

Never accidental.

---

# Cache Expiration

Entries MAY expire automatically.

Examples include:

```text
24 Hours
```

```text
7 Days
```

```text
Never

(Manual Refresh)
```

Expiration policy depends upon:

- provider freshness
- rebuild cost
- operational requirements

Not implementation convenience.

---

# Cache Rebuild

Rebuilding should always be possible.

Conceptually.

```text
Delete Cache

↓

Resolve Metadata

↓

Generate Cache

↓

Continue
```

The Runtime should never require backup restoration to recover cache contents.

---

# Locality

MOS Cache is intentionally local.

It should optimise:

- local performance
- low latency
- repeated access

Portability belongs to MOS Archives.

Runtime performance belongs to MOS Cache.

---

# Compression

MOS Cache MAY compress entries.

Compression should remain transparent.

Performance should always outweigh archive portability.

The cache exists to accelerate execution.

---

# Storage Format

The internal cache representation may evolve.

Capabilities should never depend upon:

- binary layout
- serialisation format
- compression algorithm

The Runtime owns cache implementation.

Capabilities consume cache behaviour.

---

# Observability

The Runtime SHOULD expose:

- cache size
- hit rate
- miss rate
- rebuild activity
- invalidation events
- rebuild duration

Operators should understand cache effectiveness.

Not merely cache existence.

---

# Anti-Patterns

The following practices are prohibited.

## Business State

Persisting authoritative business entities inside MOS Cache.

---

## Runtime State

Caching worker or scheduler information.

---

## Irreplaceable Information

Storing information that cannot be regenerated.

---

## Manual Cache Editing

Treating cache contents as authoritative business data.

---

## Archive Replacement

Using MOS Cache instead of MOS Archives for long-term portability.

---

## Cross-Capability Ownership

Multiple capabilities claiming authority over the same cache entries.

---

# Mosaic Guidelines

Within Mosaic:

- MOS Cache MUST contain only derived information.
- Cache entries MUST remain reproducible.
- Cache invalidation MUST remain explicit.
- Search indexes SHOULD remain cached.
- Provider mappings SHOULD remain cached.
- Artwork metadata SHOULD remain cached.
- Cache implementation MUST remain Runtime owned.
- Business correctness MUST remain independent of cache availability.

---

# Relationship to MEG

MOS Archives preserve:

> **Portable business knowledge.**

MOS Cache preserves:

> **Runtime performance.**

The next chapter introduces **Repositories**, describing how the Domain interacts with these storage technologies while remaining completely unaware of their implementation.

---

# Summary

The MOS Cache is the platform's short-term memory.

It remembers expensive work so that the Runtime does not have to repeat it.

Unlike the MOS Archive, it makes no promise of permanence.

It promises only one thing:

> **Everything stored here can always be rebuilt.**

That single guarantee allows the Runtime to optimise aggressively without ever compromising the integrity of the platform's authoritative information.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`06-mos-archives.md`

**Next File**

`08-repositories.md`
