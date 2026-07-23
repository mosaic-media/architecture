# 39. Server-owned navigation: a screen-agnostic client

**Status:** Proposed, and **not** what is built. The Shell maps URLs to screens
itself — `history.ts` parses `location.pathname` into a `{screen, params}` route
and renders routes back to paths — which is the ADR 0032-era arrangement this
record exists to replace, and the opposite of the opaque tokens it requires. What
does hold is the surrounding behaviour: the client re-declares its current route
on connect, and nav actions are the ones the server authored. Treat the gap as
open rather than as this record being partly built.
**Date:** 2026-07-21

## Context

The server-driven-UI thesis ([ADR 0023](0023-server-driven-ui-and-the-shell.md),
[ADR 0031](0031-server-owned-app-shell.md)) is that the server owns the whole
interface and a thin client renders it, so the experience can change **without
shipping a client**. That last clause is not a nicety. The web Shell can be
redeployed freely, but the planned Flutter client cannot: **every client release
is an app-store review.** So any change that requires touching the client — a new
screen, a renamed screen, a different default landing screen, a new URL shape,
changing what counts as a route versus a transient overlay — defeats the entire
premise the moment there is a native client. The bar is therefore absolute: a
navigation change must be a **server deploy only**.

The live-session/history work ([ADR 0032](0032-live-session-websocket.md), slice
3) put the browser History/URL layer in the Shell, correctly — `pushState`,
`popstate` and reading `location` are browser-only APIs the server cannot call.
But that layer currently also holds **screen-specific knowledge**:

- it **hardcodes the default screen** (empty path → `home`);
- it **parses a URL into a `{screen, params}` route** (so the URL grammar and the
  set of screens live partly in the client);
- it **infers the current screen** to highlight the active nav item.

Each of those means a routing change touches the client. On web that is a
redeploy; on Flutter it is a store review. That is the coupling this ADR removes.

## Decision

**The client holds no screen-specific navigation knowledge. Every navigation
semantic — the default screen, the URL↔screen mapping, which screen is current,
which nav item is active, what is a route versus a transient overlay — is
server-owned. The client is a *generic* executor of browser-history mechanics
plus a renderer, exchanging opaque location and screen tokens with the server and
never interpreting them.**

Concretely, the live protocol ([ADR 0032](0032-live-session-websocket.md)) grows
a navigation contract:

- **The client reports history events to the server as opaque strings; it never
  parses them.**
  - `hello` carries the boot URL (`location.pathname + location.search`)
    verbatim.
  - On `popstate` (back/forward) the client sends the entry's URL/token back as a
    navigate-by-URL intent.
  - A nav or action click dispatches the `navigate`/`invoke` action **the server
    authored** into the shell payload (a `NavItem`'s `navigate(screen)` already
    comes from the server — the client echoes it, it does not invent screen
    names).

- **The server drives the URL and the current-screen identity.** Each server→
  client `render`/`shell` message may carry a navigation directive:
  `{ url, history: "push" | "replace" | "none", screen: <opaque id> }`.
  The client applies it mechanically — `pushState`/`replaceState` with the
  server's opaque `url`, records `screen` as the current-screen id (used only for
  nav highlighting, by string equality against the server-authored nav items),
  and renders the content. **No directive** means leave the URL and current
  screen unchanged — which is exactly how a transient search overlay renders
  results without becoming a history entry.

