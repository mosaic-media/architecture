<!--
File: docs/engineering/operations/mop-001-observability-operations/02-diagnostics.md
Document: MOP-001
Status: Draft
-->

# 02 — Diagnostics

---

# Purpose

Diagnostics expose what currently exists inside the Platform.

They answer structural questions such as:

- which modules are loaded
- which capabilities are registered
- which Runtime Services are active
- which dependencies are degraded
- where work is executing

---

# Diagnostic Use

Operators should use diagnostics when health or alerts indicate that structure matters.

Diagnostics are not logs.

Logs describe history.

Diagnostics describe the current Platform shape.

---

# Operational Rule

> **Operators should not need implementation access to understand Platform structure.**
