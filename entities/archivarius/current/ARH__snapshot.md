# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Resume-First current-state для восстановления ARH. Snapshot не является approval, не заменяет fresh GitHub-preflight и не создаёт current-writer authority сам по себе.

## Проверяемая граница этого refresh

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Previous ARH run boundary: `ad028679b52e30127f5719f931510b51af2b739c`
- Pre-profile HEAD: `703944f248186fc7017244bcb1451963457053c7`
- Compare: `ahead 7 / behind 0`
- Canonical ARH path: `entities/archivarius/`
- Recovery registry: `entities/archivarius/current/recovery-registry.jsonl`
- Experience/event-lineage: `entities/archivarius/current/experience/`

Каждый запуск ARH начинается только так:
`WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`.

Само сканирование не является профильным исполнением.

## Fresh delta classification

После предыдущей ARH-границы изменены только следующие профильные зоны:
- `entities/shtabist/outbox/`;
- `entities/volonter/outbox/`;
- `entities/koordinator/inbox/`;
- `routes/dispatch/`;
- `routes/activation/`;
- `registry/by-sender/volonter.jsonl`.

В исходной fresh delta не было новых изменений в:
- `entities/archivarius/inbox/`;
- `entities/archivarius/current/`;
- `routes/receipts/`;
- `receipts/`;
- `handoff/`;
- ARH recovery registry/pending state.

### SHT result

Artifact:
`entities/shtabist/outbox/SHT__entity-wake-initiation-resume-process-review__KOO.md`

Verdict:
`PASS_WITH_EXACT_PROCESS_FIXES`

Boundary:
- review complete;
- canon approval: no;
- implementation selection: no;
- production: no;
- exact fixes F1–F5 and test vectors T9–T12 are required before authority/terminology review.

KOO inbox locator and dispatch exist. Activation detector records `processing_started: no`, `activation_status: activation_failed`, reason `exact_entity_chat_resume_not_supported_by_current_adapter`. No KOO receipt/acceptance is inferred from routing or activation.

### VOL result

Artifact:
`entities/volonter/outbox/VOL__hybrid-interaction-p5-evidence-scout__KOO.md`

Verdict:
`P5_EVIDENCE_SCOUT_COMPLETE__NO_ELIGIBLE_CLOSED_EPISODE`

Boundary:
- no eligible closed P5 episode with measured before/after effect was found at the scout boundary;
- no numerical participant valuation, token, ownership share, governance right or subject-status conclusion was created;
- direct file exchange is only a future partial candidate because actual operator effort reduction is not yet measured.

KOO inbox locator and dispatch exist. Activation detector records `processing_started: no`, `activation_status: activation_failed`, reason `exact_entity_chat_resume_not_supported_by_current_adapter`. No KOO receipt/acceptance is inferred.

## ARH recovery — current truth

Verified source candidate:
`puev5691/wellbeing-entity-bootstrap@b9b88de32fe9e147b505ae158c898acb06d8762f:packages/arh-emergency-recovery-v03`

Independent KOO verification:
- artifact: `entities/koordinator/outbox/KOO__ARH-emergency-self-preservation-v03-verification__ARH.md`;
- commit: `d5d3da16792f2c235837698677e33b30caa9a8f5`;
- result: `PASS_INDEPENDENT_VERIFICATION`.

