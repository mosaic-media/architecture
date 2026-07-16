<!--
File: docs/engineering/guides/meg-007-storage-architecture/01-storage-philosophy.md
Document: MEG-007
Status: Draft
Version: 0.4
-->

# Storage Philosophy

> **v2 decision:** The Platform uses PostgreSQL as the authoritative state store. The older polyglot-storage discussion in this chapter is historical context; Modules must use Platform storage contracts rather than selecting or owning their own database.

> *Information has different lifecycles. Storage should reflect those lifecycles rather than forcing every kind of data into one database.*

---

# Purpose

Traditional applications often begin with a single database.

Over time that database becomes responsible for:

- business transactions
- analytics
- caching
- metadata
- binary assets
- search
- reporting

Eventually:

Every problem is solved using the same storage engine.

Mosaic intentionally rejects this approach.

Instead, storage is selected according to the characteristics of the information being stored.

This document establishes the philosophical foundation for every storage decision throughout the platform.

---

# Philosophy

Within Mosaic:

> **Choose storage because of the data. Never choose the data because of the storage.**

Every storage engine exists because it is the best fit for one category of information.

No storage technology should become the default answer simply because it already exists.

---

# Information Before Technology

When designing persistence ask:

> **What kind of information is this?**

Not:

> **Which database do we already have?**

Information characteristics should determine:

- storage engine
- consistency model
- indexing strategy
- lifecycle
- backup policy

Technology follows information.

Never the reverse.

---

# Storage Is Infrastructure

Storage remains an implementation concern.

The Domain should never know whether information resides in:

- PostgreSQL
- DuckDB
- Blob Storage
- MOS Archive

The Domain simply persists business concepts.

Repositories determine where those concepts ultimately live.

This continues the architectural boundaries established in [MEG-004](../meg-004-hexagonal-architecture/index.md).

---

# Different Data Has Different Needs

Consider several examples.

Business transactions.

```mermaid
flowchart TD

N1["Strong Consistency"]
N2["PostgreSQL"]

N1 --> N2
```

Analytics.

```mermaid
flowchart TD

N1["Large Scans"]
N2["DuckDB"]

N1 --> N2
```

Artwork.

```mermaid
flowchart TD

N1["Binary Objects"]
N2["Blob Storage"]

N1 --> N2
```

Cached metadata.

```mermaid
flowchart TD

N1["Derived Information"]
N2["MOS Cache"]

N1 --> N2
```

Attempting to force these workloads into one storage engine usually produces unnecessary compromise.

---

# Polyglot Persistence

Mosaic intentionally adopts a **polyglot persistence** architecture.

This means:

Multiple specialised storage engines cooperate to form one coherent storage platform.

Each storage engine is selected because it excels at a particular workload.

Not because it can perform every workload adequately.

