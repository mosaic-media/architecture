<!--
File: docs/engineering/guides/meg-009-security-architecture/05-capability-permissions.md
Document: MEG-009
Status: Draft
-->

# Capability Permissions

> *Capabilities should possess only the authority required to fulfil their purpose. Nothing more.*

---

# Purpose

The Runtime executes many capabilities.

Examples include:

- Playback
- Library
- Metadata
- Recommendations
- Books
- Music
- Third-party modules

Every capability requires some degree of authority.

Examples include:

- scheduling work
- reading Blob Storage
- publishing Runtime Events
- accessing external networks

Without explicit permission boundaries:

- capabilities become over-privileged
- Runtime isolation weakens
- security becomes implicit

This document defines the Runtime permission model governing every capability executed by Mosaic.

---

# Philosophy

Within Mosaic:

> **Capabilities begin with zero authority. Every permission is granted explicitly by the Runtime.**

A capability should never possess authority because of:

- installation
- publisher
- implementation
- convenience

Authority is granted only because:

- it is declared
- it is reviewed
- it is approved
- it is required

Capability permissions are separate from user authorisation. A user permitted to perform an operation does not grant the executing Module unrestricted Platform access, and a Module permission does not grant a user authority.

The Platform evaluates user and device authority through the Policy Decision Point described by [04 — Authorisation](04-authorisation.md), then separately constructs the capability environment from the Module manifest and approved capability permissions.

---

# Permission Hierarchy

Capability permissions follow a simple lifecycle.

```mermaid
flowchart TD

N1["Manifest"]
N2["Validation"]
N3["Approval"]
N4["Activation"]
N5["Enforcement"]
N6["Revocation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Every stage owns one security responsibility.

---

# Capability Identity

Permissions always belong to one capability.

Example.

```mermaid
flowchart TD

N1["Metadata"]
N2["blob.read"]

N1 --> N2
```

Permissions never belong to:

- assemblies
- packages
- repositories

Capabilities are the architectural security boundary.

---

# Manifest Declaration

Every capability MUST declare its permissions.

Example.

```yaml
permissions:

  - blob.read

  - scheduler.use

  - events.publish
```

The manifest remains the authoritative declaration of requested authority.

The Runtime never infers permissions from implementation.

---

# Zero Trust

New capabilities begin with:

```text
No Permissions
```

They should not automatically receive:

- storage access
- network access
- Runtime services
- secrets

Everything must be requested explicitly.

---

# Least Privilege

Permissions SHOULD remain as narrow as possible.

Preferred.

```yaml
permissions:

  - blob.read
```

Avoid.

```yaml
permissions:

  - blob.*
```

Smaller permission surfaces reduce:

- accidental misuse
- privilege escalation
- security review complexity

---

# Permission Categories

Capability permissions naturally group into several categories.

```mermaid
flowchart TD

