<!--
File: docs/engineering/guides/meg-006-module-platform/14-developer-platform.md
Document: MEG-006
Status: Draft
-->

# Developer Platform

> *The SDK defines the contract. The Developer Platform makes that contract productive.*

---

# Purpose

The Mosaic Developer Platform is the complete toolchain through which developers create, run, test, validate, package and publish Modules.

It is larger than the Mosaic SDK.

The SDK is one component within it.

The Developer Platform should make Module development feel like ordinary Go development while hiding Mosaic runtime composition, Build Workspace and packaging mechanics.

A Module developer should be able to move from a new project to a running development Platform through the Mosaic CLI without manually managing the Supervisor or Platform assembly.

---

# Philosophy

Within Mosaic:

> **Module authors write ordinary Go against the SDK. The Developer Platform handles the environment around it.**

Module authors should not need to understand:

- production Supervisor internals
- Build Workspace layout
- generated imports
- Platform composition
- runtime assembly
- package publication internals

Those concepts remain observable for diagnosis, but they should not be routine developer tasks.

---

# Architecture

The Developer Platform contains cooperating components with separate responsibilities.

```mermaid
flowchart TD

N1["Developer"]
N2["Mosaic CLI"]
N3["Mosaic SDK"]
N4["Development Supervisor"]
N5["Development Platform"]
N6["Test Harness Modules"]
N7["Local Module"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

The SDK defines what a Module may depend on.

The CLI provides the developer workflow.

The Development Supervisor orchestrates local composition and rebuilds.

The Development Platform is the real Platform configured for development.

Test Harness Modules provide deterministic capability implementations.

The Local Module is the Module currently under development.

---

# Mosaic SDK

The Mosaic SDK is the public Platform contract.

It owns:

- capability interfaces and Ports
- canonical models
- Event Envelope and Event Bus contracts
- Module registration APIs
- permission and configuration contracts
- small helper methods
- contract-focused test utilities

The SDK should contain almost no business logic.

It must not own the development workflow, Platform composition or build orchestration.

Chapter 08 defines the authoritative SDK boundary.

---

# Mosaic CLI

The Mosaic CLI is the primary developer interface to the Mosaic ecosystem.

Its command surface may include:

```text
mosaic new module
mosaic dev
mosaic build
mosaic test
mosaic doctor
mosaic validate
mosaic package
mosaic publish
mosaic docs
```

The exact command syntax may evolve, but responsibility remains stable.

The CLI orchestrates developer workflows around SDK contracts.

It may invoke Go tooling, the Development Supervisor, the Build Pipeline, validation tooling, documentation tooling and publication services on the developer's behalf.

Developers may still use normal Go tools directly when useful.

Mosaic-specific composition should not require them to do so.

---

# Project Scaffolding

Creating a Module should produce an immediately buildable Go project.

Conceptually.

```text
mosaic new module anilist
```

May produce:

```text
anilist/

    go.mod
    module.go
    metadata.go
    README.md
    tests/
    examples/
```

Scaffolding should establish:

- SDK dependency
- Module registration
- manifest source declarations
- baseline tests
- documentation structure
- examples

Generated projects should remain ordinary Go projects rather than proprietary project containers.

---

# Development Mode

`mosaic dev` should launch a complete local Mosaic environment.

Conceptually.

```mermaid
flowchart TD