Polyglot persistence deliberately embraces multiple specialised databases instead of forcing all workloads into a single storage technology.  [thesai.org](https://thesai.org/Publications/ViewPaper?Code=ijacsa&Issue=5&SerialNo=99&Volume=13)

---

# One Source Of Truth

Although multiple storage engines exist:

Every piece of business information has exactly one authoritative owner.

Example.

```mermaid
flowchart TD

N1["Playback Progress"]
N2["PostgreSQL"]

N1 --> N2
```

Analytics derived from playback may exist elsewhere.

Those analytical copies are not authoritative.

The platform should always be able to answer:

> **Where is the source of truth?**

---

# Derived Data

Some information is reproducible.

Examples include:

- search indexes
- analytics
- thumbnails
- recommendations
- metadata caches

These should generally be treated as:

```

Derived Data
```

If lost:

The platform regenerates them.

Durable storage should be reserved for information that cannot be recreated.

---

# Business State

Business state deserves the highest protection.

Examples include:

- users
- libraries
- collections
- playback progress
- capability configuration

Business state should remain:

- durable
- transactional
- recoverable

It represents the long-term memory of the platform.

---

# Operational State

Operational state belongs to the Runtime.

Examples include:

- worker utilisation
- queue depth
- lifecycle state

Most operational state is:

- temporary
- reconstructable
- non-authoritative

The Runtime should not persist operational state unless it provides genuine operational value.

---

# Binary Data

Binary assets differ fundamentally from structured information.

Examples include:

- posters
- fan art
- subtitles
- generated previews

Binary assets should not be treated like relational data.

Storage should optimise for:

- retrieval
- streaming
- durability

rather than joins or transactions.

---

# Analytical Data

Analytical workloads differ from transactional workloads.

Examples include:

- viewing trends
- recommendation generation
- popularity analysis
- library statistics

These workloads favour:

- sequential scanning
- aggregation
- columnar storage

They should remain independent from transactional persistence.

---

# Information Lifecycle

Every category of information follows a lifecycle.

```mermaid
flowchart TD

N1["Created"]
N2["Active"]
N3["Referenced"]
N4["Archived"]
N5["Removed"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Different information progresses through these stages differently.

Storage architecture should reflect lifecycle rather than implementation convenience.

---

# Immutability

Some information should never change.

Examples include:

- event history
- audit records
- media fingerprints

Other information evolves continuously.

Examples include:

- playback progress
- metadata
- configuration

Storage selection should respect mutability characteristics.

---

# Replaceability

Storage engines should remain replaceable.

Suppose:

```mermaid
flowchart TD

N1["Blob Storage"]
N2["Alternative Blob Store"]

N1 --> N2
```

The Domain should remain unchanged.

Repositories adapt.

Storage implementation evolves.

Business behaviour remains identical.

---

# Ownership

Every storage technology owns one responsibility.

Examples.

```mermaid
flowchart TD

N1["PostgreSQL"]
N2["Transactional Business Data"]

N1 --> N2
```

```mermaid
flowchart TD

N1["DuckDB"]
N2["Analytical Data"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Blob Storage"]
N2["Binary Assets"]

N1 --> N2
```

Ownership should remain explicit.

Shared responsibility leads to ambiguity.

---

# Storage Should Be Invisible

End users should never think about storage.

They should never choose between:

- local
- remote
- cached
- archived

The platform should automatically determine the most appropriate storage strategy.

Storage should become an implementation detail hidden behind capability behaviour.

---

# Observability

Although storage should remain invisible to users, it should remain highly visible to operators.

The platform should expose:

- storage utilisation
- growth
- latency
- failures
- replication
- rebuild progress

Operational visibility should never require understanding implementation details.

---

# Simplicity

Using multiple storage engines increases operational complexity.

Therefore:

Every additional storage technology must justify its existence.

The Runtime should never introduce another persistence technology merely because it is interesting.

Each engine must solve a distinct problem that existing storage cannot solve cleanly.

One of the primary trade-offs of polyglot persistence is increased operational complexity, so each additional datastore should have a clear architectural justification.  [thesai.org](https://thesai.org/Publications/ViewPaper?Code=ijacsa&Issue=5&SerialNo=99&Volume=13)

---

# Mosaic Principles

Within Mosaic:

- Information determines storage.
- Every category of information has one authoritative owner.
- Storage remains infrastructure.
- Derived data should remain reproducible.
- Business state deserves the strongest guarantees.
- Binary assets should remain separate from transactional data.
- Analytical workloads deserve specialised storage.
- Storage should remain replaceable.
- Storage should remain invisible to end users.

These principles define the storage philosophy of the Mosaic platform.

---

# Relationship to MEG

Previous specifications established:

- how software is written
- how work executes
- how the business is modelled
- how capabilities evolve

MEG-007 begins answering:

> **Where should every kind of information live?**

The next chapter introduces the **Storage Taxonomy**, formally classifying every category of information managed by the Mosaic platform before assigning each category to its appropriate storage engine.

---

# Summary

Storage Architecture should never begin with databases.

It should begin with information.

By understanding:

- ownership
- lifecycle
- consistency
- mutability
- access patterns

the platform can naturally select the most appropriate storage technology for each responsibility.

Within Mosaic, storage exists to preserve information.

It should never dictate the architecture built upon it.
