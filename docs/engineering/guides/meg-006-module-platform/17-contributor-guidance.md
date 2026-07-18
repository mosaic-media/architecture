<!--
File: docs/engineering/guides/meg-006-module-platform/17-contributor-guidance.md
Document: MEG-006
Status: Draft
-->

# Contributor Guidance

> *Every capability added to the platform should strengthen the ecosystem rather than increase the complexity of the Runtime.*

---

# Purpose

The Module Platform exists so that the Mosaic ecosystem can continue evolving without continually modifying the Platform. The Runtime is meant to become increasingly capable without becoming increasingly complicated, and it stays that way only while new work arrives as capabilities rather than as Runtime changes. That property is not self-sustaining, so every contributor shares responsibility for preserving:

- Runtime stability
- SDK stability
- capability isolation
- manifest quality
- architectural consistency

This document provides practical guidance for engineers building new capabilities for the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Extend the platform. Do not modify it.**

The first question should never be:

> **How do I change the Runtime?**

Instead ask:

> **Can this become a capability?**

The Runtime should evolve slowly whereas capabilities should evolve continuously, and that difference in pace is what the remainder of this chapter exists to protect.

---

# Before Writing Code

Most proposed work turns out to be a capability rather than a Platform change, and the cheapest moment to establish which it is comes before any code exists. Within Mosaic a feature is not an architectural unit whereas a capability is, so the answer determines whether the work acquires a lifecycle, dependencies, contracts, a manifest and an owner at all. Before implementing a capability ask:

- Does this represent one business capability?
- Does a capability already exist?
- Should this extend an existing capability?
- Does the Runtime already expose the required contracts?

If Runtime modification appears necessary, reconsider the capability design first, because the Runtime should already contain everything required to execute future capabilities. Adding a capability does require producing a new Platform package for the selected Generation; it should not require a Runtime redesign.

---

# Before Creating A Capability

A capability is an architectural unit that owns a lifecycle, dependencies, contracts, a manifest and ownership, so the name it is given is the name operators read long afterwards. Every capability should answer one question.

> **What business value do I provide?**

Good names describe that value: `Metadata`, `Playback`, `Books`. Poor names describe the code instead: `Utilities`, `PlatformHelpers`.

Capability names should therefore describe business value rather than technical implementation, because operators should be able to tell what a capability provides without reading its source. The capability identifier also becomes immutable once registration succeeds, so a name chosen carelessly is one the platform carries indefinitely.

---

# Before Editing The Runtime

A Runtime change is inherited by every capability the platform will ever host, which gives it a cost that no single capability change carries. Runtime evolution and capability evolution are intended to remain independent, so neither should require modifying the other. The Runtime should be modified only when:

- a new Runtime capability is genuinely required
- existing Runtime contracts cannot support platform evolution
- architectural review has approved the change

Business functionality should almost never require Runtime modification, because the Runtime exists to execute capabilities rather than to contain them.

---

# Before Creating A Manifest

The manifest is the Supervisor's primary source of truth, and the Supervisor does not execute or analyse Go source to recover anything the manifest leaves out. Discovery, admission and dependency resolution all operate on metadata alone, which means anything the manifest omits stays invisible to every stage before activation. Every capability should define its manifest before implementation begins, confirming:

- identifier
- dependencies
- permissions
- contracts
- configuration
- lifecycle

If the manifest is unclear, the capability design is probably unclear. The manifest should become the architectural specification for the capability.

---

# Before Adding Dependencies

Every declared dependency becomes a constraint the Runtime validates during dependency resolution, and one an operator has to satisfy before the capability can activate. A required dependency that cannot be satisfied prevents activation entirely, whereas an optional one merely leaves the capability operating in a reduced form, so the choice between the two decides whether a missing capability blocks the platform. Ask:

- Is this dependency required?
- Could it become optional?
- Does a Runtime contract already exist?
- Am I depending upon implementation rather than contracts?

