<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/index.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# MEG-015 — Platform Foundation Implementation

> Build the first Mosaic Platform without forcing future SDK, Module or Supervisor decisions into the wrong layer.

---

# Purpose

MEG-015 turns the accepted Platform direction into a concrete first implementation path.

The guide is scoped to the Platform foundation. It explains what to build first, where code should live, which contracts must exist before adapters are accepted, and how to prove the Platform is ready for SDK extraction and Supervisor composition.

---

# Engineering Statement

Within Mosaic:

> **The Platform implementation starts as a private hexagonal Go application with explicit contracts, a mandatory PostgreSQL adapter and contract tests at every adapter boundary.**

The SDK should be generated or extracted after the Platform contract surface has been proven by the built-in PostgreSQL adapter and one reference Module path. Until then, the Platform repository may contain contract definitions, but private packages must not become public Module APIs by accident.

---

# First Build Outcomes

The first Platform build is complete when it can:

- boot with local configuration;
- create and migrate a PostgreSQL database;
- create a local user and session;
- enforce policy at application service boundaries;
- persist domain state through Platform ports;
- publish committed events through a transactional outbox;
- expose GraphQL read and command projections;
- report component health and redacted diagnostics; and
- provide a Supervisor activation target that can be health checked and rolled back by activating an earlier Generation.

---

# Reading Path

Read this guide in build order:

1. [01 — Build Scope](01-build-scope.md)
2. [02 — Repository Layout](02-repository-layout.md)
3. [03 — Platform Contracts](03-platform-contracts.md)
4. [04 — Application Boundaries](04-application-boundaries.md)
5. [05 — Storage and Migrations](05-storage-and-migrations.md)
6. [06 — Event Backbone](06-event-backbone.md)
7. [07 — Identity, Policy and Sessions](07-identity-policy-and-sessions.md)
8. [08 — Configuration and Secrets](08-configuration-and-secrets.md)
9. [09 — GraphQL and Diagnostics](09-graphql-and-diagnostics.md)
10. [10 — Supervisor Handoff](10-supervisor-handoff.md)
11. [11 — Test Gates](11-test-gates.md)
12. [12 — Build Sequence](12-build-sequence.md)

---

# Relationship to the SDK

MEG-015 deliberately keeps SDK work downstream.

The Platform should first define and prove contracts internally. [MIP-004 — Platform–SDK Contract Protocol](../../protocols/mip-004-platform-sdk-contract-protocol/index.md) then governs how those contracts become an SDK surface. The first implementation should avoid exposing internal package names as SDK commitments until the Platform has working contract tests and one built-in adapter.
