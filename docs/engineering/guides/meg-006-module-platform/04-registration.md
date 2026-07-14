<!--
File: docs/engineering/guides/meg-006-module-platform/04-registration.md
Document: MEG-006
Status: Draft
Version: 0.2
-->

# Registration

> *Discovery identifies capabilities. Registration admits them into the platform.*

---

# Purpose

Discovery locates capabilities.

Registration determines whether they become recognised members of the Runtime.

A discovered capability is simply a candidate.

A registered capability is part of the platform.

Registration establishes:

- identity
- ownership
- Runtime visibility
- lifecycle participation

It intentionally does **not** activate executable code.

Registration is a control-plane operation.

Execution comes later.

---

# Philosophy

Within Mosaic:

> **Capabilities are admitted into the Runtime through registration, not execution.**

Registration should establish trust in the capability's metadata.

It should never execute capability logic.

The Runtime should complete registration before loading any executable implementation.

---

# Registration Pipeline

Every capability follows the same registration pipeline.

```
Capability Descriptor

↓

Identity Validation

↓

Registry Admission

↓

Dependency Registration

↓

Lifecycle Registration

↓

Registered
```

Execution has still not begun.

The Runtime now knows the capability exists.

---

# Registration Before Activation

Registration intentionally precedes activation.

```
Discovery

↓

Registration

↓

Dependency Resolution

↓

Activation

↓

Execution
```

A registered capability may still fail:

- dependency resolution
- permission validation
- compatibility checks

Registration simply makes the capability visible to the Runtime.

---

# Runtime Admission

Registration admits the capability into the Capability Registry.

Conceptually.

```
Capability Descriptor

↓

Capability Registry

↓

Registered Capability
```

Once admitted, the Runtime may reason about:

- dependencies
- contracts
- lifecycle
- compatibility

without executing the capability.

---

# Identity Registration

Every registered capability MUST possess:

- unique identifier
- version
- manifest version

Example.

```yaml
id: metadata

version: 2.1.0

manifest: 1
```

Registration should fail immediately if identity conflicts exist.

Identity becomes immutable after registration.

---

# Registry Population

Registration populates the Capability Registry.

Typical information includes:

- identity
- metadata
- dependencies
- permissions
- lifecycle
- configuration schema
- provided contracts
- consumed contracts

The Registry becomes the Runtime's authoritative source of capability information.

---

# Registration Is Metadata Only

Registration MUST remain metadata driven.

The Runtime should not:

- load Go modules
- instantiate capabilities
- execute constructors
- invoke lifecycle hooks

Registration should complete entirely from the Capability Descriptor.

Separating registration from activation keeps the control plane independent of executable code, a common design principle in mature module architectures.  [OpenClaw](https://docs.openclaw.ai/modules/architecture-internals)

---

# Duplicate Registration

The Runtime MUST reject duplicate capability identifiers.

Example.

```
metadata

↓

metadata
```

Only one capability may own one identifier.

Version does not change identity.

Identifiers remain globally unique.

---

# Runtime Visibility

Once registered, the capability becomes visible to Runtime Services.

Examples include:

```
Capability Registry

↓

Execution Engine

↓

Scheduler

↓

Dependency Resolver
```

Visibility does not imply availability.

Activation has not yet occurred.

---

# Registration State

Every capability progresses through a registration lifecycle.

```
Discovered

↓

Validated

↓

Registered

↓

Awaiting Activation
```

The Capability Registry should expose this state.

Operators should understand precisely where each capability currently resides.

---

# Dependency Recording

Registration records dependency information.

Example.

```yaml
dependencies:

  - playback

  - library
```

The Runtime stores these declarations.

Resolution occurs later.

Registration records.

Resolution evaluates.

Responsibilities remain intentionally separate.

---

# Contract Registration

Capabilities SHOULD register the contracts they provide.

Example.

```yaml
provides:

  - MetadataProvider

  - ArtworkProvider
```

Likewise.

```yaml
consumes:

  - BlobStore

  - Scheduler
```

The Runtime now understands:

- provided services
- required services

before activation begins.

---

# Event Registration

Capabilities SHOULD register Runtime event metadata.

Example.

```yaml
publishes:

  - MetadataFetched
```

```yaml
subscribes:

  - MediaImported
```

Registration records these relationships.

The Runtime later builds:

- subscription graphs
- diagnostics
- architecture visualisations

No executable code is required.

---

# Permission Registration

Requested permissions SHOULD be recorded.

Example.

```yaml
permissions:

  - blob.read

  - scheduler.use
```

Permission approval occurs later.

Registration simply records requested capabilities.

This separation keeps admission distinct from authorisation.

---

# Configuration Registration

Configuration schemas SHOULD be registered.

Example.

```yaml
configuration:

  refreshInterval:

    type: duration
```

Tooling may immediately use these schemas to:

- validate configuration
- generate user interfaces
- produce documentation

Again:

No executable code is required.

---

# Registration Events

The Runtime MAY publish Runtime Events describing registration.

Examples include:

```
CapabilityRegistered
```

```
CapabilityRejected
```

```
CapabilityUpdated
```

These remain Runtime Events.

They do not represent business behaviour.

---

# Registration Persistence

The Runtime MAY persist registration metadata.

Persisted information might include:

- capability inventory
- versions
- dependency graph
- manifest hashes

Persisted registration accelerates diagnostics and upgrade planning.

It should never replace manifest validation.

The manifest remains authoritative.

---

# Registration Diagnostics

Operators should be able to answer:

- Which capabilities registered?
- Which failed?
- Why?
- Which version?
- Which dependencies?

Registration should remain fully observable.

Hidden registration behaviour complicates platform operations.

---

# Registration Independence

Registration should remain independent from:

- dependency resolution
- activation
- execution
- lifecycle callbacks

Each stage owns one concern.

Combining them increases Runtime complexity unnecessarily.

---

# Security

Registration should assume:

Every capability remains untrusted.

Registration records metadata.

It does not grant execution rights.

Execution should occur only after:

- dependency validation
- compatibility checks
- permission evaluation

complete successfully.

---

# Anti-Patterns

The following practices are prohibited.

## Executable Registration

Running capability code during registration.

---

## Implicit Registration

Automatically registering capabilities without validation.

---

## Registration Side Effects

Registration modifying Runtime behaviour immediately.

---

## Duplicate Registries

Maintaining capability information outside the Capability Registry.

---

## Runtime Mutation

Registration changing Runtime Services directly.

---

## Coupled Registration

Combining:

- registration
- activation
- execution

into one Runtime phase.

---

# Mosaic Guidelines

Within Mosaic:

- Registration MUST remain metadata driven.
- Registration MUST populate the Capability Registry.
- Registration MUST NOT execute capability code.
- Capability identifiers MUST remain globally unique.
- Registration SHOULD record dependencies, permissions and contracts.
- Registration SHOULD remain observable.
- Registration MUST precede activation.
- Registration MUST treat capabilities as untrusted until later validation stages.

---

# Relationship to MEG

Discovery answers:

> **What capabilities exist?**

Registration answers:

> **Which capabilities belong to this Runtime?**

The next chapter introduces **Dependency Resolution**, where the Runtime transforms registered capabilities into a validated capability graph ready for activation.

---

# Summary

Registration is the Runtime's admission process.

It transforms discovered metadata into recognised Runtime participants without executing a single line of capability code.

By separating:

- discovery
- registration
- dependency resolution
- activation
- execution

the Mosaic Runtime gains a predictable, observable and secure capability lifecycle that scales naturally as the platform grows.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`03-discovery.md`

**Next File**

`05-dependency-resolution.md`
