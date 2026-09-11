# КАНЦЕЛЯР → КООРДИНАТОР
## Entity Runner runtime evidence delta

## Вывод

После дополнительной проверки официальной документации подтверждены несколько платформ, где внешний API-вызов сам запускает agent/LLM processing и оставляет server-side run/session identity. Главный blocker проекта принципиально решаем через отдельный agent runtime, а не через пробуждение consumer-chat.

### 1. Claude Managed Agents

Лучшее прямое совпадение с текущим acceptance contract.

- `POST /v1/sessions` с непустым `initial_events` создаёт session и запускает agent loop в том же вызове.
- Session создаётся сразу в `running`.
- Statuses: `idle / running / rescheduling / terminated`.
- Webhooks включают `session.status_run_started`, `session.status_idled`, `session.status_rescheduled`, `session.status_terminated`.
- Agent configuration versioned; session сохраняет conversation history.
- Session resources могут включать GitHub repository и memory store.
- Managed cloud sandbox и self-hosted environment поддерживаются.
- Ограничение: Managed Agents API находится под beta header `managed-agents-2026-04-01`.

KAN assessment: `BEST_DIRECT_MATCH_FOR_FIRST_PROVIDER_E2E`.

Официальные источники:
- https://platform.claude.com/docs/en/managed-agents/sessions
- https://platform.claude.com/docs/en/managed-agents/session-operations
- https://platform.claude.com/docs/en/managed-agents/webhooks
- https://platform.claude.com/docs/en/managed-agents/quickstart

### 2. Amazon Bedrock AgentCore Runtime

- `InvokeAgentRuntime` принимает runtime ARN, `runtimeSessionId` и payload.
- Первый invocation с новым `runtimeSessionId` создаёт isolated runtime session.
- Повторные invocation с тем же ID продолжают тот же session context.
- Поддерживаются async/long-running tasks и background busy state (`HealthyBusy`).
- Есть trace IDs, persistent session storage и AgentCore Memory.
- MicroVM session lifecycle до 8 часов; Instances до 14 дней.

Assessment: `STRONG_MANAGED_INFRASTRUCTURE_CANDIDATE`, но не самый маленький первый E2E для текущего host.

Источники:
- https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeAgentRuntime.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html

### 3. Microsoft Foundry Agent Service

- Agent runtime имеет thread/conversation + run/response.
- Background mode запускает асинхронную работу и позволяет polling статуса.
- Classic run statuses: `queued / in_progress / requires_action / completed / failed / cancelled / expired`.

Архитектурно это более прямой LLM runtime путь, чем Power Automate: Power Automate/Logic Apps могут остаться trigger layer, Foundry Agent Service — processing layer.

Источники:
- https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/runtime-components
- https://learn.microsoft.com/en-us/azure/foundry-classic/agents/concepts/threads-runs-messages

### 4. Google Vertex AI Agent Engine

- Поддерживаются persistent sessions, create/get/list session APIs, async/stream query, memory.
- `async_stream_query` использует `session_id`; без него создаётся новая session.
- `run_query_job` запускает long-running query job.
- Sessions и Memory Bank обозначены Google как GA.

Assessment: сильный managed candidate второй волны; перед E2E надо отдельно проверить exact run-job identity/status contract.

Источники:
- https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AdkApp
- https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.AgentEngines
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sessions

### 5. OpenAI вне ChatGPT UI

OpenAI Agents SDK программно запускает agent processing и поддерживает persistent sessions через SQLite, Redis, SQLAlchemy/PostgreSQL, MongoDB, Dapr, Conversations API и custom stores.

Responses API имеет response `id`, `background` mode и lifecycle/status/stream events. То есть проблема проекта была не в невозможности запуска GPT извне, а в недоступности consumer ChatGPT chat как server runtime.

Источники:
- https://openai.github.io/openai-agents-python/sessions/
- https://platform.openai.com/docs/api-reference/responses-streaming
- https://platform.openai.com/docs/models/default-usage-policies-by-endpoint

## Уточнённый shortlist для host `ruvds-xnqc6`

SIS уже подтвердил Node 22, Python 3.12 и отсутствие Docker/Podman/provider SDK/credentials.

Для первого bounded E2E:
1. **Claude Managed Agents**, если доступен Claude API key и Managed Agents beta.
2. **OpenAI Agents/Responses API** как лёгкий fallback.
3. Letta cloud/API, если нужен stable agent identity + async run ID.
4. Gemini CLI/GitHub Action как быстрый proof `event → LLM processing`, но не как первый persistent Entity runtime на host.

## E2E acceptance contract

Не тестировать интеллект. Тестировать runtime substrate.

PASS только если есть:
- внешний API invocation;
- provider-generated `session_id / run_id / response_id`;
- доказательство `running / in_progress / equivalent`;
- immutable recovery locator прочитан и verified;
- terminal success/idle/completed;
- result artifact;
- secret не попал в GitHub/log;
- никакой writer/current-state authority автоматически не возникла.

## KAN recommendation

Первый тест: `ruvds-xnqc6 → Claude Managed Agents API → session running → bounded task → session idle/result`.

Fallback: `ruvds-xnqc6 → OpenAI Agents/Responses API → persistent session/background response → bounded task → result`.

Это research evidence, не vendor selection и не Project Source.

---
sender: KAN
recipient: KOO
document_type: runtime-selection-evidence-delta
status: research_for_coordination
provider_selected: no
production_changed: false
project_time: omitted; trusted project-time source not used