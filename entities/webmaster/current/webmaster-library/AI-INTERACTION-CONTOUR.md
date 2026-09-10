# AI-взаимодействие для WEB и медийного контура

## Назначение

Эта записка фиксирует рабочую идею: использовать GitHub Copilot и внешние AI/поисковые/специализированные системы как подключаемых помощников проекта, не передавая им право самостоятельно определять истину, утверждать канон или публиковать в production.

Контур относится к WEB там, где речь идёт о сайте, документации, публикациях, поисковой видимости, web-quality и contributor experience. Общепроектная оркестрация нескольких AI-систем выходит за границы одного WEB и требует участия KOD/KOO.

## Что реально есть у GitHub сейчас

### GitHub Copilot

По актуальной документации GitHub Copilot умеет не только дополнять код, но и:

- исследовать репозиторий;
- выполнять ограниченные задания через cloud agent;
- брать задачи из Issues и создавать ветки/PR;
- проводить code review;
- работать с custom agents;
- использовать Agent Skills;
- использовать Copilot Spaces как курируемый контекст;
- подключать внешние данные и инструменты через MCP;
- работать с partner/third-party agent apps;
- запускать Copilot automations по расписанию и событиям там, где эта функция доступна.

### Важное ограничение

GitHub Models как отдельный сервис уже закрыт. По документации GitHub он полностью retired 30 июля 2026 года. Новую архитектуру на GitHub Models не строить.

### Ограничение Copilot Automations

Cloud Copilot automations доступны только для private/internal repositories.

Текущий репозиторий `puev5691/wellbeing-hq` фактически public, поэтому использовать Copilot Automations непосредственно в нём нельзя при текущей конфигурации.

Это не препятствует использованию обычных GitHub Actions, Copilot agent sessions/code review и будущего отдельного private/internal служебного контура, если такой будет отдельно утверждён.

## Где WEB может получить практическую пользу

### 1. Второй разработчик, но через PR

Безопасный шаблон:

    Issue/задача
      ↓
    bounded instructions
      ↓
    Copilot agent
      ↓
    отдельная ветка / PR
      ↓
    tests + web quality
      ↓
    Copilot code review
      ↓
    WEB/KOD review
      ↓
    approval
      ↓
    merge/deploy отдельным разрешённым действием

Copilot не должен писать напрямую в production и не должен сам считать свою работу принятой.

### 2. Автоматическая проверка сайта

Полезные задачи для AI-помощника:

- найти битые ссылки;
- проверить навигацию;
- сравнить sitemap и реальные страницы;
- найти дубли/мертвые страницы;
- проверить metadata/canonical/OpenGraph;
- проверить соответствие content schema;
- подготовить accessibility-review;
- объяснить Lighthouse/Core Web Vitals регрессии;
- проверить, что публикационный pipeline не создаёт дубликаты;
- собрать changelog изменений сайта;
- предложить тесты.

Фактические измерения должны выполняться инструментами. LLM интерпретирует результаты, но не подменяет измерение.

### 3. Помощник документации и Wiki

Copilot/custom agent можно использовать для:

- создания черновика структуры Wiki;
- проверки внутренних ссылок;
- выявления противоречий между README/Pages/Wiki;
- предложения cross-links;
- подготовки onboarding;
- технического резюме изменений;
- формирования glossary candidate.

Смысл профильных документов остаётся за их владельцами. AI не становится автором канона только потому, что Markdown получился красивый.

### 4. Помощник публикационного конвейера

AI может готовить производные материалы:

- краткое описание;
- teaser;
- варианты заголовка;
- теги;
- alt-text candidate;
- перевод candidate;
- краткую версию для Telegram;
- список связанных публикаций;
- FAQ candidate.

Публичная публикация требует обычного approval-маршрута. Для юридически и репутационно значимых материалов AI-generated текст должен рассматриваться как черновик.

### 5. Вход разработчиков

Copilot может помочь:

- классифицировать Issues;
- готовить reproduction steps;
- находить подходящие `good first issue`;
- объяснять архитектуру новичку;
- предлагать документацию к PR;
- проверять contributor instructions.

