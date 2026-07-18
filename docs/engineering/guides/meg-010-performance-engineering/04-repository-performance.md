<!--
File: docs/engineering/guides/meg-010-performance-engineering/04-repository-performance.md
Document: MEG-010
Status: Draft
-->

# Repository Performance

---

# Purpose

This chapter defines how repositories should contribute to the overall performance of the Mosaic platform.

Repositories form the boundary between the Domain and storage systems.

They are responsible for efficient data access without exposing storage implementation details to the rest of the platform.

Poor repository design frequently becomes the largest source of application latency.

For this reason, repository performance is considered an architectural concern rather than a database concern.

---

# Repository Objectives

Repositories should be:

- efficient
- predictable
- storage-agnostic
- observable
- composable
- narrowly focused

Repositories should retrieve and persist information.

They should not implement business logic.

---

# Repository Responsibilities

Repositories are responsible for:

- retrieving aggregates
- persisting aggregates
- executing storage operations
- translating storage models
- exposing storage failures

Repositories are not responsible for:

- business decisions
- validation
- orchestration
- caching policy
- event publication
- runtime scheduling

Keeping repositories narrowly focused makes both performance and correctness easier to maintain.

---

# Data Access Philosophy

Repositories should retrieve only the information required by the caller.

Avoid:

- loading entire aggregates unnecessarily
- selecting unused columns
- eager loading unrelated relationships
- retrieving data "just in case"

Every byte retrieved has a cost.

Every unnecessary query increases latency.

---

# Query Efficiency

Queries should be designed to minimise:

- execution time
- network traffic
- storage workload
- memory allocation

Repositories should favour:

- indexed lookups
- bounded result sets
- targeted projections
- efficient filtering

Repository performance begins with asking for less.

---

# Round Trips

Repository interactions should minimise storage round trips.

Prefer:

- batching related operations
- retrieving related data together when appropriate
- combining compatible writes

Avoid repetitive query patterns that repeatedly request information already available.

Multiple small queries are not automatically better than one well-designed query.

Likewise, one enormous query is rarely a badge of engineering excellence.

---

# Aggregate Loading

Repositories should load complete aggregates only when business behaviour requires them.

Where appropriate, repositories may expose:

- summaries
- projections
- read models
- lightweight DTOs

Loading complete object graphs unnecessarily wastes both storage and memory resources.

---

# Write Behaviour

Write operations should:

- modify only necessary data
- avoid redundant updates
- minimise transaction duration
- complete as quickly as possible

Long-running transactions increase contention throughout the storage system.

Repositories should therefore keep transactional work focused and predictable.

---

# Storage Independence

Performance improvements should not leak storage implementation into the Domain.

Capabilities should remain unaware of:

- indexes
- SQL structure
- storage engine features
- database-specific optimisations

Repositories may evolve internally without affecting higher architectural layers.

This separation preserves both flexibility and maintainability.

---

# Concurrency

Repositories should support concurrent access safely.

Repository implementations should avoid:

- unnecessary locking
- global mutable state
- shared in-memory caches
- hidden synchronisation

Concurrency should be delegated to the storage engine wherever practical.

The database usually understands its own consistency model better than application code pretending to be one.

---

# Memory Behaviour

Repositories should avoid excessive allocation.

Prefer:

- streaming large datasets where appropriate
- bounded collections
- efficient mapping
- ownership transfer over copying

Large result sets should be handled deliberately rather than loaded indiscriminately into memory.

---

# Error Handling

Repository failures should expose useful context without leaking storage implementation details.

Errors should identify:

- operation
- repository
- failure category

Errors should not expose:

- raw SQL
- connection details
- storage internals

Performance investigations should remain possible without sacrificing abstraction.

---

# Observability

Repository performance should expose metrics including:

- query duration
- transaction duration
- read count
- write count
- error rate
- retry count
- connection utilisation

These metrics should integrate with the observability standards defined in [MEG-008](../meg-008-observability/index.md).

Repositories should never become invisible performance bottlenecks.

---

# Optimisation Strategy

When improving repository performance, contributors should investigate in the following order:

1. Remove unnecessary queries.
2. Reduce retrieved data.
3. Improve query structure.
4. Reduce transaction duration.
5. Improve indexing.
6. Batch related operations.
7. Optimise storage-specific behaviour.

Repository optimisation should begin with reducing work rather than accelerating waste.

---

# Anti-Patterns

The following repository behaviours are discouraged:

- N+1 query patterns
- loading entire tables unnecessarily
- hidden business logic
- excessive transactions
- storage-specific leakage
- repeated identical queries
- unbounded result sets
- unnecessary data copying
- long-lived transactions

These behaviours increase latency, reduce scalability and complicate future optimisation efforts.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how repositories affect overall platform performance
- why repository boundaries matter
- how to minimise storage workload
- how to reduce unnecessary data movement
- why abstraction should not be sacrificed for speed
- how repository metrics support optimisation

A good repository performs the smallest amount of storage work necessary to satisfy the Domain.

Anything more is simply making the database work overtime for no business benefit.
