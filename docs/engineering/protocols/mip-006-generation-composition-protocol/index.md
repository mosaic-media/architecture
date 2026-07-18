<!--
File: docs/engineering/protocols/mip-006-generation-composition-protocol/index.md
Document: MIP-006
Status: Draft
-->

# MIP-006 — Generation Composition Protocol

> **Outline only.** This protocol states its intended contract but has not yet been expanded into chapters. It is not ready to be implemented against, and it does not yet declare a contract version. Treat it as a statement of direction until it is completed and reviewed.

---

This protocol defines the artifact Supervisor assembles and activates.

A Generation contains Platform, Shell and admitted Modules, plus manifests, assets and signatures. It MUST NOT contain the PostgreSQL database or mutable business state. Supervisor validates manifests, SDK compatibility, signatures and dependency closure before activation, runs health checks, performs an atomic activation swap, and retains previous valid Generations for instant rollback.

Rollback means activating an earlier Generation. It MUST NOT attempt to undo database mutations; database migration and recovery follow the independent persistence strategy in [MEG-005 — Runtime Architecture](../../guides/meg-005-runtime-architecture/index.md).

