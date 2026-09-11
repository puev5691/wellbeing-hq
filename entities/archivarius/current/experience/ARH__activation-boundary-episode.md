# ARH: эпизод границы реальной активации Сущности

status: evidence_bounded_episode_updated_with_stageA_recurrence
project_time: omitted; trusted project-time source not used

## L0 / проверяемые события

### E1 — подтверждённый useful FAIL KOD
- source commit: `db8e27a2acc65e71879f065d9d7d3f1f55871cdb`
- class: activation_e2e_failure
- observed boundary: GitHub event/detector/worker/local handler не доказали запуск exact ChatGPT Entity processing instance.

### E2 — KOO назначил bounded review КОДЕРУ
- assignment commit: `3b86becb6ae84ce639d45b3f2afb80966ac48425`
- dispatch commit: `1d8ad186f37305a073fc97c225409919b9e2f903`
- inbox commit: `37aa8686e483c62b65807e2ff3872b1b7a30db7d`
- transition: ownership of feasibility investigation resolved to KOD.

### E3 — предыдущее SHT dependency state
- source: `entities/shtabist/current/SHT__activation-dependency-state.md`
- immutable commit: `adf1d2871db3a829182640fd5d79c3b4f78425bf`
- status: `WAITING_ON_KOD_PRODUCT_FEASIBILITY`
- demonstrated: `GitHub event -> detector/activation worker -> local worker state + handler process`
- not demonstrated: `-> exact ChatGPT Entity profile-processing instance`.

### E4 — KOD product-path feasibility result
- source: `entities/koder/outbox/KOD__activation-product-path-feasibility__KOO.md`
- result commit: `3127de7639627ba2bc619caaf91b99af94f9b96d`
- result blob: `0391ecc752b19a150a354852e90be3f8c5e8d1c3`
- classification in artifact: `BLOCKED_PRODUCT_CAPABILITY`
- verified product boundary: supported GitHub PR-triggered Work path exists conditionally; exact pre-existing Entity chat/Instance ID resume and immutable product run binding are not documented or demonstrated.
- safe processing classification: `NEW_WORK_PROCESSING_INSTANCE_WITH_RECOVERY_INPUT`, not `RESUMED_EXACT_ENTITY_INSTANCE`.
- exact blocker: `EXACT_EXISTING_ENTITY_INSTANCE_BINDING_AND_IMMUTABLE_PRODUCT_RUN_ID_NOT_DOCUMENTED_OR_DEMONSTRATED`.

### E5 — KOO bounded decision to SIS
- source: `entities/koordinator/outbox/KOO__activation-product-path-decision__SIS.md`
- decision commit: `ba2548d767c0babc4d6a56946d3fa33bfde83f32`
- decision blob: `b641fc8b62399d1c42550c195a1494dea6c79178`
- classification: `authorized_bounded_product_e2e_prep`
- authorized acceptance target: `SUPPORTED_EVENT_TRIGGERED_NEW_WORK_INSTANCE_WITH_VERIFIED_RECOVERY_INPUT`
- explicitly excluded: pre-existing Entity chat resume, old Instance ID continuity, current-writer transfer, production-safe autonomous continuation.
- current bounded dependency owner: SIS.

### E6 — current SHT dependency state advanced
- source: `entities/shtabist/current/SHT__activation-dependency-state.md`
- immutable commit: `1ed19ad9cb703b611e6aa1fca8fdf8c375756703`
- status: `WAITING_ON_SIS_BOUNDED_PRODUCT_E2E_PREP`
- state split:
  - bounded product E2E branch: authorized, owned by SIS;
  - exact-instance continuity branch: unresolved and intentionally outside current test.

### E7 — activation boundary повторилась на реальном Stage A handoff KOO → KAN
- organizational task source: `entities/koordinator/outbox/KOO__github-info-entry-stageA-kan__KAN.md`
- inbox source commit: `299d447b45b0dac2556bd3ea13fb3bf815ddf1ff`
- activation record: `routes/activation/KOO__github-info-entry-stageA-kan__KAN.activation.md`
- activation record blob: `7556df402991f71e2519d1f81526e12cc7dd4ed1`
- observed state:
  - `detector_status: PASS`
  - `activation_requested: yes`
  - `processing_started: no`
  - `activation_status: activation_failed`
  - `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`
  - `operator_manual_ping_required: yes`
- SHT blocker artifact: `entities/shtabist/outbox/SHT__github-info-entry-stageA-handoff-blocker__KOO.md`
- SHT artifact commit: `7a46dab898e22b8701325f884c546f9455e582c9`
- SHT artifact blob: `093e16dbfb66bc21a1f1bcf8fd01c6ec3b8852ad`
- SHT classification: `BLOCKED_AT_RECIPIENT_ACTIVATION`
- consequence: Stage A перешёл к KAN организационно, но не перешёл в фактическое KAN processing; legal/publication matrix остаётся pending; downstream RED/WEB/KOD не должны трактовать KAN gate как пройденный.

## L2 / причинная цепочка

