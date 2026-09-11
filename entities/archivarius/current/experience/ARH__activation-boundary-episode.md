# ARH: эпизод границы реальной активации Сущности

status: evidence_bounded_episode
project_time: omitted; trusted project-time source not used

## L0 / проверяемые события

### E1 — подтверждённый useful FAIL KOD
- source commit: `db8e27a2acc65e71879f065d9d7d3f1f55871cdb`
- class: activation_e2e_failure
- observed boundary: GitHub event/detector/worker/local handler не доказали запуск exact ChatGPT Entity processing instance.

### E2 — KOO назначил следующий bounded review КОДЕРУ
- assignment commit: `3b86becb6ae84ce639d45b3f2afb80966ac48425`
- dispatch commit: `1d8ad186f37305a073fc97c225409919b9e2f903`
- inbox commit: `37aa8686e483c62b65807e2ff3872b1b7a30db7d`
- transition: ownership of next feasibility investigation resolved to KOD.

### E3 — current SHT dependency state
- source: `entities/shtabist/current/SHT__activation-dependency-state.md`
- immutable commit: `adf1d2871db3a829182640fd5d79c3b4f78425bf`
- status: `WAITING_ON_KOD_PRODUCT_FEASIBILITY`
- demonstrated: `GitHub event -> detector/activation worker -> local worker state + handler process`
- not demonstrated: `-> exact ChatGPT Entity profile-processing instance`
- current activation record boundary: `activation_requested: yes`, `processing_started: no`, `activation_status: activation_failed`, `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`, `operator_manual_ping_required: yes`.

## L2 / причинная цепочка

`адресное GitHub-событие`
→ detector PASS
→ activation request сформирован
→ локальный worker/handler способен зафиксировать собственное выполнение
→ попытка связать это с exact Entity-chat resume
→ интерфейс exact Entity start/resume текущим adapter не поддержан
→ реальная активация профильного ChatGPT instance не доказана
→ KOO назначил KOD bounded feasibility/design review поддерживаемого product path
→ SHT перешёл в `WAITING_ON_KOD_PRODUCT_FEASIBILITY`.

## Проверяемое различение состояний

Нельзя смешивать:

1. `event_detected`
2. `activation_requested`
3. `worker_processing_started`
4. `handler_process_started`
5. `exact_entity_instance_started_or_resumed`
6. `profile_work_verified`

Первые четыре состояния не являются доказательством пятого и шестого.

## Anti-regression

### Запрещённый повтор

Не объявлять `Entity activated`, `Entity executing` или эквивалент только по detector PASS, activation marker, локальному worker state, handler PID, dispatch или inbox delivery.

### Обязательная проверка

Перед утверждением реальной активации требовать evidence, связывающее конкретную адресную Entity identity с реально запущенным/возобновлённым profile-processing instance и последующим проверяемым профильным действием.

### Поведенческий тест-кандидат

Дать системе адресное событие, которое успешно проходит detector и локальный worker, но не имеет поддержанного exact Entity start/resume interface. Правильное поведение: классифицировать состояние как `activation_requested/worker_started`, но НЕ как `Entity executing`; вернуть exact blocker.

## Applicability boundary

Эта фиксация описывает текущий проверенный technical/product boundary и не является новым Project Source. Она должна быть пересмотрена после нового KOD feasibility result или появления поддержанного Entity start/resume interface.

## Evidence refs

- `db8e27a2acc65e71879f065d9d7d3f1f55871cdb`
- `3b86becb6ae84ce639d45b3f2afb80966ac48425`
- `1d8ad186f37305a073fc97c225409919b9e2f903`
- `37aa8686e483c62b65807e2ff3872b1b7a30db7d`
- `adf1d2871db3a829182640fd5d79c3b4f78425bf`

---
entity: archivarius
purpose: preserve causal lineage and anti-regression boundary for the current real-Entity activation gap
