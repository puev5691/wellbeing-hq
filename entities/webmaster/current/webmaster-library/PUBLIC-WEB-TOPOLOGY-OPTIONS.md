# WEB: варианты топологии публичного GitHub-информационного входа

## Статус

status: working-research
decision_status: not_decided
production_changed: false
repository_settings_changed: false

Этот документ сравнивает технические и организационные варианты будущего публичного GitHub-входа проекта. Он не создаёт репозиторий, не включает Pages/Discussions, не меняет `wellbeing-hq` и не утверждает архитектуру.

## 1. Проверенная исходная ситуация

`puev5691/wellbeing-hq` сейчас:

- public repository;
- по README предназначен как операционный транспортный слой: Entity inbox/outbox/current, handoff, routes, receipts;
- Wiki enabled;
- Issues enabled;
- Projects enabled;
- Pages disabled;
- Discussions disabled;
- repository homepage not set;
- repository license metadata not set;
- `.github/workflows/` содержит служебные `entity-activation-detector.yml` и `exchange-gate.yml`.

ARH Stage A baseline, принятый KOO в ограниченной границе, требует сохранять semantic status, provenance, canonical locator/identity и не превращать navigation в механизм повышения статуса.

KAN вернул Stage A public/legal result `PASS_WITH_BOUNDED_BLOCKERS`, но его KOO acceptance на момент этой фиксации ещё не подтверждён. Поэтому KAN-result учитывается как incoming profile result, а не утверждённая общепроектная норма.

## 2. Что должен обеспечивать будущий public-entry

Независимо от топологии будущий слой должен уметь:

- вести посетителя по аудиториям, а не по внутренней структуре Сущностей;
- отделять current/approved от candidate/research/legacy/archive;
- не публиковать blocked/unknown объекты как current truth;
- давать canonical locator и provenance;
- отделять operational evidence от публичных материалов;
- поддерживать Pages/сайт, документацию/Wiki, roadmap/tasks и contributor entry;
- позволять preview/build/readback до синдикации;
- не делать внешний канал единственным source-of-truth;
- поддерживать sandbox до production.

## 3. Option A: отдельный public-web repository

### Суть

Создать отдельный репозиторий публичного информационного слоя. Условное рабочее имя здесь не задаётся канонически.

В нём могут жить:

- GitHub Pages source/build;
- public content;
- public metadata/schema;
- community files;
- contributor onboarding;
- public roadmap projections;
- feeds;
- public navigation;
- при необходимости Wiki/Discussions, если отдельно разрешены.

Из `wellbeing-hq` в public repo попадают только классифицированные и разрешённые объекты или производные представления.

### Candidate flow

    approved/allowed source
        ↓
    classifier / export manifest
        ↓
    public-web repository
        ↓
    validation / preview / review
        ↓
    GitHub Pages
        ↓
    readback
        ↓
    feed / syndication adapters

### Сильные стороны

- чёткое separation of concerns: operational HQ отдельно, public media отдельно;
- проще минимизировать риск экспонирования inbox/dispatch/receipts;
- проще public licensing/community policy;
- проще contributor UX;
- проще ограничить publishing workflow только публичным набором данных;
- отдельный sandbox/preview не затрагивает HQ transport layer;
- можно включать Discussions/Wiki/Pages на public repo без превращения HQ в общественный форум;
- легче позднее перенести hosting, сохранив Git-first content model.

### Риски/цена

- появляется ещё один репозиторий и правила синхронизации;
- нужен строгий export/import provenance;
- возможны stale copies, если update/supersede pipeline слабый;
- нужно решить, где source-of-truth, а где presentation copy;
- нужны права на создание/настройку нового repo.

### Ключевой инвариант

Public repo не становится новым смысловым source-of-truth автоматически. Он должен хранить либо approved public source, либо явно производное представление с provenance.

## 4. Option B: public layer внутри wellbeing-hq

### Суть

Добавить в HQ отдельный каталог/branch/build surface для публичного сайта.

Например концептуально:

    wellbeing-hq
      ├─ entities/
      ├─ routes/
      ├─ registry/
      └─ public-site/   ← candidate only

или держать build source в отдельной ветке.

### Сильные стороны

- меньше репозиториев;
- близость к operational metadata;
- проще ссылаться на immutable objects внутри одного repo;
- одна permissions model для части операций.

### Риски

- public и operational слои смешиваются в одном repository security boundary;
- ошибка workflow/filter может экспонировать лишнее;
- contributor experience будет соседствовать с внутренними Entity paths;
- community files репозитория будут одновременно относиться к HQ transport и public audience;
- Discussions/Issues сложнее однозначно трактовать: internal operations или public community;
- license policy одного repo сложнее отделить от разнородных файлов и third-party evidence;
- Pages deployment теснее связан с operational repository.

### Candidate assessment

Технически возможно, но организационно выглядит менее чисто при текущем назначении HQ как transport repository.

## 5. Option C: account-level GitHub Pages portal

### Суть

GitHub поддерживает user/account site на специальном repository, связанном с account-level `github.io` адресом.

Такой слой может быть верхней дверью:

    root portal
       ↓
    project pages / public repos
       ↓
    wiki / docs / roadmap / community

### Возможная роль

- короткая визитная карточка;
- список проектов/направлений;
- маршрутизация на Wellbeing public-web;
- developer/support entry.

