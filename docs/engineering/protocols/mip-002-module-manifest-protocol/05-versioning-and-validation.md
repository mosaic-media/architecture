<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/05-versioning-and-validation.md
Document: MIP-002
Status: Draft
Version: 0.4
-->

# 05 — Versioning And Validation

---

# Versioning

Manifest versioning communicates protocol compatibility.

Module versioning communicates module compatibility.

Runtime contract versioning communicates Platform compatibility.

These versions should remain distinct.

---

# Validation

The Supervisor should validate a manifest before invoking the Build Pipeline.

Validation should confirm:

- required fields exist
- identifiers are stable
- version constraints are satisfiable
- dependencies are available
- requested permissions are allowed
- provided contracts are coherent
- lifecycle declarations are compatible

---

# Validation Rule

> **A module that cannot be understood from its manifest should not be executed.**
