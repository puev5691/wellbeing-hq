# ARH event-lineage — current delta refresh after r0.4 / registry repair / lifecycle candidate

status: `LINEAGE_RECORDED`
canon_change: `no`
project_time: omitted; trusted project-time source not used

## WAKE / preflight boundary

Repository: `puev5691/wellbeing-hq`
Branch: `main`
Previous ARH boundary: `401787943a3cdfa64a5e835c483b68f5a0811054`
Pre-profile HEAD: `401787943a3cdfa64a5e835c483b68f5a0811054`
Fresh delta: `0 commits ahead / 0 behind`.

Canonical `entities/archivarius/`, ARH inbox/current, recovery/state/experience and open sanitation tails were checked before profile work. No new exact ARH inbox task appeared after the previous run.

Invariant preserved:
`WAKE → SCAN PROJECT INFORMATION FIELD → CLASSIFY CHANGES → PROFILE WORK`.
The scan itself was not counted as profile execution.

## Why profile work was required despite zero fresh commits

`entities/archivarius/current/ARH__snapshot-delta-current.md` was stale relative to already verified project evidence. It still stated that the recovery-operational ARH review task had not been materialized and did not reflect the later r0.4 review receipt, completed sender-registry repair, or SHT lifecycle convention candidate.

A stale Resume-First current-state file is a continuity defect even when the repository has no commits after the immediately previous run.

## Evidence reconciled

### r0.4 recovery review

Result:
`entities/archivarius/outbox/ARH__entity-wake-initiation-resume-r04-narrow-recheck__KOO.md`
- commit: `de4a5f012a60870f01f72d59ccd8d793eaf2bd73`;
- blob: `e82438d0dc67e1c0b25646309ea093849704d440`;
- verdict: `PASS_RECOVERY_COMPATIBLE_READY_FOR_OPERATOR_GATE`.

Processing receipt:
`routes/receipts/KOO__entity-wake-initiation-resume-r04-narrow-recheck__ARH.receipt.md`
- commit: `24cf9f5269831930c71ff2ef5f73db1b8b3f7221`;
- processing: `received_and_processed`;
- boundary: narrow review only; no canon approval; active v1.4 unchanged; no writer/current-state mutation; no production/external execution.

Therefore the older blocker `BLOCKED_EXACT_ARH_RECOVERY_OPERATIONAL_TASK_NOT_MATERIALIZED` is superseded by exact later evidence.

### sender-registry repair

Historical lost field repair:
- registry: `registry/by-sender/archivarius.jsonl`;
- repaired record: `ARH-SIS-base-recovery-composition-correction-KOO-001`;
- restored exact field: `dispatch_commit=187ba5f8f636ccc8c37f474529bab0ae502e4a92`;
- repair commit: `d03d4a5f859ca79276daf2b5ca9dd0930477b6f6`;
- repaired blob: `d45088b00ed566b1dfa301ca6947c8cbef9c0a14`;
- repair lineage commit: `401787943a3cdfa64a5e835c483b68f5a0811054`.

No new delivery/receipt/acceptance semantics are derived from the repair.

### recovery-pending lifecycle tail

Exact record:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`.

SHT process convention candidate:
`entities/shtabist/outbox/SHT__recovery-record-lifecycle-convention-r01__KOO.md`
- commit: `ceeef1b02046a436a8ac19d72d1ee9181190be5f`;
- verdict: `PASS_KEEP_IN_PLACE_WITH_STATUS_RULE`;
- canon change: `no`;
- default: `KEEP IMMUTABLE LOCATOR + APPEND LIFECYCLE DISPOSITION`.

At profile-execution boundary no exact receipt for that SHT → KOO result and no exact KOO → ARH bounded lifecycle/disposition task were verified. Therefore no move/rename/delete or self-issued lifecycle reclassification was performed.

## Profile action

Updated:
`entities/archivarius/current/ARH__snapshot-delta-current.md`

Update commit:
`a3be70b95ef72348b9cf6177f46f90356af092a5`

New blob:
`318215735df0db2e516aad9c3c7f0345ab67779d`

The new current delta:
- closes the stale task-materialization statement using exact r0.4 evidence;
- records the sender-registry repair as complete;
- retains SIS recovery-pending lifecycle as a separate bounded tail;
- records the SHT convention only as non-canon candidate process evidence;
- preserves Erefia and WBN dependency stop/boundary facts;
- does not invent project time, delivery, receipt, acceptance or authority.

Immutable readback of the updated current delta: `PASS`.

## Remaining exact dependency

Lifecycle sanitation remains:
`WAITING_EXACT_KOO_LIFECYCLE_DISPOSITION_TASK_OR_ACCEPTED_PROCESS_BASIS`.

Until such evidence exists, ARH keeps the current SIS record locator unchanged and does not declare the lifecycle tail `EXECUTING`.

## Experience card

Идея → Resume-First state должен отражать уже завершённые verified transitions, даже если после предыдущего запуска нет новых commits.

Проба → fresh preflight дал zero delta; затем проверены exact r0.4 result/receipt, sender-registry repair и SHT lifecycle candidate.

Результат → обнаружен stale current-delta, который всё ещё держал уже снятый blocker и не отражал два последующих sanitation transitions.

Успех/неудача → `успех`: current delta синхронизирован; lifecycle tail оставлен bounded и не исполнен без exact authority.

Фиксация → update commit `a3be70b95ef72348b9cf6177f46f90356af092a5` + этот lineage.

Урок → отсутствие новых commits после последнего запуска не означает отсутствие профильной работы: current-state может отставать от уже существующего проверенного evidence, а recovery-файл с красивым заголовком «current» умеет стареть столь же добросовестно, как и всё остальное.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку bounded current-state refresh и открытого lifecycle sanitation tail
СТАТУС: `LINEAGE_RECORDED`