N1["Runtime"]
N2["Storage"]
N3["Network"]
N4["Observability"]
N5["Capability"]
N6["Administrative"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Each category protects one architectural responsibility.

---

# Runtime Permissions

Runtime permissions provide controlled access to Runtime Services.

Examples include:

```text
scheduler.use
```

```text
events.publish
```

```text
events.subscribe
```

```text
execution.submit
```

Capabilities interact through Runtime contracts.

Permissions determine which contracts may be used.

---

# Storage Permissions

Storage permissions govern access to persistent information.

Examples include:

```text
blob.read
```

```text
blob.write
```

```text
archive.import
```

```text
archive.export
```

Repositories continue enforcing business ownership.

Permissions determine whether storage services are available at all.

---

# Network Permissions

Capabilities requiring external communication MUST declare it.

Example.

```yaml
network:

  outbound:

    - api.themoviedb.org

    - graphql.anilist.co
```

The Runtime SHOULD support host-level restrictions.

Capabilities should never receive unrestricted outbound access unless explicitly required.

---

# Capability Contract Permissions

Capabilities may consume contracts exposed by other capabilities.

Example.

```text
MetadataProvider
```

Consumption SHOULD require explicit declaration.

The Runtime resolves:

- dependency

and

- authority

independently.

A capability depending upon another capability does not automatically receive permission to invoke it.

---

# Observability Permissions

Capabilities SHOULD request observability access explicitly.

Examples include:

```text
logs.write
```

```text
metrics.publish
```

```text
traces.create
```

The Runtime owns telemetry infrastructure.

Capabilities receive only the observability facilities they require.

---

# Administrative Permissions

Very few capabilities should possess administrative authority.

Examples include:

```text
runtime.configuration.write
```

```text
capability.install
```

```text
diagnostics.read
```

Administrative permissions SHOULD remain exceptional.

Most capabilities should never require them.

---

# Permission Grant

Permission granting occurs during activation.

```mermaid
flowchart TD

N1["Manifest"]
N2["Validate"]
N3["Approve"]
N4["Inject Runtime Contracts"]
N5["Capability Ready"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Runtime injects only the services authorised by the granted permissions.

Capabilities should never receive unavailable services.

---

# Permission Enforcement

Permissions SHOULD be enforced by the SDK.

Example.

```go
ctx.BlobStore()
```

Without:

```text
blob.read
```

↓

Permission denied.

Capabilities should not implement permission checks themselves.

The Runtime owns enforcement.

---

# Runtime Contracts

Permissions determine Runtime contract availability.

Example.

Without:

```text
scheduler.use
```

↓

No Scheduler contract.

Without:

```text
events.publish
```

↓

No Publisher contract.

This creates a naturally secure programming model.

Unavailable authority simply does not exist.

---

# Permission Revocation

Permissions SHOULD remain revocable.

Example.

```mermaid
flowchart TD

N1["Capability Disabled"]
N2["Permissions Revoked"]
N3["Contracts Removed"]
N4["Execution Stops"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Revocation should occur without Runtime restart wherever practical.

Authority should disappear immediately.

---

# Runtime Visibility

Operators SHOULD inspect:

- granted permissions
- denied permissions
- unused permissions
- revoked permissions

The Runtime should answer:

> **Why does this capability possess this authority?**

Security should remain explainable.

---

# Marketplace Review

Marketplace tooling SHOULD display:

- requested permissions
- permission descriptions
- justification

Operators should understand permission requests before installation.

Installation should never become blind trust.

---

# Permission Evolution

Adding permissions SHOULD require:

- manifest update
- Runtime validation
- operator approval

Capabilities should never silently gain authority after upgrade.

Permission expansion should remain visible.

---

# Secrets

Permissions do not expose secrets.

Possessing:

```text
metadata.fetch
```

does not imply access to:

- API keys
- OAuth tokens
- credentials

Secrets remain Runtime owned.

Permissions grant capability.

Not confidential information.

---

# Security Telemetry

Permission evaluation SHOULD generate:

- logs
- metrics
- traces
- audit events

Examples include:

```text
PermissionGranted
```

```text
PermissionDenied
```

```text
PermissionRevoked
```

Operators should understand permission activity continuously.

---

# Testing

Capability permissions SHOULD be tested.

Typical tests verify:

- permission grants
- permission denial
- SDK enforcement
- Runtime contract availability
- permission revocation

Security should remain deterministic.

Testing should reinforce Runtime trust.

---

# Anti-Patterns

The following practices are prohibited.

## Runtime Discovery

Capabilities discovering privileged Runtime services dynamically.

---

## Permission Inference

Granting permissions because implementation appears to require them.

---

## Wildcard Permissions

Granting unrestricted authority without architectural justification.

---

## Capability Self-Elevation

Capabilities requesting additional permissions during execution.

---

## Shared Permissions

Granting one capability authority because another capability requires it.

---

## Permission Checks Inside Business Logic

Capabilities repeatedly checking permissions instead of relying upon Runtime-enforced contracts.

---

# Mosaic Guidelines

Within Mosaic:

- Capabilities MUST begin with zero authority.
- Permissions MUST be declared in manifests.
- Runtime MUST enforce least privilege.
- SDK MUST enforce Runtime permission boundaries.
- Runtime contracts MUST reflect granted permissions.
- Permission revocation SHOULD remain immediate.
- Permission activity SHOULD remain observable.
- Capabilities MUST NOT elevate their own authority.

---

# Relationship to MEG

Authorisation answers:

> **What may an authenticated identity do?**

Capability Permissions answer:

> **What may an executing capability do?**

These two systems intentionally remain independent.

Users receive authority through authorisation.

Capabilities receive authority through Runtime permissions.

The next chapter introduces **Secrets Management**, defining how confidential information is stored, rotated and injected into capabilities without allowing those capabilities to own or manage secrets directly.

---

# Summary

Capability permissions are the Runtime's mechanism for enforcing least privilege.

Rather than allowing capabilities unrestricted access to platform services, the Runtime constructs an execution environment containing only the authority explicitly granted during activation.

Within Mosaic, the safest capability is one that cannot even see functionality it has not been authorised to use.

Security is strongest when unavailable authority simply does not exist.
