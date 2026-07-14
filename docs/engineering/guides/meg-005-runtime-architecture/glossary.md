<!--
File: engineering/meg/MEG-005 Runtime Architecture/glossary.md
Document: MEG-005
Status: Draft
Version: 0.1
-->

# Glossary

> *The Runtime should describe itself using one consistent architectural vocabulary.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Runtime Architecture.

The definitions contained within this document establish the canonical Runtime vocabulary for:

- Architecture Specifications
- ADRs
- Runtime Documentation
- Source Code
- Contributor Guides
- Extension SDKs

Where a term has a specific meaning within the Runtime, that definition takes precedence over informal usage.

---

# B

## Bootstrap

The initial process responsible for constructing the Runtime.

Bootstrap performs:

- configuration loading
- Runtime Kernel construction
- Runtime Service construction

Bootstrap ends once the Runtime becomes operational.

---

# C

## Capability

A self-contained unit of business functionality executed by the Runtime.

Examples include:

- Playback
- Library
- Metadata
- Recommendations

Capabilities own business behaviour.

The Runtime owns execution.

---

## Capability Registry

The Runtime Service responsible for discovering, registering and exposing capabilities.

The Capability Registry maintains:

- capability metadata
- lifecycle
- dependencies
- health

It is the Runtime's authoritative source of capability information.

---

## Composition

The process of assembling Runtime Services, Adapters and Capabilities into a functioning Runtime.

Composition occurs inside the Composition Root.

---

# D

## Dependency Graph

The directed acyclic graph describing Runtime component dependencies.

The Dependency Graph determines:

- startup order
- shutdown order
- dependency validation

It is constructed before execution begins.

---

# E

## Execution Engine

The Runtime Service responsible for coordinating executable Work Units.

The Execution Engine:

- dispatches work
- tracks execution
- coordinates workers

It does not execute business behaviour itself.

---

# H

## Health

The operational readiness of a Runtime component.

Examples include:

```
Healthy
```

```
Degraded
```

```
Unavailable
```

Health describes operational capability.

Not business correctness.

---

# K

## Kernel

The central coordinating component of the Runtime.

The Runtime Kernel owns:

- lifecycle
- Runtime Services
- startup
- shutdown

It intentionally owns no business behaviour.

The Runtime Kernel resembles a microkernel by keeping only essential coordination responsibilities while delegating execution to specialised services.  [oai_citation:0‡AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html?utm_source=chatgpt.com)

---

# L

## Lifecycle

The sequence of operational states followed by every Runtime Service.

Examples include:

- Created
- Ready
- Running
- Stopping
- Disposed

Lifecycle ownership belongs to the Runtime Kernel.

---

# R

## Resource Manager

The Runtime Service responsible for managing shared Runtime resources.

Examples include:

- worker capacity
- connection pools
- memory budgets

Business capabilities consume resources.

The Runtime owns them.

---

## Runtime

The execution platform responsible for coordinating capabilities.

The Runtime owns:

- execution
- scheduling
- workers
- lifecycle
- resources

It intentionally owns no business behaviour.

---

## Runtime Kernel

The architectural centre of the Runtime.

Every Runtime Service is coordinated through the Runtime Kernel.

It should remain:

- small
- stable
- business agnostic

---

## Runtime Service

A modular component providing one Runtime responsibility.

Examples include:

- Scheduler
- Worker Manager
- Execution Engine
- Capability Registry

Runtime Services cooperate through explicit contracts.

---

## Runtime State

Operational information describing the Runtime.

Examples include:

- queue depth
- worker utilisation
- capability lifecycle

Runtime State is distinct from business state.

---

# S

## Scheduler

The Runtime Service responsible for determining when Work Units become executable.

The Scheduler owns:

- delayed execution
- recurring execution
- execution timing

It never executes work directly.

---

## Startup

The deterministic process through which the Runtime becomes operational.

Startup consists of:

- configuration
- dependency validation
- Runtime initialisation
- capability activation

---

## Shutdown

The controlled transition from a running Runtime to a fully stopped Runtime.

Shutdown includes:

- cooldown
- draining
- resource release
- service disposal

Graceful shutdown preserves business correctness.

---

# W

## Work Unit

The smallest executable Runtime operation.

Examples include:

- scheduled capability execution
- event handling
- maintenance work

The Runtime executes Work Units.

Capabilities provide their behaviour.

---

## Worker

An isolated execution environment capable of executing one Work Unit.

Workers:

- execute
- report completion
- honour cancellation

Workers do not understand business behaviour.

---

## Worker Manager

The Runtime Service responsible for:

- worker lifecycle
- worker allocation
- worker health
- worker replacement

Workers are Runtime resources.

The Worker Manager owns them.

---

## Worker Pool

A bounded collection of Runtime workers.

Worker pools provide:

- concurrency
- predictable resource usage
- execution capacity

Worker pools belong to the Worker Manager.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| DAG | Directed Acyclic Graph |
| DI | Dependency Injection |
| MEG | Mosaic Engineering Guidelines |
| SDK | Software Development Kit |
| UI | User Interface |

---

# Relationship to MEG-005

This glossary supports every document within the Runtime Architecture specification.

Definitions should remain consistent across:

- Runtime implementation
- Runtime documentation
- Extension Platform
- Contributor Guidance
- Architecture Specifications

Whenever Runtime terminology evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`15-contributor-guidance.md`

**Next File**

`references.md`
