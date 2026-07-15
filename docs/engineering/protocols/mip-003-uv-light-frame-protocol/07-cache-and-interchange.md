<!--
File: docs/engineering/protocols/mip-003-uv-light-frame-protocol/07-cache-and-interchange.md
Document: MIP-003
Status: Draft
Version: 0.1
-->

# 07 — Cache And Interchange

---

# MOS Cache

A canonical static `UVLightFrame` MAY be stored as one MOS Cache entry.

The cache entry identity SHOULD include:

- MIP-003 major version
- `sourceId`
- `sourceRevision`
- generator identity
- normalisation-profile identity

The frame is derived and reproducible.

Cache deletion MUST NOT cause permanent information loss or prevent regeneration from the source artwork.

[MEG-007 — Storage Architecture](../../guides/meg-007-storage-architecture/07-mos-cache.md) remains authoritative for MOS Cache lifecycle.

---

# Stream Persistence

Persisting sampled video frames is optional.

A runtime SHOULD avoid persistent frame accumulation unless reuse benefit exceeds storage and invalidation cost.

Stream persistence MUST NOT become a prerequisite for video presentation.

---

# Interchange

A producer and consumer exchanging serialised frames MUST support the unsupercompressed canonical KTX 2 profile.

They MAY negotiate Zstandard-supercompressed KTX 2 frames.

A producer MUST NOT send optional compression before confirming consumer support.

Transport framing, authentication and delivery are outside MIP-003.

The enclosing transport MUST preserve each KTX 2 payload without mutation.

---

# Integrity

The enclosing MOS Cache or transport MAY attach a content digest.

If present, integrity validation MUST complete before the frame becomes active.

A failed integrity check invalidates the frame but MUST NOT block playback or invalidate the last stable field.
