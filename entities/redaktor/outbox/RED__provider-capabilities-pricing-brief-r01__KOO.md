# RED → KOO: операторский brief по API-провайдерам r0.1

verdict: `PASS_PROVIDER_OPERATOR_BRIEF_R01`
status: `READY_FOR_KOO_REVIEW`
production: `no`
live_provider_calls: `no`
credentials_created_or_used: `no`
account_creation_or_purchase: `no`
project_time: omitted

## 0. Короткий вывод для ОПЕРАТОРА

Для текущей инфраструктурной линии проекта разумная последовательность остаётся прежней:

1. **OpenAI — первым**: это уже принятая проектная линия; официальный API сейчас даёт понятную лестницу стоимости от `GPT-5.6 Luna` до `GPT-5.6 Sol`, структурированный вывод, вызов функций и встроенные инструменты, а `Batch API` даёт асинхронную обработку со снижением стоимости на 50%. Это **рекомендация проекта**, а не заявление OpenAI о превосходстве.
2. **Anthropic — следующим**, если на этапе аккаунта/оплаты не появится конкретный внешний блокер: у Claude есть прямая API-линейка Haiku/Sonnet/Opus, вызов инструментов, структурированный вывод, prompt caching и Batch со скидкой 50%. В просмотренных официальных источниках технического блокера для обычной API-интеграции не найдено. Точный первый шаг по созданию/финансированию нового Anthropic-аккаунта в этом FAST_PATH не подтверждён и помечен `UNVERIFIED`.
3. **Google AI / Gemini API — параллельный или следующий кандидат**: API требует ключ и проект; для paid tier Google документирует Cloud Billing и предварительное пополнение минимум на $5. Есть дешёвые Flash-Lite модели, функция вызова инструментов, JSON Schema, Batch, кэш контекста, Google Search, File Search и Computer Use. Для сложной работы актуален `gemini-3.1-pro-preview`, но это preview-модель; точную текущую цену этой модели в данном brief я не привязываю и отмечаю `UNVERIFIED`.

Ни один провайдер этим документом не подключается, не оплачивается и не получает данные проекта.

---

# 1. OpenAI

## Доступ и учётная структура

**Документировано.** OpenAI API принимает bearer-учётные данные из API keys либо краткоживущих access tokens через workload identity federation. В административном API существуют Projects, service accounts и API keys. OpenAI прямо указывает, что API key является секретом и его нельзя помещать в клиентский код; ключ следует загружать из переменной окружения или серверного key-management service.

Официальный источник:
- `https://developers.openai.com/api/reference/overview`

**UNVERIFIED в этом brief:** точные стартовые требования к биллингу/минимальному пополнению нового API-аккаунта. Не додумывать до отдельной проверки.

**Рекомендация проекта.** Для WELLBEING использовать отдельный Project/service account и внешний secret store; не хранить API key в GitHub, логах, task-envelope или публичных артефактах.

## Текущая ценовая лестница моделей

Официальные model pages на момент проверки:

| Модель | Документированное назначение | Input / 1M | Cached input / 1M | Output / 1M |
|---|---|---:|---:|---:|
| `GPT-5.6 Luna` | cost-sensitive, high-volume | $0.20 | $0.02 | $1.20 |
| `GPT-5.6 Terra` | баланс интеллекта и стоимости | $2.00 | $0.20 | $12.00 |
| `GPT-5.6 Sol` | сложная профессиональная работа | $4.00 | $0.40 | $20.00 |

Официальные источники:
- `https://developers.openai.com/api/docs/models/gpt-5.6-luna`
- `https://developers.openai.com/api/docs/models/gpt-5.6-terra`
- `https://developers.openai.com/api/docs/models/gpt-5.6-sol`

**Рекомендация проекта.**
- routine/массовые простые задачи Сущностей: начать измерения с `GPT-5.6 Luna`;
- обычная координационная/редакторская/инженерная работа: `GPT-5.6 Terra` как кандидат по балансу цены и качества;
- сложные проверки, архитектура, неоднозначная аналитика: `GPT-5.6 Sol`.

Это проектная схема маршрутизации, не официальный рейтинг моделей.

## Функции, структурированный вывод, инструменты

**Документировано.** В Responses/Agents API доступны встроенные tools, function calling, web search, file search, tool search и remote MCP; документация отдельно содержит computer use и code/shell-related tools. Наличие и конфигурация конкретного инструмента зависят от выбранной интеграции. Structured Outputs ограничивает ответ заданной JSON Schema; для строгого режима неподдерживаемая схема приводит к ошибке, а не к произвольной форме.

