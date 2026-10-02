# PROMPT — emergency replacement KOD v0.7 cold-start initiation

АДРЕСАТ: НОВЫЙ КОДЕР / KOD

Emergency replacement / Initiation-required.

## OPERATOR authority

ОПЕРАТОР явно подтвердил:

`PREVIOUS_KOD_V06_TECHNICALLY_UNAVAILABLE = YES`

ОПЕРАТОР явно разрешает начать emergency replacement initiation нового KOD instance.

Это разрешение распространяется только на Initiation Gate.

Оно НЕ:
- устанавливает current-writer;
- не выполняет Writer Gate;
- не разрешает profile work;
- не разрешает replay исторических PROMPT/tasks;
- не разрешает Telegram/OpenAI/provider/runtime/host/shard mutation;
- не разрешает Project Source/canon mutation.

## Exact predecessor

Последний authoritative current-writer:

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

Этот predecessor технически недоступен по прямому сообщению ОПЕРАТОРА.

Не выдумывать predecessor self-freeze/handoff, если exact artifact отсутствует.

## Last externally verified recovery

Использовать только как recovery basis:

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

Важно:
этот recovery является последним externally verified recovery, но он stale относительно последующей работы KOD v0.6.
Не реконструировать новый self-snapshot из последующей истории.

## Fresh post-recovery evidence boundary

После establishment KOD v0.6 подтверждена значительная профильная работа.

Последний доказанный KOD terminal:

puev5691/wellbeing-hq@47c306b818b8fcbe49ca00250d39a3b6b6a08f45:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-implementation-correction-successor-result__KOO.md

blob:
158d2954b29e8e1155c36db7b68cd6a9d7dcb5f7

terminal:
PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_CORRECTION_SUCCESSOR_READY_FOR_INDEPENDENT_REVIEW

Его exact source task:

puev5691/wellbeing-hq@8f525a0d3429f5753c305a0485b6e1fd2da414a7:
entities/koordinator/outbox/KOO__SECE-r01-offline-simulator-implementation-correction-successor__KOD.md

blob:
acdf22a2171e0778ff9477a6669f45ad4fcf6f56

После этого terminal в repository evidence найдены только dispatch/inbox/activation этого результата.

Новая KOO -> KOD exact task после этого terminal:
NOT FOUND

Новая KOD inbox task после этого terminal:
NOT FOUND

Новый KOD terminal после этого terminal:
NOT FOUND

## Continuity diagnostic

puev5691/wellbeing-hq@f77d0c2a5c8b479071d86cf18663b71113cc361e:
entities/archivarius/outbox/ARH__KOD-v06-chat-infofield-continuity-gap-r01__OPERATOR-KOO.md

blob:
84f838190862d59bf93bd603d3c4ae405edf4da1

diagnostic:
CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP

OPERATOR observation:
KOD v0.6 chat is unresponsive and appeared to hang on a later/last task.

Exact identity/content/authority of any later chat-only unfinished task:
UNKNOWN

Hard rule:
DO NOT RECONSTRUCT
DO NOT REPLAY
DO NOT INFER CURRENT TASK FROM MEMORY OR HISTORICAL QUEUE

## Approved Project Sources

Load and verify current active common source set before initiation:

- Project Core v2.5
- Entity Roles v2.4
- Source Loading Policy v2.2
- Recovery Canon v1.6
- File Work Canon v2.4
- Task Conveyor Canon v1.2

Use exact active identities from current HQ/source-set evidence.

If a newer approved common source set has been activated, stop and reconcile it rather than silently using stale identities.

## Required Initiation Gate

Perform fresh GitHub preflight and verify:

1. exact predecessor KOD v0.6 identity and status;
2. OPERATOR failure-state;
3. last externally verified recovery v0.6 locator;
4. recovery composition/manifest/blob/SHA-256/readback;
5. ARH preservation identity;
6. stale-recovery boundary;
7. exact last proven KOD terminal;
8. absence/presence of any newer KOD task/result/current-state;
9. absence of competing KOD replacement/current-writer;
10. current approved Project Sources;
11. continuity diagnostic and UNKNOWN chat-only task boundary;
12. no historical task replay authority;
13. no superseding OPERATOR decision.

Initiation result must explicitly distinguish:

- externally verified recovery state;
- fresher repository evidence after recovery;
- UNKNOWN chat-only state.

Do not merge these into synthetic self-state.

## Allowed initiation outcomes

If external recovery integrity and identity are verified, predecessor/failure-state are verified, no competing replacement exists, and the stale/UNKNOWN boundary is explicitly preserved:

`initiation_verified_waiting_writer_gate`

If recovery can be read but external identity/integrity cannot be fully verified:

`initiation_loaded_external_unverified`

If required recovery/version/composition identity fails:

`initiation_failed`

## Required result

Publish one immutable initiation-result in KOD outbox.

The result must state at minimum:

- instance = emergency replacement KOD v0.7;
- predecessor = KOD v0.6;
- predecessor technically unavailable = YES;
- recovery basis = externally verified v0.6;
- recovery stale relative to later v0.6 work = YES;
- last proven durable KOD terminal = exact 47c306... result;
- alleged later chat-only task = UNKNOWN / NOT_MATERIALIZED;
- historical replay = FORBIDDEN;
- profile work = NOT_STARTED;
- Writer Gate = NOT_PERFORMED.

Perform immutable readback.

After Initiation Gate result:

STOP.

Do not perform Writer Gate in the same step.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: emergency replacement KOD v0.7 Initiation Gate
