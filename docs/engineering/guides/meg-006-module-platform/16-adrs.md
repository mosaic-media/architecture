<!--
File: docs/engineering/guides/meg-006-module-platform/16-adrs.md
Document: MEG-006
Status: Draft
-->

# Architectural Decision Guidance

> *Decision history belongs in decision records. This chapter identifies when MEG-006 needs them and where readers should look for the governing process.*

---

# Purpose

MEG-006 may require architecture decisions when changes alter long-lived engineering direction, compatibility expectations or responsibility boundaries. The decision process itself is governed by **[MDG-001 — Documentation Authority Guide](../../documentation/mdg-001-documentation-authority-guide/index.md)**, and this chapter avoids repeating ADR process rules so the documentation library has one authoritative home for decision practice.

---

# Decision Areas

Create or update a decision record when a change affects:

- Manifest-Driven Platform
- Capability-Oriented Architecture
- SDK Stability Policy
- Permission Model
- Capability Lifecycle
- Dependency Resolution Strategy
- Marketplace Compatibility
- Module Isolation
- Static Go Module Composition
- SDK Registry Registration
- Generated Imports
- SDK Public Contract Boundary
- Manifest Generation
- Developer Platform Boundary
- Mosaic CLI Ownership
- Development Supervisor
- Test Harness Modules
- Test Harness Scenarios
- Event Simulation
- Local Module Composition

---

# MEG-006 ADR-001 — Static Go Module Composition

**Status**

Accepted

**Decision Date**

2026-07-14

---

## Context

Mosaic needs an extensibility model that fits Go instead of fighting it. Runtime plugin systems introduce complexity through dynamic loading, RPC boundaries, reflection, version skew and operational failure modes, whereas Go already provides strong primitives for modular composition:

- modules
- semantic versions
- static linking
- explicit imports
- package initialisation

Mosaic should use those primitives directly.

---

## Decision

Mosaic will not support runtime plugins. Modules are ordinary Go libraries that implement the Mosaic SDK, and the Supervisor resolves selected Module manifests and invokes the Build Pipeline.

The Build Pipeline creates a temporary build workspace, updates the temporary `go.mod`, generates a single `imports.go` file containing blank imports for selected Modules and builds a statically linked Platform Binary. Each Module uses `init()` only to register itself with the SDK registry, and at Platform startup the Platform asks the SDK registry for registered Modules. No reflection, scanning, dynamic library loading or Module RPC boundary is required.

`imports.go` is the only generated source required for Module integration, because Capability Managers, event handling, GraphQL schema contribution and provider routing must operate through SDK contracts rather than generated glue code.

---

## Alternatives Considered

| Alternative | Outcome | Reason |
|-------------|---------|--------|
| Runtime plugin loading | Rejected | It adds dynamic loading and compatibility complexity that Go does not optimise for. |
| Module RPC processes | Rejected | It turns local capability composition into distributed-system coordination. |
| Reflection-based discovery | Rejected | It weakens explicitness and makes startup less deterministic. |
| Source-code analysis by Supervisor | Rejected | Manifests should be the source of truth; Go source should not be inspected for architecture. |

---

## Consequences

The final Runtime is a single statically linked Go executable, so to the finished Platform Binary, Platform code and Module code are both ordinary Go code. Module extensibility remains deterministic because the Build Pipeline imports exactly the selected Modules.

The Supervisor stays manifest-driven and does not edit source repositories, whereas the Build Pipeline owns temporary workspace preparation, `go.mod` updates, generated imports and package build mechanics. Module `init()` functions become part of the architecture and must therefore remain registration only.

Development tooling must preserve the same model. The Development Supervisor may orchestrate compilation of local Modules into a development Platform through the Build Pipeline, but it should not introduce runtime loading semantics.

---

## Implementation Implications

The Build Pipeline should create a temporary workspace with the following shape.

```text
workspace/

    platform/
    sdk/
    modules/
    generated/
```

It should update the temporary `go.mod` using normal Go tooling, for example.

```text
go mod edit -require=github.com/mosaic/module-anilist@v1.2.0
go mod tidy
```

It should then generate exactly one imports file.

```go
package generated

import (
    _ "github.com/mosaic/module-anilist"
    _ "github.com/mosaic/module-playback"
    _ "github.com/mosaic/module-jellyfin"
)
```

Development tooling should support this model through the Mosaic CLI, Development Supervisor and Test Harness, with typical commands such as the following.

```text
mosaic new module anilist
mosaic dev
mosaic test
mosaic build
mosaic publish
```

