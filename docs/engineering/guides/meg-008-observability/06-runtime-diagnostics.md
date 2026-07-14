<!--
File: docs/engineering/guides/meg-008-observability/06-runtime-diagnostics.md
Document: MEG-008
Status: Draft
Version: 0.1
-->

# Runtime Diagnostics

> *Health tells operators that something is wrong. Diagnostics explain the architecture behind the problem.*

---

# Purpose

Logs, metrics and traces explain Runtime behaviour.

Sometimes operators need something different.

They need to understand:

- what currently exists
- how the Runtime is assembled
- what dependencies are active
- which capabilities are loaded
- where work is executing

This is the purpose of **Runtime Diagnostics**.

Diagnostics expose the Runtime's internal architecture in a safe, observable and operationally useful manner.

---

# Philosophy

Within Mosaic:

> **The Runtime should always be able to explain itself.**

Operators should never need to:

- inspect memory
- attach debuggers
- read implementation code

to answer architectural questions.

The Runtime already possesses this information.

Diagnostics simply expose it.

---

# Diagnostics Are Not Logs

Logs describe:

> **What happened?**

Diagnostics describe:

> **What currently exists?**

Examples include:

- active capabilities
- worker pools
- dependency graph
- Runtime services
- storage providers

Diagnostics describe Runtime structure.

Not Runtime history.

---

# Diagnostic Hierarchy

Diagnostics naturally follow the Runtime Architecture.

```text
Platform

↓

Runtime

↓

Capabilities

↓

Storage

↓

Infrastructure
```

Each architectural layer should expose diagnostic information independently.

The Runtime becomes inspectable layer by layer.

---

# Runtime Inspection

The Runtime SHOULD expose:

- Runtime version
- startup time
- uptime
- lifecycle state
- Runtime Services
- dependency graph

Operators should immediately understand:

> **What Runtime am I operating?**

---

# Capability Inspection

Capability diagnostics SHOULD expose:

- identifier
- version
- lifecycle
- health
- permissions
- configuration schema
- dependencies
- provided contracts
- consumed contracts

Capabilities should become self-describing.

The Runtime already possesses this information through the Capability Registry.

Diagnostics simply expose it.

---

# Runtime Service Inspection

Every Runtime Service SHOULD expose:

- lifecycle
- health
- metrics
- configuration
- dependencies

Examples include:

```text
Scheduler
```

```text
Execution Engine
```

```text
Worker Manager
```

```text
Capability Registry
```

Operators should inspect Runtime Services individually.

Not only the platform as a whole.

---

# Dependency Graph

The Runtime SHOULD expose the complete dependency graph.

Example.

```text
Library

↓

Metadata

↓

Playback

↓

Recommendations
```

Likewise.

```text
Scheduler

↓

Execution Engine

↓

Worker Manager
```

The dependency graph should be:

- queryable
- visualisable
- exportable

Understanding Runtime dependencies should never require reading source code.

---

# Worker Inspection

The Worker Manager SHOULD expose:

- worker count
- worker state
- active executions
- worker utilisation
- idle workers
- failed workers

Operators should always understand:

> **What are my workers doing right now?**

---

# Scheduler Inspection

The Scheduler SHOULD expose:

- waiting schedules
- recurring schedules
- delayed work
- execution backlog

The Scheduler already understands time.

Diagnostics expose that understanding.

---

# Execution Inspection

The Execution Engine SHOULD expose:

- active Work Units
- queued work
- execution duration
- execution ownership
- cancellation state

Operators should answer:

> **What is executing right now?**

without examining logs.

---

# Storage Inspection

Storage diagnostics SHOULD expose:

- PostgreSQL status
- DuckDB status
- Blob Storage status
- MOS Cache
- MOS Archives

Examples include:

- utilisation
- migrations
- rebuild activity
- cache statistics

Storage diagnostics complement Storage Health.

They explain storage architecture.

Not merely storage readiness.

---

# Configuration Inspection

The Runtime SHOULD expose configuration metadata.

Examples include:

- Runtime configuration
- capability configuration
- manifest versions
- configuration sources

Sensitive values MUST remain redacted.

Diagnostics explain configuration.

They do not expose secrets.

---

# Event Inspection

The Runtime MAY expose Runtime Event diagnostics.

Examples include:

- published events
- subscribers
- dead letters
- retry queues

Operators should understand event topology.

