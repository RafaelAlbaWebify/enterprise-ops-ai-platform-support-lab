# KB-004 — VM Snapshot vs Backup

## Snapshot

A snapshot is a short-term restore point of a VM state.

Useful for:

- Testing changes
- Temporary rollback point
- Configuration changes

Risks:

- Not a replacement for backup
- Can affect performance if kept too long
- Can grow in size
- Should be managed carefully

## Backup

A backup is an independent recovery copy.

Useful for:

- Disaster recovery
- Long-term retention
- Recovery from VM loss
- Protection against corruption or deletion

## Support explanation

A snapshot helps roll back a recent change. A backup protects against broader failure scenarios.
