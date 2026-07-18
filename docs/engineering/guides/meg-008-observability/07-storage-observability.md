<!--
File: docs/engineering/guides/meg-008-observability/07-storage-observability.md
Document: MEG-008
Status: Draft
-->

# Storage Observability

> *The platform should not only know where information is stored. It should know how well every storage system is performing that responsibility.*

---

# Purpose

[MEG-007](../meg-007-storage-architecture/index.md) defined the Storage Architecture.

Mosaic persists information across several specialised storage systems.

These include:

- PostgreSQL
- DuckDB
- Blob Storage
- MOS Archives
- MOS Cache

Each system owns different information.

Each therefore requires different observability.

Storage Observability exposes the operational behaviour of every storage subsystem while preserving the architectural ownership established in [MEG-007](../meg-007-storage-architecture/index.md).

---

# Philosophy

Within Mosaic:

> **Observe storage according to the information it owns, not according to the database implementing it.**

Operators should understand:

- information health
- storage performance
- storage lifecycle
- recovery readiness

Storage engines are implementation details.

Information ownership remains the primary architectural concern.

---

# Storage Observability Hierarchy

Storage telemetry follows the Storage Taxonomy.

```mermaid
flowchart TD

N1["Business State"]
N2["Analytical State"]
N3["Binary Assets"]
N4["Derived Assets"]
N5["Archive Data"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every storage engine exposes telemetry appropriate to its responsibility.

No storage engine should expose metrics belonging to another storage class.

---

# Business State Observability

Business State resides primarily within PostgreSQL.

The platform SHOULD observe:

- transaction latency
- commit rate
- rollback rate
- connection pool usage
- lock contention
- migration status

Operators should understand:

> **Can authoritative business information be safely persisted?**

Business correctness remains the highest storage priority.

---

# Analytical Observability

DuckDB primarily serves analytical workloads.

The platform SHOULD observe:

- query duration
- aggregation latency
- recommendation rebuild time
- ingestion throughput
- analytical storage growth

Operators should understand:

> **How efficiently is the analytical platform operating?**

Analytical telemetry should remain independent of transactional telemetry.

---

# Blob Storage Observability

Blob Storage SHOULD expose:

- blob count
- storage utilisation
- retrieval latency
- upload latency
- streaming throughput
- corruption detection
- deduplication efficiency

Operators should understand:

> **How efficiently are binary assets being managed?**

Business metadata remains outside Blob Storage.

Observability should reinforce that separation.

---

# MOS Archive Observability

Archive operations SHOULD expose:

- archive version
- export duration
- import duration
- integrity verification
- compatibility warnings
- migration activity

Operators should answer:

> **Can archived information still be restored safely?**

Archive observability focuses upon portability rather than Runtime performance.

---

# MOS Cache Observability

MOS Cache SHOULD expose:

- cache size
- hit ratio
- miss ratio
- rebuild frequency
- invalidation rate
- rebuild duration

Operators should understand:

> **Is the cache improving Runtime performance?**

Cache observability should never imply cache authority.

---

# Repository Observability

Repositories form the architectural boundary between:

- Domain
- Storage

Repository implementations SHOULD expose:

- repository latency
- storage backend
- cache usage
- transaction duration
- retry activity

Repositories describe persistence behaviour.

They do not expose SQL implementation details.

---

# Storage Lifecycle Events

Storage lifecycle operations SHOULD produce observable events.

Examples include:

```text
Media Imported
```

```text
Artwork Cached
```

```text
MOS Archive Exported
```

```text
Recommendation Rebuilt
```

These events describe information movement throughout the Storage Lifecycle.

They complement Runtime Events defined in [MEG-002](../meg-002-event-driven-runtime/index.md).

---

# Storage Health

Every storage system SHOULD expose health independently.

Examples.

```mermaid
flowchart TD

N1["PostgreSQL"]
N2["Healthy"]

N1 --> N2
```

```mermaid
flowchart TD

N1["DuckDB"]
N2["Healthy"]

N1 --> N2
```

```mermaid
flowchart TD

N1["Blob Storage"]
N2["Degraded"]

