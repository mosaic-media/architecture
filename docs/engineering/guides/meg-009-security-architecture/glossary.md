<!--
File: docs/engineering/guides/meg-009-security-architecture/glossary.md
Document: MEG-009
Status: Draft
Version: 0.1
-->

# Glossary

> *Security becomes predictable when every engineer uses the same vocabulary to describe trust, authority and protection.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Security Architecture.

These definitions establish the canonical security vocabulary for:

- Runtime documentation
- SDK documentation
- Architecture specifications
- Contributor guidance
- Operational runbooks
- Marketplace documentation

Where a term has a specific meaning within Mosaic, that definition takes precedence over informal usage.

---

# A

## Authentication

The process of verifying the identity of an external actor.

Authentication answers:

> **Who are you?**

Authentication does **not** determine authority.

---

## Authorisation

The process of determining whether an authenticated identity may perform a particular operation.

Authorisation answers:

> **What are you allowed to do?**

---

## Audit Event

A durable security record describing a significant security decision.

Examples include:

- administrator login
- permission change
- capability installation
- trust revocation

Audit Events support long-term accountability.

---

# C

## Capability Permission

An explicit Runtime permission granted to a capability.

Examples include:

```text
blob.read
```

```text
scheduler.use
```

Capability permissions protect the Runtime.

They differ from user permissions.

---

## Confidentiality

The property ensuring information is accessible only to authorised identities.

Confidentiality is one of the three primary information security objectives alongside:

- integrity
- availability

---

## Cryptographic Key

A confidential value used for:

- encryption
- signing
- verification

Private keys remain Runtime owned.

Capabilities should never access them directly.

---

# D

## Data Protection

The collection of architectural mechanisms protecting:

- confidentiality
- integrity
- availability

throughout the information lifecycle.

---

## Digital Signature

A cryptographic mechanism proving:

- origin
- authenticity
- integrity

Signatures do not imply authority.

They establish identity.

---

# E

## Extension Trust

The Runtime process responsible for determining whether an extension may safely execute.

Extension trust includes:

- verification
- compatibility
- permission approval

Execution occurs only after trust has been established.

---

# I

## Identity

A verified representation of:

- user
- administrator
- service account
- API client

Identity establishes:

Who.

Authority determines:

What.

---

## Integrity

The assurance that information has not been modified without authorisation.

Integrity is commonly verified through:

- hashes
- signatures
- checksums

---

# L

## Least Privilege

The principle that every identity and capability should possess only the minimum authority required to perform its responsibilities.

Least privilege is one of the foundational principles of Mosaic Security.

---

# M

## Manifest Permission

A permission declared inside a Capability Manifest.

Manifest permissions describe requested authority.

The Runtime decides whether that authority is granted.

---

## Multi-Factor Authentication (MFA)

An authentication mechanism requiring multiple independent proofs of identity.

Examples include:

- password
- authenticator application
- hardware security key

MFA strengthens identity verification.

---

# N

## Network Trust Boundary

Any point where information crosses between:

- Runtime
- external systems

Every network boundary begins untrusted.

Trust must be established before execution.

---

# P

## Permission

An explicit declaration of authority.

Permissions determine:

What operations may be performed.

Permissions never establish identity.

---

## Personally Identifiable Information (PII)

Information capable of identifying an individual.

Examples include:

- names
- email addresses
- usernames

PII requires additional protection throughout the platform.

---

## Principal

Any authenticated identity capable of requesting Runtime operations.

Examples include:

- user
- administrator
- service account

---

# R

## Revocation

The process of removing previously granted authority.

Examples include:

- session revocation
- permission revocation
- capability revocation
- trust revocation

Revocation should take effect immediately wherever practical.

---

## Runtime Trust

The trust inherently placed in Runtime components forming the platform's trusted computing base.

Examples include:

- Runtime Kernel
- Scheduler
- Worker Manager
- Capability Registry

---

# S

## Secret

Confidential information managed by the Runtime.

Examples include:

- API keys
- OAuth credentials
- signing keys
- encryption keys

Capabilities consume secrets through Runtime contracts.

They never own them.

---

## Security Boundary

An architectural boundary across which trust must be explicitly established.

Examples include:

- network boundary
- capability boundary
- storage boundary

Security boundaries reinforce architectural boundaries.

---

## Security Observability

The collection of logs, metrics, traces and audit events describing security behaviour without exposing confidential information.

---

## Session

A temporary authenticated relationship between an identity and the Runtime.

Sessions establish:

Authenticated identity.

They do not establish authority.

---

# T

## Trust

The Runtime's confidence that a component, identity or artefact has satisfied the requirements necessary to participate within the platform.

Trust is:

- explicit
- observable
- revocable

Trust should never be assumed.

---

## Trust Model

The architectural model defining:

- trusted components
- conditionally trusted components
- untrusted components

The Trust Model underpins every other security mechanism within Mosaic.

---

## Trusted Computing Base (TCB)

The collection of Runtime components whose correct behaviour is essential to the platform's overall security.

Within Mosaic this primarily includes:

- Runtime Kernel
- Runtime Services
- SDK
- Repository implementations

---

# Z

## Zero Trust

The principle that no component, identity or capability receives implicit trust.

Authority must always be:

- requested
- validated
- granted

Zero Trust is the default security posture of the Mosaic platform.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| API | Application Programming Interface |
| HSM | Hardware Security Module |
| MFA | Multi-Factor Authentication |
| OIDC | OpenID Connect |
| OAuth | Open Authorization |
| PII | Personally Identifiable Information |
| SDK | Software Development Kit |
| TCB | Trusted Computing Base |
| TLS | Transport Layer Security |

---

# Relationship to MEG-009

This glossary supports every document within the Security Architecture specification.

Definitions should remain consistent across:

- Runtime documentation
- Extension Platform
- SDK documentation
- Marketplace documentation
- Operational guidance

Whenever security terminology evolves, this glossary SHOULD be updated before introducing new terminology elsewhere.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`14-contributor-guidance.md`

**Next File**

`references.md`
