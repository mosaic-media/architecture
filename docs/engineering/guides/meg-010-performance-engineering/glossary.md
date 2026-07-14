<!--
File: docs/engineering/guides/meg-010-performance-engineering/glossary.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# Glossary

---

# Purpose

This glossary defines terminology used throughout MEG-010.

The definitions are specific to the Mosaic architecture and should be interpreted alongside previous MEG specifications.

---

## Allocation

The reservation of memory required to create new objects during execution.

---

## Back-Pressure

A Runtime mechanism that slows or limits incoming work when processing capacity is temporarily exceeded.

---

## Benchmark

A controlled measurement used to compare the performance characteristics of one implementation against another.

---

## Blocking Operation

An operation that prevents execution from progressing while waiting for another resource or process.

---

## Cache

A temporary storage layer used to avoid repeating expensive computation or data retrieval.

Caches are optimisation mechanisms rather than sources of truth.

---

## Capability

A self-contained unit of business behaviour executed by the Mosaic Runtime.

Defined in MEG-005.

---

## Concurrency

The ability for multiple independent units of work to make progress during overlapping periods of time.

---

## Contention

Competition between concurrent operations for the same resource.

---

## Critical Path

The sequence of operations that directly determines the latency of a request or workload.

---

## Event Throughput

The rate at which events are published, routed and processed throughout the Runtime.

---

## Garbage Collection

The automatic recovery of memory occupied by objects that are no longer reachable.

---

## Latency

The time required for an individual operation to complete.

Usually measured in milliseconds.

---

## Memory Ownership

The architectural concept that every allocation has a clearly defined owner and lifetime.

---

## Optimisation

A deliberate change intended to improve measurable performance while preserving architectural correctness.

---

## Predictability

The consistency of platform behaviour under varying workloads.

---

## Profiling

The process of measuring how execution time, memory and Runtime resources are actually consumed.

---

## Repository

The architectural boundary responsible for translating between the Domain and storage systems.

Defined in MEG-004.

---

## Runtime

The Mosaic execution engine responsible for scheduling, coordination and execution of work.

Defined in MEG-002.

---

## Scheduling

The process by which the Runtime determines when and where work executes.

---

## Throughput

The quantity of work completed within a given period of time.

Usually measured as operations or events per second.

---

## Workload

A collection of operations executed by the platform over a period of time.

Representative workloads should resemble real production behaviour.

---

# Next File

`refrences.md`
