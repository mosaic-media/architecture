# Repository names encode role, not the org — drop the redundant prefix

**Status:** Accepted; the convention stands and the table below is the state of the day it was applied. Two of its rows have moved since: `sdui` was renamed again to `contracts` by [contracts#6](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0006-contracts-protobuf-workspace.md) (`github.com/mosaic-media/contracts`), and the three web repositories left untouched here were consolidated into `web` and archived by [web#3](https://github.com/mosaic-media/web/blob/main/docs/adr/0003-frontend-workspace.md)
**Date:** 2026-07-21

## Context

Every repository in the `mosaic-media` org carried a `mosaic-` prefix:
`mosaic-platform`, `mosaic-sdk`, `mosaic-sdui`, `mosaic-module-stremio`,
`mosaic-architecture`, and the three web repos. The org name already namespaces
them, and so does the local checkout — the prefix restated, on every clone URL
and every Go import path, a fact the surrounding context had already given. It
was decoration.

Decoration is not free. A prefix that appears *everywhere* carries no
information *anywhere* — and that is the problem, because there is exactly one
axis where a repository name *should* carry information and the blanket prefix
was drowning it: **direction of integration.** Two kinds of repo sit at Mosaic's
edges and point opposite ways:

- **Inbound** — Mosaic consumes a foreign system. The Stremio integration is a
  Go client of the Stremio addon protocol, built against the SDK, importing
  nothing of the Platform ([platform#15](https://github.com/mosaic-media/platform/blob/main/docs/adr/0015-module-capability-and-invocation.md),
  [module-stremio-addons#1](https://github.com/mosaic-media/module-stremio-addons/blob/main/docs/adr/0001-completing-the-stremio-source-surface.md)). It is an
  anti-corruption layer: the foreign shape stops at its boundary.
- **Outbound** — Mosaic exposes *itself* through a foreign client's protocol, so
  that client can talk to Mosaic thinking it is talking to something else. A
  Jellyfin-compatible adaptor is the motivating case. It is a facade: Mosaic's
  shape is hidden behind the foreign one.

These are inverses. A bare name — `stremio`, `jellyfin` — hides the direction
*and* reads as a fork or mirror of the upstream project rather than as Mosaic's
adaptor to it. This is the one place a prefix earns its keep.

[web#3](https://github.com/mosaic-media/web/blob/main/docs/adr/0003-frontend-workspace.md) asked a related but distinct question —
*how many* repositories should exist, and which boundaries justify a split. This
ADR asks the orthogonal question: *whatever* repositories exist, **what are they
called.** The two compose: 0042 decides the web packages collapse into one
workspace; this ADR decides that workspace is named `web`.

## Decision

**Drop the `mosaic-` prefix. Name a repository for the role it plays, and add a
prefix only where the prefix is informative — where it signals the direction of
an integration, not merely that the repo belongs to Mosaic.**

| Category | Naming | Examples |
|---|---|---|
| **Core / contracts** | bare name | `platform`, `sdk`, `sdui`, `architecture` |
| **Modules** — inbound, Mosaic consumes an upstream (ACL) | `module-<system>` | `module-stremio-addons` |
| **Consumer modules** — act on the materialised library rather than sourcing from an upstream | `module-<capability>` | `module-remote-playback` ([platform#25](https://github.com/mosaic-media/platform/blob/main/docs/adr/0025-playback-consumer-and-media-origin.md)) |
| **Gateways** — outbound, Mosaic hosts a foreign protocol for downstream clients (facade) | `gateway-<system>` | *reserved — none built; e.g. a future `gateway-jellyfin`* |
| **Clients** — web / native | target name, not framework name | `web` ([web#3](https://github.com/mosaic-media/web/blob/main/docs/adr/0003-frontend-workspace.md)); future `ios`, `android` |

Four points of the scheme are load-bearing:

- **A consumer module names its *capability*, because it has no upstream.**
  [platform#24](https://github.com/mosaic-media/platform/blob/main/docs/adr/0024-capability-gated-affordances.md)'s consumer roles act on the
  materialised library rather than pulling a system in, so `<system>` has nothing
  to fill it. `module-remote-playback` names what it does. It keeps the `module-`
  prefix because it is a Module in the [platform#4](https://github.com/mosaic-media/platform/blob/main/docs/adr/0004-static-go-module-composition.md)
  sense — compiled in, SDK-only, independently versioned — and the prefix marks
  that shape, not the direction.
- **`module-<system>` names the *foreign system*, precisely.** The Stremio repo
  is `module-stremio-addons`, not `module-stremio`, because it is specifically a
  client of the Stremio **addon protocol** — not the Stremio SDK, not the
  player. The precision is the point of the name.
- **`gateway-*` is reserved, and inverts `module-*`.** A module is an
  anti-corruption layer pulling an upstream *in*; a gateway is a facade pushing
  Mosaic's surface *out* under a foreign protocol. Different direction, different
  prefix, so the two never read alike in a repo list. No gateway is built, and
  its implementation shape — whether a gateway is itself a Module in the
  [platform#4](https://github.com/mosaic-media/platform/blob/main/docs/adr/0004-static-go-module-composition.md) sense or Platform transport
  code — is out of scope here and undecided.
- **Clients take the *target* name, never the framework.** `mosaic-media/web`,
  not `mosaic-media/react`: a framework name reads as a fork of that framework
  and says nothing about which client it is. `web`, `ios`, `android` name the
  thing the user runs.

**Package identity is not repository identity.** The npm scope already decouples
them — `@mosaic-media/sdui-react` is unchanged by any repo rename, because the
package boundary ([platform#12](https://github.com/mosaic-media/platform/blob/main/docs/adr/0012-published-contract-surface.md)), not the repo
boundary, is what a consumer depends on. Only two things move with a repo name:
the GitHub URL (which GitHub redirects) and the **Go module path** (which it does
not — see Consequences).

### Executed 2026-07-21

The rename was carried out the day this ADR was accepted. Go module paths were
rewritten leaf-first so each downstream `require` resolved against a real
published tag; the module *identity* changing warranted a minor bump on each.

| Was | Now | Go module path | New tag |
|---|---|---|---|
| `mosaic-architecture` | `architecture` | — (docs) | — |
| `mosaic-platform` | `platform` | `github.com/mosaic-media/platform` | — (application; untagged) |
| `mosaic-sdk` | `sdk` | `github.com/mosaic-media/sdk` | v0.8.0 |
| `mosaic-sdui` | `sdui` | `github.com/mosaic-media/sdui` | v0.3.0 |
| `mosaic-module-stremio` | `module-stremio-addons` | `github.com/mosaic-media/module-stremio-addons` | v0.8.0 |

The three web repos (`mosaic-shell`, `mosaic-sdui-react`, `mosaic-storybook`)
were left untouched pending the [web#3](https://github.com/mosaic-media/web/blob/main/docs/adr/0003-frontend-workspace.md)
consolidation into `web`; renaming them individually would be work thrown away by
that merge.

## Alternatives considered

**Keep the `mosaic-` prefix everywhere (status quo).** *Rejected.* The org and
the checkout already namespace every repo, so the prefix is pure restatement —
and by appearing uniformly it flattens the one distinction that matters, leaving
`mosaic-module-stremio` and a future `mosaic-gateway-jellyfin` no more visibly
opposite than any two repos in the list.

**Bare names everywhere, including the integrations** — `stremio`, `jellyfin`.
*Rejected.* This erases direction and, worse, makes Mosaic's adaptor to a project
share a name with the project itself; `mosaic-media/jellyfin` reads as a fork of
Jellyfin, not as Mosaic's Jellyfin-compatible gateway. The prefix here is the
disambiguation.

**Encode direction only in the repo description or topic, not the name.**
*Rejected.* The name is the first and most repeated thing anyone sees — the clone
URL, the Go module path, every import line. A convention that lives only in a
description disciplines nothing that a reader actually reads.

**Framework-named clients** — `react`, `swiftui`. *Rejected*, for the same reason
as bare-named integrations: `mosaic-media/react` reads as a fork of React and
does not say *which* client it is. The target name does both jobs.

## Consequences

- **The Go module path rename is the one real cost, and it was paid now on
  purpose.** A GitHub rename redirects the URL, so `git` and `go get` keep
  resolving the old path — nothing breaks the instant it happens. But the
  `module` line in `go.mod` and every importer's path do **not** follow the
  redirect; they must be rewritten and retagged in lockstep. That is cheapest
  pre-1.0 with in-house consumers only, which is exactly now. Done later, across
  external consumers, it is a breaking change on a public surface.
- **npm identities are untouched** — `@mosaic-media/sdui-react` and its siblings
  keep their names and versions; downstream sees no break.
- **`gateway-*` is reserved but empty.** The first outbound adaptor — a
  Jellyfin-compatible gateway is the anticipated one — instantiates the category
  and will trigger its own ADR for *what a gateway is*, distinct from this ADR's
  concern of what it is *called*.
- **This refines [web#3](https://github.com/mosaic-media/web/blob/main/docs/adr/0003-frontend-workspace.md).** That ADR used the
  working name `mosaic-web`; under this convention the consolidated client
  workspace is `web`.
- **"Gateway" enters the controlled vocabulary** (`docs/index.md`) as a reserved
  term, so the inbound/outbound pair keeps one meaning each and `gateway` never
  drifts into naming an inbound thing.
- **Loose ends remain.** Local checkout folders still read `mosaic-*` (cosmetic;
  builds do not care), and a handful of doc links still point at the old GitHub
  URLs (they redirect, but should be corrected when those pages are next
  touched, per this repository's "the document is wrong, fix it" rule).