Официальные источники:
- `https://developers.openai.com/api/docs/guides/tools`
- `https://developers.openai.com/api/docs/guides/structured-outputs`

**Рекомендация проекта.** На первом инфраструктурном этапе оставить web/file/computer/MCP как отдельные разрешаемые data/authority paths. Сам факт поддержки tool не означает разрешение Сущности им пользоваться.

## Кэширование, Batch и асинхронность

**Документировано.** В model pages есть отдельная более низкая цена cached input. `Batch API` обрабатывает группы запросов асинхронно, имеет отдельный пул rate limits, целевой turnaround до 24 часов и документированное снижение стоимости на 50% для задач без требования немедленного ответа.

Официальные источники:
- model pages выше;
- `https://developers.openai.com/api/docs/guides/batch`

**Рекомендация проекта.** Повторяющийся системный/канонический контекст оценивать через caching; массовые ночные проверки, классификацию и eval — через Batch, если задержка допустима.

## Rate limits и организационные ограничения

**Документировано.** Rate/usage limits видны для организации в account settings; при росте API spend аккаунт обычно переводится на следующий usage tier, что увеличивает лимиты для большинства моделей.

Официальный источник:
- `https://developers.openai.com/api/docs/guides/rate-limits`

**Рекомендация проекта.** Не закладывать фиксированные RPM/TPM в архитектуру как вечную константу; читать текущие limits из аккаунта и иметь backoff/queue.

## Практическая пригодность для WELLBEING

**Проектная рекомендация:** `OPENAI_FIRST`.

Причины: это уже утверждённая приоритетная линия; есть дешёвая routine-модель, средняя модель и сложная модель; документированы строгие структуры, tools и дешёвая асинхронная обработка. На старте держать provider calls отдельно от authority: модель выдаёт candidate/result, но не сама принимает проектное решение.

---

# 2. Anthropic

## Доступ и организация

**Документировано.** Claude Platform использует Organizations/Workspaces. В workspace можно назначать участников, service accounts и API keys, а также задавать spend/rate limits; workspace limits могут быть ниже организационных, но не выше, и общие organizational limits продолжают действовать.

Официальный источник:
- `https://platform.claude.com/docs/en/manage-claude/workspaces`

**UNVERIFIED в этом brief:** точная процедура первого создания/финансирования Anthropic API account и минимальный платёж, если он требуется сейчас.

**Рекомендация проекта.** Создавать отдельный workspace/service identity для WELLBEING и хранить ключ только во внешнем secret store. Никаких ключей в GitHub.

## Текущие цены и роли моделей

Официальная pricing page сейчас даёт в том числе:

| Модель | Роль по официальной cost-optimization guidance | Input / 1M | Output / 1M |
|---|---|---:|---:|
| `Claude Haiku 4.5` | простые/дешёвые задачи | $1 | $5 |
| `Claude Sonnet 5` | основная production-нагрузка | $2 | $10 |
| `Claude Opus 5` | наиболее сложное reasoning | $5 | $25 |

Для prompt caching документация указывает 5-минутную запись 1.25× базовой input-цены, 1-часовую запись 2×, обычное cache read 0.1× базовой input-цены. Batch processing снижает input и output token cost на 50%.

Официальный источник:
- `https://platform.claude.com/docs/en/about-claude/pricing`

**Рекомендация проекта.**
- routine: Haiku;
- основная внешняя роль AUTHOR/VERIFIER: Sonnet как первый кандидат;
- тяжёлый независимый анализ: Opus только там, где добавочная стоимость оправдана измеряемым результатом.

Это проектная маршрутизация, не рейтинг Anthropic.

## Tool use и structured output

**Документировано.** Claude поддерживает user-defined/client tools и Anthropic server tools. Client tool вызывает structured tool request, который исполняет приложение; server tools вроде web search, web fetch, code execution и tool search исполняются на инфраструктуре Anthropic. Structured Outputs поддерживает JSON output и strict tool use на поддерживаемых моделях.

Официальные источники:
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview`
- `https://platform.claude.com/docs/en/build-with-claude/structured-outputs`

**Граница.** Server tools означают отдельный provider-side путь обработки. Их нельзя автоматически включать только потому, что модель их поддерживает.

## Search/file/computer boundaries

**Документировано.** Web search является server-side tool Anthropic. Computer/browser относятся к tool-модели, где фактическое действие выполняет приложение/окружение клиента. Files/stateful features имеют отдельные retention boundaries в документации Anthropic и не должны молча приравниваться к простому stateless Messages API.

Официальные источники:
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview`
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool`
- `https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool`

**Рекомендация проекта.** Первый Anthropic этап: plain Messages API + client-defined tools only when separately authorized; server web/search/computer/file-state не включать до отдельной проверки data-path.

