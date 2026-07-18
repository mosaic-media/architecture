<!--
File: docs/engineering/guides/meg-007-storage-architecture/06-mos-archives.md
Document: MEG-007
Status: Draft
-->

# MOS Archives

> *A MOS archive is not a database. It is a portable snapshot of media knowledge.*

---

# Purpose

Mosaic supports many kinds of media.

Examples include:

- local libraries
- remote libraries
- Stremio sources
- Jellyfin migrations
- Plex migrations
- archived collections

The Runtime requires a portable format capable of preserving media information independently of:

- databases
- storage engines
- Runtime versions
- deployment environments

That format is the **MOS Archive**.

A MOS archive represents long-lived, portable media knowledge.

It exists independently of the Runtime.

---

# Philosophy

Within Mosaic:

> **MOS archives preserve information. They do not execute it.**

A MOS archive should answer:

> **What does this media collection represent?**

It should not answer:

> **How should the Runtime execute it?**

Execution belongs to the Runtime.

Persistence belongs to the archive.

---

# What Is A MOS Archive?

A MOS archive is a portable package describing media.

Conceptually.

```mermaid
flowchart TD

N1["MOS Archive"]
N2["Media Identity"]
N3["Metadata"]
N4["Artwork References"]
N5["Provider References"]
N6["Playback Metadata"]
N7["Relationships"]
N8["Archive Metadata"]

N1 --> N2
N1 --> N3
N1 --> N4
N1 --> N5
N1 --> N6
N1 --> N7
N1 --> N8
```

The archive is self-describing.

It should remain readable independently of the Runtime.

---

# Why MOS Exists

Without MOS:

```mermaid
flowchart TD

N1["Runtime"]
N2["Database"]
N3["Media Lost Outside Runtime"]

N1 --> N2
N2 --> N3
```

Media knowledge becomes tightly coupled to one installation.

Instead.

```mermaid
flowchart TD

N1["Runtime"]
N2["MOS Archive"]
N3["Portable"]

N1 --> N2
N2 --> N3
```

The archive becomes:

- exportable
- importable
- versionable
- durable

---

# Archive Responsibility

MOS archives own:

- media identity
- metadata references
- provider mappings
- archive metadata
- media relationships

They intentionally do **not** own:

- Runtime state
- worker state
- scheduler state
- capability lifecycle
- execution metadata

MOS preserves media.

The Runtime executes media.

---

# Archive Is Not Storage

MOS should not be mistaken for:

```

Primary Persistence
```

Business State continues to live inside PostgreSQL.

The MOS archive is:

- portable
- durable
- shareable

It complements the Storage Architecture.

It does not replace it.

---

# Archive Structure

Conceptually.

```mermaid
flowchart TD

N1["Archive Header"]
N2["Media Entries"]
N3["Provider References"]
N4["Relationships"]
N5["Checksums"]
N6["Manifest"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Every archive should remain self-describing.

Future Runtime versions should understand the archive without external context.

---

# Media Identity

Every media object MUST possess a stable identity.

Example.

```text
MOS Media ID
```

External identifiers may include:

- TMDB
- IMDb
- TVDB
- AniList
- MAL

The MOS identifier remains the Runtime's canonical archive identity.

---

# Metadata

MOS archives preserve metadata.

Examples include:

- titles
- synopsis
- genres
- release dates
- studios
- cast
- tags

Metadata should remain portable.

The archive should not depend upon external APIs remaining available forever.

---

# Provider References

MOS archives SHOULD preserve external provider mappings.

Examples.

```mermaid
flowchart TD

N1["TMDB"]
N2["12345"]

N1 --> N2
```

```mermaid
flowchart TD

N1["AniList"]
N2["99887"]

N1 --> N2
```

```mermaid
flowchart TD

N1["IMDb"]
N2["tt1234567"]

