# Extension installation is user-initiated and persistent

**Status:** Proposed
**Date:** 2026-07-24

Refines [ADR 0079](0079-the-platform-manages-extension-modules.md), which made
the Platform the actor for the whole extension lifecycle but left *how* an
extension comes to be installed unspecified. Builds on
[ADR 0065](0065-module-distribution-and-trust.md) (the signed repository and the
verification mechanism), [ADR 0061](0061-one-client-transport.md) (the client
surface and its `Invoke` lane), and is deliberately kept distinct from
[ADR 0021](0021-module-settings.md) (per-module user settings). Nothing here is
built beyond the install-and-verify path ADR 0079 already produced.

## Context

The producer side of the extension ecosystem is now real and live: a module
publishes signed cross-compiled binaries and a manifest, the official registry
aggregates and signs an index of them, and the Platform trusts that index's key
and can download, verify and spawn a binary from it. What ADR 0079 did *not*
decide is the shape of the act in the middle — how an extension goes from
*available in the repository* to *running in this Platform*, and what happens to
that choice when the Platform restarts.

Three shapes were on the table, and they are genuinely different products:

- An **operator-named set**, extending the `MOSAIC_MODULES` environment bridge
  ([ADR 0063](0063-platform-binary-built-by-ci.md)) to extensions: the operator
  lists the extensions to run, and the Platform installs them at boot.
- An **install-at-boot default**: the Platform installs some baseline set from
  the repository every time it starts.
- A **user-initiated, persistent install**: a person browsing a settings surface
  chooses to install an extension; the Platform adopts it and keeps adopting it
  across restarts until the same person uninstalls it.

The first two make the *operator* or the *build* choose extensions, and re-couple
that choice to process configuration and restarts — which is exactly right for
*core* modules (a Generation-class decision, ADR 0063) and exactly wrong for an
open ecosystem a user curates at runtime. The third is the product: extensions
are the dynamic, user-facing half of the tier split, and choosing them is a
user's runtime act, not an operator's config or a build's manifest.

## Decision

**An extension is installed by a user, from a Platform surface, and the
installation is durable Platform-owned state the Platform re-adopts across
restarts until the user uninstalls it. Nothing is installed by default.**

### Not installed by default

A fresh Platform composes its **core** modules and nothing else. The
installed-extension set starts empty. This is what keeps a default install
honest: the guaranteed metadata floor is a core module (Cinemeta,
[ADR 0072](0072-the-guaranteed-metadata-provider-needs-no-credential.md)), so a
Platform with no extensions is fully functional rather than inert, and every
extension present is one someone chose.

### Installed by a user, from a settings surface

