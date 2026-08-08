# Unreachable capability

**A register of what the Platform can do that nobody can ask it to do.**

Every row here is a working application service — validated, authorised,
transactional, tested — with no way for a user or a client to reach it.
[ADR 0061](adr/0061-one-client-transport.md) created most of this register by
deleting the GraphQL transport; it did not create the *situation*, because a
GraphQL mutation with no UI behind it was already unreachable by anyone who was
not holding a `curl` command. What changed is that the debt is now written down
instead of being implied by a schema.

## Why this document exists

This kind of debt is unusually good at disappearing, and it disappears in a
specific way worth naming.

**The build is green and the tests pass.** Every application service listed
below has passing tests. They are tested *at the command boundary* —
shape validation, authentication, policy denial, transaction rollback, outbox
atomicity — which is the layer that matters and the layer that is hardest to
get right. None of those tests notice that no transport calls them. `go build`,
`go vet`, `go test ./...` and every CI gate stay green forever with this
register at any length.

**The roadmap says "done".** [ADR 0021](adr/0021-module-settings.md) module
settings, permissions management, config versioning — each of these landed as a
real slice, was demonstrated working, and was correctly recorded as complete.
They *are* complete as Platform capability. The slice that was never scheduled
is the one that puts a door on them. Permissions management is the worked
example, in both directions: it sat here for the whole life of the project, and
the milestone that finally put doors on it found seven defects in services that
had been passing every test throughout. Config versioning then repeated it in
miniature — three more defects, including a field of the schema's own choosing
that nothing reads.

So there is no automated signal, and the written record reads like success. The
only thing standing between "deferred" and "forgotten" is a list somebody
maintains. This is that list.

**It is not a backlog.** Nothing here is scheduled, estimated or prioritised —
the roadmap does that. This answers a narrower question: *if someone claims
Mosaic can do X, is there anything a human can press to make it do X?*

## How to read it

Each row is classified, and the classification is the point:

| Status | Meaning |
|---|---|
| **Owed** | Real, working capability with no client path. This is the debt. |
| **Migrated** | Still reachable, by a different route. Recorded so it is not re-implemented by someone reading the deleted schema. |
| **Never worked** | Was a stub that returned `Unavailable`. Removing it removed nothing; the underlying feature was always unbuilt and is tracked as unbuilt, not as removed. |

A row leaves this register **only** when a human can exercise it end to end in a
running Mosaic. Not when an RPC exists — when a screen exists and someone has
clicked it.

---

## Owed

### Reading one configuration version by id

| Removed operation | Application service | What it does |
|---|---|---|
| `configVersion` | `GetConfigVersion` | Read a version by id |