Capabilities should depend upon SDK contracts and declared capability contracts, never Runtime implementation, because the SDK forms the isolation boundary between Runtime evolution and module stability. A capability that reaches past that boundary turns every Runtime change into a potential breaking change for itself.

---

# Before Requesting Permissions

Permissions bound what a capability can reach when it behaves incorrectly, so authority granted for convenience is authority that remains granted after a compromise. The Runtime evaluates the declarations in the manifest during activation and permissions are never discovered dynamically, which makes the request written here the authority the capability holds for the whole of its life. Ask:

> **Do I genuinely require this permission?**

Prefer:

```yaml
blob.read
```

Rather than:

```yaml
blob.*
```

The principle of least privilege should guide every permission request, and permissions should remain:

- minimal
- explicit
- justified

Marketplace tooling displays those requests to the operators deciding whether to trust the capability, so a request that cannot be justified is one that will not be granted.

---

# Before Adding Configuration

The Runtime validates configuration before activation, which means a poorly defined required value prevents the capability starting rather than failing quietly during execution. Missing required configuration must fail activation, so marking a value required is a decision about whether the capability can start at all. Configuration should answer:

> **What does the operator need to control?**

Avoid configuration that exists solely because of implementation, and declare configuration only when it changes operational behaviour. Configuration should remain:

- typed
- validated
- documented

---

# Before Publishing Events

An event is a public contract that other capabilities subscribe to without the publisher ever learning who they are, so its name outlives the code that raised it. Events should represent completed business facts: `MetadataFetched` records something that happened, whereas `FetchMetadataNow` issues an instruction to whoever is listening.

Capabilities should publish facts rather than instructions, because a publisher that does not know its subscribers is in no position to address them. This reinforces the Event-Driven Runtime defined in [MEG-002](../meg-002-event-driven-runtime/index.md).

---

# Before Consuming Events

A subscription is the one form of coupling a capability can create unilaterally, since the publishing capability never agreed to it and cannot see it. Subscriptions are declared in the manifest and the Runtime builds subscription graphs and diagnostics from those declarations, so an unnecessary one becomes part of how the platform's architecture is described. Ask:

> **Does this capability genuinely need this business fact?**

Avoid subscribing simply because:

> "It might be useful."

Every event subscription introduces architectural coupling, so subscriptions should remain intentional.

---

# Before Exposing Contracts

A contract constrains every later version of the capability behind it, because consumers depend upon the contract rather than the implementation. Removing one is a breaking change requiring a major version increment, and deprecation should precede removal, so exposing an interface commits the capability to supporting it through a migration period. Public Runtime contracts should therefore remain:

- stable
- documented
- business focused

Avoid exposing:

- internal implementation
- temporary APIs
- experimental interfaces

SDK contracts should become long-lived commitments.

---

# Before Releasing

Release is the point at which a capability stops being the author's concern and becomes the operator's, so anything left unverified is discovered during installation instead. The Runtime checks registration, the dependency graph, version compatibility, permissions and configuration before activation begins, and a failure in any of them leaves the capability inactive rather than partially working. Every capability should verify:

- manifest valid
- permissions minimal
- dependencies explicit
- configuration documented
- tests complete
- compatibility declared

Releases should be predictable rather than exploratory, because installation should never become trial and error.

---

# Marketplace Readiness

A capability should be installable by someone who has never seen its source, which means the published listing has to carry everything that decision needs. Marketplace tooling exposes the capability version, its SDK requirement, Runtime compatibility and the configuration it requires, but it can present only what the capability has declared. Before publishing a capability confirm:

- installation instructions exist
- configuration documented
- permissions explained
- compatibility declared
- version correct
- changelog updated

Marketplace quality begins with capability quality.

---

# Runtime Compatibility

The Runtime validates compatibility before activation using what a capability declares, not what it assumes, and version numbers exist to communicate that compatibility rather than progress. Capabilities depend upon the SDK version and the Runtime contracts rather than upon the Runtime version itself, which keeps compatibility constraints from spreading further than they need to. Capability authors should never assume:

