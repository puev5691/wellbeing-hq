# Безопасные пилоты ВЕБМАСТЕРА

## Назначение

Очередь самостоятельных экспериментов, которые можно выполнять после согласования приоритетов, не трогая существующий production.

## P0. Read-only карта текущего веб-контура

Это по-прежнему базовая задача после cold-start.

Проверить и зафиксировать:

- фактические сайты/домены;
- доступные web-репозитории;
- текущие published pages;
- Проводник;
- document roots и build/deploy mechanism, если доступны read-only;
- DNS/HTTPS только как наблюдаемое состояние, без присвоения профильной authority;
- current/legacy/unknown.

Результат: карта фактов, на которую можно накладывать новые технологии.

## P1. Standalone publication prototype

Отдельный каталог/репозиторий, никак не связанный с production credentials.

Одна Markdown-публикация -> HTML -> sitemap -> Atom.

Проверяемый результат: build artifact и preview URL.

## P2. Preview + quality gates

Добавить GitHub Actions:

- schema validation;
- build;
- link check;
- Lighthouse CI;
- artifact retention.

Результат: commit/PR нельзя считать publish-ready, пока gate не PASS.

## P3. Post-deploy readback

После test deployment workflow проверяет опубликованный URL и marker/version.

Результат: различаются `deployed` и `verified_published`.

## P4. Telegram dry-run adapter

Сформировать payload Telegram без отправки.

Вход: `publication.published.json`.

Выход: нормализованный текст/caption + target metadata + idempotency key.

Результат можно проверять без bot token.

## P5. Telegram sandbox

После отдельного разрешения и выдачи безопасного тестового канала подключить Bot API.

Проверить:

- create;
- edit/correction;
- retry;
- duplicate prevention;
- сохранение external message id.

Production channel не использовать на пилоте.

## P6. Editorial UI

Поднять Decap CMS поверх prototype content repo.

Проверить сценарий:

`draft -> review -> preview -> approve -> merge`.

Цель — понять, сможет ли РЕДАКТОР/автор работать через браузер без Git-команд.

## P7. n8n comparison

На sandbox сравнить два варианта Telegram adapter:

A. GitHub Action/маленький Worker;
B. self-hosted n8n.

Сравнивать не по количеству красивых блоков, а по:

- поддержке retries;
- журналу;
- secrets;
- portability;
- сложности backup/recovery;
- ресурсоёмкости;
- возможности добавлять новые каналы.

## P8. WebSub

Когда появятся хотя бы два независимых подписчика на feed, проверить hub-based push.

До этого polling/обычный feed проще.

## P9. Federated media spike

Только после стабильного P0-P8: короткое исследование ActivityPub/Micropub для собственного публичного узла проекта.

Не смешивать с первой версией сайта.

## Критерий готовности медийного контура

Контур можно считать технологически зрелым, когда новый материал проходит путь:

`approved source -> deterministic build -> preview/gates -> production -> readback -> syndication -> external receipts`

и по любому опубликованному объекту можно восстановить исходный commit и результаты доставки.

---

entity: WEB
document_type: pilot-backlog
status: working_research_candidate
production_changed: false
project_time: generated_without_trusted_project_time
