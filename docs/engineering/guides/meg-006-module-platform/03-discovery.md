<!--
File: docs/engineering/guides/meg-006-module-platform/03-discovery.md
Document: MEG-006
Status: Draft
-->

# Discovery

> *A Module cannot participate in Mosaic until the Supervisor has resolved its manifest.*

---

# Purpose

The Module Manifest defines **what** a Module contributes, whereas Discovery defines **how** the Supervisor finds it before build-time composition. The Discovery process is responsible for locating every selected Module before the Build Pipeline creates a Platform package, and it is deliberately kept separate from registration, dependency resolution, activation and execution. A discovered Module is not yet trusted; it is merely known.

---

# Philosophy

Within Mosaic:

> **Discovery identifies Modules. It never executes them.**

The Supervisor should discover manifests, metadata, dependencies and contracts without loading any executable code, so that a Module is completely understood before the Build Pipeline is invoked.

---

# Discovery Pipeline

Every selected Module follows the same discovery pipeline.

```mermaid
flowchart TD

N1["Locate Manifest"]
N2["Read Manifest"]
N3["Validate Manifest"]
N4["Create Module Descriptor"]
N5["Dependency Resolver"]
N6["Ready For Build Workspace"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Execution has not begun at any point along that path, because only metadata has been processed.

---

# Discovery Before Execution

One of the most important Runtime guarantees is the fixed order in which a capability advances towards execution.

```mermaid
flowchart TD

