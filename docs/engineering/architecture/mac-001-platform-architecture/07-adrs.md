<!--
File: docs/engineering/architecture/mac-001-platform-architecture/07-adrs.md
Document: MAC-001
Status: Draft
-->

# Architectural Decision Records

---

# Purpose

This chapter records decisions that govern MAC-001.

Decision process, lifecycle and review expectations are governed by **[MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/index.md)**.

---

# MAC-001 ADR-001 — Platform As Execution Kernel

**Status**

Accepted

**Decision Date**

2026-07-14

---

## Context

Mosaic is a self-hosted media centre whose architecture is evolving toward an operating-system-like model.

The Supervisor owns installation, lifecycle, update, rollback, recovery and activation.

Modules provide most business functionality.

The Platform sits between them and must provide a stable runtime for independently developed capabilities without becoming the place where every feature lives.

Calling the Platform the centre of Mosaic risks implying that product behaviour should move into the Platform.

That would make Mosaic harder to extend and would cause the Platform to evolve as quickly as product features.

---

## Decision

Mosaic defines the Platform as the execution kernel of Mosaic.

The Platform is a runtime, not an application.

It owns:

- stable contracts,
- Capability Managers,
- orchestration,
- provider routing policy,
- Event Bus,
- GraphQL assembly,
- Runtime SDUI production,
- permissions,
- storage,
- scheduler,
- configuration,
- Service Registry,
- Runtime lifecycle.

It does not own business-specific functionality such as playback, metadata interpretation, Jellyfin integration, AniList integration, TMDB integration, recommendations, search providers, artwork providers or transcoding.

The Supervisor owns lifecycle and composition around the Platform.

Modules own business implementations.

The SDK defines the public contract surface used by Modules.

Capabilities belong to the Platform.

Providers belong to Modules.

New capabilities require Platform and SDK evolution.

New providers for existing capabilities should usually require only new Modules.

The final runtime is a single statically compiled Go executable assembled through the Supervisor-orchestrated Build Pipeline.

---

## Alternatives Considered

| Alternative | Outcome | Reason |
|-------------|---------|--------|
| Platform as application | Rejected | It encourages business behaviour to accumulate in the Platform. |
| Platform as feature host only | Rejected | It under-specifies contracts, orchestration and lifecycle. |
| Modules coordinate directly | Rejected | It creates dependency coupling and weakens Platform policy. |
| Dynamic runtime scanning | Deferred | The current architecture favours static Go composition through the Build Pipeline. |
| Platform owns presentation technology | Rejected | Clients should render Runtime SDUI using their own presentation systems. |
| Modules define new capability contracts independently | Rejected | It fragments SDK stability and makes orchestration policy unenforceable. |

---

## Consequences

The Platform should evolve slowly.

Most user-facing functionality should evolve through Modules.

Capability Managers become the primary orchestration point for providers.

Modules communicate through Platform contracts, Capability Managers and the Event Bus rather than direct references.

Provider metadata becomes part of the contract between Module manifests, SDK registration and Capability Managers.

Orchestration policy belongs to the Platform, not Modules.

The Platform can remain testable and deterministic because it owns runtime behaviour, not domain behaviour.

Client presentation remains separate because the Platform emits Runtime SDUI rather than HTML, CSS, Flutter widgets or other technology-specific presentation instructions.

---

## Implementation Implications

Engineering guides should treat MAC-001 as the authority for Platform ownership.

[MEG-005](../../guides/meg-005-runtime-architecture/index.md) should describe Runtime implementation details without redefining Platform purpose.

[MEG-006](../../guides/meg-006-module-platform/index.md) should describe Module participation without giving Modules direct coordination authority.

MIP specifications should define protocol details for events and manifests without changing ownership boundaries.

[MDS-008](../../../design/system/mds-008-component-library/index.md) should govern how Runtime SDUI becomes client presentation.
