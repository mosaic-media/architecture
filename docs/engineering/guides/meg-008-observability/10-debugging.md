<!--
File: docs/engineering/guides/meg-008-observability/10-debugging.md
Document: MEG-008
Status: Draft
-->

# Debugging

> *Debugging support should explain behaviour without changing it.*

---

# Purpose

[MOP-001](../../operations/mop-001-observability-operations/index.md) defines operational debugging boundaries.

This chapter explains how engineers should provide safe investigation mechanisms.

---

# Engineering Guidance

Debugging features should be reserved for questions that normal observability cannot answer.

If routine operation depends on debugging, observability is incomplete.

---

# Implementation Expectations

Debugging mechanisms should be:

- deterministic
- permission-gated
- observable themselves
- non-invasive
- safe for production use where explicitly allowed
- redacted where sensitive data may appear

They should not bypass Platform authority or expose hidden operational APIs.

---

# Reference

Operational authority is provided by:

- [MOP-001 — Observability Operations](../../operations/mop-001-observability-operations/index.md)
