<!--
File: engineering/meg/MEG-001 Go Engineering Standards/12-performance.md
Document: MEG-001
Status: Draft
Version: 0.1
-->

# Performance

> *Performance is an architectural characteristic, not a coding style. Optimise systems by understanding them, not by guessing.*

---

# Purpose

Performance is an important quality attribute of every Mosaic service.

However, performance is not the primary objective.

Correctness always comes first.

Maintainability comes second.

Only once software is correct and maintainable should optimisation become a priority.

This document defines how performance should be approached throughout the Mosaic ecosystem.

---

# Philosophy

Within Mosaic:

> **Measure first. Optimise second.**

Performance work without measurements is engineering theatre.

Optimisations should be driven by:

- benchmarks
- profiling
- production telemetry
- evidence

Never by intuition alone.

---

# Performance Hierarchy

Performance decisions should follow the same order.

```
Correctness

↓

Readability

↓

Maintainability

↓

Measurement

↓

Optimisation
```

Optimising incorrect software simply produces incorrect software more quickly.

---

# Premature Optimisation

Premature optimisation is prohibited.

Engineers SHOULD NOT:

- introduce complexity for hypothetical gains
- sacrifice readability
- duplicate logic for tiny performance improvements
- rewrite stable code without evidence

Simple software is often surprisingly fast.

Optimisation should solve demonstrated bottlenecks.

Not imagined ones.

---

# Measure Everything

Before optimising, answer:

- What is slow?
- How slow is it?
- Why is it slow?
- What evidence exists?
- What is the expected improvement?

If these questions cannot be answered, optimisation should not begin.

---

# Profiling

Profiling SHOULD always precede optimisation.

The preferred workflow is:

```
Observe

↓

Profile

↓

Identify Bottleneck

↓

Optimise

↓

Benchmark

↓

Repeat
```

Go provides excellent profiling tools.

Examples include:

- CPU profiling
- Heap profiling
- Goroutine profiling
- Mutex profiling
- Block profiling

Profile first.

Guess later.

---

# Benchmark Before And After

Every meaningful optimisation SHOULD include benchmarks.

Example:

```text
Before

↓

Optimisation

↓

Benchmark

↓

Compare
```

An optimisation without measurable improvement should be reconsidered.

Benchmarks should demonstrate value.

Not merely existence.

---

# Allocations

Memory allocations are inexpensive.

Large numbers of unnecessary allocations are not.

Reducing allocations can significantly reduce garbage collection pressure.

However:

Readability remains more important than avoiding a single allocation.

Only optimise allocation-heavy paths identified through profiling.

---

# Escape Analysis

Go automatically determines whether values remain on the stack or escape to the heap.

Engineers SHOULD understand escape analysis.

They SHOULD NOT write unreadable code attempting to outsmart the compiler.

Escape analysis should be inspected using:

```
go build -gcflags="-m"
```

