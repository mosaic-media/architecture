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
is the one that puts a door on them.

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

### Permissions and users

The Platform has full ABAC authority management. None of it is reachable.

| Removed operation | Application service | What it does |
|---|---|---|
| *(never exposed)* | `CreateLocalUser` | Provision a user with a password credential — see below |
| `createRole` | `CreateRole` | Define a role and its permission set |
| `grantRole` | `GrantRole` | Grant a role to a user |
| `rolesForUser` | `GetRolesForUser` | Read a user's roles |
| `grantsForUser` | `GetGrantsForUser` | Read a user's grants |
| `effectivePermissions` | `GetEffectivePermissions` | Resolve a user's flattened authority |
| `users` / `user` | `ListUsers` / `GetUserByID` | Read the user directory |
| `setUserStatus` | `SetUserStatus` | Suspend or reactivate a user |

**Consequence, stated plainly: Mosaic is effectively single-user.**
`bootstrap.EnsureAdmin` ([ADR 0018](adr/0018-first-admin-bootstrap.md)) seeds
exactly one administrator from environment variables, idempotently, and that is
the entire user story. Roles and grants can only be established by that bootstrap
or by raw SQL. ADR 0018 anticipated this: it justifies the bootstrap as the
bridge over the fact that every command able to grant the first authority is
itself policy-gated. It was never meant to be the only path *permanently*.

This is the largest single gap in the register and the one most likely to be
misread, because "permissions management" is recorded as a landed slice in the
roadmap. It landed. It has no door.

**`CreateLocalUser` is the exemplar this whole document exists for**, and it is
worth looking at directly. `app.CreateLocalUser` provisions a user with a
password credential. It is a complete command: shape validation, caller
authentication, `user.create` policy authorisation, a `UnitOfWork`, and an
outbox event in the same transaction. It has dedicated tests for command-boundary
order, for policy denial not mutating state, and for rejecting an unauthenticated
session. It is exercised against real PostgreSQL in the integration suite.

**Its only callers are tests.** No transport has ever exposed it — not the
session transport, and not GraphQL before it. It did not appear in the deleted
schema, so it is not a casualty of
[ADR 0061](adr/0061-one-client-transport.md); it has been unreachable since the
day it was written, behind a permanently green build and a suite that asserts it
works. Nothing in the repository will ever tell you this. That is precisely the
failure mode this register is here to catch, and if it can hide a whole
command it can hide anything else on this page.

### Configuration versioning

| Removed operation | Application service | What it does |
|---|---|---|
| `draftConfigVersion` | `DraftConfigVersion` | Draft a new configuration version |
| `validateConfigVersion` | `ValidateConfigVersion` | Validate a draft and classify its reload class |
| `activateConfigVersion` | `ActivateConfigVersion` | Activate a validated version |
| `activeConfigVersion` | `GetActiveConfigVersion` | Read the active version |
| `configVersion` | `GetConfigVersion` | Read a version by id |

The reload-class machinery — every config field declares `Hot`, `Restart`,
`Generation` or `Recovery`, and only a Hot-only change activates without
escalation — is implemented and tested, and no administrator can drive it. (It
is a standing invariant in [architecture.md](architecture.md) rather than an ADR
of its own; there is no decision record for configuration versioning.)

**Partial exception:** the Supervisor handoff serves `GET :8080/config`, which
reports *which* version is active and its reload class. That is a read-only
operational probe that deliberately bypasses the policy gate; it cannot draft,
validate or activate anything. It does not discharge these rows.

### Library content: direct reads and manual editing

| Removed operation | Application service | Reachable instead? |
|---|---|---|
| `searchContent` | `SearchContent` | **Partly.** The search screen calls `SearchAvailableContent`, which unions the library with module results. Searching the library *alone* has no path. |
| `contentByExternalId` | `FindContentByExternalID` | No. |
| `moduleSettings` | `ModuleSettings` | No — reading a module's raw settings document. The *settings screen* renders `ModuleSettingsUI` and `configureModule` writes it, so a user can edit settings without being able to read the document behind them. |
| `addContentWork` | `AddContentWork` | Not from a client. |
| `addContentChild` | `AddContentChild` | Not from a client. |
| `attachContentPart` | `AttachContentPart` | Not from a client. |
| `relateContent` | `RelateContent` | Not from a client. |
| `bindContentSource` | `BindContentSource` | Not from a client. |
| `resolveContentBinding` | `ResolveContentBinding` | Not from a client. |

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

