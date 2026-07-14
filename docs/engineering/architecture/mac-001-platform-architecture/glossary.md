<!--
File: docs/engineering/architecture/mac-001-platform-architecture/glossary.md
Document: MAC-001
Status: Draft
Version: 0.4
-->

# Glossary

---

# Capability

A self-contained unit of Mosaic product behaviour hosted by the Platform.

---

# Capability Contract

A Platform-owned SDK interface that defines one capability port.

Modules implement Capability Contracts.

The Platform orchestrates implementations through Capability Managers.

---

# Capability Manager

A Platform-owned orchestrator for one capability family.

Capability Managers discover providers, build routing tables, apply orchestration policy and coordinate provider cooperation.

Modules do not coordinate themselves.

---

# Capability Metadata

Provider support information used by Capability Managers to route and orchestrate work.

Examples include supported media types, identifiers, languages, priority, permissions and event declarations.

---

# Event Bus

The Platform-owned asynchronous transport used by capabilities and Modules to publish and consume events without direct dependency.

The Event Bus owns transport and routing behaviour.

Modules own domain event meaning.

---

# Module

A delivery package that contributes one or more capabilities or providers to Mosaic.

---

# Platform

The execution kernel of Mosaic.

The Platform provides stable execution, composition, governance and operational visibility for independently developed capabilities.

It is a runtime, not an application.

---

# Platform Contract

A stable contract defined by the Platform and published through the SDK for Modules to implement or consume.

Examples include provider contracts, capability contracts and event envelopes.

---

# Orchestration Policy

Platform-owned rules that determine how providers are selected, combined, cached, merged or used for fallback.

Modules implement behaviour.

They do not own cross-provider orchestration policy.

---

# Provider

A Module-contributed implementation of a Platform contract.

Providers are selected and coordinated by Capability Managers.

---

# Provider Routing

The Platform process of selecting eligible providers based on capability metadata, configuration, health, permissions and Capability Manager policy.

---

# Runtime

The Platform subsystem responsible for execution, lifecycle, scheduling, resource ownership and Runtime State.

---

# Runtime SDUI

The semantic server-driven UI contract emitted by the Platform for normal Mosaic presentation.

Runtime SDUI is rendered by clients.

It is not HTML, CSS, Flutter widgets or any other client presentation technology.

---

# Runtime State

Operational state describing how the Platform is running, not business state describing what users or capabilities are doing.

---

# SDK

The public contract surface used by Modules to register capabilities, implement provider contracts and interact with Platform-owned services.

---

# Service Registry

The Platform-owned registry of runtime services and capability infrastructure available inside an activated Platform.

---

# Supervisor

The host-level Mosaic manager that owns installation, Build Pipeline orchestration, activation, updates, rollback and recovery around the Platform.
