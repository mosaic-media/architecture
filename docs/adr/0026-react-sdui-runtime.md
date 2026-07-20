# 26. The React SDUI runtime is a shared package

**Status:** Accepted
**Date:** 2026-07-20

## Context

[ADR 0023](0023-server-driven-ui-and-the-shell.md)–[ADR 0025](0025-sdui-contract-repository.md) established Server-Driven UI, the primitive/definition component model, and the technology-agnostic contract ([`mosaic-sdui`](https://github.com/mosaic-media/mosaic-sdui)). The **web** renderer of that contract — the React implementation of the primitives, the registry, the recursive renderer, the definition expander, the runtime context/provider, and the token-driven skin — was first written inside the Shell.

But more than one web surface needs to render SDUI. The Shell is one; a **component storybook** is another; embeds and future surfaces will be more. If the renderer lives inside the Shell, every other consumer depends on a package published *out of the Shell's repo*, which makes the Shell privileged and invites the renderer to drift as it is copied.

## Decision

Extract the React renderer into its own repository and published package — **[`mosaic-sdui-react`](https://github.com/mosaic-media/mosaic-sdui-react)** / `@mosaic-media/sdui-react`. It is the reference **web** implementation of the [ADR 0024](0024-primitives-and-definitions.md) primitive vocabulary, and the Shell and the storybook consume it as **peers**.

- It is a **client implementation**, not the contract. The contract (`@mosaic-media/sdui`, Apache-2.0) is technology-agnostic data; this is one specific way to render it, in React. A native client (Flutter) would be a *separate* runtime implementing the same contract — not this package.
- It is therefore **AGPL-3.0-only** — first-party client code, like the Shell ([ADR 0022](0022-licensing.md)). React is a peer dependency; it builds to `dist` and ships `@mosaic-media/sdui-react/styles.css`.
- The **Shell** ([`mosaic-shell`](https://github.com/mosaic-media/mosaic-shell)) is now a thin app — chrome, routing, mock screens — on top of this runtime.
- The **storybook** ([`mosaic-storybook`](https://github.com/mosaic-media/mosaic-storybook)) is a separate showcase: every component rendered live from `@mosaic-media/sdui` data beside the `UINode` payload that produced it, deployed to GitHub Pages. Bespoke rather than Storybook.js, because a definitions-as-data component's API *is* its payload, not React props.

## Alternatives considered

**Keep the renderer inside the Shell (a monorepo).** Makes the Shell privileged; every other consumer depends on a package published from the app's repo, and the app-vs-library boundary is muddy. *Rejected* — the renderer is a shared library with multiple peers, so it is its own repo, matching how the contract and the SDK are their own repos.

**One runtime repo for all clients (React and Flutter together).** Per-language rendering engines share nothing as code — only the contract. *Rejected* — a Flutter runtime is its own repo implementing the same contract.

**Storybook.js.** Its args/controls model documents React prop APIs; Mosaic components are data. *Rejected* in favour of a bespoke render-plus-payload view.

## Consequences

- The web renderer is a **versioned shared library**. A change to the primitives or the skin is a runtime version bump that the Shell and storybook pick up as peers; when the Mosaic Design Language lands, it ships here (a token swap) and every web surface updates together.
- The repo topology settles: `mosaic-sdui` (contract, Apache) → consumed by producers and clients; `mosaic-sdui-react` (runtime, AGPL) → consumed by web clients; `mosaic-shell` and `mosaic-storybook` → peer consumers of both.
- **Known duplication to resolve:** the standard definitions currently exist both baked into `@mosaic-media/sdui-react` and seeded as data in `@mosaic-media/sdui`. They match today; the runtime should eventually load them from the contract package so there is a single source. Recorded, not yet done.

## Implementation

`mosaic-sdui-react` publishes `@mosaic-media/sdui-react` to npm (`v0.1.0`); `mosaic-shell` and `mosaic-storybook` require it (`^0.1.0`), with a `file:` link for local cross-repo work. The storybook deploys to `mosaic-media.github.io/mosaic-storybook` via GitHub Actions.
