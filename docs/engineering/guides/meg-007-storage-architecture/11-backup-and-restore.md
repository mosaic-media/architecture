<!--
File: docs/engineering/guides/meg-007-storage-architecture/11-backup-and-restore.md
Document: MEG-007
Status: Draft
-->

# Backup and Restore

> *Backups exist to protect business information, not implementation details.*

---

# Purpose

Storage systems fail.

Examples include:

- hardware failure
- accidental deletion
- corrupted databases
- operator mistakes
- failed upgrades
- ransomware
- catastrophic system loss

The purpose of backup is not simply to duplicate storage.

Its purpose is to preserve the information that cannot be recreated.

This document defines the backup and recovery strategy for the Mosaic platform.

---

# Philosophy

Within Mosaic:

> **Back up information according to its business value, not according to where it is stored.**

Not every storage system deserves equal protection.

Business information should always take precedence over:

- caches
- analytics
- generated assets

Recovery should restore:

The platform.

Not every implementation detail.

---

# Recovery Goals

A successful recovery should preserve:

- users
- libraries
- playback progress
- capability configuration
- media relationships
- archive information

The Runtime should automatically regenerate:

- caches
- search indexes
- analytical datasets

Recovery effort should remain proportional to information value.

---

# Backup Categories

Storage systems naturally divide into:

```mermaid
flowchart TD

N1["Critical"]
N2["Important"]
N3["Rebuildable"]

N1 --> N2
N2 --> N3
```

This classification determines backup policy.

---

# Critical Data

Critical information includes:

- PostgreSQL
- MOS archives
- capability configuration

Loss results in permanent business information loss.

These systems MUST be backed up.

---

# Important Data

Important information includes:

- Blob Storage
- artwork
- subtitles
- generated previews (where regeneration is expensive)

Backup strategy depends upon regeneration cost.

If regeneration is inexpensive:

Rebuilding may be preferable.

---

# Rebuildable Data

Rebuildable information includes:

- MOS Cache
- DuckDB analytical datasets
- search indexes
- recommendation inputs

These SHOULD generally not be backed up.

Instead.

```mermaid
flowchart TD

N1["Restore"]
N2["Rebuild"]

N1 --> N2
```

Derived information should remain disposable.

---

# Backup Strategy

Typical backup flow.

```mermaid
flowchart TD

N1["PostgreSQL"]
N2["Backup"]
N3["Archive"]
N4["Verify"]
N5["Retention"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
```

Every backup should be:

- complete
- verifiable
- restorable

An untested backup should not be assumed to be valid.

---

# PostgreSQL Backup

Business State MUST receive regular backups.

Examples include:

- users
- playback
- libraries
- collections
- configuration

Backups should preserve transactional consistency.

Point-in-time recovery MAY be supported where operational requirements justify it.

---

# Blob Backup

Blob Storage backup policy depends upon asset class.

Examples.

Critical.

- user artwork
- uploaded subtitles

Rebuildable.

- generated thumbnails
- derived previews

Asset lifecycle should determine backup priority.

---

# MOS Archive Backup

MOS archives are already portable.

Nevertheless:

They SHOULD be included in platform backups.

Archives provide:

- migration
- recovery
- offline preservation

Losing archives unnecessarily reduces recovery options.

---

# DuckDB Recovery

DuckDB SHOULD generally rebuild rather than restore.

Recovery flow.

```mermaid
flowchart TD

N1["Restore PostgreSQL"]
N2["Replay Events"]
N3["Rebuild DuckDB"]

N1 --> N2
N2 --> N3
```

Analytical correctness should derive from business correctness.

Not backup frequency.

---

# MOS Cache Recovery

MOS Cache should never be restored.

Preferred.

```mermaid
flowchart TD

N1["Delete"]
N2["Rebuild"]

N1 --> N2
```

Cache regeneration should occur automatically during Runtime startup.

---

# Backup Integrity

Every backup SHOULD be verified.

Examples include:

- checksum
- hash
- test restore
- corruption detection

Verification should occur before backups are considered complete.

A backup that cannot be restored is operationally equivalent to no backup at all.

---

# Backup Frequency

Backup frequency depends upon information value.

Examples.

Business State.

