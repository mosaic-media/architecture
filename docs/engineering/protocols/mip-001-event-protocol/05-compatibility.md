<!--
File: docs/engineering/protocols/mip-001-event-protocol/05-compatibility.md
Document: MIP-001
Status: Draft
Version: 0.4
-->

# 05 — Compatibility

---

# Compatibility Goal

The Event Protocol exists so independently evolving capabilities can communicate safely.

A capability should be able to publish or consume events without knowing another capability's implementation.

---

# Compatibility Responsibilities

Publishers should:

- preserve event meaning
- version payload contracts deliberately
- document compatibility expectations
- avoid removing fields without migration
- declare public published events in the Module manifest
- keep private events out of the external integration contract

Subscribers should:

- tolerate unknown compatible fields
- validate required fields
- fail explicitly on unsupported versions
- avoid relying on Platform envelope internals beyond the published contract
- subscribe only to public events or Platform events unless explicitly participating in the same Module implementation boundary

The Platform should:

- route events without interpreting domain payloads
- expose event visibility and version metadata to diagnostics
- validate manifest-declared event publications and subscriptions before build where possible

---

# Protocol Rule

> **Events are contracts. Contracts evolve deliberately, never accidentally.**

Public events are contracts.

Private events are implementation details.
