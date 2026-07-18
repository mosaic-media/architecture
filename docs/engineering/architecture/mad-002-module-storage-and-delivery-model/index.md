<!--
File: docs/engineering/architecture/mad-002-module-storage-and-delivery-model/index.md
Document: MAD-002
Status: Draft
-->

# MAD-002 — Module Storage and Delivery Model

> Modules are Go libraries the Supervisor compiles into the Platform binary. They use Platform-owned storage; they never own it. Community and essential modules differ only in delivery.

---

# Purpose

MAD-002 records the accepted model for what a Module is, how it is delivered, and how it stores data. Several of these rules already existed scattered across [MEG-006 — Module Platform](../../guides/meg-006-module-platform/index.md), [MEG-015 — Platform Foundation Implementation](../../guides/meg-015-platform-foundation-implementation/index.md), [MIP-005 — Module Adapter Contract Protocol](../../protocols/mip-005-module-adapter-contract-protocol/index.md) and [MAD-001 — Transactional Store Extensibility](../mad-001-transactional-store-extensibility/index.md). This record consolidates them into one accepted decision and makes them Canon in [MAC-001 — Platform Architecture](../mac-001-platform-architecture/index.md) and [MEG-007 — Storage Architecture](../../guides/meg-007-storage-architecture/index.md).

---

# Decision In Brief

1. A Module is an ordinary Go library. The Supervisor compiles selected Modules into a single Platform binary at build time, producing a Generation. There are no runtime plugins.
2. Modules do not own storage or schema. The Platform owns a deliberately content-agnostic shared schema; Modules persist what they need through Platform-owned storage contracts.
3. Community and essential Modules are architecturally identical. They differ only in **delivery**: an essential Module ships in the Platform repository and cannot be deselected; a community Module lives in its own repository and is pulled and compiled into the binary by the Supervisor at Generation time.
4. Analytical processing is a **port**, not a mandated engine. PostgreSQL satisfies it today; a second engine may later be added as an essential Module behind the same port. The Platform mandates the capability, never the number of databases.

---

# Reading Path

1. [01 — Context](01-context.md)
2. [02 — Decision](02-decision.md)
3. [03 — Alternatives Considered](03-alternatives-considered.md)
4. [04 — Consequences](04-consequences.md)
5. [05 — Implementation Implications](05-implementation-implications.md)