В public repository автоматическое действие по входящему контенту от неизвестных пользователей особенно опасно из-за prompt injection. Read-only/limited tools по умолчанию.

## Самая перспективная идея: опыт Сущностей как Agent Skills

GitHub поддерживает Agent Skills: каталог инструкций, скриптов и ресурсов с `SKILL.md`, который агент загружает для специализированной работы. Формат описан как открытый стандарт и применяется не только Copilot.

Для проекта это может стать машинно-исполняемым слоем накопленного опыта.

Примеры будущих skills:

- `web-publication-readback` — как проверять факт публикации;
- `web-broken-link-audit` — как собирать и проверять карту ссылок;
- `web-no-production-without-approval` — стоп-условия production;
- `web-canon-source-check` — как отличать approved/candidate/legacy;
- `web-media-syndication` — как готовить производные версии публикаций;
- `web-experience-card` — формат «идея → проба → результат → вывод → фиксация».

Важно: сторонние skills нельзя ставить вслепую. GitHub прямо предупреждает о prompt injection и вредоносных скриптах; skill нужно предварительно инспектировать и желательно pin-ить immutable version.

## Как взаимодействовать с другими нейросетями

Не строить архитектуру `WEB → конкретная модель`.

Предпочтительная схема:

    профильная задача
      ↓
    task package
      ↓
    AI broker / adapter layer
      ↓
    ├─ GitHub Copilot
    ├─ внешний general-purpose LLM
    ├─ поисковый/research agent
    ├─ специализированный анализатор
    └─ будущие агенты
      ↓
    structured result + evidence
      ↓
    validation
      ↓
    профильная Сущность
      ↓
    утверждённое действие

Так можно менять провайдера без изменения канона задачи.

## Открытые стандарты, которые стоит использовать

### MCP

Model Context Protocol задаёт стандарт подключения моделей к инструментам и данным.

Практический смысл для проекта:

- один MCP-сервер может давать контролируемый доступ к проектным данным;
- разные AI-клиенты могут использовать одинаковые инструменты;
- можно разделить read-only и write toolsets;
- права можно давать минимально;
- внешняя модель не обязана получать полный архив проекта.

GitHub Copilot официально поддерживает MCP.

### A2A

Agent2Agent — открытый протокол для взаимодействия AI-агентов, переданный в Linux Foundation. В 2026 году проект заявляет production-ready статус и поддержку более чем 150 организаций.

В перспективе это интереснее самодельных «бот вызывает бота по своему JSON», но внедрять A2A имеет смысл только после появления реальной межагентной задачи.

### AGENTS.md

GitHub Copilot поддерживает repository instructions через `.github/copilot-instructions.md` и `AGENTS.md`.

Для проекта это может быть способом дать разным coding agents компактные проверяемые правила конкретного репозитория:

- границы роли;
- approved sources;
- запрет production mutation;
- required tests;
- правила файлов;
- routing requirements.

Это не заменяет проектный канон, а предоставляет агенту operational-проекцию канона.

## Поисковые и специализированные системы

Задачи поиска нужно отделять от задач синтеза.

### Поисковый слой

В зависимости от темы можно подключать:

- обычный web search;
- GitHub code search;
- поисковые API;
- научные индексы;
- репозитории нормативных/официальных источников;
- специализированные каталоги и базы.

Поисковик выдаёт кандидаты источников. LLM не должен превращать snippets в установленный факт без чтения источника.

### Research layer

Для исследования WEB интересны:

- поиск современных web-технологий;
- сравнительный анализ generator/deployment вариантов;
- мониторинг изменений GitHub Pages/Copilot;
- поиск accessibility/performance практик;
- поиск документации API внешних площадок.

Результат исследования должен сохранять URLs, тезисы и разделение «подтверждено / вывод / гипотеза».

### Специализированный layer

В перспективе подключать отдельные инструменты там, где они лучше LLM:

- security scanners;
- link checkers;
- Lighthouse;
- accessibility engines;
- SEO validators;
- translation engines;
- OCR/vision для медиа;
- duplicate/plagiarism detectors;
- научные индексы;
- репозитории изображений и лицензий.

Принцип: специализированный инструмент измеряет, AI объясняет и помогает исправить.

