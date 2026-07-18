<!--
File: docs/engineering/guides/meg-009-security-architecture/10-cryptography.md
Document: MEG-009
Status: Draft
-->

# Cryptography

> *Cryptography should protect trust, not become the architecture itself.*

---

# Purpose

Throughout the previous chapters, the Security Architecture established:

- trust
- authentication
- authorisation
- permissions
- secrets
- module validation
- network security

Many of these mechanisms rely upon cryptography.

Examples include:

- password hashing
- digital signatures
- archive integrity
- encrypted transport
- encrypted storage
- API tokens

This document defines how cryptography supports the Mosaic platform while remaining an implementation detail beneath the Runtime.

---

# Philosophy

Within Mosaic:

> **Architecture determines what must be protected. Cryptography determines how it is protected.**

The Runtime should never choose cryptographic techniques arbitrarily.

Every cryptographic operation should exist to enforce an architectural trust boundary.

Cryptography supports architecture.

It should never replace it.

---

# Cryptographic Responsibilities

Cryptography protects:

- confidentiality
- integrity
- authenticity

It intentionally does **not** determine:

- business permissions
- Runtime ownership
- capability authority

Those remain architectural concerns.

---

# Cryptographic Hierarchy

Cryptographic operations naturally align with the platform.

```mermaid
flowchart TD

N1["Identity"]
N2["Integrity"]
N3["Confidentiality"]
N4["Authenticity"]
N5["Non-Repudiation"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Each layer reinforces platform trust.

---

# Hashing

Hashing SHOULD protect information integrity.

Examples include:

- capability packages
- MOS archives
- blob verification
- downloaded assets

Hashes answer:

> **Has this information changed?**

Hashes do not answer:

> **Who created it?**

Integrity and identity remain separate.

---

# Password Hashing

Passwords MUST be stored using modern password hashing algorithms designed for credential storage.

Recommended characteristics include:

- memory hard
- computationally expensive
- resistant to GPU attacks

Passwords should never be:

- encrypted
- reversibly encoded
- stored directly

Password verification should occur entirely inside the Runtime.

Capabilities should never participate.

---

# Digital Signatures

Digital signatures SHOULD establish authenticity.

Examples include:

- module packages
- MOS archives
- marketplace downloads

Signatures answer:

> **Who signed this artefact?**

Combined with integrity verification they establish trusted origin.

---

# Signature Verification

The Runtime SHOULD verify signatures before:

- capability activation
- archive import
- marketplace installation

Verification should occur before executable code is trusted.

Execution should never precede verification.

---

# Encryption

Encryption SHOULD protect confidential information.

Typical examples include:

- secrets
- credentials
- sensitive configuration
- encrypted backups

Encryption protects confidentiality.

Integrity should still be verified independently.

---

# Encryption At Rest

Sensitive storage SHOULD support encryption at rest.

Examples include:

- secret stores
- signing keys
- encrypted backups

The Runtime should determine which information requires encryption.

Capabilities should remain unaware of storage implementation.

---

# Encryption In Transit

Transport encryption SHOULD protect every external Runtime boundary.

Examples include:

- HTTPS
- TLS
- Secure WebSockets

Transport encryption protects communication.

Authentication determines identity.

These responsibilities remain independent.

---

# Key Management

Cryptographic keys SHOULD remain Runtime owned.

Examples include:

- signing keys
- encryption keys
- token signing keys

Capabilities should request:

```text
Sign

Encrypt

Verify
```

They should never receive private keys directly.

Dedicated Runtime services perform cryptographic operations.

---

# Randomness

Security-sensitive operations MUST use cryptographically secure random number generation.

Examples include:

- session identifiers
- API tokens
- nonce generation
- invitation codes

Predictable randomness weakens every security mechanism built upon it.

---

# Checksums

Checksums MAY protect against accidental corruption.

Examples include:

- Blob Storage
- MOS Cache
- generated artefacts

Checksums detect corruption.

Digital signatures establish trust.

The Runtime should distinguish these purposes.

---

# Token Signing

Authentication tokens SHOULD be cryptographically signed.

Examples include:

- session tokens
- API tokens
- service account tokens

Signing prevents unauthorised modification.

Signing should not replace authorisation.

---

# Archive Protection

MOS Archives SHOULD support:

- integrity verification
- optional encryption
- optional signing

Portability should never weaken security.

Archives should remain independently verifiable.

---

# Blob Integrity

Blob Storage SHOULD support integrity verification.

Typical lifecycle.

```mermaid
flowchart TD