The rest of the configuration block left this register in M4 — see
[below](#discharged-in-m4-configuration-versioning). This row did not: nothing
lists the versions, so there is no id for a screen to pass. A history of what
the install was configured to do, and when, is a reasonable thing to want and
nothing needs it yet.

### The saved-search library rule

| Capability | Where it lives | Reachable? |
|---|---|---|
| A library rule that is a saved provider search | `domain.LibraryRuleQuery`, validated by `CreateLibraryRule`, evaluated by `evaluateQueryRule`, run by the maintenance pass | **No client path.** The settings surface creates collection rules only. |
| Choosing an audio track for one playback | `playEnvelope.AudioIndex`, applied by `playback.WithAudioOverride` | **No client path.** No screen offers the tracks; a client that sends the index gets it. |

**The audio-override row was created deliberately, in the same change that built
the mechanism** ([ADR 0116](adr/0116-a-preference-is-a-default-an-override-is-a-sitting.md)).
The play path honours a named audio stream and re-decides the plan around it, so
switching to a track the client cannot decode correctly becomes a transcode
rather than silence. What does not exist is a control that offers the tracks: the
source picker lists *releases*, and the panel that would list a release's streams
beside them is not built. Subtitles are not in the same position — embedded
tracks are HLS renditions and switchable in the player's own menu
([ADR 0113](adr/0113-subtitles-are-a-rendition.md)) — so the gap is audio alone,
which is why it is one row rather than two.

**This row was created deliberately in M2a rather than discovered afterwards.**
[ADR 0104](adr/0104-the-library-is-built-from-rules.md) names two kinds of rule
and both are built: the store carries the kind, the command validates it, the
evaluator runs it against one module's search role, and the maintenance pass
reconciles from it exactly as it does from a collection. What does not exist is a
way to *make* one.

The reason is a design question rather than a missing form. A rule is created
from a thing you are looking at — the collection panel offers the catalogs the
installed modules expose, so a catalog id cannot be mistyped into a rule that
silently matches nothing. A saved search has no equivalent list to pick from; its
natural home is a "save this search" control on the search screen, where the text
and the source are already in front of somebody. Building a form with a module
picker and a free-text box in settings instead would be the version that produces
rules nobody can check.

**What discharges it** is that control on the search screen, and the small
question it forces: a search fans out to every provider, and a rule is addressed
to one, so the affordance has to say which source is being saved.

### Library content: direct reads and manual editing

| Removed operation | Application service | Reachable instead? |
|---|---|---|
| `searchContent` | `SearchContent` | **Partly, and the gap moved rather than closing.** The search screen calls `SearchAvailableContent`, which unions the library with module results, and M2a's Library screen browses the library alone — through `ListLibrary`, a Platform query with paging and a real total, not through this. So *browsing* the library is reachable and this particular service still has no caller outside a module. See below. |
| `contentByExternalId` | `FindContentByExternalID` | No. |
| `moduleSettings` | `ModuleSettings` | No — reading a module's raw settings document. The *settings screen* renders `ModuleSettingsUI` and `configureModule` writes it, so a user can edit settings without being able to read the document behind them. |
| `addContentWork` | `AddContentWork` | Not from a client. |
| `addContentChild` | `AddContentChild` | Not from a client. |
| `attachContentPart` | `AttachContentPart` | Not from a client. |
| `relateContent` | `RelateContent` | Not from a client. |
| `bindContentSource` | `BindContentSource` | Not from a client. |
| `resolveContentBinding` | `ResolveContentBinding` | Not from a client. |

**`SearchContent` is a row worth reading carefully, because M2a could be
mistaken for having discharged it.** The Library screen reads the same store
with the same filters, and does *not* go through this service: browsing needs an
offset and a total, which nothing sourcing content has ever asked for, so those
went on `NodeQuery`/`NodeStore` and on a new Platform query rather than growing
the SDK surface every installed extension holds. `SearchContent` remains the
published "do I already have this?" read, exercised on every module import and
by no client.

**M2b answered the open question here, and the answer was the other one.**
Faceting was named as the thing that would eventually *need* a client-side
library-only search with the attribute filter. When it was built, the filters
went on `ListLibrary` — genre, then streaming service — rather than on
`SearchContent`, for the reason M2a already gave: a browse needs an offset and a
total, and growing the SDK surface every installed extension holds to serve a
Platform screen is the wrong direction. So `SearchContent` is not debt awaiting
its caller; it is a module-facing read a Platform browse was never going to be
built on. It stays on this register because a *user* still cannot search the
library alone.

**The six content commands need care, and are the most likely row to be
misjudged in either direction.**

They are *not* dead code. They are the published SDK surface
([ADR 0016](adr/0016-published-contract-surface.md)) that every module writes
through — the Stremio module builds an entire content tree with them on every
import, exercised end to end against real PostgreSQL. They are among the
best-tested code in the repository.

What is missing is a *human* path. A user cannot correct a wrong title, attach a
local file to an episode, relate an adaptation to its source, or fix a bad
source binding. Everything in the library arrives through a module and can only
be changed by a module. That is a real product gap — it is roughly "no manual
library editing" — but it is **not** the same gap as the permissions one, and
restoring an RPC would not fix it. What fixes it is an editing surface, which is
a design question before it is a transport question.
### Grouping the library by streaming service

**The refresh is built. The surface was built, put in front of somebody, and
taken back out** — and that is the most useful thing this row has ever recorded.

| Capability | Where it lives | Reachable? |
|---|---|---|
| Filter the library by streaming service | `NodeQuery.WatchProviders` → `node_watch_availability` (M2b) | **No client path**, and now deliberately so. |
| Keeping that answer true | `library.availability`, daily, never-asked first then oldest | Built and running; nothing reads what it maintains. |
| Streaming availability per work, as a module records it | `module-tmdb`'s `tmdbWatch` attribute (`v0.4.0`) | Still stored, still read by nothing. The Platform's own projection replaced it as the thing a screen would query. |

**Why this row stayed open so long is worth keeping**, because it is the only
entry here that was left unreachable on purpose and the reason was correctness
rather than schedule. Both halves worked for a long time: a TMDB import recorded
which services carry a title in the configured region, and the store filtered on
it. What did not exist was anything that *refreshed* it — and availability churns
monthly, so a group saying "on Netflix" for something that left in March is
**actively wrong**, which is a worse failure than an absent group: a user can see
that a feature is missing, and cannot see that a feature is lying.

**M2b built the refresh, and it departed from what this row predicted.**
Refreshing the module's own attribute would need the Platform writing into a
document [ADR 0013](adr/0013-object-graph.md) says it never interprets, or a
refresh verb on the SDK and a release of every module. What landed reads
`ContentMetadata.Watch` — a typed contract field
[ADR 0107](adr/0107-the-platform-keeps-what-a-source-told-it.md)'s pass already
fetches — and projects it into the Platform's own indexed store. The facet is
therefore not TMDB's: any metadata provider that fills `Watch` populates it.

**Then the surface went on the Library screen and was wrong on sight.**
Availability answers *"what could I watch on this service"*, and that question
spans what the library holds **and what it does not**. Answering it over the
shelf alone hands a user the small half while looking like the whole — a subtler
version of the same failure this row was already about. It was removed. Genre
stays on that screen, because a genre *is* a property of what you own, so
narrowing the shelf by one has a complete answer.

The cross-source affordance exists and needs none of this: a source's catalogue
browsed with library items marked, where `module-tmdb` now declares a
`with_watch_providers` filter on its discover-backed catalogs from the configured
region's own provider list. It asks TMDB live, exactly as this row's closing note
always said it would.

**So what discharges this row is narrower than it was.** Not a facet over the
library, but a **union**: an "on Netflix" surface showing the source's catalogue
and the titles you already own on that service together. The stored projection is
what answers the second half without a provider round trip per title, which is
the one thing a live query cannot do. Until something builds it, this is a
maintained capability with no reader — and whether it should be carried at all,
rather than deleted and rebuilt when that surface is scheduled, is an open
question this register should not pretend to settle.

### The subtitles provider role

| Capability | Where it lives | Reachable? |
|---|---|---|
| Subtitle tracks resolved for an item | `v1.SubtitlesProvider`, filled by `module-stremio-addons` and `module-aiostreams`, resolvable through `CapabilityRegistry.SubtitlesProvider` | **No.** No application service calls it, so there is nothing for a client to reach. |

**This row was added when the role stopped being incomplete, not when it stopped
being reachable** — it was never reachable. The role landed under
[ADR 0037](adr/0037-completing-the-stremio-source-surface.md) ahead of the player
that would consume it, which was the deliberate and correct order; what it did
not have until SDK `v0.26.0` was the ability to name an episode.
`SubtitlesRequest` carried no season or episode, so a provider asked about
content it did not source — the only way `module-aiostreams` is ever asked
anything — could answer for a film and for nothing else. Both modules composed
their addressing from two literal zeroes and said so in a comment.

That half is now closed and the role is complete: filled by two modules,
correctly addressable, verified across a real process boundary. **And nothing
calls it.** The registry can resolve a subtitles provider and no caller asks it
to; the enrichment pass that reaches stream providers for foreign content
(`internal/platform/app/enrich_streams.go`) resolves streams only.

**What discharges it** is the player — M3's track-selection work, which is where
a subtitle track is first something a person can choose. Until then this is the
register's purest example of its own thesis: a capability made *more* correct in
a change that brought it no closer to anyone being able to use it, with every
gate green throughout.

### The segmented playback origin

| Capability | Where it lives | Reachable? |
|---|---|---|
| A transcoded release served as seekable HLS | `internal/transport/playback` serving `index.m3u8`, `init.mp4` and numbered segments; `@mosaic-media/sdui-react` `0.22.0` reading them | **Written on both sides, and never played.** Every part exists and nothing has been watched through it. |

**The reason this row exists changed, and it did not discharge.** It was added
because the origin served HLS and the Shell could not read it —
[ADR 0070](adr/0070-the-web-player-is-the-browser.md)'s condition met and its
consequence unpaid. The consequence is now paid: the `Player` primitive reads a
playlist natively on Safari and through hls.js elsewhere.

What remains is the thing this register was written to keep visible. **A
capability nobody has exercised is not reachable, however complete it looks.**
Slice 4 has now produced four designs; three of them passed every unit test they
had and failed the moment a real decoder assembled the responses, and the fourth
has the same green suite the other three did.

The relayed path is unaffected — a release needing no work is still the
upstream's own bytes, still byte-range seekable, and still what most plays
should be once selection ranks on codec and dynamic range. So the practical
reach of this row shrinks as the selection train lands, which is an argument
for that order rather than a reason to leave this outstanding.

**What discharges it** is one viewer watching one release that needed ffmpeg —
opened, seeked, resumed, against a running instance. Nothing else. The rule at
the foot of this document already says a passing test is never evidence a row is
discharged; this row is the clearest case of it the register has held.

## Discharged in M1 — permissions and users

The whole permissions-and-users block left this register on 2026-07-27, and it
is recorded rather than deleted because it was the largest gap here and the one
most likely to be re-read as still open.

| Application service | Where a human reaches it |
|---|---|
| `CreateLocalUser` | Settings › People › Add a viewer / Add an administrator |
| `CreateRole` / `GrantRole` | The same form, and "Grant User"/"Grant Administrator" on a person's panel |
| `GetRolesForUser` / `GetEffectivePermissions` | A person's panel: the roles they hold and the flattened set the policy engine decides with |
| `ListUsers` / `GetUserByID` | Settings › People, and each row's Manage |
| `SetUserStatus` | Suspend / Reactivate on a person's panel |
| `GrantablePermissions` | What the create form says it will grant, computed from the grantor's own authority (ADR 0069) |

`CreateLocalUser` was this document's stated exemplar — "unreachable since the
day it was written, behind a permanently green build and a suite that asserts it
works". Four accounts now exist on a box that was claimed through a browser, and
three of them were made through that form.

**`GetGrantsForUser` is the one row of the block that is not discharged.** A
person's panel shows their roles and their effective permissions, which is what
answers "what may they do"; the grant rows themselves — the join between a user
and a role — surface nowhere, and nothing yet needs them to. It stays owed.

**What discharging it cost is worth reading**, because it is the argument for
this register existing. Every service above was complete, tested and
transactional, and putting doors on them found seven defects that no gate could
have: an ordinary account could not sign in, could not sign itself out, and
could not read its own name; settings would not open for one at all; "Add to
library" was drawn for people who cannot import; creating four accounts produced
three with no authority; and a claimed server never reconciled its owner's role.
Each one is a service that worked perfectly and a product that did not.

---

## Discharged in M4 — configuration versioning

The reload-class machinery left this register on 2026-08-08. It is recorded
rather than deleted for the reason the M1 block is: it sat here from the day it
was written, and a deleted entry reads as a capability nobody ever missed.

| Application service | Where a human reaches it |
|---|---|
| `DraftConfigVersion` | Settings › Configuration › Apply |
| `ValidateConfigVersion` | The same control — a rejected value comes back on the field that carried it |
| `ActivateConfigVersion` | The same control — the toast says whether it applied or is waiting |
| `GetActiveConfigVersion` | The panel's rows: what each setting is worth right now |

`GetConfigVersion` is the one row of the block that is not discharged, and it
stays [owed above](#reading-one-configuration-version-by-id).

**One control, not three.** Draft, validate and activate are the machinery of
the model rather than a workflow a person performs: somebody changing how often
the library pass runs is not drafting a version. Three controls would make an
operator drive an implementation in order, and leave a half-finished draft
behind every time they changed their mind.

**Putting a door on it found four things no gate could have**, which is the
argument for this register in the miniature. The fourth needed more than a
door — it needed somebody looking at the screen: the pending banner listed the
payload's keys, and a pending version is a whole configuration rather than a
patch, so changing one setting announced a change waiting to set two others to
the values they already had. The other three:

- **`runtime.log_level` is read by nothing.** The schema's own comment calls it
  "the canonical hot-reload example", and it is the first field anybody would
  put on a configuration screen. A control for it would have saved a value,
  reported that it applied, and changed nothing. `runtime.environment` is in the
  same position. Both are excluded, and a test now asserts every offered field
  against the readers' own constants.
- **A number submitted as text validates and is then ignored.** Every reader
  type-asserts a JSON number; validation checks only that a field is
  *registered*, never what type it holds. So `"30"` would have drafted,
  validated, activated and reported "Applied." while the reader kept using the
  default. The transport parses at the boundary.
- **The stored payload is not what is in force.** Each reader applies its own
  default for an unset field, falls back again for an unusable one, and the
  audit floor ([ADR 0057](adr/0057-audit-is-a-store-not-a-log-stream.md)) is applied after
  both — so a panel formatting the payload would have shown "not set" on a
  fresh install while the Platform kept logs for a fortnight. The panel asks the
  readers, which are the definition of what applies.

The earlier **partial exception** stands and is unchanged: the Supervisor
handoff's `GET :8080/config` reports which version is active and its reload
class, as a read-only operational probe that deliberately bypasses the policy
gate. It never discharged anything; the screen did.

---

## Migrated

Recorded so nobody reading the deleted schema rebuilds them.

| Removed operation | Now reached by |
|---|---|
| `signIn` / `signOut` | `mosaic.auth.v1.AuthService` ([ADR 0061](adr/0061-one-client-transport.md)), and since M1 the doorway's own form and the account cluster's Sign out |
| `screen(name, params)` | The session push lane — the Platform renders and pushes region updates ([ADR 0041](adr/0041-cross-client-transport-two-lane-rpc.md)) |
| `importContent` | The `importContent` action, via session `Invoke` |
| `configureModule` | The `configureModule` action, via session `Invoke` |
| `contentNode` | The detail screen (`GetContentNode`) |
| `searchAvailableContent` | The search screen |
| `moduleCatalogs` / `catalogItems` | The collections and catalog screens |
| `moduleSettingsUI` | The settings screen ([ADR 0038](adr/0038-module-contributed-settings-ui.md)) — for *every* module that fills the role since [ADR 0076](adr/0076-a-curated-stream-provider-beside-the-addon-host.md) added the index. Until then the host named one module by constant, so `module-tmdb`'s credential form was reachable only by hand-crafting a `moduleId` param: the operation was reachable, one of its answers was not. |

## Never worked

These returned a flagged `Unavailable` rather than inventing behaviour. They are
tracked as **unbuilt features**, not as removed surfaces — deleting them cost
nothing, and building the feature is what the roadmap should say.

| Removed operation | Underlying gap |
|---|---|
| ~~`jobs` / `job` / `jobLogs`~~ | **Discharged.** The runner landed with M0.1, and a Jobs screen behind `job.read` shows the queue, each job's attempt history and the lines it recorded — reachable by a human in expert mode. `retryJob` is *not* discharged: a dead-lettered job is visible and there is no way to ask for another attempt, which is the row that remains. |
| `componentHealth` | No cross-component diagnostics query service. |
| ~~`refreshSession`~~ | **Discharged.** `AuthService.Refresh` exchanges a refresh token for a new pair (M0.3, [ADR 0102](adr/0102-the-session-credential-is-a-bearer-pair.md)), and the Shell calls it — ahead of an expiry, and once after an `Unauthenticated`. |
| `remoteSignInChallengeStatus` | No device-pairing or challenge flow exists. |

## Also owed, though never removed

These belong on this register though GraphQL never carried them, because the
honest question is "what can a user not reach", not "what did ADR 0061 delete":

- **`SetContentArtwork` has no client path, and the artwork picker it exists for
  does not exist.** The command is implemented, validated, authorised and
  transactional; the artwork enrichment pass calls it
  ([ADR 0075](adr/0075-the-artwork-provider-role.md)), so it is exercised
  server-side and its tests pass. What nobody can press is the half it was
  *designed* for: [ADR 0074](adr/0074-artwork-is-a-candidate-set.md) stores every
  poster, logo and backdrop a source offered as candidates specifically so a user
  can choose among them, and there is no screen that renders the alternatives.
  Selection resolves by a stated rule and a user cannot override it.

    This is the register's own failure mode in miniature: the rule produces
    visibly better art than before, so the feature *looks* delivered, and the
    reason artwork was moved onto the node at all
    ([ADR 0071](adr/0071-content-artwork-is-stored-on-the-node.md) — "user-swappable
    artwork becomes possible") is the part still owed. It also has a second-order
    debt: `SetContentArtwork` replaces rather than merges, so once a picker
    exists, a user's choice needs marking as theirs or the next enrichment pass
    will overwrite it.

    **M2b removed the last thing that could be mistaken for the blocker.**
    `module-fanart-tv`'s project credential had never been linked into any build,
    so an obvious reading was that artwork enrichment was simply unconfigured.
    It is now linked and guarded — and it changes nothing a user can see, which
    is the point. A real library of 152 works already carries a logo on 130 of
    them, a backdrop on 151 and a poster on 152, all from TMDB. What fanart adds
    is *alternatives*: forty variants where TMDB returns one. Those are exactly
    what [ADR 0074](adr/0074-artwork-is-a-candidate-set.md) stores and what this
    row says nobody can choose between. **The credential was a prerequisite, not
    the gap.**

- **`recordImpression` has nothing that can cause one.** The action is
  implemented, authorised against the session it arrived on, and it writes a
  telemetry record naming the node that was seen
  ([ADR 0090](adr/0090-lifecycle-triggers-and-the-absent-telemetry-lane.md)).
  Reaching it requires a screen carrying an `onAppear` trigger, and no screen
  carries one — the emit-side has the helpers and uses none of them. So the
  Platform can record what a user actually looked at, and nothing in Mosaic can
  make it do so.

    It belongs here rather than in the roadmap's unbuilt column because the
    distinction this register draws is exactly this one: the capability is
    *finished*. It was demonstrated end to end against a running stack — a
    search grid mounted 29 cards, 15 were at least half on screen, and 15
    impressions arrived — with an emit that was reverted afterwards because it
    was a probe. A capability proven to work and then left with no caller is the
    most convincing kind of "done" there is, and the least true.

    The rest of that vocabulary's trailing edge shares the shape without being
    rows here, because they are contract surfaces rather than Platform services:
    nothing emits an `onDisappear`, an accessibility prop or a focus prop
    either. The roadmap's fifth thread names them.

---

## How a row is discharged

[ADR 0061](adr/0061-one-client-transport.md) chose deletion over re-porting on
the grounds that these surfaces return *as screens*, not as a second set of
RPCs. Concretely, discharging a row means:

1. **A screen builder** in `internal/transport/screens`, reading the application
   query service and emitting a `UINode` tree ([ADR 0029](adr/0029-sdui-emit-side.md)).
2. **A `dispatch` case** in `internal/transport/session` for each write, decoding
   the action envelope into the command. The dispatch switch is the complete
   enumeration of what a client can invoke — if it is not there, it does not
   exist.
3. **A route** the shell screen can navigate to, so the screen is reachable by
   pressing something rather than only by an intent a developer sends by hand.
4. **Capability gating** ([ADR 0036](adr/0036-capability-gated-affordances.md)):
   an affordance the caller could not exercise should not be rendered. The open
   problem this step used to name is closed — `domain.Session.Capabilities` is
   populated at issue time and re-resolved on every refresh, and
   `mosaic.auth.v1.Session` carries it — so a client that composes its own
   chrome can make the same omission the emit-side makes. It remains a
   *drawing* decision and never a check: every call re-authorises against the
   grants as they are then.
5. **Exercised end to end** in a running Mosaic, then struck from this register
   in the same change.

The order the rows should be discharged in is a roadmap question, not this
document's.

## Rules

- **Adding a row is part of removing a surface.** A change that deletes a client
  path adds its row here, in the same commit, or the deletion is not complete.
- **Striking a row requires a demonstration, not a merge.** "The RPC exists" is
  not discharge. Someone clicked it in a running Mosaic.
- **Never cite a passing test as evidence a row is discharged.** The tests pass
  now, with every row outstanding. That is the whole reason this file exists.
- **If a slice is recorded as "done" in the roadmap and appears here, both are
  true.** The capability is done; the door is not. Say so in both places rather
  than downgrading the slice.
