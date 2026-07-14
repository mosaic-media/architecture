<!--
File: docs/engineering/guides/meg-006-module-platform/03-discovery.md
Document: MEG-006
Status: Draft
Version: 0.2
-->

# Discovery

> *A capability cannot participate in the platform until the Runtime knows it exists.*

---

# Purpose

The Capability Manifest defines **what** a capability is.

Discovery defines **how** the Runtime finds it.

The Discovery process is responsible for locating every capability available to the platform before Runtime startup continues.

Discovery is intentionally separated from:

- registration
- dependency resolution
- activation
- execution

A discovered capability is not yet trusted.

It is merely known.

---

# Philosophy

Within Mosaic:

> **Discovery identifies capabilities. It never executes them.**

The Runtime should discover:

- manifests
- metadata
- dependencies
- contracts

without loading any executable code.

A capability should be completely understood before activation begins.

---

# Discovery Pipeline

Every capability follows the same discovery pipeline.

```
Locate

↓

Read Manifest

↓

Validate Manifest

↓

Create Capability Descriptor

↓

Capability Registry

↓

Ready For Registration
```

Execution has not yet begun.

Only metadata has been processed.

---

# Discovery Before Execution

One of the most important Runtime guarantees is:

```
Discovery

↓

Validation

↓

Registration

↓

Activation

↓

Execution
```

A capability should never execute simply because it exists on disk.

The Runtime must first determine:

- what it is
- whether it is valid
- whether it is compatible

---

# Discovery Sources

Capabilities MAY be discovered from multiple sources.

Examples include:

```
Platform Capability
```

```
Modules Directory
```

```
Marketplace Cache
```

```
Enterprise Repository
```

```
Development Workspace
```

Regardless of origin:

Every capability enters the Runtime through the same discovery process.

---

# Filesystem Discovery

The default discovery mechanism is filesystem scanning.

Conceptually.

```
modules/

    playback/

        capability.yaml

    metadata/

        capability.yaml

    books/

        capability.yaml
```

The Runtime searches configured discovery locations for manifests.

It should not inspect executable code during discovery.

Filesystem scanning combined with manifest parsing is one of the most common approaches used by extensible platforms because it separates discovery from activation.  [zylos.ai](https://zylos.ai/research/2026-02-21-ai-agent-plugin-extension-architecture/)

---

# Built-In Capability Discovery

Platform capabilities participate in discovery exactly like modules.

Example.

```
platform/

    playback/

        capability.yaml

    metadata/

        capability.yaml
```

The Runtime should not maintain a special discovery path for built-in capabilities.

Built-in capabilities differ only in delivery.

Architecturally, it remains another capability.

---

# Manifest Discovery

Discovery operates entirely on manifests.

Example.

```
Capability

↓

capability.yaml

↓

Runtime
```

No Go code should execute.

No modules should load.

No lifecycle methods should run.

Discovery should remain metadata driven.

---

# Capability Descriptor

Following successful discovery, the Runtime constructs a Capability Descriptor.

Conceptually.

```
Capability Descriptor

↓

Identity

↓

Version

↓

Dependencies

↓

Permissions

↓

Contracts
```

The Descriptor becomes the Runtime's internal representation of the capability.

The manifest itself is no longer required for most Runtime operations.

---

# Discovery Validation

Discovery performs structural validation only.

Examples include:

- manifest exists
- schema valid
- required fields present
- identifier valid
- version valid

Discovery should **not** validate:

- dependency compatibility
- permission approval
- Runtime contracts

Those occur during later stages.

Each phase should own one responsibility.

---

# Duplicate Detection

Discovery MUST detect duplicate capability identifiers.

Poor.

```
metadata

↓

metadata
```

The Runtime should reject ambiguous capability identities.

Identifiers must remain globally unique within one Runtime instance.

---

# Discovery Errors

Discovery failures should be explicit.

Examples include:

- missing manifest
- malformed manifest
- unsupported schema version
- duplicate identifier

Capabilities failing discovery should never progress further into the Runtime lifecycle.

---

# Discovery Order

Discovery order should not matter.

Suppose:

```
Playback

↓

Metadata
```

or

```
Metadata

↓

Playback
```

The resulting Capability Registry should be identical.

Ordering should become relevant only during dependency resolution.

---

# Lazy Discovery

The Runtime MAY support lazy discovery for specialised deployment models.

Example.

```
Marketplace

↓

Discover Manifest

↓

Download Capability

↓

Register
```

However:

Platform Runtime startup should generally prefer discovering every available capability before activation begins.

Predictability outweighs marginal startup optimisation.

---

# Discovery Metadata

Discovery SHOULD record:

- source
- manifest version
- discovery timestamp
- capability location

This metadata improves:

- diagnostics
- auditing
- marketplace tooling

It should not influence business behaviour.

---

# Discovery Events

The Runtime MAY publish Runtime Events describing discovery.

Examples include:

```
CapabilityDiscovered
```

```
CapabilityRejected
```

```
ManifestValidated
```

These are operational events.

Not Domain Events.

---

# Discovery Performance

Discovery should remain inexpensive.

The Runtime should parse:

- manifests
- metadata

It should avoid:

- reflection
- package loading
- dependency injection
- executable inspection

Startup performance depends heavily upon efficient discovery.

---

# Discovery Caching

The Runtime MAY cache discovery results.

Examples include:

- manifest hashes
- parsed descriptors
- schema validation

Caching should never bypass validation after a manifest changes.

Correctness always outweighs startup speed.

---

# Runtime Visibility

Operators should be able to answer:

- Which capabilities were discovered?
- Which failed discovery?
- Why were they rejected?
- Where were they found?

Discovery should remain fully observable.

Hidden discovery behaviour inevitably complicates debugging.

---

# Security

Discovery should treat every capability as untrusted.

Until:

- validation
- dependency resolution
- permission evaluation

complete successfully,

the Runtime should assume the capability cannot execute.

Trust should be earned.

Not assumed.

---

# Anti-Patterns

The following practices are prohibited.

## Executing During Discovery

Loading Go code merely to inspect a capability.

---

## Reflection-Based Discovery

Requiring executable inspection to determine metadata.

---

## Implicit Registration

Automatically registering discovered capabilities without validation.

---

## Runtime Side Effects

Discovery modifying Runtime state beyond the Capability Registry.

---

## Discovery Ordering Dependencies

Assuming discovery sequence determines execution behaviour.

---

## Multiple Discovery Mechanisms

Different capability types using fundamentally different discovery pipelines.

Every capability should follow one canonical process.

---

# Mosaic Guidelines

Within Mosaic:

- Discovery MUST occur before execution.
- Discovery MUST operate on manifests rather than executable code.
- Every capability MUST produce a Capability Descriptor.
- Duplicate identifiers MUST be rejected.
- Discovery SHOULD remain deterministic.
- Discovery SHOULD remain observable.
- Built-in and module-delivered capabilities MUST use the same discovery pipeline.
- Discovery MUST treat capabilities as untrusted until later validation stages.

---

# Relationship to MEG

The Capability Manifest defines:

> **What a capability declares.**

Discovery determines:

> **How the Runtime finds those declarations.**

The next chapter introduces **Registration**, where successfully discovered capabilities become recognised participants within the Runtime and enter the Capability Registry.

---

# Summary

Discovery is the Runtime's first interaction with every capability.

It should answer one question:

> **What capabilities are available to this Runtime?**

Nothing more.

By separating discovery from validation, activation and execution, the Mosaic Runtime remains predictable, observable and secure while allowing the platform to grow through independently developed capabilities.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`02-module-manifest.md`

**Next File**

`04-registration.md`
