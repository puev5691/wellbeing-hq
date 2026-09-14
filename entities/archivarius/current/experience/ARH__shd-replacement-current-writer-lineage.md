# ARH — SHD replacement current-writer event-lineage

status: `REPLACEMENT_CURRENT_WRITER_ESTABLISHED__WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`
entity: `ARH / АРХИВАРИУС`
project_time: omitted; trusted project-time source not used

## Fresh GitHub-preflight

Previous ARH boundary:
`f60eaf8332e3e22140ff0317e062f130f647852f`

Pre-profile HQ HEAD:
`4abab83e831d236e3a97949c103675460c261bb9`

Compare result:
- status: `ahead`;
- ahead: 2 commits;
- behind: 0;
- changed project-field paths: only `entities/shardovik/current/`;
- no fresh changes in `entities/*/inbox/`, `entities/*/outbox/`, `routes/dispatch/`, `routes/receipts/`, `receipts/`, `handoff/`, `registry/` or recovery/activation-state before ARH profile work.

Fresh commits:
1. `85260a61784e9aec33784c5d50cfbc3bfceab19b` — `SHD: establish replacement current-writer after verified recovery`;
2. `4abab83e831d236e3a97949c103675460c261bb9` — `SHD: enter waiting state after replacement initiation`.

## Classified state transition

The earlier ARH state recorded only:
- KOO correction/re-verification PASS;
- practical replacement cold-start permitted;
- practical initiation not yet performed;
- replacement current-writer not yet established.

Fresh SHD evidence now closes that exact dependency.

### Current-writer artifact

Artifact:
`entities/shardovik/current/SHD__replacement-initiation-current-writer.md`

Immutable identity:
- commit: `85260a61784e9aec33784c5d50cfbc3bfceab19b`;
- blob: `88473e85feab1ae5482ff33268ca488abc42f8a4`.

Recorded state:
- `status: initiation_verified`;
- `current_writer_state: replacement_current_writer_established`;
- `old_writer_state: historical_non_authoritative`;
- production mutation: `no`;
- secrets/credentials: `not_accessed`.

The artifact records passage of the ordered recovery gates: approved sources, corrected base-recovery integrity, emergency overlay, independent KOO PASS, fresh HQ preflight, bounded MAZHOR read-only gate and absence of competing replacement-writer evidence.

### Immutable readback / post-handoff state

Artifact:
`entities/shardovik/current/SHD__replacement-resume-state.md`

Immutable identity:
- commit: `4abab83e831d236e3a97949c103675460c261bb9`;
- blob: `0df4a0b7c135f515b9923f53eb68a32846beb449`.

It records immutable readback `PASS` for the current-writer artifact and moves SHD to:
`WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`.

This waiting state is not a recovery failure and does not revoke replacement writer authority. It means no fresh exact SHD profile task was present after the handoff.

KOO remains control owner. `scheduler_eligible: false` remains consistent with `entities/koordinator/current/KOO__shd-control-return-v01.md`, which requires an exact OPERATOR direction before KOO creates the next SHD task.

## ARH recovery-state reconciliation

ARH reconciled:
`entities/archivarius/current/recovery-registry.jsonl`

Registry commit:
`61cce19205d9f1b7ad59c8ca909f8c0db0e58a56`

Registry blob:
`210d65590e974c769e4ce53d89ebfb37aef336aa`

The SHD record now states:
- practical replacement initiation: `performed_and_verified_by_shd_current_writer_artifact`;
- current-writer transfer: `replacement_current_writer_established`;
- post-handoff state: `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION`;
- control owner: `KOO`;
- scheduler eligible: `false`;
- production mutation: `no`;
- secrets/credentials: `not_accessed`.

Historical checksum defect and corrected candidate integrity layer remain preserved as provenance. The correction candidate was not promoted to canon.

## Exact current boundary

Factual now:
- corrected SHD recovery integrity was independently verified by KOO;
- practical replacement initiation was performed;
- replacement SHD current-writer was established;
- exact current-writer artifact was read back successfully;
- old degraded SHD writer is historical/non-authoritative;
- replacement SHD is waiting for an exact OPERATOR profile direction through KOO.

Not factual / not authorized by this event:
- a new SHD profile task exists;
- SHD is currently executing profile work;
- WBN/WBNP/TERA2 launch occurred;
- production mutation occurred;
- firewall/service changes occurred;
- secrets/credentials were accessed;
- candidate/research material became canon.

## Anti-regression lesson

`cold-start permitted` and `cold-start performed` are different states.

The transition to replacement writer authority is accepted here only because the exact SHD current-writer artifact exists and the subsequent SHD resume artifact records immutable readback PASS. Neither the earlier KOO permission nor OPERATOR routing alone was sufficient.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить проверяемый переход SHD от разрешённого cold-start к фактически установленному replacement current-writer и синхронизировать recovery-state без расширения полномочий
СТАТУС: `replacement_current_writer_established_waiting_operator_exact_profile_direction`