The Test Harness should provide fake capability providers for integration testing against a real development Platform.

---

# MEG-006 ADR-002 — SDK As Public Contract Language

**Status**

Accepted

**Decision Date**

2026-07-14

---

## Context

Mosaic Modules need a stable way to integrate with the Platform without importing Platform internals. The Platform owns orchestration and implementation while Modules own capability implementations, so both sides need a shared language for capability contracts, models, events, registration, permissions and testing. If the SDK becomes a framework or implementation library instead, Platform concerns will leak into Modules and SDK versioning will become unstable.

---

## Decision

The Mosaic SDK is the public contract language between the Platform and Modules. The SDK owns:

- capability interfaces,
- canonical Platform models,
- Event Envelope,
- Event Bus interfaces,
- core Platform events,
- Module registration APIs,
- small validation and version helpers,
- testing utilities.

The SDK must remain lightweight, which means it must not contain database logic, storage implementation, GraphQL implementation, scheduler implementation, HTTP server code, caching implementation, business logic, Capability Manager orchestration or rendering.

Both the Platform and Modules depend on the SDK, but Modules must not depend directly on the Platform and the Platform must not depend directly on Modules. SDK tooling may generate Module manifests from Go Module definitions, and the generated manifest still remains the build-time artefact consumed and validated by the Supervisor.

---

## Alternatives Considered

| Alternative | Outcome | Reason |
|-------------|---------|--------|
| SDK as framework | Rejected | It would accumulate behaviour and reduce Platform ownership clarity. |
| SDK as helper library | Rejected | It under-specifies the contract authority needed by Modules. |
| Modules import Platform internals | Rejected | It couples Modules to Runtime implementation details. |
| Platform imports Modules directly | Rejected | It breaks selected build-time composition and Module independence. |
| Source code as discovery authority | Rejected | Supervisor discovery must remain manifest-driven and non-executing. |

---

## Consequences

The SDK should be among the most stable Mosaic repositories, so breaking SDK changes should be rare and deliberate. Module authors can build against the Platform contract without understanding Platform implementation, and the Platform can in turn evolve internals while preserving SDK compatibility. Manifest generation can therefore improve developer ergonomics without weakening Supervisor validation.

---

## Implementation Implications

SDK repository structure should reinforce contract vocabulary, with the proposed shape below.

```text
mosaic-sdk/

    capabilities/
    events/
    models/
    module/
    permissions/
    registration/
    helpers/
    testing/
```

SDK tests should include contract assertions and provider fixtures, and CLI tooling should provide developer workflows such as the following.

```text
mosaic new module
mosaic dev
mosaic build
mosaic validate
mosaic publish
```

The CLI owns developer workflow, whereas the SDK owns developer contract.

---

# MEG-006 ADR-003 — Developer Platform As Integrated Toolchain

**Status**

Accepted

**Decision Date**

2026-07-14

---

## Context

The Mosaic SDK defines the public contract between Platform and Modules, but a library alone does not provide scaffolding, local composition, real-Platform integration testing, validation, packaging or publication workflows. Requiring Module authors to understand Supervisor internals, Build Workspaces, generated imports and runtime assembly would expose infrastructure that the Developer Platform can automate consistently, yet that development convenience must not create a second Platform architecture or a runtime plugin model.

---

## Decision

Mosaic will define a Developer Platform composed of:

- Mosaic SDK
- Mosaic CLI
- Development Supervisor
- production-equivalent Development Platform
- Test Harness Modules
- local Module composition
- validation, packaging and publication tooling

The SDK owns developer contracts and the CLI owns developer workflow, while the Development Supervisor orchestrates local rebuilds through the Build Pipeline. It is a development-only Supervisor implementation that should reuse production Supervisor behaviour wherever practical while adding file watching, local source mapping, automatic restart, client notification and development diagnostics.

The Development Platform is the real Platform running in development configuration, and Test Harness functionality is delivered through explicit Modules that provide deterministic capability implementations. Local Modules are statically composed into candidate Platform binaries and do not require publication to a remote catalogue, so Test Harness Modules and Local Modules participate as peer Modules in the same Development Platform composition.

---

## Alternatives Considered

