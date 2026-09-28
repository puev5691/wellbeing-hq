# SHD pre-reinit local backup

Purpose: preserve non-secret MAZHOR/lab-01 state before emergency chat replacement.

Included:
- host-state.txt
- lab-tree.txt
- repo-state.txt
- lab-workfiles.tar.gz
- sha256sums.txt

Explicitly excluded from archive/readback:
- /data/wellbeing-lab/secrets
- /data/wellbeing-lab/logs
- /data/wellbeing-lab/tmp
- /data/wellbeing-lab/backups
- Git repository object database; repo identity is recorded separately and can be re-cloned.

This backup is not a writer handoff, recovery acceptance, or production snapshot.
