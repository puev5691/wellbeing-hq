# КАНЦЕЛЯР → КООРДИНАТОР
## Anthropic direct Claude API: доступ, цена, возможности и готовность первого D0_SYNTHETIC live pilot

## Вердикт

`READY_WITH_EXACT_ACCOUNT_PREREQUISITES`

Причина: технический и policy-контур direct Anthropic API для одного минимального `D0_SYNTHETIC` запроса подтверждён свежими официальными источниками, но фактическое состояние конкретной Claude Console organization сейчас не проверено и по условию задачи не должно проверяться через подключение аккаунта.

До первого live запроса остаются account-specific проверки:
- существует/доступна Claude Console organization;
- есть разрешённый billing state: положительный prepaid credit balance либо invoicing arrangement;
- создан отдельный разрешённый API key или настроен иной разрешённый auth path;
- подтверждены текущие tier/rate limits и spend limit именно этой organization/workspace;
- подтверждён доступ к выбранной модели в конкретном аккаунте.

Этот файл не создаёт account/API key, не покупает credits, не подключает provider и не разрешает D1/D2+.

---

# 1. Exact task и граница проверки

KOO task:

`entities/koordinator/outbox/KOO__anthropic-live-d0-access-cost-capabilities__KAN.md`

commit:

`fcd32868450afee2611ae795b71f0ba5a2c56620`

blob:

`94e127c5542c4c827b5e1447d5a6de383483fa75`

Проверяемый route:

`project local gateway/client → https://api.anthropic.com → Messages API → exact Claude model`

Не смешивать с:
- Claude Free / Pro / Max;
- Amazon Bedrock;
- Google Cloud;
- Microsoft Foundry;
- Claude Platform on AWS;
- Managed Agents;
- Files API;
- MCP connector;
- server-side search/code tools.

Первый D0 pilot ниже намеренно использует самый простой direct Messages route без stateful/tool side-boundaries.

---

# 2. Доступ и аутентификация

## Подтверждённый direct API path

Claude API — REST API на:

`https://api.anthropic.com`

Для direct model access официальный базовый endpoint:

`POST /v1/messages`

Минимальные prerequisites официальной документации:
- Claude Console account;
- API key **или** Workload Identity Federation.

Для первого ручного bounded pilot наиболее простой технический путь — API key.

## API key

Ключ создаётся в Claude Console:

`Settings → API keys → Create key`

Документация поддерживает:
- personal key;
- service account key;
- workspace scoping;
- expiration;
- disable/delete;
- переменную среды `ANTHROPIC_API_KEY` для SDK.

Для одиночного pilot рекомендуется:
- отдельный workspace для эксперимента, если это удобно текущей organization;
- workspace-scoped key;
- короткий разумный срок действия;
- передача только через approved secret mechanism;
- никогда не писать secret value в GitHub, prompt, result/provenance или debug log.

Для shared/unattended runtime позже предпочтительнее service-account credential либо Workload Identity Federation, но это не prerequisite первого ручного D0 запроса.

## Exact auth headers

Direct HTTP request использует:
- `Authorization: Bearer <key>` либо legacy `x-api-key`;
- `anthropic-version`;
- `content-type: application/json`.

Если key не scoped к одному workspace, может потребоваться `anthropic-workspace-id`.

---

# 3. Billing / credits

Anthropic Help Center указывает:
- большинство Claude API organizations оплачивают usage через prepaid usage credits;
- credits покупаются до использования API;
- organizations с invoicing arrangement получают monthly invoice вместо prepaid credits;
- при нулевом balance API/playground недоступны до пополнения;
- failed requests не тарифицируются, но запрос, оборвавшийся на стороне клиента/timeout после начала успешного выполнения, может быть тарифицирован;
- купленные credits действуют один год и не возвращаются.

Для покупки credits нужна роль Admin или Billing в Console:

`Settings → Billing → Buy credits`

Этот KAN task **не разрешает покупку**.

## Что неизвестно без конкретного Console account

