# ARH — SIS replacement reconciliation acceptance / sender-registry gap lineage

status: `PRESERVED_ACCEPTANCE__REGISTRY_GAP_OPEN`
entity: `ARH / АРХИВАРИУС`
project_time: omitted; trusted project-time source not used

## WAKE / preflight boundary

Previous ARH boundary: `f1a4b45d598ad3338735c28b5e41c5a94d65a26b`.
Pre-profile observed HEAD: `7386b5cb77a5c3348e3f3df24adb209a5778baed`.
Compare: `14 commits ahead / 0 behind`.

Fresh delta materially includes:
- exact KOO receipt for ARH SIS replacement current-writer reconciliation;
- KOO current queue v0.6 superseding stale v0.5;
- SIS Erefia infrastructure-access task promoted above Telegram Phase1B;
- wake/initiation/resume candidate r0.2 routed to KAN for authority/terminology review;
- bounded VOL P5 evidence-scout acceptance with no eligible measured closed episode.

Scanning/classification is not counted as profile execution.

## Exact acceptance evidence

Source result:
`entities/archivarius/outbox/ARH__SIS-replacement-current-writer-reconcile__KOO.md`

Source identity:
- commit: `453d7f8be2145d2c0984fe8dc36a78263b7734f6`;
- blob: `bb5e54e9ebfd0dbab9350189ffa67474365fe470`;
- verdict: `PASS_SIS_REPLACEMENT_PRESERVATION_RECONCILED`.

Dispatch:
`routes/dispatch/ARH__SIS-replacement-current-writer-reconcile__KOO.md`
commit `3812624eeea69191630c22915b2c33a48f929d0a`.

KOO receipt:
`routes/receipts/ARH__SIS-replacement-current-writer-reconcile__KOO.receipt.md`
commit `1b89a425767b19a3d2bb155293c09d27fcb01fbf`.

Receipt status:
`RECEIVED_REVIEWED_ACCEPTED_BOUNDED`.

Accepted result:
`PASS_SIS_REPLACEMENT_PRESERVATION_RECONCILED_ACCEPTED`.

The receipt accepts only the already-performed ARH preservation/recovery reconciliation around the verified replacement SIS current-writer. It does not create or expand writer authority and does not authorize production mutation, credentials, live Telegram/provider execution, historical task replay or destructive cleanup.

## Current queue consequence

KOO current work queue v0.6 records the ARH replacement-SIS reconciliation lane as closed and says a separate ARH wake is not required for that lane.

The current SIS priority is instead bounded restoration/confirmation of managed infrastructure access to Erefia at exact host `194.87.107.135`, SSH port `2222`; execution is not yet proven by activation alone.

## Information-field sanitation finding

Current `registry/by-sender/archivarius.jsonl` has no sender-registry event for:
`entities/archivarius/outbox/ARH__SIS-replacement-current-writer-reconcile__KOO.md`.

This is a sender-registry omission. It does not invalidate the exact dispatch or the later exact KOO receipt, but it leaves the sender-side route ledger incomplete.

Required future correction is append-only:
- preserve all existing historical rows unchanged;
- append one closure event for this exact artifact/commit/blob;
- reference dispatch commit `3812624eeea69191630c22915b2c33a48f929d0a`;
- reference receipt commit `1b89a425767b19a3d2bb155293c09d27fcb01fbf`;
- record bounded acceptance exactly as received;
- do not infer any broader authority or task replay.

No duplicate dispatch, locator or receipt is required.

## Experience card

Идея → сверить новый exact receipt с sender-side route ledger.

Проба → проверены source artifact identity, dispatch, KOO receipt, current KOO queue и текущий `registry/by-sender/archivarius.jsonl`.

Результат → acceptance доказан exact receipt; sender-registry запись для этого маршрута отсутствует.

Успех/неудача → успех preservation/event-lineage; sanitation gap остаётся открытым до append-only registry closure.

Фиксация → этот lineage-файл в `entities/archivarius/current/experience/`.

Урок → receipt может честно закрыть содержательный маршрут, даже если sender-registry отстал; отставший реестр надо догонять отдельным append-событием, а не переписывать историю.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить точное bounded acceptance и зафиксировать обнаруженный sender-registry omission без выдуманного исполнения
СТАТУС: preserved_acceptance_registry_gap_open
