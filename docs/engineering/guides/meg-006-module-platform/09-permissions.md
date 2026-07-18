<!--
File: docs/engineering/guides/meg-006-module-platform/09-permissions.md
Document: MEG-006
Status: Draft
-->

# Permissions

> *Capabilities should receive only the authority required to fulfil their purpose. Nothing more.*

---

# Purpose

Not every capability should have unrestricted access to the Runtime. One capability reads Blob Storage, another is scheduling work, publishing Runtime Events, accessing metadata providers or communicating over the network, and each of those is a distinct piece of authority rather than a single undifferentiated grant. The Runtime must ensure that capabilities receive only the permissions necessary to perform their declared responsibilities, which makes permissions one of the primary security boundaries of the Module Platform.

---

# Philosophy

Within Mosaic:

> **Authority is granted deliberately. It is never assumed.**

Capabilities should begin with no permissions at all, and every permission a capability ends up holding should have been requested, declared, validated and granted. The Runtime should never infer capability permissions from implementation, so permissions remain explicit. The principle of least privilege is widely recognised as the foundation of secure module platforms because it limits the impact of compromised or malicious modules. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions))

---

# Permission Model

Permissions describe:

> **What a capability may access.**

They do **not** describe:

> **What the capability does.**

Business behaviour belongs to the capability, whereas authority belongs to the Runtime.

---

# Capability Permission Declarations

Every capability should declare its required permissions inside its manifest, as in the following example.

```yaml
permissions:
  - scheduler.use
  - blob.read
  - metadata.fetch
```

The Runtime evaluates these declarations during activation, and permissions are never discovered dynamically.

---

# Least Privilege

Capabilities should request the minimum authority required. A capability that needs only to read stored objects should declare exactly that:

```yaml
permissions:
  - blob.read
```

rather than claiming a whole namespace, which is the poor alternative:

```yaml
permissions:
  - blob.*
```

