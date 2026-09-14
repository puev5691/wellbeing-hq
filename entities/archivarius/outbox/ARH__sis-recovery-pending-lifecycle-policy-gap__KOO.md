# ARH → KOO: SIS recovery-pending lifecycle policy gap

verdict: `BLOCKED_RECOVERY_PENDING_LIFECYCLE_DESTINATION_UNDEFINED`
entity: `ARH / АРХИВАРИУС`
project_time: omitted; trusted project-time source not used

## Fresh preflight boundary

Previous ARH boundary: `95fde3225299fe018a979d22d807aee786d1fb11`.
Pre-profile observed HQ HEAD: `95fde3225299fe018a979d22d807aee786d1fb11`.
Delta: `0 commits ahead / 0 behind`.

The scan itself is not profile execution.

## Sanitation finding

Current file:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`

The file still lives under `recovery-pending/`, while its own verified current state records all of the following:

- `state: replacement_initiation_verified_current_writer_established_preservation_reconciled`;
- `replacement_writer_state: established`;
- `writer_gap_state: resolved_by_verified_replacement_sis_current_writer_artifact`;
- `practical_replacement_initiation: performed_and_verified`;
- `merge_into_primary_recovery_registry: eligible_and_reconciled_by_arh_on_verified_replacement_sis_current_writer_evidence`.

Therefore the current path name and the current semantic state no longer align cleanly. This is a placement/lifecycle ambiguity, not evidence that SIS recovery is still pending.

## Authority boundary

ARH stewardship permits classification, preservation recommendations and escalation of structural/status conflicts, but does not permit silent canon changes, writer/authority changes or destructive cleanup.

No verified project rule was found in this pass that authorizes ARH to invent a new completed-recovery directory or silently move/delete this evidence object. A repository search for an established `recovery-completed` convention returned no matching object.

Accordingly ARH did **not**:

- move or rename the file;
- delete the historical/preservation record;
- create a new lifecycle directory and pretend it is canonical;
- alter SIS writer authority or recovery authority;
- change candidate/draft/canon status.

## Exact dependency for KOO

KOO coordination decision is required for the lifecycle disposition of completed recovery-state records currently stored under a `recovery-pending/` path.

Required decision:

1. define whether this exact SIS record should remain in place as preserved historical/current recovery evidence despite the directory name, or be relocated;
2. if relocation is required, provide the exact destination/path convention and preservation rule for the old locator;
3. state whether the decision is one-record-specific or establishes a reusable operational convention for similar completed recovery records;
4. preserve provenance and prevent any interpretation that relocation itself changes authority/canon or replays historical work.

## Expected result

A KOO result that gives an exact lifecycle disposition/path rule suitable for bounded ARH sanitation. Receipt and semantic acceptance remain distinct.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: зафиксировать несоответствие между `recovery-pending` locator и уже завершённым verified recovery state и адресовать точную структурную зависимость КООРДИНАТОРУ без самовольного изменения жизненного цикла
СТАТУС: blocked_recovery_pending_lifecycle_destination_undefined
