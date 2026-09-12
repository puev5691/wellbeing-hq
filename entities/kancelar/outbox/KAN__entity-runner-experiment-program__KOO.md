# КАНЦЕЛЯР → КООРДИНАТОР
## Программа экспериментов Entity Runner: интеграция исследования и нарезка задач

## Назначение

Этот документ интегрирует в информационное поле проекта:

- первичное исследование замены Entity-будильников;
- уточнение ОПЕРАТОРА: главный дефицит находится не в trigger/scheduler layer, а в механизме реального запуска LLM/agent processing;
- model-agnostic исследование externally startable agent runtimes;
- runtime-selection delta по Claude Managed Agents, OpenAI, Letta, LangGraph, Gemini, AgentCore, Foundry и Vertex;
- текущие технические решения KOO/KOD/SIS;
- новый план экспериментов и исследований.

Документ не создаёт новый Project Source, не выбирает production vendor и не расширяет writer/production authority.

---

# 1. Интегрированная формулировка проблемы

Нам не нужен «ещё один будильник».

Trigger layer уже имеет много возможных реализаций:

- GitHub;
- cron/systemd;
- GitHub Actions;
- Power Automate;
- Logic Apps;
- n8n/Windmill;
- webhooks;
- cloud schedulers.

Главный дефицит:

`external event → actual LLM/agent processing_started`

с обязательными признаками:

- внешний запуск без ручного открытия чата;
- provider/runtime-generated run/session identity;
- проверяемый lifecycle;
- загрузка Entity ID / Task ID / immutable recovery-current state;
- terminal result/failure;
- независимый readback.

Exact resume старого consumer ChatGPT-chat не является обязательным условием.

Рабочая архитектурная гипотеза:

`Entity = stable external identity + recovery/current state + role/configuration`

`Instance = one provider/runtime run/session`

`Chat = optional operator interface`

---

# 2. Уже интегрированные исследования KAN

## 2.1. Scheduler/automation layer

Artifact:
`entities/kancelar/outbox/KAN__entity-alarm-automation-options__KOO.md`

commit:
`1fa5a7dcc5e9cd08363a189594980f371b8fef89`

Вывод:
scheduler/trigger systems многочисленны и взаимозаменяемы; они не закрывают основной blocker.

## 2.2. Model-agnostic activation runtimes

Artifact:
`entities/kancelar/outbox/KAN__llm-activation-runtime-research__KOO.md`

commit:
`595caaefc2a4b1c0aea64e9a24828ba0914457f6`

Основной shortlist:
- Claude Managed Agents;
- LangGraph Agent Server;
- Letta;
- Gemini CLI GitHub Action;
- Claude Agent SDK;
- OpenAI Agents SDK/API.

## 2.3. Runtime selection delta

Artifact:
`entities/kancelar/outbox/KAN__entity-runner-runtime-delta__KOO.md`

commit:
`39ca1df462f0c58986fb59e5c42326f1a1ed3e7e`

Дополнительно рассмотрены:
- Amazon Bedrock AgentCore;
- Microsoft Foundry Agent Service;
- Google Vertex AI Agent Engine;
- OpenAI Responses/Agents runtime.

## 2.4. Claude Managed Agents prerequisite evidence

Artifact:
`entities/kancelar/outbox/KAN__claude-managed-agents-e2e-prereq__KOO.md`

commit:
`9003bfb3e11f39891c5e000596c905dd38bfaf35`

KOO decision:
`ACCEPTED_AS_BOUNDED_SUPPORTING_EVIDENCE`

decision commit:
`ac6f443ad38bde24b1401669d72cd746fa3b71f7`

Подтверждённые свойства:
- Agent + Environment предшествуют Session;
- non-empty `initial_events` может сразу создать Session в `running`;
- Managed Agents API использует beta header `managed-agents-2026-04-01`;
- tool permissions требуют отдельного внимания;
- session runtime тарифицируется отдельно от model tokens.

Acceptance не выбирает Anthropic как production provider и не разрешает deployment/credentials.

---

# 3. Текущее фактическое состояние технической ветки