Only optimise escape behaviour when measurements demonstrate heap allocations are a bottleneck.  [oai_citation:0‡Golang Design](https://golang.design/under-the-hood/en/part5toolchain/ch15compile/escape/?utm_source=chatgpt.com)

---

# Prefer Values

Small immutable values SHOULD generally be passed by value.

Example:

```go
type Position struct {
    X int
    Y int
}
```

Returning values often allows the compiler to keep them on the stack.

Pointers should be introduced because ownership or mutation requires them.

Not because "objects should always be pointers."

---

# Slices

Slices are lightweight descriptors.

Engineers SHOULD:

- preallocate capacity when known
- reuse slices where practical
- avoid unnecessary copying

Example:

```go
items := make([]Item, 0, expected)
```

Preallocation should only be used when the approximate size is genuinely known.

Avoid arbitrary capacity guesses.

---

# Maps

Maps SHOULD be preallocated when expected size is known.

Example:

```go
cache := make(map[string]Media, expected)
```

This reduces internal resizing.

Again:

Estimate based on real knowledge.

Not speculation.

---

# Strings

Avoid unnecessary string construction.

Poor:

```go
result := a + b + c + d + e
```

Repeated concatenation within loops should generally use:

- `strings.Builder`
- `bytes.Buffer`

Appropriate buffering reduces temporary allocations.

---

# Buffers

Temporary buffers SHOULD be reused when profiling demonstrates significant allocation pressure.

Examples include:

- JSON encoding
- Media parsing
- Image processing
- Metadata ingestion

Simple code should always come first.

Pooling should only be introduced where evidence supports it.

---

# sync.Pool

`sync.Pool` is an advanced optimisation tool.

It SHOULD only be used when:

- temporary objects are allocated frequently
- profiling identifies allocation pressure
- reuse measurably reduces GC overhead

It SHOULD NOT become a general-purpose object cache.

Objects stored in a pool may be discarded during garbage collection, so correctness must never depend upon their continued existence.  [oai_citation:1‡Go](https://go.dev/wiki/Performance?utm_source=chatgpt.com)

---

# Avoid Reflection

Reflection introduces:

- allocations
- complexity
- reduced compile-time guarantees
- slower execution

Reflection SHOULD be avoided within performance-critical paths.

Code generation or explicit implementations are generally preferable.

---

# Avoid unsafe

The `unsafe` package SHOULD NOT be used.

Exceptions require:

- measurable performance justification
- architectural review
- comprehensive testing
- clear documentation

Breaking Go's safety guarantees is a significant architectural decision.

Not an optimisation technique.

---

# Database Performance

Performance problems should rarely be solved inside Go first.

Instead examine:

- indexes
- query plans
- batching
- pagination
- network latency

A poor SQL query cannot be fixed through clever Go code.

---

# Network Performance

Network performance is usually dominated by latency rather than CPU.

Prefer:

- batching
- caching
- compression
- connection reuse

before attempting micro-optimisations.

---

# Concurrency

Concurrency is not automatically a performance optimisation.

Poor:

```
Sequential

↓

Concurrent

↓

Wait
```

Nothing has improved.

Concurrency should reduce waiting.

Not merely increase goroutine count.

---

# Garbage Collection

The Go garbage collector is highly optimised.

Engineers SHOULD trust it.

Avoid:

- manual memory management patterns
- premature pooling
- complicated allocation avoidance

Reduce allocation pressure only where profiling identifies GC as a bottleneck.

---

# Caching

Caching should improve overall system performance.

Caching should never hide poor architecture.

Before introducing a cache ask:

- What invalidates it?
- Who owns it?
- How is freshness guaranteed?
- Can correctness be affected?

An incorrect cache is worse than no cache.

---

# Observability

Performance cannot be improved if it cannot be observed.

Every production service SHOULD expose:

- latency
- throughput
- allocation rate
- goroutine count
- memory usage
- request duration

Operational metrics should identify regressions before users do.

---

# Performance Reviews

Every significant optimisation SHOULD answer:

- What was measured?
- What changed?
- Why did it improve?
- How much faster is it?
- Was readability affected?

If the improvement cannot be demonstrated objectively, it should be reconsidered.

---

# Anti-Patterns

The following practices are prohibited.

## Optimising Without Profiling

```
"I think this is slow."
```

---

## Premature sync.Pool

Using pooling before allocation pressure exists.

---

## Excessive Pointer Usage

Returning pointers simply because "Go passes everything by reference."

---

## Reflection For Convenience

Reflection replacing explicit code without measurable benefit.

---

## Using unsafe

Breaking type safety to save hypothetical nanoseconds.

---

## Benchmarking Unrealistic Workloads

Benchmarks should represent production behaviour.

Synthetic numbers without context are misleading.

---

# Mosaic Guidelines

Within Mosaic:

- Correctness MUST precede optimisation.
- Profiling MUST precede optimisation.
- Benchmarks SHOULD accompany significant performance work.
- Escape analysis SHOULD inform optimisation decisions.
- `sync.Pool` SHOULD only be introduced after profiling.
- Reflection SHOULD be avoided in hot paths.
- `unsafe` requires architectural approval.
- Production services SHOULD expose performance metrics.

---

# Summary

Performance is the result of good architecture.

It is rarely the result of clever code.

Within Mosaic, engineers optimise by:

- measuring first
- understanding bottlenecks
- improving architecture
- validating improvements
- preserving readability

Fast software is valuable.

Understandable fast software is considerably more valuable.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`11-testing.md`

**Next File**

`13-design-patterns.md`
