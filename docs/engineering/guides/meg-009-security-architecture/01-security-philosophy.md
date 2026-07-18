<!--
File: docs/engineering/guides/meg-009-security-architecture/01-security-philosophy.md
Document: MEG-009
Status: Draft
-->

# Security Philosophy

> *Security is not about preventing every attack. It is about ensuring that every capability possesses only the authority it has explicitly earned.*

---

# Purpose

Security is frequently treated as a collection of technologies.

Examples include:

- TLS
- JWT
- OAuth
- encryption
- passwords

These technologies are important.

They are **not** architecture.

Within Mosaic, security begins much earlier.

It begins by deciding:

- what the Runtime trusts
- what it does not trust
- who owns authority
- how authority is granted
- how authority is revoked

This chapter establishes the architectural philosophy behind every security decision in the platform.

---

# Philosophy

Within Mosaic:

> **Trust nothing implicitly. Grant authority deliberately.**

Every architectural component begins with:

```

No Trust
```

Authority is gained only through:

- identity
- permissions
- Runtime contracts
- explicit validation

Trust should never emerge accidentally.

---

# Security Is Architecture

Security should not be layered on top of the platform.

It should emerge naturally from:

- Runtime ownership
- capability ownership
- storage ownership
- repository boundaries
- module isolation

Every previous MEG already contributes to security.

Examples.

```mermaid
flowchart TD

N1["MEG-003"]
N2["Business Ownership"]

N1 --> N2
```

```mermaid
flowchart TD

N1["MEG-004"]
N2["Architectural Boundaries"]

N1 --> N2
```

```mermaid
flowchart TD

N1["MEG-005"]
N2["Runtime Isolation"]

N1 --> N2
```

```mermaid
flowchart TD

N1["MEG-006"]
N2["Capability Permissions"]

N1 --> N2
```

```mermaid
flowchart TD

N1["MEG-007"]
N2["Storage Ownership"]

N1 --> N2
```

Security reinforces these architectural boundaries.

It does not replace them.

---

# Trust Before Technology

A useful principle is:

> **Define trust before selecting security technology.**

The platform should first answer:

- Who is trusted?
- Why are they trusted?
- How is that trust established?
- When does trust end?

Only afterwards should it decide:

- authentication mechanisms
- encryption algorithms
- token formats

Technology implements trust.

It does not define it.

---

# Identity Before Authority

Identity answers:

> **Who are you?**

Authority answers:

> **What may you do?**

The platform should never confuse these concepts.

Example.

```

Authenticated

≠

Authorised
```

Identity always precedes authority.

Authority should never be inferred merely because identity exists.

---

# Least Privilege

Every component should possess only the authority required for its responsibility.

Examples include:

```mermaid
flowchart TD

N1["Capability"]
N2["blob.read"]

N1 --> N2
```

Not:

```mermaid
flowchart TD

N1["Capability"]
N2["blob.*"]

N1 --> N2
```

The Runtime should continually minimise authority.

Not maximise convenience.

Least privilege remains one of the most enduring principles of secure system design because limiting authority reduces both accidental misuse and the impact of compromise.

---

# Explicit Trust

Trust should always be explicit.

Good.

```mermaid
flowchart TD

N1["Capability"]
N2["Permission"]
N3["Granted"]

N1 --> N2
N2 --> N3
```

Poor.

```mermaid
flowchart TD

N1["Capability"]
N2["Probably Needs It"]

N1 --> N2
```

Implicit trust inevitably becomes invisible.

Invisible trust becomes unreviewable.

---

# Defence In Depth

Security should never depend upon one mechanism.

Example.

```mermaid
flowchart TD

N1["Authentication"]
N2["Authorisation"]
N3["Permissions"]
N4["Runtime Isolation"]
N5["Storage Protection"]
N6["Observability"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Each layer reinforces the others.

Failure of one layer should not immediately compromise the platform.

---

# Runtime Neutrality

The Runtime should remain security neutral.

It should enforce:

- permissions
- contracts
- identity

It should not understand:

- movies
- anime
- music
- books

Business concepts belong to capabilities.

Security concepts belong to the Runtime.

---

# Capability Neutrality

Likewise.

Capabilities should not implement:

- authentication
- permission systems
- secret storage

They consume Runtime security services through SDK contracts.

The Runtime owns security.

Capabilities consume security.

---

# Secure By Default

Every new capability should begin with:

- zero permissions
- no network access
- no storage access
- no secret access

Capability authors explicitly request authority.

The Runtime explicitly grants it.

Security should begin from denial.

Not assumption.

---

# Fail Securely

When uncertainty exists:

The Runtime should refuse.

Examples include:

- invalid manifests
- unknown permissions
- incompatible signatures
- missing dependencies

The safest behaviour is generally:

```

Do Not Execute
```

Security failures should prevent execution rather than allowing undefined behaviour.

---

# Isolation

Every capability executes inside explicit architectural boundaries.

Capabilities should never directly access:

- Runtime internals
- storage implementation
- other capabilities

Interaction occurs only through:

- contracts
- Runtime Events
- SDK

Isolation reduces both accidental coupling and security risk.

---

# Security Is Observable

Security should never become invisible.

Operators should understand:

- permission denials
- authentication failures
- capability isolation
- module trust
- secret access

Security should explain itself through:

- logs
- metrics
- traces
- diagnostics

The platform should never require guessing why authority was denied.

---

# Security Is Continuous

Security is not:

```mermaid
flowchart TD

N1["Login"]
N2["Finished"]

N1 --> N2
```

Security continues throughout Runtime execution.

Every operation should continue respecting:

- identity
- authority
- permissions
- trust boundaries

Security should become a permanent Runtime property.

Not a gateway.

---

# Simplicity

Complex security models usually fail operationally.

Security should remain:

- understandable
- reviewable
- explainable

Operators should answer:

> **Why is this capability allowed to do this?**

without reading implementation.

Simple security is generally stronger security.

---

# Human Trust

The platform should distinguish between:

- trusted Runtime
- trusted operators
- trusted publishers
- trusted capabilities

Each possesses different authority.

Trust should remain contextual.

Never global.

---

# Revocation

Trust must be reversible.

Examples include:

- revoke token
- disable capability
- remove permission
- revoke publisher

Authority should disappear immediately once trust disappears.

Revocation is as important as granting authority.

---

# Privacy

Security protects:

- systems
- users
- information

Observability should never compromise privacy.

Security decisions should preserve:

- confidentiality
- integrity
- availability

while remaining observable.

---

# Mosaic Principles

Within Mosaic:

- Trust MUST remain explicit.
- Identity MUST precede authority.
- Authority MUST follow least privilege.
- Runtime boundaries MUST enforce isolation.
- Capabilities SHOULD begin with zero trust.
- Security SHOULD remain observable.
- Revocation MUST remain possible.
- Simplicity SHOULD outweigh unnecessary complexity.

These principles define the Security Architecture of the Mosaic platform.

---

# Relationship to MEG

Previous specifications defined:

- ownership
- Runtime
- capabilities
- storage
- observability

MEG-009 now begins defining:

> **How every one of those architectural boundaries becomes a security boundary.**

The next chapter introduces the **Trust Model**, formally defining which architectural components the Runtime trusts, which it conditionally trusts and which it intentionally treats as untrusted.

---

# Summary

Security is not a firewall around the platform.

It is the architecture through which the platform decides:

- what it believes
- what it verifies
- what it allows

Within Mosaic, every permission, every capability and every Runtime interaction ultimately derives from one principle:

> **Trust should always be explicit, limited and explainable.**

That principle becomes the foundation upon which every remaining security mechanism is built.
