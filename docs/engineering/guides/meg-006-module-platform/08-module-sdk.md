<!--
File: docs/engineering/guides/meg-006-module-platform/08-module-sdk.md
Document: MEG-006
Status: Draft
Version: 0.2
-->

# Module SDK

> *The SDK is not the platform. It is the language through which modules communicate with the platform.*

---

# Purpose

The Runtime exposes capabilities through stable contracts.

Module authors require a safe, supported mechanism for interacting with those contracts.

That mechanism is the **Module SDK**.

The SDK provides the APIs, interfaces and abstractions that allow modules to participate in the Runtime without depending upon Runtime implementation details.

The SDK is the only supported programming interface between:

- the Runtime
- capabilities
- third-party developers

---

# Philosophy

Within Mosaic:

> **The SDK exposes capabilities. It hides implementation.**

Module authors should never interact directly with:

- Runtime internals
- worker pools
- dependency graphs
- schedulers
- capability registry implementation

Instead, the SDK exposes stable contracts representing supported platform functionality.

The SDK should remain considerably more stable than the Runtime beneath it.

---

# What Is The SDK?

The Module SDK is the public programming surface of the Mosaic platform.

Conceptually.

```
Runtime

↓

SDK

↓

Module
```

The Runtime owns implementation.

The SDK owns contracts.

Modules consume only the SDK.

---

# Why An SDK Exists

Without an SDK:

```
Module

↓

Runtime Internals
```

Every Runtime change becomes:

- breaking
- expensive
- risky

Instead.

```
Module

↓

SDK

↓

Runtime
```

The Runtime evolves.

The SDK remains stable.

Modules continue functioning.