```

Frequent
```

Blob Storage.

```

Scheduled
```

Caches.

```

Never
```

Recovery objectives should determine scheduling.

Not implementation convenience.

---

# Restore Order

Recovery follows storage ownership.

```mermaid
flowchart TD

N1["Configuration"]
N2["PostgreSQL"]
N3["Blob Storage"]
N4["MOS Archives"]
N5["DuckDB Rebuild"]
N6["MOS Cache Rebuild"]
N7["Runtime Startup"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Derived information always follows authoritative information.

---

# Disaster Recovery

Complete platform recovery should follow this sequence.

```mermaid
flowchart TD

N1["Provision Runtime"]
N2["Restore Configuration"]
N3["Restore PostgreSQL"]
N4["Restore Blob Storage"]
N5["Import MOS Archives"]
N6["Rebuild Derived Storage"]
N7["Start Runtime"]

N1 --> N2
N2 --> N3
N3 --> N4
N4 --> N5
N5 --> N6
N6 --> N7
```

Recovery should be deterministic.

Every operator should follow the same procedure.

---

# Incremental Backup

The Runtime MAY support incremental backups.

Suitable candidates include:

- PostgreSQL WAL
- Blob Storage changes
- MOS archive additions

Incremental backup should reduce operational cost while preserving recovery guarantees.

---

# Offline Backup

Backups SHOULD support offline storage.

Examples include:

- removable storage
- encrypted archives
- cloud storage
- cold storage

Business continuity should not depend upon one physical location.

---

# Encryption

Backup media SHOULD support encryption.

Especially:

- user information
- authentication data
- capability configuration

Encryption policy belongs to the Security Architecture ([MEG-009](../meg-009-security-architecture/index.md)).

Backup systems should integrate with those requirements.

---

# Testing Recovery

Recovery procedures SHOULD be tested regularly.

Typical exercises include:

- restoring PostgreSQL
- rebuilding DuckDB
- validating MOS archives
- regenerating caches

Recovery documentation should remain executable.

Not theoretical.

---

# Recovery Objectives

The platform SHOULD define:

- Recovery Point Objective (RPO)
- Recovery Time Objective (RTO)

These values determine:

- backup frequency
- infrastructure investment
- operational planning

Business requirements should drive recovery strategy.

---

# Observability

Backup systems SHOULD expose:

- backup duration
- backup size
- verification results
- restore duration
- rebuild progress

Operators should always understand:

> **Can this platform be recovered?**

Observability is as important during recovery as during normal operation.

---

# Anti-Patterns

The following practices are prohibited.

## Backing Up Caches

Persisting MOS Cache unnecessarily.

---

## Ignoring Verification

Assuming backups are valid without testing restoration.

---

## Restoring Derived Data

Restoring analytical datasets instead of rebuilding them.

---

## Runtime Recovery

Attempting to restore Runtime execution state.

Runtime State should begin cleanly.

---

## Single Backup Copy

Maintaining only one recoverable copy of business information.

---

## Untested Disaster Recovery

Documenting recovery procedures without executing them.

---

# Mosaic Guidelines

Within Mosaic:

- Business State MUST be backed up.
- Derived information SHOULD be rebuilt rather than restored.
- Backup integrity MUST be verified.
- Restore order MUST follow storage ownership.
- Runtime State MUST NOT be backed up.
- Recovery SHOULD remain deterministic.
- Backup encryption SHOULD protect sensitive information.
- Disaster recovery SHOULD be exercised regularly.
- Backup success MUST remain observable.

---

# Relationship to MEG

Migrations explain:

> **How storage evolves.**

Backup and Restore explain:

> **How storage survives failure.**

The next chapter introduces **Storage Guidelines**, bringing together the architectural principles of MEG-007 into practical guidance for engineers designing new persistence within the Mosaic platform.

---

# Summary

Backups should preserve information.

Not implementations.

Within Mosaic:

- PostgreSQL preserves business truth.
- MOS archives preserve portability.
- Blob Storage preserves binary assets where appropriate.
- DuckDB and MOS Cache preserve performance, not permanence.

By restoring authoritative information first and rebuilding everything else, the platform achieves both reliable recovery and operational simplicity.
