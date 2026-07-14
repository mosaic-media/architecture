<!--
File: docs/engineering/guides/meg-006-extension-platform/02-capability-manifest.md
Document: MEG-006
Status: Draft
Version: 0.1
-->

# Capability Manifest

> *Before the Runtime executes a capability, it should understand it.*

---

# Purpose

The Runtime cannot safely execute arbitrary code.

Before a capability becomes part of the platform, the Runtime must understand:

- what it is
- what it provides
- what it requires
- what it is permitted to do
- whether it is compatible

This information is described by the **Capability Manifest**.

The Capability Manifest is the Runtime's primary contract with every capability.

Without a valid manifest:

The capability does not exist from the Runtime's perspective.

---

# Philosophy

Within Mosaic:

> **The manifest is the contract. The implementation is merely one possible fulfilment of that contract.**

The Runtime should understand a capability completely before loading any executable code.

Execution should never be required simply to discover metadata.

This mirrors modern extension ecosystems, where a manifest acts as the authoritative description of an extension before the runtime loads it.  [oai_citation:0‡Chrome for Developers](https://developer.chrome.com/extensions/manifest?utm_source=chatgpt.com)

---

# What Is A Capability Manifest?

A Capability Manifest is a machine-readable document describing a capability.

It contains:

- identity
- metadata
- dependencies
- permissions
- contracts
- lifecycle
- configuration

The Runtime consumes the manifest.

Capabilities consume the Runtime.

---

# Why A Manifest Exists

Without a manifest:

```
Capability

↓

Execute

↓

Discover Requirements
```

The Runtime cannot validate:

- dependencies
- permissions
- compatibility

Instead.

```
Capability

↓

Manifest

↓

Validation

↓

Registration

↓

Execution
```

The Runtime understands the capability before activation.

---

# Manifest Before Code

The Runtime startup sequence should be:

```
Discover Manifest

↓

Validate

↓

Register Capability

↓

Resolve Dependencies

↓

Activate

↓

Execute
```

The Runtime should never instantiate a capability simply to inspect it.

---

# Manifest Ownership

Every capability owns exactly one manifest.

Conceptually.

```
Capability

↓

capability.yaml
```

The manifest becomes part of the capability itself.

It should evolve alongside the implementation.

---

# Manifest Structure

Every Capability Manifest SHOULD contain:

```
Identity

↓

Metadata

↓

Dependencies

↓

Permissions

↓

Configuration

↓

Contracts

↓

Lifecycle

↓

Capabilities
```

Each section owns one architectural concern.

---

# Identity

Every capability MUST declare:

- identifier
- name
- version

Example.

```yaml
id: metadata

name: Metadata

version: 1.2.0
```

Identity should remain stable.

Changing the identifier represents a new capability.

---

# Metadata

Metadata describes the capability.

Typical fields include:

- author
- description
- homepage
- licence
- tags

Metadata improves:

- discovery
- diagnostics
- marketplaces
- tooling

It should not influence Runtime behaviour.

---

# Dependencies

Capabilities MUST declare Runtime dependencies explicitly.

Example.

```yaml
dependencies:

  - playback

  - library
```

The Runtime should validate dependencies before activation.

Capabilities should never discover missing dependencies during execution.

---

# Optional Dependencies

Capabilities MAY declare optional dependencies.

Example.

```yaml
optionalDependencies:

  - recommendations
```

If unavailable:

The capability should continue operating with reduced functionality.

The Runtime should distinguish clearly between:

- required
- optional

dependencies.

---

# Version Constraints

Dependencies SHOULD include version requirements.

Example.

```yaml
dependencies:

  playback: ">=2.0.0"

  library: "^1.4.0"
```

The Runtime should validate compatibility before startup.

Version negotiation belongs to the Runtime.

Not the capability.

---

# Permissions

Every capability MUST explicitly request permissions.

Examples include:

```yaml
permissions:

  - blob.read

  - blob.write

  - metadata.fetch

  - scheduler.use
```

Capabilities should receive only the permissions they require.

Least privilege should remain a platform principle.

Modern extension manifests similarly require capabilities and permissions to be declared up front so the host can validate them before execution.  [oai_citation:1‡Chrome for Developers](https://developer.chrome.com/extensions/manifest?utm_source=chatgpt.com)

---

# Configuration Schema

Capabilities SHOULD describe their configuration.

Example.

```yaml
configuration:

  provider:

    type: string

  refreshInterval:

    type: duration
```

The Runtime should validate configuration before activation.

Invalid configuration should prevent startup.

---

# Runtime Contracts

Capabilities SHOULD declare Runtime contracts.

Examples include:

```yaml
provides:

  - MetadataProvider
```

```yaml
consumes:

  - Scheduler

  - BlobStore
```

The Runtime should use these declarations during dependency resolution.

---

# Events

Capabilities SHOULD declare Runtime Events.

Example.

```yaml
publishes:

  - MetadataFetched

  - MetadataCorrected
```

```yaml
subscribes:

  - MediaImported
```

This information allows the Runtime to:

- visualise event flow
- validate dependencies
- generate documentation

Execution should not be required to discover event relationships.

---

# Lifecycle

Capabilities SHOULD describe lifecycle participation.

Example.

```yaml
lifecycle:

  startup: required

  shutdown: graceful
```

The Runtime should understand lifecycle expectations before execution begins.

---

# Health

Capabilities MAY declare health providers.

Example.

```yaml
health:

  readiness: supported

  liveness: supported
```

The Runtime should automatically integrate these into platform observability.

---

# Resource Requirements

Capabilities SHOULD declare expected Runtime resources.

Examples include:

```yaml
resources:

  workers: 2

  memory: 256Mi

  scheduling: required
```

The Resource Manager may use this information during planning and admission control.

These declarations should remain advisory rather than absolute.

---

# Runtime Validation

The Runtime SHOULD validate:

- manifest syntax
- required fields
- identifier uniqueness
- dependency graph
- permission requests
- version compatibility

before any capability is loaded.

Invalid manifests should fail immediately.

Not during execution.

---

# Tooling

The Capability Manifest should become the foundation for tooling.

Examples include:

- dependency visualisation
- marketplace indexing
- compatibility checking
- documentation generation
- architecture diagrams
- capability discovery

The Runtime should not be the only consumer of manifests.

Tooling should benefit equally.

---

# Manifest Evolution

The manifest schema will evolve.

Changes SHOULD remain:

- backwards compatible where practical
- versioned
- documented

The Runtime should support manifest version negotiation.

Capabilities should declare which manifest version they implement.

---

# Anti-Patterns

The following practices are prohibited.

## Hidden Dependencies

Capabilities discovering required dependencies during execution.

---

## Runtime Inspection

The Runtime loading executable code merely to obtain metadata.

---

## Implicit Permissions

Capabilities assuming access to Runtime services without declaring permissions.

---

## Runtime Configuration In Code

Embedding configuration schema inside implementation rather than the manifest.

---

## Duplicate Metadata

Maintaining separate metadata sources instead of one authoritative manifest.

---

## Business Logic

Using the manifest to encode business rules.

The manifest describes the capability.

It does not implement it.

---

# Mosaic Guidelines

Within Mosaic:

- Every capability MUST have exactly one manifest.
- The Runtime MUST validate manifests before execution.
- Dependencies MUST be declared explicitly.
- Permissions MUST follow least privilege.
- Configuration SHOULD be schema driven.
- Runtime contracts SHOULD be declared explicitly.
- Event publication and subscription SHOULD be discoverable through the manifest.
- The manifest SHOULD become the Runtime's primary source of capability metadata.

---

# Relationship to MEG

The Extension Philosophy established:

> **Why capabilities exist.**

The Capability Manifest defines:

> **How the Runtime understands those capabilities.**

The next chapter introduces **Discovery**, describing how the Runtime locates manifests, validates them and constructs the initial platform model before activation begins.

---

# Summary

The Capability Manifest is far more than metadata.

It is the architectural contract between a capability and the Runtime.

Within Mosaic, the Runtime should understand:

- identity
- dependencies
- permissions
- contracts
- configuration

before executing a single line of capability code.

That single decision makes the entire platform:

- safer
- more observable
- more extensible
- easier to reason about

The Runtime executes capabilities.

The manifest explains what those capabilities are.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`01-extension-philosophy.md`

**Next File**

`03-discovery.md`
