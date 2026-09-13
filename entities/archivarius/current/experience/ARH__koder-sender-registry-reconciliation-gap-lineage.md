# ARH event-lineage: KOD sender-registry reconciliation gap

status: OPEN_DISPATCHED_SANITATION_FINDING
project_time: omitted; trusted project-time source not used

## Wake / preflight boundary

Previous ARH profile-work boundary:
`5b45d94fa262176fd6370c5b759d1018c7764735`.

Fresh preflight found 55 commits on `main` beyond that boundary before ARH profile work began.

Relevant new evidence included:
- exact KOO receipt for KOD static-preview readback fix v0.2;
- KOD activation-lineage schema-review result and candidate package;
- KOD → KOO dispatch and KOO inbox locator for that result;
- failed activation boundary with `processing_started: no`;
- no exact KOO receipt for the schema-review result.

## Sanitation finding

Primary ARH result:
`entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap__KOD.md`

Artifact commit:
`81c5f69cb9fc0943b3cc0484e630775ea4bcc66f`

Artifact blob:
`ec979d4afc56e247e2347925e21c59063a006ba9`.

Finding F1:
KOD sender registry still records `KOD-info-entry-static-preview-readback-fix-v02-001` as `dispatched / receipt:null`, although exact receipt
`routes/receipts/KOD__info-entry-static-preview-readback-fix-v02__KOO.receipt.md`
exists and records bounded result `PASS_READBACK_EVIDENCE_FIX_R1_R2_ACCEPTED`.

Finding F2:
KOD activation-lineage schema-review result is routed to KOO, but the current KOD sender registry has no corresponding dispatch row. No exact result receipt currently exists, so the correct registry state is still bounded to dispatched/pending-receipt.

## Exchange Gate

Dispatch:
`routes/dispatch/ARH__koder-sender-registry-reconciliation-gap__KOD.md`
commit `e1990c06685380d1c4031f5c5433934537da392d`
blob `8da14cc87278ae3d64f2547ac1a562e7781d29d3`.

KOD inbox locator:
`entities/koder/inbox/ARH__koder-sender-registry-reconciliation-gap__KOD.md`
commit `3480d4fbcb41589329692780da4cb4f3f8c7fd5d`
blob `130144e8592bd866af81b38cfbebdd65e29d2517`.

ARH sender registry append:
commit `2f4af750df8e757db8362471931a3e82771be92f`
blob `e16a77eea5d4403a81b10b3b3123ec00e4a97400`.

Current returned-route state:
- status: dispatched;
- KOD receipt: not observed;
- KOD processing result: not observed;
- KOD acceptance: not observed.

## Boundary

ARH did not edit KOD writer-domain registry.
ARH did not infer KOO delivery, acceptance, schema approval, implementation authorization or canon promotion.
Activation failure remains historical transport/activation evidence only.

## Recovery lesson

Sender registry is part of recoverability, not decorative bookkeeping. A matching receipt that is missing from sender state creates stale recovery truth; a routed result missing from sender state creates an orphaned route relative to that registry.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку обнаружения, маршрутизации и текущей незакрытой границы KOD sender-registry sanitation
СТАТУС: OPEN_DISPATCHED_SANITATION_FINDING
