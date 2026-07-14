<!--
File: docs/engineering/guides/meg-010-performance-engineering/08-memory-ownership.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Memory Ownership

---

# Purpose

This chapter defines how memory should be managed throughout the Mosaic platform.

Memory behaviour has a direct impact on latency, throughput and overall system stability.

Poor ownership leads to unnecessary allocation, excessive copying, unpredictable garbage collection and increased resource consumption.

Mosaic therefore treats memory ownership as an architectural concern rather than a low-level implementation detail.

---

# Memory Objectives

Memory usage should be:

- predictable
- efficient
- bounded
- observable
- ownership-driven
- proportional to workload

The platform should use memory deliberately rather than accumulating it incidentally.

---

# Ownership Philosophy

Memory should always have a clear owner.

Every allocation should answer three questions:

- Who owns it?
- How long is it needed?
- When can it be released?

If ownership is unclear, lifetime is usually unclear.

If lifetime is unclear, memory usage inevitably grows.

---

# Ownership Transfer

Where practical, ownership should move rather than data being copied.

Prefer:

- passing ownership
- immutable sharing
- lightweight references
- streaming data

Avoid repeatedly copying:

- aggregates
- collections
- payloads
- event data
- storage results

Moving ownership is generally cheaper than duplicating memory.

---

# Allocation Strategy

Allocations should occur only when necessary.

Contributors should minimise:

- temporary objects
- short-lived collections
- repeated allocation inside loops
- unnecessary object construction

Reducing allocation pressure improves both execution speed and garbage collection behaviour.

---

# Object Lifetime

Objects should exist only for as long as they provide value.

Short-lived objects should be released naturally.

Long-lived objects should exist only when justified by:

- caching
- configuration
- Runtime state
- shared immutable data

Retaining objects beyond their useful lifetime wastes memory and increases garbage collection overhead.

---

# Data Copying

Copying should be treated as a measurable cost.

Avoid copying data:

- between architectural layers
- between repositories
- between capabilities
- during event publication
- during serialization

Copies should occur only when:

- ownership changes require it
- isolation requires it
- mutation safety requires it

Every copy consumes memory bandwidth and CPU time.

---

# Collection Management

Collections should remain appropriately sized.

Avoid:

- unbounded slices
- oversized maps
- permanently growing buffers
- retaining unused capacity

Collections should grow only when workload requires it.

Memory retained "just in case" usually remains allocated "just because."

---

# Streaming

Large datasets should be streamed where practical.

Streaming reduces:

- peak memory usage
- allocation pressure
- processing latency

Streaming should be preferred over loading complete datasets into memory when consumers process data sequentially.

Not every workload needs to hold the entire world in RAM before making its first decision.

---

# Shared State

Shared mutable memory should be minimised.

Prefer:

- immutable data
- ownership transfer
- message passing
- isolated state

Shared mutable state increases:

- contention
- synchronisation overhead
- complexity
- performance variability

The fastest shared state is the one that no longer needs sharing.

---

# Memory Reuse

Memory reuse should be considered where profiling demonstrates meaningful allocation pressure.

Examples include:

- reusable buffers
- pooled objects
- serialization buffers

Reuse should improve performance without introducing:

- ownership confusion
- stale state
- hidden coupling

Reuse is an optimisation.

Correct ownership remains the priority.

---

# Garbage Collection

The Runtime should cooperate with Go's garbage collector rather than attempting to outsmart it.

Contributors should focus on reducing:

- unnecessary allocation
- unnecessary retention
- excessive copying

Manual optimisation should only occur when supported by profiling evidence.

The garbage collector is remarkably capable.

It only becomes unhappy when the application insists on manufacturing unnecessary work for it.

---

# Memory Metrics

Memory behaviour should expose metrics including:

- heap allocation
- allocation rate
- object count
- garbage collection frequency
- garbage collection duration
- retained heap size
- peak memory usage
- allocation hotspots

These metrics should integrate with the observability standards defined in MEG-008.

Memory optimisation should always be evidence-driven.

---

# Optimisation Strategy

When improving memory performance, contributors should investigate in the following order:

1. Remove unnecessary allocations.
2. Reduce unnecessary copying.
3. Shorten object lifetime.
4. Stream large datasets.
5. Reduce retained memory.
6. Reuse memory where appropriate.
7. Tune allocation-heavy code.

The objective is to reduce memory pressure rather than simply hiding it.

---

# Anti-Patterns

The following memory behaviours are discouraged:

- unnecessary object copying
- retaining large collections indefinitely
- loading complete datasets unnecessarily
- hidden global caches
- shared mutable structures
- unbounded buffers
- allocation-heavy loops
- speculative object creation
- premature pooling

These patterns increase memory consumption while making performance increasingly unpredictable.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how ownership affects memory performance
- why allocation should be deliberate
- how copying influences latency
- when streaming should be preferred
- why object lifetime matters
- how memory metrics support optimisation

Good memory management is rarely about clever tricks.

It is about ensuring every allocation has a clear owner, a clear purpose and a clear end.

---

# Next File

`09-caching-strategy.md`
