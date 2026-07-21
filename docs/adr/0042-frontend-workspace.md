# 42. The web frontend is one workspace; split repos only to enforce a boundary

**Status:** Proposed
**Date:** 2026-07-21

## Context

The repository count has reached eight, and each split was reasonable when it was
made. With a multi-client future pushing new contracts into being
([ADR 0041](0041-cross-client-transport-two-lane-rpc.md)), it is worth checking
the topology against a sharper rule before it grows further.

The governing insight: **isolation between consumers is enforced by the published
*package* boundary, not the *repository* boundary.** A repo split earns its keep
only when it enforces something a package cannot:

- a **license** separation (Apache/MIT contract vs AGPL client code, [ADR 0022](0022-licensing.md));
- a **trust / compile** boundary (a third party must compile against it *without*
  the rest — the executable stop point of [ADR 0016](0016-published-contract-surface.md));
- a **polyglot** contract two language ecosystems both consume.

Absent one of those, a split is *organizational* — same license, same toolchain,
co-evolving — and it buys no isolation the package boundary does not already give,
while costing a version-pinned cross-repo dance on every change.

Measured against that rule (verified from the repos), five boundaries are
load-bearing and three are organizational:

| Repo | License | Boundary it enforces | |
|---|---|---|---|
| `mosaic-platform` | AGPL | the application itself | **load-bearing** |
| `mosaic-sdk` | Apache | third-party compile boundary — zero platform deps *by construction* ([ADR 0016](0016-published-contract-surface.md)) | **load-bearing** |
| `mosaic-module-stremio` | MIT | the extension model, dogfooded — imports only the SDK ([ADR 0019](0019-module-capability-and-invocation.md)) | **load-bearing** |
| `mosaic-sdui` | Apache | the polyglot contract — consumed by the Go side *and* the TS side | **load-bearing** |
| `mosaic-architecture` | CC-BY | docs — different license, audience, cadence | **load-bearing** |
| `mosaic-shell` | AGPL | — | *organizational* |
| `mosaic-sdui-react` | AGPL | — | *organizational* |
| `mosaic-storybook` | AGPL | — | *organizational* |

The last three are the fan-out: all **AGPL-3.0-only**, all React/TS/Vite, tightly
coupled (the Shell and the storybook both consume the runtime; the storybook also
consumes the contract), ~88 files combined. None of the three boundaries enforces
anything a package boundary does not.

[ADR 0026](0026-react-sdui-runtime.md) extracted the React runtime into its own
repo for a real reason — so the renderer would not be published *out of the
Shell's repo* and make the Shell privileged. That reasoning stands. But it argues
against "the renderer inside the app," not against a **neutral workspace** in
which the renderer is a first-class sibling package no app owns.

## Decision

**The three AGPL web packages — the runtime, the Shell, and the storybook — live
in one workspace repository, each still published as an independent package. A
repository is split from that workspace only where the split enforces a license,
a trust/compile, or a polyglot-contract boundary.**

- One repo — a pnpm/npm **workspace** (working name `mosaic-web`) holding
  `@mosaic-media/sdui-react` (the runtime → npm), the Shell (the app), and the
  storybook (GitHub Pages).
- **`@mosaic-media/sdui-react` stays an independently versioned, independently
  published npm package.** A consumer requires only it; the Shell and the
  storybook are sibling workspace packages, never transitive dependencies of the
  runtime. The package boundary — the thing that actually protects a consumer — is
  unchanged. This honours [ADR 0026](0026-react-sdui-runtime.md)'s "shared,
  versioned package" intent; only its *"own repository"* clause is amended.
- **No app is privileged.** The runtime is published from a neutral workspace
  where it is a peer of the Shell and the storybook alike — not from the Shell's
  repo, which was ADR 0026's actual objection.
- **The storybook co-locates with the runtime it documents** — the universal
  pattern — so a component change is one commit, not a two-repo version-pin.
- **The load-bearing boundaries are untouched.** `mosaic-sdui` (the Apache
  contract) stays its own repo, and nothing folds into `mosaic-platform`.
  Smallness is not a reason to merge a contract; its separateness *is* the
  boundary.

The durable rule, stated plainly: **prefer a workspace of published packages over
a repository per package; keep a repository boundary only where it enforces a
license, a trust/compile boundary, or a polyglot contract.** This is the same
rule [ADR 0041](0041-cross-client-transport-two-lane-rpc.md) applies on the
contract side — the SDUI and transport protobuf contracts share one buf workspace
as two packages, because once their schemas import each other the split is
organizational.

## Alternatives considered

**Status quo — three web repos.** *Rejected.* Three organizational splits, each
imposing a cross-repo version dance. The storybook↔runtime split especially: the
storybook exists only to render the runtime's components, and every component
change is a two-repo, version-pinned round trip.

**Merge only the storybook into the runtime.** *Considered.* The minimal move
(8 → 7) and the single clearest win, since a storybook belongs with its library.
A fine first step, but it leaves the Shell↔runtime split, which is the same
organizational shape; the full workspace (8 → 6) finishes the job with no extra
principle.

**Fold the runtime into the Shell.** *Rejected*, for ADR 0026's reason: it
privileges the app and publishes the renderer out of an app repo. The *neutral*
workspace is precisely what makes consolidation safe — the runtime is nobody's
subordinate.

**Collapse the contracts too — `mosaic-sdk` / `mosaic-module-stremio` /
`mosaic-sdui` into `mosaic-platform`.** *Rejected.* Those enforce license and
trust boundaries; merging them destroys the executable "compile against the SDK
without the platform" guarantee ([ADR 0016](0016-published-contract-surface.md))
and mixes Apache/MIT into AGPL. The small contract repos are not the fan-out;
*unenforced* repos are.

## Consequences

- **One CI with path filters** (build the storybook only when it or the runtime
  changes), coordinated versioning across the three web packages, and a single
  lint/test gate. Modest, standard frontend-workspace setup.
- **Different artifact types together** — an npm library, a deployed app, a Pages
  site — which is routine for design-system monorepos; the workspace tool handles
  per-package build and deploy.
- **The ADR 0026 duplication is easier to close.** ADR 0026 recorded that the
  standard definitions live both baked into the runtime and seeded in the
  contract; co-locating the runtime with its consumers makes the single-source fix
  easier to land, though the dedup still crosses the Apache/AGPL line into the
  contract package and is not itself changed here.
- **Less drift.** One fewer place for the renderer to be copied, and the storybook
  can no longer lag the runtime version.
- This **amends [ADR 0026](0026-react-sdui-runtime.md)** (the "own repository"
  clause) and refines [ADR 0025](0025-sdui-contract-repository.md)'s topology note.
  It does **not** change licensing ([ADR 0022](0022-licensing.md)) — every merged
  package stays AGPL-3.0-only.

## Implementation implications

Create the `mosaic-web` workspace and move `mosaic-sdui-react`, `mosaic-shell`
and `mosaic-storybook` in as workspace packages, preserving git history where
practical. Keep the published npm identities (`@mosaic-media/sdui-react`, …) and
their versions unchanged so downstream consumers see no break. Wire one CI with
path-filtered jobs and the storybook's Pages deploy. Archive the three old repos
with a forwarding pointer. Set ADR 0026's status to Amended on acceptance.

This is pure topology — no runtime behaviour changes — so it can land
independently of, and in parallel with, the ADR 0041 transport work. If a smaller
first step is preferred, merge the storybook into the runtime (8 → 7) and take the
Shell in a second pass; the end state is the same workspace.
