# КАНЦЕЛЯР → КООРДИНАТОР
## Исследование: внешний запуск LLM/agent processing вместо «пробуждения чата»

## Главное открытие

После уточнения ОПЕРАТОРА задача переформулирована правильно:

> искать не новый таймер, а runtime, который по внешнему API/event реально переводит LLM/agent в состояние обработки, создаёт или продолжает проверяемую сессию и оставляет run/session identity.

По этому критерию уже найдено несколько систем, которые технически ближе к потребности ШТАБА, чем ChatGPT Scheduled Tasks.

Самый сильный новый кандидат на быстрый E2E: **Claude Managed Agents**.

Он умеет:
- создавать агентную сессию API-вызовом;
- запускать agent loop сразу при создании через `initial_events`;
- сохранять conversation history внутри session;
- выдавать session ID и statuses (`idle`, `running`, `rescheduling`, `terminated`);
- слать webhooks, включая `session.status_run_started`;
- запускать recurring sessions через Scheduled Deployments;
- подключать GitHub repository resources;
- подключать persistent memory stores, живущие между сессиями;
- работать в Anthropic cloud sandbox или self-hosted sandbox;
- иметь собственный chat UI поверх той же session model.

Это уже не «будильник, который просит человека открыть чат». Это API, создающий и запускающий agent instance.

---

# 1. Критерии отбора

Кандидат интересен только если он подтверждённо поддерживает цепочку:

`external event/API → processing_started → run/session identity → completion/failure`

Дополнительно оценивается:

`Entity ID + Task ID + recovery/current state → new or resumed agent session`

Exact старого UI-чата не требуется.

Желательные свойства:
- persistent thread/session;
- background execution;
- status/readback;
- tool access;
- GitHub/files;
- retry/failure state;
- self-host option;
- model/provider independence;
- возможность построить chat UI поверх runtime.

---

# 2. Кандидат A: Claude Managed Agents

## Почему это почти прямое попадание

Anthropic определяет session как **agent instance within an environment**.

Сессию можно:
1. создать;
2. отправить `user.message` / `user.define_outcome`;
3. либо создать сразу с `initial_events`, что немедленно запускает agent loop и создаёт session в `running`.

API:
- create session: `POST /v1/sessions`;
- send events: `POST /v1/sessions/{session_id}/events`.

`initial_events` позволяет создать session и начать работу одним API call.

### Проверяемая жизнь session

Statuses:
- `idle`;
- `running`;
- `rescheduling`;
- `terminated`.

Webhooks:
- `session.status_run_started`;
- `session.status_idled`;
- `session.status_rescheduled`;
- `session.status_terminated`;
- другие lifecycle events.

То есть внешний Supervisor получает именно то, чего нам недоставало: проверяемое событие **processing actually started**.

### Scheduled Deployments

Managed Agents умеют сами запускать agent sessions по cron.

Scheduled deployment:
- содержит agent configuration;
- environment;
- initial event;
- cron expression + timezone;
- каждый fire создаёт deployment run;
- successful deployment run содержит `session_id`;
- run history различает success/error;
- есть manual `run` endpoint.

То есть для этой платформы даже M365/GitHub scheduler необязателен.

### Persistent Entity memory

Memory Stores:
- живут между sessions;
- монтируются в agent sandbox;
- поддерживают read-only/read-write;
- изменения версионируются;
- поздние sessions видят сохранённые данные;
- отдельные immutable memory versions дают audit trail.

Для ШТАБА это потенциально можно разделить:
- GitHub recovery/current = canonical project truth;
- Claude memory store = вспомогательный Experience Layer/cache, не источник истины.

### Tools / environment

Agent definition включает:
- model;
- system prompt;
- tools;
- MCP servers;
- skills.

Cloud environment даёт isolated Linux sandbox.
Есть self-hosted sandbox mode.

### Chat UI

Официальные quickstart показывают чат как отдельный frontend поверх той же session model:
- Vercel Chat SDK;
- assistant-ui;
- CopilotKit / AG-UI;
- возможна адаптация под Slack/Teams/Discord/WhatsApp.

Следовательно, интерфейс разговора можно сделать отдельно. Runtime Сущности не обязан быть равен vendor chat product.

### Ограничения

- продукт beta;
- нужен Claude API account/key;
- Managed Agents billed по tokens + session runtime;
- состояние хранится server-side;
- нет Zero Data Retention / HIPAA BAA для Managed Agents;
- memory stores требуют отдельной дисциплины trust/prompt-injection;
- Claude-specific, не model-agnostic.

## Оценка

**P0 кандидат на практический E2E.**

Проверяемый target:

`external API call → Claude Managed Agent session running → read GitHub recovery → bounded task → write result artifact → webhook/readback`

---

# 3. Кандидат B: LangGraph Agent Server / LangSmith Deployment

## Сильная сторона

Это уже не одна LLM, а runtime для agent workflows.

Agent Server имеет:
- assistants;
- threads;
- runs;
- cron jobs;
- persistence;
- task queue;
- checkpoints;
- long-term memory.