- есть ли уже бесплатный/остаточный credit balance;
- минимальная доступная сумма пополнения в конкретном Console flow;
- есть ли invoicing arrangement;
- текущий organization tier;
- текущий spend limit/workspace limit;
- доступна ли нужная модель конкретной organization без дополнительных account-side ограничений.

Это должны быть проверяемые account facts перед live pilot, а не догадка из публичной документации.

---

# 4. Актуальные цены моделей direct Claude API

Все цены ниже — USD за миллион токенов (`MTok`) для first-party Claude API standard mode.

| Model | Model ID | Input | Output | 5m cache write | 1h cache write | Cache read |
|---|---|---:|---:|---:|---:|---:|
| Claude Sonnet 5 | `claude-sonnet-5` | $2 | $10 | $2.50 | $4 | $0.20 |
| Claude Opus 5 | `claude-opus-5` | $5 | $25 | $6.25 | $10 | $0.50 |
| Claude Fable 5.1 | `claude-fable-5-1` | $10 | $50 | $12.50 | $20 | $0.25 |

Особенность Fable 5.1: cache read тарифицируется по `0.025x` base input price; для остальных перечисленных моделей стандартный cache-read multiplier — `0.1x`.

## Batch API

Message Batches дают скидку 50% на input/output:
- Sonnet 5: `$1 / $5`;
- Opus 5: `$2.50 / $12.50`;
- Fable 5.1: `$5 / $25`.

Batch API не нужен первому live D0 request, потому что задача состоит в проверке direct synchronous Messages route.

## Prompt caching

Официальные множители:
- 5m cache write: `1.25x` base input;
- 1h cache write: `2x`;
- cache read: обычно `0.1x`, для Fable 5.1 — `0.025x`.

Первый D0 request следует делать **без caching**, чтобы не вводить лишнее state/cost evidence и не усложнять первый provenance envelope.

## Tool-specific pricing, которое materially relevant

Если инструменты будут включены позднее:
- web search: `$10 / 1000 searches` плюс обычные token costs;
- web fetch: без отдельной платы, но загруженный контент становится input tokens;
- code execution без web search/fetch: отдельная тарификация container runtime; с web search/web fetch code execution не имеет отдельной доплаты;
- computer/browser use в основном увеличивают input token overhead и token usage;
- Managed Agents дополнительно тарифицируются за session runtime: `$0.08 / session-hour` в состоянии `running` плюс model/tool tokens.

Для первого D0 pilot все server/client tools должны быть OFF, поэтому эти расходы **не входят** в первый тест.

---

# 5. Rate limits и spend tiers

Anthropic различает:
- spend limits;
- API rate limits.

## Usage tiers

Публичная документация содержит уровни:
- `Start`;
- `Build`;
- `Scale`;
- `Custom`.

Публичные monthly spend caps:
- Start: `$500`;
- Build: `$1,000`;
- Scale: `$200,000`;
- Custom: договорной режим без стандартного monthly cap.

Новые/малопользовавшиеся organizations могут первоначально находиться в `Evaluation` tier с лимитами **ниже** стандартных tier tables.

## Rate-limit dimensions

Messages API ограничивается отдельно по model class:
- RPM — requests per minute;
- ITPM — input tokens per minute;
- OTPM — output tokens per minute.

Rate limiting использует token-bucket behavior; короткие burst могут получить `429`, даже если среднее значение кажется ниже минутного лимита.

Для большинства текущих моделей cache-read tokens не считаются в ITPM; cache-creation и uncached input считаются.

Fable 5.1 и Fable 5 используют общий Fable 5.x rate-limit bucket.

## Что нельзя достоверно определить без Console account

Нельзя заранее заявить фактические:
- tier organization;
- RPM;
- ITPM;
- OTPM;
- acceleration behavior;
- per-workspace overrides;
- доступный headroom.

Источником истины для конкретного аккаунта является:
- Claude Console → Rate limits / Usage / Billing;
- либо Rate Limits API для organization, если есть подходящий Admin credential.

Для первого одного малого D0 request exact throughput практически не является архитектурным требованием, но его всё равно надо зафиксировать перед live pilot как account evidence.

---

# 6. Context и model boundaries

