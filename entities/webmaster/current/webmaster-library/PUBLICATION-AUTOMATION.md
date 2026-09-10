# Автоматизация публикаций: предлагаемый конвейер

## Цель

Получить процесс, в котором один утверждённый материал превращается в сайт и внешние публикации без ручного копирования, но при этом каждый шаг проверяем и обратим.

## 1. Канонический объект публикации

Исходная статья хранится отдельно от HTML-представления, например:

`content/posts/<slug>.md`

Минимальные поля frontmatter:

- `id` — устойчивый идентификатор;
- `title`;
- `slug`;
- `summary`;
- `author/entity`;
- `status: draft|review|approved|published|withdrawn`;
- `tags`;
- `canonical_url` после первой публикации;
- `syndication` — какие адаптеры разрешены;
- `source_commit` — версия исходника, если нужна строгая provenance.

Время публикации нельзя выдумывать. Если проекту требуется проектная временная метка, она должна приходить из разрешённого проверяемого источника.

## 2. Pipeline

### Этап A: изменение исходника

Автор/РЕДАКТОР создаёт commit или pull request.

### Этап B: машинная валидация

До build проверяются:

- обязательные поля frontmatter;
- уникальность `id` и `slug`;
- внутренние ссылки;
- запрещённые/битые asset paths;
- формат Markdown/HTML;
- отсутствие случайно закоммиченных секретов;
- при необходимости словарь допустимых статусов и тегов.

### Этап C: preview build

Создаётся preview конкретной версии. Получатель review видит не diff разметки, а будущую страницу.

### Этап D: quality gate

Минимум:

- build PASS;
- link check PASS;
- HTML validation PASS;
- accessibility smoke test PASS;
- Lighthouse CI без критической регрессии;
- sitemap/feed generation PASS.

Пороговые значения лучше хранить как код в репозитории, а не помнить в голове.

### Этап E: approval

Production job использует GitHub Environment `production` с отдельными protection rules. При необходимости требуется reviewer. Секреты environment не доступны job до прохождения защиты.

### Этап F: deploy

Варианты:

- GitHub Pages для простого статического контура;
- Cloudflare Workers для нового более гибкого контура;
- существующий VDS, если аудит покажет, что его рационально сохранить.

Для внешнего cloud-provider предпочтителен OIDC и короткоживущие токены вместо постоянного deploy-secret, если провайдер это поддерживает.

### Этап G: readback

Deploy сам по себе не равен публикации. После deployment workflow должен проверить фактический URL:

- HTTP status;
- наличие ожидаемого `publication id` или content hash/marker;
- canonical URL;
- основные assets;
- при необходимости sitemap/feed.

Только после readback материал получает операционный статус `published`.

### Этап H: post-publish event

После подтверждённого readback формируется событие, например:

```json
{
  "event": "publication.published",
  "publication_id": "...",
  "canonical_url": "...",
  "title": "...",
  "summary": "...",
  "source_commit": "..."
}
```

Это событие передаётся адаптерам, а не заставляет site-core напрямую разговаривать со всеми соцсетями.

### Этап I: syndication adapters

Каждый адаптер возвращает собственный результат:

- channel;
- external message/post id;
- URL/locator;
- source publication id;
- статус;
- ошибка, если была.

Ошибка Telegram не должна откатывать уже состоявшуюся публикацию сайта. Она создаёт retry-задачу конкретного адаптера.

## 3. Планировщик

GitHub Actions поддерживает `on.schedule` с cron и timezone. Это позволяет реализовать очередь материалов с publish-after, если потом будет утверждён способ достоверно фиксировать требуемое время.

Альтернатива: внешний orchestrator (например n8n) получает очередь и инициирует публикацию через API/webhook.

## 4. Rollback

Нужны два разных rollback:

1. **сайт** — вернуть предыдущий проверенный deployment;
2. **синдикация** — удалить/исправить внешнюю публикацию или выпустить correction.

Нельзя считать удаление Telegram-поста эквивалентом отката канонической публикации.

## 5. Идемпотентность

Любой post-publish adapter должен уметь безопасно получить повторное событие. Ключом служит `publication_id + target_channel`.

Повторный запуск не должен создавать второй одинаковый пост, если первый уже подтверждён.

## 6. Наблюдаемость

Минимальный журнал публикации:

`publication_id -> source commit -> build run -> deploy identity -> canonical URL -> readback result -> syndication results`

Это позволяет ответить на простой вопрос «что именно сейчас опубликовано?» без археологических раскопок по чатам.

## 7. Безопасный первый прототип

Создать отдельный standalone prototype, который:

1. принимает один Markdown-файл;
2. строит одну HTML-страницу;
3. создаёт Atom feed и sitemap;
4. запускает Lighthouse CI;
5. публикует preview;
6. делает readback;
7. формирует локальный `publication.published.json`;
8. **не** имеет production credentials и не отправляет ничего в Telegram.

После проверки можно подключать один внешний адаптер.

---

entity: WEB
document_type: publication-pipeline-proposal
status: working_research_candidate
production_changed: false
project_time: generated_without_trusted_project_time