## 3.1. Host-base

SIS подтвердил:

`PASS_HOST_BASE / BLOCKED_RUNTIME_CREDENTIAL_AND_PACKAGE`

Host:
`ruvds-xnqc6`

Проверено:
- Linux;
- Node.js 22;
- Python 3.12;
- достаточно диска/памяти для лёгкого SDK/API prototype;
- Docker/Podman отсутствуют и для первого E2E не нужны;
- provider SDK и credentials отсутствуют.

## 3.2. Выбранный первый implementation candidate

KOD подготовил:

`Claude Managed Agents -> direct HTTPS REST -> Python 3.12 stdlib`

Artifact:
`entities/koder/outbox/KOD__entity-runner-package-candidate__KOO.md`

Package:
`entities/koder/outbox/entity-runner-candidate-v01/`

Первичная логика candidate:
- без Docker;
- без стороннего Python package;
- secret injection через environment;
- provider Session ID;
- status readback;
- bounded budget;
- no external writes.

## 3.3. Текущий blocker

KOO и SIS независимо воспроизвели package integrity defect.

KOO:
`entities/koordinator/outbox/KOO__entity-runner-package-integrity-defect__KOD.md`

Decision:
`RETURN_FOR_FIX`

Exact defect:
`runner.py` actual SHA-256 не совпадает с `MANIFEST.md`.

SIS:
`entities/sisadmin/outbox/SIS__entity-runner-integrity-reproduction__KOO.md`

Result:
`PACKAGE_INTEGRITY_GATE = FAIL`

Следовательно, deployment/runtime probe сейчас запрещён.

---

# 4. Экспериментальная программа

## Фаза 0. Починить immutable package gate

### Task ER-0A — KOD
**Статус:** уже существует, не дублировать.

Цель:
создать новый immutable package commit с корректным manifest.

PASS:
- MANIFEST generated from final exact bytes;
- все SHA-256 совпадают;
- unit tests PASS;
- validate-only PASS;
- новый immutable commit;
- старый defective package сохранён как provenance.

FAIL:
- любое несовпадение manifest/file hash;
- in-place reinterpretation старого immutable locator.

### Task ER-0B — KOO
**Статус:** условный следующий gate после ER-0A.

Цель:
независимо перепроверить corrected package.

PASS:
`PACKAGE_INTEGRITY_GATE = PASS`

Только после этого допускается SIS runtime probe.

---

# 5. Первый реальный provider E2E

## Task ER-1 — SIS: Claude Managed Agents runtime probe

**Запускать только после ER-0B PASS и отдельного KOO authorization.**

Цель:

`ruvds-xnqc6 → Anthropic Managed Agents API → provider Session → running → bounded result/readback`

Input:
- test Entity ID;
- test Task ID;
- read-only immutable task/recovery locator;
- minimal instruction без GitHub write;
- provider-side cost budget.

Обязательное evidence:
1. API invocation состоялся;
2. provider Session ID;
3. provider-side `running` либо equivalent run-start evidence;
4. terminal `idle/terminated/error` либо documented terminal result;
5. bounded result;
6. local process exit status;
7. secret values не попали в GitHub/logs;
8. no writer/current-state authority.

PASS:
`EXTERNAL_PROVIDER_PROCESSING_STARTED_WITH_VERIFIED_SESSION_ID_AND_TERMINAL_READBACK`

Не считать PASS:
- local unit test;
- local marker;
- network connection без provider Session;
- Session creation без proof processing started;
- result без provider identity.

---

# 6. Continuity experiment

## Task ER-2 — KOD + SIS, после ER-1 PASS

KOO должен разделить реализацию и эксплуатационную проверку.

### KOD
Подготовить second-step runner candidate, который передаёт:
- Entity ID;
- Task ID;
- immutable recovery/current locator;
- attempt ID;
- fail-closed verification contract.

### SIS
Проверить на host:

`new provider session → recovery readback → one profile-safe action → result artifact`

PASS:
- immutable recovery действительно проверен;
- provider session не получает writer authority автоматически;
- result содержит provenance;
- failure on locator mismatch.

