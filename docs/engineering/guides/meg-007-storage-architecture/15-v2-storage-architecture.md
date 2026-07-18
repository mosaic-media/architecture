<!--
File: docs/engineering/guides/meg-007-storage-architecture/15-v2-storage-architecture.md
Document: MEG-007
Chapter: 15
Title: v2 Storage Architecture
Status: Draft
Version: 0.4
-->

# v2 Storage Architecture

> **Current direction:** PostgreSQL is Mosaic's authoritative state store. Modules use Platform-owned storage contracts and do not create independent databases.

This chapter records the authoritative v2 storage design for the Mosaic Platform Foundation. It refines the existing storage taxonomy around one consistency domain, a shared object graph and logical bounded contexts. Where earlier chapters in this specification describe a mandatory second analytical database, this chapter supersedes them. The decision behind it is recorded in [MAD-002 — Module Storage and Delivery Model](../../architecture/mad-002-module-storage-and-delivery-model/index.md).

## Ownership Rule

The Platform owns the storage authority, connection lifecycle, migrations, transactions, access policy, backup boundary and repository contracts.

Modules contribute domain behaviour and use scoped repositories or services exposed by the Platform. They do not own storage engines, define their own tables, modify Platform schema, bypass Platform policy or query another context's tables directly ([MIP-005](../../protocols/mip-005-module-adapter-contract-protocol/index.md)).

The schema is designed so this is practical rather than limiting. The Platform's object model is deliberately **content-agnostic** — a recursive node tree, a separate relation graph, engine-neutral identity and flexible per-type attributes — so any Module maps its data onto existing structure. Adding a new content capability is new rows and attribute data, not new schema. A genuinely new data-owning domain is Platform and SDK evolution, decided deliberately, not something a Module introduces on its own.

Bounded contexts own logical aggregates and persistence responsibility within the shared database. Logical ownership is not permission to create a fragmented storage system.

```mermaid
flowchart TD

P["Mosaic Platform Storage"]
R["Scoped Repository Contracts"]
C1["Catalog Context"]
C2["Ingest Context"]
C3["Source Context"]
C4["Playback Context"]
C5["Asset Context"]
C6["Access Context"]

P --> R
R --> C1
R --> C2
R --> C3
R --> C4
R --> C5
R --> C6
```

## Object Graph

Mosaic represents media through three related concepts:

- **Node** — a recursive Work, Container or Item tree;
- **Part** — a playable, readable or otherwise selectable edition/source belonging to an Item; and
- **Relation** — a graph edge for relationships that are not containment.

This supports variable-depth structures without media-specific table trees:

| Example | Node structure |
|---------|----------------|
| Movie | Work → Item |
| TV or anime series | Work → Season → Episode |
| Manga with volumes | Work → Volume → Chapter |
| Ongoing chapter-only manga | Work → Chapter |
| Album | Work → Disc → Track |
| Book | Work → Item or Chapter |

An edition or cut remains a Part, not a second media Node. Anime and its source manga remain separate Works connected by a Relation.

## PostgreSQL State Store

PostgreSQL is the single authoritative database for transactional and queryable Mosaic state. It stores the object graph, access state, source bindings, jobs, domain events, projections and control-plane records in one consistency domain.

The v2 design does not place PostgreSQL and a separate analytical database on competing critical paths. A separate analytical database is not required for the Platform Foundation.

## Analytical Processing Port

Analytical work — recommendations, cross-provider correlation, reporting, popularity ranking and search candidates — is defined behind a Platform-owned **analytical processing port**, not bound to a specific engine.

```mermaid
flowchart TD

N1["Analytical Processing Port"]
N2["PostgreSQL adapter (today)"]
N3["Dedicated analytical engine (later, if needed)"]

N1 --> N2
N1 -.->|"added only if PostgreSQL cannot carry the load"| N3
```

PostgreSQL satisfies the port today, through materialised views, relation edges and the `SKIP LOCKED` job queue. One database is sufficient for the Platform Foundation.

If PostgreSQL cannot carry the analytical load alone, an additional engine — for example DuckDB — is added as an **essential Module implementing the same port**, exactly like any other adapter. It never becomes a competing source of business truth: authoritative state stays in the state store and analytical outputs remain derived and reproducible.

The Platform therefore mandates the analytical capability, not the number of databases that provide it. This is the storage-as-a-port principle of [MAD-001 — Transactional Store Extensibility](../../architecture/mad-001-transactional-store-extensibility/index.md) applied to analytics.

The core object tables are conceptually:

```text
nodes
parts
relations
source_bindings
users and access records
registered_devices and sessions
domain_events
jobs
```

## Logical Bounded Contexts

The contexts share PostgreSQL but preserve aggregate boundaries in code and through repository contracts:

| Context | Aggregate root | Primary responsibility |
|---------|----------------|------------------------|
| Catalog | Node | Identity, tree structure, relations and source bindings |
| Ingest | ImportJob | Discovery, staging, quarantine and import completion |
| Source | Source | Source registration, health and resolver state |
| Playback | PlaybackSession | Part selection, resume and playback policy |
| Asset | Asset | Artwork candidates, selection and blob lifecycle |
| Access | User | Accounts, permissions, device sessions and per-user state |

Cross-context work communicates through application services and domain events. Context code must not reach across another context's tables to bypass those boundaries.

## Transactional Event Outbox

Domain state changes and their corresponding events commit atomically:

```text
state change + domain_events row
        → one PostgreSQL transaction
        → commit
        → dispatcher wakes
        → in-process Event Bus fan-out
        → GraphQL subscriptions and workers
```

An undispatched event remains recoverable after restart. Background work uses the same PostgreSQL job queue with retry, dead-letter and `SKIP LOCKED` claiming semantics.

## Filesystem And `.mos` Canon

`.mos` files and `.mosaic` packages contain metadata, intent and references. They never contain primary media bytes.

Packages should be human-browsable and written at container granularity, such as one manifest per season or manga volume. Primary media remains in its native format: MKV, MP4, FLAC, EPUB, CBZ and similar formats.

## Blob Plane

Artwork, thumbnails, subtitles and generated assets use content-addressed blob storage. The database stores stable blob identifiers and metadata; it does not make physical paths part of Module or client contracts.

Primary media remains source-owned and is served through the Playback context without being wrapped in a custom Mosaic media container.

## GraphQL And Playback

GraphQL is a projection layer over Platform domain services. It contains no storage logic and may expose subscriptions backed by the Event Bus.

Playback resolves the best Part for the user and client, then serves local or remote bytes through a range-capable path. Import, enrichment and event processing must not block direct playback unnecessarily.

## Consequences

This design provides:

- one transaction and backup boundary;
- one source of truth for catalog, access and operational state;
- shared storage infrastructure without Module-owned database fragmentation;
- logical context ownership without synchronisation between separate engines;
- replayable domain events and recoverable background work; and
- a clear path from local deployment to larger PostgreSQL-backed installations.

The trade-off is that PostgreSQL is a Platform dependency rather than an optional implementation detail for the first deployment profile. A future embedded packaging strategy may improve installation UX without changing the storage contracts.
