<!--
File: docs/engineering/guides/meg-010-performance-engineering/05-storage-performance.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Storage Performance

---

# Purpose

This chapter defines how storage systems should contribute to the overall performance of the Mosaic platform.

Storage is frequently the slowest component involved in a business operation.

Every unnecessary read, write and transaction increases latency throughout the platform.

Storage performance is therefore achieved by reducing unnecessary work before attempting to make storage engines themselves faster.

---

# Storage Objectives

Storage should be:

- predictable
- efficient
- scalable
- observable
- resilient
- appropriately specialised

Different storage technologies exist because different workloads have different characteristics.

Mosaic embraces specialised storage engines while ensuring that the rest of the platform remains storage-agnostic.

---

# Storage Responsibilities

Storage systems are responsible for:

- durable persistence
- efficient retrieval
- transactional consistency
- indexing
- query execution
- concurrency management

Storage systems are not responsible for:

- business behaviour
- orchestration
- workflow decisions
- capability execution
- event processing

The closer storage remains to its intended purpose, the easier it becomes to optimise.

---

# Storage Selection

Storage technology should be selected according to workload characteristics rather than popularity.

Selection criteria include:

- access patterns
- consistency requirements
- latency expectations
- throughput requirements
- query complexity
- operational overhead

A storage engine should solve the problem it was designed for.

Using every database because it looked impressive in a conference talk is not considered architecture.

---

# Data Locality

Performance improves when related data is stored close to where it is consumed.

Contributors should minimise:

- unnecessary cross-storage lookups
- repeated remote requests
- fragmented ownership
- unnecessary joins across systems

Moving computation towards data is often cheaper than moving data towards computation.

---

# Read Performance

Read operations should prioritise:

- indexed access
- targeted retrieval
- bounded result sets
- projection where appropriate

Avoid:

- table scans without justification
- retrieving unused columns
- unnecessarily large object graphs
- repeated identical lookups

Read performance begins with asking smaller questions.

---

# Write Performance

Write operations should:

- update only necessary fields
- minimise transaction duration
- batch compatible writes
- avoid unnecessary persistence

Repeated writes for unchanged data should be avoided wherever practical.

Storage should not be asked to confirm what is already known.

---

# Transactions

Transactions should be:

- short-lived
- focused
- predictable
- bounded

Long-running transactions increase:

- contention
- lock duration
- retry frequency
- latency

Repositories should complete transactional work as quickly as possible.

---

# Indexing

Indexes exist to accelerate common access patterns.

Indexes should be:

- deliberate
- measurable
- workload-driven

Excessive indexing increases:

- storage overhead
- write latency
- maintenance complexity

Every index carries both a benefit and a cost.

Both should be understood before introducing one.

---

# Storage Communication

Communication with storage systems should minimise:

- network round trips
- protocol overhead
- repeated authentication
- unnecessary serialization

Efficient communication often produces larger gains than query optimisation alone.

---

# Storage Isolation

Capabilities should never rely upon storage-specific behaviour.

They should remain unaware of:

- SQL dialects
- index hints
- execution plans
- storage engine features

Storage optimisation belongs inside repository implementations and storage adapters.

Architectural boundaries remain more valuable than isolated performance gains.

---

# Scaling Storage

Storage scalability should prioritise:

- reducing unnecessary load
- efficient indexing
- workload distribution
- horizontal partitioning where appropriate
- caching frequently accessed data

Scaling should not become an excuse for inefficient queries.

Buying larger hardware to compensate for poor design is surprisingly common.

It is rarely elegant.

---

# Storage Metrics

Storage systems should expose metrics including:

- read latency
- write latency
- transaction duration
- connection utilisation
- query frequency
- index utilisation
- lock contention
- retry rates
- storage capacity

These metrics should integrate with the observability standards defined in MEG-008.

Storage performance should never rely upon assumptions.

---

# Optimisation Strategy

When improving storage performance, contributors should investigate in the following order:

1. Remove unnecessary storage operations.
2. Reduce transferred data.
3. Improve indexing.
4. Reduce transaction duration.
5. Batch compatible operations.
6. Reduce network overhead.
7. Tune storage-engine-specific behaviour.

The objective is to reduce work before accelerating work.

---

# Anti-Patterns

The following storage behaviours are discouraged:

- unnecessary full table scans
- excessive indexing
- repeated identical writes
- oversized transactions
- storage-specific Domain logic
- unbounded result sets
- excessive storage round trips
- duplicated persistence

These behaviours reduce scalability while increasing operational complexity.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how storage influences platform performance
- why workload determines storage selection
- how efficient reads and writes reduce latency
- why transactions should remain small
- how indexing should be applied deliberately
- how storage metrics support optimisation

Good storage performance is achieved by asking storage systems to perform only the work that genuinely needs to be durable.

Everything else belongs elsewhere in the architecture.

---

# Next File

`06-event-throughput.md`