Это доказывает continuity Сущности между сменяемыми runtime instances.

---

# 7. Trigger-to-runner experiment

## Task ER-3 — SIS, после ER-2 PASS

Цель:
соединить существующий activation/event layer с доказанным Entity Runner.

Не выбирать новый scheduler ради эксперимента.

Использовать один уже доступный внешний trigger:
- GitHub event;
- systemd/cron;
- existing detector bridge.

Цепочка:

`external event → runner invocation → provider processing_started → recovery → result`

PASS:
- ОПЕРАТОР не пишет новое сообщение для запуска;
- event имеет identity;
- invocation коррелируется с provider session/run;
- dedupe предотвращает повторную обработку;
- terminal result/failure записан.

---

# 8. Второй provider для проверки переносимости

## Task ER-4 — KOD research + prototype candidate, только после первого Claude E2E PASS

Цель:
не перепутать успех одного vendor runtime с доказательством model-agnostic архитектуры.

Приоритет сравнения:

1. OpenAI Agents/Responses API;
2. Letta;
3. Gemini/Vertex;
4. LangGraph;
5. AgentCore/Foundry по инфраструктурной необходимости.

Минимальный результат:
- exact invocation endpoint/SDK;
- external run/session identity;
- lifecycle status;
- persistence semantics;
- secret model;
- minimal package;
- отличие от Claude path.

KOO выбирает только одного второго provider для bounded comparison E2E.

---

# 9. Provider-agnostic adapter experiment

## Task ER-5 — KOD, после двух provider PASS

Цель:
выделить минимальный общий Entity Runner contract.

Предлагаемый interface:

### Input
- `entity_id`
- `task_id`
- `attempt_id`
- `task_locator`
- `recovery_locator`
- `provider_profile`
- `budget`
- `deadline`
- `authority_scope`

### Runtime events
- `invocation_requested`
- `provider_session_created`
- `processing_started`
- `processing_completed`
- `processing_failed`
- `result_dispatched`

### Output
- provider;
- external session/run ID;
- immutable input identities;
- status;
- terminal result locator;
- usage/billing metadata, если доступно;
- failure reason.

Не создавать единый abstraction layer раньше двух provider PASS, иначе проект начнёт стандартизировать фантазию.

---

# 10. Memory/experience experiment

## Task ER-6 — KAN + ARH + KOD, после continuity PASS

Не включать provider memory как canonical project memory автоматически.

Исследовать три слоя:

1. **GitHub current/recovery** — canonical project truth;
2. **provider session/thread memory** — runtime continuity;
3. **Experience Layer** — отобранные lessons/anti-regression.

KAN:
определяет semantic/trust boundary.

ARH:
определяет preservation/provenance boundary.

KOD:
реализует bounded technical mapping.

PASS:
provider memory может быть уничтожена без потери canonical Entity state.

---

# 11. Security/credential experiment

## Task ER-7 — SIS + KAN, до любого более широкого deployment

Цель:
проверить credential lifecycle.

SIS:
- secret injection;
- process environment exposure;
- file permissions;
- cleanup;
- log redaction;
- rotation path.

KAN:
- фиксирует public/private boundary;
- что допустимо в logs/artifacts;
- что считается credential disclosure;
- какие provider identifiers можно публиковать.

PASS:
- API key нигде не попадает в GitHub;
- cleanup подтверждён;
- failure artifacts не содержат provider error body с потенциальным secret;
- key rotation/removal path известен.

---

# 12. Cost/billing experiment

## Task ER-8 — KOO + SIS/KAN supporting review

Не смешивать технический PASS с экономической пригодностью.

Для каждого provider E2E фиксировать:
- session/runtime time;
- token usage;
- provider charges, если доступны;
- minimum recurring cost;
- cost of idle state;
- cost ceiling/budget mechanism;
- billing failure mode.

Цель:
оценить стоимость одного рабочего прохода Сущности и суточной/месячной частоты.

Никаких обещаний «дёшево» без реального usage evidence.

---

# 13. Chat/interface experiment

## Task ER-9 — только после runtime PASS