Not merely event throughput.

---

# Resource Inspection

The Resource Manager SHOULD expose:

- CPU utilisation
- memory utilisation
- worker capacity
- connection pools
- storage utilisation

Resources should become visible through one architectural interface.

---

# Capability Graph

Beyond the dependency graph, the Runtime SHOULD expose the capability graph.

Example.

```text
Capability

↓

Contracts

↓

Events

↓

Dependencies

↓

Permissions
```

The capability graph becomes one of the platform's most valuable diagnostic artefacts.

It explains:

How the ecosystem is assembled.

---

# Runtime Snapshot

The Runtime SHOULD support diagnostic snapshots.

Example.

```text
Snapshot

↓

Runtime

↓

Capabilities

↓

Workers

↓

Storage

↓

Configuration
```

Snapshots should remain:

- read only
- deterministic
- inexpensive

Operators should capture Runtime state without disrupting execution.

---

# Diagnostic API

Diagnostics SHOULD be exposed through dedicated Runtime APIs.

Typical categories include:

```text
/runtime
```

```text
/capabilities
```

```text
/storage
```

```text
/workers
```

```text
/dependencies
```

Diagnostics should remain separate from business APIs.

The Runtime should expose architecture.

Capabilities expose business functionality.

---

# Runtime Explainability

A useful architectural principle is:

> **Every Runtime decision should have a corresponding diagnostic explanation.**

Example.

Question.

```
Why is Metadata inactive?
```

Diagnostics.

```
Dependency Missing

↓

TMDB Provider
```

The Runtime should explain itself naturally.

---

# Security

Diagnostic interfaces SHOULD respect Runtime permissions.

Examples include:

- administrator only
- read only
- capability scoped

Architecture visibility should never compromise platform security.

Detailed authorisation is defined in MEG-009.

---

# Performance

Diagnostics SHOULD remain lightweight.

Avoid:

- rebuilding dependency graphs
- expensive analytical queries
- deep storage scans

The Runtime already possesses most diagnostic information.

Diagnostics should simply expose it.

---

# Export

Diagnostic information SHOULD support export.

Examples include:

- JSON
- GraphViz
- Mermaid
- OpenTelemetry resources

Export enables:

- architecture documentation
- support bundles
- issue reporting
- automated analysis

One Runtime.

Many consumers.

---

# Testing

Diagnostic interfaces SHOULD be tested.

Typical tests verify:

- dependency graph
- capability inspection
- Runtime snapshot
- worker visibility
- configuration redaction

Diagnostics should remain predictable.

Operators should trust them.

---

# Anti-Patterns

The following practices are prohibited.

## Hidden Runtime State

Important Runtime information existing only in memory.

---

## Source Code Inspection

Requiring developers to inspect implementation to understand Runtime state.

---

## Diagnostic Side Effects

Diagnostic endpoints modifying Runtime behaviour.

---

## Sensitive Configuration

Exposing credentials through diagnostic APIs.

---

## Duplicate Diagnostics

Multiple Runtime Services exposing conflicting architectural information.

---

## Business APIs

Mixing Runtime diagnostics with capability business endpoints.

---

# Mosaic Guidelines

Within Mosaic:

- The Runtime SHOULD explain its own architecture.
- Diagnostic ownership MUST follow Runtime ownership.
- Dependency graphs SHOULD remain observable.
- Runtime snapshots SHOULD remain read only.
- Sensitive information MUST remain redacted.
- Diagnostics SHOULD remain lightweight.
- Diagnostic APIs MUST remain separate from business APIs.
- Operators SHOULD understand Runtime composition without reading implementation code.

---

# Relationship to MEG

The Health Model answers:

> **Can the platform operate?**

Runtime Diagnostics answer:

> **How is the platform currently constructed and why is it behaving this way?**

The next chapter introduces **Storage Observability**, defining how PostgreSQL, DuckDB, Blob Storage, MOS Archives and MOS Cache expose operational telemetry while preserving the architectural boundaries established in MEG-007.

---

# Summary

Diagnostics make the Runtime self-describing.

They expose:

- architecture
- dependencies
- composition
- execution
- configuration

rather than simply recording behaviour.

Within Mosaic, diagnostics transform the Runtime from a system that merely executes into one that can explain itself continuously.

That capability is one of the defining characteristics of a mature platform.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`05-health-model.md`

**Next File**

`07-storage-observability.md`