N1 --> N2
```

These mappings allow the Runtime to reconnect archived media with external ecosystems when appropriate.

---

# Artwork References

MOS archives SHOULD reference artwork.

The preferred model is:

```text
Artwork Blob ID
```

or

```text
Artwork URL
```

The archive should avoid unnecessarily embedding large binary assets unless explicitly requested.

Binary assets remain the responsibility of Blob Storage.

---

# Media Relationships

MOS archives preserve logical relationships.

Examples include:

- collections
- franchises
- sequels
- seasons
- episodes

Relationships are business information.

They belong inside the archive.

---

# Playback Information

MOS archives MAY preserve portable playback metadata.

Examples include:

- watched
- watch history
- resume position
- ratings

These are business concepts.

They differ from Runtime execution history.

Operational Runtime information should never appear inside MOS.

---

# Capability Independence

MOS archives should remain independent of capabilities.

The archive should never contain:

- capability identifiers
- Runtime contracts
- SDK versions

Capabilities interpret archives.

Archives should not depend upon capabilities.

---

# Archive Versioning

Every MOS archive MUST declare its archive version.

Example.

```text
MOS Archive v2
```

Versioning allows future Runtime releases to:

- migrate
- validate
- import

older archives safely.

Archive evolution should remain backwards compatible where practical.

---

# Compression

MOS archives MAY be compressed.

Compression should remain transparent.

The archive format should remain logically identical regardless of compression strategy.

Compression optimises transport.

Not semantics.

---

# Integrity

Every archive SHOULD include integrity information.

Examples include:

- checksums
- hashes
- signatures

Integrity verification should occur before import.

Corrupted archives should never partially import.

---

# Import

Import follows a deterministic lifecycle.

```mermaid
flowchart TD

N1["Read Archive"]
N2["Validate"]
N3["Verify Integrity"]
N4["Migrate"]
N5["Import"]
N6["Complete"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Import should never modify an archive.

The Runtime adapts itself.

The archive remains immutable.

---

# Export

Export should produce a self-contained representation of media knowledge.

Export should never depend upon:

- Runtime state
- active workers
- scheduler state

Exports should remain reproducible.

Given identical business information:

The resulting archive should be functionally identical.

---

# Archive Independence

A MOS archive should remain usable:

- offline
- years later
- on another Runtime
- on another operating system

Portability is one of its defining architectural characteristics.

---

# Backup

MOS archives naturally complement platform backups.

Examples include:

- library export
- migration
- disaster recovery
- offline archive

Unlike database backups:

MOS archives represent logical media collections rather than implementation-specific persistence.

---

# Archive Is Not Cache

MOS archives should never contain:

- Runtime caches
- analytical datasets
- worker information
- temporary metadata

Caches remain reproducible.

Archives preserve durable knowledge.

---

# Archive Is Not Runtime

The Runtime may consume MOS archives.

The archive should never describe:

- execution
- scheduling
- capability activation
- Runtime topology

Those concepts remain implementation details.

---

# Observability

Import and export operations SHOULD expose:

- archive version
- media count
- validation results
- migration activity
- integrity verification

Operators should always understand:

> **What happened during archive processing?**

---

# Anti-Patterns

The following practices are prohibited.

## Runtime State

Persisting worker or scheduler information inside MOS.

---

## Embedded Database Dumps

Treating MOS as a PostgreSQL backup.

---

## Runtime Contracts

Embedding SDK or Runtime implementation details.

---

## Mutable Archives

Modifying archives during import.

---

## Cache Data

Persisting search indexes or analytical caches.

---

## Capability Metadata

Encoding capability implementation details inside the archive.

---

# Mosaic Guidelines

Within Mosaic:

- MOS archives MUST remain portable.
- MOS archives MUST remain Runtime independent.
- Every archive MUST declare its version.
- Archive integrity SHOULD be verified before import.
- Business information SHOULD remain self-contained.
- Runtime state MUST NOT appear inside archives.
- Binary assets SHOULD remain externally referenced where practical.
- Import MUST remain deterministic.
- Export SHOULD produce reproducible archives.

---

# Relationship to MEG

Blob Storage preserves:

> **Binary assets.**

MOS archives preserve:

> **Portable business knowledge.**

The next chapter introduces **MOS Cache**, defining Mosaic's high-performance derived cache format for information that can always be regenerated and therefore should never become authoritative.

---

# Summary

A MOS archive is the long-term memory of a media collection.

It preserves:

- identity
- metadata
- relationships
- portability

while remaining completely independent of:

- Runtime implementation
- storage engines
- execution models

Within Mosaic, a MOS archive should still be meaningful decades later, even if the Runtime that created it no longer exists.

That permanence is its defining architectural responsibility.