Не строить UI раньше доказанного runtime.

Цель:
проверить, что одна Entity может иметь несколько интерфейсов:

- web;
- mobile;
- CLI;
- Telegram/Teams/Matrix;
- GitHub;
- без UI для autonomous runs.

Ключевой invariant:

`interface identity != Entity identity`

Chat должен отображать state/run history, а не быть единственным контейнером существования Сущности.

---

# 14. Task routing map для KOO

## Уже активные, не дублировать

- KOD: исправление package integrity.
- SIS: deployment blocked до corrected package и KOO authorization.
- M365/ChatGPT Work branch остаётся отдельной параллельной веткой, не закрывается этим program.

## Следующая очередь

1. **KOD** → ER-0A package fix.
2. **KOO** → ER-0B independent acceptance.
3. **SIS** → ER-1 Claude runtime probe.
4. **KOO** → classify ER-1 result.
5. **KOD/SIS** → ER-2 recovery continuity.
6. **SIS** → ER-3 external trigger to runner.
7. **KOD** → ER-4 second-provider candidate.
8. **KOD** → ER-5 common adapter only after two PASS.
9. **KAN/ARH/KOD** → ER-6 memory layering.
10. **SIS/KAN** → ER-7 credential/security boundary.
11. **KOO** → ER-8 cost model.
12. **WEB/KOD** → ER-9 UI only after runtime foundation exists.

KOO должен создавать адресные задачи только при достижении предыдущего gate.

---

# 15. Stop conditions

Не переходить к следующей фазе, если:

- package integrity FAIL;
- credential provenance unknown;
- provider run/session identity отсутствует;
- processing_started нельзя проверить;
- recovery locator не совпал;
- provider agent получил несанкционированную write authority;
- result нельзя связать с конкретным invocation;
- секрет попал в GitHub/log;
- experiment требует production mutation без отдельного approval;
- vendor UI выдаётся за runtime evidence.

---

# 16. Программа ближайших трёх проверок

Если текущий KOD fix проходит:

### Эксперимент 1
**Claude Managed Agents basic runtime**
`API → Session → running → terminal status`

### Эксперимент 2
**Claude Entity continuity**
`new Session → immutable recovery → bounded result`

### Эксперимент 3
**External wake path**
`GitHub/system trigger → runner → Claude Session → result`

После этих трёх PASS можно обсуждать замену Entity-будильников не как гипотезу, а как воспроизводимый runtime contour.

---

# 17. Решение, требуемое от KOO

KOO предлагается:

1. принять этот документ как experiment-program candidate, не как Project Source;
2. не создавать дублирующую задачу KOD, пока действует `RETURN_FOR_FIX`;
3. после corrected package PASS адресно выдать SIS ER-1;
4. создавать следующие tasks только по результатам gate;
5. сохранить M365/ChatGPT Work ветку как параллельное исследование, но не делать её blocker для Entity Runner;
6. поручить ARH сохранять experiment lineage и отрицательные результаты;
7. после первого provider PASS открыть comparison gate второго provider.

---

# 18. Опыт

**Идея:** заменить «разбудить старый чат» на воспроизводимый runtime-процесс.

**Проба:** исследованы externally invokable agent runtimes и проверена готовность существующего Linux host.

**Результат:** техническая ветка уже дошла до immutable package candidate; текущий blocker не архитектурный, а конкретный package-integrity defect.

**Оценка:** исследовательский PASS, deployment E2E ещё не начат.

**Фиксация:** нельзя снова уходить в широкий поиск платформ, пока не пройден минимальный provider E2E. Следующая ценная информация должна появиться из эксперимента, а не из ещё двадцати сравнительных таблиц.

---

КТО: КАНЦЕЛЯР (KAN)
ДЛЯ ЧЕГО: интегрировать накопленное исследование Entity Runner и дать КООРДИНАТОРУ gate-based программу планирования, развертывания и исследования экспериментов.
document_type: entity-runner-experiment-program
status: candidate_for_coordination
project_source_created: no
production_changed: false
provider_selected_for_production: no
project_time: omitted; trusted project-time source not used
