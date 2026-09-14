# ARH event-lineage — emergency snapshot refresh to current verified truth

status: `PROFILE_WORK_COMPLETE`
project_time: omitted; trusted project-time source not used

## Trigger

Previous ARH run boundary:
`ad028679b52e30127f5719f931510b51af2b739c`

Fresh pre-profile HEAD:
`703944f248186fc7017244bcb1451963457053c7`

Fresh compare:
- ahead: 7;
- behind: 0.

Observed fresh delta affected SHT/VOL outbox, KOO inbox, dispatch/activation and VOL sender-registry. It did not itself modify ARH inbox/current/recovery.

## Sanitation finding

`entities/archivarius/current/ARH__snapshot.md` was materially stale against already verified repository evidence accumulated after its old boundary.

Critical stale claims included:
1. SHD replacement cold-start/current-writer still described as permission-only/not performed;
2. SIS replacement writer evidence absent from snapshot;
3. KOD Anthropic live-transport exact KOO receipt described as absent;
4. the current SHD→SIS эРэФия host-access open route was absent;
5. fresh SHT wake/initiation/resume review and VOL P5 evidence scout were absent.

## Evidence used

### SHD

- current-writer publication commit: `85260a61784e9aec33784c5d50cfbc3bfceab19b`;
- artifact: `entities/shardovik/current/SHD__replacement-initiation-current-writer.md`;
- current-writer blob: `88473e85feab1ae5482ff33268ca488abc42f8a4`;
- post-handoff commit: `4abab83e831d236e3a97949c103675460c261bb9`;
- recovery registry already records `practical_replacement_initiation_state=performed_and_verified_by_shd_current_writer_artifact` and `current_writer_transfer_state=replacement_current_writer_established`.

### SIS

- preferred recovery basis: `puev5691/wellbeing-entity-bootstrap@dfac1b1f4a4664f85f12c6590a511502b9828ace:entities/sis/preservation/pending/self-preservation-current-writer-v02`;
- current-writer artifact: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`;
- commit: `2926908f9843a8c325a975dcf5180fa51baef2c5`;
- blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`;
- initiation report commit: `551abc81d6950b868d37607643456e0cc5bff982`;
- report states `current_writer_state: ESTABLISHED`, immutable readback PASS, only-one-replacement-writer PASS.

Candidate boundary retained: preferred recovery basis is not promoted to Project Source/canon.

### KOD Anthropic live transport

Exact receipt exists:
`routes/receipts/KOD__anthropic-live-transport-r01__KOO.receipt.md`

Receipt verdict:
`ACCEPTED_BOUNDED_TECHNICAL_TRANSPORT`

Boundaries retained:
- provider calls: 0;
- real credentials: 0;
- credit purchase: 0;
- production deployment: 0;
- no live Anthropic request authority;
- separate OPERATOR account/billing/key/model-access gate remains.

### SHD → SIS эРэФия route

Source artifact:
`entities/shardovik/outbox/SHD__erefia-host-access-restore__SIS.md`

Exchange Gate exists, but activation records:
- detector PASS;
- processing_started: no;
- activation_status: activation_failed;
- reason: `exact_entity_chat_resume_not_supported_by_current_adapter`.

Exact receipt `routes/receipts/SHD__erefia-host-access-restore__SIS.receipt.md` is absent.
No restored access/delivery/processing/acceptance is inferred.

### Fresh SHT/VOL delta

SHT:
- artifact: `entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md`;
- verdict: `PASS_WITH_EXACT_PROCESS_FIXES`;
- canon approval: no.

VOL:
- artifact: `entities/volonter/outbox/VOL__hybrid-interaction-p5-evidence-scout__KOO.md`;
- verdict: `P5_EVIDENCE_SCOUT_COMPLETE__NO_ELIGIBLE_CLOSED_EPISODE`;
- no fabricated measured effect or allocation.

Both KOO activations record `processing_started: no` and `activation_failed`; no KOO receipt/acceptance is inferred.

## Action

Updated:
`entities/archivarius/current/ARH__snapshot.md`

Publication commit:
`60fe36a885c507cfc4fea3866659b9313185ee1f`

Published blob:
`ddcaa054f28b7e7b5ee33f1140985ed96df80d71`

Immutable readback:
`PASS`

The refresh replaced stale current-state claims while preserving historical provenance and authority boundaries.

## Exchange Gate decision

No new Exchange Gate route was created.

Reason:
this profile step is ARH-owned current-state/recovery sanitation. It does not create a new inter-entity task or result requiring recipient processing.

## Anti-regression lesson

A recovery snapshot is allowed to preserve historical failure, but it must not keep presenting an old intermediate state as current after exact later evidence exists. `PERMITTED`, `PERFORMED`, `CURRENT_WRITER_ESTABLISHED`, `RECEIVED` and `ACCEPTED` remain distinct states and must be updated only from exact evidence.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную цепочку refresh emergency snapshot после обнаружения stale SHD/SIS/KOD/current-route truth
СТАТУС: profile_work_complete_readback_pass
