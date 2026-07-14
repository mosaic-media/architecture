<!--
File: docs/engineering/guides/meg-009-security-architecture/references.md
Document: MEG-009
Status: Draft
Version: 0.2
-->

# References

> *Security is strongest when it emerges naturally from architecture rather than being layered on afterwards.*

---

# Purpose

This document records the primary references that influenced the Security Architecture established throughout MEG-009.

Unlike many security guides that begin with cryptographic algorithms or authentication frameworks, Mosaic begins with:

- trust
- ownership
- Runtime boundaries
- capability isolation

Technology exists to implement those architectural principles.

It does not define them.

---

# Primary References

## Zero Trust Architecture

The Zero Trust model strongly influenced the Runtime trust boundaries defined throughout MEG-009.

Relevant concepts include:

- explicit trust
- continuous verification
- least privilege
- no implicit authority

Within Mosaic:

Every capability begins with zero authority.

Trust is granted explicitly through Runtime validation.

**Reference**

NIST SP 800-207

https://csrc.nist.gov/pubs/sp/800/207/final

---

## Principle of Least Privilege

The Runtime permission model intentionally follows the Principle of Least Privilege.

Relevant concepts include:

- minimal authority
- explicit permissions
- privilege reduction
- revocation

Least privilege underpins:

- capability permissions
- Runtime contracts
- SDK design

Authority should continually shrink rather than expand.

---

# Capability Security

The Module Platform strongly influenced the security architecture.

Relevant concepts include:

- manifest validation
- capability permissions
- Runtime isolation
- controlled execution

Security follows the same architectural ownership model established in:

- MEG-005
- MEG-006

Capabilities consume Runtime services.

They never own Runtime security.

---

# Authentication

Authentication guidance intentionally follows modern identity standards.

Relevant technologies include:

- OpenID Connect
- OAuth 2.0
- Multi-Factor Authentication

Within Mosaic:

Authentication establishes:

Identity.

Authorisation determines:

Authority.

These responsibilities remain intentionally separate.

---

# Authorisation

The Runtime permission model intentionally separates:

- user permissions
- capability permissions
- Runtime contracts

Authority always follows:

- explicit permission
- Runtime validation
- least privilege

This separation prevents business capabilities from becoming responsible for platform security.

---

# Secrets Management

Secrets management follows modern platform security practices.

Relevant concepts include:

- Runtime ownership
- secret rotation
- secret injection
- short-lived credentials

Capabilities consume:

Secrets.

The Runtime owns:

Secret lifecycle.

This dramatically reduces the trusted computing surface.

---

# Cryptography

Cryptography within Mosaic intentionally supports architecture rather than defining it.

Relevant concepts include:

- password hashing
- digital signatures
- integrity verification
- encryption

The Runtime should remain cryptographically agile.

Algorithms evolve.

Architecture should not.

---

# Secure Transport

Network protection builds upon:

- TLS
- HTTPS
- secure WebSockets

Transport security protects:

Communication.

Authentication establishes:

Identity.

Authorisation establishes:

Authority.

These concerns remain intentionally independent.

---

# OWASP

OWASP guidance influenced several Runtime principles.

Relevant concepts include:

- defence in depth
- secure defaults
- least privilege
- secure secret handling
- input validation

Security guidance should remain implementation independent while adopting proven operational practices.

**Reference**

https://owasp.org/

---

# NIST Cybersecurity Guidance

NIST publications influenced:

- trust
- identity
- cryptographic policy
- Zero Trust
- risk management

Rather than prescribing implementation technologies, Mosaic adopts the architectural principles behind these recommendations.

---

# Domain-Driven Design

Eric Evans

Security ownership intentionally follows the ownership boundaries established within the Domain Model.

Examples include:

- Aggregate ownership
- Repository ownership
- Capability ownership

Security should reinforce Domain ownership.

Not bypass it.

---

# Hexagonal Architecture

Alistair Cockburn

