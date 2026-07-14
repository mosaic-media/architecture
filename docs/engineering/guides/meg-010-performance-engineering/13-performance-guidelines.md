<!--
File: docs/engineering/guides/meg-010-performance-engineering/13-performance-guidelines.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Performance Guidelines

---

# Purpose

This chapter provides practical engineering guidance for maintaining performance throughout the Mosaic platform.

The previous chapters explain the principles of performance engineering.

This chapter translates those principles into everyday engineering practices that contributors should apply during design, implementation, review and maintenance.

These guidelines are intended to prevent performance regressions before they occur rather than correcting them afterwards.

---

# Guiding Principle

Performance should emerge naturally from good engineering.

Contributors should not think:

> "How do I make this code faster?"

Instead, they should ask:

> "How do I reduce the amount of work this system performs?"

Removing unnecessary work almost always produces larger improvements than performing unnecessary work more efficiently.

---

# Design Guidelines

When designing new capabilities or services, contributors should:

- minimise responsibilities
- minimise dependencies
- minimise data movement
- minimise coordination
- minimise storage access

Simple designs generally produce simpler execution paths.

Simple execution paths are usually easier to optimise.

---

# Runtime Guidelines

Contributors should:

- prefer asynchronous execution where appropriate
- avoid blocking operations
- keep foreground work short-lived
- delegate long-running work
- respect Runtime ownership

Capabilities should never attempt to optimise the scheduler by implementing their own scheduling behaviour.

The Runtime already has that responsibility.

---

# Repository Guidelines

Repositories should:

- retrieve only required data
- minimise storage round trips
- avoid repeated queries
- keep transactions short
- expose measurable behaviour

Storage performance should improve because repositories request less work, not because storage engines are forced to work harder.

---

# Event Guidelines

Events should:

- represent meaningful business changes
- remain small
- avoid duplicated information
- avoid excessive fan-out
- remain independently consumable

Publishing more events than necessary increases workload across the entire platform.

Every consumer pays for every unnecessary event.

---

# Memory Guidelines

Contributors should:

- minimise allocation
- minimise copying
- avoid retaining unnecessary objects
- stream large datasets where practical
- prefer ownership transfer

Memory should be treated as a finite resource rather than an infinite convenience.

---

# Cache Guidelines

Caches should:

- have explicit ownership
- have bounded lifetime
- expose measurable effectiveness
- support deterministic invalidation
- remain optional

If removing a cache breaks correctness, the cache has become part of the architecture rather than an optimisation.

That should be treated as a design issue.

---

# Concurrency Guidelines

Concurrency should only be introduced when it provides measurable benefit.

Contributors should avoid:

- unnecessary goroutines
- unnecessary synchronisation
- speculative parallelism
- shared mutable state

More concurrency does not automatically produce more throughput.

It frequently produces more scheduling overhead instead.

---

# Measurement Guidelines

Before introducing an optimisation, contributors should:

- establish a baseline
- identify the bottleneck
- collect measurements
- define success criteria

After implementation they should:

- benchmark the change
- profile the change
- validate behaviour under representative workloads
- confirm that maintainability has not been compromised

Performance improvements should always be demonstrable.

---

# Review Guidelines

Performance should be considered during every code review.

Reviewers should consider:

- unnecessary allocations
- unnecessary copying
- repeated repository access
- blocking behaviour
- event volume
- cache usage
- concurrency decisions

Performance review is not reserved for specialist contributors.

It is part of normal engineering review.

---

# Scalability Guidelines

Contributors should design for predictable growth.

Systems should scale by:

- distributing work
- reducing coordination
- reducing contention
- reducing unnecessary storage operations
- reducing duplicated processing

Scaling should not depend upon increasingly powerful hardware alone.

Good architecture usually scales more effectively than expensive infrastructure.

---

# Operational Guidelines

Performance should remain observable in production.

Operational monitoring should include:

- latency
- throughput
- queue depth
- worker utilisation
- memory usage
- allocation rate
- storage latency
- cache effectiveness
- event throughput

Performance that cannot be observed cannot be improved with confidence.

---

# Continuous Improvement

Performance engineering is an ongoing activity.

Contributors should regularly:

- review benchmarks
- compare profiles
- investigate regressions
- simplify implementations
- remove unnecessary work

Optimisation should become part of normal platform evolution rather than an emergency activity performed shortly before release.

---

# Performance Checklist

Before merging significant changes, contributors should ask:

- Is this work necessary?
- Can this perform less work?
- Can data movement be reduced?
- Can storage operations be reduced?
- Can allocation be reduced?
- Is concurrency justified?
- Is caching necessary?
- Can this be measured?
- Can this be observed?
- Does this remain architecturally consistent?

A "yes" to every optimisation opportunity is not the goal.

A well-reasoned answer is.

---

# Anti-Patterns

The following engineering behaviours are discouraged:

- optimising before measuring
- sacrificing readability for minor gains
- introducing complexity without evidence
- optimising synthetic workloads
- hiding inefficiencies behind caches
- treating benchmarks as production truth
- ignoring observability
- allowing performance regressions to accumulate

Performance debt behaves much like technical debt.

It compounds quietly until it suddenly becomes everyone's problem.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how performance principles apply to everyday engineering
- how to identify unnecessary work
- how to review changes with performance in mind
- why optimisation should remain evidence-driven
- how observability supports continuous improvement
- how architectural consistency protects long-term performance

Performance should become a natural consequence of good engineering practice rather than a specialised activity performed only when something becomes painfully slow.

---

# Next File

`14-adrs.md`
