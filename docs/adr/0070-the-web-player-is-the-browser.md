# 70. The web player is the browser, not a media framework

**Status:** Accepted (built)
**Date:** 2026-07-23

Supersedes the "web client is Shaka Player" bullet of
[ADR 0047](0047-player-as-client-primitive.md) and the clause of
[ADR 0048](0048-stream-selection-against-a-client-profile.md) that makes Shaka's
support probe the source of the declared capability profile. The rest of both
records stands.

## Context

[ADR 0047](0047-player-as-client-primitive.md) named Shaka Player as the web
client's renderer, and the reasoning was sound at the time: Shaka is the right
renderer for an adaptive stream, and
[ADR 0048](0048-stream-selection-against-a-client-profile.md) built on it by
making Shaka's static support probe the thing the client measures its profile
from — so a browser-version quirk would not become a server-side lookup table
nobody maintains.

Building the playback thread changed one fact underneath both records: **there
is no adaptive stream, and there is no path to one from here.** The origin
serves exactly two things
([ADR 0045](0045-playback-consumer-and-media-origin.md),
[ADR 0050](0050-probing-and-the-per-stream-playback-decision.md)):

- an upstream location relayed with range pass-through, whose container is
  whatever the source had, and
- a single fragmented-MP4 stream out of an ffmpeg pipe.

Both are progressive. HLS — the thing that would make an encoded stream seekable
and would give Shaka something only it can do — is named in ADR 0050 and is not
built.

For a progressive source, Shaka forwards to the same `<video>` element the
client would otherwise use directly. It adds no codec support: the browser
decodes either way, which ADR 0047 said itself. So adopting it now buys the
dependency and none of the property the dependency exists for.

The probe half does not survive either, but for a different reason. Shaka's
support probe is a *client* measurement, and there is currently no channel for a
client measurement to reach selection: no client declares capabilities on
`Attach`, so `ResolvePlayback` is handed a preference the session transport
hard-codes. Shaka's probe would have had nowhere to go.

## Decision

**The web client plays through a bare `<video>` element. It adopts a media
framework when the Platform serves something a `<video>` element cannot play —
which today means HLS — and not before.**

- **The `Player` node contract is unchanged.** ADR 0047's limit holds exactly as
  written: the server owns everything about a playback session except the
  decoding pipeline and the transport controls. This record changes which
  library runs the decoding pipeline, which is the half ADR 0047 assigned to the
  client in the first place.
- **The capability profile is measured from the browser itself**, through
  `canPlayType`/`MediaSource.isTypeSupported`, when the declaration channel
  ADR 0047 specifies is built. ADR 0048's requirement — that the profile is
  *measured rather than assumed* — is preserved; only its stated source changes.
  A framework's probe is a convenience over those APIs, not a capability beyond
  them.
- **The trigger for revisiting is a served format, not a release date.** When
  the origin emits HLS, the renderer is reconsidered as part of that slice,
  because that is the point at which a framework does something the element
  cannot.

## Alternatives considered

**Adopt Shaka now, as ADR 0047 decided.** *Rejected.* It would be a dependency
whose entire justification is a stream the Platform does not serve, in a client
that is the only client. The cost is not the bundle size; it is that a wrapper
adopted before it does anything becomes the thing every later playback change
has to be threaded through, and its behaviour on the progressive path — where it
is a pass-through — is untested precisely because it is doing nothing.

**Adopt it for the probe alone.** *Rejected.* The probe reads
`MediaSource.isTypeSupported` and `HTMLMediaElement.canPlayType`, which are the
browser's own APIs. Taking a framework to reach two platform calls inverts the
cost, and it would sit behind an unbuilt declaration channel meanwhile.

**Write the profile as a server-side table of what browsers support.** *Rejected,
and it is what the code does today under protest.* The session transport
hard-codes a browser preference at the `playPart` call site, which is honest for
one client and a lie for four — ADR 0048 rejected exactly this and was right to.
It stands as a stopgap, named in the roadmap, not as an answer.

## Consequences

- **One dependency not taken, and the reason is recorded rather than implied.**
  The absence of Shaka in the web client currently reads as an omission; after
  this record it reads as a decision with a stated trigger for reversal.
- **`docs/architecture.md` and the roadmap describe a `<video>` element.** The
  roadmap already does; this is the record it was describing.
- **ADR 0048's implementation note is now partly wrong**, and stays wrong on
  purpose — it lists "Web: Shaka Player, with its support probe feeding the
  declared profile" among the work. The work is still owed; the library named in
  it is not. Bodies are not annotated in this repository, which is why this
  record exists rather than an edit to that line.
- **Nothing about selection changes.** Ranking, the per-stream decision and the
  ticket are untouched: this is a statement about which client library renders
  the result, not about how the result is chosen.
- **A desktop client with libmpv remains the answer to a fat profile**, exactly
  as ADR 0047 says. That thread is unaffected — it was never going to be Shaka.

## Implementation implications

Already built: `web/packages/sdui-react/src/components/player.tsx` renders a
`<video>` with the ticket URL as `src`, applies the resume offset once the
element reports it can seek, and treats a non-seekable remuxed stream as a
no-op rather than an error.

Owed, unchanged by this record: the `Attach` capability declaration
([ADR 0047](0047-player-as-client-primitive.md)), and with it the browser
measurement that replaces the hard-coded preference; the source picker and the
no-candidate state ([ADR 0048](0048-stream-selection-against-a-client-profile.md));
HLS ([ADR 0050](0050-probing-and-the-per-stream-playback-decision.md)), which is
the point at which this record is revisited.