Thread — persistent conversation/state container.
Run — отдельный execution.
Background run можно запустить REST API и сразу получить `run_id`.

Пример entry point:

`POST /threads/{thread_id}/runs`

или background stateless:
`POST /runs`.

Поддерживаются:
- `webhook` после завершения;
- `multitask_strategy`;
- `durability`;
- `on_disconnect: continue`;
- checkpoint resume;
- queue execution.

## Особо интересно для ШТАБА

Можно иметь:

`Entity ID ↔ LangGraph thread_id`

а каждое пробуждение:

`Task ID ↔ run_id`

Это почти готовая схема Entity/Instance.

Cron может запускать run **на существующем thread**, сохраняя continuity, либо stateless cron может создавать новый thread.

Agent Server хранит assistants/threads/runs/cron jobs/checkpoints в PostgreSQL; queue workers выполняют runs.

Есть standalone self-host через Docker/Docker Compose/Kubernetes.

## Model independence

LangGraph может вызывать разные model providers внутри graph. Runtime не завязан на одну LLM.

## Ограничения

- надо построить graph/agent loop;
- самим определить tool/security/authority integration;
- self-host требует Postgres и эксплуатацию;
- UI «чат» строится отдельно.

## Оценка

**P0/P1 кандидат на долговременный model-agnostic Entity Runner.**

---

# 4. Кандидат C: Letta

## Почему интересен

Letta прямо позиционирует себя как platform for **stateful agents with persistent memory**.

REST:
`POST /v1/agents/{agent_id}/messages`

Async:
`POST /v1/agents/{agent_id}/messages/async`

Async endpoint:
- реально запускает background processing;
- сразу возвращает `run.id`;
- status можно читать по run;
- предусмотрен `callback_url`.

У агента есть стабильный `agent_id`.

### Persistent identity/memory

Letta agent хранит:
- perpetual message history;
- memory blocks;
- agent state.

Есть background / long-running agents и resumable streaming.

Можно self-host через собственный Letta server.

### Почему похоже на нашу Сущность

Возможная модель:

`Entity ID ↔ Letta agent_id`

`Task attempt ↔ run_id`

Внешний Supervisor отправляет сообщение существующему agent ID и запускает processing без открытия UI.

### Ограничения

- concurrent requests одному agent могут interleave; документация советует последовательную обработку;
- нужно отдельно проверить GitHub/write-tool integration;
- Memory Letta не должна автоматически заменять canonical GitHub recovery;
- эксплуатационная зрелость для нашего контура требует E2E.

## Оценка

**P0/P1 кандидат, особенно интересен концептуально для долговечных Сущностей.**

---

# 5. Кандидат D: Claude Agent SDK

Это более низкоуровневый и более контролируемый путь, чем Managed Agents.

Python/TypeScript SDK:
- `query()` реально запускает agent loop;
- сессия получает session ID;
- можно `resume=session_id`;
- session содержит prompt, tool calls, tool results, responses;
- можно продолжать после process restart;
- для cross-host есть SessionStore / перенос transcript.

Внешний Supervisor может запускать наш worker process:

`GitHub/webhook/cron → entity-runner.py → Claude Agent SDK query/resume`

### Сильная сторона

Не надо ждать, пока сторонний chat product «разбудит чат».

Мы сами владеем launcher process.

### Ограничения

- session files/state надо хранить правильно;
- cross-host resume требует shared session storage;
- sandbox/security/tool approvals проектируем сами;
- Claude-specific.

## Оценка

**Очень практичный prototype path, особенно на нашем Linux server.**

---

# 6. Кандидат E: Gemini CLI GitHub Action

Google публикует официальный `google-github-actions/run-gemini-cli`.

Action:
- непосредственно **invokes Gemini CLI from a GitHub Action**;
- может работать по GitHub events;
- может работать по schedule;
- умеет автономно делать code analysis/modification, triage, PR review;
- принимает custom prompt;
- использует `GEMINI.md` как repository context;
- поддерживает tools/extensions.

То есть для repo-centric задач уже есть готовая цепочка:

`GitHub event → GitHub Actions runner → Gemini CLI agent processing`

Это полностью обходит ChatGPT Work.

### Ограничения

- это скорее новый instance на каждый workflow run;
- continuity придётся строить через GitHub recovery/current state;
- не полноценный long-lived chat/session substrate;
- особенно хорош для KOD/SIS/ARH-type repo tasks, слабее как общий conversational Entity runtime.

## Оценка

**P0 кандидат на очень дешёвый доказательный E2E: событие действительно запускает LLM agent без ОПЕРАТОРА.**

---

# 7. OpenAI API / Agents SDK как отдельный от ChatGPT путь

Проблема ChatGPT product UI не означает проблему OpenAI model runtime.

OpenAI Agents SDK поддерживает persistent Sessions:
- runner загружает history;
- добавляет новый input;
- сохраняет output;
- можно использовать Conversations API, SQLite, Redis, SQLAlchemy, MongoDB и custom stores.

Это означает, что собственный Entity Runner может запускать GPT processing обычным API/SDK вызовом.

