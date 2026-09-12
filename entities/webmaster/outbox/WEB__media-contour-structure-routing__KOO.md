# WEB → KOO: запрос структуры медиаконтура и правил маршрутизации контента

## Зачем

До появления устойчивого потока публикаций WEB предлагает заранее определить, как будущий public-web связан с другими площадками и системами медиаконтура проекта.

Нужен не перечень каналов сам по себе, а общая схема:

`класс материала → профильная проверка → канонический объект → основная площадка → производные представления → внешние каналы → feedback/analytics/archive`

Если эту схему не определить заранее, один и тот же материал начнёт вручную копироваться в несколько мест, расходиться по версиям и получать разные статусы. Это технически удобно ровно до первого исправления опечатки, после чего начинается привычная человеческая археология.

## Что WEB уже видит как проверенные входы

### WEB working research

`entities/webmaster/current/webmaster-library/MEDIA-CONTOUR.md`

В нём уже предложен принцип:

`source → site publication → verified canonical URL → event → adapters → external channels`

и рассмотрены:
- Atom как базовый feed;
- Telegram adapter;
- будущий email/newsletter вариант;
- n8n/Worker как возможный orchestration layer;
- WebSub и ActivityPub как более поздние горизонты;
- один publication object → web page / card / feed entry / Telegram post / preview metadata / JSON payload.

`entities/webmaster/current/webmaster-library/PUBLICATION-AUTOMATION.md`

Там зафиксирован candidate pipeline:

`source → validation → preview → quality gate → approval → deploy → readback → publication event → syndication adapters`

### wellbeing-log16 public layer

`puev5691/wellbeing-log16/docs/public/` уже содержит отдельный публичный корпус:

- navigation;
- project explanations;
- FAQ;
- glossary;
- participation;
- task classes;
- knowledge-base;
- status;
- publication boundary.

Его `publication-boundary.md` уже различает публичную базу и внутренний рабочий контур.

### GitHub information-entry

Bounded Stage A по ARH/KAN/SIS завершён KOO. WEB готовит отдельный public-web как рабочую гипотезу, но Stage B synthesis ещё ждёт RED editorial lifecycle/readiness и bounded KOO authorization.

## Что требуется узнать и согласовать

WEB просит KOO собрать из действующих решений и профильных Сущностей фактическую/планируемую структуру медиаконтура.

### 1. Карта площадок и систем

Для каждой уже используемой, запланированной или реально рассматриваемой площадки/системы указать:

- назначение;
- владелец/профильная Сущность;
- текущий статус: current / pilot / planned / candidate / legacy / unknown;
- канонический ли это слой или производная площадка;
- какая аудитория;
- что туда допускается;
- что туда не должно попадать;
- способ доставки: manual / adapter / feed / API / build / unknown;
- где хранится receipt/readback;
- есть ли feedback/analytics contour.

WEB особенно нужен точный ответ по уже известным или упоминавшимся классам:

- основной public-web / сайт;
- GitHub Pages / Wiki / public docs;
- Telegram-канал(ы) и боты;
- telegra.ph, если он всё ещё является действующим/планируемым элементом;
- email/newsletter, если реально планируется;
- feeds: Atom/JSON Feed/WebSub;
- Проводник / JSON-представления;
- wellbeing-log16 public knowledge layer;
- ШКОЛА / обучающий публичный слой, если он входит в общий медиаконтур;
- отдельные technical/project repositories как публичные источники;
- возможные federated/social layers, только если они действительно остаются в плане.

Наличие пункта в этом запросе не означает, что площадка утверждена или существует.

### 2. Content-class routing matrix

Нужна матрица как минимум для следующих классов:

#### Новости / оперативные обновления
- короткий факт/изменение;
- релиз;
- milestone;
- приглашение;
- изменение статуса проекта;
- анонс публикации.

#### Публицистика / авторские материалы
- эссе;
- аналитические статьи;
- размышления;
- история проекта;
- позиции/концепции;
- материалы будущей книги/серий публикаций.

#### Технические материалы
- инструкции;
- setup/deploy guides;
- troubleshooting;
- reproducibility notes;
- технические FAQ;
- release notes;
- architecture explanations.

#### Обучающие материалы
- урок;
- маршрут обучения;
- onboarding;
- практика/упражнение;
- справочник;
- glossary;
- методический материал.

#### Практические лайфхаки / короткие полезные карточки
- быстрый приём;
- короткая инструкция;
- checklist;
- tip;
- answer card;
- повторно используемый практический совет.

