<!--
File: docs/roadmaps/mrm-001-mosaic-platform-foundation/04-completion-evidence.md
Document: MRM-001
Chapter: 04
Status: Draft
Version: 0.1
-->

# 04 — Completion Evidence

MRM-001 is complete only when the following evidence exists and is linked from the release record.

## Platform Evidence

- an authenticated session can be established and revoked,
- local username/password and passkey sign-in work without email, phone or an external identity provider,
- recovery codes and trusted-device or administrator-assisted recovery are tested,
- a television or other limited-input client can complete one-time phone-assisted sign-in,
- paired devices can be renamed, inspected and remotely revoked,
- policy decisions combine user authority, resource relationships, device policy and session state,
- denied decisions are explainable and auditable,
- representative state persists and can be retrieved,
- GraphQL contracts are exercised by a client,
- a representative event is published, consumed and observed,
- health and diagnostics are available for the core runtime.

## Supervisor Evidence

- the Supervisor assembles the Mosaic binary from declared parts,
- the binary starts through the Supervisor,
- failed health checks produce actionable diagnostics,
- controlled restart or recovery is demonstrated,
- the first Module runs under Supervisor lifecycle control.

## SDK Evidence

- SDK examples compile against the supported Platform contracts,
- authentication, GraphQL, events and Module registration are covered,
- SDK failures expose stable typed errors,
- no consumer needs direct access to private Platform internals.

## Shell Evidence

- the Shell renders the core navigation and host states,
- loading, empty, error and recovery states are represented,
- accessibility settings are honoured,
- Module surfaces mount through the supported SDK/Shell boundary,
- the client-side MDL/MDS implementation remains the rendering authority.

## Module Evidence

- Jellyfin API integration completes the reference end-to-end path,
- Remote Media and Anime Modules use the same SDK and lifecycle contracts,
- Modules can be added or removed without a Platform fork,
- Module health and failure state are visible through the Supervisor and Shell.

## Roadmap Closure

The roadmap owner records which outcomes are complete, which are deferred and which require a follow-up MRM. Completion evidence must reference the authoritative specification or test artifact that proves each outcome.
