<!--
File: docs/engineering/protocols/mip-005-module-adapter-contract-protocol/index.md
Document: MIP-005
Status: Draft
Version: 0.1
-->

# MIP-005 — Module Adapter Contract Protocol

This protocol defines how a Module fulfils a Platform port.

An adapter MUST implement the SDK contract, declare its manifest through [MIP-002 — Module Manifest Protocol](../mip-002-module-manifest-protocol/index.md), honour lifecycle and permission decisions, and use Platform-owned storage, events, configuration and diagnostics contracts. Modules MUST NOT own parallel databases, bypass policy, read secrets directly or depend on another Module’s implementation.

Mandatory built-in adapters, such as PostgreSQL, use this same protocol. “Built-in” controls admission and distribution; it does not create a private architectural path.

