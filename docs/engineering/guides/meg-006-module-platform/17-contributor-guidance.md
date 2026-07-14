<!--
File: docs/engineering/guides/meg-006-module-platform/17-contributor-guidance.md
Document: MEG-006
Status: Draft
Version: 0.8
-->

# Contributor Guidance

> *Every capability added to the platform should strengthen the ecosystem rather than increase the complexity of the Runtime.*

---

# Purpose

The Module Platform exists so that the Mosaic ecosystem can continue evolving without continually modifying the Platform.

Every contributor therefore shares responsibility for preserving:

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

The Runtime should evolve slowly.

Capabilities should evolve continuously.

---

# Before Writing Code

Before implementing a capability ask:

- Does this represent one business capability?
- Does a capability already exist?
- Should this extend an existing capability?
- Does the Runtime already expose the required contracts?

If Runtime modification appears necessary:

Reconsider the capability design first.

---

# Before Creating A Capability

Every capability should answer one question.

> **What business value do I provide?**

Examples.

```
Metadata
```

```
Playback
```

```
Books
```

Poor.

```
Utilities
```

```
PlatformHelpers
```

Capability names should describe business value.

Not technical implementation.

---

# Before Editing The Runtime

The Runtime should be modified only when:

- a new Runtime capability is genuinely required
- existing Runtime contracts cannot support platform evolution
- architectural review has approved the change

Business functionality should almost never require Runtime modification.

The Runtime exists to execute capabilities.

Not contain them.

---

# Before Creating A Manifest

Every capability SHOULD define its manifest before implementation begins.

Confirm:

- identifier
- dependencies
- permissions
- contracts
- configuration
- lifecycle

If the manifest is unclear:

The capability design is probably unclear.

The manifest should become the architectural specification for the capability.

---

# Before Adding Dependencies

Ask:

- Is this dependency required?
- Could it become optional?
- Does a Runtime contract already exist?
- Am I depending upon implementation rather than contracts?

Capabilities should depend upon:

- SDK contracts
- declared capability contracts

Never Runtime implementation.

---

# Before Requesting Permissions

Ask:

> **Do I genuinely require this permission?**

Prefer:

```yaml
blob.read
```

Rather than:

```yaml
blob.*
```

The principle of least privilege should guide every permission request.

Permissions should remain:

- minimal
- explicit
- justified

---

# Before Adding Configuration

Configuration should answer:

> **What does the operator need to control?**

Avoid configuration that exists solely because of implementation.

Capabilities should declare configuration only when it changes operational behaviour.

Configuration should remain:

- typed
- validated
- documented

---

# Before Publishing Events

Events should represent:

Completed business facts.

Good.

```
MetadataFetched
```

Poor.

```
FetchMetadataNow
```

Capabilities should publish facts.

Not instructions.

This reinforces the Event-Driven Runtime defined in MEG-002.

---

# Before Consuming Events

Ask:

> **Does this capability genuinely need this business fact?**

Avoid subscribing simply because:

> "It might be useful."

Every event subscription introduces architectural coupling.

Subscriptions should remain intentional.

---

# Before Exposing Contracts

Public Runtime contracts should remain:

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

Every capability SHOULD verify:

- manifest valid
- permissions minimal
- dependencies explicit
- configuration documented
- tests complete
- compatibility declared

Releases should be predictable.

Not exploratory.

---

# Marketplace Readiness

Before publishing a capability confirm:

- installation instructions exist
- configuration documented
- permissions explained
- compatibility declared
- version correct
- changelog updated

Marketplace quality begins with capability quality.

---

# Runtime Compatibility

Capability authors should never assume:

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

Capability reviews should focus upon:

- business value
- manifest quality
- Runtime contracts
- dependency clarity
- permission justification
- platform consistency

Review should ask:

> **Would another engineer confidently install this capability without reading its implementation?**

If not:

Improve the capability before release.

---

# Refactoring

Capability refactoring should generally:

- simplify contracts
- reduce dependencies
- narrow permissions
- improve documentation
- clarify ownership

Refactoring should make the capability easier to integrate into the platform.

Not merely reorganise code.

---

# Testing

Every capability SHOULD provide tests for:

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

Capability documentation should evolve alongside implementation.

Whenever introducing:

- new contracts
- new permissions
- new configuration
- new events

update:

- manifest
- documentation
- examples
- compatibility notes

Documentation should remain part of the capability.

Not an afterthought.

---

# Contributor Checklist

Before requesting review confirm:

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

Avoid:

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

Module authors should strive to:

- simplify capability design
- reduce coupling
- improve discoverability
- document contracts
- minimise permissions
- preserve Runtime independence

The platform should become easier to extend as it grows.

Not harder.

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

The Module Platform succeeds when adding a new capability feels routine.

No Runtime redesign.

No architectural debate.

Simply:

- manifest
- discovery
- registration
- activation
- execution

Within Mosaic, every contribution should strengthen the ecosystem by making capabilities:

- easier to discover
- easier to understand
- easier to trust
- easier to evolve

The Runtime provides the platform.

Contributors determine how valuable that platform becomes.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`16-adrs.md`

**Next File**

`references.md`
