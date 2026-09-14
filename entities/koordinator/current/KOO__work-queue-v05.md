# KOO — рабочая очередь v0.5

status: `ACTIVE_RECONCILED_QUEUE`
canon: `no`
project_time: omitted; trusted project-time source not used

## Fresh preflight basis

Fresh HQ preflight before this orchestration pass observed HEAD:
`08b254eb780e1e5bfda54baec96e48f5094822fb`.

Material newer state:
- replacement SIS current-writer established and immutable readback recorded;
- VOL Russian P2+P4 result arrived for KOO review;
- KOD E1 and SHD WBN/TERA2 readiness tasks remain addressed but not proven started;
- no newer KOD or SHD result exists after those task commits.

## READY_PARALLEL

### O1 — KOD / КОДЕР

State: `READY_WAKE_MANUAL_RESUME_REQUIRED`.

Exact input:
`entities/koder/inbox/KOO__info-entry-static-preview-E1-fix-v03__KOD.md`

task commit:
`ed84c8c379dc1ba450310fd6be46b2fa30e30fad`

Purpose: close only Static Preview E1 byte-reproducibility defect.

Activation evidence remains:
- `activation_requested: yes`;
- `processing_started: no`;
- exact Entity-chat resume unsupported by current adapter.

Stop condition: return exact KOD result/package through Exchange Gate.

### O2 — SHD / ШАРДОВИК

State: `READY_WAKE_MANUAL_RESUME_REQUIRED`.

Exact input:
`entities/shardovik/inbox/KOO__wbn-tera2-launch-readiness-r01__SHD.md`

task commit:
`9d916dcf0e14d7926986784a8ed23e52da5d2dd4`

Purpose: bounded read-only WBN/WBNP/TERA2 launch-readiness reconciliation on MAZHOR/lab-01.

Activation evidence remains:
- `activation_requested: yes`;
- `processing_started: no`;
- exact Entity-chat resume unsupported by current adapter.

No node launch, production mutation or secrets.

### O3 — SIS / СИСАДМИН

State: `READY_WAKE`.

Replacement current-writer:
`entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
commit `2926908f9843a8c325a975dcf5180fa51baef2c5`
blob `6590555d95275d18f4eee4478dad0f80ec9b260f`.

Exact input:
`entities/sisadmin/inbox/KOO__telegram-phase1b-resume-gate-r04__SIS.md`

task commit:
`88bfefeeb212bcd991a70cfcd15d4b242f14ce1f`

Purpose: fresh Phase1B resume gate after replacement; verify current host state and resume-aware v2 script without replaying historical v1 sudo action.

If interactive sudo is actually required, SIS must return one exact Termux block and stop in `WAITING_OPERATOR_EXACT_HUMAN_ACTION`.

No live Telegram, public webhook, production or credentials.

### O4 — ARH / АРХИВАРИУС

State: `READY_WAKE`.

Exact input:
`entities/archivarius/inbox/KOO__sis-replacement-preservation-reconcile__ARH.md`

task commit:
`aafd5aa7bbe226f27254fa172571b5c3f353a0bc`

Purpose: independently reconcile preservation/recovery registry state after verified SIS replacement current-writer establishment.

ARH does not create writer authority and does not execute SIS profile work.

## KOO_ONLY completed in this pass

VOL Russian P2+P4 research result:
`entities/volonter/outbox/VOL__hybrid-interaction-p2p4-pilot__KOO.md`
commit `078b16aa071d0df630c72f426e02b8834abb72fd`.

KOO receipt:
`routes/receipts/VOL__hybrid-interaction-p2p4-pilot__KOO.receipt.md`
commit `17d450ffa1f5a68c4c170a155553916e78871fa9`.

Verdict:
`ACCEPTED_BOUNDED_P2P4_RESEARCH__P5_BLOCKED_NO_MEASURED_EFFECT`.

No VOL wake follows automatically.

## WAITING_DEPENDENCY

### WEB
Waits for KOD E1 corrected package. After KOO accepts that result, create a new exact WEB v0.3 narrow recheck task; do not reuse the old v0.2 task blindly.

### SHT
Waits for KOD activation-lineage schema F1/F2 correction and then a bounded org-fit recheck.

### KOD serialized successors
After O1 is closed and fresh preflight:
1. activation-lineage schema F1/F2 correction;
2. sender-registry sanitation, append-only, including ARH F3.

Source queue:
`entities/koordinator/current/KOO__kod-serialized-queue-v03.md`.

These are not RUNNING and should not be started concurrently with O1 by the same KOD current-writer.

## WAITING_OPERATOR / EXTERNAL

### Anthropic live D0
State:
`WAITING_OPERATOR_ACCOUNT_BILLING_KEY_AND_EXPLICIT_LIVE_D0_AUTHORIZATION`.

Technical adapter/transport are ready, but no live call is authorized.

### Entity Runner
State:
`BLOCKED_EXTERNAL`.

Only host/runtime readiness is accepted. Provider entitlement/billing, Agent/Environment, API-key validity and provider-side execution remain unproved.

## HOLD_ROUTING

### VOL → SHK participant capability source

Addressed input exists:
`entities/shkola/inbox/VOL__participant-capability-testing-source__SHK.md`
commit basis `db8aec242c236e62395bb7f77662045857cf627f`.

Current general approved role source defines `ШКОЛА` as a functional area, not a distinct current-writer Entity `SHK` with an execution authority boundary.

Therefore orchestrator must NOT invent a `SHK` chat wake from the folder name. This input remains `HOLD_ROUTING` until an active School governance source resolves the exact recipient Entity.

## Conflict graph

O1 KOD, O2 SHD, O3 SIS and O4 ARH are safe in parallel:
- different profile owners/current writers;
- different primary mutable targets;
- SHD is read-only;
- KOD edits its package/result lane only;
- SIS is bounded to Phase1B non-production host gate;
- ARH edits preservation/recovery bookkeeping only;
- no shared production mutation is authorized.

Hard serialization remains inside KOD only.

## Orchestration transition rules

For every returned result:
1. fresh HQ preflight;
2. verify exact immutable result identity;
3. KOO accepts/fails bounded result;
4. recompute conflict graph;
5. materialize the next exact task before any downstream wake.

Never treat inbox placement, dispatch, activation request or timer firing as `RUNNING`.

If current adapter cannot resume an exact Entity chat, orchestrator state must remain `READY_WAKE_MANUAL_RESUME_REQUIRED`, not `RUNNING`.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать исполнимую очередь после SIS replacement handoff и новых VOL результатов
СТАТУС: active_reconciled_queue_v05
