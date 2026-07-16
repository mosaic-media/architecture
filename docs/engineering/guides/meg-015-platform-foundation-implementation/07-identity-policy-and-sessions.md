<!--
File: docs/engineering/guides/meg-015-platform-foundation-implementation/07-identity-policy-and-sessions.md
Document: MEG-015
Status: Draft
Version: 0.1
-->

# 07 — Identity, Policy and Sessions

---

# Local Identity Scope

Mosaic Platform identity is local-first.

The first implementation should support:

- local user accounts;
- password credentials where enabled;
- passkey credential records;
- local recovery factors;
- session issuance and revocation;
- remote sign-in challenges for TV and shared-screen flows; and
- admin-controlled permission assignment.

Apple, Google and other external identity providers are out of scope for the Platform foundation.

---

# Session Model

Sessions should be server-issued, revocable and device-aware.

Each session should include:

| Field | Purpose |
|-------|---------|
| `session_id` | Server-side session identity |
| `user_id` | Authenticated user |
| `device_id` | Registered device or browser identity |
| `issued_at` | Creation time |
| `last_seen_at` | Activity tracking and remote sign-out |
| `expires_at` | Expiration boundary |
| `auth_strength` | Password, passkey or recovery flow strength |
| `capabilities` | Session-level capability constraints |

Remote sign-out should revoke server-side session records, not rely on clients deleting tokens.

---

# Policy Model

The first policy engine should keep an ABAC-ready shape even if the initial rules are simple.

```text
decision = authorize(subject, action, resource, context)
```

| Input | Example |
|-------|---------|
| Subject | user, role, session strength, device trust |
| Action | `platform.config.update`, `user.session.revoke` |
| Resource | user, device, configuration version, job |
| Context | local network, request origin, admin mode, recovery mode |

The policy decision point may start in-process. The enforcement point must be application services.

---

# Audit Events

Authentication, authorization and session lifecycle changes should publish audit events through the Platform event backbone.

Audit payloads must avoid credential material and must be compatible with redacted diagnostics.
