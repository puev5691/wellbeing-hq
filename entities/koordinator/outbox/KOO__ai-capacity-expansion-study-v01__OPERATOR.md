# KOO — исследование наращивания вычислительных возможностей ШТАБА v0.1

status: RESEARCH_RESULT__PILOT_RECOMMENDED
scope: capacity, model diversification, parallel execution, routing
external_publication: no
project_time: omitted; trusted project-time source not used

## 1. Вывод

Рост времени ожидания вызван не только недостатком "умности" одной модели. В текущем ручном контуре есть три разных ограничения:

1. **quota/compute** — одна Сущность упирается в лимит доступных вычислений и длину/сложность прохода;
2. **serialization** — ОПЕРАТОР вручную будит одну Сущность, затем ждёт результат, затем запускает следующую;
3. **single-model concentration** — одинаковые классы работ конкурируют за один и тот же дорогой reasoning-ресурс, хотя значительная часть работы дешевле и может выполняться другими моделями параллельно.

Поэтому увеличение только тарифа полезно, но не является достаточным решением.

Целевая архитектура должна быть:

`KOO scheduler → task decomposition → model/router selection → parallel bounded workers → immutable results → independent verifier → KOO dependency reconciliation → next route`.

## 2. Что даёт повышение тарифа ChatGPT

OpenAI сейчас разделяет индивидуальные Pro-уровни по объёму использования.

По официальной справке:
- Plus: $20/месяц;
- Pro $100: примерно 5× usage относительно Plus;
- Pro $200: примерно 20× usage относительно Plus;
- новые покупки/upgrade Pro $200 временно приостановлены с 10 сентября 2026;
- Pro $100 остаётся доступным;
- Pro даёт более высокие лимиты, Pro reasoning, максимальные Codex/deep-research возможности и больший контекст.

Практический вывод:

**Pro $100 — разумный немедленный шаг, если текущий bottleneck действительно quota/usage.**

Но это не создаёт независимые параллельные workers и не решает exact Entity activation.

Источники:
- https://help.openai.com/en/articles/9793128-what-is-chatgpt-pro/
- https://help.openai.com/en/articles/6950777-wh
- https://chatgpt.com/pricing/

## 3. OpenAI API как вычислительный слой

Текущая линейка:
- GPT-5.6 Sol: $4/M input, $20/M output, context 1.05M;
- GPT-5.6 Terra: $2/M input, $12/M output, context 1.05M;
- GPT-5.6 Luna: $0.20/M input, $1.20/M output, context 1.05M.

Это позволяет разделить работу:
- Luna — классификация, preflight summaries, extraction, queue reconciliation;
- Terra — обычный технический анализ, drafting, средняя сложность;
- Sol — final reasoning, cross-pipeline decisions, сложные проверки.

Тем самым дорогой model-time перестаёт тратиться на рутинную сортировку.

Источники:
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://developers.openai.com/api/docs/models/gpt-5.6-terra
- https://developers.openai.com/api/docs/models/gpt-5.6-luna

## 4. Anthropic / Claude

Актуально интересны два класса:

### Claude Sonnet 5
- $2/M input;
- $10/M output;
- позиционируется для coding, knowledge work и agentic execution.

### Claude Opus 5
- $5/M input;
- $25/M output;
- более сильный уровень для сложной инженерной/knowledge work проверки.

Claude Pro стоит $20/месяц помесячно; Max начинается от $100 и даёт 5× или 20× usage относительно Pro.

Практическая роль для ШТАБА:
- независимый code review;
- второй reasoning opinion для KOO/KAN/SHT;
- кодовые/репозиторные задачи через Claude Code;
- независимая модель-ревизор, чтобы author и verifier не были одной системой.

Источники:
- https://www.anthropic.com/pricing
- https://platform.claude.com/docs/en/about-claude/pricing
- https://www.anthropic.com/news/claude-opus-5
- https://www.anthropic.com/news/claude-sonnet-5

## 5. Google Gemini

Gemini API сейчас особенно интересен не как "ещё один чат", а как набор специализированных agent/model сервисов.

Подтверждённые возможности:
- Gemini 3.1 Pro: ~1.05M input context, text/image/video/audio/PDF input, code execution, function calling, search grounding, URL context;
- Gemini 3.8 Flash: модель для long-horizon software engineering, autonomous agents и enterprise workflows;
- отдельные managed models: Deep Research, Deep Research Max, Computer Use, Antigravity Agent;
- Gemini Deep Research умеет планировать многошаговое исследование по множеству источников;
- Antigravity Agent получает isolated Linux sandbox, умеет работать с кодом, файлами и web.

