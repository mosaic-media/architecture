<!--
File: docs/engineering/guides/meg-006-module-platform/02-module-manifest.md
Document: MEG-006
Status: Draft
Version: 0.2
-->

# Module Manifest

> *Module engineering begins with the manifest, but the protocol belongs to MIP-002.*

---

# Purpose

MEG-006 explains how engineers build the Module Platform.

The authoritative manifest contract is defined by **MIP-002 — Module Manifest Protocol**.

This chapter describes the engineering implications of that protocol.

---

# Engineering Guidance

Module loading should always follow the same order:

```text
Discover Manifest
↓
Validate Manifest
↓
Register Module
↓
Resolve Dependencies
↓
Activate Module
```

The Runtime should not execute module code simply to discover identity, dependencies, permissions or contracts.

---

# Implementation Expectations

Module Platform implementations should provide:

- deterministic manifest discovery
- clear validation errors
- permission review before activation
- dependency resolution before execution
- diagnostic visibility into accepted and rejected modules

---

# Reference

Protocol authority is provided by:

- MIP-002 — Module Manifest Protocol