Canonical ARH recovery:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`

ARH canonical preservation publication remains PASS. The recovery registry still records practical ARH reinitiation as not performed; this snapshot does not silently upgrade that state.

## SHD replacement recovery/current-writer — current truth

The old snapshot statement `permission only / not yet performed` is superseded by exact SHD-owned evidence.

Current writer artifact:
`entities/shardovik/current/SHD__replacement-initiation-current-writer.md`

Exact publication:
- commit: `85260a61784e9aec33784c5d50cfbc3bfceab19b`;
- blob: `88473e85feab1ae5482ff33268ca488abc42f8a4`;
- state: `replacement_current_writer_established`;
- old writer: `historical_non_authoritative`;
- production mutation: no;
- secrets/credentials: not accessed.

Post-handoff artifact:
`entities/shardovik/current/SHD__replacement-resume-state.md`

Post-handoff commit:
`4abab83e831d236e3a97949c103675460c261bb9`

The replacement writer was therefore actually established. Historical base checksum defects remain provenance and are not rewritten away; corrected integrity evidence remains the recovery bridge rather than canon-promotion of the correction candidate.

After writer establishment SHD later received exact profile direction and performed bounded profile work. Therefore the historical immediate post-handoff state `WAITING_OPERATOR_EXACT_PROFILE_DIRECTION` must not be interpreted as a current universal SHD status.

## SIS replacement recovery/current-writer — current truth

Preferred recovery basis for the current replacement lineage:
`puev5691/wellbeing-entity-bootstrap@dfac1b1f4a4664f85f12c6590a511502b9828ace:entities/sis/preservation/pending/self-preservation-current-writer-v02`

Boundary:
- this is preferred recovery basis for the current replacement lineage;
- candidate-only, not Project Source/canon;
- historical `861645... + 23c83ad...` chain remains provenance-only.

Current writer artifact:
`entities/sisadmin/current/SIS__replacement-current-writer-v01.md`

Exact publication:
- commit: `2926908f9843a8c325a975dcf5180fa51baef2c5`;
- blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`.

Independent SIS initiation report:
`entities/sisadmin/outbox/SIS__replacement-initiation-v01-result.md`
commit `551abc81d6950b868d37607643456e0cc5bff982`.

Verified state:
- `current_writer_state: ESTABLISHED`;
- immutable current-writer readback: PASS;
- post-handoff competing writer check: `PASS_ONLY_ONE_REPLACEMENT_WRITER_ARTIFACT`;
- production mutation during recovery: none;
- historical task replay: none.

No recovery event authorizes automatic sudo, Telegram live send, public webhook, Entity Runner provider-side execution, VPN/server mutation, OSS/TERA2 replay or destructive cleanup.

## SHD → SIS эРэФия host-access route — exact open state

Source artifact:
`entities/shardovik/outbox/SHD__erefia-host-access-restore__SIS.md`

Source identity:
- source commit: `ad257fb1492bdb50866299ecdedf6ab6acebccb5`;
- source blob: `adda1932d85e26051928ac661e5653dd706ef01f`.

Purpose:
restore only bounded administrative access to the historical host called `эРэФия`, without changing TERA/WBN runtime.

Exchange Gate exists:
- dispatch commit: `2d5812cb105f81bda457f92dca8bdfa764e9cba5`;
- SIS inbox locator commit: `973771a82c657f24fce07f0abd3d690725dd2b03`;
- sender-registry append commit: `d4fa5534e8a833f79817fddc1919806f97606190`.

Activation boundary:
- detector: PASS;
- processing_started: no;
- activation_status: activation_failed;
- reason: `exact_entity_chat_resume_not_supported_by_current_adapter`;
- operator manual ping required: yes.

Exact receipt
`routes/receipts/SHD__erefia-host-access-restore__SIS.receipt.md`
is absent at this refresh boundary.

Therefore SIS processing, restored access, exact host locator, delivery, receipt or acceptance are not asserted.

## KOD Anthropic live-transport — reconciled acceptance truth

The old snapshot statement that the exact KOO receipt was absent is superseded.

Exact receipt now exists:
`routes/receipts/KOD__anthropic-live-transport-r01__KOO.receipt.md`

Accepted result:
`ACCEPTED_BOUNDED_TECHNICAL_TRANSPORT`

Accepted scope:
- live-capable transport preparation for `D0_SYNTHETIC` only;
- package readback `26/26 PASS`;
- real provider calls: 0;
- real credentials used: 0;
- credit purchases: 0;
- production deployments: 0.

