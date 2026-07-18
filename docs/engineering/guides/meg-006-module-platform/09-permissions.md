<!--
File: docs/engineering/guides/meg-006-module-platform/09-permissions.md
Document: MEG-006
Status: Draft
-->

# Permissions

> *Capabilities should receive only the authority required to fulfil their purpose. Nothing more.*

---

# Purpose

Not every capability should have unrestricted access to the Runtime.

Examples include:

- reading Blob Storage
- scheduling work
- publishing Runtime Events
- accessing metadata providers
- communicating over the network

The Runtime must ensure that capabilities receive only the permissions necessary to perform their declared responsibilities.

Permissions therefore form one of the primary security boundaries of the Module Platform.

---

# Philosophy

Within Mosaic:

> **Authority is granted deliberately. It is never assumed.**

Capabilities should begin with:

```

No Permissions
```

Every permission should be:

- requested
- declared
- validated
- granted

The Runtime should never infer capability permissions from implementation.

Permissions should remain explicit.

The principle of least privilege is widely recognised as the foundation of secure module platforms because it limits the impact of compromised or malicious modules.  [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)

---

# Permission Model

Permissions describe:

> **What a capability may access.**

They do **not** describe:

> **What the capability does.**

Business behaviour belongs to the capability.

Authority belongs to the Runtime.

---

# Capability Permission Declarations

Every capability SHOULD declare its required permissions inside its manifest.

Example.

```yaml
permissions:

  - scheduler.use

  - blob.read

  - metadata.fetch
```

The Runtime evaluates these declarations during activation.

Permissions are never discovered dynamically.

---

# Least Privilege

Capabilities should request the minimum authority required.

Good.

```yaml
permissions:

  - blob.read
```

Poor.

```yaml
permissions:

  - blob.*
```

Broad permissions should be exceptional.

Narrow permissions should be the default.