This stable abstraction layer is a defining characteristic of mature module ecosystems.  [Visual Studio Code](https://code.visualstudio.com/api/references/module-manifest)

---

# SDK Ownership

The Runtime owns the SDK.

Module authors consume it.

Modules should never:

- extend the SDK
- replace SDK contracts
- depend upon internal Runtime packages

The SDK represents the official contract between the platform and module developers.

---

# SDK Responsibilities

The SDK provides access to:

- lifecycle
- configuration
- scheduling
- capability contracts
- execution
- logging
- observability
- permissions

It intentionally does **not** expose:

- worker implementation
- execution engine internals
- runtime kernel
- dependency graph internals

Internal Runtime architecture remains private.

---

# Stable Surface

The SDK should remain:

- documented
- versioned
- backwards compatible where practical

Breaking SDK changes should be rare.

Runtime implementation may evolve much more rapidly.

The SDK protects module authors from that evolution.

---

# Capability Context

Every capability SHOULD execute within a Capability Context supplied by the SDK.

Conceptually.

```go
type CapabilityContext struct {

    Logger

    Scheduler

    Configuration

    Events

    Health

}
```

The context provides Runtime services through stable abstractions.

Modules should never construct Runtime services themselves.

---

# Lifecycle APIs

The SDK SHOULD expose lifecycle contracts.

Examples.

```text
Initialise()

Start()

Stop()

Dispose()
```

These contracts should remain consistent for every capability.

Lifecycle semantics belong to the Runtime.

The SDK merely exposes them.

---

# Configuration APIs

Capabilities obtain configuration through the SDK.

Example.

```go
config := ctx.Configuration()
```

The SDK hides:

- configuration files
- environment variables
- storage implementation

Configuration remains a Runtime concern.

The SDK exposes only the contract.

---

# Scheduling APIs

Capabilities request scheduling through SDK abstractions.

Example.

```go
ctx.Scheduler().Schedule(...)
```

The capability expresses intent.

The Runtime determines:

- execution time
- worker allocation
- retries

The SDK exposes scheduling.

It does not expose scheduler implementation.

---

# Event APIs

Capabilities interact with Runtime Events through SDK contracts.

Examples.

```go
ctx.Events().Publish(...)
```

```go
ctx.Events().Subscribe(...)
```

The SDK should expose:

- business-oriented event APIs

It should not expose:

- event bus implementation
- transport protocols
- queue management

Messaging infrastructure remains hidden.

---

# Logging APIs

Capabilities SHOULD receive structured logging through the SDK.

Example.

```go
ctx.Logger().Info(...)
```

The SDK hides:

- log sinks
- storage
- formatting
- aggregation

Capabilities should simply express operational intent.

---

# Health APIs

Capabilities SHOULD expose Runtime health through SDK contracts.

Example.

```go
ctx.Health().Ready()
```

The Runtime determines:

- aggregation
- reporting
- monitoring

The SDK provides the abstraction.

---

# Permissions

The SDK should automatically enforce Runtime permissions.

Suppose a capability requests:

```go
ctx.BlobStore()
```

Without:

```
blob.read
```

permission.

The SDK should reject the request.

Permission enforcement belongs to the Runtime.

The SDK simply provides controlled access.

---

# Capability Discovery

Capabilities should not discover other capabilities dynamically.

Poor.

```go
ctx.Runtime().FindCapability(...)
```

Preferred.

Capabilities consume:

- declared contracts
- injected services

The Runtime resolves dependencies during startup.

The SDK should not expose Runtime discovery internals.

---

# Testing

The SDK SHOULD provide testing utilities.

Examples include:

- fake contexts
- fake schedulers
- fake configuration
- fake event publishers

Module authors should be able to test capabilities without starting the full Runtime.

This dramatically improves developer productivity.

---

# SDK Versioning

The SDK SHOULD be versioned independently.

Example.

```
SDK 1.2

↓

Runtime 1.5
```

Compatibility should be explicit.

Capabilities should declare the SDK version they require.

The Runtime validates compatibility during startup.

---

# SDK Documentation

Every public SDK contract SHOULD include:

- documentation
- examples
- compatibility notes
- lifecycle expectations

The SDK should become the primary documentation surface for module developers.

Developers should rarely need to understand Runtime internals.

---

# Runtime Independence

The SDK should shield module authors from Runtime evolution.

Changing:

- Worker Manager
- Scheduler
- Execution Engine

should rarely require SDK changes.

If Runtime implementation changes require SDK changes, the abstraction should be reconsidered.

---

# Anti-Patterns

The following practices are prohibited.

## Runtime Imports

Modules importing Runtime implementation packages.

---

## Internal APIs

Using undocumented Runtime interfaces.

---

## Reflection

Inspecting Runtime internals dynamically.

---

## Service Locator

Modules resolving arbitrary Runtime services.

---

## Worker Awareness

Modules depending upon worker identity or execution environment.

---

## SDK Leakage

Exposing Runtime implementation details through SDK contracts.

---

# Mosaic Guidelines

Within Mosaic:

- The SDK MUST be the only supported Runtime programming interface.
- Modules MUST depend only upon the SDK.
- Runtime implementation MUST remain hidden.
- SDK contracts SHOULD remain stable.
- Permissions SHOULD be enforced through SDK abstractions.
- Configuration SHOULD be accessed only through the SDK.
- The SDK SHOULD provide testing support.
- Runtime evolution SHOULD rarely require SDK changes.

---

# Relationship to MEG

The Module Lifecycle explains:

> **How capabilities participate in the Runtime.**

The SDK explains:

> **How module authors build those capabilities.**

The next chapter introduces **Permissions**, defining how the Runtime safely controls access to Runtime services while preserving capability isolation.

---

# Summary

The Module SDK is the public face of the Runtime.

It allows module authors to build sophisticated capabilities while remaining completely insulated from Runtime implementation details.

Within Mosaic, the SDK should feel:

- stable
- expressive
- well documented
- intentionally small

The Runtime evolves.

The SDK endures.

That separation allows the platform to grow without forcing module authors to continually chase internal architectural changes.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`07-module-lifecycle.md`

**Next File**

`09-permissions.md`