Security remains infrastructure.

The Domain never:

- authenticates
- authorises
- manages secrets

Infrastructure adapts security around business behaviour.

The Domain remains independent.

---

# Capability Runtime

MEG-005 strongly influences Runtime security.

Examples include:

- Runtime Kernel
- Worker Manager
- Scheduler
- Capability Registry

Security follows Runtime ownership.

Every Runtime Service becomes responsible for protecting its own architectural boundary.

---

# Module Platform

MEG-006 influences:

- capability permissions
- manifest validation
- module trust
- SDK security

Security naturally extends the Module Platform.

It does not replace it.

---

# Storage Architecture

MEG-007 influences:

- Business State protection
- secret storage
- archive integrity
- blob verification

Information protection follows Storage ownership.

Storage technologies remain implementation details.

---

# Observability

MEG-008 influences:

- security telemetry
- audit events
- trust diagnostics
- Runtime explainability

Security should remain continuously observable without exposing confidential information.

Observability strengthens security.

It does not weaken it.

---

# Go References

The Security Architecture intentionally embraces idiomatic Go.

Recommended references include:

## Effective Go

Topics include:

- package ownership
- interfaces
- composition
- error handling

https://go.dev/doc/effective_go

---

## Go Cryptography Packages

Relevant concepts include:

- cryptographically secure randomness
- TLS
- hashing
- signatures

The Runtime should prefer well-tested standard library implementations wherever practical.

https://pkg.go.dev/crypto

---

# Internal Mosaic Specifications

The following specifications complement MEG-009.

## Engineering

- MEG-001 Go Engineering Standards
- MEG-002 Reactive Runtime
- MEG-003 Domain-Driven Design
- MEG-004 Hexagonal Architecture
- MEG-005 Capability Runtime
- MEG-006 Module Platform
- MEG-007 Storage Architecture
- MEG-008 Observability

---

## Planned Engineering Specifications

- MEG-010 Performance Engineering
- MEG-011 Deployment Architecture
- MEG-012 API Architecture
- MEG-013 Event Architecture

---

## Mosaic Design Language

- MDL-001 Vision
- MDL-002 Principles
- MDL-003 Mental Model
- MDL-004 Interaction Model
- MDL-005 Composition Model

---

## Mosaic Design Specifications

- MDS-001 Design Token Architecture
- MDS-002 Colour System
- MDS-003 Material System
- MDS-004 Typography System
- MDS-005 Motion System
- MDS-006 Composition Engine
- MDS-007 Tile Framework
- MDS-008 Component Library

---

# Security Principles

The Security Architecture established throughout MEG-009 intentionally builds upon several enduring principles.

These include:

- Trust is explicit.
- Identity precedes authority.
- Authority follows least privilege.
- Runtime owns security.
- Capabilities consume security.
- Secrets remain Runtime owned.
- Security follows architectural ownership.
- Every trust decision remains observable.
- Cryptography supports architecture.
- Security should remain explainable.

These principles should remain considerably more stable than the implementation technologies used to realise them.

---

# Keeping References Current

Security practices evolve continuously.

Cryptographic algorithms improve.

Identity standards mature.

Threat models change.

This reference list SHOULD therefore be reviewed periodically to ensure:

- security guidance remains relevant
- obsolete practices are removed
- stronger architectural approaches are incorporated

The Runtime's trust model should remain stable even as security technologies continue evolving.

---

# Closing Statement

MEG-009 intentionally does not define security as a collection of technologies.

Instead, it defines security as an architectural property emerging from:

- Runtime ownership
- capability isolation
- explicit trust
- least privilege
- observable enforcement

The resulting Security Architecture ensures that every important security decision can be explained through the same architectural principles governing every other part of the Mosaic platform.

Security should never feel bolted on.

It should feel inevitable.

When trust naturally follows architecture, the platform becomes easier to understand, easier to review and significantly harder to compromise.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`glossary.md`

**Next File**

**End of Specification**
