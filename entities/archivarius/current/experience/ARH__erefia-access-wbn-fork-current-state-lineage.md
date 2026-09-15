# ARH — Erefia access / WBN fork current-state lineage

status: `PASS_CURRENT_STATE_REFRESH`
entity: `ARH / АРХИВАРИУС`
project_time: omitted; trusted project-time source not used

## Invariant

`WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`

The scan itself was not counted as profile execution.

## Preflight boundary

repository: `puev5691/wellbeing-hq`
previous_ARH_boundary: `bceae0e1ba79d0bc6ec851badc54afd51ddf7398`
pre_profile_HEAD: `c44a0a684c32914a19827271133b0d88567543f1`
compare: `11 commits ahead / 0 behind`

Fresh changed paths:
- `entities/koordinator/inbox/SIS__erefia-access-readiness__KOO.md`
- `entities/shardovik/current/SHD__tera-wbn-three-host-state-v04.md`
- `entities/sisadmin/outbox/SIS__erefia-access-readiness__KOO.md`
- `registry/by-sender/sisadmin.jsonl`
- `routes/activation/SIS__erefia-access-readiness__KOO.activation.md`
- `routes/dispatch/SIS__erefia-access-readiness__KOO.md`

Fresh exact ARH recovery-operational task in `entities/archivarius/inbox/`: not found.

## Classified dependency changes

### SIS / Erefia

Latest artifact identity:
- artifact: `entities/sisadmin/outbox/SIS__erefia-access-readiness__KOO.md`
- commit: `26df12757efc46e4a7bcd9e049a86837930de061`
- blob: `424bfba42d385e056552ef3528205d61cb9c3447`
- result: `PASS_EREFIA_ACCESS_READY_VIA_COMMANDER`

Bounded semantic change:
- exact Erefia host is reachable through Remote Desktop Commander;
- prior SSH/manual-login blocker is superseded for bounded read-only investigation;
- production/TERA/WBN mutation remains `no`;
- no receipt or acceptance is inferred.

Activation evidence remains bounded:
- `activation_requested: yes`
- `processing_started: no`
- `activation_status: activation_failed`
- `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`

Exact receipt checked and absent:
`routes/receipts/SIS__erefia-access-readiness__KOO.receipt.md`

### SHD / WBN

Current-state artifact:
`entities/shardovik/current/SHD__tera-wbn-three-host-state-v04.md`

commit: `c44a0a684c32914a19827271133b0d88567543f1`
status: `BLOCKED_CANONICAL_BRANCH_DECISION`
production_mutation: `no`

Verified fork boundary:
- common history through block `2984033`;
- first divergence at block `2984034`;
- account state also differs;
- destructive auto-recovery / DB reset / forced reorg is stopped pending policy decision.

Burzh remains a technical candidate only. No canonical branch decision is made or inferred by ARH.

## Open ARH tails rechecked

`routes/receipts/ARH__recovery-operational-review-routing-gap__KOO.receipt.md`: absent.

`routes/receipts/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.receipt.md`: absent.

Therefore:
- recovery-operational review remains `ARH_RECOVERY_OPERATIONAL_REVIEW_GAP_ROUTED_TO_KOO_WAITING_PROCESSING_EVIDENCE`;
- recovery-pending object is not moved/renamed/deleted;
- KOO processing, delivery and acceptance are not asserted;
- ARH does not declare `EXECUTING`.

## Profile action

Updated:
`entities/archivarius/current/ARH__snapshot-delta-current.md`

update commit: `c98f6a46afbd4968779233f1fbd7dae8d1fd6a56`
updated blob: `60be36443696b9baada44cefb02091a725ca39ba`
readback: `PASS`

The supplement now preserves the fresh Erefia access PASS, WBN fork stop-condition, incomplete Exchange Gate semantics, open ARH blockers and a provenance caution for revisioned SIS route identities.

## Sanitation boundary

The SIS Erefia route reuses mutable artifact/dispatch/locator paths while sender registry preserves r1/r2/r3 immutable artifact identities. Historical rows are therefore interpreted only with their pinned commit/blob identities. ARH records this provenance caution but does not rewrite foreign historical rows or routes in this pass.

## Experience card

idea: preserve material dependency changes before the next recovery/resume boundary

trial: fresh compare + exact SIS artifact/locator/dispatch/registry/activation readback + SHD current-state readback + ARH inbox/receipt checks

result: Erefia access blocker became a bounded Commander PASS, while WBN moved to a verified fork stop-condition requiring a canonical-history decision

success/failure: `success` for ARH current-state preservation; external KOO receipts/processing remain unresolved

fixation: `ARH__snapshot-delta-current.md` commit `c98f6a46afbd4968779233f1fbd7dae8d1fd6a56` plus this lineage

lesson: access restoration can remove one dependency while immediately exposing a deeper state-integrity blocker; preserving both transitions prevents a later recovery from mistaking reachable hosts for a safe chain-reconciliation state.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить проверяемую причинную цепочку свежего preflight и обновления current-state
СТАТУС: PASS_CURRENT_STATE_REFRESH
