<!--
File: docs/engineering/protocols/mip-004-platform-sdk-contract-protocol/index.md
Document: MIP-004
Status: Draft
Version: 0.1
-->

# MIP-004 — Platform–SDK Contract Protocol

This protocol defines the stable contract surface generated from Platform ports for SDK consumers.

The contract source is Platform-owned. Generated SDK output MUST identify its Platform contract version and expose compatibility metadata. The contract includes capability identifiers, lifecycle hooks, configuration declarations, permission declarations, event types, error categories and test seams.

SDK helpers may improve ergonomics but MUST NOT change the normative contract. A Module MUST be able to compile against the SDK without importing private Platform packages. Breaking contract changes require a new major contract version and an explicit compatibility decision.