- **URLs stay human-readable, but the client treats them as opaque.** The server
  computes legible URLs (`/detail?ref=…`, `/home`) so links remain shareable and
  deep-linkable, and the client only ever **reads** the URL (to report it) or
  **writes** it (on the server's directive) — it never parses one into a screen.
  Shareability is kept; the parsing grammar moves entirely to the server.

The result: adding or renaming a screen, changing the default landing screen,
reworking the URL scheme, or reclassifying a screen as transient is a **server
change only**. The Flutter client ships once with the generic
history-executor + renderer and never needs a navigation-related update again.

## Alternatives considered

**Keep client-side routing (status quo).** *Rejected.* Every default/URL/screen
change is a client release — an app-store review on Flutter — which is precisely
what SDUI exists to avoid. Acceptable only while web is the only client, which is
not the plan.

**Opaque server-issued route tokens instead of human URLs.** *Considered and
folded in, not adopted wholesale.* The server could hand the client an opaque
token per screen and the client would just stash it in history, with no
human-readable URL at all — maximal client isolation. But it loses legible,
shareable deep-links. The decision keeps **human-readable URLs the client treats
opaquely**, which gives the same isolation (no client parsing) while preserving
shareable links.

**Config-driven client router: the client keeps a router but downloads its route
table from the server.** *Rejected.* It still ships routing logic in the client
and adds a config format and a sync path; "the server renders and directs the
history" is fewer moving parts and no client-side interpretation at all.

**Server re-emits the shell with the active nav item marked, instead of a
current-screen id.** *Considered.* It is marginally purer (the client does no
equality check at all), but it re-pushes chrome on every navigation, where the
shell is designed to persist ([ADR 0031](0031-server-owned-app-shell.md)). The
current-screen id in the render directive is lighter and keeps the highlight a
trivial equality of two server-provided values; either is server-owned, so this
is an implementation detail, not a boundary difference.

## Consequences

- **The client becomes truly navigation-agnostic** — no screen names, no default,
  no URL parsing. Any navigation change is a server deploy, so a native client
  never needs a store review for a UI/navigation change. This is what makes the
  SDUI promise real for Flutter, not just web.
- **The live protocol grows** a server→client navigation directive and a
  client→server navigate-by-URL intent. Both are versioned, as
  [ADR 0032](0032-live-session-websocket.md) already requires of the message
  schema.
- **The server gains a URL router** (path+query ↔ screen+params) beside the
  existing screen registry ([ADR 0029](0029-sdui-emit-side.md)) — a small,
  natural addition where the screen definitions already live.
- **Boot and back/forward each cost one extra round-trip** (client sends a URL,
  server resolves and renders). Negligible on a self-hosted/localhost link, and
  it is already how deep-links resolve. It also removes the current
  boot-time double render (the server pushing a default *and* the client
  re-declaring a route), since the client no longer declares a route at all — the
  server resolves the `hello` URL once.
- **Nav highlighting** is driven by a server-provided current-screen id rather
  than client inference.
- **Honest limit — what stays in the client, by necessity:** the *generic*
  History-API plumbing (call `pushState`, listen for `popstate`, read
  `location`). That is inherent browser mechanics, not screen knowledge, and a
  Flutter client carries the analogous generic navigation-stack plumbing. What is
  eliminated is every screen-*specific* fact. The line this ADR draws is:
  *mechanism* may live in the client; *policy* may not.

## Implementation implications

This refines [ADR 0032](0032-live-session-websocket.md) slice 3, superseding the
client-side default screen and URL parsing it introduced.

- **Platform** (`internal/transport/live`, `internal/transport/screens`): a URL
  router mapping a path+query to a screen+params and back, beside the screen
  registry; `hello` resolves its carried URL; `render`/`shell` messages carry the
  `{url, history, screen}` directive; the input handler marks a transient search
  render `history: "none"`; back/forward resolves a client-sent URL.
- **Shell** (`src/lib/live.ts`, `src/App.tsx`, `src/lib/history.ts`): strip route
  parsing and the default screen; `hello` sends the boot URL; apply the server's
  history directive (`pushState`/`replaceState`/none) with the opaque URL;
  `popstate` sends the entry's URL back; the current screen for nav highlighting
  comes from the server. `history.ts` collapses to "apply an opaque URL + a
  history op" — no screen vocabulary.

Not built in this ADR — proposed for review, then a slice of its own, so the
navigation contract is settled before the Flutter client is built against it
(the whole point being that the client is built once and left alone).
