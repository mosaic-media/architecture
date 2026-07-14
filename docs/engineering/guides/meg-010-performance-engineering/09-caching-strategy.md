<!--
File: docs/engineering/guides/meg-010-performance-engineering/09-caching-strategy.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Caching Strategy

---

# Purpose

This chapter defines how caching should be used throughout the Mosaic platform.

Caching exists to reduce unnecessary work.

It is not intended to compensate for poor architecture, inefficient repositories or excessive storage access.

A well-designed cache improves responsiveness by avoiding repeated computation and repeated retrieval of data that has not changed.

---

# Caching Objectives

Caching should be:

- deliberate
- measurable
- predictable
- bounded
- observable
- disposable

The platform should remain correct even when every cache is empty.

Caches improve performance.

They must never become a dependency for correctness.

---

# Caching Philosophy

Caches are an optimisation layer.

They are not a source of truth.

The authoritative source for any piece of information remains:

- the Domain
- persistent storage
- external systems of record

Cached data is always a temporary representation.

If a cache disappears, the platform should continue operating correctly, albeit more slowly.

---

# Cache Ownership

Every cache must have a clearly defined owner.

The owner is responsible for:

- populating entries
- invalidating entries
- defining expiration
- monitoring effectiveness

Shared ownership leads to inconsistent invalidation.

Inconsistent invalidation leads to stale data.

Stale data leads to very uncomfortable conversations with users.

---

# What Should Be Cached

Caching is appropriate for data that is:

- expensive to retrieve
- expensive to compute
- frequently accessed
- relatively stable
- inexpensive to invalidate

Examples include:

- metadata
- configuration
- capability discovery
- extension manifests
- external API responses
- computed read models

Caching should be driven by workload rather than convenience.

---

# What Should Not Be Cached

The following should generally not be cached:

- rapidly changing state
- security decisions
- authorisation results
- transactional state
- write operations
- mutable aggregates

Caching volatile information often introduces more complexity than performance benefit.

---

# Cache Scope

Caches should exist at the smallest appropriate scope.

Typical scopes include:

- request
- capability
- process
- distributed platform

Smaller caches are generally:

- easier to invalidate
- easier to understand
- cheaper to maintain

Global caches should only exist when justified by workload.

---

# Expiration

Every cache should have an explicit expiration strategy.

Common strategies include:

- time-to-live
- event-driven invalidation
- version changes
- manual invalidation
- dependency invalidation

Caches should never exist indefinitely without deliberate justification.

Forever is rarely an acceptable cache duration.

---

# Invalidation

Invalidation is part of cache design.

It is not an afterthought.

Cache invalidation should occur when:

- business state changes
- source data changes
- configuration changes
- capabilities are updated
- extensions are installed or removed

Invalidation should be deterministic wherever possible.

Guessing whether cached data is still valid is not an engineering strategy.

---

# Cache Population

Caches should generally be populated:

- lazily
- on demand
- through predictable background processes

Avoid eagerly caching information that may never be used.

Unused cached data consumes resources without improving performance.

---

# Cache Consistency

Different caches may require different consistency models.

Examples include:

- strongly consistent
- eventually consistent
- best-effort
- immutable

The required consistency level should be determined by business requirements rather than implementation preference.

Not every cache needs to be perfectly fresh.

Not every cache is allowed to be stale.

---

# Cache Size

Caches should remain bounded.

Boundaries may be based on:

- entry count
- memory usage
- storage size
- lifetime

Unbounded caches eventually become memory leaks with marketing material.

---

# Cache Metrics

Caching systems should expose metrics including:

- hit rate
- miss rate
- eviction count
- expiration count
- invalidation count
- cache size
- lookup latency
- population duration

These metrics should integrate with the observability standards defined in MEG-008.

A cache that cannot be measured cannot be evaluated.

---

# Optimisation Strategy

When improving cache performance, contributors should investigate in the following order:

1. Determine whether caching is necessary.
2. Reduce unnecessary cache entries.
3. Improve invalidation behaviour.
4. Reduce cache lookup overhead.
5. Improve population efficiency.
6. Adjust expiration strategy.
7. Tune cache implementation.

Adding another cache should be considered only after understanding why the previous cache was insufficient.

---

# Anti-Patterns

The following caching behaviours are discouraged:

- caching everything
- unbounded caches
- stale cache ownership
- hidden cache dependencies
- duplicated caches
- caching mutable business state
- permanent cache entries
- cache invalidation by manual restart
- using caches to hide inefficient repositories

These behaviours increase complexity while reducing predictability and correctness.

---

# Expected Outcome

After reading this chapter contributors should understand:

- when caching should be used
- what information is suitable for caching
- why ownership matters
- how invalidation affects correctness
- why cache scope should remain small
- how cache metrics support optimisation

A good cache quietly removes unnecessary work.

A bad cache quietly creates unnecessary bugs.

---

# Next File

`10-back-pressure.md`