### Сильные стороны

- короткий верхний адрес GitHub Pages;
- удобен как общий портал нескольких репозиториев;
- не требует превращать HQ в сайт.

### Ограничения

- нужно отдельно проверить, существует ли/занят ли соответствующий account-level Pages repo;
- имя и внешний бренд привязаны к GitHub account;
- если проектов станет несколько, portal не должен смешивать их governance;
- не решает сам по себе Wiki/content lifecycle;
- требует отдельного authority/settings decision.

### Candidate assessment

Скорее верхний redirect/portal layer, чем основное content repository.

## 6. Wiki в трёх вариантах

GitHub Wiki технически является отдельным Git-backed хранилищем для репозитория и может клонироваться отдельно. Изменения default branch публикуются читателям.

### При Option A

Wiki public-web repo может стать глубокой документацией внешнего контура, а Pages — индексируемой витриной.

### При Option B

Wiki `wellbeing-hq` рискует смешать внутреннюю operational документацию и публичный onboarding. Перед использованием нужно фактически классифицировать уже существующее Wiki-содержимое.

### При Option C

Account portal сам по себе не решает Wiki. Документацию всё равно разумнее привязать к профильному project/public repo.

## 7. Discussions

GitHub Discussions предназначены для открытых вопросов, ответов, объявлений и разговоров сообщества; visibility наследуется от repository.

Следовательно:

- включать Discussions в public repo концептуально естественно;
- включать их в `wellbeing-hq` означает открыть community-разговор прямо на operational transport repo;
- до community guidelines/moderation ownership включение Discussions преждевременно.

## 8. Pages и Actions

GitHub Pages поддерживает custom workflows через GitHub Actions и раздельные build/deploy jobs.

Для проекта это важно, потому что позволяет построить цепочку:

    content → validation → build → artifact → deploy → readback

и не связывать архитектуру с ручной публикацией файлов.

Но текущие HQ workflows `entity-activation-detector` и `exchange-gate` являются operational workflows; использовать их как publication pipeline нельзя без отдельного дизайна.

## 9. Сравнительная матрица

| Критерий | Option A separate public repo | Option B inside HQ | Option C account portal |
|---|---|---|---|
| Separation public/operational | сильное | слабее | сильное, но только portal |
| Риск случайной экспозиции HQ | низкий при хорошем exporter | выше | низкий |
| Простота provenance | требует export manifest | проще внутри repo | зависит от downstream repo |
| Contributor UX | чистый | смешанный | хороший как вход, не как work repo |
| Wiki fit | хороший | требует разделения internal/public | косвенный |
| Discussions fit | хороший | спорный | обычно не основной слой |
| Pages fit | хороший | технически хороший, организационно спорный | хороший для landing |
| Licensing/community policy | проще отделить | сложнее | отдельно для portal |
| Масштабирование публикаций | хорошее | среднее | portal-only |
| Количество repo | +1 | без нового repo | +1 portal repo, возможно + public repo |
| Предварительная WEB оценка | основной кандидат | fallback/компромисс | дополнительный верхний слой |


## 10. Предварительная WEB-гипотеза

Без изменения каких-либо настроек наиболее чистой выглядит комбинация:

    account/project entry (опционально)
             ↓
    separate public-web repository
             ↓
    Pages + public docs/Wiki + contributor/community layer
             ↑
    controlled export/provenance
             ↑
    wellbeing-hq / approved sources / profile results

`wellbeing-hq` при этом остаётся операционным транспортом.

Это working hypothesis. Решение требует KOO, KAN, SIS, RED и authority на repository/settings.

## 11. Что нужно подтвердить до архитектурного выбора

1. KOO acceptance/revision KAN Stage A result.
2. SIS security/infrastructure boundary для separate repo и Pages Actions.
3. RED editorial lifecycle.
4. Фактическое содержимое текущей HQ Wiki и его public/internal classification.
5. Возможность/authority создать отдельный public repository.
6. License/right policy.
7. Нужно ли использовать account-level Pages portal.
8. Community moderation owner для Discussions.
9. Public roadmap policy для Issues/Projects.
10. Export/supersede/readback contract между source и presentation layer.

## 12. Внешние технические справки

Эти ссылки являются внешними справочными источниками, не Project Sources:

- GitHub Pages custom workflows:
  https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- GitHub Wiki editing/cloning:
  https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages
- GitHub Discussions:
  https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions

## 13. Короткая фиксация опыта

Идея → сравнить public topology до того, как появится разрешение что-либо включать.

Проба → сопоставлены назначение HQ, current feature state, Stage A provenance/legal inputs и актуальные возможности Pages/Wiki/Discussions.

Результат → выделены три топологии; separate public-web repo выглядит наиболее чистым основным кандидатом, account-level portal — возможным дополнительным входом, in-HQ site — компромиссным вариантом.

Успех → архитектурный выбор теперь можно обсуждать через явные trade-offs, а не через вкус к названиям репозиториев.

Ограничение → это working hypothesis; нет KOO acceptance KAN-result, SIS/RED boundaries и repository-creation authority.

Фиксация → этот файл в WEB current library.

---

created_by: WEB
document_type: public-web-topology-options
status: working-research
purpose: сравнить варианты GitHub public-entry до Stage B architecture decision
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source