N1["Blob Stored"]
N2["Hash Recorded"]
N3["Blob Retrieved"]
N4["Integrity Verified"]

N1 --> N2
N2 --> N3
N3 --> N4
```

Corrupted blobs should never silently enter the Runtime.

---

# Capability Packages

Capability packages SHOULD support:

- hashing
- signatures
- version verification

The Runtime should establish:

- integrity
- authenticity

before activation begins.

---

# Algorithm Agility

The Runtime SHOULD avoid coupling itself to one cryptographic algorithm.

Examples include:

- hash algorithms
- signature algorithms
- encryption algorithms

Algorithms evolve.

Architecture should not.

The platform should support algorithm replacement without redesigning Runtime security.

---

# Cryptographic Agility

New cryptographic mechanisms SHOULD be introducible without changing:

- capability contracts
- Runtime APIs
- storage ownership

Cryptography should remain replaceable.

Capabilities should consume cryptographic services rather than implementations.

---

# Secret Separation

Secret values SHOULD never become cryptographic keys automatically.

Examples include:

```

API Key

≠

Signing Key
```

Different security responsibilities require different cryptographic material.

Reuse should be avoided.

---

# Auditability

Cryptographic operations SHOULD remain observable.

Examples include:

- signature verification
- archive verification
- key rotation
- encryption failures

Secret material MUST remain hidden.

Operational behaviour should remain visible.

---

# Performance

Cryptographic operations SHOULD remain efficient.

Examples include:

- caching verified signatures where appropriate
- avoiding repeated verification
- minimising unnecessary encryption

Security should remain strong without becoming an architectural bottleneck.

---

# Testing

Cryptographic services SHOULD be tested.

Typical tests verify:

- hashing
- signing
- verification
- encryption
- key rotation
- archive integrity

Testing should validate behaviour.

Not merely implementation.

---

# Anti-Patterns

The following practices are prohibited.

## Home-Grown Cryptography

Implementing custom cryptographic algorithms.

---

## Private Key Exposure

Providing signing keys directly to capabilities.

---

## Reversible Password Storage

Encrypting passwords instead of hashing them.

---

## Integrity Without Verification

Computing hashes that are never validated.

---

## Static Secrets

Long-lived keys without rotation strategy.

---

## Algorithm Coupling

Embedding specific cryptographic algorithms into business contracts.

---

# Mosaic Guidelines

Within Mosaic:

- Cryptography MUST support architectural trust boundaries.
- Passwords MUST be stored using modern password hashing algorithms.
- Sensitive information SHOULD support encryption.
- Digital signatures SHOULD establish authenticity.
- Hashes SHOULD verify integrity.
- Private keys MUST remain Runtime owned.
- Cryptographic algorithms SHOULD remain replaceable.
- Cryptographic operations SHOULD remain observable without exposing secret material.

---

# Relationship to MEG

Network Security defines:

> **How communication remains protected.**

Cryptography defines:

> **How trust, confidentiality and integrity are technically enforced beneath those architectural boundaries.**

The next chapter introduces **Security Observability**, describing how authentication, authorisation, permissions and trust decisions become visible to operators without exposing confidential information.

---

# Summary

Cryptography is one of the Runtime's supporting technologies.

It protects:

- identities
- secrets
- archives
- capability packages
- transport

Within Mosaic, cryptography exists to enforce architectural trust rather than define it.

The architecture decides:

> **What must be protected.**

Cryptography provides the mechanisms that make those decisions enforceable.