## Правила безопасности и доверия

1. Внешний AI — не источник истины.
2. Его вывод — candidate до проверки.
3. Read-only доступ по умолчанию.
4. Write — только в отдельную ветку/PR или sandbox.
5. Никаких production secrets в prompt.
6. Минимальные tool permissions.
7. Содержимое Issues/PR/web pages считать потенциально враждебным prompt input.
8. Никакого auto-merge для значимых изменений на первом этапе.
9. Никакой автоматической публичной публикации AI-generated текста без профильного approval.
10. Каждая значимая AI-задача должна оставлять проверяемый результат: PR, файл, отчёт, evidence/links.
11. Несогласие нескольких моделей не решается голосованием моделей; конфликт возвращается профильной Сущности.
12. Стоимость/лимиты провайдеров учитывать до массовой автоматизации.

## Предлагаемый первый пилот

Не трогая production:

1. В отдельном sandbox создать минимальные repository instructions.
2. Создать один маленький WEB skill, например `web-publication-audit`.
3. Дать Copilot bounded Issue: проверить тестовый статический сайт и подготовить PR/отчёт.
4. Запросить Copilot code review.
5. Ту же задачу независимо проверить вторым AI/WEB.
6. Сравнить:
   - фактические находки;
   - ложные срабатывания;
   - пропуски;
   - соблюдение стоп-условий;
   - качество provenance;
   - стоимость/сложность.
7. Результат оформить в опыт:
   `идея → проба → результат → успех/неудача → фиксация`.

## Разделение ответственности

### WEB

Может исследовать и проектировать AI-assisted workflow для:

- сайта;
- Wiki;
- публикаций;
- feeds;
- contributor experience;
- web QA;
- media adapters.

### KOD

Должен участвовать, если появляется:

- общепроектный AI broker;
- MCP/A2A service;
- backend;
- общая библиотека agent skills;
- программная оркестрация нескольких моделей.

### KOO

Определяет:

- общепроектную норму;
- межсущностные права AI-агентов;
- canonical routing;
- можно ли вводить отдельную AI-Сущность/контур;
- какие действия допускаются автоматически.

## Фактическое состояние wellbeing-hq на момент проверки

Репозиторий:

- visibility: public;
- Wiki: enabled;
- Pages: disabled;
- Discussions: disabled;
- Issues: enabled;
- Projects: enabled.

Это только состояние репозитория, а не решение включать/выключать функции.

## Источники

GitHub Copilot:
https://docs.github.com/en/copilot

Copilot agents:
https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/overview

Copilot code review:
https://docs.github.com/en/copilot/concepts/agents/code-review

Agent Skills:
https://docs.github.com/en/copilot/concepts/agents/about-agent-skills

Custom agents:
https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents

Copilot Spaces:
https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/copilot-spaces/create-copilot-spaces

MCP:
https://docs.github.com/en/copilot/concepts/context/mcp
https://blog.modelcontextprotocol.io/posts/2026-07-28/

Copilot automations:
https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations

GitHub Models retirement:
https://docs.github.com/en/github-models

AGENTS.md / repository instructions:
https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide

A2A:
https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year

## Короткая фиксация опыта

Идея → использовать «нейронку GitHub» и другие AI как совместимых помощников проекта.

Проба → проверены актуальные возможности Copilot, Agent Skills, custom agents, MCP, A2A и ограничения GitHub Models/Copilot Automations.

Результат → полезнее строить не интеграцию с одной моделью, а adapter/broker архитектуру с проверяемыми результатами и минимальными правами.

Успех → найден особенно сильный механизм для накопления опыта: Agent Skills/AGENTS.md могут превратить проверенные проектные процедуры в переносимый operational-контекст для разных AI.

Ограничение → GitHub Models уже закрыт; cloud Copilot Automations нельзя использовать непосредственно в текущем public wellbeing-hq.

Фиксация → эта записка сохранена в WEB library; production и настройки репозитория не изменялись.

---

created_by: WEB
document_type: research-and-design-note
status: working-research
purpose: спроектировать полезное взаимодействие WEB/медийного контура с GitHub Copilot и внешними AI-системами
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source
