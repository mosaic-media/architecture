<!--
File: docs/engineering/guides/meg-009-security-architecture/12-security-guidelines.md
Document: MEG-009
Status: Draft
Version: 0.2
-->

# Security Guidelines

> *Good security is rarely about writing more code. It is about making fewer assumptions.*

---

# Purpose

The previous chapters established the architectural foundations of Mosaic Security:

- Security Philosophy
- Trust Model
- Authentication
- Authorisation
- Capability Permissions
- Secrets Management
- Data Protection
- Module Trust
- Network Security
- Cryptography
- Security Observability

This document combines those concepts into practical engineering guidance.

Its purpose is to answer one question.

> **"How should engineers build secure capabilities without weakening the Runtime?"**

---

# Philosophy

Within Mosaic:

> **Security should emerge naturally from architectural ownership.**

The Runtime owns:

- trust
- identity
- permissions
- secrets

Capabilities own:

- business behaviour

Keeping those responsibilities separate produces stronger security with less complexity.

---

# Start With Trust

Before implementing any feature ask:

> **What does this component trust?**

Then ask:

> **Why should it trust it?**

If the answer is:

> "Because it probably came from..."

The trust boundary is unclear.

Trust should always be explicit.

---

# Start With Least Privilege

Every new capability begins with:

```text
No Authority
```

Before requesting a permission ask:

- Is this genuinely required?
- Can the permission become narrower?
- Can another Runtime contract satisfy this need?

Authority should be minimised continuously.

---

# Before Adding A Permission

Ask:

> **Does this permission describe business intent?**

Good.

```text
blob.read
```

Poor.

```text
runtime.*
```

Permissions should remain:

- narrow
- explicit
- reviewable

Every permission becomes part of the platform's long-term security model.

---

# Before Reading Configuration

Configuration belongs to the Runtime.

Capabilities should consume:

```go
ctx.Configuration()
```

They should never inspect:

- environment variables
- configuration files
- secret stores

Security improves when Runtime ownership remains intact.

---

# Before Accessing Secrets

Capabilities should never:

- cache secrets
- store secrets
- rotate secrets

Instead:

```go
ctx.Secrets()
```

provides controlled access.

The Runtime remains the owner.

Capabilities remain consumers.

---

# Before Using The Network

Ask:

> **Which external hosts are genuinely required?**

Declare only those hosts.

Avoid unrestricted outbound communication.

Every network connection expands the Runtime's attack surface.

Network permissions should remain intentionally narrow.

---

# Before Trusting External Data

Assume every external response is:

- incomplete
- malformed
- malicious
- unavailable

Validation should occur:

Before.

Business processing.

Capabilities should never assume external correctness.

---

# Before Logging

Never log:

- passwords
- tokens
- secrets
- personal information
- encryption keys

Instead log:

- authentication result
- permission decision
- trust transition

Logs should explain security.

Not compromise it.

---

# Before Creating A Capability

Ask:

- What authority does it require?
- What information does it protect?
- What information does it expose?
- What Runtime contracts does it consume?

If security cannot be described through the manifest:

The capability design probably requires refinement.

---

# Before Modifying Runtime Contracts

Runtime contracts become security boundaries.

Before changing one ask:

- Does this expand authority?
- Does this weaken isolation?
- Does this expose implementation?

Security should become stronger after Runtime evolution.

Not weaker.

---

# Before Modifying Storage

Storage ownership contributes directly to security.

Ask:

- Does ownership remain explicit?
- Is Business State still authoritative?
- Does another capability now gain unnecessary visibility?

Shared persistence often becomes shared security responsibility.

Avoid both.

---

# Before Introducing Cryptography

Ask:

> **What architectural problem is this solving?**

Examples.

Integrity.

↓

Hashing.

Authenticity.

↓

Digital signatures.

Confidentiality.

↓

Encryption.

Cryptography should solve architectural problems.

Not exist because it appears secure.

---

# Before Requesting Review

Every security contribution SHOULD satisfy the following checklist.

## Trust

- [ ] Trust boundary identified.
- [ ] Trust remains explicit.
- [ ] Revocation possible.

---

## Permissions

- [ ] Least privilege maintained.
- [ ] Manifest updated.
- [ ] Runtime enforcement preserved.

---

## Secrets

- [ ] Runtime owns secrets.
- [ ] No secret persistence.
- [ ] No secret logging.

---

## Data

- [ ] Information classification considered.
- [ ] Confidentiality preserved.
- [ ] Integrity maintained.

---

## Observability

- [ ] Security decisions observable.
- [ ] Confidential information protected.
- [ ] Audit events generated where appropriate.

---

## Documentation

- [ ] MEG updated where required.
- [ ] Permission changes documented.
- [ ] Security assumptions documented.
- [ ] ADR created where appropriate.

---

# Recognising Security Drift

The following symptoms usually indicate architectural drift.

- Capabilities reading environment variables.
- Runtime permissions expanding continually.
- Shared secrets.
- Broad wildcard permissions.
- Business code performing authentication.
- Direct storage access.
- Runtime implementation imported into modules.
- Hidden trust assumptions.

Security drift should be corrected immediately.

It compounds over time.

---

# Refactoring Security

When improving security ask:

- Can trust become more explicit?
- Can permissions become narrower?
- Can Runtime ownership become clearer?
- Can capabilities become less privileged?
- Can security become more observable?

Security refactoring should reduce assumptions.

Not increase complexity.

---

# Review Mindset

Security reviews should focus upon:

- trust boundaries
- ownership
- authority
- isolation
- observability

Questions such as:

> **Why is this allowed?**

are generally more valuable than:

> **Can this be made more secure?**

Security begins by understanding authority.

Not by adding controls.

---

# Learning The Security Architecture

New contributors SHOULD study MEG-009 in the following order.

```text
Security Philosophy

↓

Trust Model

↓

Authentication

↓

Authorisation

↓

Capability Permissions

↓

Secrets

↓

Data Protection

↓

Module Trust
```

Understanding trust first makes every later security mechanism significantly easier to understand.

---

# Engineering Culture

Security contributors should strive to:

- minimise authority
- simplify trust
- strengthen isolation
- improve observability
- reduce assumptions
- preserve Runtime ownership

Good security often means removing unnecessary authority rather than adding additional controls.

---

# Contributor Checklist

Before requesting review, confirm:

- [ ] Trust boundary is explicit.
- [ ] Identity precedes authority.
- [ ] Least privilege preserved.
- [ ] Runtime ownership maintained.
- [ ] Secrets remain Runtime managed.
- [ ] Security remains observable.
- [ ] Confidential information remains protected.
- [ ] Documentation updated.
- [ ] The platform is more trustworthy than before.

---

# Relationship to MEG

This document explains how contributors should evolve the Security Architecture established throughout MEG-009.

The previous chapters define:

> **How the platform protects itself.**

This chapter defines:

> **How engineers preserve that protection over time.**

Security survives because contributors consistently reinforce architectural trust boundaries rather than relying upon implementation details.

---

# Summary

Security is one of the few architectural qualities that becomes increasingly difficult to improve once a platform matures.

Within Mosaic, every engineering decision should strengthen:

- trust
- ownership
- authority
- observability

rather than weakening them.

A secure platform is not one with the most security features.

It is the one where every permission, every trust decision and every security boundary is obvious, deliberate and explainable.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`11-security-observability.md`

**Next File**

`13-adrs.md`