Но:
- это **не ChatGPT chat**;
- consumer ChatGPT conversation не становится автоматически API session;
- UI придётся строить отдельно.

То есть GPT можно оставить как одну из моделей, если отказаться от требования «разбудить именно чат ChatGPT».

---

# 8. Dify и другие app runtimes

Dify имеет API:
- `POST /chat-messages`;
- conversations;
- `POST /workflows/run`;
- workflow run IDs/logs.

Это позволяет внешнему событию запускать LLM workflow или продолжать conversation.

Но по текущему evidence Dify менее точно совпадает с Entity continuity, чем Claude Managed Agents, LangGraph и Letta.

Оставить P2 кандидатом.

---

# 9. Что прототипировать первыми

## E2E-1: Gemini CLI GitHub Action

Цель:
`GitHub event → LLM processing`.

PASS:
- controlled GitHub event без сообщения ОПЕРАТОРА;
- Gemini CLI реально запускается;
- читает immutable task/recovery locator;
- создаёт result artifact;
- оставляет workflow run identity.

## E2E-2: Claude Managed Agents

Цель:
`API → session running → GitHub recovery → profile step → result → session idle/webhook`.

Проверить:
- доступ API account;
- create Agent;
- create Environment;
- create Session с `initial_events`;
- GitHub resource mount;
- status/webhook;
- result commit в test branch;
- memory store только read-only на первом тесте.

## E2E-3: Letta

Цель:
`HTTP async message → stable agent_id → run_id → callback → result`.

Проверить:
- self-host Docker;
- один agent = одна test Entity;
- sequential queue;
- read-only recovery pull;
- result write в GitHub.

## E2E-4: LangGraph

После доказательства принципа:
- один thread = Entity;
- run = work instance;
- Postgres/checkpoint;
- fail-closed recovery;
- model swap;
- cron/webhook;
- test с взаимозаменяемыми providers.

---

# 10. Архитектурный сдвиг

Вместо:

`Entity = ChatGPT chat`

проверить:

`Entity = external identity + recovery/current state + agent configuration`

`Instance = one LLM runtime session/run`

`Chat = optional operator interface to the same Entity runtime`

Тогда интерфейс может быть web/mobile/Telegram/Matrix/Teams/CLI/GitHub или отсутствовать для автоматического прохода.

---

# 11. Ранжирование

1. **Claude Managed Agents** — лучшее прямое совпадение.
2. **LangGraph Agent Server** — лучший model-agnostic фундамент.
3. **Letta** — сильное совпадение с persistent Entity memory/stable agent identity.
4. **Gemini CLI GitHub Action** — самый дешёвый proof, что событие запускает LLM agent processing.
5. **Claude Agent SDK** — простой собственный runner.
6. **OpenAI Agents SDK** — рабочий GPT API path вне ChatGPT UI.

---

# 12. Решение для координации

Не углублять Power Automate как главный путь до проверки execution substrate.

Параллельно запустить два bounded prototype:

1. Gemini GitHub Action:
   `GitHub event → LLM processing`.
2. Claude Managed Agents:
   `external API → persistent agent session → recovery → result`.

Если второй PASS, вопрос «как разбудить чат» снимается архитектурно:
чат становится интерфейсом, а не контейнером жизни Сущности.

После этого сравнить Managed Agents с self-hosted LangGraph/Letta по стоимости, portability, data control, memory semantics, GitHub integration, auditability и authority boundaries.

---

# Проверенные web sources

Anthropic:
- https://platform.claude.com/docs/en/managed-agents/overview
- https://platform.claude.com/docs/en/managed-agents/sessions
- https://platform.claude.com/docs/en/managed-agents/events-and-streaming
- https://platform.claude.com/docs/en/managed-agents/scheduled-deployments
- https://platform.claude.com/docs/en/managed-agents/memory
- https://platform.claude.com/docs/en/managed-agents/webhooks
- https://code.claude.com/docs/en/agent-sdk/sessions
- https://code.claude.com/docs/en/agent-sdk/overview

LangGraph/LangSmith:
- https://docs.langchain.com/langsmith/runs
- https://docs.langchain.com/langsmith/background-run
- https://docs.langchain.com/langsmith/use-threads
- https://docs.langchain.com/langsmith/cron-jobs
- https://docs.langchain.com/langsmith/agent-server
- https://docs.langchain.com/langsmith/deploy-standalone-server

Letta:
- https://docs.letta.com/
- https://docs.letta.com/api/resources/agents
- https://docs.letta.com/api/typescript/resources/agents/subresources/messages/methods/create_async
- https://docs.letta.com/api/typescript

Google:
- https://github.com/google-github-actions/run-gemini-cli

OpenAI:
- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-js/guides/sessions/

---

КТО: КАНЦЕЛЯР (KAN)
ДЛЯ ЧЕГО: продолжить model-agnostic поиск механизма, который реально запускает LLM/agent processing, а не только ловит trigger.
document_type: llm-activation-runtime-research
status: research_result_for_coordination
priority: high
project_source_created: no
production_changed: false
project_time: omitted; trusted project-time source not used
