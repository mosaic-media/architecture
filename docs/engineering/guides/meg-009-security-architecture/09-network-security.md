<!--
File: docs/engineering/guides/meg-009-security-architecture/09-network-security.md
Document: MEG-009
Status: Draft
Version: 0.1
-->

# Network Security

> *Every network boundary is a trust boundary until proven otherwise.*

---

# Purpose

The Mosaic Runtime communicates with many external systems.

Examples include:

- Web browsers
- Mobile clients
- TV clients
- Third-party metadata providers
- Extension APIs
- Marketplace services
- Reverse proxies
- Other Mosaic instances

Every network interaction crosses a trust boundary.

This document defines how the Runtime protects those boundaries while preserving the architectural principles established throughout the previous MEGs.

---

# Philosophy

Within Mosaic:

> **No network is trusted. Every connection must establish trust before meaningful communication begins.**

The Runtime should assume:

- requests are malformed
- payloads are hostile
- networks are unreliable
- remote services may fail

Trust begins only after:

- identity
- encryption
- validation
- authorisation

have succeeded.

---

# Network Trust Boundary

Every incoming or outgoing connection crosses a trust boundary.

```text
Remote System

↓

Network

↓

Runtime

↓

Capability
```

The Runtime owns this boundary.

Capabilities should never bypass it.

---

# Network Principles

Network security within Mosaic is built upon several principles.

- Encrypt every trusted connection.
- Validate every request.
- Authenticate every identity.
- Authorise every operation.
- Minimise exposed surface area.
- Fail safely.
- Observe every significant interaction.

Every later decision reinforces these principles.

---

# Secure Transport

Every external Runtime interface SHOULD support encrypted transport.

Examples include:

- HTTPS
- Secure WebSockets
- TLS-protected APIs

Plaintext transport SHOULD be considered exceptional.

Confidentiality should begin before authentication.

---

# TLS

TLS provides:

- confidentiality
- integrity
- endpoint authentication

TLS does **not** provide:

- authorisation
- business validation
- capability permissions

The Runtime should clearly distinguish between:

Secure connection.

and.

Trusted request.

---

# API Boundaries

Every Runtime API SHOULD be treated as untrusted until validated.

Typical lifecycle.

```text
Request

↓

TLS

↓

Authentication

↓

Authorisation

↓

Validation

↓

Capability
```

Capabilities should never receive unvalidated requests.

The Runtime owns request validation.

---

# Reverse Proxies

Reverse proxies MAY terminate TLS.

Examples include:

- Caddy
- Nginx
- Traefik

The Runtime should continue enforcing:

- authentication
- authorisation
- permissions

TLS termination does not eliminate Runtime security responsibilities.

---

# Client Authentication

Network clients SHOULD authenticate before accessing protected Runtime functionality.

Examples include:

- Web UI
- Mobile applications
- TV clients
- CLI tools

Identity should remain independent of transport protocol.

---

# API Tokens

API clients MAY authenticate using:

- bearer tokens
- personal access tokens
- service account tokens

Tokens establish identity.

Authorisation determines permitted operations.

Tokens should remain:

- revocable
- time limited
- observable

---

# Request Validation

Every request SHOULD undergo validation before reaching a capability.

Validation includes:

- syntax
- schema
- size limits
- content type
- mandatory fields

Business validation remains inside capabilities.

Transport validation belongs to the Runtime.

---

# Rate Limiting

The Runtime SHOULD support rate limiting.

Examples include:

- authentication attempts
- API requests
- administrative endpoints

Rate limiting protects:

- Runtime resources
- external providers
- operators

Capabilities should remain unaware of rate-limiting implementation.

---

# Network Timeouts

Every outbound request SHOULD define:

- connection timeout
- request timeout
- read timeout

Capabilities should never wait indefinitely for remote systems.

The Runtime should fail predictably.

---

# Outbound Communication

Capabilities requiring outbound communication MUST declare:

- required permission
- permitted hosts

Example.

```yaml
network:

  outbound:

    - api.themoviedb.org
```

The Runtime SHOULD enforce outbound restrictions.

Capabilities should not possess unrestricted internet access by default.

---

# Host Allow Lists

The Runtime SHOULD support host allow lists.

Example.

```text
Metadata Capability

↓

TMDB

↓

AniList
```

↓

Allowed.

Everything else.

↓

Denied.

Allow lists reduce the attack surface significantly.

---

# Network Isolation

Capabilities should never open arbitrary network listeners.

