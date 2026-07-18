<!--
File: docs/engineering/guides/meg-006-module-platform/08-module-sdk.md
Document: MEG-006
Status: Draft
-->

# Module SDK

> *The SDK is not the platform. It is the language through which modules communicate with the platform.*

---

# Purpose

The Mosaic SDK is the public contract between the Mosaic Platform and Mosaic Modules, and it defines the language the two use to communicate. The Runtime exposes capabilities through stable contracts, and module authors require a safe, supported mechanism for interacting with those contracts. That mechanism is the **Module SDK**.

The SDK provides the APIs, interfaces and abstractions that allow Modules to participate in the Runtime without depending upon Runtime implementation details, which makes it the only supported programming interface between the Runtime, capabilities and third-party developers. It deliberately contains almost no business logic, and it should remain one of the most stable repositories in the Mosaic ecosystem.

---

# Philosophy

Within Mosaic:

> **The SDK defines contracts, not behaviour.**

The SDK is not a framework, the Platform, a collection of broad helper utilities, or a place for business logic. It instead defines what can exist within the Mosaic ecosystem: the Platform implements those contracts and Modules satisfy them.

Module authors should therefore never interact directly with Runtime internals, worker pools, dependency graphs, schedulers or the capability registry implementation. The SDK exposes stable contracts representing supported platform functionality in their place, which is why it should remain considerably more stable than the Runtime beneath it.

---

# What Is The SDK?

The Module SDK is the public programming surface of the Mosaic platform. The Platform owns implementation and orchestration, the SDK owns contracts, and Modules consume only the SDK — never the Runtime directly.

What the SDK includes:

- interfaces and ports
- models
- Event Envelope
- Event Bus contracts
- registration APIs
- helper utilities
- testing framework

It is intentionally mostly definitions, and only a small amount of executable code should exist to support registration, validation and developer ergonomics.

---

# Dependency Direction

Both the Platform and Modules depend on the Mosaic SDK, and neither should depend directly on the other. The SDK is the shared contract surface between them, so it should not become an implementation bridge that leaks Platform internals.

---

# Why An SDK Exists

