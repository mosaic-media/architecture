<!--
File: docs/engineering/guides/meg-010-performance-engineering/03-capability-performance.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Capability Performance

---

# Purpose

This chapter defines how performance should be achieved within Mosaic Capabilities.

Capabilities represent the primary unit of business execution within the platform.

Their responsibility is to implement business behaviour, not to implement performance mechanisms.

Performance should therefore emerge from good capability design rather than from isolated optimisation efforts.

---

# Performance Objectives

Capabilities should be:

- lightweight
- predictable
- stateless where practical
- independently scalable
- observable
- composable

A capability should execute its responsibility efficiently without becoming responsible for the efficiency of the entire platform.

---

# Capability Responsibilities

Capabilities are responsible for:

- executing business logic
- validating requests
- coordinating repositories
- publishing events
- returning results

Capabilities are not responsible for:

- thread management
- scheduling
- caching infrastructure
- storage optimisation
- connection pooling
- worker management

Those responsibilities belong elsewhere within the architecture.

---

# Single Responsibility

Capabilities should perform one business responsibility well.

Large capabilities often become slow because they accumulate unrelated work.

When execution becomes increasingly complex, contributors should first ask:

> **Does this capability now have more than one responsibility?**

Splitting responsibilities usually improves both clarity and performance.

---

# Execution Scope

Capabilities should execute only the work required to satisfy the requested business operation.

Avoid:

- speculative work
- unnecessary lookups
- duplicate validation
- repeated repository access
- eager loading without purpose

Every additional operation increases latency.

Work that provides no business value is simply overhead with better marketing.

---

# Repository Usage

Capabilities should minimise repository interaction.

Preferred behaviour includes:

- requesting only required data
- batching related operations
- avoiding repeated queries
- avoiding unnecessary writes

Capabilities should never repeatedly query repositories for information they already own.

Every storage operation has a cost.

Treat it accordingly.

---

# Event Publishing

Capabilities should publish events only when meaningful business state changes occur.

Events should not be emitted:

- for logging
- for tracing
- for debugging
- for internal implementation details

Excessive event generation increases platform workload without increasing platform value.

An event should represent something the business actually cares about.

---

# Blocking Behaviour

Capabilities should avoid blocking operations wherever practical.

Long-running work should be:

- delegated
- scheduled
- executed asynchronously
- processed by background workers where appropriate

User-facing capabilities should complete their work as quickly as the business permits.

---

# Memory Behaviour

Capabilities should minimise unnecessary allocation.

Contributors should avoid:

- repeated object creation
- excessive copying
- large temporary collections
- retaining data beyond its useful lifetime

Ownership should move wherever practical rather than copying data repeatedly.

The cheapest allocation is the one that never occurs.

---

# Data Movement

Capabilities should minimise the amount of data transferred between layers.

Prefer:

- domain objects over generic structures
- focused DTOs
- explicit mappings
- small payloads

Avoid retrieving entire datasets when only a subset is required.

Moving data is work.

Moving unnecessary data is wasted work.

---

# Dependency Usage

Capabilities should depend only upon the interfaces required to complete their responsibility.

Excessive dependencies increase:

- execution cost
- testing complexity
- maintenance effort
- coupling

Smaller dependency graphs generally produce simpler execution paths.

---

# Latency Expectations

Capability execution should remain proportional to the business operation being performed.

Simple operations should remain simple.

Expensive operations should have obvious architectural justification.

Unexpected latency should always be investigated rather than accepted.

Slow capabilities tend to become slower over time unless deliberately managed.

---

# Scaling Characteristics

Capabilities should scale horizontally without requiring coordination with other capability instances.

They should avoid reliance upon:

- shared mutable state
- process-local assumptions
- execution ordering
- singleton business logic

A capability should behave identically regardless of how many instances are executing simultaneously.

---

# Observability

Capability execution should expose sufficient information to understand:

- execution duration
- success rate
- failure rate
- repository usage
- downstream dependencies
- event publication
- retry behaviour

Performance investigations should begin with evidence rather than intuition.

Observability provides that evidence.

---

# Optimisation Strategy

When improving capability performance, contributors should investigate in the following order:

1. Remove unnecessary work.
2. Reduce repository operations.
3. Reduce data movement.
4. Reduce blocking behaviour.
5. Simplify business flow.
6. Improve algorithms.
7. Consider caching where appropriate.

Low-level optimisation should be considered only after higher-level improvements have been exhausted.

Improving architecture usually produces larger gains than improving syntax.

---

# Anti-Patterns

The following behaviours are discouraged:

- capabilities that perform unrelated work
- multiple repository queries for identical data
- synchronous waiting on background processes
- emitting unnecessary events
- excessive dependency injection
- hidden storage access
- business logic driven by infrastructure concerns
- speculative optimisation without measurement

These patterns increase complexity while reducing performance and maintainability.

---

# Expected Outcome

After reading this chapter contributors should understand:

- how capabilities influence overall platform performance
- how capability boundaries affect latency
- how to minimise unnecessary work
- why repositories should be used deliberately
- why business execution should remain focused
- how observability supports optimisation

A performant capability is not one filled with clever code.

It is one that performs exactly the work the business requires, no more and no less.

---

# Next File

`04-repository-performance.md`