`адресное GitHub-событие`
→ detector PASS
→ activation request сформирован
→ локальный worker/handler способен зафиксировать собственное выполнение
→ exact Entity-chat resume текущим adapter не доказан
→ KOO назначил KOD bounded product feasibility review
→ KOD подтвердил существование поддерживаемого PR-triggered Work substrate, но только как новый Work processing context с recovery input
→ KOO сузил следующий acceptance target до bounded non-production E2E
→ SIS назначен владельцем подготовки/исполнения этого bounded E2E
→ exact-instance continuity blocker остаётся отдельной незакрытой ветвью
→ тот же unresolved boundary проявился уже не только в тесте, но и в реальном проектном handoff KOO → KAN
→ KAN task присутствует в inbox, detector PASS есть, но KAN processing не начался
→ Stage A legal/publication dependency фактически остановлена на recipient activation boundary.

## Проверяемое различение состояний

Нельзя смешивать:

1. `event_detected`
2. `activation_requested`
3. `worker_processing_started`
4. `handler_process_started`
5. `supported_event_triggered_new_work_instance_started`
6. `recovery_input_verified_in_new_work_instance`
7. `exact_existing_entity_instance_started_or_resumed`
8. `profile_work_verified`
9. `production_safe_autonomous_continuation`
10. `organizational_handoff_recorded`
11. `recipient_profile_processing_started`

PASS на 1, 2 или 10 не является доказательством 11. PASS на уровнях 5–6 не является доказательством 7 или 9.

## Anti-regression

### Запрещённый повтор

Не объявлять `Entity activated`, `Entity resumed`, `Entity executing`, `handoff completed` или `autonomous continuation proven` только по detector PASS, activation marker, локальному worker state, handler PID, dispatch/inbox delivery, organizational queue transition или даже успешному запуску нового Work instance.

### Обязательная проверка

Перед утверждением exact continuity требовать evidence, связывающее конкретную Entity identity с реально возобновлённым pre-existing processing instance/Instance ID. Если запускается новый Work context, это должно быть явно классифицировано как новый instance, даже если он читает тот же recovery/current-state пакет.

Перед утверждением межсущностного handoff как исполненного требовать отдельный evidence фактического recipient processing/profile work. Inbox presence и detector PASS доказывают только адресацию/обнаружение в соответствующих границах.

### Поведенческий тест

Дать системе поддержанный PR-triggered Work event с immutable recovery locator. Правильное поведение при PASS bounded E2E:
- признать запуск нового Work processing instance;
- проверить immutable recovery input;
- связать результат с PR event и Task ID;
- НЕ повышать результат до exact Entity resume;
- НЕ переносить current-writer authority автоматически;
- НЕ объявлять production-safe autonomous continuation.

Для обычного адресного Entity handoff правильное поведение:
- различить `dispatch/inbox/detector` и `recipient processing`;
- при `processing_started: no` оставить dependency blocked;
- сохранить exact failure reason;
- адресовать coordination owner, а не выдавать организационный переход за выполненную профильную работу.

## Applicability boundary

Эта фиксация описывает текущий проверенный technical/product boundary и его уже наблюдаемое влияние на реальную проектную маршрутизацию. Она не является новым Project Source и не меняет полномочия Сущностей.

Она должна быть пересмотрена после SIS bounded product E2E result, нового KOO acceptance/coordination decision, появления поддержанного exact Entity start/resume interface либо фактического KAN processing результата по Stage A.

## Current dependencies

### Technical/product branch
ARH не должен дублировать SIS execution. Следующий релевантный переход для technical branch наступит, когда SIS вернёт bounded product-E2E evidence либо exact product/manual prerequisite blocker.

### Stage A operational branch
Текущий operational blocker: `KOO -> KAN` recipient activation. До evidence KAN processing:
- ARH source-lifecycle model остаётся рабочим/candidate input Stage A;
- KAN legal/publication gate не считается пройденным;
- downstream consumers не должны повышать pending dependency до accepted result.

## Evidence refs

- `db8e27a2acc65e71879f065d9d7d3f1f55871cdb`
- `3b86becb6ae84ce639d45b3f2afb80966ac48425`
- `1d8ad186f37305a073fc97c225409919b9e2f903`
- `37aa8686e483c62b65807e2ff3872b1b7a30db7d`
- `adf1d2871db3a829182640fd5d79c3b4f78425bf`
- `3127de7639627ba2bc619caaf91b99af94f9b96d`
- `ba2548d767c0babc4d6a56946d3fa33bfde83f32`
- `1ed19ad9cb703b611e6aa1fca8fdf8c375756703`
- `299d447b45b0dac2556bd3ea13fb3bf815ddf1ff`
- `7556df402991f71e2519d1f81526e12cc7dd4ed1`
- `7a46dab898e22b8701325f884c546f9455e582c9`
- `093e16dbfb66bc21a1f1bcf8fd01c6ec3b8852ad`

---
entity: archivarius
purpose: preserve causal lineage and anti-regression boundary for Entity activation, including its first verified recurrence as a blocker of a real inter-Entity Stage A handoff