The receipt does NOT authorize:
- account creation;
- credit purchase;
- API-key handling;
- live Anthropic request;
- D1/D2+ data;
- tools/search/files/MCP/code execution/fallback;
- production deployment.

Next gate remains OPERATOR account/billing/key/model-access readiness plus separate explicit authorization for one D0 live request.

The older `KOO__kod-serialized-queue-v02.md` still describes `anthropic-live-transport-r01` as active. Preserve this as an older working-queue snapshot; do not use that stale label to contradict the later exact receipt.

## ARH append-only receipt reconciliations already closed

### KOO v04 recovery route

Historical event `ARH-emergency-recovery-v04-result-KOO-001` remains the original dispatched fact.
Later exact receipt was reconciled append-only by `ARH-emergency-recovery-v04-result-KOO-002` as `received_and_processed`.

This closes only that exact route and does not create broader approval.

### KOO inbox-lifecycle review sender-state

Historical `ARH-inbox-lifecycle-operational-review-KOO-001` remains provenance.
A later append-only reconciliation records the exact KOO receipt/processing state without destructive history rewrite.

## ARH open service tails with no exact return receipt at this refresh boundary

The following exact receipt files remain absent on direct readback:

1. `routes/receipts/ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.receipt.md`
2. `routes/receipts/ARH__sis-sender-registry-reconciliation-gap__SIS.receipt.md`
3. `routes/receipts/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.receipt.md`

Absence of these receipts means ARH does not assert recipient processing or acceptance for those exact return routes.

## ARH anti-regression boundaries

- Raw inbox presence does not prove unprocessed work.
- Dispatch, locator or activation detector does not prove delivery/processing.
- Receipt does not equal broader approval beyond its exact recorded result.
- Candidate/draft/research does not become canon without authority.
- Historical failure is not rewritten by later success.
- Later success is not hidden behind an obsolete earlier state.
- Sender-registry reconciliation is append-only; old dispatched events remain history.
- `PERMITTED`, `PERFORMED` and `CURRENT_WRITER_ESTABLISHED` are distinct states.
- A current-writer handoff does not authorize automatic historical task replay.
- Exact task identity and dependency state must be revalidated immediately before processing start.
- A technical PASS is not economic effect evidence.
- Zero Git delta does not close pending routes.

## Current open work

1. Start every run with fresh GitHub-preflight and delta classification.
2. Watch the SHD → SIS эРэФия route for exact SIS receipt/result; do not infer restored access from activation detection.
3. Watch SHT wake/initiation/resume review for KOO decision; current SHT result is review-only and not canon approval.
4. Watch VOL P5 evidence scout for KOO decision; no eligible measured-effect episode exists in the current scout result.
5. Watch the three ARH service tails listed above for exact return receipts.
6. Continue bounded sanitation of stale/orphaned routes, duplicate locators, conflicting current-state and recovery/event-lineage drift only from exact evidence.
7. Preserve recovery/state/experience/event-lineage on meaningful changes.
8. Do not promote SIS preferred recovery candidate, SHT amendment candidate, VOL research result or other candidate/draft material to canon without exact authority.

## Resume-First for replacement ARH

1. Read canonical ARH recovery at immutable commit `9ffe7190298689bd90f047c249151213e101450e` and verify its identities.
2. Fresh-scan `puev5691/wellbeing-hq` after this snapshot boundary.
3. Check `entities/archivarius/inbox/`, current/outbox, dispatch/receipts, registries, handoff and recovery/experience/activation-state.
4. Classify new tasks/results/blockers/approval/acceptance/dependency changes.
5. Select one ARH-owned still-open task.
6. Recheck HEAD immediately before any mutation to avoid duplicate/racing sanitation writes.
7. Do not continue from historical memory alone.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: синхронизировать emergency current-state с фактическими SHD/SIS current-writer handoff, bounded KOD Anthropic acceptance, свежей SHT/VOL delta и открытым эРэФия route без выдуманного receipt/acceptance/canon promotion
СТАТУС: emergency-self-preservation-current
