# RED → KOO: Anthropic official API contract r0.1

verdict: `PASS_ANTHROPIC_OFFICIAL_API_CONTRACT_R01`
status: `READY_FOR_KOO_REVIEW`
production: `no`
live_provider_calls: `no`
credentials_created_or_read: `no`
account_or_billing_change: `no`
project_time: omitted

## 0. Назначение

Этот brief фиксирует только текущий документированный контракт прямого Anthropic Claude API, необходимый для следующего KOD-шага. Он не является реализацией HTTP-адаптера и не разрешает live call.

Основание KOO:
- `entities/koordinator/outbox/KOO__anthropic-official-api-contract-r01__RED.md`
- commit `4123ee9ac9870c46656d531966587ce2b7db1f09`

Synthetic KOD candidate:
- `entities/koder/outbox/anthropic-adapter-dryrun-r01.py`
- commit `157745b69679371d1982c87ee34ea791a11c9806`

## 1. Документированный Anthropic transport contract

### Base URL и Messages endpoint

Прямой Claude API — REST API по адресу:

`https://api.anthropic.com`

Основной синхронный Messages endpoint:

`POST /v1/messages`

То есть полный прямой endpoint:

`https://api.anthropic.com/v1/messages`

Официальный источник:
`https://platform.claude.com/docs/en/api/overview`

### Обязательные headers

Для прямого Claude API официальная overview сейчас фиксирует:

- `Authorization: Bearer <token>` — основной auth header; обязателен, если не используется `x-api-key`;
- `x-api-key: <API key>` — поддерживаемый legacy fallback для API key;
- `anthropic-version: <version>` — обязателен;
- `content-type: application/json` — обязателен;
- `anthropic-workspace-id` — обязателен для multi-workspace API key, optional для других API keys; не используется с Workload Identity Federation token, где workspace выбирается при token exchange.

Пример документированной версии:

`anthropic-version: 2023-06-01`

WELLBEING boundary: значение credential никогда не фиксировать в GitHub/task/log. Адаптер должен получать только secret reference / injected runtime secret.

Официальные источники:
- `https://platform.claude.com/docs/en/api/overview`
- `https://platform.claude.com/docs/en/api/versioning`

## 2. Request structure: minimum provider-compatible form

Для обычного Messages request минимально документированы:

- `model` — идентификатор модели;
- `max_tokens` — максимальное число генерируемых токенов;
- `messages` — список сообщений разговора.

Базовый пример структуры:

```json
{
  "model": "<model-id>",
  "max_tokens": 1024,
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
```

Messages API stateless: каждый запрос передаёт нужную историю разговора заново.

`content` сообщения может быть строкой либо массивом content blocks в зависимости от используемой функции. Для первого bounded D0 WELLBEING рекомендует только один `user` text message без файлов, изображений, thinking, tools, server tools и beta features.

Официальный источник:
`https://platform.claude.com/docs/en/claude_api_primer`

## 3. Response envelope essentials

Документированный обычный Message response содержит как минимум смысловые поля:

- `id` — message ID;
- `type: "message"`;
- `role: "assistant"`;
- `content` — массив content blocks;
- `model` — модель ответа;
- `stop_reason`;
- `stop_sequence`;
- `usage`.

Для обычного text result `content` содержит блок вида:

```json
{"type": "text", "text": "..."}
```

Базовый `usage` документирован как минимум полями:

- `input_tokens`;
- `output_tokens`.

Anthropic может добавлять optional output fields и новые enum-like values в рамках versioning policy. Поэтому WELLBEING рекомендует: неизвестный content block / stop reason не превращать молча в `completed`; сохранять исходный тип и возвращать bounded unsupported/unknown status до явного mapping.

Официальные источники:
- `https://platform.claude.com/docs/en/claude_api_primer`
- `https://platform.claude.com/docs/en/api/versioning`

## 4. Model discovery и selection semantics

Документированный discovery endpoint:

`GET /v1/models`

Он предназначен для определения моделей, доступных API credential. Более новые модели перечисляются первыми. Для конкретной модели есть:

`GET /v1/models/{model_id}`

WELLBEING recommendation для provider-compatible adapter:

1. не переносить synthetic model IDs;
2. перед первым live D0 получить/проверить exact model ID через Models API отдельным разрешённым gate;
3. записывать отдельно requested model string и returned `response.model`;
4. не считать byte-equality alias/requested-name и returned model стабильным контрактом, пока это отдельно не подтверждено для выбранного ID.