Only the Runtime exposes public interfaces.

Capabilities consume Runtime contracts.

They do not become independent servers.

This preserves:

- security
- observability
- operational simplicity

---

# Internal Communication

Communication between Runtime Services SHOULD remain internal.

Examples include:

- Scheduler
- Worker Manager
- Execution Engine

These interactions should not require external network transport unless explicitly architected for distributed deployment.

The Runtime should avoid unnecessary network boundaries.

---

# Distributed Deployments

Future distributed Runtime deployments SHOULD authenticate Runtime-to-Runtime communication.

Examples include:

- mutual TLS (mTLS)
- signed service identities
- service account credentials

Runtime identity should remain explicit even within trusted infrastructure.

---

# External Providers

External APIs SHOULD always be treated as untrusted.

Examples include:

- TMDB
- AniList
- Trakt

The Runtime should assume:

- unexpected responses
- malformed payloads
- temporary outages
- protocol changes

Validation should occur before information enters Business State.

---

# Marketplace Communication

Marketplace downloads SHOULD support:

- TLS
- integrity verification
- signature verification

Transport security protects delivery.

Extension Trust verifies execution.

These responsibilities remain separate.

---

# Network Observability

The Runtime SHOULD expose:

- request rate
- response latency
- timeout count
- failed connections
- TLS failures
- rate-limit events

Operators should understand network behaviour independently from capability behaviour.

---

# Failure Handling

Network failures SHOULD remain isolated.

Example.

```text
TMDB Offline

↓

Metadata Capability

↓

Degraded
```

↓

Platform remains operational.

External failures should rarely compromise the Runtime itself.

---

# Denial Of Service

The Runtime SHOULD defend against resource exhaustion.

Examples include:

- oversized requests
- connection floods
- repeated authentication failures

Protection mechanisms may include:

- rate limiting
- connection limits
- request size limits
- timeouts

The Runtime should protect shared resources before capabilities execute.

---

# Network Logging

Significant network events SHOULD produce structured logs.

Examples include:

- authentication failure
- TLS failure
- denied outbound request
- rate limiting
- invalid request

Sensitive request contents MUST remain absent from logs.

---

# Privacy

Network telemetry MUST avoid exposing:

- credentials
- tokens
- cookies
- personally identifiable information

Observability should explain communication.

Not expose confidential content.

---

# Testing

Network security SHOULD be tested.

Typical tests verify:

- TLS enforcement
- request validation
- rate limiting
- host restrictions
- timeout handling
- outbound permissions

Security should remain deterministic.

Networking should never weaken Runtime trust.

---

# Anti-Patterns

The following practices are prohibited.

## Plain HTTP

Serving authenticated Runtime endpoints without transport encryption.

---

## Unrestricted Outbound Access

Capabilities connecting to arbitrary internet hosts.

---

## Runtime Listeners

Capabilities opening their own public network ports.

---

## Infinite Timeouts

Waiting indefinitely for external services.

---

## Network Trust

Assuming remote systems return valid information.

---

## Authentication Bypass

Forwarding unauthenticated requests directly into capabilities.

---

# Mosaic Guidelines

Within Mosaic:

- Every network boundary MUST be treated as untrusted.
- Encrypted transport SHOULD protect all external communication.
- Authentication MUST precede capability execution.
- Request validation MUST occur inside the Runtime.
- Capabilities MUST declare outbound network requirements.
- Outbound communication SHOULD remain restricted.
- Network failures SHOULD remain isolated.
- Network activity SHOULD remain observable.
- Sensitive network information MUST remain protected.

---

# Relationship to MEG

Extension Trust defines:

> **How executable code becomes trusted.**

Network Security defines:

> **How communication entering and leaving that trusted Runtime remains protected.**

The next chapter introduces **Cryptography**, defining how Mosaic uses hashing, signatures, encryption and integrity verification to protect information while remaining independent of specific cryptographic implementations.

---

# Summary

Networks connect the platform to the outside world.

They are therefore one of the Runtime's most important trust boundaries.

Within Mosaic, every connection should progress through the same sequence:

- secure transport
- identity
- authority
- validation
- execution

Only after these architectural boundaries have been satisfied should a capability ever become aware that a request existed.

The Runtime protects the network.

Capabilities simply perform their business responsibilities.

---

# Review Status

**Status**

Draft

**Owner**

Lead Software Architect

**Previous File**

`08-extension-trust.md`

**Next File**

`10-cryptography.md`
