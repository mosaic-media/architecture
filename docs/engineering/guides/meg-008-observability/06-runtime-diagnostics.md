<!--
File: docs/engineering/guides/meg-008-observability/06-runtime-diagnostics.md
Document: MEG-008
Status: Draft
-->

# Runtime Diagnostics

> *Diagnostics are engineered surfaces that let operations inspect Platform structure safely.*

---

# Purpose

[MOP-001](../../operations/mop-001-observability-operations/index.md) defines how diagnostics are used operationally.

This chapter explains how engineers should provide diagnostic surfaces without exposing implementation internals.

---

# Engineering Guidance

Diagnostics should describe current Platform structure:

- loaded modules
- registered capabilities
- active Runtime Services
- dependency status
- worker allocation
- queue depth
- storage provider state

Diagnostics should not require operators to inspect memory, read source code or attach debuggers.

---

# Implementation Expectations

Diagnostic APIs should be:

- explicit
- permission-gated
- safe for production use
- redacted where needed
- stable enough for tooling
- separate from business APIs

---

# Reference

Operational authority is provided by:

- [MOP-001 — Observability Operations](../../operations/mop-001-observability-operations/index.md)