N1 --> N2
```

Health should describe operational readiness.

Not business correctness.

Platform health aggregates storage health.

It does not replace it.

---

# Capacity Monitoring

Storage capacity SHOULD remain continuously observable.

Examples include:

- PostgreSQL growth
- DuckDB growth
- Blob utilisation
- cache utilisation
- archive growth

Capacity trends frequently reveal architectural problems long before failures occur.

Storage growth should therefore become a first-class metric.

---

# Data Integrity

Storage observability SHOULD include integrity verification.

Examples include:

- checksum failures
- corruption detection
- archive validation
- blob verification
- migration verification

Integrity failures should always generate:

- logs
- metrics
- health updates

Information integrity is considerably more important than storage availability.

---

# Storage Performance

Performance telemetry SHOULD focus upon architectural responsibilities.

Examples.

PostgreSQL.

- transaction latency

DuckDB.

- analytical throughput

Blob Storage.

- streaming latency

MOS Cache.

- rebuild performance

Every storage engine should be measured according to the workload it was selected to perform.

---

# Recovery Observability

Recovery operations SHOULD expose:

- restore progress
- rebuild progress
- migration progress
- verification status

Operators should always understand:

> **Can the platform currently recover from failure?**

Recovery readiness is an operational capability.

It deserves direct visibility.

---

# Dependency Awareness

Storage observability should respect architectural ownership.

Example.

```mermaid
flowchart TD

N1["Blob Storage"]
N2["Unavailable"]
N3["Metadata Capability"]
N4["Degraded"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Storage failures naturally propagate through:

- repositories
- capabilities
- Runtime health

The dependency graph already models these relationships.

Observability should expose them.

---

# Cross-Storage Correlation

Operators should be able to correlate storage operations.

Example.

```mermaid
flowchart TD

N1["Playback Saved"]
N2["PostgreSQL"]
N3["Recommendation Updated"]
N4["DuckDB"]
N5["Cache Invalidated"]
N6["MOS Cache"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The complete storage journey should be visible through:

- traces
- logs
- metrics

Storage systems should not appear as isolated components.

---

# Storage Diagnostics

Diagnostic interfaces SHOULD expose:

- storage topology
- storage ownership
- repository mapping
- active migrations
- rebuild activity
- storage versions

The Runtime should explain:

> **Where is every category of information currently stored?**

Storage diagnostics should reinforce the Storage Taxonomy.

---

# Storage Dashboards

Operational dashboards SHOULD present storage according to information classes.

Preferred.

```text
Business State

Analytical State

Binary Assets

Derived Assets

Archive Data
```

Avoid dashboards organised solely by:

- database vendor
- implementation
- deployment

Operators should think about information.

Not technology.

---

# Alerting

Storage alerts SHOULD focus upon:

- business information risk
- corruption
- recovery failure
- replication failure
- storage exhaustion

Cache misses or analytical rebuilds should rarely generate critical alerts.

Business information always takes priority.

---

# Performance Cost

Storage telemetry SHOULD remain inexpensive.

Avoid:

- deep storage scans
- unnecessary integrity verification
- expensive aggregation

Observability should describe storage.

It should not become the largest storage workload.

---

# Anti-Patterns

The following practices are prohibited.

## SQL Metrics

Publishing metrics for individual SQL statements.

---

## Cache As Health

Treating cache misses as business failures.

---

## Storage Coupling

One storage engine exposing telemetry describing another storage engine.

---

## Missing Integrity

Ignoring corruption detection because storage appears available.

---

## Business Metrics

Using storage telemetry to describe business behaviour.

---

## Technology Dashboards

Organising operational dashboards around database products rather than information ownership.

---

# Mosaic Guidelines

Within Mosaic:

- Storage observability MUST follow information ownership.
- Every storage engine MUST expose health.
- Business information MUST receive the highest observability priority.
- Repository telemetry SHOULD remain storage independent.
- Storage lifecycle SHOULD remain observable.
- Integrity verification SHOULD remain visible.
- Storage dashboards SHOULD reinforce the Storage Taxonomy.
- Storage telemetry SHOULD complement Runtime telemetry.

---

# Relationship to MEG

Runtime Diagnostics explain:

> **How the Runtime is currently assembled.**

Storage Observability explains:

> **How every storage system supporting that Runtime is currently behaving.**

The next chapter introduces **Performance Telemetry**, defining how Mosaic measures latency, throughput, utilisation and efficiency across the entire platform while remaining independent of individual implementation details.

---

# Summary

Storage is not merely about persistence.

It is about preserving information throughout its entire lifecycle.

Within Mosaic, Storage Observability ensures that operators understand:

- what information exists
- where it is stored
- how efficiently it is managed
- whether it remains safe

The platform should never leave information architecture hidden behind database implementations.

Instead, storage should explain itself through the same architectural principles that govern every other part of the platform.