Without an SDK a Module would have to reach into Runtime internals, which makes every Runtime change breaking, expensive and risky. Placing the SDK between the Module and the Runtime removes that coupling: the Runtime evolves, the SDK remains stable, and Modules continue functioning. This stable abstraction layer is a defining characteristic of mature module ecosystems.  [Visual Studio Code](https://code.visualstudio.com/api/references/module-manifest)

---

# SDK Ownership

The Platform owns SDK contract authority and module authors consume it, which means Modules should never extend the SDK, replace SDK contracts, or depend upon internal Runtime packages. The SDK represents the official contract between the Platform and Module developers.

---

# SDK Responsibilities

The SDK has five primary responsibilities.

## Contracts

The SDK defines every public Platform capability contract, including MetadataProvider, MediaProvider, ArtworkProvider, SearchProvider, AuthenticationProvider and NotificationProvider. Ownership divides cleanly across the three parties: the SDK owns the interfaces, the Platform owns orchestration, and Modules own implementations.

## Models

The SDK defines the canonical Platform models — Metadata, Media, Artwork, User, Library and PlaybackSession among them. These are Platform models rather than implementation-specific DTOs, because every Module should share the same vocabulary.

## Events

The SDK owns the Event Envelope, the Event Bus interfaces and the core Platform events, but it does not own every event. Modules may define their own, such as `platform.started`, `anime.episode.released` and `playback.started`. The Platform routes events, whereas Modules own domain event meaning.

## Registration

The SDK exposes Module registration APIs and maintains the runtime registry used during Platform startup, and every Module exposes itself through a single registration point.

```go
func init() {
    sdk.Register(NewModule())
}
```

The Platform then asks for the registry and receives every registered Module in return.

```go
sdk.Modules()
```

No reflection, runtime scanning or plugin loading is required.

## Helper Utilities

The SDK may include small utilities that improve developer experience, such as Module builders, registration helpers, validation helpers, testing helpers and version helpers. Helpers should support contracts rather than become business logic.

---

# SDK Non-Responsibilities

The SDK intentionally avoids implementation, so it should never contain any of the following:

- database logic
- storage implementation
- GraphQL implementation
- scheduler implementation
- HTTP server
- caching implementation
- business logic
- Capability Manager orchestration
- rendering
- worker implementation
- execution engine internals
- runtime kernel
- dependency graph internals
- media business policy

The distinction extends to the lifecycle itself: the SDK may define lifecycle contracts, but it must not own lifecycle implementation, because that belongs to the Platform or to Modules. Internal Runtime architecture remains private.

---

# Stable Surface

The SDK should remain documented, versioned and backwards compatible where practical, and breaking SDK changes should be rare. Runtime implementation may evolve much more rapidly, and the SDK exists in part to protect module authors from that evolution.

---

# Capability Context

Every capability should execute within a Capability Context supplied by the SDK, which gathers the Runtime services a capability is permitted to use into a single value.

```go
type CapabilityContext struct {
    Logger
    Scheduler
    Configuration
    Events
    Health
}
```

The context provides those Runtime services through stable abstractions, so Modules should never construct Runtime services themselves.

---

# Lifecycle APIs

The SDK should expose lifecycle contracts, and those contracts should remain consistent for every capability.

```text
Initialise()
Start()
Stop()
Dispose()
```

Lifecycle semantics belong to the Runtime, as described in the Module Lifecycle chapter; the SDK merely exposes them.

---

# Configuration APIs

Capabilities obtain configuration through the SDK rather than reading it themselves.

```go
config := ctx.Configuration()
```

The SDK hides configuration files, environment variables and storage implementation behind that call. Configuration remains a Runtime concern, and the SDK exposes only the contract.

---

# Scheduling APIs

Capabilities request scheduling through SDK abstractions.

```go
ctx.Scheduler().Schedule(...)
```

The capability expresses intent and the Runtime determines execution time, worker allocation and retries. The SDK therefore exposes scheduling without exposing the scheduler implementation.

---

# Event APIs

Capabilities interact with Runtime Events through SDK contracts, publishing and subscribing through the context rather than through the bus itself.

```go
ctx.Events().Publish(...)
```

```go
ctx.Events().Subscribe(...)
```

The SDK should expose business-oriented event APIs, and it should not expose the event bus implementation, transport protocols or queue management. Messaging infrastructure remains hidden.

---

# Logging APIs

Capabilities should receive structured logging through the SDK.

```go
ctx.Logger().Info(...)
```

The SDK hides log sinks, storage, formatting and aggregation, so capabilities should simply express operational intent.

---

# Health APIs

Capabilities should expose Runtime health through SDK contracts.

```go
ctx.Health().Ready()
```

The Runtime determines aggregation, reporting and monitoring, and the SDK provides the abstraction through which a capability reports into them.

---

# Permissions

The SDK should automatically enforce Runtime permissions. Suppose a capability requests a store it has not been granted.

```go
ctx.BlobStore()
```

Without the `blob.read` permission the SDK should reject that request. Permission enforcement belongs to the Runtime, and the SDK simply provides controlled access to what the Runtime has already approved.

---

# Capability Discovery

Capabilities should not discover other capabilities dynamically, which makes the following poor practice.

```go
ctx.Runtime().FindCapability(...)
```

Capabilities should instead consume declared contracts and injected services, because the Runtime resolves dependencies during startup. The SDK should not expose Runtime discovery internals.

---

# Testing

The SDK should provide testing utilities so that module authors can test capabilities without starting the full Runtime, which dramatically improves developer productivity. Those utilities include:

- fake contexts
- fake schedulers
- fake configuration
- fake event publishers
- contract assertions
- provider fixtures

Conceptually, a test assembles a platform, registers a provider and asserts against it.

```go
sdktest.NewPlatform().
    Register(provider).
    Assert(...)
```

SDK testing utilities should validate behaviour against Platform contracts, and they should not require a complete Mosaic installation.

---

# Developer Tooling Boundary

The SDK is a Go library, and the Mosaic CLI provides the developer experience around it. Typical CLI commands include:

```text
mosaic new module
mosaic dev
mosaic build
mosaic test
mosaic doctor
mosaic validate
mosaic package
mosaic publish
mosaic docs
```

The CLI may scaffold, develop, test, diagnose, validate, build, package, publish and document Modules, but the SDK remains the developer contract and the CLI is tooling around that contract. Chapter 14 defines the complete Developer Platform around the SDK.

---

# Manifest Generation

SDK tooling may generate Module manifests from Go Module definitions. A Module may, for example, declare its identity, capabilities, events and permissions in source.

```go
sdk.Module{
    ID: "...",
    Capabilities: ...
    Events: ...
    Permissions: ...
}
```

Tooling may then generate `module.yaml` from that definition, which reduces drift between source declarations and manifest metadata. The generated manifest nevertheless remains the artefact consumed by the Supervisor during discovery and dependency resolution, so the Supervisor should still validate the manifest before invoking the Build Pipeline. Manifest generation must not allow executable code to replace manifest validation.

---

# Proposed Repository Structure

The SDK repository should be organised around contract vocabulary rather than around layers of implementation.

```text
mosaic-sdk/
    capabilities/
    events/
    models/
    module/
    permissions/
    registration/
    helpers/
    testing/
```

Most packages should contain definitions, interfaces, models and small support helpers, so that the repository structure itself reinforces that the SDK is a contract language rather than an implementation framework.

---

# SDK Versioning

The SDK should be versioned independently of the Runtime, so that a release line such as SDK 1.2 evolves separately from Runtime 1.5. Compatibility between the two should be explicit: capabilities should declare the SDK version they require, and the Runtime validates that compatibility during startup.

---

# SDK Documentation

Every public SDK contract should include documentation, examples, compatibility notes and lifecycle expectations. The SDK should become the primary documentation surface for module developers, who should rarely need to understand Runtime internals.

---

# Runtime Independence

The SDK should shield module authors from Runtime evolution, so changing the Worker Manager, the Scheduler or the Execution Engine should rarely require SDK changes. If Runtime implementation changes do require SDK changes, the abstraction should be reconsidered.

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

- The SDK must be the only supported programming interface between Platform and Modules.
- The SDK must define contracts rather than behaviour.
- Modules must depend only upon the SDK.
- The Platform must implement SDK contracts.
- Modules must satisfy SDK contracts.
- Runtime implementation must remain hidden.
- SDK contracts should remain stable.
- Permissions should be enforced through SDK abstractions.
- Configuration should be accessed only through the SDK.
- The SDK should provide testing support.
- SDK tooling may generate Module manifests, but generated manifests must still be validated by the Supervisor.
- The SDK must not contain business logic, Capability Manager orchestration or Platform implementation.
- Runtime evolution should rarely require SDK changes.

---

# Relationship to MEG

The Module Lifecycle explains:

> **How capabilities participate in the Runtime.**

The SDK explains:

> **How module authors build those capabilities.**

The next chapter introduces **Permissions**, defining how the Runtime safely controls access to Runtime services while preserving capability isolation.

---

# Summary

The Module SDK is the public contract language of the Mosaic ecosystem, and it allows module authors to build sophisticated capabilities while remaining completely insulated from Runtime implementation details. Within Mosaic, the SDK should feel stable, expressive, well documented and intentionally small.

The Runtime evolves; the SDK endures. That separation allows the platform to grow without forcing module authors to continually chase internal architectural changes.