Requesting only the permissions required for functionality improves security and makes platform behaviour easier to reason about.  [Chrome for Developers](https://developer.chrome.com/docs/modules/develop/concepts/declare-permissions?hl=en)

---

# Permission Categories

Permissions naturally fall into several categories.

```mermaid
flowchart TD

N1["Runtime"]
N2["Platform"]
N3["Storage"]
N4["Network"]
N5["Capability"]
N6["Observability"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Each category describes one class of Runtime authority.

---

# Runtime Permissions

Runtime permissions provide controlled access to Runtime services.

Examples include:

```yaml
scheduler.use
```

```yaml
execution.submit
```

```yaml
events.publish
```

```yaml
events.subscribe
```

Capabilities should never access Runtime internals directly.

Permissions always mediate Runtime interaction.

---

# Platform Permissions

Platform permissions expose shared platform facilities.

Examples include:

```yaml
configuration.read
```

```yaml
health.report
```

```yaml
logging.write
```

These services are intentionally provided through the SDK.

Permissions determine access.

---

# Storage Permissions

Storage permissions control access to persistent resources.

Examples include:

```yaml
blob.read
```

```yaml
blob.write
```

```yaml
filesystem.read
```

```yaml
filesystem.write
```

The Runtime should distinguish:

- read
- write
- delete

rather than exposing broad storage authority.

---

# Network Permissions

Some capabilities require external communication.

Example.

```yaml
network.outbound
```

The Runtime SHOULD support future scoping.

Conceptually.

```yaml
network:

  hosts:

    - api.themoviedb.org

    - api.anilist.co
```

Capabilities should not automatically receive unrestricted network access.

Granular host-level permissions are increasingly regarded as a security best practice for module ecosystems.  [Chrome for Developers](https://developer.chrome.com/docs/modules/develop/concepts/declare-permissions?hl=en)

---

# Capability Contract Permissions

Capabilities may expose contracts consumed by other capabilities.

Example.

```yaml
consumes:

  - MetadataProvider
```

Possessing a contract does **not** automatically imply permission to invoke it.

The Runtime may require explicit capability-level permissions.

Example.

```yaml
capability.metadata.use
```

This separates:

- dependency resolution
- authorisation

These concerns should remain independent.

---

# Observability Permissions

Capabilities SHOULD explicitly declare access to operational facilities.

Examples include:

```yaml
metrics.publish
```

```yaml
trace.write
```

```yaml
logs.write
```

Observability should remain intentional.

Not automatic.

---

# Permission Granting

The Runtime grants permissions during activation.

```mermaid
flowchart TD

N1["Manifest"]
N2["Permission Validation"]
N3["Capability Activated"]

N1 --> N2
N2 --> N3
```

Capabilities should never request additional permissions dynamically unless the Runtime explicitly supports optional permission flows.

---

# Permission Enforcement

Permissions SHOULD be enforced by SDK contracts.

Example.

```go
ctx.BlobStore()
```

Without:

```yaml
blob.read
```

permission:

The SDK rejects the request.

Capabilities should not perform permission checks themselves.

The Runtime owns enforcement.

---

# Permission Denial

When permission is denied:

```mermaid
flowchart TD

N1["Capability"]
N2["SDK"]
N3["Permission Denied"]

N1 --> N2
N2 --> N3
```

The Runtime should provide:

- clear diagnostics
- structured errors
- operator visibility

Silent failures should be avoided.

---

# Optional Permissions

The Runtime MAY support optional permissions.

Example.

```yaml
optionalPermissions:

  - network.outbound
```

Operators may enable these later without modifying the capability itself.

Optional permissions should remain explicit.

Not implicit.

---

# Permission Evolution

Permissions should evolve conservatively.

Adding new permissions should generally require:

- manifest update
- Runtime validation
- operator approval

Capabilities should never silently gain additional authority following an upgrade.

Permission expansion should remain visible.

---

# Runtime Isolation

Permissions complement Runtime isolation.

Even if a capability is compromised:

Its authority remains limited to:

- declared
- granted

permissions.

Runtime isolation and least privilege work together.

Neither replaces the other.

---

# Diagnostics

The Runtime SHOULD expose:

- granted permissions
- denied permissions
- unused permissions
- permission failures

Operators should always understand:

> **Why does this capability have this authority?**

Permission state should remain fully observable.

---

# Marketplace

Marketplace tooling SHOULD display:

- requested permissions
- permission descriptions
- justification

Module authors should explain:

> **Why is this permission required?**

Permission transparency improves trust.

Modern module ecosystems increasingly encourage or require authors to explain permission requests to users.  [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)

---

# Future Permissions

The permission model should remain extensible.

Future categories may include:

- AI models
- GPU execution
- hardware devices
- media decoders
- external authentication

The Runtime should evolve by introducing new permission types rather than broadening existing ones.

---

# Anti-Patterns

The following practices are prohibited.

## Implicit Permissions

Granting authority because a capability "probably needs it."

---

## Wildcard Permissions

```yaml
runtime.*
```

without strong architectural justification.

---

## Runtime Bypass

Capabilities accessing Runtime internals directly.

---

## Self-Elevation

Capabilities requesting additional authority during execution.

---

## Permission Inference

The Runtime analysing implementation to determine required permissions.

Permissions must remain manifest driven.

---

## Permanent Broad Authority

Granting unrestricted access when narrower permissions exist.

---

# Mosaic Guidelines

Within Mosaic:

- Every permission MUST be declared explicitly.
- The Runtime MUST enforce least privilege.
- Permissions MUST be granted before execution.
- SDK contracts MUST enforce permission boundaries.
- Permission denial MUST remain observable.
- Optional permissions SHOULD remain explicit.
- Permission changes SHOULD require manifest updates.
- Capabilities MUST NOT bypass Runtime permission enforcement.

---

# Relationship to MEG

The Module SDK defines:

> **How capabilities interact with the Runtime.**

Permissions define:

> **Which Runtime capabilities they are authorised to use.**

The next chapter introduces **Configuration**, defining how capabilities receive validated configuration from the Runtime while remaining independent of configuration storage and deployment mechanisms.

---

# Summary

Permissions define the authority of a capability.

Not its behaviour.

Within Mosaic:

- manifests declare permissions
- the Runtime validates permissions
- the SDK enforces permissions
- capabilities consume permissions

This separation preserves one of the platform's most important architectural guarantees:

> **No capability should possess more authority than it explicitly requested and the Runtime explicitly granted.**
