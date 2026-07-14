<!--
File: docs/engineering/guides/meg-006-extension-platform/glossary.md
Document: MEG-006
Status: Draft
Version: 0.1
-->

# Glossary

> *The platform grows through shared understanding. Shared understanding begins with a shared vocabulary.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Extension Platform.

These definitions establish the canonical vocabulary for:

- Runtime documentation
- SDK documentation
- Capability manifests
- Architecture specifications
- Marketplace tooling
- Contributor guidance

Where a term has a specific meaning within the Mosaic platform, that definition takes precedence over informal usage.

---

# A

## Activation

The Runtime process through which a registered capability becomes operational.

Activation occurs only after:

- discovery
- registration
- dependency resolution
- permission validation
- configuration validation

Activation is owned by the Runtime.

Not the capability.

---

# C

## Capability

A self-contained unit of business functionality executed by the Runtime.

Capabilities:

- own business behaviour
- expose contracts
- declare permissions
- participate in the Runtime lifecycle

Capabilities are the primary architectural unit of the Mosaic platform.

---

## Capability Descriptor

The Runtime's internal representation of a capability.

A Capability Descriptor is created from the Capability Manifest during discovery.

It contains:

- identity
- metadata
- dependencies
- permissions
- contracts

The Runtime uses descriptors during registration and dependency resolution.

---

## Capability Manifest

The machine-readable contract describing a capability.

Typically named:

```
capability.yaml
```

The manifest declares:

- identity
- version
- permissions
- dependencies
- configuration
- contracts

The Runtime consumes manifests before executing capability code.

Manifest-driven platforms separate metadata from implementation, enabling validation before activation.  [oai_citation:0‡chromium.googlesource.com](https://chromium.googlesource.com/chromium/src/%2B/HEAD/extensions/docs/overview.md?utm_source=chatgpt.com)

---

## Contract

A stable interface exposed by either:

- the Runtime
- another capability

Capabilities depend upon contracts.

Never implementations.

---

# D

## Dependency Resolution

The Runtime process responsible for validating:

- dependencies
- versions
- contracts
- compatibility

Dependency Resolution produces the Capability Graph used for activation.

---

## Discovery

The Runtime process responsible for locating capability manifests.

Discovery operates entirely upon metadata.

No executable code should run during discovery.

---

# E

## Extension

A packaged delivery mechanism for one or more capabilities.

Within Mosaic:

Core capabilities and third-party extensions are architecturally equivalent.

They differ only in:

- distribution
- installation

Not execution.

---

## Extension Platform

The Runtime subsystem responsible for:

- discovery
- registration
- activation
- lifecycle
- SDK
- capability integration

The Extension Platform enables the Mosaic ecosystem to evolve without modifying the Runtime.

---

# I

## Isolation

The architectural principle that capabilities should remain independent while collaborating through Runtime contracts.

Isolation applies to:

- lifecycle
- execution
- permissions
- configuration
- business state
- failures

---

# M

## Manifest

A machine-readable metadata document describing an extension or capability.

Within Mosaic:

The Capability Manifest is the authoritative source of capability metadata.

The Runtime validates manifests before activation.

---

## Marketplace

A platform through which capabilities may be:

- discovered
- installed
- upgraded
- removed

Marketplace behaviour should follow Runtime architecture rather than redefine it.

---

# P

## Permission

An explicitly declared authority granted to a capability.

Examples include:

```
blob.read
```

```
scheduler.use
```

```
network.outbound
```

Permissions are:

- declared
- validated
- granted

They are never assumed.

---

## Platform Contract

A stable Runtime API exposed through the SDK.

Platform contracts evolve more slowly than Runtime implementation.

---

# R

## Registration

The Runtime process that admits a discovered capability into the Capability Registry.

Registration records metadata.

It does not activate executable code.

---

## Runtime Contract

A Runtime capability exposed through the SDK.

Examples include:

- Scheduler
- Configuration
- Events
- Logging

Capabilities consume Runtime contracts.

They do not consume Runtime implementation.

---

# S

## SDK

The official programming interface between:

- Runtime
- capabilities

The SDK exposes stable contracts while hiding Runtime implementation.

Extension authors should depend only upon the SDK.

---

# V

## Version Compatibility

The Runtime's ability to determine whether:

- capability
- SDK
- Runtime
- manifest

can safely operate together.

Compatibility is determined before activation.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| API | Application Programming Interface |
| SDK | Software Development Kit |
| MEG | Mosaic Engineering Guidelines |
| YAML | YAML Ain't Markup Language |

---

# Relationship to MEG-006

This glossary supports every document within the Extension Platform specification.

Definitions should remain consistent across:

- Runtime documentation
- SDK documentation
- Marketplace documentation
- Capability manifests
- Architecture specifications

Whenever platform terminology evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.

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
