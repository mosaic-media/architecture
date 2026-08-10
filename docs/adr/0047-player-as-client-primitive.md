# The player is a client primitive over a server-issued ticket

**Status:** Accepted; **built.** `playPart` resolves to
a `Player` node carrying a ticket URL, and the web runtime renders it. **The
capability declaration is now built**: `AttachRequest` carries an optional
`ClientProfile`, the web Shell fills it from the browser's own `canPlayType`,
and the Platform records it on the live session and ranks against it — the
hard-coded browser preference at the `playPart` call site is gone, surviving
only as the fallback for a client that declares nothing. **The four things this
line called unbuilt have all landed since**: the player reports progress
(`reportProgress`, dispatched from `sdui-react`'s player), the node carries
`subtitleTracks` ([ADR 0115](0115-a-styled-subtitle-goes-to-the-client.md)) and
a real `resumeAt`, and "what comes next" is a server-emitted `Button` the host
renders. `@mosaic-media/sdui-react` now depends on `hls.js` and `jassub`,
attached conditionally to read
[ADR 0109](0109-the-transcoded-stream-is-segmented.md)'s segmented origin and
ADR 0115's styled tracks — the condition
[ADR 0070](0070-the-web-player-is-the-browser.md) set for adopting a library,
met. **Partly superseded:**
the "web client is Shaka Player" bullet below was reversed by
[ADR 0070](0070-the-web-player-is-the-browser.md) — the renderer is a bare
`<video>` element. The rest of this record stands.
**Date:** 2026-07-22

## Context

[ADR 0045](0045-playback-consumer-and-media-origin.md) produces bytes at a URL and
[ADR 0046](0046-playback-state-is-platform-owned.md) records where the viewer got
to. Something has to actually play. That something sits on the wrong side of the
line Mosaic has held since [contracts#1](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0001-server-driven-ui-and-the-shell.md): the
server owns the interface and the client is a pure renderer
([ADR 0031](0031-server-owned-app-shell.md) went as far as emitting the app shell
itself).

Taken literally, that thesis says the Platform should emit the player's chrome —
its controls, its scrub position, its buffering state — as `UINode`s over the
session stream. That does not survive contact with video. A scrub bar tracks a
position that changes continuously; buffering, track switching and seeking are
sub-frame concerns; and every client platform has its own decoder pipeline
(`<video>` and Media Source Extensions on the web, ExoPlayer on Compose, AVPlayer
on iOS, libmpv on desktop) that cannot be driven by a declarative tree pushed over
a network. The four-client bar [contracts#5](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0005-cross-client-transport-two-lane-rpc.md)
set is precisely what makes this concrete rather than theoretical.

Stremio's answer is the one every real client converges on: the player is native,
and it is handed a URL, a set of tracks, a starting offset and enough metadata to
title itself. Its addons never touch the player.

The `Play` action already exists in the SDUI vocabulary (`playPart`), and the web
runtime answers it with a toast because there was nothing behind it. What it
should resolve to has never been decided.

## Decision

**The player is a structural client primitive, driven by a server-emitted node
carrying a playback ticket. The server decides *what* plays, *from where*, *from
what offset* and *what comes next*; the client owns the decoding pipeline and the
transport controls.**

- **`Play` resolves to a ticket, not to a screen.** Invoking the `playPart`
  action is an intent on the session; the Platform resolves the Part
  ([ADR 0045](0045-playback-consumer-and-media-origin.md)), mints a ticket and
  emits a `Player` node. The client never constructs a media URL and never talks
  to a module.
- **The client declares its capabilities on `Attach`.** Containers, video codecs
  and audio codecs it can decode, sent on the session intent it already issues
  ([contracts#5](https://github.com/mosaic-media/contracts/blob/main/docs/adr/0005-cross-client-transport-two-lane-rpc.md)). The Platform then
  never issues a ticket the client cannot play — it selects a stream the client
  can ([ADR 0048](0048-stream-selection-against-a-client-profile.md)). **The
  client declares; the server decides.** An earlier draft had the client refuse
  what it could not decode, which is the same rule stated backwards: it pushes a
  server decision into four clients and makes failure the normal path rather than
  the exception.
- **The `Player` node is the whole contract**: the ticket URL, the resume offset
  ([ADR 0046](0046-playback-state-is-platform-owned.md)), subtitle tracks, title
  and artwork for the player's own chrome, and the next-up reference for
  continuity. Every field is server-decided.
- **The web client is Shaka Player**, and is deliberately limited-mode. Shaka
  adds no codec support of its own — the browser decodes, and Shaka feeds it
  through MSE — but it is the right renderer for the adaptive path, and its
  static support probe is what the web client declares its profile from, so the
  profile is measured rather than assumed. A desktop client with libmpv is the
  answer to a fat profile and is a later thread.
- **This is the same move as `AppShell`, not an exception to it.**
  [ADR 0031](0031-server-owned-app-shell.md) established that a structural
  primitive may own a *mechanism* the server names but does not micro-manage —
  the shell owns its slot layout, the player owns its transport. The thesis is
  "the server owns the interface", not "the server emits every frame". Stated as
  a limit: **the server owns everything about a playback session except the
  decoding pipeline and the transport controls.**
- **Progress flows back as session intents**, coalesced by the Platform
  ([ADR 0046](0046-playback-state-is-platform-owned.md)). The client reports; it
  does not decide what the report means.
- **Continuity is server-decided.** What plays after this episode, and whether it
  auto-plays, is resolved server-side and delivered as the next-up reference. A
  client must never walk the graph to find the next episode — that would put
  library structure in four clients.
- **External handoff stays available as an explicit affordance**, not as the
  player: an `OpenURL` action on the ticket for mpv/VLC/Infuse users. It captures
  no progress, and that trade is the user's to make deliberately.

## Alternatives considered

**Emit the player chrome as SDUI.** *Rejected.* Maximally faithful to the thesis
and unworkable: a scrub bar pushed over a network is a per-frame round trip, and
every client would still need a native escape hatch for the decoder — so the
purity would be nominal while the cost would be real.

**External handoff only.** *Rejected as the primary path.* It is the cheapest
possible slice and it forfeits resume, watched state and continuity — i.e. it
forfeits [ADR 0046](0046-playback-state-is-platform-owned.md) entirely, which is
the half that makes the product feel alive.

**Let the client resolve the stream itself** (hand it the Part and let it pick).
*Rejected.* It puts source selection, debrid credentials and provider precedence
in every client, and re-implements them per platform — the exact failure
[ADR 0036](0036-capability-gated-affordances.md) rejected client-side gating for.

**A `player` *screen* rather than a node.** *Rejected as under-specified.* A
screen implies navigation semantics (back, deep link, history) that a playback
session does not have — a player is a surface over the current context, and it
must be able to sit above the shell without unmounting it. The overlay/surface
machinery already in the runtime is the right host.

## Consequences

- **The SDUI thesis gains its first stated limit, and it is a narrow one.** Two
  things are client-owned: the decoding pipeline and the transport controls.
  Writing that down is better than leaving four clients to each decide where the
  line falls.
- **The SDUI vocabulary grows a `Player` component** and `playPart` acquires a
  defined resolution after existing as a stub since the first mock screens.
- **Every client implements a player.** That is unavoidable — it is the one place
  platform-native code cannot be amortised — but the *contract* is one node, so
  the second client implements a renderer, not a policy.
- **A source picker becomes necessary on the detail screen.** With several streams
  resolved for one item, the user's choice is what answers
  [ADR 0027](0027-modules-as-typed-capability-providers.md)'s precedence seam for
  foreground playback. Background auto-play (next episode) still needs a rule and
  does not get one here.
- **The ticket is a security boundary.** It is short-lived, signed, and bound to
  the session and the Part; a leaked media URL must not be a permanent open door
  to the library, and must not carry a debrid token.
- **Transcoding's absence becomes visible, honestly.** When no candidate stream
  suits the declared profile, the Platform says so with counts and reasons
  ([ADR 0048](0048-stream-selection-against-a-client-profile.md)) rather than
  handing over a ticket that fails at the video element. That state is the
  placeholder for the deferred transcoding slice, and how often it appears is the
  evidence for building it.

## Implementation implications

`sdui`: a `Player` component in `ui.spec.json` and the `playPart` resolution in
the session contract. Platform emit-side: the source picker and Play/Resume
affordances on detail, the `Player` node on invoke, next-up resolution. `web`:
a real player primitive in `@mosaic-media/sdui-react` over `<video>` — tracks,
resume seek, throttled progress intents, next-up — replacing the toast in
`ShellProvider`. Verified the way every screen slice has been: live in a browser
against real PostgreSQL and live addons.
