# 22. Licensing

**Status:** Accepted
**Date:** 2026-07-20

## Context

Mosaic is an open-source project with a public extension model: a published SDK third parties build modules against ([ADR 0008](0008-sdk-as-public-contract-language.md)), and modules statically compiled into the Platform binary ([ADR 0007](0007-static-go-module-composition.md)). Making the repositories public required choosing licenses.

The pivotal fact is **static composition**. Because a module is compiled *into* the Platform binary rather than run as a separate process, the Platform's license would otherwise reach every module linked into it — a copyleft Platform would force modules to be copyleft too. That would contradict the central thesis, which is that anyone can write a module, under any license, against the SDK.

So the license choice is not one decision but a shape: the SDK almost has to be permissive regardless, and the Platform's choice is where any protective intent lives.

## Decision

**Protected core, permissive SDK.**

- **Platform** — **AGPL-3.0 with a Module Linking Exception** (an additional permission under AGPL section 7, in `LICENSE-EXCEPTION`). The AGPL protects the Platform from being repackaged as a closed hosted service without contributing back — its section 13 network-use clause closes the SaaS loophole. The exception frees any **Module** — an independent work that interacts with the Platform solely through the SDK, including one compiled into a Platform binary — to be released under any license its author chooses. **The exception frees the Module, not the Platform:** modifications to the Platform, and serving it over a network, remain governed by the AGPL.
- **SDK** — **Apache-2.0**. It is the contract modules build against, so it must be permissive or a module author would be forced into copyleft by depending on it. Apache over MIT for the explicit patent grant, appropriate for a contract surface.
- **Optional modules** — their authors' choice. The first, [`mosaic-module-stremio`](https://github.com/mosaic-media/mosaic-module-stremio), is **MIT** (matching the Stremio addon SDK it interoperates with).
- **First-party clients** — **AGPL-3.0-only**, no linking exception. A client (the web [`mosaic-shell`](https://github.com/mosaic-media/mosaic-shell); a future Flutter client for TV, desktop and mobile) is part of the protected first-party product, so it matches the Platform's copyleft — as Jellyfin, Nextcloud and Immich license their own official clients. It carries **no** Module Linking Exception: that permission exists to free a work *compiled into* the Platform binary, and a client links nothing in — it is a separate program talking to the Platform over the network. The **SDUI contract** a client renders (the technology-agnostic node vocabulary + action envelope that also drives the Flutter client) is, like the SDK, permissive when extracted — so a *third-party* client, in any language, may be any license. First-party polish stays copyleft; the contract stays open.
- **This documentation** — **CC-BY-4.0**.

## Alternatives considered

**Permissive everywhere (Apache-2.0 / MIT for the Platform too).** *Rejected:* it allows a proprietary, closed hosted fork of the Platform. The project wants to prevent that while keeping the module ecosystem fully open — which is exactly what AGPL-plus-exception expresses.

**Source-available for the Platform (BSL, SSPL).** *Rejected:* appropriate only if the intent were to commercialize the Platform itself (sell it, or a hosted version, and stop others self-hosting free). The project is community open-source with no such plan; AGPL, not a source-available license, fits.

**Copyleft SDK.** *Rejected:* it would drag every compiled-in module into copyleft through the dependency, defeating [ADR 0008](0008-sdk-as-public-contract-language.md)'s open-ecosystem purpose.

## Consequences

The module ecosystem stays open — a module can be any license — while the Platform core cannot be turned into a proprietary hosted product without contributing changes back. This is the "open core, permissive SDK" shape common to self-hosted software (Jellyfin, Nextcloud, Immich).

Two honest limits, recorded rather than hidden:

1. **The linking exception is bespoke wording** adapted from the FSF's own established exceptions (the GPL Classpath exception and the GCC Runtime Library Exception). It has **not** had individual legal review — a deliberate call for a project without a legal budget. Its worst case if imperfectly worded is that modules are more encumbered than intended, not liability for users.
2. **Copyright is attributed to "the Mosaic authors,"** a placeholder convention, pending a specific person or entity.

AGPL obligations are dormant while a repository is private and activate on public or network use; the Platform is now public.

## Implementation

Each repository carries its `LICENSE` (and the Platform its `LICENSE-EXCEPTION`). Every Platform Go file carries an SPDX header, applied by a tool (`tools/licenseheader`) rather than by hand and enforced in CI (a `verify` workflow runs the check on every push and pull request), with a local pre-commit hook that adds it automatically.
