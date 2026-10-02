# PROMPT — KOO fresh reconciliation after KOD v0.7 replacement + continuity-gap handling

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

ОПЕРАТОР активирует NEW exact coordination task:

1. выполнить fresh task-conveyor reconciliation для нового KOD v0.7;
2. отдельно разобрать continuity defect:
   CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP;
3. не реконструировать и не replay возможную chat-only незавершённую задачу predecessor KOD v0.6;
4. определить следующий exact authorized KOD task только из текущего durable information field и явных решений ОПЕРАТОРА;
5. определить, какой governance/context-engine шаг нужен для предотвращения повторения дефекта.

## Current KOO writer

puev5691/wellbeing-hq:
entities/koordinator/current/KOO__replacement-current-writer-r10.md

blob:
8416e945418a4a86764edafbbd06682f6c84682b

status:
WRITER_ESTABLISHED

## New KOD current-writer

puev5691/wellbeing-hq@efd030dccc5ba96f61d4a45e1f19705a18fee98a:
entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

Writer Gate result:

puev5691/wellbeing-hq@269a2c4cb42bc59e789b1bd1e9d89a553b1f4d93:
entities/koder/outbox/KOD__emergency-replacement-writer-gate-v07-result__KOO.md

blob:
c33b4d8d49cef4a98ca33e4e49744330dfe112a4

terminal:
PASS_KOD_EMERGENCY_REPLACEMENT_V07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

KOO inbox locator:

puev5691/wellbeing-hq@a7afeedb182a8beb375ee76cb312938164cf6b8d:
entities/koordinator/inbox/KOD__emergency-replacement-writer-gate-v07-result__KOO.md

status:
dispatched_pending_receipt

Do not treat inbox placement as receipt/acceptance/processing proof.

## Predecessor continuity boundary

Previous writer:
KOD v0.6

failure-state:
PREVIOUS_KOD_V06_TECHNICALLY_UNAVAILABLE = YES

Last externally verified recovery:

puev5691/wellbeing-entity-bootstrap@51704f5eb7a4bf43210c9760905f486a2e58b5ce:
entities/kod/recovery/versions/kod-recovery-v06

Last proven durable KOD terminal:

puev5691/wellbeing-hq@47c306b818b8fcbe49ca00250d39a3b6b6a08f45:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-implementation-correction-successor-result__KOO.md

blob:
158d2954b29e8e1155c36db7b68cd6a9d7dcb5f7

terminal:
PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_CORRECTION_SUCCESSOR_READY_FOR_INDEPENDENT_REVIEW

After that terminal, repository evidence contained no newer:
- KOO -> KOD exact task;
- KOD inbox task;
- KOD terminal;
- KOD current-state artifact,

until emergency replacement work began.

## Continuity diagnostic

puev5691/wellbeing-hq@f77d0c2a5c8b479071d86cf18663b71113cc361e:
entities/archivarius/outbox/ARH__KOD-v06-chat-infofield-continuity-gap-r01__OPERATOR-KOO.md

blob:
84f838190862d59bf93bd603d3c4ae405edf4da1

diagnostic:
CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP

OPERATOR observation:
the KOD v0.6 chat became unresponsive and appeared to be working on a later task.

Exact identity/content/authority of that possible task:
UNKNOWN / NOT_MATERIALIZED

Hard boundary:
DO NOT RECONSTRUCT
DO NOT REPLAY
DO NOT INFER CURRENT TASK FROM MEMORY OR HISTORICAL QUEUE

## Required KOO action

Fresh-reconcile at least:

- current KOO writer;
- current KOD v0.7 writer;
- KOD v0.7 Writer Gate result;
- entities/koder/current/;
- entities/koder/inbox/;
- entities/koder/outbox/;
- entities/koordinator/outbox/*__KOD;
- routes/dispatch relevant to KOD;
- routes/receipts relevant to KOD;
- routes/activation relevant to KOD;
- current active queue/serialized KOD queue;
- OPERATOR decisions;
- supersession;
- current Project Sources/canon;
- terminal results newer than the last durable KOD terminal;
- continuity diagnostic.

Then distinguish:

A. exact new KOD task currently authorized and not already completed;
B. historical/completed/stale task;
C. unknown chat-only work;
D. governance/context-engine defect work.

Do not silently convert B or C into A.

If an exact KOD profile task is currently authorized:
- materialize exactly one NEW KOO -> KOD task;
- perform immutable readback;
- give OPERATOR one complete copy-paste PROMPT for KOD v0.7;
- STOP.

If no exact KOD profile task is currently authorized:
- return WAITING_EXACT_TASK;
- do not replay old work.

## Continuity-defect governance work

Separately determine the next authorized owner and exact task for the defect.

Evaluate at minimum these candidate invariants:

`NO_PROCESSING_BEFORE_DURABLE_TASK_BOUNDARY`

Meaning:
a significant task must have durable identity/authority/inputs/writer/task-state evidence before processing can be claimed started.

`NO_TERMINAL_STOP_WITHOUT_NEXT_CAUSAL_ACTION`

Meaning:
when a terminal/STOP leaves a required next human gate, the Entity must return one explicit next OPERATOR action or one complete PROMPT.

Also evaluate whether the Entity context/control engine needs an additional durable execution-state layer, for example:
- task_id / exact authority identity;
- writer identity;
- processing_started checkpoint;
- current execution step;
- last durable checkpoint;
- pending result locator;
- crash/replacement disposition;
- explicit UNKNOWN state for chat-only/unmaterialized work.

These are candidates for analysis, not automatically active canon.

Do not mutate Project Sources/canon unless separately authorized.

Return:
1. exact KOD task state;
2. exact next KOD step or WAITING_EXACT_TASK;
3. exact owner/task for continuity-defect analysis;
4. one complete OPERATOR PROMPT for the next manual activation, if needed;
5. stop condition.

---
КТО: ОПЕРАТОР через ARH
ДЛЯ ЧЕГО: KOD v0.7 post-replacement reconciliation + continuity-gap governance routing
