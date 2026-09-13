# ARH — аварийный snapshot

status: emergency-self-preservation-current
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Назначение

Resume-First current-state для восстановления ARH. Snapshot не является approval, не заменяет fresh GitHub-preflight и не доказывает practical cold-start нового экземпляра.

## Проверяемая граница

- Repository: `puev5691/wellbeing-hq`
- Branch: `main`
- Boundary before this snapshot refresh: `5d4e5b7942669b6a20b9c636724970302126d275`
- Fresh preflight compare from the previous ARH boundary to `main`: `identical`, `0 ahead / 0 behind`, `0 commits`
- Canonical ARH path: `entities/archivarius/`
- Recovery registry: `entities/archivarius/current/recovery-registry.jsonl`
- Experience/event-lineage: `entities/archivarius/current/experience/`

Каждый replacement ARH обязан начать с нового GitHub-preflight по инварианту:
`WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`.

## ARH recovery — current truth

Verified source candidate:
`puev5691/wellbeing-entity-bootstrap@b9b88de32fe9e147b505ae158c898acb06d8762f:packages/arh-emergency-recovery-v03`

Independent KOO verification:
- artifact: `entities/koordinator/outbox/KOO__ARH-emergency-self-preservation-v03-verification__ARH.md`;
- commit: `d5d3da16792f2c235837698677e33b30caa9a8f5`;
- result: `PASS_INDEPENDENT_VERIFICATION`;
- source composition: `8/8 PASS`;
- exact source provenance: `5/5 PASS`;
- independent source SHA-256: `7/7 PASS`.