Consumer tiers:
- Google AI Pro: $19.99/месяц;
- Google AI Ultra: от $99.99/месяц, более высокие лимиты и agent/deep-think функции.

Практическая роль:
- длинные мультимодальные документы;
- независимый web/deep research;
- managed sandbox-agent для bounded внешних исследований;
- отдельный multimodal verifier.

Источники:
- https://ai.google.dev/gemini-api/docs/models
- https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview
- https://gemini.google/subscriptions/

## 6. GitHub Copilot как готовый multi-model слой для КОДЕРА

Это один из наиболее интересных вариантов именно для текущей архитектуры проекта.

GitHub Copilot сейчас предоставляет:
- cloud agent;
- code review;
- CLI/IDE agent mode;
- возможность delegate tasks coding agents;
- third-party agents, включая Claude Code и Codex;
- широкий model catalog OpenAI / Anthropic / Google / xAI / другие.

Individual tiers:
- Pro: $10/месяц;
- Pro+: $39/месяц;
- Max: $100/месяц.

Pro+ включает premium models и существенно больший AI-credit pool; Max предназначен для sustained high-volume agent workflows.

Это может позволить вынести часть очереди KOD непосредственно в GitHub, где agent получает repository context и возвращает commit/PR/result вместо длинного диалога.

**Для ШТАБА GitHub Copilot Pro+ выглядит более полезной второй покупкой после увеличения основного ChatGPT compute, чем покупка ещё одного обычного consumer chat.**

Источник:
- https://github.com/features/copilot/plans

## 7. xAI / Grok

API имеет модели с крупным context:
- Grok 4.6: 500k, $2/M input, $6/M output;
- Grok 4.3 и Grok 4.20 family: до 1M context;
- function calling / structured outputs / configurable reasoning;
- отдельные X Search/server tools.

Ниша для проекта:
- independent cross-check;
- X/social-web research, если это реально требуется;
- дополнительный agent/tool-calling backend.

Не вижу оснований покупать его первым. Он полезен как специализированный backend после появления общего router.

Источники:
- https://docs.x.ai/developers/models
- https://docs.x.ai/developers/pricing

## 8. Mistral

Плюсы:
- низкая API-цена;
- широкий диапазон моделей;
- специализированные OCR/audio модели;
- европейский поставщик;
- удобен как дешёвый worker для document/OCR/routine processing.

Примеры API:
- Mistral Large 3: $0.5/M input, $1.5/M output;
- Mistral Small 4: $0.15/M input, $0.6/M output;
- Ministral family ещё дешевле;
- OCR тарифицируется отдельно по страницам.

Роль:
- массовая обработка;
- документы/OCR;
- дешёвые независимые проверки;
- потенциальная база для local/private веток, если будут выбраны подходящие веса/развёртывание.

Источники:
- https://docs.mistral.ai/inference/pricing
- https://mistral.ai/pricing/

## 9. DeepSeek

Текущий API особенно агрессивен по цене:
- DeepSeek V4 Flash / Pro;
- context 1M;
- thinking/non-thinking;
- JSON, tool calls, Responses API;
- OpenAI- и Anthropic-compatible API surfaces.

Цена V4 Flash:
- cache-miss peak примерно $0.44/M input;
- output peak примерно $1.32/M;
- off-peak ниже.

V4 Pro:
- cache-miss peak примерно $1.32/M input;
- output peak примерно $3.96/M.

Роль:
- массовые background/subagent задачи;
- дешёвые классификации и first-pass reviews;
- резервный provider.

Ограничение: до использования с проектными данными требуется отдельная privacy/data-governance проверка. Низкая цена не является разрешением отправлять ему чувствительное содержимое.

Источник:
- https://api-docs.deepseek.com/quick_start/pricing/

## 10. Как объединить поставщиков

### Вариант A — OpenRouter

Уже умеет:
- несколько моделей в одном API;
- provider routing;
- automatic fallback;
- выбор по price / throughput / latency;
- BYOK;
- ограничения data collection / Zero Data Retention endpoints.

Плюс: очень быстрый путь к эксперименту.

Минус: появляется дополнительный посредник и дополнительная trust/data boundary.

Источники:
- https://openrouter.ai/docs/guides/routing/provider-selection
- https://openrouter.ai/docs/guides/routing/model-fallbacks

### Вариант B — собственный LiteLLM gateway

LiteLLM предоставляет:
- единый OpenAI-compatible API к 100+ LLM;
- router / retry / fallback;
- budgets и spend tracking;
- возможность поднять Proxy Server как собственный LLM Gateway.

Для архитектуры БЛАГОПОЛУЧИЯ это стратегически интереснее:
`entities → project LLM gateway → provider adapters`.

