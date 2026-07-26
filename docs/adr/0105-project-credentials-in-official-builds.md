# 105. Official builds carry project credentials, and a personal key replaces one

**Status:** Accepted. **Built for `module-tmdb`** — `platform`'s release
workflow links `defaultReadAccessToken`, and `linkercheck_test.go` fails if the
`-X` symbol path stops resolving. **Declared and not built for
`module-fanart-tv`**: the symbol and its whole policy exist in a doc comment,
that comment names `./cmd/mosaic-platform` as the build path, and
[ADR 0081](0081-extension-installation-is-user-initiated-and-persistent.md) took
that module out of the binary — no workflow injects the key, no guard test
catches it, so every released binary ships an empty one and the module answers
"fanart.tv API key not set". **Partly supersedes
[ADR 0072](0072-the-guaranteed-metadata-provider-needs-no-credential.md): the
Mosaic-held-key alternative it rejected is reversed here. The rest of ADR 0072
stands, and `module-cinemeta` remains the zero-configuration floor.**
**Date:** 2026-07-26

## Context

[ADR 0072](0072-the-guaranteed-metadata-provider-needs-no-credential.md) rejected
shipping a Mosaic-held key on four grounds: a key in a public binary is not a
secret; one key means one rate limit shared by every install; it makes Mosaic a
party to a third party's terms on behalf of its users; and it is a cost and
distribution commitment. All four are still true.

Two things changed since.

**The product's requirement moved from identification to presentation.** ADR 0072
answered *can a fresh install identify content*, and `module-cinemeta` answers it
with no credential at all. The first release asks whether a fresh install can
*present* content — similar and related titles, collections, certifications,
watch providers, crew, per-episode runtimes, genre data rich enough to browse by,
and artwork better than the metadata source happened to carry. Every one of those
comes from a credentialed provider, and none of them is optional in the release.

**And the question recurs per module.** TMDB needs a read access token; fanart.tv
needs a project key; a ratings or subtitles provider will need one next. Deciding
it module by module is what has already happened, and the result is the
asymmetry this record was written to fix: one module has the mechanism, a guard
test and a three-state settings screen, and another has the same policy written
carefully in a Go comment and nothing that implements it.

**The tier split moved where injection can even happen**, and that is the part
that got missed. A core module is linked into `cmd/mosaic-platform`, so
`platform`'s release workflow is the only place a `-X` can reach it. An
**extension** module is cross-compiled by its own repository and distributed
through the signed registry ([ADR 0065](0065-module-distribution-and-trust.md),
[ADR 0081](0081-extension-installation-is-user-initiated-and-persistent.md)), so
its `-X` belongs in *its* `release.yml`. `module-fanart-tv`'s comment still names
the core path it was moved off, which is exactly how a credential can be
thoroughly documented and never linked.

## Decision

**An official Mosaic build may carry a project credential for a module, so that
module works out of the box. A user's own key always replaces it. Six rules
govern every such credential, and they are the same rules for every module.**

**1 — What may be a project credential.** Read-only; scoped to a public
catalogue; revocable centrally by the issuer; and under terms Mosaic can hold on
its users' behalf. A credential that writes, that carries or identifies per-user
data, or whose terms forbid redistribution is **not** eligible, and convenience
is not an argument against that.

**2 — It is injected by the workflow that builds the artefact that ships it.**
A core module's key is linked by `platform`'s release workflow; an extension
module's key is linked by that module's own `release.yml` `binaries` job, so it
travels inside the artefact the registry catalogues and signs. Never committed,
never in an image's environment, never in a configuration file, never written
into the module's settings document.

**3 — A guard test is mandatory.** `-X` against a symbol that no longer resolves
is **ignored silently**, so a rename, a package move or a tier change turns a
credentialed build into an uncredentialed one with nothing going red anywhere.
Every module carrying a project credential ships a linker check that fails when
the symbol path breaks. `module-tmdb`'s is the pattern; its absence in
`module-fanart-tv` is why that module's key has never once been linked.

