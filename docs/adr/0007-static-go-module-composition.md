# Static Go module composition

**Status:** Accepted
**Date:** 2026-07-14

## Context

Mosaic needs an extensibility model that fits Go instead of fighting it. Runtime plugin systems introduce complexity through dynamic loading, RPC boundaries, reflection, version skew and operational failure modes, whereas Go already provides strong primitives for modular composition:

- modules
- semantic versions
- static linking
- explicit imports
- package initialisation

Mosaic should use those primitives directly.

## Decision

Mosaic does not support runtime plugins. Modules are ordinary Go libraries that implement the Mosaic SDK, and the Supervisor resolves selected Module manifests and invokes the Build Pipeline.

The Build Pipeline creates a temporary build workspace, updates the temporary `go.mod`, generates a single `imports.go` file containing blank imports for the selected Modules, and builds a statically linked Platform Binary. Each Module uses `init()` only to register itself with the SDK registry, and at Platform startup the Platform asks the SDK registry for registered Modules. No reflection, scanning, dynamic library loading or Module RPC boundary is required.

`imports.go` is the only generated source required for Module integration, because Capability Managers, event handling, GraphQL schema contribution and provider routing must operate through SDK contracts rather than generated glue code.

## Alternatives considered

**Runtime plugin loading.** *Rejected:* it adds dynamic loading and compatibility complexity that Go does not optimise for.

**Module RPC processes.** *Rejected:* it turns local capability composition into distributed-system coordination, paying a distributed-systems cost for a problem that is not distributed.

**Reflection-based discovery.** *Rejected:* it weakens explicitness and makes startup less deterministic.

**Source-code analysis by the Supervisor.** *Rejected:* manifests should be the source of truth, and Go source should not be inspected to establish architecture.

## Consequences

The final Runtime is a single statically linked Go executable, so to the finished Platform Binary, Platform code and Module code are both ordinary Go code. Module extensibility remains deterministic because the Build Pipeline imports exactly the selected Modules.

The Supervisor stays manifest-driven and does not edit source repositories, whereas the Build Pipeline owns temporary workspace preparation, `go.mod` updates, generated imports and package build mechanics. Module `init()` functions become part of the architecture, and must therefore remain registration only.

Development tooling must preserve the same model. The Development Supervisor may orchestrate compilation of local Modules into a development Platform through the Build Pipeline, but it should not introduce runtime loading semantics — see ADR 0009.

## Implementation implications

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

The Test Harness should provide fake capability providers for integration testing against a real development Platform, as described in ADR 0010.