KOO/SHT смогут задавать routing policy, а secrets каждого поставщика останутся в одном системном контуре.

Источник:
- https://docs.litellm.ai/

## 11. Предлагаемая специализация моделей

Не делать "одна Сущность = одна нейросеть".

Делать "тип шага = класс вычислительного ресурса".

### CLASS L — дешёвый массовый worker
Задачи:
- preflight;
- diff classification;
- extraction;
- registry consistency;
- candidate triage;
- checksum/result summarization.

Кандидаты:
GPT-5.6 Luna, Mistral Small, DeepSeek V4 Flash, Gemini Flash.

### CLASS M — основной профильный worker
Задачи:
- bounded review;
- код;
- анализ документов;
- draft технического решения;
- тестовый план.

Кандидаты:
GPT-5.6 Terra/Sol, Claude Sonnet 5, Gemini 3.8 Flash.

### CLASS H — дорогой verifier / сложный reasoning
Задачи:
- KOO final decision;
- SHT cross-layer review;
- KAN sensitive semantic/legal review;
- architectural conflict;
- independent adversarial check.

Кандидаты:
GPT-5.6 Sol/Pro/Astra where available, Claude Opus 5, Gemini Pro/Deep Think.

### CLASS S — специализированный
Задачи:
- deep research;
- computer use;
- OCR;
- audio;
- image/video;
- web/social research.

Выбор конкретного сервиса по способности, а не по привычке.

## 12. Правило независимой проверки

Для значимых решений желательно:

`AUTHOR(provider A) → VERIFIER(provider B) → KOO acceptance`.

Это не гарантирует истину, но снижает correlated model error и одновременно превращает multi-provider архитектуру в реальный контроль качества, а не в коллекцию подписок.

## 13. Что покупать первым

### Шаг 1 — немедленный capacity relief
Если текущий ChatGPT plan упирается в usage:
**ChatGPT Pro $100**.

Причина:
- 5× usage против Plus;
- больше reasoning/context/Codex/deep research;
- минимальное изменение текущей рабочей схемы.

Не пытаться сейчас строить план вокруг Pro $200: новые upgrades временно закрыты.

### Шаг 2 — coding parallelism
**GitHub Copilot Pro+ $39** как пилот.

Причина:
- cloud agent;
- code review;
- multi-model catalog;
- Claude Code + Codex;
- работа прямо рядом с текущим GitHub information field.

Если реальная нагрузка быстро съест Pro+ pool, тогда оценивать Max $100 по фактической статистике.

### Шаг 3 — API pilot вместо множества consumer subscriptions
Не покупать одновременно Claude Max + Gemini Ultra + Grok + Mistral consumer plans.

Выделить небольшой capped API budget и проверить:
- Anthropic Sonnet 5;
- Gemini Flash/Pro;
- DeepSeek V4 Flash;
- Mistral Small/Large;
- OpenAI Luna/Terra/Sol.

Для первых опытов использовать либо OpenRouter с жёсткими data/provider настройками, либо собственный LiteLLM gateway.

### Шаг 4 — измерить
На каждой задаче фиксировать:
- task class;
- model/provider;
- tokens/cost;
- latency;
- pass/fail;
- human/KOO correction required;
- verifier disagreement;
- final accepted result.

После 50–100 реальных bounded tasks будет понятно, что покупать, а что было красивой маркетинговой мебелью.

## 14. Что НЕ решит покупка дополнительных моделей

Не исчезнут автоматически:
- exact Entity-chat activation;
- current-writer/recovery;
- Exchange Gate;
- provenance;
- authority;
- dependency scheduling.

Модель может выполнить работу, но **право выполнить её и доказательство, что выполнилась именно нужная задача над нужной версией**, остаются функциями нашей архитектуры.

## 15. Предлагаемый следующий технический результат

Не подключать новые API сразу.

Сначала подготовить отдельную спецификацию:

`KOO__multi-model-worker-gateway-pilot-spec-v01.md`

В ней определить:
- task classes L/M/H/S;
- разрешённые providers;
- data sensitivity classes;
- model selection/fallback;
- author/verifier separation;
- budget caps;
- immutable request/result envelope;
- provider/model/version provenance;
- timeout/retry;
- exact handoff обратно в Exchange Gate;
- запрет поставщику автоматически менять project state.

После SHT/KAN review можно дать KOD bounded implementation task на локальный gateway prototype без реальных project secrets.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: оценить варианты увеличения вычислительных ресурсов и привлечения сторонних нейросетей без разрушения provenance/authority модели проекта
СТАТУС: research_result__pilot_recommended