Narrow permissions should be the default and broad permissions should be exceptional, because requesting only the permissions required for functionality improves security and makes platform behaviour easier to reason about. ([Chrome for Developers](https://developer.chrome.com/docs/modules/develop/concepts/declare-permissions?hl=en))

---

# Permission Categories

Permissions naturally fall into several categories — Runtime, Platform, Storage, Network, Capability and Observability — and each category describes one class of Runtime authority. The sections that follow take them in turn.

---

# Runtime Permissions

Runtime permissions provide controlled access to Runtime services, and include `scheduler.use`, `execution.submit`, `events.publish` and `events.subscribe`. Capabilities should never access Runtime internals directly, because permissions always mediate Runtime interaction.

---

# Platform Permissions

Platform permissions expose shared platform facilities such as `configuration.read`, `health.report` and `logging.write`. These services are intentionally provided through the SDK, so permissions determine access to them.

---

# Storage Permissions

Storage permissions control access to persistent resources, and include `blob.read`, `blob.write`, `filesystem.read` and `filesystem.write`. Rather than exposing broad storage authority, the Runtime should distinguish read from write and both from delete.

---

# Network Permissions

Some capabilities require external communication, which the `network.outbound` permission grants. The Runtime should support future scoping, so that conceptually a permission could name the hosts a capability is allowed to reach:

```yaml
network:
  hosts:
    - api.themoviedb.org
    - api.anilist.co
```

Capabilities should not automatically receive unrestricted network access, because granular host-level permissions are increasingly regarded as a security best practice for module ecosystems. ([Chrome for Developers](https://developer.chrome.com/docs/modules/develop/concepts/declare-permissions?hl=en))

---

# Capability Contract Permissions

Capabilities may expose contracts consumed by other capabilities, declared in the manifest:

```yaml
consumes:
  - MetadataProvider
```

Possessing a contract does **not** automatically imply permission to invoke it, and the Runtime may require an explicit capability-level permission such as `capability.metadata.use` alongside the declared dependency. This separates dependency resolution from authorisation, and those two concerns should remain independent.

---

# Observability Permissions

Capabilities should explicitly declare access to operational facilities such as `metrics.publish`, `trace.write` and `logs.write`. Observability should remain intentional rather than automatic.

---

# Permission Granting

The Runtime grants permissions during activation: the manifest is read, the permissions it declares go through permission validation, and only then is the capability activated. Capabilities should never request additional permissions dynamically unless the Runtime explicitly supports optional permission flows.

---

# Permission Enforcement

Permissions should be enforced by SDK contracts, which places the check at the point of use rather than inside the capability. Consider a capability that calls:

```go
ctx.BlobStore()
```

Without the `blob.read` permission the SDK rejects the request. Capabilities should therefore not perform permission checks themselves, because the Runtime owns enforcement.

---

# Permission Denial

When the SDK denies a request a capability has made, the Runtime should provide clear diagnostics, structured errors and operator visibility. Silent failures should be avoided.

---

# Optional Permissions

The Runtime may support optional permissions, declared separately from the required ones:

```yaml
optionalPermissions:
  - network.outbound
```

Operators may enable these later without modifying the capability itself, and optional permissions should remain explicit rather than implicit.

---

# Permission Evolution

Permissions should evolve conservatively. Adding a new permission should generally require a manifest update, Runtime validation and operator approval, so that capabilities never silently gain additional authority following an upgrade and permission expansion remains visible.

---

# Runtime Isolation

Permissions complement Runtime isolation, because even if a capability is compromised its authority remains limited to the permissions that were declared and granted. Runtime isolation and least privilege work together, and neither replaces the other.

---

# Diagnostics

The Runtime should expose granted permissions, denied permissions, unused permissions and permission failures, because operators should always be able to answer one question:

> **Why does this capability have this authority?**

Permission state should remain fully observable.

---

# Marketplace

Marketplace tooling should display the requested permissions, a description of each and the justification for it, and module authors should be able to explain:

> **Why is this permission required?**

Permission transparency improves trust, and modern module ecosystems increasingly encourage or require authors to explain permission requests to users. ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions))

---

# Future Permissions

The permission model should remain extensible. Future categories may include AI models, GPU execution, hardware devices, media decoders and external authentication, and the Runtime should evolve by introducing new permission types rather than broadening existing ones.

---

# Anti-Patterns

The following practices are prohibited.

## Implicit Permissions

Granting authority because a capability "probably needs it."

---

## Wildcard Permissions

Declaring `runtime.*` without strong architectural justification.

---

## Runtime Bypass

Capabilities accessing Runtime internals directly.

---

## Self-Elevation

Capabilities requesting additional authority during execution.

---

## Permission Inference

The Runtime analysing implementation to determine required permissions, when permissions must instead remain manifest driven.

---

## Permanent Broad Authority

Granting unrestricted access when narrower permissions exist.

---

# Mosaic Guidelines

Within Mosaic:

- Every permission must be declared explicitly.
- The Runtime must enforce least privilege.
- Permissions must be granted before execution.
- SDK contracts must enforce permission boundaries.
- Permission denial must remain observable.
- Optional permissions should remain explicit.
- Permission changes should require manifest updates.
- Capabilities must not bypass Runtime permission enforcement.

---

# Relationship to MEG

The Module SDK defines:

> **How capabilities interact with the Runtime.**

Permissions define:

> **Which Runtime capabilities they are authorised to use.**

The next chapter introduces **Configuration**, defining how capabilities receive validated configuration from the Runtime while remaining independent of configuration storage and deployment mechanisms.

---

# Summary

Permissions define the authority of a capability rather than its behaviour. Within Mosaic manifests declare permissions, the Runtime validates them, the SDK enforces them and capabilities consume them, and that separation preserves one of the platform's most important architectural guarantees:

> **No capability should possess more authority than it explicitly requested and the Runtime explicitly granted.**
