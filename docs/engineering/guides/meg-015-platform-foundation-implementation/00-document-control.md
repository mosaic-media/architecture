<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/00-document-control.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# Document Control

---

# Document Information

| Field | Value |
|-------|-------|
| Document | MEG-015 |
| Title | Platform Foundation Implementation |
| Status | Draft |
| Version | 0.1 |
| Owner | AdamNi-7080 |
| Audience | Platform, SDK, Supervisor and infrastructure engineers |
| Classification | Engineering specification |
| Scope | First implementation guidance for Mosaic Platform foundation |

---

# Authority

MEG-015 owns implementation guidance for the first Platform build:

- repository and Go package layout;
- Platform-owned contracts and private implementation boundaries;
- application service transaction boundaries;
- mandatory PostgreSQL adapter implementation;
- transactional outbox and Event Bus bootstrap;
- identity, policy and session foundations;
- configuration and secret broker bootstrap;
- GraphQL and diagnostics projections;
- Supervisor handoff for the first Generation; and
- implementation test gates.

MEG-015 does not own:

- Mosaic Platform architectural definition, owned by [MAC-001 — Platform Architecture](../../architecture/mac-001-platform-architecture/index.md);
- general Go engineering standards, owned by [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md);
- general hexagonal architecture guidance, owned by [MEG-004 — Hexagonal Architecture](../meg-004-hexagonal-architecture/index.md);
- Module ecosystem guidance, owned by [MEG-006 — Module Platform](../meg-006-module-platform/index.md);
- storage architecture beyond the first adapter implementation, owned by [MEG-007 — Storage Architecture](../meg-007-storage-architecture/index.md);
- security architecture beyond first implementation guidance, owned by [MEG-009 — Security Architecture](../meg-009-security-architecture/index.md); or
- roadmap sequencing, owned by [MRM-001 — Mosaic Platform Foundation](../../../roadmaps/mrm-001-mosaic-platform-foundation/index.md).

---

# Maturity

Version 0.1 defines the first implementation-grade Platform guide. It is sufficient for repository scaffolding, first port implementation, adapter contract tests and the initial Supervisor handoff.

It still requires implementation feedback before technical review, especially around generated SDK extraction and production-grade operational defaults.

Implementation feedback from `mosaic-platform` through the Transactional outbox slice has been incorporated: the repository layout is now the three-tier Core Platform / built-in module / external module model ([02 — Repository Layout](02-repository-layout.md)); the first contract set gained `CredentialStore` ([03 — Platform Contracts](03-platform-contracts.md)); the event envelope's `redaction_class` is now enumerated ([06 — Event Backbone](06-event-backbone.md)); and the session model gained `revoked_at` ([07 — Identity, Policy and Sessions](07-identity-policy-and-sessions.md)). Migration tooling remains an open question — the first implementation used an in-house deterministic migrator rather than an existing tool; this guide does not yet mandate one either way.

A design correction from the Reference capability slice has also been incorporated: the transaction contract has moved from a closed `Tx` interface of named Core Platform stores to uniform, port-based store resolution behind a replaceable storage adapter ([03 — Platform Contracts](03-platform-contracts.md)). The closed shape gave a capability no way to participate in a transaction without editing Core Platform on its behalf, contradicting the extensibility principle of [MEG-006 — Module Platform](../meg-006-module-platform/index.md) and this guide's own built-in-module-equality stance in [02 — Repository Layout](02-repository-layout.md). Core Platform and capability stores are now resolved identically, and the store set can grow without editing a central interface.

---

# Required Reading

- [MAC-001 — Platform Architecture](../../architecture/mac-001-platform-architecture/index.md)
- [MEG-001 — Go Engineering Standards](../meg-001-go-engineering-standards/index.md)
- [MEG-004 — Hexagonal Architecture](../meg-004-hexagonal-architecture/index.md)
- [MEG-005 — Runtime Architecture](../meg-005-runtime-architecture/index.md)
- [MEG-006 — Module Platform](../meg-006-module-platform/index.md)
- [MEG-007 — Storage Architecture](../meg-007-storage-architecture/index.md)
- [MEG-009 — Security Architecture](../meg-009-security-architecture/index.md)
- [MIP-006 — Generation Composition Protocol](../../protocols/mip-006-generation-composition-protocol/index.md)
