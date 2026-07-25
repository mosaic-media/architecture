# 90. Lifecycle triggers, and the telemetry lane that is not needed

**Status:** Accepted (built)

**Date:** 2026-07-25

## Context

[ADR 0084](0084-vocabulary-negotiation-and-deliberate-degradation.md) deferred a
question and named where it would be answered: *a client-to-server telemetry
lane, so the client's own observations reach the server.* It was deferred
because it is a decision about what a client may report unprompted, and because
it needs the per-node identity that would make such a report attributable.

Both halves land here. The vocabulary has no way to say "this was seen", so
telemetry cannot attribute anything to what a user actually looked at — only to
what the server sent, which is a different and much larger number.

## Decision

**A node can carry `onAppear` and `onDisappear`, and they carry an `Action`.**

That is the whole design rather than an implementation detail. **The server
decides what being seen means, because the server wrote the action.** A client
fires what it was handed and reports nothing it was not asked to.

**So there is no telemetry lane, and there does not need to be one.** The invoke
lane already exists, and the server controls what travels on it. The question
ADR 0084 deferred turns out to have a shape rather than an answer: the
distinction is **prompted versus unprompted**. An impression the server asked for
rides an action the server authored. An unknown-type sighting is the client
volunteering something nobody requested, and it stays where ADR 0084 put it — the
console, with the trace id. One lane carrying both would have made the second
into the first by accident.

**"Seen" is a measurement, not a mount.** A rail of forty cards mounts forty and
shows two. Attributing an impression to a card that rendered off-screen is worse
than attributing none, because it looks like data. The threshold is **half the
node on screen** — arbitrary, like any threshold, but *stated* and identical
everywhere, so two clients measuring the same screen agree.

- **`onAppear` fires once**, not once per scroll. A user scrolling a rail back
  and forth has seen the card once; a counter that says eleven is measuring
  scrolling, not attention.
- **`onDisappear` is symmetric** — it fires on the leave that follows a real
  appearance, so a node never seen never reports leaving.
- **No `IntersectionObserver` means no report.** Firing on mount instead would
  produce impressions for things nobody saw, and a gap in the data is better than
  fiction in it.
- **The node's `id` is the analytics identity**, not a second field beside it.
  Two identities drift. The schema now states what choosing badly costs: an id
  that is a row index attributes nothing, one that names the thing attributes
  everything, and only the emit-side knows which it wrote.
- **The Platform records an impression to telemetry and stores nothing.** A
  table filled first and queried never is a retention liability, not an analytics
  capability. When there is a question worth keeping impressions to answer, that
  is when a store earns its place.

## Alternatives considered

**A dedicated `Report` RPC on `SessionService`.** *Rejected* — it is the obvious
shape and it is the wrong one. It creates a surface a client may send anything
on, which then needs rate limits, a schema, and a policy about what is
acceptable to report. Routing impressions through an action the server authored
gives the server the same information with none of that, because the server
already decided what would be sent.

**Fire on mount and let the server discount it.** *Rejected* — the server cannot
discount what it cannot distinguish. A mount and a sighting are different facts
and only the client can tell them apart.

**A configurable visibility threshold per node.** *Rejected* — it makes two
screens' numbers incomparable for a reason nobody will remember, and the
comparison is the entire value of the measurement.

**A separate `analyticsId` beside `id`.** *Rejected* — two identities for one
node drift, and the drift is invisible: the analytics id is only ever read by a
system nobody is looking at.

## Consequences

- **The question ADR 0084 deferred is closed, by not building the thing.** That
  is worth saying plainly: the answer is "no lane", not "a lane later".
- **A `display: contents` wrapper cannot be observed**, and this was found by
  the live check rather than by review. The wrapper is `display: contents` so a
  node that reports its visibility is laid out identically to one that does not —
  but an element with `display: contents` generates no box, so the observer
  reported nothing, forever, silently. What is observed is the child it wraps.
  This is precisely the failure mode the thread exists to remove, produced by the
  code meant to measure it.
- **Verified live**: a search grid mounted **29** cards, **15** were at least
  half on screen, and **15** impressions reached the Platform — one per card
  actually visible, none for the fourteen that were not.
- **Nothing in the Platform emits a lifecycle trigger.** `recordImpression`
  exists and the emit-side has the helpers; no screen carries one. The first will
  be whichever screen has a question about what people look at.
- **`onDisappear` has no consumer at all**, and dwell time — the obvious reason
  to want it — needs a clock the contract does not have. It is declared because
  its absence would be retrofitted into `onAppear` as a flag.
