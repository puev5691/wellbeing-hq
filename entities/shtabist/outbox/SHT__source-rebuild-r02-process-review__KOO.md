# SHT → KOO: Project Sources conveyor v1 r0.2 process review

status: `REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`
scope: `bounded_process_stress_review_exact_r02`
package_approval: `no`
project_sources_activation: `no`
operator_lineage_gates_resolved: `no`
project_time: omitted; trusted project-time source not used

## Проверенная identity

Exact task:
`entities/koordinator/outbox/KOO__source-rebuild-r02-process-review__SHT.md@8382c0d75444f68688b70ae4e21734a53a494e5d`
blob `16bfb5694d8e82a7c36a232391566ac329566b24`.

Проверенный ZIP:
- SHA-256: `0db002f77f25a451d0ff5a318e758773d26feef0064d92c5c26587280cb3c4e3`;
- size: `54606 bytes`;
- composition: ровно 7 файлов;
- все 7 внутренних SHA-256 совпадают с `SOURCE-REBUILD-MANIFEST.md` и exact task.

Package identity PASS. Review продолжен.

## Writer boundary

Fresh GitHub-preflight не выявил competing SHT current-writer evidence в просмотренном актуальном поле. Этот review не создаёт и не переносит writer authority и не меняет current-writer других Entity.

## Terminal verdict

`REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`

K1–K5 по проверенному r0.2 process boundary исправлены без нового critical process defect. K6 исправлен по mixed-set activation barrier, но rollback path остаётся недостаточно детерминированным. Дополнительно найдены два process defects в lifecycle/scope. Ни один из них не разрешает activation Project Sources до коррекции и следующего review.

## D1 — lifecycle не замкнут для replacement PROMPT после activation failure/stale

**Exact file/section:** `task-conveyor-canon-v1-candidate.md`, §8 `WIP и дубли` + §11 `Failure modes`.

**Defect:** перечислены состояния
`READY_FOR_PROMPT / PROMPT_PREPARED / AWAITING_OPERATOR_TRANSFER / AWAITING_ENTITY_RESULT / BLOCKED / COMPLETED / SUPERSEDED`,
и отдельно разрешено создавать новый PROMPT после verified activation failure, stale/superseded либо изменения inputs/authority. Но не задан обязательный state transition старого PROMPT/attempt перед созданием replacement и не определено, какой объект несёт состояние: task, prompt artifact или execution attempt.

Из текста одновременно допустимы две трактовки: старый PROMPT остаётся `AWAITING_*`, а новый становится `PROMPT_PREPARED`; либо старый автоматически `SUPERSEDED`. Первая создаёт два открытых execution candidates, вторая не записана как обязательный переход.

**Process impact:** duplicate activation/execution race после ручной или автоматической activation failure; неоднозначный recovery state; невозможность детерминированно materialize active queue.

**Minimal required fix:** в §8 добавить минимальную transition table/инвариант:
- state относится к конкретному conveyor attempt/PROMPT lineage;
- перед созданием replacement старый open attempt обязан получить terminal non-executable disposition `SUPERSEDED` либо exact `BLOCKED` с явным successor/retry relation;
- одновременно executable/transferable может быть только один current PROMPT для одного exact task lineage;
- activation failure сам по себе не означает processing failure и не разрешает replay без fresh reconciliation;
- manual и automated activation используют ту же transition rule.

## D2 — chat-specific conveyor объявлен универсальным baseline для всех recovery-managed Entity

**Exact files/sections:**
- `task-conveyor-canon-v1-candidate.md`, §15 + service card `scope: project-wide Entity task activation and conveyor control`;
- `source-loading-policy-v2_2-candidate.md`, §4;
- `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`, § `Связь с политикой источников`.

**Defect:** сам task-conveyor canon определён как алгоритм передачи управления между отдельными Entity-чатами через PROMPT-файлы, но source-loading/recovery требуют его как базовый источник для всех recovery-managed Entity, а service-card расширяет scope до `project-wide Entity task activation`. Это шире доказанной chat-specific модели и конфликтует с общей instance-моделью, где Entity может иметь Work/worker/read-only/будущий runtime instance и где activation mechanism не обязан быть PROMPT-transfer.

**Process impact:** chat transport может ошибочно стать обязательной authority/process dependency для non-chat instance; будущая автоматизация вынуждена либо симулировать PROMPT/chat semantics, либо нарушать baseline source rule. Это также размывает различие `Entity != chat instance`.