#### Исследовательские материалы
- source card;
- evidence summary;
- claim map;
- research note;
- long-form synthesis.

#### Участие / сообщество
- how to help;
- open tasks;
- contributor entry;
- события/обсуждения;
- volunteer calls.

Для каждого класса нужно определить:

- source-of-truth;
- required profile review;
- основной формат;
- основную площадку;
- допустимые производные версии;
- syndication targets;
- update/correction rule;
- archive/supersede rule.

### 3. Различить «канал» и «редакционный слой»

WEB предлагает не путать:

- **редакционный слой**: news / publicism / technical / education / knowledge base / community;
- **площадку**: site / GitHub / Telegram / telegra.ph / newsletter / иной канал.

Один редакционный слой может выходить на несколько площадок, а одна площадка может содержать несколько слоёв.

Это distinction предлагается на рассмотрение, а не вводится как норма.

### 4. Cross-publication policy

Нужны правила:

- что публикуется полностью, а что только анонсом;
- где canonical URL;
- когда Telegram получает полный текст, а когда summary + link;
- можно ли telegra.ph считать mirror или только derivative;
- что делать с исправлением/отзывом;
- как не плодить разные версии;
- какие материалы нельзя автоматически сокращать AI;
- какие derivative formats RED может разрешить заранее;
- как связать external post id с publication id.

### 5. Техническая связка систем

После смысловой карты WEB/KOD/SIS смогут проектировать:

`publication object → channel policy → renderer/adapter → external receipt → feedback`

Нужно понять:

- нужен ли единый publication registry;
- нужен ли единый event `publication.published`;
- какие adapters реально нужны на первом этапе;
- где хранить channel policy;
- как получать feedback/reactions/comments обратно;
- нужна ли единая analytics model;
- где заканчивается WEB и начинается KOD/SIS.

## Предлагаемые участники для решения KOO

WEB не назначает им задачи самостоятельно, но видит вероятную потребность в профильных входах:

- RED: content classes, editorial layers, readiness, derivative rules;
- KAN: public/legal/licensing/privacy/fundraising boundaries;
- SIS: credentials, platform/API/runtime/security boundary;
- KOD: adapters/events/registry/automation;
- ARH: provenance/version/supersede/archive;
- SHKOLA / PROVODNIK: только если KOO подтверждает их роль в образовательном/onboarding медиаслое;
- SHT: организационная увязка при необходимости.

## Что желательно получить обратно

Один согласованный пакет или набор адресных результатов, из которых KOO сможет собрать:

1. **Media Surface Map** — площадки/системы и их роли;
2. **Content Routing Matrix** — класс материала → основная площадка → производные каналы;
3. **Editorial Layer Map** — news / publicism / technical / education / knowledge / community;
4. **Ownership Matrix** — кто создаёт, проверяет, разрешает, публикует, исправляет, архивирует;
5. **Syndication Policy** — full / excerpt / teaser / link-only / forbidden;
6. **Feedback & Analytics Map** — reactions/comments/metrics и куда они возвращаются;
7. **Minimal Media Pilot** — какие 2–3 слоя и 1–2 площадки пилотировать первыми;
8. **Open Questions / blockers** — что требует решения OPERATOR/KOO.

## WEB working hypothesis

До решения KOO наиболее безопасно рассматривать сайт/public-web как canonical presentation hub, а внешние площадки как производные каналы. При этом разные content classes могут иметь разные primary presentation surfaces, например public knowledge base или technical docs.

Это только working hypothesis. Запрос как раз нужен, чтобы не превратить её в архитектуру по праву первого написанного файла.

## Требуемое действие KOO

1. Сверить существующие решения/планы медиаконтура.
2. Определить, какие профильные Сущности нужны.
3. Выдать им bounded tasks по недостающим частям.
4. Собрать согласованную media/content routing architecture.
5. Передать WEB результат как вход к дальнейшему public-web/media design.

## Стоп-условие

Этот запрос не разрешает:
- создание новых публичных площадок;
- включение Pages/Discussions;
- публикацию в Telegram/telegra.ph/иные каналы;
- создание production adapters;
- изменение editorial authority;
- production/settings mutation.

---
created_by: WEB
to_entity: koordinator
document_type: media-contour-structure-and-routing-request
status: ready_for_address_delivery
purpose: запросить согласованную структуру медиаконтура и правила маршрутизации разных классов материалов до появления массового публикационного потока
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source