N1["mosaic dev"]
N2["Development Supervisor"]
N3["Development Platform"]
N4["Test Harness Modules"]
N5["Local Module"]
N6["Client"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

The Local Module runs against a real Platform.

Development Mode should not replace Platform behaviour with a mock runtime.

---

# Development Supervisor

The Development Supervisor is a development-only Supervisor implementation optimised for rapid feedback.

It should share production Supervisor orchestration, validation, build invocation, health-check and activation behaviour wherever practical.

The Mosaic CLI starts and controls it for the developer.

It may:

- watch local source files
- invoke automatic rebuilds
- include local Modules in the desired composition
- maintain development configuration
- request Test Harness Module inclusion
- restart the Development Platform after successful builds
- notify connected clients when the active development build changes
- launch and connect the Web Shell when requested
- use development-oriented health-check timing
- expose verbose diagnostics
- use a local Module Catalogue
- preserve build and activation logs

It prioritises feedback speed over production deployment conservatism.

It must still preserve the production architecture.

The Development Supervisor must not:

- dynamically inject code into a running Platform
- introduce runtime plugin loading
- bypass manifest validation
- mutate Platform or Module source repositories
- replace the Build Pipeline with development-only composition logic

The term `inject local Modules` means adding local Module paths to an isolated development build.

It does not mean runtime code injection.

The Development Supervisor owns the local development lifecycle and the mapping from working directories to desired Module composition.

The Build Pipeline owns creation and mutation of the Local Build Workspace.

---

# Development Platform

The Development Platform is the real Mosaic Platform running in a development configuration.

It is not a fork, mock or reduced implementation.

Conceptually.

```yaml
mode: development
modules:
  local:
    - ../module
```

Development configuration may enable:

- verbose logging
- deterministic test providers
- shorter rebuild cycles
- development diagnostics
- local-only data

Platform contracts, capability orchestration, Event Bus behaviour, registration and lifecycle should remain production-equivalent.

The Development Platform contains the same architectural services as production, including:

- Event Bus
- Capability Managers
- GraphQL
- storage
- Scheduler
- permission enforcement
- Runtime SDUI

Development convenience may change surrounding configuration and diagnostics.

It must not replace those services with development-only equivalents.

---

# Local Module Composition

Local Module development should not require publication to a remote catalogue.

Conceptually.

```mermaid
flowchart TD

N1["Local Module"]
N2["Development Supervisor"]
N3["Build Pipeline"]
N4["Isolated Build Workspace"]
N5["Development Platform"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The Development Supervisor supplies local Module paths as build inputs.

The developer's working directory is the source of truth for the Local Module during development.

The Build Pipeline still owns workspace preparation, temporary `go.mod` updates, generated `imports.go`, dependency resolution and compilation mechanics.

Local composition must produce a statically linked Platform Binary using the same architecture as production.

No registry publication is required for this loop.

Production composition resolves Module inputs from configured catalogue sources.

Development composition may resolve the Local Module from the filesystem while resolving all other Modules through normal sources.

This difference in origin must not alter manifest admission, SDK registration, static linking or Platform lifecycle.

---

# Automatic Build Loop

Development should support a short, observable rebuild loop.

The Development Supervisor should monitor relevant inputs, including:

- Go source
- Module declarations and manifests
- generated source inputs
- Module-owned assets where applicable

Generated outputs should not trigger an unbounded rebuild loop.

```mermaid
flowchart TD

N1["Save Source"]
N2["Detect Change"]
N3["Build Candidate Platform"]
N4["Run Health Checks"]
N5["Activate Development Platform"]
N6["Notify Connected Clients"]
N7["Reconnect Or Refresh Client"]
N8["Continue"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
N7 --> N8
```

Failed builds should leave diagnostics available and must not be mistaken for successful activation.

The implementation may preserve the previous healthy development Platform when that improves feedback, but it must clearly identify which source revision is running.

Only a candidate that passes development health checks may replace the active Development Platform.

---

# Development Composition

The Development Supervisor should automatically request a composition containing the Local Module and configured Test Harness Modules.

Conceptually.

```mermaid
flowchart TD

N1["Development Platform Binary"]
N2["Platform"]
N3["Test Harness Modules"]
N4["Local Module"]

N1 --> N2
N1 --> N3
N1 --> N4
```

Test Harness Modules and the Local Module are peers inside the composed Platform.

Neither contains or wraps the other.

The CLI should provide useful defaults so a normal `mosaic dev` workflow does not require manual Platform configuration.

Explicit configuration should remain available when a developer needs different providers or multiple Local Modules.

---

# Test Harness Modules

Test Harness functionality should be delivered through ordinary Modules.

Test Harness Modules may provide deterministic implementations of capabilities such as:

- Metadata
- Media
- Artwork
- Authentication
- Search
- Event Sources

The Local Module therefore interacts with genuine Platform contracts and Capability Managers while its external dependencies are controlled.

Test Harness Modules should be:

- explicit
- replaceable
- deterministic
- unavailable to production composition by default

They must not introduce hidden test behaviour into the Platform.

Using ordinary Modules for these fakes continuously exercises manifest discovery, dependency validation, SDK registration, Capability Manager routing and Module lifecycle.

Chapter 15 defines the authoritative Test Harness capability, data, scenario and event-simulation model.

---

# Testing Modes

The Developer Platform supports two complementary testing levels.

SDK test utilities support fast isolated contract tests without a complete Platform.

The Development Platform and Test Harness Modules support integration tests against real Platform behaviour.

`mosaic test` may orchestrate:

```mermaid
flowchart TD

N1["Start Development Supervisor"]
N2["Compose Development Platform"]
N3["Install Test Harness Modules And Local Module"]
N4["Execute Tests"]
N5["Report Results And Diagnostics"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The CLI should remove manual environment setup from normal integration testing.

It should not force every unit test to start a Platform.

---

# Browser And Shell Integration

For Web development, `mosaic dev` should be able to complete the normal local startup path.

Conceptually.

```mermaid
flowchart TD

N1["Start Development Supervisor"]
N2["Compose And Start Development Platform"]
N3["Start Or Connect Shell"]
N4["Launch Browser"]
N5["Notify On Successful Rebuild"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

The developer should remain inside the running application while candidate builds are prepared.

After successful activation, the Shell should reconnect or refresh the affected runtime state automatically.

Browser launch should be configurable for headless, automated and non-Web development workflows.

---

# Development Diagnostics

The Development Supervisor should expose diagnostics that explain both Module and Platform behaviour.

Useful diagnostics include:

- initial build and rebuild duration
- rebuild count
- active source revision
- active Modules
- registered capabilities
- Capability Manager routing tables
- event traffic
- SDK compatibility results
- build and health-check status
- Platform restart history
- connected client state

Diagnostics should be observable through the CLI and may also be exposed through development UI surfaces.

Verbose diagnostics must not change Platform behaviour.

---

# Validation

The CLI should validate a Module before packaging or publication.

Validation may include:

- SDK compatibility
- manifest generation and schema validation
- capability registration
- dependency declarations
- public and private event declarations
- permission declarations
- configuration declarations
- documentation presence
- test results
- package reproducibility

Validation should produce actionable diagnostics before a package reaches the Module Catalogue.

The Supervisor remains responsible for validating manifests and compatibility when a Module is selected for composition.

Developer validation does not replace runtime admission.

---

# Manifest Generation

Go declarations should be the authoring source for Module metadata when the SDK can express that metadata completely.

Conceptually.

```go
sdk.Module{
    ID: "anilist",
    Capabilities: capabilities,
    Events: events,
    Permissions: permissions,
}
```

The CLI may generate:

```text
module.yaml
```

The generated manifest is the declarative artefact consumed by the Supervisor and Module Catalogue.

Generation should reduce duplicate maintenance without allowing executable source inspection during Supervisor discovery.

Generated manifests must still pass [MIP-002](../../protocols/mip-002-module-manifest-protocol/index.md) validation.

---

# Packaging And Publishing

`mosaic publish` should orchestrate a controlled publication pipeline.

Conceptually.

```mermaid
flowchart TD

N1["Validate"]
N2["Generate Manifest"]
N3["Run Tests"]
N4["Package"]
N5["Sign And Upload"]
N6["Module Catalogue"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
```

Publication tooling should hide repository implementation details while preserving visible validation, package identity and provenance.

Package and catalogue protocols require their own specifications before these commands become stable public interfaces.

This chapter defines workflow ownership, not those future wire formats.

---

# Documentation Tooling

The Mosaic CLI may expose documentation workflows such as:

```text
mosaic docs validate
mosaic docs build
mosaic docs nav
mosaic docs new
```

These commands should invoke the documentation rules governed by [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md).

The CLI must not define a second documentation standard.

Documentation remains a first-class engineering artefact and authored Markdown remains canonical.

---

# Developer Experience Boundary

The Developer Platform should expose simple workflows while retaining access to underlying diagnostics.

It should hide routine mechanics, not hide failures.

Developers should be able to inspect:

- generated manifests
- Build Specifications
- Build Pipeline stages
- compiler output
- Platform health checks
- registration and activation diagnostics
- test results

This keeps automation understandable and debuggable.

---

# Production Fidelity

Development should exercise the same architecture used after publication.

The intended development differences are limited to:

- Local Modules may originate from filesystem paths instead of a remote Module Catalogue
- Test Harness Modules may be included automatically
- rebuild timing and health checks may be tuned for rapid feedback
- development diagnostics may be more detailed
- local-only configuration and data may be used

The following must remain production-equivalent:

- SDK contracts
- manifest validation
- static Module composition
- generated registration imports
- Platform startup and Module registration
- Capability Manager orchestration
- Event Bus behaviour
- permission enforcement
- Runtime SDUI contracts

Development therefore acts as continuous validation of the production composition architecture.

---

# Anti-Patterns

## SDK As Developer Platform

Putting scaffolding, build orchestration and publication behaviour inside the SDK library.

## Development Runtime Fork

Maintaining a special Platform implementation whose behaviour differs from production.

## Runtime Hot Loading

Loading changed Module code into a running Platform instead of rebuilding a statically composed candidate.

## Hidden Test Behaviour

Embedding mocks or test-only branches into production Platform code.

## Publication Before Validation

Uploading packages before manifest, compatibility, documentation and test checks complete.

## Opaque Automation

Hiding build failures or active source revisions behind a simplified CLI experience.

---

# Mosaic Guidelines

Within Mosaic:

- The Developer Platform MUST preserve ordinary Go Module projects.
- The SDK MUST define developer contracts and MUST NOT own developer workflow.
- The Mosaic CLI SHOULD be the primary interface for Mosaic-specific development workflows.
- `mosaic dev` SHOULD run the real Platform in development configuration.
- The Development Supervisor MUST use the same static composition model as production.
- The Development Supervisor SHOULD share production Supervisor orchestration and activation behaviour wherever practical.
- The Development Supervisor MAY resolve Local Modules from filesystem working directories.
- The Development Supervisor SHOULD watch relevant Module inputs and notify clients after successful activation.
- Local Module composition MUST NOT require publication to a remote catalogue.
- Local Module composition MUST NOT introduce runtime plugin loading.
- The Build Pipeline MUST retain ownership of build mechanics.
- Test Harness behaviour SHOULD be supplied through explicit Modules.
- Test Harness Modules and Local Modules MUST participate as peer Modules in the composed Development Platform.
- SDK utilities SHOULD support isolated contract tests.
- Development Platform tests SHOULD support real integration behaviour.
- CLI validation MUST NOT replace Supervisor admission validation.
- Manifest generation MUST produce a declarative artefact that conforms to [MIP-002](../../protocols/mip-002-module-manifest-protocol/index.md).
- Documentation commands MUST follow [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md) rather than define separate rules.
- Developer automation SHOULD expose sufficient diagnostics to explain failures.

---

# Relationship To MEG

This chapter extends:

- Chapter 08, which defines the SDK contract boundary.
- Chapter 13, which defines practical Module design guidance.
- [MEG-005](../meg-005-runtime-architecture/index.md), which defines Supervisor and Build Pipeline responsibilities.
- [MIP-002](../../protocols/mip-002-module-manifest-protocol/index.md), which defines the generated Module Manifest contract.
- [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md), which governs documentation tooling behaviour.

The governing decision is recorded in:

- MEG-006 ADR-003 — Developer Platform As Integrated Toolchain.

---

# Summary

The Developer Platform combines contracts, workflow, real Platform execution, deterministic test capabilities and publication tooling into one coherent development experience.

The intended path is:

```mermaid
flowchart TD

N1["mosaic new module my-provider"]
N2["mosaic dev"]
N3["Running Development Platform"]

N1 --> N2
N2 --> N3
```

The SDK defines the contract.

The CLI provides the experience.

The Development Supervisor and Build Pipeline preserve production-equivalent composition.
