<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/glossary.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# Glossary

---

# Application Service

A Platform service that owns command or query orchestration, including validation, authentication, policy, transaction handling and contract use.

---

# Built-In Adapter

A Module or adapter compiled into the Platform distribution and required for a valid Generation. Built-in status does not bypass Platform contracts.

---

# Candidate Contract Package

A Go package that may become generated SDK source after implementation proves the contract shape.

---

# Generation Handoff

The metadata, health and lifecycle surface the Platform exposes so the Supervisor can activate and observe a Generation.

---

# Platform Foundation

The first runnable Platform implementation containing identity, policy, storage, events, configuration, diagnostics and Supervisor handoff, without media-specific product behaviour.

---

# Transactional Outbox

A persistence pattern where domain state changes and event records are committed in the same database transaction, then published asynchronously after commit.
