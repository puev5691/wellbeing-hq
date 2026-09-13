# Anthropic / Claude — цена доступа и технические возможности

status: CURRENT_OPERATOR_BRIEF
provider_priority: Anthropic first
fallback_provider: Google acceptable
project_time: omitted; trusted project-time source not used

## Коротко

Для первого реального внешнего пилота проекту имеет смысл идти напрямую через Claude API, без агрегатора.

Рекомендуемый первый модельный кандидат KOO: `claude-sonnet-5` — не потому, что он «лучший вообще», а потому что сейчас это наиболее дешёвый сбалансированный способ проверить интеграцию, tool use и agentic workflow на реальном Anthropic API.

После проверки механики можно отдельно сравнить `claude-opus-5` и `claude-fable-5-1` на более тяжёлых задачах.

## 1. Текущая цена API

По свежим официальным материалам Anthropic:

### Claude Sonnet 5

- input: `$2 / 1M tokens`
- output: `$10 / 1M tokens`
- модель: `claude-sonnet-5`

Пример порядка стоимости:
100k входных + 10k выходных токенов ≈ `$0.30`.

Официальный источник:
https://www.anthropic.com/news/claude-sonnet-5

### Claude Opus 5

- input: `$5 / 1M tokens`
- output: `$25 / 1M tokens`
- модель: `claude-opus-5`

Пример:
100k входных + 10k выходных токенов ≈ `$0.75`.

Официальный источник:
https://www.anthropic.com/news/claude-opus-5

### Claude Fable 5.1

- input: `$10 / 1M tokens`
- output: `$50 / 1M tokens`
- cache read: `$0.25 / 1M tokens`
- модель: `claude-fable-5-1`

Пример без учёта cache:
100k входных + 10k выходных токенов ≈ `$1.50`.

Официальный источник:
https://www.anthropic.com/claude-fable-and-mythos-5-1

Цены относятся к API/token billing и не равны стоимости подписки Claude.ai.

## 2. Доступ

Для direct route нужен Claude Platform / Claude API account и API key.

Типовой клиент использует переменную:
`ANTHROPIC_API_KEY`

Официальная документация Claude Platform прямо предусматривает:
- получение API key;
- Messages API;
- SDK;
- Playground;
- usage/rate-limit controls в Claude Console.

Документация:
https://docs.anthropic.com/

Rate limits зависят от usage tier/account state. Anthropic сейчас использует уровни `Start / Build / Scale`; точные доступные limits надо смотреть в Claude Console конкретной организации, поэтому KOO их не выдумывает заранее.

## 3. Что технически умеет текущая платформа

Официально поддерживаются, в зависимости от модели/режима:

- Messages API;
- streaming;
- adaptive thinking / effort control;
- client-side tool use;
- server-side tools;
- prompt caching;
- batch processing;
- Files API;
- PDF processing;
- vision/image input;
- structured outputs;
- web search;
- code execution;
- MCP connector;
- Managed Agents;
- computer/browser use на поддерживаемых моделях.

Claude Platform docs:
https://docs.anthropic.com/

## 4. Контекст

Для современных Sonnet 5 / Opus 5 / Fable 5-линий официальная документация указывает контекст до `1M tokens` на поддерживаемых платформах/маршрутах.

Для Opus 5 и Fable 5 документация также указывает большие output limits и long-horizon agentic workloads.

Это делает Claude интересным не только как отдельный чат, а как worker для длинных проектных задач с большим контекстом, tool use и проверяемыми артефактами.

## 5. Tool / agent возможности, особенно полезные проекту

### Sonnet 5

Anthropic позиционирует его как наиболее agentic Sonnet: планирование, coding, browser/terminal tool use, многошаговое выполнение. По цене это хороший первый реальный worker.

### Opus 5

Сильнее ориентирован на deep reasoning, coding и long-horizon agentic tasks. Поддерживает computer use/browser use на Claude API.

### Fable 5.1

Самый дорогой из рассматриваемых вариантов; Anthropic позиционирует его как наиболее мощный вариант для сложной knowledge/coding работы. Имеет особенно дешёвые cache reads, что может быть интересно для больших повторно используемых проектных контекстов.

## 6. Дополнительные расходы

Некоторые server tools тарифицируются отдельно.

Пример: web search в Claude API — `$10 / 1000 searches` плюс обычная token стоимость результатов/ответа.

Официальная документация web search:
https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool

## 7. Рекомендуемый первый эксперимент

### Этап A — без расходов API

KOD готовит direct Anthropic adapter для текущего local multi-model gateway:
- provider = Anthropic;
- first model = `claude-sonnet-5`;
- data class = только `D0_SYNTHETIC`;
- API key только через environment/secret boundary;
- tools/search/fallback выключены;
- hard cost ceiling;
- immutable request/result provenance.

### Этап B — человеческий шаг

ОПЕРАТОР:
- создаёт/подтверждает Claude Platform account;
- включает billing/credits, если Anthropic этого требует;
- создаёт API key;
- передаёт его только через approved secret mechanism, не GitHub.

### Этап C — первый live D0 request

Одна синтетическая задача, малый token budget, один exact model, без project/private данных.

После этого KOO сравнивает:
- стоимость;
- latency;
- качество;
- provenance;
- удобство интеграции;
- ограничения/rate limits.

Только после успешного D0 решается вопрос о D1 или роли Anthropic как AUTHOR/VERIFIER worker.

## 8. Что пока не разрешено

- D2+;
- private/project-sensitive data;
- unlimited spend;
- production routing;
- automatic provider fallback;
- secrets in GitHub;
- считать Claude.ai Pro/Max подписку заменой API billing.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ русскоязычное текущее описание цены, доступа и технических возможностей Anthropic перед первым D0 pilot
СТАТУС: current_operator_brief
