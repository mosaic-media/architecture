<!--
File: docs/engineering/guides/meg-005-runtime-architecture/glossary.md
Document: MEG-005
Status: Draft
-->

# Glossary

> *The Runtime should describe itself using one consistent architectural vocabulary.*

---

# Purpose

This glossary defines the terminology used throughout the Mosaic Runtime Architecture, and the definitions contained within it establish the canonical Runtime vocabulary for:

- Architecture Specifications
- ADRs
- Runtime Documentation
- Source Code
- Contributor Guides
- Module SDKs

Where a term has a specific meaning within the Runtime, that definition takes precedence over informal usage.

---

# B

## Build Specification

The declarative description of the desired Mosaic runtime produced by onboarding, recording selections such as runtime channel, features, providers and Modules.

The Supervisor uses the Build Specification to orchestrate dependency resolution, compatibility validation, Build Workspace preparation and Build Pipeline invocation.

It describes desired composition and does not contain build mechanics.

---

## Build Workspace

An isolated temporary workspace used to assemble a candidate Platform package.

The Build Workspace may contain Platform, SDK, selected Modules and generated integration files, and it protects source repositories and the active Generation from mutation during build preparation.

---

## Build Pipeline

The Platform packaging process defined by the [MEG-006 Build Pipeline](../meg-006-module-platform/glossary.md#build-pipeline).

The Supervisor invokes the Build Pipeline but does not contain build logic.

The Build Pipeline owns build mechanics such as temporary `go.mod` updates, generated imports, `go mod tidy` and `go build`.

---

## Bootstrap

The initial process responsible for constructing the Runtime.

Bootstrap performs:

- configuration loading
- Runtime Kernel construction
- Runtime Service construction

Bootstrap ends once the Runtime becomes operational.

---

# C

## Capability

A self-contained unit of business functionality executed by the Runtime.

Examples include:

- Playback
- Library
- Metadata
- Recommendations

Capabilities own business behaviour, whereas the Runtime owns execution.

---

## Capability Registry

The Runtime Service responsible for discovering, registering and exposing capabilities.

The Capability Registry maintains:

- capability metadata
- lifecycle
- dependencies
- health

It is the Runtime's authoritative source of capability information.

---

## Composition

The process of assembling Runtime Services, Adapters and Capabilities into a functioning Runtime, which occurs inside the Composition Root.

---

# D

## Dependency Graph

The directed acyclic graph describing Runtime component dependencies.

The Dependency Graph determines:

- startup order
- shutdown order
- dependency validation

It is constructed before execution begins.

---

# E

## Embedded Recovery Renderer

A Supervisor-owned browser fallback that renders Recovery SDUI when the Shell or Web Renderer cannot run.

The Embedded Recovery Renderer is a single self-contained HTML document with inline CSS and JavaScript only.

It exists for bootstrap and Shell-failure recovery and is not the normal Mosaic Web UI.

During first installation it reports Shell bootstrap progress and automatically yields to the Shell when the Shell becomes available.

---

## Execution Engine

The Runtime Service responsible for coordinating executable Work Units.

The Execution Engine:

- dispatches work
- tracks execution
- coordinates workers

It does not execute business behaviour itself.

---

# G

## Generation

An immutable installed Mosaic system version containing the Platform package, Shell, Modules, manifests, assets and signatures required for activation.

The Supervisor activates one Generation at a time, so rollback means activating a previous known good Generation.

---

# H

## Health

The operational readiness of a Runtime component.

Examples include:

- Healthy
- Degraded
- Unavailable

Health describes operational capability rather than business correctness.

---

# I

## Isolated Runtime Build

A Supervisor-orchestrated build flow that assembles a candidate Mosaic runtime in a clean workspace before validation and activation.

An Isolated Runtime Build must not mutate the active Generation.

---

# K

## Kernel

The central coordinating component of the Runtime.

The Runtime Kernel owns:

- lifecycle
- Runtime Services
- startup
- shutdown

It intentionally owns no business behaviour.

The Runtime Kernel resembles a microkernel by keeping only essential coordination responsibilities while delegating execution to specialised services.  [AWS Documentation](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html)

---

# L

## Lifecycle

The sequence of operational states followed by every Runtime Service.

Examples include:

- Created
- Ready
- Running
- Stopping
- Disposed

Lifecycle ownership belongs to the Runtime Kernel.

---

# P

## Platform Binary

The executable Platform output contained within a Platform package.

The Supervisor should not compile the Platform Binary directly, because the Build Pipeline produces it.

---

## Platform Package

The Platform artefact produced by the Build Pipeline and stored within a Generation.

The Supervisor validates and activates Platform packages, whereas build mechanics belong to the Build Pipeline.

---

# R

## Recovery UI

The user-facing recovery experience used to diagnose and recover Mosaic when normal Platform interaction is unavailable.

Recovery UI should normally be rendered by the Shell from Recovery SDUI.

When the Shell is unavailable, the embedded recovery renderer displays Recovery SDUI in the browser.

Recovery UI knows about Generations, logs, health, configuration, storage, network, diagnostics and recovery actions, but it does not know media semantics.

---

## Recovery Hierarchy

The ordered set of presentation layers used during Mosaic recovery.

The hierarchy is:

- Normal Runtime
- Supervisor Recovery Using Shell or a Native Client Renderer
- Embedded Recovery Renderer for Web
- No UI

The Supervisor should always use the richest available layer.

Client renderers present recovery state while the Supervisor recovers the Platform or Web Shell; they do not supervise the Supervisor.

---

## Recovery SDUI

The small server-driven UI contract emitted by the Supervisor for recovery, onboarding and diagnostics states.

Recovery SDUI includes only primitive components such as:

- Heading
- Paragraph
- Status
- Progress
- Button
- Form
- Table
- Log

The Supervisor emits Recovery SDUI rather than HTML.

---

## Resource Manager

The Runtime Service responsible for managing shared Runtime resources.

Examples include:

- worker capacity
- connection pools
- memory budgets

Business capabilities consume resources, but the Runtime owns them.

---

## Runtime

The execution platform responsible for coordinating capabilities.

The Runtime owns:

- execution
- scheduling
- workers
- lifecycle
- resources

It intentionally owns no business behaviour.

---

## Runtime SDUI

The server-driven UI contract emitted by the Platform for normal Mosaic user interface presentation.

The Shell and client renderers render Runtime SDUI, which the Supervisor does not produce.

---

## Runtime Kernel

The architectural centre of the Runtime, through which every Runtime Service is coordinated.

It should remain:

- small
- stable
- business agnostic

---

## Runtime Service

A modular component providing one Runtime responsibility.

Examples include:

- Scheduler
- Worker Manager
- Execution Engine
- Capability Registry

Runtime Services cooperate through explicit contracts.

---

## Runtime State

Operational information describing the Runtime.

Examples include:

- queue depth
- worker utilisation
- capability lifecycle

Runtime State is distinct from business state.

---

# S

## Scheduler

The Runtime Service responsible for determining when Work Units become executable.

The Scheduler owns:

- delayed execution
- recurring execution
- execution timing

It never executes work directly.

---

## Startup

The deterministic process through which the Runtime becomes operational.

Startup consists of:

- configuration
- dependency validation
- Runtime initialisation
- capability activation

---

## Shutdown

The controlled transition from a running Runtime to a fully stopped Runtime.

Shutdown includes:

- cooldown
- draining
- resource release
- service disposal

Graceful shutdown preserves business correctness.

---

## Shell

The operational facade over the Platform for web onboarding, administration and user interaction.

The Supervisor installs and manages the Shell, because the Platform does not present itself directly.

The Shell should render Recovery SDUI whenever it is available.

During onboarding, the Shell renders Recovery SDUI until the Platform exists and can produce Runtime SDUI.

The Shell remains loaded during initial Platform build and activation; it switches backend and SDUI producer after Platform health checks pass.

---

## Supervisor HTTP Entry Point

The single public HTTP entry point for Mosaic user access.

All browser traffic enters through the Supervisor, so the Platform never exposes UI directly.

---

## Supervisor

The immutable always-running Mosaic host manager responsible for installing, activating, upgrading and recovering Mosaic.

The Supervisor owns:

- Shell installation
- onboarding entry point
- Module resolution
- Build Pipeline invocation
- Generation activation
- atomic activation
- rollback
- recovery UI

It exists outside Platform packages and Generations.

It should not own media business behaviour.

---

# W

## Work Unit

The smallest executable Runtime operation.

Examples include:

- scheduled capability execution
- event handling
- maintenance work

The Runtime executes Work Units, whereas capabilities provide their behaviour.

---

## Worker

An isolated execution environment capable of executing one Work Unit.

Workers:

- execute
- report completion
- honour cancellation

Workers do not understand business behaviour.

---

## Worker Manager

The Runtime Service responsible for:

- worker lifecycle
- worker allocation
- worker health
- worker replacement

Workers are Runtime resources, and the Worker Manager owns them.

---

## Worker Pool

A bounded collection of Runtime workers.

Worker pools provide:

- concurrency
- predictable resource usage
- execution capacity

Worker pools belong to the Worker Manager.

---

# Common Acronyms

| Acronym | Meaning |
|----------|---------|
| ADR | Architectural Decision Record |
| DAG | Directed Acyclic Graph |
| DI | Dependency Injection |
| MEG | Mosaic Engineering Guidelines |
| SDK | Software Development Kit |
| UI | User Interface |

---

# Relationship to MEG-005

This glossary supports every document within the Runtime Architecture specification.

Definitions should remain consistent across:

- Runtime implementation
- Runtime documentation
- Module Platform
- Contributor Guidance
- Architecture Specifications

Whenever Runtime terminology evolves, this glossary should be updated before introducing new terminology elsewhere.