Discovery and install are a **Platform client surface** — the admin surface
ADR 0079 named and did not shape. It lists what the trusted repository offers
(the signed index), shows what is installed, and installs or uninstalls on the
user's action. It is served like every other surface (SDUI, ADR 0061); install
and uninstall are `Invoke`-lane actions, the same shape `configureModule`
already has. Adding or consenting to a *third-party* repository is a further
action on the same surface (ADR 0065's trust decision), still open in its
detail.

### The installed set is durable, and the Platform re-adopts it at boot

The set of installed extensions is **Platform-owned durable state**, not
environment and not build config. Its durable truth is *which extensions, from
which repository, at which version, verified against whose key* — the identity
and provenance. The verified binary on disk is a cache of that record,
re-acquirable from the recorded repository and version if it is missing.

At boot the Platform reads the set and **re-adopts each entry** from the on-disk
cache: it re-verifies the cached binary against the manifest that was
authenticated at install — the digest re-checked in the process that grants
authority, immediately before every spawn (ADR 0079) — and spawns and registers
it. This confirms the exact **pinned** bytes without re-fetching an index that
may by then list a newer version, so a registry that has moved on does not
silently upgrade an install. The signature-and-key check runs at install (and at
any reinstall or update), which is the act that grants authority; boot re-adoption
re-confirms the bytes that act vouched for. Only when the cache is gone does boot
re-install from the repository, re-verifying against the trusted key. A restart
therefore reconstructs exactly the running set the user last chose, with no
operator action and no re-consent.

### Adoption is dynamic, because the trigger is a live user action

Install and uninstall take effect **while the Platform is serving**, not only at
the next boot: installing spawns and registers the capability then; uninstalling
stops the process, unregisters the capability, and lets its in-flight invocation
handles die with it (ADR 0017, ADR 0064). This is the sharp contrast with
*core-module selection*, which is Generation-class precisely because changing the
binary's contents is not a runtime act. Extensions are runtime by construction,
so their adoption is too.

### Installation is not settings

Whether the Platform *has* a module and how a module the Platform has is
*configured* are different questions. Installation is the first; module settings
(ADR 0021) are the second. Both are user-managed and durable, but conflating them
would let a module that was never installed carry a settings document, or make
uninstalling lose configuration that should outlive a reinstall. An installed
extension is configured through the settings mechanism that already exists; the
install record and the settings document are separate state.

## Alternatives considered

**Extend `MOSAIC_MODULES` to name extensions (the operator-named set).**
*Rejected* for extensions, kept for core. It makes the operator choose from an
ecosystem meant for the user, and ties a runtime choice to process config and a
restart. `MOSAIC_MODULES` remains the right bridge for *core* selection, which
genuinely is an operator, Generation-class decision.

**Install a baseline set from the repository at every boot.** *Rejected.* It
makes every deployment reach the repository at startup and runs modules nobody
chose; "nothing by default, everything by choice" is the product, and it is also
the safer default — a Platform that phones a host at boot is a dependency and an
attack surface a default-off Platform does not have.

**Model installation as module settings (ADR 0021).** *Rejected.* Settings
presuppose the module exists; installation is the prior question. A single store
answering both would have to represent "configured but not installed" and
"installed but never configured" as states of one document, which is two
concerns wearing one row.

**Hold the installed set in the Supervisor.** *Rejected*, and already rejected in
substance by ADR 0079: the installed set is a dynamic, third-party,
failure-prone concern, which is the whole class of thing the durable host layer
must not depend on. It is Platform state.

## Consequences

- **The Platform gains a durable installed-extensions store**, a new
  Platform-owned store (on `Tx`, ADR 0012's shape), read at boot and mutated by
  install and uninstall. It records identity, source repository, pinned version
  and verifying-key provenance; the binary is a cache keyed on that record.
- **The capability registry must support add and remove while serving.** Today it
  is built once at composition and only read during serving; dynamic install and
  uninstall make it a concurrent structure. This is the main new engineering risk
  and is its own slice.
- **The static `require` on `module-stremio-addons` is dropped.** Stremio becomes
  an available-not-installed extension: a fresh Platform does not have it until a
  user installs it, and `RequireComposedRoleClasses` still passes because Stremio
  fills no required class and the core metadata floor is unchanged.
- **The binary and its authenticated manifest are cached on disk beside each
  other.** The store's row is the durable record of intent; the cache is the
  bytes. Boot re-adoption re-hashes the cached binary against the cached
  manifest's digest — cheap, offline, and preserving the pin — and reaches the
  repository only to install, reinstall, or replace a missing cache. That is the
  posture ADR 0079 chose: verify in the process that grants authority, every time
  it spawns, over trusting an earlier check.
- **Uninstall must revoke cleanly**: stop the process, unregister the capability
  so nothing resolves it, and drop the install record. In-flight invocation
  handles die with the process, which is the existing guarantee.
- **Open, and named rather than invented:** what *updating* an installed
  extension to a newer catalogued version looks like (a user action, an
  auto-update policy, or neither), and how a **revoked** key or yanked version
  reaches an already-installed extension. Both are the discovery/revocation
  questions ADR 0065 left open, now clearly the Platform's and clearly attached
  to this durable set.