- Runtime version
- SDK implementation
- internal Runtime behaviour

Capabilities should rely only upon:

- documented SDK
- documented contracts
- manifest declarations

Everything else is implementation.

---

# Review Mindset

Review is the last point at which a capability can be corrected cheaply, and the first at which someone other than its author has to understand it. Capability reviews should focus upon:

- business value
- manifest quality
- Runtime contracts
- dependency clarity
- permission justification
- platform consistency

Review should ask:

> **Would another engineer confidently install this capability without reading its implementation?**

If not, improve the capability before release, because discovery should become a platform feature rather than a documentation exercise.

---

# Refactoring

Refactoring is an opportunity to reduce what the rest of the platform depends upon, not merely to rearrange what sits behind an unchanged contract. Capability refactoring should generally:

- simplify contracts
- reduce dependencies
- narrow permissions
- improve documentation
- clarify ownership

Refactoring should make the capability easier to integrate into the platform rather than simply reorganising code.

---

# Testing

Capabilities are upgraded independently of one another, so a capability's own tests are what keeps each upgrade from becoming a risk to the platform. An upgrade runs through the same lifecycle as an installation, stopping, deactivating and removing the running capability before its replacement is discovered, registered, resolved and activated, so anything the tests missed is discovered on a live platform. Every capability should provide tests for:

- business behaviour
- configuration validation
- manifest validity
- Runtime integration
- contract compatibility

Capabilities should remain testable using:

- fake Runtime context
- fake SDK
- fake dependencies

The full Runtime should rarely be required.

---

# Documentation

Documentation is how a capability is evaluated by operators who will never read its code, which is why it should change alongside the contract it describes rather than after it. Capability documentation should evolve alongside implementation, so whenever introducing:

- new contracts
- new permissions
- new configuration
- new events

update:

- manifest
- documentation
- examples
- compatibility notes

Documentation should remain part of the capability rather than an afterthought.

---

# Contributor Checklist

Before requesting review confirm the following.

## Capability

- [ ] One business capability.
- [ ] Clear business value.
- [ ] Manifest complete.

---

## Platform

- [ ] Runtime unchanged.
- [ ] Contracts documented.
- [ ] Dependencies explicit.

---

## Security

- [ ] Permissions minimal.
- [ ] Configuration validated.
- [ ] SDK only.

---

## Runtime

- [ ] Lifecycle respected.
- [ ] Runtime contracts used.
- [ ] No Runtime implementation imports.

---

## Documentation

- [ ] Manifest updated.
- [ ] Documentation updated.
- [ ] Compatibility documented.
- [ ] Examples verified.

---

# Common Platform Mistakes

The following recur often enough to name, and each erodes one of the boundaries established earlier in MEG-006. Avoid:

- modifying Runtime internals
- bypassing SDK contracts
- hidden dependencies
- broad permissions
- oversized capabilities
- undocumented configuration
- Runtime implementation imports
- duplicate business capabilities

These mistakes usually reduce platform quality long before they become operational problems.

---

# Engineering Culture

The platform should become easier to extend as it grows rather than harder, and that property is sustained by habit rather than by enforcement. Module authors should therefore strive to:

- simplify capability design
- reduce coupling
- improve discoverability
- document contracts
- minimise permissions
- preserve Runtime independence

---

# Relationship to MEG

This document explains how contributors should evolve the Module Platform established throughout MEG-006.

The previous chapters define:

> **How capabilities integrate with the Runtime.**

This chapter defines:

> **How engineers should preserve that integration over time.**

A platform survives because contributors consistently reinforce its architectural principles.

---

# Summary

The Module Platform succeeds when adding a new capability feels routine: no Runtime redesign, no architectural debate, simply manifest, discovery, registration, activation and execution.

Within Mosaic, every contribution should strengthen the ecosystem by making capabilities:

- easier to discover
- easier to understand
- easier to trust
- easier to evolve

The Runtime provides the platform. Contributors determine how valuable that platform becomes.
