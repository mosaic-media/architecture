<!--
File: docs/engineering/protocols/mip-002-module-manifest-protocol/03-dependencies-and-permissions.md
Document: MIP-002
Status: Draft
-->

# 03 — Dependencies And Permissions

---

# Dependencies

Modules should declare dependencies explicitly.

Dependencies may include:

- Platform version
- Runtime contract version
- SDK version
- required capabilities
- optional capabilities
- incompatible modules

The Supervisor should validate dependencies before invoking the Build Pipeline.

---

# Permissions

Modules should declare requested permissions explicitly.

Permission declarations should answer:

- what authority is requested
- why the authority is required
- which contracts are needed
- whether the permission is optional

The Platform grants authority deliberately.

It should not infer authority from implementation.
