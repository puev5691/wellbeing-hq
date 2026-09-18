# KOO → ARH: project preservation / backup audit r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

## Purpose

Perform a fresh project-wide preservation and backup audit. The goal is to determine whether the WELLBEING project can survive loss or corruption of its primary working surfaces without relying on chat memory or a single GitHub repository.

## Fresh preflight

First perform fresh GitHub preflight over:
- puev5691/wellbeing-hq
- puev5691/wellbeing-entity-bootstrap
- puev5691/wellbeing-archivist

Use approved project/recovery/file canons.

## Required audit

1. Inventory current preservation mechanisms:
   - canonical/replacement recovery packages;
   - entity snapshots;
   - sender/route/receipt registries where relevant;
   - local host backups already known;
   - any existing external backup index.

2. Inventory project repositories/data surfaces that would need recovery after loss of the primary working environment.

3. For each important surface, classify:
   - primary working copy;
   - existing backup/recovery copy;
   - independent/offsite copy;
   - immutable/version identity;
   - checksum/readback status;
   - restore procedure availability;
   - last verified restore/readback evidence;
   - secret-exclusion boundary.

4. Explicitly verify known Mazhor backup evidence:
   external index commit
   `d36ea0c8a7ee85f1df41a10df25eb8e6b7eec05d`
   local locator
   `/data/wellbeing-lab/backups/shd-pre-reinit-v01`
   and classify its scope/limitations.

5. Determine gaps:
   - no independent mirror;
   - single-point repository/storage dependency;
   - no scheduled backup;
   - no restore drill;
   - stale backup;
   - missing checksum/index;
   - missing secrets exclusion;
   - recovery package not sufficient for project-wide recovery.

6. Produce a proposed project backup topology with at least:
   - primary Git repository layer;
   - independent repository mirror / bare clone layer;
   - local/offsite archive layer;
   - entity recovery package layer;
   - optional host/lab data archive layer.

7. Propose backup cadence without enabling automation yet:
   - event-driven preservation after major accepted milestones;
   - daily/regular repository mirror cadence;
   - periodic archive checkpoint;
   - periodic restore/readback drill.

8. Define in plain language:
   - maximum acceptable data loss window;
   - maximum acceptable recovery delay;
   without inventing values if OPERATOR has not set them. If values require OPERATOR decision, mark them as exact decision inputs.

9. Produce:
   - one current-state audit artifact;
   - one backup topology/cadence proposal;
   - one exact next-action list for KOO/OPERATOR/SIS/KOD if implementation is required.

## Boundaries

Do not:
- delete or rewrite any recovery package;
- change canonical recovery/current pointers;
- create destructive backups;
- read or copy secrets;
- enable cron/systemd/automation;
- alter production/runtime;
- claim backup/restore success without readback evidence.

If an existing backup locator cannot be accessed, record that exact limitation instead of inferring success.

## Expected terminal

`PASS_ARH_PROJECT_BACKUP_AUDIT_R01_READY_FOR_OPERATOR_DECISION`
or exact `BLOCKED_* / FAIL_*`.

Return results to KOO through Exchange Gate and stop.
