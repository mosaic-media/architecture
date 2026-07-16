<!--
File: docs/engineering/protocols/index.md
Document: Protocols
Status: Draft
Version: 0.3
-->

# Protocols

Integration Protocol specifications define Mosaic interoperability contracts, message shapes and compatibility expectations.

This section contains MIP documents. Engineering guides should reference protocol documents when describing implementation practices around shared contracts.

## Integration Protocols in Brief

| Specification | In one sentence |
|---------------|-----------------|
| [MIP-001 — Event Protocol](mip-001-event-protocol/index.md) | Defines the canonical event envelope, ownership, naming, versioning and compatibility contract. |
| [MIP-002 — Module Manifest Protocol](mip-002-module-manifest-protocol/index.md) | Defines the manifest contract used to identify, validate and admit Modules safely. |
| [MIP-003 — UVLightFrame Protocol](mip-003-uv-light-frame-protocol/index.md) | Defines the canonical artwork-light frame exchanged between analysis, MOS Cache and client renderers. |
| [MIP-004 — Platform–SDK Contract Protocol](mip-004-platform-sdk-contract-protocol/index.md) | Defines the generated SDK contract published from Platform ports. |
| [MIP-005 — Module Adapter Contract Protocol](mip-005-module-adapter-contract-protocol/index.md) | Defines how optional and built-in Modules implement Platform ports. |
| [MIP-006 — Generation Composition Protocol](mip-006-generation-composition-protocol/index.md) | Defines Generation contents, validation, atomic activation and rollback. |

Read [MEG-002 — Event-Driven Runtime](../guides/meg-002-event-driven-runtime/index.md) for event-driven implementation guidance and [MEG-006 — Module Platform](../guides/meg-006-module-platform/index.md) for Module implementation guidance.

For artwork-derived Acrylic lighting, read [MDS-003 — Material System](../../design/system/mds-003-material-system/index.md) before [MIP-003](mip-003-uv-light-frame-protocol/index.md).

The linked MIP specifications define the contracts; this catalogue does not repeat their normative requirements.
