<!--
File: docs/engineering/guides/meg-010-performance-engineering/references.md
Document: MEG-010
Status: Draft
Version: 0.1
-->

# References

---

# Purpose

This document lists the primary references that informed the architectural principles described in MEG-010.

The intention is not to mandate specific technologies or implementations, but to acknowledge the engineering literature and platform documentation that influenced the design of Mosaic's performance philosophy.

---

# Internal References

## MEG-001 — Go Engineering Standards

Defines engineering practices and coding standards used throughout the platform.

---

## MEG-002 — Reactive Runtime

Defines the Runtime execution model, scheduling philosophy and event-driven architecture.

---

## MEG-003 — Domain-Driven Design

Defines Domain boundaries, aggregates and business ownership.

---

## MEG-004 — Hexagonal Architecture

Defines architectural boundaries, repositories and dependency direction.

---

## MEG-005 — Capability Runtime

Defines capabilities as the primary unit of business execution.

---

## MEG-006 — Extension Platform

Defines extension execution, lifecycle and Runtime integration.

---

## MEG-007 — Storage Architecture

Defines storage responsibilities, repository interaction and persistence strategy.

---

## MEG-008 — Observability

Defines logging, metrics, tracing and operational monitoring.

---

## MEG-009 — Security Architecture

Defines platform security principles that performance optimisations must preserve.

---

# External References

## Go Project Documentation

https://go.dev/doc/

Official documentation covering the Go language, runtime, concurrency model and performance guidance.

---

## Effective Go

https://go.dev/doc/effective_go

Guidance on writing clear, idiomatic and maintainable Go code.

---

## Go Memory Model

https://go.dev/ref/mem

Defines the guarantees provided by Go's concurrency and memory model.

---

## Go Performance Wiki

https://go.dev/wiki/Performance

General guidance on benchmarking, profiling and optimisation.

---

## Go Testing Package

https://pkg.go.dev/testing

Documentation for Go's benchmarking framework.

---

## Go pprof

https://pkg.go.dev/runtime/pprof

Documentation covering CPU, memory and execution profiling.

---

## OpenTelemetry

https://opentelemetry.io/

Industry-standard observability framework referenced throughout the Mosaic architecture.

---

## Martin Fowler

https://martinfowler.com/

Reference material covering architecture, refactoring, performance trade-offs and software design.

---

## Eric Evans

*Domain-Driven Design: Tackling Complexity in the Heart of Software*

Referenced for architectural boundaries and domain ownership.

---

## Vaughn Vernon

*Implementing Domain-Driven Design*

Referenced for aggregate design and repository patterns.

---

## Michael Nygard

*Release It!*

Referenced for resilience, operational stability and graceful degradation.

---

## Brendan Gregg

*Systems Performance*

Referenced for performance analysis, profiling and systems engineering practices.

---

## Google Site Reliability Engineering

https://sre.google/books/

Referenced for operational performance, scalability and reliability principles.

---

# Engineering Principle

MEG-010 intentionally favours architectural simplicity over platform-specific optimisation techniques.

Contributors should use measurements, profiling and architectural reasoning to guide performance work rather than relying on folklore or anecdotal "best practices."

---

# Final Statement

Performance within Mosaic is not achieved through isolated optimisation.

It emerges from thousands of small engineering decisions that collectively reduce unnecessary work while preserving correctness, observability and architectural clarity.

The goal is not to build the fastest possible system.

The goal is to build a system that remains fast as it continues to evolve.

Those are very different achievements.

One wins benchmark competitions.

The other survives real users.

---

# Completion

This concludes **MEG-010 — Performance Engineering**.

The principles defined throughout this specification establish how Mosaic should remain efficient, responsive and scalable without compromising the architectural foundations established by previous MEGs.

Subsequent specifications build upon these principles rather than replacing them.