| Capability | Where it lives | Reachable? |
|---|---|---|
| Filter the library by a module's attributes | `SearchContentQuery.AttributesContain` → `NodeQuery.AttributesContain` (SDK `v0.19.0`) | No client path. |
| Streaming availability per work | `module-tmdb` writes the `tmdbWatch` attribute at import (`v0.4.0`) | Stored, queryable, never read by a screen. |

**This row is different from every other one here, and the difference is worth
stating: it was left unreachable on purpose, and the reason is correctness
rather than schedule.**

Both halves work. A TMDB import records which services carry a title in the
configured region, `SearchContent` will filter on it by containment against an
indexed document, and the contract suite proves any `StorageAdapter` must answer
that. What does not exist is anything that *refreshes* it — the jobs runner,
scheduler and system principal are all named-and-unbuilt
([ADR 0017](adr/0017-how-a-capability-acts.md), [ADR 0058](adr/0058-telemetry-storage-retention-and-expert-mode.md)).

Streaming availability churns monthly. A group that says "on Netflix" for
something that left in March is **actively wrong**, which is a worse failure
than an absent group: a user can see that a feature is missing, and cannot see
that a feature is lying. So the storage and the query landed and the surface did
not, deliberately, with the `checkedAt` timestamp written alongside every record
so the eventual refresh knows what to re-fetch first.

**What discharges this row** is a scheduled refresh, and then a browse surface
over it — in that order. Building the surface first would put a confidently
wrong answer in front of a user, which is the one outcome worth avoiding.

Adjacent and *not* blocked: a provider **catalog** — "what's on Netflix" as a
discover-backed rail — needs none of this, because it asks TMDB live rather than
reading anything stored. `module-tmdb`'s custom catalogs already do it with a
`with_watch_providers` query. That is a different feature (browse the source's
catalogue, with library items marked) and it is reachable today.

---

## Migrated

Recorded so nobody reading the deleted schema rebuilds them.

| Removed operation | Now reached by |
|---|---|
| `signIn` / `signOut` | `mosaic.auth.v1.AuthService` ([ADR 0061](adr/0061-one-client-transport.md)) |
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
| `jobs` / `job` / `jobLogs` / `retryJob` | The jobs runner. Tables exist (`jobs`, `job_attempts`, `job_logs`); no service. Wanted by four callers now — retention deletion, partition management, resolution-cache refresh, torrent eviction. |
| `componentHealth` | No cross-component diagnostics query service. |
| `refreshSession` | `sessions.Manager` has `Issue`/`Validate`/`Revoke` and no refresh. |
| `remoteSignInChallengeStatus` | No device-pairing or challenge flow exists. |

## Also owed, though never removed

These belong on this register though GraphQL never carried them, because the
honest question is "what can a user not reach", not "what did ADR 0061 delete":

- **`CreateLocalUser` never had a transport at all** — see the permissions
  section above. Listed twice deliberately: it is the register's clearest case.
- **`SignOut` has no caller.** The RPC is implemented and tested. The Shell signs
  in on boot and has no sign-out affordance, so nothing calls it.
- **There is no sign-in UI.** `devSignIn` authenticates on boot with credentials
  from build-time environment variables. A real login form is unbuilt.
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
   an affordance the caller could not exercise should not be rendered. Note the
   open problem — `mosaic.auth.v1.Session` carries no capability set, because
   nothing populates `domain.Session.Capabilities` at issue time, so gating is
   currently a server-side omission decision rather than something a client can
   make.
5. **Exercised end to end** in a running Mosaic, then struck from this register
   in the same change.

The order the rows should be discharged in is a roadmap question, not this
document's. One observation belongs here, though: **permissions and user
management gate everything multi-user about the product**, and no other row
blocks as much.

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
