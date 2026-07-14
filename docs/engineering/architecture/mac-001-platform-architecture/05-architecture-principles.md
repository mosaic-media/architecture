<!--
File: docs/engineering/architecture/mac-001-platform-architecture/05-architecture-principles.md
Document: MAC-001
Status: Draft
Version: 0.4
-->

# 05 — Architecture Principles

---

# Purpose

The Platform Architecture is governed by a small set of durable principles.

These principles should guide future MAC, MEG, MIP and MOP documents.

---

# Platform Before Application

Mosaic should remain a platform capable of hosting evolving product behaviour.

Avoid adding product behaviour directly to the Platform when the behaviour can be expressed as a capability.

The Platform is a runtime, not an application.

---

# Contracts Before Coupling

Components should interact through stable contracts.

Direct implementation coupling makes independent evolution harder and weakens module safety.

The Platform owns contracts.

Modules implement them.

---

# Manifest Before Execution

The Platform should understand a module before it executes module code.

Discovery and validation must happen before activation.

---

# Events Before Direct Dependency

Capabilities should communicate through events and published contracts when direct dependency would create lifecycle or ownership coupling.

The Event Bus transports events.

Modules own domain event meaning.

---

# Managers Before Module Coordination

Capability Managers own orchestration.

Modules should not coordinate each other directly.

Provider routing, fallback and merge policy should live in the Platform.

---

# Semantic UI Before Presentation Technology

The Platform may emit Runtime SDUI.

It should not emit presentation technology decisions.

Clients render Runtime SDUI using their own presentation systems and the Mosaic Design Language.

---

# Observability Before Intervention

The Platform should explain itself before operators or engineers need to intervene.

Operational visibility is part of the architecture, not an afterthought.

---

# Ownership Before Convenience

Every concept should have a clear owner.

Convenient shortcuts that blur Platform, Runtime, capability and module responsibilities should be treated as architectural drift.

---

# Supervisor Before Platform Lifecycle

The Supervisor owns composition, activation, update, rollback and recovery.

The Platform runs inside an activated Generation and should not manage its own installation lifecycle.
