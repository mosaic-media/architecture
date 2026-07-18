<!--
File: docs/engineering/guides/meg-005-runtime-architecture/02-runtime-kernel.md
Document: MEG-005
Status: Draft
-->

# Runtime Kernel

> *The Runtime Kernel owns the platform itself. Every other runtime component exists because the Kernel allows it to.*

---

# Purpose

The Runtime consists of many independent subsystems.

Examples include:

- Capability Registry
- Execution Engine
- Worker Manager
- Scheduler
- Resource Manager
- Lifecycle Manager

Something must own the coordination of these subsystems.

Within Mosaic, that responsibility belongs to the **Runtime Kernel**.

The Runtime Kernel is the architectural centre of the Runtime.

It owns:

- lifecycle
- coordination
- service registration
- dependency graph
- runtime state

It intentionally owns no business behaviour.

---

# Philosophy

Within Mosaic:

> **The Runtime Kernel coordinates runtime services. It never becomes one.**

The Runtime Kernel should remain extremely small.

It should provide only the minimum capabilities required for the Runtime to function.

Everything else becomes a Runtime Service.

This mirrors microkernel operating system design, where the kernel retains only essential responsibilities while higher-level services are implemented separately.  [Operating Systems](https://operatingsystemsauthority.com/operating-system-kernel)

---

# What Is The Runtime Kernel?

The Runtime Kernel is the root object of the Mosaic Runtime.

Conceptually.

```mermaid
flowchart TD

N1["Runtime Kernel"]
N2["Capability Registry"]
N3["Execution Engine"]
N4["Scheduler"]
N5["Worker Manager"]
N6["Resource Manager"]
N7["Lifecycle Manager"]
N8["Observability"]

N1 --> N2
N1 --> N3
N1 --> N4
N1 --> N5
N1 --> N6
N1 --> N7
N1 --> N8
```

The Kernel owns these components.

Those components do not own one another.

---

# Why A Kernel Exists

Without a Runtime Kernel:

```mermaid
flowchart TD

N1["Scheduler"]
N2["Worker Manager"]
N3["Capability Registry"]
N4["Execution Engine"]
N5["Everyone Knows Everyone"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Eventually:

- dependencies become circular
- lifecycle becomes inconsistent
- ownership becomes unclear

Instead.

```mermaid
flowchart TD

N1["Runtime Kernel"]
N2["Coordinates"]
N3["Runtime Services"]

N1 --> N2
N2 --> N3
```

Dependencies remain explicit.

Responsibilities remain isolated.

---

# Kernel Responsibilities

The Runtime Kernel owns:

- runtime bootstrap
- service registration
- lifecycle coordination
- dependency graph construction
- runtime state
- service discovery
- shutdown coordination

The Runtime Kernel intentionally does **not** own:

- scheduling
- worker execution
- event delivery
- business behaviour
- persistence

These belong to dedicated Runtime Services.

---

# Runtime Composition

Every Runtime Service is composed through the Kernel.

```mermaid
flowchart TD

N1["Bootstrap"]
N2["Runtime Kernel"]
N3["Runtime Services"]
N4["Capabilities"]

N1 --> N2
N2 --> N3
N3 --> N4
```

The Kernel becomes the root of the Runtime object graph.

---

# Runtime Registry

The Kernel maintains a registry of Runtime Services.

Conceptually.

```mermaid
flowchart TD

N1["Runtime Kernel"]
N2["Register Scheduler"]
N3["Register Worker Manager"]
N4["Register Resource Manager"]

N1 --> N2
N2 --> N3
N3 --> N4
```

This registry exists solely for Runtime coordination.

It is **not** a Service Locator.

Runtime Services should still receive explicit dependencies through construction.

---

# Lifecycle Ownership

The Runtime Kernel owns lifecycle transitions.

```mermaid
flowchart TD

N1["Initialise"]
N2["Start"]
N3["Running"]
N4["Stopping"]
N5["Shutdown"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every Runtime Service participates.

No Runtime Service should transition independently.

Lifecycle ownership remains centralised.

---

# Runtime State

The Kernel owns operational state.

Examples include:

- runtime status
- registered services
- loaded capabilities
- startup progress
- shutdown progress

Business state remains entirely outside the Runtime.

---

# Runtime Contracts

Runtime Services interact with the Kernel through contracts.

Examples include:

```

LifecycleService
```

```

CapabilityRegistry
```

```

ExecutionEngine
```

Services should never depend upon Kernel implementation details.

Only Kernel contracts.

---

# Kernel Simplicity

The Runtime Kernel should remain intentionally small.

A useful question is:

> **Could this responsibility become its own Runtime Service?**

If yes:

It probably should.

The Kernel should coordinate.

Not accumulate functionality.

---

# Runtime Services

The Runtime should resemble:

```mermaid
flowchart TD

N1["Kernel"]
N2["Small Services"]

N1 --> N2
```

Not:

```mermaid
flowchart TD

N1["Kernel"]
N2["Large Internal Modules"]

N1 --> N2
```

Small Runtime Services provide:

- replaceability
- testability
- isolation
- observability

Large kernels become difficult to evolve.

---

# Capability Independence

Capabilities should never communicate directly with the Kernel.

Instead.

```mermaid
flowchart TD

N1["Capability"]
N2["Runtime Service"]
N3["Kernel"]

N1 --> N2
N2 --> N3
```

The Kernel remains an internal Runtime concern.

Capabilities should interact only with published Runtime contracts.

---

# Fault Isolation

Suppose:

```mermaid
flowchart TD

N1["Scheduler"]
N2["Failure"]

N1 --> N2
```

The Runtime Kernel should:

- detect failure
- report failure
- coordinate recovery

The Scheduler should not attempt to restart itself.

Operational coordination belongs to the Kernel.

---

# Service Independence

Runtime Services should remain unaware of one another wherever practical.

Poor.

```mermaid
flowchart TD

N1["Scheduler"]
N2["Worker Manager"]
N3["Capability Registry"]
N4["Execution Engine"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Preferred.

```mermaid
flowchart TD

N1["Scheduler"]
N2["Kernel"]
N3["Worker Manager"]

N1 --> N2
N2 --> N3
```

The Kernel coordinates communication.

Runtime Services remain independent.

---

# Runtime Growth

As Mosaic evolves, new Runtime Services should integrate naturally.

Example.

Initially.

```mermaid
flowchart TD

N1["Kernel"]
N2["Workers"]
N3["Scheduler"]

N1 --> N2
N2 --> N3
```

Later.

```mermaid
flowchart TD

N1["Kernel"]
N2["Workers"]
N3["Scheduler"]
N4["Metrics"]
N5["Health"]
N6["Capability Discovery"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Kernel should grow through composition.

Not through increasing internal complexity.

---

# Startup

During startup.

```mermaid
flowchart TD

N1["Bootstrap"]
N2["Kernel Created"]
N3["Services Registered"]
N4["Services Started"]
N5["Capabilities Started"]
N6["Runtime Ready"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Kernel owns this sequence.

Startup order should never be implicit.

---

# Shutdown

Likewise.

```mermaid
flowchart TD

N1["Shutdown Requested"]
N2["Kernel"]
N3["Stop Capabilities"]
N4["Stop Services"]
N5["Release Resources"]
N6["Exit"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Every Runtime Service follows the same lifecycle.

The Kernel coordinates.

---

# Testing

The Runtime Kernel should be testable independently.

Typical tests verify:

- lifecycle ordering
- service registration
- dependency graph
- startup
- shutdown

Business capabilities should not be required.

The Kernel exists independently of the business.

---

# Anti-Patterns

The following practices are prohibited.

## Business Logic

The Runtime Kernel making business decisions.

---

## Service Locator

Runtime Services requesting arbitrary services dynamically.

---

## Large Kernel

Moving every Runtime feature into the Kernel.

---

## Circular Runtime Services

Runtime Services depending directly upon one another.

---

## Capability Awareness

The Kernel understanding:

- playback
- metadata
- collections

The Kernel coordinates execution.

It never understands the business.

---

# Mosaic Guidelines

Within Mosaic:

- The Runtime Kernel MUST remain small.
- The Runtime Kernel MUST own lifecycle coordination.
- Runtime Services MUST remain independently replaceable.
- The Runtime Kernel MUST NOT contain business behaviour.
- Runtime Services SHOULD communicate through Kernel contracts.
- Startup and shutdown MUST be coordinated by the Kernel.
- Runtime growth SHOULD occur through composition.
- The Runtime Kernel SHOULD resemble a microkernel rather than a monolith.

---

# Relationship to MEG

The Runtime Philosophy established:

> **What the Runtime is.**

The Runtime Kernel establishes:

> **Which component owns the Runtime itself.**

The next chapter introduces the **Capability Registry**, the subsystem responsible for discovering, registering and exposing every capability participating in the Mosaic platform.

---

# Summary

The Runtime Kernel is the smallest yet most important component within the Runtime.

It owns:

- coordination
- lifecycle
- composition

It intentionally avoids owning:

- business
- execution
- scheduling
- persistence

By remaining small, explicit and stable, the Kernel allows the Runtime to continue evolving through independently replaceable services rather than accumulating complexity at its centre.