Для всех трёх выбранных моделей официальная документация указывает:
- context window: `1M tokens`;
- max output: `128K tokens`;
- input: text + images;
- output: text.

Общая модельная линейка поддерживает vision и tool use.

## Claude Sonnet 5

- `1M` context;
- `128K` max output;
- adaptive thinking включён по умолчанию;
- full feature set Sonnet 4.6 плюс stable computer/browser use на Claude API/Google Cloud;
- prompt caching, Batch API, Files/PDF, vision, client/server tools поддерживаются;
- `Priority Tier` не поддерживается.

## Claude Opus 5

- `1M` context;
- `128K` max output;
- adaptive thinking / effort;
- fast mode доступен в research preview на first-party Claude API по отдельной цене `$10/$50` input/output MTok;
- tool use, vision, computer/browser use поддерживаются;
- Priority Tier не поддерживается.

## Claude Fable 5.1

- `1M` context;
- `128K` max output;
- adaptive thinking always on;
- default effort `high`;
- active latest model;
- direct Claude API model ID: `claude-fable-5-1`;
- Anthropic рекомендует использовать Fable 5.1 для demanding reasoning/long-horizon work, когда Opus 5 на высоком effort недостаточен.

Fable 5.1 существенно дороже Sonnet 5 и Opus 5, поэтому для plumbing/readiness pilot она не нужна.

---

# 7. Feature / tool boundaries

Ниже — подтверждённые возможности платформы, но **не разрешение включать их в первый pilot**.

## Vision / images

Claude API поддерживает image content blocks; текущие 1M-context models могут принимать до 600 images/PDF pages per request, хотя request-size limit может сработать раньше.

## PDF

PDF support анализирует текст и визуальное представление страниц; применяется обычная token pricing. Можно передавать document blocks напрямую либо через Files API.

## Files API

Поддерживает upload/list/retrieve/delete и reuse через `file_id`.

Важная privacy boundary: Files API **not ZDR eligible** и хранит state. Для первого D0 pilot Files API OFF.

## Prompt caching

Поддерживается; 5m и 1h caching ZDR-eligible. Для первого pilot OFF, потому что caching не нужен для проверки direct access path.

## Batch

Все active models поддерживают Message Batches. Для первого pilot OFF.

## Web search / web fetch

Claude API поддерживает server-side web search и web fetch.

Privacy nuance: web search/fetch могут иметь отдельные ZDR conditions; dynamic filtering использует code execution. Первый D0 pilot: OFF.

## Code execution

Claude API поддерживает sandboxed bash/python code execution.

Ключевая retention boundary: code execution **not ZDR eligible**. Первый D0 pilot: OFF.

## MCP connector

Messages API имеет beta MCP connector к remote MCP servers.

MCP connector **not ZDR eligible**. Первый D0 pilot: OFF.

## Managed Agents

Это отдельный stateful agent runtime, а не plain Messages API.

Managed Agents:
- beta;
- sessions store conversation history/sandbox state/output server-side;
- not ZDR eligible;
- поддерживают files/bash/web/MCP/tool execution.

Для первого D0 pilot Managed Agents OFF. Этот pilot должен проверить только direct model API, не autonomous-agent runtime.

## Computer/browser use

Current direct Claude API поддерживает computer use и browser use на Sonnet 5, Opus 5 и Fable 5/5.1.

Computer/browser tools требуют выполнения действий в контролируемой клиентом среде и добавляют значительный token/tool overhead.

Первый D0 pilot: OFF.

---

# 8. Data use / retention direct commercial API

Эта часть относится только к commercial Anthropic API, не к Claude consumer Free/Pro/Max.

## Training

Anthropic официально указывает:

по умолчанию inputs/outputs коммерческих продуктов, включая Anthropic API, **не используются для обучения моделей**.

Исключения:
- явный feedback/report;
- Development Partner Program / иное явное opt-in.

Первый pilot должен быть без feedback/opt-in.

## Standard API retention

Для Anthropic API standard retention:
- inputs/outputs автоматически удаляются с backend в пределах 30 дней;
- исключения: features с более длинным retention, иной договор, safety/Usage Policy enforcement, legal retention.

