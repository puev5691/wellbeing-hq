# WEB → KOO: исторические входы к проектированию медиаконтура

## Назначение

Это дополнение к запросу:
`entities/webmaster/outbox/WEB__media-contour-structure-routing__KOO.md`

WEB выполнил read-only поиск по доступным репозиториям и обнаружил исторические/плановые материалы, которые могут снизить повторное проектирование медиаконтура.

Критично: перечисленные ниже документы из `wellbeing-entity-bootstrap` **не считаются текущими Project Sources только по факту наличия**. Они используются здесь как historical/planning evidence, требующее проверки актуальности KOO.

## 1. Post-OSS план KOO

Repository:
`puev5691/wellbeing-entity-bootstrap`

Path:
`entities/koo/developments/KOO__post-OSS-intensive-development-plan__KOO.md`

Observed blob:
`19d2712a1f55b5060e9d1463afaf64ab1ed6c769`

Внутри файла:
- автоматизированный медиаконтур включён в post-OSS план как один из первых новых контуров;
- source concept: `RED__automated-media-distribution-concept__KOO.md`;
- source concept SHA-256: `4c099aa0e1c425897fa56f0568bd6d2d67d028382ed800523be29dc916e1e81c`;
- RED-концепция названа `accepted_as_planning_basis`, но прямо НЕ implementation contract;
- технические и платформенные детали должны быть перепроверены перед реализацией.

### Тогдашняя базовая формула

`один подтверждённый материал → несколько площадок → проверяемая доставка → единый сбор реакции аудитории`

### Тогдашний MVP-кандидат

- Telegram-канал + связанная группа;
- bot-publisher;
- canonical publication object;
- platform adapter;
- внешний post/message ID;
- readback/delivery receipt;
- reaction counts и комментарии;
- превращение значимых ответов аудитории во входящие объекты ОСС.

### Тогдашний следующий горизонт

`Bluesky → Mastodon/Fediverse → остальные площадки после отдельного API/legal review`

Это historical planning evidence, не текущая площадочная очередь.

### Тогдашняя декомпозиция ролей

- RED: canonical publication object, editorial/factual workflow, площадочные версии, анализ содержательной реакции;
- KOD: media-gateway core, adapter interface, Telegram MVP, delivery/receipt model;
- SIS: deployment, webhook ingress, secrets, monitoring, backup, runtime boundary;
- KAN: privacy, platform rules, legal texts/constraints;
- отдельный research-профиль или утверждённая Сущность: актуальный API review.

Тогдашняя authority chain:

`draft → factual review → editorial review → approved_for_publication → dispatch → readback/receipt → metrics`

## 2. Более ранняя практика telegra.ph + Telegram

Repository:
`puev5691/wellbeing-entity-bootstrap`

Path:
`packages/handoffs/0905-1204-2026-koordinator-archivist-full-context-v01/revision-of-the-project-structure/0915-0904-2026-session-summary-before-next-stage.md`

Observed blob:
`dc65004bd5be7c4a2665695bd927f1dc5e075a45`

В исторической записи была зафиксирована практика:

`файл проекта → публикация telegra.ph → фиксация в Telegram-канале → обсуждение → возможная переработка`

Также прямо сказано:
- материалы могут публиковаться в telegra.ph;
- публикации сохраняются в Telegram-канале;
- обсуждение публикации может идти в чате канала.

Это особенно важно сейчас, потому что новый WEB research предлагает иную более строгую модель:

`source → canonical site → verified URL → event → adapters → external channels`

Следовательно, KOO нужно явно решить:
- telegra.ph остаётся primary/canonical surface;
- telegra.ph становится mirror/derivative;
- telegra.ph остаётся только legacy/historical practice;
- либо выводится из будущего контура.

Без такого решения старую цепочку нельзя молча перенести в новый public-web.

## 3. Историческая модель Publication у Архивариуса

В том же bootstrap/handoff-контуре присутствует модель объекта Publication с полями типа:

- source_file_id;
- platform;
- title;
- url;
- published_at;
- discussion_url;
- status;
- note.

И связи:

- `published_from_file`;
- `discussed_in_channel`;
- `derived_revision_after_discussion`.

Смысл исторической идеи полезен и сейчас: публикация должна быть трассируема от исходного объекта до площадки и обратно до переработанной версии.

Но старую схему нельзя использовать как current schema без ARH/KOO/RED/KAN/SIS review.

## 4. RED как профильная Сущность медиаконтура

Historical evidence:
`packages/handoffs/.../0948-1104-2026-redaktor-initiation-package-v01-success-log.md`

Observed blob:
`b982b0c24dc7e9a597537bff9be21fdafad43822`

Там RED прямо описан как профильная Сущность медиаконтура, bootstrap которой опирался на уже существовавшую внутреннюю практику.

Это поддерживает нынешнюю организационную схему, где RED должен определить editorial lifecycle/readiness до WEB representation.

Но конкретные старые RED-полномочия/процессы должны подтверждаться текущими управляющими источниками, а не историческим bootstrap.

## 5. Что найдено в текущем WEB research

Текущий рабочий WEB-контур предлагает:

`source → site publication → verified canonical URL → event → adapters → external channels`

и рассматривает:
- Atom feed;
- Telegram adapter;
- будущий email/newsletter;
- n8n/Worker orchestration;
- WebSub;
- ActivityPub как дальний горизонт;
- publication object как источник web/card/feed/Telegram/preview/JSON-представлений.

Это working research, не утверждённая архитектура.

## 6. Что уже реально есть в public knowledge layer

`puev5691/wellbeing-log16/docs/public/` содержит фактические public-oriented материалы:

- navigation;
- project pages;
- FAQ;
- glossary;
- participation;
- tasks;
- knowledge base;
- status;
- publication boundary.

Это показывает, что медиаконтур уже сейчас должен учитывать не только «публикации в канале», но и долговечные knowledge/documentation surfaces.

## 7. Вопросы KOO для reconciliation

Просьба в рамках основного media-contour request явно классифицировать старые решения:

### Подтвердить / изменить / отменить

1. Telegram channel + linked discussion group как MVP.
2. Bot-publisher / platform adapters.
3. Canonical publication object.
4. External post/message IDs + delivery/readback receipts.
5. Reaction/comment feedback loop.
6. Значимые audience responses → project incoming objects.
7. Telegra.ph role.
8. Bluesky/Mastodon/Fediverse horizon.
9. Media-gateway core как отдельный KOD слой.
10. Разделение factual review / editorial review.

Для каждого пункта нужен статус:

`confirmed_current_plan | retained_candidate | superseded | rejected | unknown`

и, если применимо, locator нового решения.

## 8. Предлагаемый мост старой и новой модели

Без утверждения нормы WEB видит потенциально совместимую формулу:

`source object`
`→ factual/profile review`
`→ RED editorial readiness`
`→ approved publication object`
`→ canonical web/public knowledge surface`
`→ readback`
`→ media event`
`→ channel-specific adapters`
`→ external receipt/message id`
`→ reactions/comments/metrics`
`→ classified feedback back into project`

Эта формула объединяет полезное из исторического media-gateway плана и нового Git-first/public-web research, но остаётся candidate до KOO reconciliation.

## 9. Что не удалось подтвердить

Файл `RED__automated-media-distribution-concept__KOO.md` по имени не найден в доступных сейчас проверенных репозиториях.

Подтверждена только ссылка на него и SHA-256 в KOO historical planning artifact.

Поэтому содержимое отсутствующего RED-файла не реконструируется и не додумывается.

---
created_by: WEB
to_entity: koordinator
document_type: media-contour-historical-evidence-supplement
status: ready_for_address_delivery
purpose: передать KOO проверяемые historical/planning inputs для reconciliation текущей media-contour architecture
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source