## Rate limits

**Документировано.** Rate limits зависят от usage tier; Anthropic использует Start/Build/Scale tiers. Workspace может иметь более низкие spend/rate limits, но organizational limits всё равно действуют.

Официальные источники:
- `https://platform.claude.com/docs/en/api/rate-limits`
- `https://platform.claude.com/docs/en/manage-claude/workspaces`

## Практическая пригодность для WELLBEING

**Проектная рекомендация:** `ANTHROPIC_NEXT`, если не появится конкретный account/billing blocker.

Причины: прямой API route, понятная Haiku/Sonnet/Opus лестница, structured outputs, tool calling, cache и Batch. Хороший кандидат для независимой второй модельной линии после стабилизации OpenAI-first coordination path.

---

# 3. Google AI / Gemini API

## Доступ и аккаунт

**Документировано.** Gemini API требует API key. Google AI Studio для нового пользователя создаёт project + API key. Переход на paid tier увеличивает rate limits и требует Cloud Billing; текущая getting-started page указывает создание/привязку billing account, payment method и предварительное пополнение минимум на $5 (или эквивалент).

Официальный источник:
- `https://ai.google.dev/gemini-api/docs/get-started`

**Рекомендация проекта.** Для WELLBEING использовать отдельный Google project/key; ключ — только в secret store, не в GitHub.

## Модели и цена

**Документировано.** Current Models page на 2026-09-15 показывает:
- `gemini-3.1-flash-lite` — stable, cost-oriented Flash-Lite;
- `gemini-3.8-flash` — stable, наиболее интеллектуальный Flash для long-horizon software engineering, autonomous agents и complex enterprise workflows;
- `gemini-3.1-pro-preview` — preview-модель для advanced intelligence и complex problem solving.

Официальный источник:
- `https://ai.google.dev/gemini-api/docs/models`

Для `gemini-3.1-flash-lite` pricing page документирует Standard paid tier: $0.25/1M input tokens (text/image/video), $1.50/1M output tokens, context cache $0.025/1M плюс storage $1.00/1M tokens/hour.

Официальный источник:
- `https://ai.google.dev/gemini-api/docs/pricing`

**UNVERIFIED:** точная текущая цена `gemini-3.8-flash` и `gemini-3.1-pro-preview` не фиксируется в этом FAST_PATH, потому что извлечённый pricing fragment не дал безопасной однозначной привязки заголовка к каждой цене. Перед реальным вызовом цену выбранного exact model ID нужно перепроверить.

**Рекомендация проекта.**
- routine/high-volume: начать оценку с stable Flash-Lite;
- сложная работа: сравнивать stable `gemini-3.8-flash` и preview `gemini-3.1-pro-preview`, но preview не считать долгоживущим production default без отдельного решения.

## Function calling и structured output

**Документировано.** Gemini Function Calling соединяет модель с внешними tools/APIs: модель формирует имя функции и параметры, а приложение исполняет действие. Structured Outputs может ограничивать ответ переданной JSON Schema.

Официальные источники:
- `https://ai.google.dev/gemini-api/docs/function-calling`
- `https://ai.google.dev/gemini-api/docs/structured-output`

## Кэширование, Batch и асинхронность

**Документировано.** Gemini API имеет context caching. Batch API обрабатывает большой объём запросов асинхронно за 50% standard interactive cost; целевое время выполнения — до 24 часов. Для long-running/batch operations документированы webhook notifications.

Официальные источники:
- `https://ai.google.dev/gemini-api/docs/caching`
- `https://ai.google.dev/gemini-api/docs/batch-api`
- `https://ai.google.dev/gemini-api/docs/pricing`

## Search, File Search, Computer Use и другие tools

**Документировано.** В Gemini API есть built-in tools: Google Search, Google Maps, Code Execution, URL Context, File Search; custom tools подключаются через Function Calling. Computer Use находится в Preview и требует client-side execution environment.

File Search создаёт persistent File Search store: временный File object удаляется через 48 часов, а импортированные embeddings/data остаются до ручного удаления или депрекации модели. Это важная отдельная data-storage boundary.

Computer Use официально отмечен как Preview; Google рекомендует sandboxed VM/container и human supervision для важных действий.

Официальные источники:
- `https://ai.google.dev/gemini-api/docs/tools`
- `https://ai.google.dev/gemini-api/docs/google-search`
- `https://ai.google.dev/gemini-api/docs/file-search`
- `https://ai.google.dev/gemini-api/docs/computer-use`