| Alternative | Outcome | Reason |
|-------------|---------|--------|
| SDK library as the complete developer experience | Rejected | A contract library should not own scaffolding, orchestration, packaging or publication workflows. |
| Mock development runtime | Rejected | It would allow development behaviour to drift from the real Platform. |
| Runtime hot loading for local Modules | Rejected | It would create a development-only plugin architecture unlike production composition. |
| Platform-owned fake capabilities | Rejected | Test Harness Modules preserve normal capability contracts without adding hidden test behaviour to the Platform. |
| Manual Go and Build Workspace orchestration | Rejected | It exposes repetitive infrastructure and creates inconsistent development environments. |
| Publication required for every local rebuild | Rejected | Local path composition can preserve static linking without remote catalogue publication. |
| Separate development composition engine | Rejected | Development should continuously exercise the production Build Pipeline and static composition model. |

---

## Consequences

Module development can feel like ordinary Go while using a real Mosaic Platform, and the CLI becomes the primary interface for Mosaic-specific developer workflows. Development and production retain the same static Module composition architecture, so the Developer Platform becomes a broader ecosystem than the SDK without weakening the SDK's intentionally small contract boundary. Developer tooling must therefore remain observable enough to diagnose build, registration, health-check and activation failures.

---

## Implementation Implications

The CLI should support a coherent path from scaffolding to publication, with conceptual commands as follows.

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

The Development Supervisor should watch local sources, request isolated rebuilds, use development health-check timing and expose verbose diagnostics. After a healthy candidate is activated, it should restart or switch the Development Platform and notify connected clients. The CLI may launch the Web Shell and browser as part of `mosaic dev`, while allowing headless operation.

The Build Pipeline should continue to own workspace preparation, Go dependency handling, generated imports and compilation. Publishing protocols and stable command schemas should be specified separately before they become compatibility commitments.

---

# MEG-006 ADR-004 — Test Harness As Development Modules

**Status**

Accepted

**Decision Date**

2026-07-14

---

## Context

Module development needs deterministic Metadata, Media, Artwork, Authentication, Search, Recommendations and Event Sources without requiring every production integration. A special mocking framework or test-mode Platform would exercise different architecture from production and allow capability registration, routing, permissions and Event Bus behaviour to drift, whereas the Developer Platform already supports statically composing development-only Modules alongside Local Modules.

---

## Decision

Mosaic will implement Test Harness functionality through ordinary development-only Modules. Test Harness Modules will provide deterministic capability implementations through normal SDK contracts, and they will participate in manifest discovery, Build Pipeline composition, SDK registration, Module lifecycle, Capability Manager routing, permissions and Event Bus delivery.

The Development Supervisor should include the default Test Harness composition automatically for development workflows, and Test Harness Modules and Local Modules remain peers inside the real Development Platform. Event simulation must use declared Test Harness event-source Modules and the normal Event Bus path, so test tooling must not impersonate another Module's identity or event namespace.

---

## Alternatives Considered

| Alternative | Outcome | Reason |
|-------------|---------|--------|
| Mock Platform | Rejected | It would not exercise production Platform composition and behaviour. |
| Platform test-mode branches | Rejected | Hidden test behaviour would weaken production fidelity. |
| External mocking framework as primary integration environment | Rejected | Capability providers can supply deterministic behaviour through normal Module contracts. |
| Hardcoded fixtures inside the Platform | Rejected | Fixture ownership belongs to replaceable Test Harness Modules. |
| Arbitrary event namespace impersonation | Rejected | It violates Module event ownership and weakens diagnostic identity. |
| Versioned Scenario Profiles | Deferred | The concept is valuable, but schema, compatibility and CLI contracts require a later protocol decision. |

---

## Consequences

Development continuously validates the Module architecture itself, and deterministic data can support Module, UI and automated integration development without mutable external services. The Platform remains free of test-only capability implementations, which is why Test Harness packages require controls that exclude them from production composition by default. Event simulation likewise remains faithful to event ownership rather than becoming a privileged bypass.

---

## Implementation Implications

The Test Harness should provide deterministic baseline datasets and capability providers, and the CLI may expose event and scenario controls only through declared Test Harness contracts. [MIP-002](../../protocols/mip-002-module-manifest-protocol/index.md) should define development-only Module eligibility before it becomes stable manifest metadata, and a future Scenario Profile protocol should define versioned datasets, provider state, personas, deterministic failures and event schedules.

---

# Relationship To [MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md)

[MDG-001](../../documentation/mdg-001-documentation-authority-guide/index.md) defines ADR structure, review expectations, lifecycle and cross-reference rules, so this guide should reference decisions that affect it without redefining the decision process.

---

# Review Guidance

During review, confirm that the guide and any related decision record agree. If a decision changes the meaning of this guide, update the affected chapter and reference the decision from this page.