N1["Discovery"]
N2["Validation"]
N3["Registration"]
N4["Activation"]
N5["Execution"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

A capability should never execute simply because it exists on disk. The Supervisor must first determine what it is, whether it is valid and whether it is compatible.

---

# Discovery Sources

Modules may be discovered from multiple sources. Examples include:

- Platform Capability
- Modules Directory
- Marketplace Cache
- Enterprise Repository
- Development Workspace

Regardless of origin, every selected Module enters the Build Pipeline through the same discovery process.

---

# Manifest Source Discovery

The default discovery mechanism is manifest resolution from configured sources, which conceptually looks like this:

```text
module-index/
    anilist.yaml
    jellyfin.yaml
    tmdb.yaml
```

The Supervisor reads manifests from selected Module sources and should not inspect executable code during discovery, because manifest parsing is what separates selection and validation from build-time composition.

---

# Module Catalogue

The Module Catalogue is the metadata-only view of Modules available from configured discovery sources. The Supervisor queries the Module Catalogue during onboarding so the Shell can present current feature, provider and optional Module choices, and because catalogue entries are derived from Module manifests, the Shell must not maintain a separate hardcoded list of available Modules. Adding a manifest to a configured discovery source should therefore make that Module available as a selection candidate without requiring a Shell release.

Catalogue presence does not establish compatibility, and catalogue discovery does not:

- download or execute Module code
- register Modules with the Platform
- activate capabilities
- guarantee that a selected Module is compatible

Selection creates desired composition input, but manifest admission, dependency resolution and SDK compatibility validation still occur before the Build Pipeline is invoked.

---

# Build Workspace Preparation

After discovery and dependency resolution, the Supervisor invokes the Build Pipeline to prepare a temporary build workspace, conceptually:

```text
workspace/
    platform/
    sdk/
    modules/
    generated/
```

The Supervisor must ensure that composition does not modify the Platform source repository or Module source repositories. The Build Pipeline uses the temporary workspace to:

1. resolve selected Go modules,
2. update the temporary `go.mod`,
3. generate `imports.go`,
4. build the Platform Binary.

The workspace is an assembly area, not a new source of architectural truth.

---

# Built-In Capability Discovery

Platform capabilities participate in discovery exactly like modules, carrying their own `capability.yaml` alongside the Platform source.

```text
platform/
    playback/
        capability.yaml
    metadata/
        capability.yaml
```

The Supervisor should not maintain a special discovery path for built-in capabilities, because built-in capabilities differ only in delivery. Architecturally, it remains another capability.

---

# Manifest Discovery

Discovery operates entirely on manifests: a Capability reaches the Runtime through its `capability.yaml` and through nothing else. No Go code should execute, no modules should load and no lifecycle methods should run, because discovery should remain metadata driven.

---

# Capability Descriptor

Following successful discovery, the Supervisor constructs a Module Descriptor, which conceptually carries the following.

```mermaid
flowchart TD

N1["Module Descriptor"]
N2["Identity"]
N3["Version"]
N4["Dependencies"]
N5["Permissions"]
N6["Contracts"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Descriptor becomes the Supervisor's internal representation of the Module during composition, which means the manifest itself is no longer required for most Runtime operations.

---

# Discovery Validation

Discovery performs structural validation only. Examples include:

- manifest exists
- schema valid
- required fields present
- identifier valid
- version valid

Discovery should **not** validate dependency compatibility, permission approval or Runtime contracts. Those occur during later stages, because each phase should own one responsibility.

---

# Duplicate Detection

Discovery must detect duplicate capability identifiers, because two capabilities both claiming `metadata` leave the Runtime with no way to say which one owns the name. The Runtime should reject ambiguous capability identities, so identifiers must remain globally unique within one Runtime instance.

---

# Discovery Errors

Discovery failures should be explicit. Examples include:

- missing manifest
- malformed manifest
- unsupported schema version
- duplicate identifier

Capabilities failing discovery should never progress further into the Runtime lifecycle.

---

# Discovery Order

Discovery order should not matter: whether Playback is discovered before Metadata or Metadata before Playback, the resulting Capability Registry should be identical. Ordering should become relevant only during dependency resolution.

---

# Lazy Discovery

The Supervisor may support lazy manifest retrieval for specialised deployment models, where a manifest is discovered from a Marketplace and the capability downloaded before registration.

```mermaid
flowchart TD

N1["Marketplace"]
N2["Discover Manifest"]
N3["Download Capability"]
N4["Register"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Platform package preparation should nevertheless prefer discovering every selected Module before the Build Pipeline begins, because predictability outweighs marginal startup optimisation.

---

# Discovery Metadata

Discovery should record:

- source
- manifest version
- discovery timestamp
- capability location

This metadata improves diagnostics, auditing and marketplace tooling, but it should not influence business behaviour.

---

# Discovery Events

The Supervisor may record events describing discovery for diagnostics, such as `CapabilityDiscovered`, `CapabilityRejected` and `ManifestValidated`. These are operational events, not Domain Events.

---

# Discovery Performance

Discovery should remain inexpensive. The Runtime should parse manifests and metadata while avoiding reflection, package loading, dependency injection and executable inspection, because build preparation performance depends heavily upon efficient discovery.

---

# Discovery Caching

The Supervisor may cache discovery results such as manifest hashes, parsed descriptors and schema validation. Caching should never bypass validation after a manifest changes, because correctness always outweighs startup speed.

---

# Runtime Visibility

Operators should be able to answer:

- Which capabilities were discovered?
- Which failed discovery?
- Why were they rejected?
- Where were they found?

Discovery should therefore remain fully observable, because hidden discovery behaviour inevitably complicates debugging.

---

# Security

Discovery should treat every capability as untrusted. Until validation, dependency resolution and permission evaluation complete successfully, the Runtime should assume the capability cannot execute. Trust should be earned, not assumed.

---

# Anti-Patterns

The following practices are prohibited.

## Executing During Discovery

Loading Go code merely to inspect a capability. This defeats the guarantee that discovery identifies Modules without ever executing them.

---

## Reflection-Based Discovery

Requiring executable inspection to determine metadata. Discovery should remain metadata driven, and reflection sits among the operations the Runtime is expected to avoid.

---

## Implicit Registration

Automatically registering discovered capabilities without validation. Discovery and registration are separate phases, and a discovered Module is not yet trusted.

---

## Runtime Side Effects

Discovery modifying Runtime state beyond the Capability Registry. Discovery exists to answer what capabilities are available and nothing more.

---

## Discovery Ordering Dependencies

Assuming discovery sequence determines execution behaviour. Discovery order should not matter, and ordering becomes relevant only during dependency resolution.

---

## Multiple Discovery Mechanisms

Different capability types using fundamentally different discovery pipelines. Every capability should follow one canonical process, because built-in and module-delivered capabilities differ only in delivery.

---

# Mosaic Guidelines

Within Mosaic:

- Discovery must occur before execution.
- Discovery must operate on manifests rather than executable code.
- Every capability must produce a Capability Descriptor.
- Duplicate identifiers must be rejected.
- Discovery should remain deterministic.
- Discovery should remain observable.
- Built-in and module-delivered capabilities must use the same discovery pipeline.
- Discovery must treat capabilities as untrusted until later validation stages.

---

# Relationship to MEG

The Capability Manifest defines:

> **What a capability declares.**

Discovery determines:

> **How the Runtime finds those declarations.**

The next chapter introduces **Registration**, where successfully discovered capabilities become recognised participants within the Runtime and enter the Capability Registry.

---

# Summary

Discovery is the Runtime's first interaction with every capability, and it should answer one question:

> **What capabilities are available to this Runtime?**

Nothing more. By separating discovery from validation, activation and execution, the Mosaic Runtime remains predictable, observable and secure while allowing the platform to grow through independently developed capabilities.
