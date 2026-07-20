# 29. The Platform's SDUI emit-side

**Status:** Accepted
**Date:** 2026-07-20

## Context

The client half of the server-driven interface is built: the Shell renders a
tree of `UINode`s carrying `Action` envelopes ([ADR 0023](0023-server-driven-ui-and-the-shell.md),
[ADR 0024](0024-primitives-and-definitions.md)), the contract is published with
a Go producer binding ([ADR 0025](0025-sdui-contract-repository.md)), and the
React runtime renders it ([ADR 0026](0026-react-sdui-runtime.md)). But the
**Platform emits no screens** — the Shell runs on mock payloads, because nothing
on the server builds a `UINode` tree from real state.

The provider-model backend ([ADR 0027](0027-modules-as-typed-capability-providers.md),
[ADR 0028](0028-virtual-and-materialized-content.md)) just made two screens
worth emitting real: a **user search screen** (search with no raw id) and an
**admin collection browser** (browse a module's catalogs, publish a selection).
The GraphQL those screens need — `searchAvailableContent`, `moduleCatalogs`,
`catalogItems`, `importContent` — exists. What is missing is the server building
the screens and a transport that serves them.

A `UINode`'s `Action` references a Platform operation *by name*: a `Query` action
names a query to run, an `Invoke` action names a mutation. So the emit-side is
not just "build a tree" — it is how screens are served *and* how their actions
bind to the operations that already exist.

## Decision

**The Platform emits screens through a GraphQL `screen(name, params)` query that
returns a `UINode` tree, built with the `mosaic-sdui` Go producer binding by a
Platform-owned screen registry. A screen's actions name the Platform's own
GraphQL operations.**

- **One transport, GraphQL.** `screen(name: String!, params: JSON): JSON`
  returns the serialized `UINode` tree. The Shell already speaks GraphQL, and a
  screen's `Query`/`Invoke` actions name GraphQL operations — so screens and the
  data their actions drive share one transport, rather than a screens endpoint
  that references operations on a different one. A dedicated `/screens` endpoint
  was the alternative; it splits the surface for no gain here.
- **A Platform-owned screen registry.** `name → builder(ctx, caller, params) →
  sdui.Node`, a closed set the Platform owns: `search` and `collections` now,
  `library`/`detail`/`playback` as they are built. The builder calls application
  **query services only** — the same rule GraphQL resolvers follow ([ADR 0016](0016-published-contract-surface.md)):
  a screen is a projection, never a persistence path, and never touches a store.
- **Screens are Platform-emitted; modules contribute data, not UI.** A module
  imports only the SDK and cannot import the SDUI binding or a Platform transport
  ([ADR 0008](0008-sdk-as-public-contract-language.md)), so it does not emit
  screens. The Platform composes a screen from module *data* — the provider
  results of [ADR 0027](0027-modules-as-typed-capability-providers.md) — not from
  module-supplied `UINode`s. A module extends *what content exists*; the Platform
  owns *how it is shown*.
- **Actions bind to the slice-3 operations.** The search screen's `SearchBar`
  submit is a `Query` action running `searchAvailableContent` into the
  results-grid region; each result card is `Invoke: importContent(ref)` to
  materialise, or `Navigate` to a detail screen. The collection browser lists
  `moduleCatalogs`/`catalogItems`; publishing a selection is `importContent`.
- **The virtual/materialized split is visible.** A result carries `InLibrary`
  ([ADR 0028](0028-virtual-and-materialized-content.md)); the builder renders an
  in-library item differently from a virtual one (a badge, and an *open* action
  rather than a *materialise* one), so the two planes read as one list without
  the user needing to know the model.
- **Auth is uniform.** `screen` carries the caller like every other query; each
  builder authorises through the services it calls, so a screen shows exactly
  what its caller may see.

## Alternatives considered

**A dedicated `/screens` HTTP endpoint, separate from the GraphQL data API.**
*Rejected:* a screen's actions reference GraphQL operations regardless, so a
second transport would straddle the two. One surface keeps screens and the
operations they invoke aligned.

**Modules emit their own screens.** *Rejected:* a module imports only the SDK and
cannot import the SDUI binding or a Platform transport ([ADR 0008](0008-sdk-as-public-contract-language.md)),
the same boundary that made `importContent` a generic Platform surface ([ADR 0019](0019-module-capability-and-invocation.md)).
The Platform composes screens from module data. (A future module-contributed-UI
story, if one is ever wanted, is its own decision, not this one.)

**The Shell builds `UINode`s from raw GraphQL data itself (a thin client
adapter).** *Rejected:* it bypasses the whole point of server-driven UI — that
the server owns the screen and a second client (a future Flutter app) renders
the same payload ([ADR 0023](0023-server-driven-ui-and-the-shell.md), [ADR 0024](0024-primitives-and-definitions.md)).
The screen must be built once, on the server.

## Consequences

The Shell stops running on mock payloads for these two screens — the first real
server-emitted screens, and the first time the extension backend is reachable by
a human through the interface rather than through raw GraphQL. The screen
registry is the seam every later screen slots into.

Three honest limits:

1. **Region-refresh protocol.** A `Query` action refreshing a named region (the
   search grid) needs the Shell and the emit-side to agree on how a partial
   result replaces a region. The contract has the `Into` field ([ADR 0025](0025-sdui-contract-repository.md));
   the end-to-end refresh is exercised for the first time here and may surface
   contract gaps — the same forcing-function role modules play for the SDK.
2. **Modules cannot contribute UI.** Deliberate ([ADR 0008](0008-sdk-as-public-contract-language.md)),
   but it means a module that wants a bespoke configuration screen has none; the
   Platform renders module settings generically. Named, not solved.
3. **The skin is still neutral.** These screens render on the Shell's neutral
   token skin; the Mosaic Design Language ([roadmap](../roadmap.md)) that replaces
   it is separate work.

## Implementation implications

The Platform gains a `go get github.com/mosaic-media/mosaic-sdui` dependency and
a screen package that builds `sdui.Node` trees from the application query
services, plus the `screen` GraphQL query over a registry. The two builders
(`search`, `collections`) read the slice-3 services and emit the standard
component vocabulary ([ADR 0024](0024-primitives-and-definitions.md)) — `Screen`,
`SearchBar`, `Grid`, `PosterCard`, `EmptyState`, `Button`. The Shell then points
those two routes at `screen(...)` instead of its mock payloads. Building the
screens is expected to pressure-test the `Action`/region contract, and any gap
found is a `mosaic-sdui` change, tagged and consumed like any other.
