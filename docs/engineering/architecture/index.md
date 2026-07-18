<!--
File: docs/engineering/architecture/index.md
Document: Architecture
Status: Draft
-->

# Architecture

Architecture documentation contains accepted Mosaic platform structure and clearly separated proposals for architecture that is not yet authoritative.

MAC documents are authoritative Architecture Canon. MAD documents record accepted architecture decisions and their reasoning. MDP documents preserve proposals and must be read according to their recorded Status.

## Architecture Canon in Brief

| Specification | In one sentence |
|---------------|-----------------|
| [MAC-001 — Platform Architecture](mac-001-platform-architecture/index.md) | Defines the accepted Platform structure, its responsibilities and the boundaries between the Platform, Supervisor, capabilities and Modules. |

## Architecture Decisions

| Decision | Status | In one sentence |
|----------|--------|-----------------|
| [MAD-001 — Transactional Store Extensibility](mad-001-transactional-store-extensibility/index.md) | Accepted | Records why the Platform transaction boundary resolves stores through a uniform port instead of a closed interface of named Core Platform stores. |
| [MAD-002 — Module Storage and Delivery Model](mad-002-module-storage-and-delivery-model/index.md) | Accepted | Records that Modules are Go libraries compiled into the binary, never own storage or schema, differ only in delivery, and that analytical processing is a port rather than a mandated engine. |

## Deferred Proposals

| Proposal | Status | In one sentence |
|----------|-------------|-----------------|
| [MDP-001 — Adaptive Composition Runtime](mdp-001-adaptive-composition-runtime/index.md) | Deferred | Preserves the post-v1 mathematical composition solver, normalised spatial model and calibration questions without making them current architecture. |
| [MDP-002 — Tile Framework](mdp-002-tile-framework/index.md) | Deferred | Preserves the post-v1 behavioural Tile model, its resolution pipeline and lifecycle. The authoritative v1 Tile is a governed Container Component owned by [MDS-008 — Component Library](../../design/system/mds-008-component-library/index.md). |

Begin here when you need to understand what Mosaic is. Continue to [Engineering Guides](../guides/index.md) for implementation practice, [Protocols](../protocols/index.md) for interoperability contracts and [Operations](../operations/index.md) for operational expectations.

The Architecture Canon is authoritative. Deferred proposals are non-authoritative and unscheduled until a later decision changes their Status. This catalogue provides orientation only.