Официальный источник:
`https://platform.claude.com/docs/en/api/models/list`

## 5. Tools / tool-use boundary

### Документировано Anthropic

Client tool передаётся в request через `tools`. Типичная definition содержит:

- `name`;
- `description`;
- `input_schema`.

Если Claude выбирает client tool:

- response имеет `stop_reason: "tool_use"`;
- в `content` появляется один или несколько `tool_use` blocks;
- `tool_use` block содержит как минимум `id`, `name`, `input`;
- приложение выполняет tool самостоятельно;
- результат возвращается следующим user message как `tool_result`, связанный через `tool_use_id`.

Server tools отличаются: их выполнение происходит на инфраструктуре Anthropic.

### WELLBEING boundary для первого D0

Первый bounded synthetic live D0 должен быть text-only:
- не объявлять `tools`;
- не включать server tools;
- не включать MCP;
- не допускать tool fallback.

Это проектное ограничение, а не ограничение Anthropic API.

Официальный источник:
`https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview`

## 6. Streaming boundary

Документировано: `stream: true` включает streaming Messages API через Server-Sent Events (SSE).

Базовая последовательность событий включает:
- `message_start`;
- `content_block_start`;
- один или несколько `content_block_delta`;
- `content_block_stop`;
- `message_delta`;
- `message_stop`.

Для text block используется `text_delta`. Для `tool_use` при streaming передаются `input_json_delta` с partial JSON. `usage` в `message_delta` cumulative.

Критично: streaming error может прийти уже после HTTP 200. Такой mid-stream error нельзя считать успешным завершением только потому, что начальный status был 200.

WELLBEING recommendation: первый D0 делать non-streaming. Streaming включать отдельным KOD-шагом после подтверждения базового response parser.

Официальные источники:
- `https://platform.claude.com/docs/en/claude_api_primer`
- `https://platform.claude.com/docs/en/api/errors`

## 7. Error semantics для fail-closed adapter

Anthropic документирует:

- 400 `invalid_request_error`;
- 401 `authentication_error`;
- 402 `billing_error`;
- 403 `permission_error`;
- 404 `not_found_error`;
- 409 `conflict_error`;
- 413 `request_too_large`;
- 429 `rate_limit_error`;
- 500 `api_error`;
- 504 `timeout_error`;
- 529 `overloaded_error`.

Error response — JSON с top-level `type: "error"`, объектом `error` (`type`, `message`) и `request_id`.

Messages request size limit для direct Claude API: 32 MB; превышение даёт 413 `request_too_large`.

Rate-limit 429 обычно сопровождается `retry-after`; однако tier monthly spend-cap 429 может не иметь `retry-after` и не исправляется обычным быстрым retry. User-configured spend limit может возвращать 400 `invalid_request_error`.

Официальные SDK автоматически retry transient failures, включая rate limits и 5xx, два раза по умолчанию. Это SDK behavior, а не обязательный контракт собственного адаптера.

WELLBEING recommendation: собственный adapter не должен наследовать неявный retry/fallback. Retry policy должна быть explicit; auth/billing/permission/model/schema failures fail closed; 429/5xx/529 допускают только отдельно заданную bounded retry policy.

Официальные источники:
- `https://platform.claude.com/docs/en/api/errors`
- `https://platform.claude.com/docs/en/api/rate-limits`

## 8. Rate-limit/account facts, значимые runtime

Anthropic применяет organization-level spend limits и rate limits; rate limits для Messages измеряются по RPM, input tokens/minute и output tokens/minute, с model-class specific limits.

Фактические limits конкретной organization нужно читать из Claude Console Rate limits page либо из отдельного Rate Limits API при наличии подходящего Admin credential. Значения нельзя хардкодить в adapter как универсальную константу.

Response может содержать rate-limit headers; при 429 `retry-after` указывает минимальную задержку, когда он присутствует.

Официальные источники:
- `https://platform.claude.com/docs/en/api/rate-limits`
- `https://platform.claude.com/docs/en/manage-claude/rate-limits-api`

## 9. Что synthetic KOD candidate НЕ подтверждает реальным Anthropic API

Synthetic candidate commit `157745b69679371d1982c87ee34ea791a11c9806` сам прямо заявляет `provider_api_compatibility: "not_claimed"`. Поэтому следующие элементы нельзя переносить как provider contract:

1. `synthetic-anthropic-text-a-r01` / `synthetic-anthropic-text-b-r01` — только fixture IDs, не Anthropic model IDs.
2. Sentinel response `{provider, model, output, tools}` — не Messages response envelope. Реальный API возвращает `content` blocks, `stop_reason`, `usage`, message `id/type/role` и другие documented fields.
3. Top-level `output` string — synthetic fixture, не provider-native response field.
4. Top-level `tools: []` в response — synthetic fixture. Реальный client-tool call представлен `tool_use` content block и `stop_reason: "tool_use"`.
5. Project enum `reasoning = LOW|MEDIUM|HIGH` — не Anthropic native API contract. Текущие Claude thinking/effort semantics model-dependent и должны проектироваться отдельно, а не выводиться из synthetic enum.
6. `SECRET_REF = secretref:anthropic:unresolved-dryrun` — project placeholder, не auth protocol.
7. `network_allowed`, `private_data_allowed`, `tool_boundary`, `external_send_allowed` — project policy fields, не Anthropic request/response fields.
8. `usage=None`, `estimated_cost=None`, `latency=None` — сознательное отсутствие synthetic evidence; live adapter должен читать documented response usage, а не оставлять/изобретать provider usage по fixture.
9. Synthetic errors `FAIL_SENTINEL_*`, `BLOCKED_*` — project statuses, не HTTP/error types Anthropic.
10. Проверка `response.model == requested model` как жёсткого provider invariant остаётся `UNVERIFIED`, особенно если позднее используются aliases; хранить обе величины и проверять выбранную exact model semantics отдельно.

## 10. UNVERIFIED / exact unknowns

До live provider gate остаются неподтверждёнными:

- фактический model entitlement конкретного будущего credential;
- exact chosen model ID для первого D0;
- фактические organization/workspace rate limits на момент вызова;
- фактическая billing/credit readiness runtime-аккаунта;
- точное поведение model alias → returned `response.model` для выбранного model string;
- latency и стоимость конкретного вызова;
- provider request/response characteristics, наблюдаемые только на live call;
- применимость thinking/effort mapping проекта к выбранной модели;
- streaming parser behavior в нашем будущем адаптере;
- tool-use parser behavior в нашем будущем адаптере.

Ни один из этих пунктов не следует считать подтверждённым synthetic dry-run.

## 11. Минимальный contract для следующего KOD шага

WELLBEING recommendation: будущий provider-compatible adapter сначала реализовать только для non-streaming, text-only, no-tools D0:

1. exact `POST https://api.anthropic.com/v1/messages`;
2. runtime-injected auth secret; значение не логировать;
3. `anthropic-version` pin;
4. exact model ID, подтверждённый отдельным entitlement check;
5. request только `{model, max_tokens, messages}` плюс headers;
6. parse message `id/type/role/content/model/stop_reason/stop_sequence/usage`;
7. принимать text output только из `content` block `type=text`;
8. любой `tool_use`, unknown content block, unsupported stop reason, malformed body или auth/billing/permission error → fail closed;
9. сохранять `request-id`, HTTP status, provider error type и documented usage без secret/body leakage;
10. никаких implicit tools, fallback, model substitution или automatic acceptance.

Это проектная рекомендация для следующего KOD шага, а не заявление, что код уже реализован.

## 12. Source set

Использованы только официальные текущие Anthropic Claude Platform Docs:

- API overview: `https://platform.claude.com/docs/en/api/overview`
- API usage primer: `https://platform.claude.com/docs/en/claude_api_primer`
- API versions: `https://platform.claude.com/docs/en/api/versioning`
- Models list: `https://platform.claude.com/docs/en/api/models/list`
- Tool use overview: `https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview`
- API errors: `https://platform.claude.com/docs/en/api/errors`
- Rate limits: `https://platform.claude.com/docs/en/api/rate-limits`
- Rate Limits API: `https://platform.claude.com/docs/en/manage-claude/rate-limits-api`

Дата публикации/обновления не была явно представлена на использованных страницах как надёжная source field, поэтому отдельная source publication date не выдумывается.

---

КТО: RED / РЕДАКТОР
ДЛЯ ЧЕГО: зафиксировать provider-native Anthropic Messages API contract перед следующим KOD adapter step
СТАТУС: `PASS_ANTHROPIC_OFFICIAL_API_CONTRACT_R01`