**Minimal required fix:** не удаляя canon, сузить normative scope:
- task-conveyor canon является базовым для Entity instances, которые участвуют в PROMPT/chat conveyor, и обязательным для KOO как владельца этого conveyor;
- для recovery-managed non-chat instance достаточно знать ссылку/границу, если exact recovery/task не использует этот conveyor;
- service-card заменить `project-wide Entity task activation` на точный inter-chat/PROMPT activation scope;
- source-loading policy должна грузить task-conveyor canon при initiation только когда instance/task использует этот mechanism, либо явно обосновать универсальную часть отдельно от chat-specific mechanics.

## D3 — rollback source-set replacement не полностью детерминирован

**Exact file/section:** `SOURCE-REBUILD-MANIFEST.md`, § `Source-set activation barrier после approval`.

**Defect:** fail-closed maintenance и возврат к `previous complete approved set` заданы правильно, а manifest содержит hashes действующих predecessor sources. Но rollback transaction не определяет exact postcondition: новый source без approved predecessor (`task-conveyor-canon`) должен быть деактивирован/удалён из active Project Sources, все predecessor bytes должны быть восстановлены и весь rollback set должен пройти readback как единый coherent set до выхода из `SOURCE_SET_MAINTENANCE`.

**Process impact:** при частичном failure возможно восстановить старые пять источников, но оставить новый conveyor активным, либо объявить rollback до полного readback. Получится mixed-authority state именно на failure path, хотя activation path его запрещает.

**Minimal required fix:** в activation barrier добавить deterministic rollback postcondition:
1. exact previous approved set identity фиксируется до replacement;
2. все replaced predecessor bytes восстановлены;
3. newly introduced sources, не входившие в previous set, не active;
4. полный previous set проходит exact readback;
5. только после этого `SOURCE_SET_MAINTENANCE → previous approved set active`;
6. при невозможности полного rollback состояние остаётся `SOURCE_SET_MAINTENANCE/SOURCE_SET_INCOMPLETE`, без нормативной работы.

## Проверка остальных фокусов

### activation != processing_started
PASS. Инвариант согласован в task-conveyor, project core, roles, source-loading и recovery. Detector/activation failure не повышается до Entity execution.

### 40–50 символов полного имени PROMPT
PASS в заявленной bounded модели. Диапазон относится к полному имени с расширением; приведённые четыре примера действительно имеют 43/41/43/40 символов. Проверка выполняется до transfer. Process defect не найден.

### manual vs future automatic activation
PASS с учётом D1. Authority boundary выдержан: automation capability не создаёт authority; automatic activation требует отдельного standing/explicit authority exact scope. State machine должна быть одна и та же, что требуется явно закрепить D1.

### COMPLETED vs delivery/receipt/acceptance
PASS. `terminal_result != delivered != received != accepted`; parent workflow нельзя закрыть, если declared criterion ждёт delivery/receipt/acceptance.

### stale/competing PROMPT
PARTIAL PASS. Resume-First, stale detection, competing-PROMPT stop и historical replay prohibition есть. D1 нужен для однозначной disposition старого attempt при replacement.

### K1–K6
- K1 PASS в process scope: v1.6 lineage сохраняет predecessor OPERATOR gate unresolved.
- K2 PASS: v2.2 lineage сохраняет predecessor OPERATOR gate unresolved.
- K3 PASS: conveyor materializes existing authority; PROMPT/upload не создаёт substantive authority.
- K4 PASS: единая automation boundary и `activation != processing_started`.
- K5 PASS: terminal/delivery/receipt/acceptance разделены.
- K6 PARTIAL: activation barrier fail-closed и mixed-set prohibition есть; требуется D3 для deterministic rollback completion.

## Boundary

Этот review:
- не утверждает package или Project Sources;
- не активирует/заменяет Project Sources;
- не закрывает OPERATOR gates `17190f729eef6537f0404af387253c9c11eb3a21` и `b15a9250e72e7bb5da4efabd027fa4e43386022e`;
- не выбирает KOD/SIS implementation;
- не расширяет authority;
- требует correction только D1–D3 и следующий bounded review.

## EXPERIENCE

Идея → проверить не красивые happy-path формулировки, а места, где система повторяет PROMPT, откатывает source-set или выходит за chat boundary.

Проба → exact ZIP/hash/manifest verification + bounded cross-file lifecycle stress-review.

Результат → identity PASS; K1–K5 закрыты; K6 почти закрыт; три process gaps требуют точной коррекции.

Вердикт → `REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`.

Урок → fail-closed система ломается не только когда разрешает лишнее, но и когда не определяет, какой именно старый объект перестал быть исполнимым. А слово «всем» в source-loading policy иногда стоит дороже половины автоматики.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: bounded process/stress-review exact source-rebuild r0.2
СТАТУС: REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02
