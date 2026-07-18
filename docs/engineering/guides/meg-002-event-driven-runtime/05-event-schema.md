<!--
File: docs/engineering/guides/meg-002-event-driven-runtime/05-event-schema.md
Document: MEG-002
Status: Draft
-->

# Event Schema

> *The schema belongs to the protocol. Engineering belongs to preserving it.*

---

# Purpose

[MIP-001](../../protocols/mip-001-event-protocol/index.md) defines the canonical event envelope and payload boundary, and this chapter describes how engineering teams should implement that boundary.

---

# Engineering Guidance

Runtime code should treat the envelope as Platform-owned metadata, whereas capability code should treat the payload as business-owned data. Implementations should not blur this boundary by placing Runtime routing decisions into payload fields or by forcing the Runtime to inspect business payloads unnecessarily.

---

# Implementation Expectations

Event implementation should make the following boundaries clear:

- envelope fields are stable Platform metadata
- payload fields are owned by the publishing capability
- tracing and correlation remain available to observability tooling
- compatibility metadata is visible without decoding business payloads

---

# Reference

Protocol authority is provided by:

- [MIP-001 — Event Protocol](../../protocols/mip-001-event-protocol/index.md)
