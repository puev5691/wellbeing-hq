# KOO current active queue r1.06

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
project_time: omitted

## JOURNAL-FEED V1.3 DECISION GATE

KAN terminal:
`PASS_KAN_JOURNAL_FEED_R02_NORMATIVE_READY_FOR_KOO_GATE`

KAN commit:
`603c6a4fb02733d8e807bd6d7f2c5d3434f0ba92`

Delta candidate:
`entities/kancelar/outbox/KAN__task-conveyor-v1_3-journal-feed-r02-delta-candidate__KOO.md`

delta commit:
`d06773bbd91f1105e6c2657f6a3ccf8f51748e00`

Target successor:
`task-conveyor-canon-v1_2-approved.md → task-conveyor-canon-v1_3-approved.md`

Decision gate:
`entities/koordinator/outbox/KOO__task-conveyor-v1_3-gate__OPERATOR.md`

gate commit:
`984711364e2902e61500ed43a4db183cbf92fffe`

Requested token:
`APPROVE_TASK_CONVEYOR_CANON_V1_3_INCREMENTAL_JOURNAL_FEED`

v1.3 remains NOT ACTIVE until explicit approval + materialization + source activation/readback barrier PASS.

Required initial state after activation:
`last_scanned_commit + pending_candidate_refs + last_red_journal_sweep_ref`

Initial cursor must equal exact activation/reconciliation boundary; no historical full scan.

## OTHER ACTIVE WORK

Booster-v2 shape-binding correction lane remains separate and is not altered by this decision gate.

## NEXT

`WAITING_OPERATOR_TASK_CONVEYOR_V1_3_DECISION`