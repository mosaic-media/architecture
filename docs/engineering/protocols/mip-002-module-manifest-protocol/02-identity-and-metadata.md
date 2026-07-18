<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/02-identity-and-metadata.md
Document: MIP-002
Status: Draft
-->

# 02 — Identity And Metadata

---

# Identity

Every module must declare stable identity information.

At minimum, identity should include:

- module identifier
- display name
- module version
- manifest version
- provider or author

The identifier is the stable Platform reference.

The display name is presentation metadata.

---

# Metadata

Metadata should help humans and tooling understand the module without executing it.

Useful metadata includes:

- description
- supported Mosaic versions
- documentation references
- ownership information
- support contact

Metadata should not be used as an authority mechanism.

Permissions and contracts define authority.

---

# Catalogue And Onboarding Metadata

Module manifests provide the metadata from which the Supervisor builds Module Catalogue and onboarding views.

That metadata should be sufficient to describe:

- the user-facing Module name and description
- feature and provider categories
- supported media domains
- whether selection is optional or required by another Module
- available release or update channels
- documentation and support references

Clients may choose platform-appropriate presentation, but they must derive available Module choices from manifest metadata rather than a hardcoded catalogue.

Catalogue metadata is descriptive.

It does not bypass dependency, permission, SDK compatibility or admission validation.