**4 — Exactly one function reads it.** That is what makes "never logged, never
rendered, never returned by an API, never sent over the module wire" verifiable
by reading the code rather than by trusting a claim.

**5 — Obscurity is not security, and nothing here pretends otherwise.** A string
linked into a distributed binary is recoverable with `strings`. What is claimed:
it is absent from source control, from every log, from every API response, from
every screen, from the module wire and from the settings document. What is **not**
claimed: secrecy from anybody holding the binary. It is a *shared* credential
whose exposure is accepted, not a hidden one.

**6 — A personal key always wins, and the screen says which is in use.** Three
states, because the middle one is real: no key at all (explain how to get one),
the project key in use (say so, name the benefit of adding your own, and show
nothing of the project key — it is not this user's credential and there is
nothing for them to copy, verify or fix), and a personal key in use (masked,
clearable, with clearing stated to fall back rather than to break).

**The floor does not move.** A module holding a project credential is still not a
guarantee-clause provider. `module-cinemeta` stays core and stays the
zero-configuration floor, because a shared credential can be revoked or throttled
and a guarantee resting on one is not a guarantee. This record narrows what
ADR 0072's guarantee is claimed to deliver: **installability, not richness.**

## Alternatives considered

**Collect a key during onboarding.** *Rejected.* It puts a third-party sign-up in
the middle of a first run, and every screen the release cares about is degraded
until somebody finishes it. It was ADR 0072's other rejected option, for the same
reason.

**Ship no project credentials and accept Cinemeta-grade richness by default.**
*Rejected.* It makes similar-and-related, genre browsing, certifications and
artwork enrichment unavailable on a default install, and those are release
requirements rather than refinements.

**Decide it per module, as has happened so far.** *Rejected*, and this record is
the correction. Two modules reached two different answers — one implemented, one
documented — and neither of them was wrong on its own terms. The policy is the
same every time, so it belongs somewhere a third module inherits it.

**Encrypt or obfuscate the key inside the binary.** *Rejected.* The decryption
routine ships in the same binary as the ciphertext, so it deters casual
extraction and nothing else — while implying a security property that does not
exist, which is worse than the honest statement in rule 5.

**A Mosaic-operated proxy holding the keys server-side.** *Rejected for now, and
named as the escalation.* It is the only option that keeps a credential genuinely
secret and its quota governable, and it makes every self-hosted install depend on
infrastructure Mosaic runs — the dependency a self-hosted product exists to
avoid. If quota abuse becomes real, this replaces the linked credential, and it
is a new record when it does.

## Consequences

- A fresh install is fully featured, which is what the release requires, and
  onboarding has no credential step it cannot skip.
- **Shared quota is shared fate.** Abuse or growth degrades every default install
  at once, so an issuer throttling a project credential must be visible in
  telemetry, attributed to that credential, *before* it is felt on a home screen.
- **Rotation costs differ by tier, and the extension case is worse than it
  looks.** Rotating a core module's key is a Platform release. Rotating an
  extension module's key is a module release, a registry catalogue bump and a
  republish — and an install **pins the version it installed** and re-adopts it
  from disk across restarts
  ([ADR 0081](0081-extension-installation-is-user-initiated-and-persistent.md)),
  so a rotated key does not reach it until that user updates the extension. A
  revoked extension credential is therefore a degraded capability on every
  install until each one acts. Opt-in automatic extension updates would close
  that, and they are deferred past the first release along with the update policy
  they need.
- The fallback chain — personal key, then project key, then the zero-configuration
  floor — must be exercised rather than assumed, so a build with an empty
  credential stays a configuration the gate covers.
- `module-fanart-tv` has an outstanding defect rather than a hypothesis: the key
  its code documents has never been linked into anything, which is a live reason
  artwork enrichment has never been seen on a screen.
