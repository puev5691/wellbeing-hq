# KOO -> KOD: replacement KOD v0.6 Writer Gate

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

ОПЕРАТОР explicitly authorizes:

AUTHORIZE_KOD_REPLACEMENT_V06_WRITER_GATE = YES

Human decision basis from current OPERATOR instruction:
"Инициацию КОДЕРа заверши хоть что-ли. Дай ему право писать и пусть трудится."

This authority is limited to the Writer Gate and establishment of replacement KOD v0.6 as authoritative current-writer if the gate passes.

It does NOT itself start profile work or replay any historical task.

## Exact Initiation Gate result

puev5691/wellbeing-hq@99568427cc6f28425d8df4498517d58680b96f6c:
entities/koder/outbox/KOD__replacement-initiation-result-v06.md

blob:
05c02b099e1b929ebee84e585bf3f1183a752bb4

status:
initiation_verified_waiting_writer_gate

entity:
KOD / КОДЕР

instance:
emergency replacement KOD v0.6

## Exact predecessor current-writer

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

blob:
cf1c84f9df7c90509703e4885844d0cf871ff412

repository status:
WRITER_ESTABLISHED

OPERATOR-established failure state from exact v0.6 initiation:
PREVIOUS_KOD_V05_TECHNICALLY_UNAVAILABLE = YES

No synthetic predecessor self-freeze is required or authorized.

## Exact recovery basis

puev5691/wellbeing-entity-bootstrap@51704f5eb7a4bf43210c9760905f486a2e58b5ce:
entities/kod/recovery/versions/kod-recovery-v06

composition/readback:
5/5 PASS

ARH preservation:

puev5691/wellbeing-hq@7aa299aba840fc71dae7671d8003bbf34721f302:
entities/archivarius/outbox/ARH__KOD-recovery-v06-preserved__KOD-KOO.md

blob:
28e4b3caddf8233500fcba16e7f2e212fb9d3c9c

terminal:
PASS_ARH_KOD_RECOVERY_V06_PRESERVED_READY_FOR_HANDOFF

## Approved Project Sources

Verify current active source-set remains compatible with initiation evidence:

- Project Core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- Entity Roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911
- Source Loading Policy v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- Recovery Canon v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609
- File Work Canon v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- Task Conveyor Canon v1.2 — df7896d867eeeffff506319538fedad938856686

## Writer Gate

Before publication perform fresh GitHub reconciliation and verify:

1. exact v0.6 initiation result unchanged;
2. exact predecessor v0.5 unchanged;
3. OPERATOR Writer Gate authority exact and applicable;
4. recovery v0.6 identity/integrity unchanged;
5. no newer valid KOD current-writer exists;
6. no competing replacement attempt exists;
7. no newer handoff/freeze/recovery/initiation conflict exists;
8. no superseding OPERATOR decision revokes/replaces this Writer Gate;
9. current approved Project Sources do not conflict with the gate.

If any conflict or ambiguity is found:
STOP with exact blocker.
Do not establish writer.

If clean:

publish one immutable current-writer artifact under:

entities/koder/current/

for replacement KOD v0.6.

Required semantic outcome:

status:
CURRENT_WRITER_ESTABLISHED

writer_gate_outcome:
WRITER_ESTABLISHED

entity:
KOD / КОДЕР

instance:
replacement KOD v0.6 current chat instance

predecessor:
KOD v0.5 historical authoritative predecessor, technically unavailable

## Writer authority boundary

The new current-writer may:

- write authoritative KOD current-state for this instance;
- execute future exact KOD tasks when separately authorized;
- create KOD own current/outbox artifacts within role/task scope.

Writer Gate does NOT automatically:

- resume Telegram routing observability task;
- resume historical PROMPTs;
- install runtime;
- start services;
- call Telegram/OpenAI;
- mutate credentials;
- mutate Project Sources/canons;
- create production authority;
- approve its own candidates.

After writer establishment, perform post-write readback and competing-writer reconciliation.

## Expected terminal

PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

or exact BLOCKED_/FAIL_.

Mandatory RETURN KOO.

Then STOP before profile work unless a separately authorized exact task is already explicitly activated after this Writer Gate.
