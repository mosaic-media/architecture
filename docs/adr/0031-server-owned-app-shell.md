# 31. The Shell is a pure renderer; the app shell is server-emitted

**Status:** Proposed
**Date:** 2026-07-20

## Context

The server-driven UI thesis ([ADR 0023](0023-server-driven-ui-and-the-shell.md),
[ADR 0024](0024-primitives-and-definitions.md)) is that the server owns the
interface and a thin client renders it, so the UI can change without shipping a
client and a second client (a future Flutter app) renders the same payloads.

The built Shell cheats on this. Its sidebar, top bar, branding, library
thumbnails and the "Components" link are **hardcoded React chrome**; only the
content area renders a server payload ([ADR 0029](0029-sdui-emit-side.md)). So
the navigation and layout *cannot* change without a client deploy, and any
second client would have to re-implement the chrome by hand — exactly what SDUI
exists to avoid. The chrome was a walking-skeleton shortcut, not the
architecture.

## Decision

**The Shell renders payloads and owns no layout. The Platform emits the *app
shell* — the nav rail, top bar, branding and a content region — as a payload,
the same way it emits a screen. Without a reachable server the Shell shows only
a client-owned standby state, never chrome.**

The Shell keeps exactly three things, none of them layout:

- **The connection lifecycle** — connect, authenticate, retry.
- **A small set of client-owned meta states** — *connecting…*, *can't reach the
  server*, *standby*. These are the one thing that cannot come from the server,
  because they are shown precisely when the server is unreachable. They are
  deliberately minimal — a message and a spinner, not a fake app.
- **The renderer and primitives** — the engine that turns `UINode`s into pixels
  ([ADR 0024](0024-primitives-and-definitions.md)).

Everything else is a payload. The Platform emits an **app-shell layout**: a
root `UINode` with the navigation, chrome, and a named **content region** that
navigation fills. This needs a few contract additions to the SDUI vocabulary
([ADR 0024](0024-primitives-and-definitions.md), [ADR 0025](0025-sdui-contract-repository.md)) —
an app-shell/layout node with named regions, a nav-rail and nav-item, and
region-targeted rendering — and it **subsumes the mock chrome screens**
(home/settings/gallery), which become server-emitted or disappear.

This refines [ADR 0029](0029-sdui-emit-side.md): the Platform emits the *whole
shell*, not isolated screens; a screen renders **into the shell's content
region** rather than replacing the page. The `screen` registry becomes the
region's content source; the shell is the frame around it.

## Alternatives considered

**Keep client chrome; server only the content (status quo).** *Rejected:* the
navigation and layout cannot evolve without a client deploy, and a second client
re-implements the chrome — the two things the SDUI thesis exists to prevent.

**A client-owned "default chrome" shown while offline.** *Rejected:* the offline
state is a standby screen, not chrome. Rendering stale or invented chrome with no
live data behind it misleads — the honest offline signal is "not connected".

**A hybrid: some chrome client-owned, some server-owned.** *Rejected:* the line
is arbitrary and drifts over time. "All layout is a payload" is the rule that
stays honest; the client's only visuals are the meta states above.

## Consequences

The app's whole look and navigation become server-controlled, so they can change
without a release and a Flutter client renders the identical shell. The Shell
shrinks to a renderer plus a connection — which is what makes swapping its
transport to a live channel ([ADR 0032](0032-live-session-websocket.md)) a
contained change rather than a rewrite.

Two honest limits:

1. **The vocabulary needs the shell components.** An app-shell/layout with named
   regions and a nav rail are new standard components ([ADR 0024](0024-primitives-and-definitions.md));
   until they exist the shell cannot be expressed. Small, additive.
2. **The meta states are the client's only holdout.** *Connecting / unreachable /
   standby* live in the client forever, by necessity. Keeping that set tiny — and
   resisting the urge to grow a client-side "offline mode" — is the discipline
   this ADR asks for.
