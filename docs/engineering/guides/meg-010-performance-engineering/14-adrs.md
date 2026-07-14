<!--
File: docs/engineering/guides/meg-010-performance-engineering/14-adrs.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Architecture Decision Records

---

# Purpose

This chapter records the architectural decisions that define the performance engineering philosophy of the Mosaic platform.

Architecture Decision Records (ADRs) explain **why** significant decisions were made.

They provide historical context so future contributors understand the reasoning behind architectural choices rather than simply inheriting them.

A documented decision is easier to review, challenge and evolve than an undocumented assumption.

---

# ADR-001

## Title

Performance Is an Architectural Property

### Status

Accepted

### Decision

Performance shall be treated as a platform-wide architectural concern rather than a late-stage optimisation activity.

### Rationale

Performance is determined by:

- Runtime behaviour
- architectural boundaries
- storage design
- event flow
- scheduling
- memory ownership
- caching
- observability

Improving individual functions cannot compensate for poor architecture.

Performance must therefore be designed from the beginning.

---

# ADR-002

## Title

Measure Before Optimising

### Status

Accepted

### Decision

Performance work must be supported by measurable evidence.

### Rationale

Optimisation based upon assumptions frequently increases complexity while producing little measurable benefit.

Benchmarking and profiling should identify genuine bottlenecks before implementation changes are made.

Engineering decisions should be evidence-driven rather than intuition-driven.

---

# ADR-003

## Title

Reduce Work Before Accelerating Work

### Status

Accepted

### Decision

Contributors should remove unnecessary work before attempting to optimise existing work.

### Rationale

Eliminating unnecessary processing generally produces larger improvements than accelerating inefficient processing.

Preferred optimisation order:

1. Remove work.
2. Simplify execution.
3. Reduce data movement.
4. Reduce allocation.
5. Optimise implementation.

This approach preserves architectural simplicity while improving performance.

---

# ADR-004

## Title

Runtime Owns Execution

### Status

Accepted

### Decision

Scheduling, execution and concurrency remain Runtime responsibilities.

Capabilities must not implement their own execution policies.

### Rationale

Centralised execution management provides:

- predictable scheduling
- consistent fairness
- simpler optimisation
- unified observability
- controlled back-pressure

Separating execution from business logic improves both maintainability and performance.

---

# ADR-005

## Title

Repositories Own Storage Optimisation

### Status

Accepted

### Decision

Storage-specific optimisation shall remain inside repositories and storage adapters.

### Rationale

Capabilities should remain storage-agnostic.

Allowing storage implementation details to leak into higher architectural layers increases coupling and reduces long-term flexibility.

Repositories provide the appropriate abstraction boundary for performance improvements.

---

# ADR-006

## Title

Caching Is Optional

### Status

Accepted

### Decision

Caches are optimisation layers rather than sources of truth.

### Rationale

The platform must remain functionally correct when caches are empty or unavailable.

Cache failures should reduce performance rather than compromise correctness.

This keeps cache behaviour predictable and simplifies invalidation strategies.

---

# ADR-007

## Title

Back-Pressure Protects Platform Stability

### Status

Accepted

### Decision

The Runtime shall apply bounded back-pressure when workload exceeds processing capacity.

### Rationale

Unlimited queues and unlimited concurrency eventually produce instability.

Applying controlled back-pressure allows the platform to remain operational while preventing resource exhaustion.

Graceful degradation is preferable to catastrophic failure.

---

# ADR-008

## Title

Performance Must Remain Observable

### Status

Accepted

### Decision

Every significant Runtime component shall expose performance metrics.

### Rationale

Performance cannot be improved if it cannot be measured.

Observability allows contributors to:

- identify bottlenecks
- detect regressions
- validate optimisation
- understand workload behaviour

Measurement transforms optimisation from speculation into engineering.

---

# ADR-009

## Title

Memory Ownership Over Memory Tricks

### Status

Accepted

### Decision

The platform should optimise memory ownership before introducing advanced allocation techniques.

### Rationale

Reducing unnecessary allocation and copying usually provides greater benefit than introducing complex pooling or custom memory management.

Clear ownership also improves correctness and maintainability.

---

# ADR-010

## Title

Predictability Is More Valuable Than Peak Performance

### Status

Accepted

### Decision

The platform should favour stable, predictable behaviour over isolated benchmark victories.

### Rationale

Users experience consistency rather than benchmark scores.

Predictable latency, bounded memory usage and graceful degradation provide greater operational value than occasional exceptional performance under ideal conditions.

Engineering decisions should therefore optimise for sustained platform behaviour rather than isolated measurements.

---

# Decision Review

Architectural decisions should be reviewed when:

- significant workload characteristics change
- Runtime architecture evolves
- storage technologies change
- observability identifies systemic issues
- platform scaling assumptions change

Changes should be documented by introducing new ADRs or superseding existing ones rather than silently rewriting architectural history.

The goal is to preserve the reasoning behind the architecture, not merely its current implementation.

---

# Expected Outcome

After reading this chapter contributors should understand:

- why the major performance decisions were made
- how those decisions relate to the wider architecture
- when architectural decisions should be revisited
- why optimisation should remain consistent across the platform

ADRs preserve architectural intent.

Without them, future contributors are left to reconstruct design decisions from commit messages, half-remembered conversations and the archaeological layers of old pull requests. History suggests humans are remarkably optimistic about that working.

---

# Next File

`15-contributor-guidance.md`