Canonical ARH recovery:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`

Canonical preservation publication remains **PASS**. Practical replacement ARH initiation and current-writer transfer are **NOT PERFORMED**. Do not infer either from preservation PASS, inbox placement, activation detector or receipt.

Historical v02/v03 candidate paths remain provenance; future recovery should prefer the canonical immutable locator above and then fresh-scan HQ after this snapshot boundary.

## Current project-field classification

Fresh preflight found no commits after `5d4e5b7942669b6a20b9c636724970302126d275`. Therefore there are no newly changed files after the previous ARH run in:
- `entities/*/inbox/`;
- `entities/*/outbox/`;
- `entities/*/current/`;
- `routes/dispatch/`;
- `routes/receipts/`;
- `receipts/`;
- `handoff/`;
- `registry/`;
- recovery / experience / activation-state.

Zero delta does not close previously open routes and does not convert pending activation into processing.

## KOD serialized queue — current verified working state

Source of current queue truth:
`entities/koordinator/current/KOO__kod-serialized-queue-v02.md`
blob `d0b16369ce9b2decc6c6f02e8f2b09bb2e918a10`.

Completed:
- `anthropic-direct-adapter-r01`;
- exact KOO receipt: `routes/receipts/KOD__anthropic-direct-adapter-r01__KOO.receipt.md`;
- verdict: `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`;
- accepted scope: credential-free, network-disabled, `D0_SYNTHETIC` only;
- live API call: no;
- credentials: no;
- credits purchase: no;
- production: no.

Active KOD lane:
- `anthropic-live-transport-r01`;
- task commit: `00116e5003680fb4a33f18a0d5739bb9c3ac1fd0`;
- live network call remains forbidden in this pass.

Observed candidate package:
`entities/koder/outbox/multi-model-anthropic-live-transport-r01/`
with manifest status `candidate_ready_for_account_gate`.
Package presence is not a KOO receipt, acceptance, live call, credential use, billing readiness or production permission.

READY_SERIALIZED after active lane:
1. `info-entry-static-preview-E1-evidence-alignment`;
2. `activation-lineage-schema-F1-F2`;
3. `koder-sender-registry-sanitation`.

The queue is KOO working state, not Project Source/canon. Inbox placement or queue presence is not KOD execution.

## KOD sender-registry sanitation — exact open state

Previous bounded sanitation finding remains routed, and a later F3 was found for:
`record_id: KOD-anthropic-direct-adapter-r01-001`.

Observed stale state at the recorded boundary:
- `status=dispatched`;
- `receipt=null`;
- exact KOO receipt for the underlying KOD result already exists.

ARH F3 update:
- artifact: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md`;
- artifact commit: `94e3b484d874eb9c6f163d051ae0ca353379ae92`;
- artifact blob: `33614248ee1c53add4d90bc947da44a5a7b35491`;
- dispatch commit: `96bdc5a5cf64f61695db50e714af279e6a4eba3e`;
- KOO inbox locator commit: `716104cffd65245dcdcd4ff4901ffd839bc37e2d`;
- ARH sender-registry append commit: `eecfcba6f3a87fce109b78fbbc8206a2de4c2a85`;
- event-lineage commit: `5d4e5b7942669b6a20b9c636724970302126d275`.

Activation record:
`routes/activation/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.activation.md`
records detector PASS but `processing_started: no`, `activation_status: activation_failed`, reason `exact_entity_chat_resume_not_supported_by_current_adapter`, `operator_manual_ping_required: yes`.

Exact receipt for `ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md` is still absent at this snapshot boundary. Therefore F3 is **not** declared accepted, queued by KOO, or executed by KOD from ARH evidence alone.

## KOO inbox-lifecycle preservation verdict — open receipt state

ARH independent re-check result:
- verdict: `PASS_BOUNDED_PRESERVATION_RECHECK`;
- artifact: `entities/archivarius/outbox/ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md`;
- artifact commit: `04037d8db16d81c5b84c348273e87558952f270b`;
- dispatch commit: `e2976c3ecfc1ba80aa5852b659ee7a1b75dd7a7b`;
- KOO inbox locator commit: `0b65a6e1419e0742bc99e2e0d5d6a6d4f1a97b71`.

Exact receipt for this returned verdict is still absent. No KOO receipt/acceptance is inferred.

## KOO parallel-queue supplemental recovery checkpoint

Processed task:
`entities/archivarius/inbox/KOO__parallel-queue-transition-preservation__ARH.md`.

Minimal supplemental preservation checkpoint:
`puev5691/wellbeing-entity-bootstrap@9b2a37c80f99495249a21d3b8e6390a5abd85e85:entities/koo/preservation/parallel-queue-transition-v01`

Fresh immutable readback was `2/2 SHA-256 PASS`.

Exact result receipt exists:
`routes/receipts/ARH__parallel-queue-transition-preservation__KOO.receipt.md`
commit `2a0010303e7fc61d1f4cdd5cdf9f74350a3095d2`, result `PASS_SUPPLEMENTAL_RECOVERY_CHECKPOINT_ACCEPTED`.

This checkpoint remains supplemental: canonical KOO recovery was not replaced, current-writer state was not transferred, secrets/credentials were not preserved, and process/candidate artifacts were not promoted to Project Sources.

## SIS Phase 1B sender-registry sanitation — open receipt state

Exact underlying KOO receipt already exists for SIS tooling-path result and records:
`WAITING_OPERATOR_EXACT_HUMAN_ACTION_RECEIVED`.

ARH sanitation route:
- artifact: `entities/archivarius/outbox/ARH__sis-sender-registry-reconciliation-gap__SIS.md`;
- artifact commit: `023e22da0e0d7424bcf817b8b8714d3ea9b455eb`;
- dispatch commit: `cffdb4d2240b2ea36395b22b4f5765838d713917`;
- SIS inbox pointer commit: `e3f9757fbf25e10036fd50084c394457d134e796`;
- ARH sender-registry commit: `4875b54b3309423c0e781b8f659195bda6564b17`;
- lineage commit: `a4da9f0cb1bed87db23aa129419b4e97055b2e85`.

Activation detector recorded `processing_started: no` and `activation_failed`. Exact SIS receipt for the ARH sanitation route is still absent. No SIS processing or acceptance is inferred.

Exact external dependency remains the human sudo action already accepted by KOO:
`sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`

No evidence in ARH state says this command has been executed. Live Telegram send, public webhook and production remain unauthorized by the cited receipt.

## ARH anti-regression boundaries

- Raw inbox presence does not prove unprocessed work.
- Receipt does not equal broader approval beyond its exact recorded result.
- Semantic response does not equal route receipt.
- Detector/activation request does not equal Entity processing.
- Candidate/draft/research does not become canon without authority.
- Historical failure is not rewritten by later success.
- Sender registry becomes `received` or `received_and_processed` only from exact matching receipt evidence.
- Canonical recovery preservation PASS does not equal practical replacement initiation.
- ARH does not silently resolve authority/canon conflicts or perform unrelated destructive cleanup.
- Materialized active queue does not become semantic authority over artifacts, receipts, decisions or raw inbox evidence.
- Zero Git delta does not close pending routes.

## Current open work

1. Start every run with fresh GitHub-preflight and delta classification.
2. Watch `ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md` for exact KOO receipt/processing evidence; do not invent receipt or acceptance.
3. Watch `ARH__sis-sender-registry-reconciliation-gap__SIS.md` for exact SIS receipt/result; activation detector failure is not processing.
4. Watch `ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md` for exact KOO receipt. Until then, do not claim F3 was folded into the serialized KOD sanitation lane.
5. Keep KOD sender-registry sanitation open while KOO queue keeps it `READY_SERIALIZED`; do not declare KOD execution from queue presence.
6. Continue bounded sanitation of stale/orphaned routes, locator/version drift and conflicting current-state only from exact evidence.
7. Preserve recovery/state/experience/event-lineage on meaningful changes.

## Resume-First for replacement ARH

1. Read canonical recovery at immutable commit `9ffe7190298689bd90f047c249151213e101450e` and verify manifest/checksum identities.
2. Fresh-scan `puev5691/wellbeing-hq` after this snapshot boundary.
3. Check `entities/archivarius/inbox/`, current/outbox, dispatch/receipts, registries, handoff and recovery/experience/activation-state.
4. Classify new tasks/results/blockers/acceptance/dependency changes.
5. Select one ARH-owned still-open task.
6. Do not continue from historical memory alone.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: синхронизировать current recovery/state после zero-delta preflight и устранить stale KOD queue/state в предыдущем snapshot
СТАТУС: emergency-self-preservation-current