Ad hoc deletion отдельного paid API request Anthropic не поддерживает; следует исходить из общей retention policy.

## ZDR

ZDR — отдельное arrangement, включаемое Anthropic для approved organizations.

Plain eligible Messages API может быть ZDR, но ZDR **не является prerequisite D0_SYNTHETIC pilot**.

## Fable 5.1 special retention

Claude Fable 5.1 относится к `Covered Models`.

Anthropic требует для Fable 5.1 **30-day data retention**, и модель обычно недоступна в ZDR workspace, если Anthropic отдельно не разрешил исключение.

Для обычного non-ZDR commercial API account это не добавляет новый retention срок сверх обычного 30-day D0 понимания, но это важный blocker, если organization позже окажется configured for ZDR.

Sonnet 5 и Opus 5 не перечислены в официальном current Covered Models list на проверенной странице.

---

# 9. Recommended first model candidate

Техническая/cost recommendation KAN:

`claude-sonnet-5`

Причина не в authority или утверждении «лучшая модель».

Для первого D0 pilot проверяется:
- authentication;
- billing;
- request format;
- exact model provenance;
- usage/cost capture;
- immutable result route.

Sonnet 5 делает это дешевле из трёх выбранных моделей:
- `$2 / MTok` input;
- `$10 / MTok` output;
- при этом имеет тот же `1M` context и `128K` output ceiling.

Opus 5 разумно сравнивать после успешного plumbing pilot на более содержательной synthetic benchmark task.

Fable 5.1 разумно подключать только для задач, где собственная оценка покажет недостаточность Opus 5, особенно учитывая цену и Covered Model retention boundary.

Google сохраняется как уже исследованный резервный/comparison route; широкая повторная Google-оценка в этой задаче не выполнялась.

---

# 10. Exact prerequisites первого D0_SYNTHETIC live pilot

До одного live API request должны одновременно быть выполнены следующие условия.

## Human/account prerequisites

1. ОПЕРАТОР подтверждает использование direct Anthropic route для одного D0 request.
2. Claude Console organization существует и доступна.
3. Billing page показывает:
   - положительный usable credit balance, **или**
   - действующий invoicing arrangement.
4. На workspace/organization установлен bounded spend limit, выбранный ОПЕРАТОРОМ, если Console это позволяет.
5. Claude Console показывает текущий tier/rate limits.
6. Подтверждён доступ к `claude-sonnet-5` в этой organization.
7. Создан workspace-scoped API key только после отдельного разрешения ОПЕРАТОРА/технического маршрута.

## Secret prerequisites

8. Key хранится только в approved secret boundary.
9. Runtime получает key через `ANTHROPIC_API_KEY` или эквивалентный secret injection.
10. Key value не попадает в:
    - GitHub;
    - task/result artifacts;
    - prompt;
    - command history, если это можно избежать;
    - stdout/stderr/debug logs.

## Request prerequisites

11. Route только:

`POST https://api.anthropic.com/v1/messages`

12. Model:

`claude-sonnet-5`

13. Только один локально созданный synthetic fixture класса `D0_SYNTHETIC`.
14. Никакого текста/файлов/имён/идентификаторов реального проекта в model input.
15. Tools/search/web/MCP/files/code execution/computer/browser/Managed Agents — OFF.
16. Prompt caching — OFF.
17. Batch — OFF.
18. Fallback model — OFF.
19. `max_tokens` — небольшой bounded ceiling, заданный pilot spec; KAN рекомендует не более `1024` для plumbing test.
20. Exact `anthropic-version` фиксируется в request provenance.

## Evidence prerequisites

21. До вызова записываются без secret value:
    - gateway run id;
    - task id;
    - D0 sensitivity class;
    - model ID;
    - route = direct Anthropic Messages API;
    - declared max_tokens/budget;
    - current account tier/rate limit evidence locator.
22. После ответа записываются:
    - provider `request_id`, если возвращён;
    - returned model ID;
    - stop reason;
    - input/output token usage;
    - HTTP terminal status;
    - result artifact immutable identity;
    - observed latency;
    - billing/usage evidence locator без secret.