**Рекомендация проекта.** Первый Google-маршрут делать без Search/File Search/Computer Use. Особенно не подключать File Search к project data до отдельного решения по persistent store.

## Rate/quota constraints

**Документировано.** Gemini rate limits применяются к project, а не к отдельному API key. Они зависят от модели и usage tier; preview/experimental модели могут иметь более жёсткие лимиты. Текущие лимиты следует смотреть в Google AI Studio.

Официальный источник:
- `https://ai.google.dev/gemini-api/docs/rate-limits`

## Практическая пригодность для WELLBEING

**Проектная рекомендация:** `GOOGLE_PARALLEL_OR_NEXT`.

Google подходит как третья независимая линия: есть стабильные Flash-модели, дешёвый Flash-Lite, rich tool surface и Batch. Но проект должен отдельно решить billing/project setup и не смешивать простой Gemini API call с persistent File Search, Google Search grounding или Computer Use.

---

# 4. Bounded implementation sequence

## Этап 1 — OpenAI first

**Рекомендация проекта.**

1. Создать/выделить отдельный API Project/service identity после отдельного OPERATOR authorization.
2. Secret — только внешний secret store/environment; GitHub остаётся без ключей.
3. Первый smoke path: text-only, no tools, exact model ID, synthetic/public-safe input.
4. Затем structured output/function calling.
5. Потом caching/Batch для стоимости.
6. Web search/file search/computer/MCP — только отдельными gates.

Текущая задача этого не авторизует.

## Этап 2 — Anthropic next

Если exact account/billing step не даёт внешнего блокера:

1. отдельный workspace/service identity;
2. plain Messages API;
3. exact model ID;
4. D0 synthetic route;
5. structured output/client tool call;
6. cache/Batch;
7. server web search/computer/files — отдельными data-path решениями.

Точный account-funding dependency сейчас: `UNVERIFIED`.

## Этап 3 — Google parallel/next

1. отдельный Google project/API key;
2. если нужен paid tier — Cloud Billing и задокументированное минимальное пополнение;
3. первый D0 — exact stable model, без Search/File Search/Computer Use;
4. затем JSON Schema/function calling;
5. caching/Batch;
6. Pro preview — только после exact price/model lifecycle recheck;
7. persistent File Search — отдельный storage/privacy gate.

---

# 5. Итог для решения

**Документированный факт:** все три провайдера имеют API-поверхность, function/tool mechanisms и способы структурировать ответы; у всех есть отдельные rate/quota/account boundaries. OpenAI, Anthropic и Google документируют механизмы, пригодные для агентной инфраструктуры, но их tool/data paths различаются и должны разрешаться отдельно.

**Рекомендация проекта:**

`OpenAI first → Anthropic next → Google parallel/next`.

Причина — не «кто умнее», а минимальная последовательность интеграционного риска: сначала уже принятая OpenAI-линия, затем независимый direct Anthropic route, затем Google с его project/billing и большим набором built-in tools.

## Что этим brief НЕ разрешено

- создавать аккаунты;
- покупать тарифы/кредиты;
- создавать или запрашивать API keys;
- выполнять live provider calls;
- передавать provider'у данные проекта;
- включать search/file/computer/tools;
- публиковать credentials;
- менять authority/status проекта.

---

# 6. Telemetry FAST_PATH

- `tool_calls`: 22
- `source_reads`: 19 official-provider pages/fragments materially inspected
- `github_reads`: 8 prewrite/preflight reads/searches + 1 exact task read
- `github_writes`: 0 at document-build point; Exchange Gate writes follow separately
- `retries`: 0
- `reconciliations`: 1
- `operator_rewakes`: 0
- `budget_exceeded`: yes
- `budget_exceeded_reason`: current RED writer boundary had no single explicit repository marker, so admission required several narrow current/handoff/search checks; provider facts were split across pricing, tools, auth, quota and model pages for three providers. After sufficient evidence for each required scope item, research stopped.

## INSTANCE_ADMISSION

`PASS_CURRENT_RED_WRITER_NO_CONFLICT_FOUND`

Проверка текущего `entities/redaktor/current/` показала актуальный RED current-state; `entities/redaktor/handoff/` не содержит competing handoff/current-writer artifact; поиски по wellbeing-hq не нашли conflicting RED writer marker. Этот же чат является продолжающимся RED writer instance текущей цепочки и получает exact addressed task. Противоречащего current-writer evidence не обнаружено.

---

КТО: RED / РЕДАКТОР
ДЛЯ ЧЕГО: компактный операторский brief по OpenAI / Anthropic / Google API для следующего этапа multi-model infrastructure
СТАТУС: `PASS_PROVIDER_OPERATOR_BRIEF_R01`
