<!--
File: docs/engineering/protocols/mip-004-platform-sdk-contract-protocol/index.md
Document: MIP-004
Status: Draft
-->

# MIP-004 — Platform–SDK Contract Protocol

> **Outline only.** This protocol states its intended contract but has not yet been expanded into chapters. It is not ready to be implemented against, and it does not yet declare a contract version. Treat it as a statement of direction until it is completed and reviewed.

---

This protocol defines the stable contract surface generated from Platform ports for SDK consumers.

The contract source is Platform-owned. Generated SDK output MUST identify its Platform contract version and expose compatibility metadata. The contract includes capability identifiers, lifecycle hooks, configuration declarations, permission declarations, event types, error categories and test seams.

SDK helpers may improve ergonomics but MUST NOT change the normative contract. A Module MUST be able to compile against the SDK without importing private Platform packages. Breaking contract changes require a new major contract version and an explicit compatibility decision.

