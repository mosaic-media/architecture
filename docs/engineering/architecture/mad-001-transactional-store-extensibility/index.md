<!--
File: docs/engineering/architecture/mad-001-transactional-store-extensibility/index.md
Document: MAD-001
Status: Draft
-->

# MAD-001 — Transactional Store Extensibility

> The Platform transaction boundary resolves stores through a uniform port, not through a closed interface of named Core Platform stores.

---

# Purpose

MAD-001 records why the Platform's transaction contract moved from a closed `Tx` interface — a fixed accessor list of Core Platform stores — to uniform, port-based store resolution behind a replaceable storage adapter.

The decision itself is now expressed in [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/03-platform-contracts.md). This record preserves the reasoning: the contradiction that forced it, the alternatives weighed, the consequences accepted and the follow-up work deferred. It exists so the direction is not re-litigated or forgotten once the code and the guide have moved on.

---

# Decision In Brief

A capability that needs its own store committed atomically alongside outbox events could not participate in the Platform transaction without Core Platform's closed `Tx` interface being edited on its behalf. That contradicted [MEG-006 — Module Platform](../../guides/meg-006-module-platform/index.md)'s principle that the Runtime require no modification to support new capabilities, and [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/index.md)'s own built-in-module-equality stance.

The transaction scope now exposes no fixed accessor list. Core Platform stores and capability stores are resolved identically through a typed accessor, and storage is a port so PostgreSQL can be replaced without touching a call site.

---

# Reading Path

1. [01 — Context](01-context.md)
2. [02 — Decision](02-decision.md)
3. [03 — Alternatives Considered](03-alternatives-considered.md)
4. [04 — Consequences](04-consequences.md)
5. [05 — Implementation Implications](05-implementation-implications.md)