23. Result остаётся `external_model_candidate_result` до отдельной project-side проверки/acceptance.
24. Provider/model не получает право писать current/recovery или принимать свои результаты.

---

# 11. Что всё ещё UNKNOWN до account-side проверки

До подключения конкретного Claude Console account нельзя подтвердить:
- фактический tier (`Evaluation/Start/Build/Scale/Custom`);
- exact RPM/ITPM/OTPM;
- current available credits;
- actual spend limit;
- workspace IDs;
- наличие/отсутствие ZDR arrangement;
- model visibility/access для этой organization;
- account-specific contractual terms/discounts;
- billing method;
- current API key state.

Это не blocker policy/technical readiness, но это exact prerequisite live execution.

---

# 12. Official source locators

Access/API/authentication:
- `https://platform.claude.com/docs/en/api/overview`
- `https://platform.claude.com/docs/en/get-started`
- `https://platform.claude.com/docs/en/manage-claude/authentication`

Billing/rate limits:
- `https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage`
- `https://platform.claude.com/docs/en/api/rate-limits`
- `https://platform.claude.com/docs/en/manage-claude/rate-limits-api`

Pricing/context/models:
- `https://platform.claude.com/docs/en/about-claude/pricing`
- `https://platform.claude.com/docs/en/build-with-claude/context-windows`
- `https://platform.claude.com/docs/en/models/overview`
- `https://platform.claude.com/docs/en/models/sonnet-5/whats-new-sonnet-5`
- `https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5`
- `https://platform.claude.com/docs/en/models/fable-5-1/overview`

Feature boundaries:
- `https://platform.claude.com/docs/en/build-with-claude/overview`
- `https://platform.claude.com/docs/en/build-with-claude/files`
- `https://platform.claude.com/docs/en/build-with-claude/pdf-support`
- `https://platform.claude.com/docs/en/build-with-claude/vision`
- `https://platform.claude.com/docs/en/build-with-claude/batch-processing`
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool`
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool`
- `https://platform.claude.com/docs/en/agents-and-tools/mcp-connector`
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool`
- `https://platform.claude.com/docs/en/managed-agents/overview`

Data use/retention:
- `https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training`
- `https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data`
- `https://privacy.claude.com/en/articles/7996875-can-you-delete-data-that-i-sent-via-api`
- `https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to`
- `https://platform.claude.com/docs/en/manage-claude/api-and-data-retention`
- `https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models`

---

# 13. Final decision

`READY_WITH_EXACT_ACCOUNT_PREREQUISITES`

Meaning:
- official technical/data/cost evidence is sufficient to prepare one direct Anthropic D0 live pilot;
- recommended first model is `claude-sonnet-5` as a cost-efficient plumbing candidate;
- actual live request must wait for explicit account/key/billing preparation and separate authorization;
- no D1/D2+ permission is created here.

No live call, provider connection, key creation or purchase occurred in this task.

---

## Experience fixation

**Идея:** readiness for an external LLM route is not the same as having an API key.

**Проба:** direct Anthropic route was decomposed into account, billing, auth, model, rate-limit, feature and retention prerequisites using current official documentation.

**Результат:** platform-side readiness is clear; the remaining unknowns are concrete Console-account facts, not architectural mysteries.

**Оценка:** `READY_WITH_EXACT_ACCOUNT_PREREQUISITES`.

**Фиксация:** first paid call should test the pipe, not Anthropic's entire product catalog. Turning on Files, web search, MCP, code execution and Managed Agents in the same first request would be a very efficient way to learn absolutely nothing about which boundary failed.

---

sender: KAN
recipient: KOO
document_type: anthropic-d0-access-cost-capabilities-readiness
status: READY_WITH_EXACT_ACCOUNT_PREREQUISITES
provider_connected: no
credentials_created: no
credits_purchased: no
live_call_performed: no
project_data_transferred: no
D1_or_higher_authorized: no
project_time: omitted; trusted project-time source not used
