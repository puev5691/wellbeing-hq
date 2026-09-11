# WEB: multi-repo source map для будущего public-web

status: working-research
decision_status: not_decided
production_changed: false
repository_settings_changed: false

## Назначение

Будущий отдельный public-web repository не должен становиться новым местом ручного копирования всего проекта. Его задача — собирать только разрешённые публичные представления из нескольких профильных репозиториев с сохранением provenance, immutable identity и статусов.

Этот документ фиксирует результаты текущего read-only сканирования доступных репозиториев `puev5691` и предлагает режимы их использования.

Наличие репозитория не означает, что его содержимое разрешено публиковать или считать current truth.

## 1. Режимы подключения источников

### `curated-content`
Репозиторий может давать отдельные материалы в public-web, но только через allowlist путей и профильные gates.

### `metadata-only`
Сайт может читать ограниченную служебную metadata: статус, locator, release/commit identity, публичные summary. Тело служебных материалов не импортируется.

### `technical-curated`
Технический репозиторий используется только для проверенных технических страниц/статусов после профильной проверки KOD/SIS/RED/KAN по применимости.

### `historical-curated`
Исторический/experience слой допускает только специально подготовленные обезличенные/очищенные выводы. Raw corpus запрещён для автоматического public ingestion.

### `external-reference-only`
Fork/upstream/external code не импортируется как собственный материал проекта. Сайт может давать ссылку/атрибуцию и использовать только материал с проверенным rights basis.

### `exclude-by-default`
Не сканировать содержимое для публикации без отдельного решения.

## 2. Проверенная карта репозиториев

| Repository | Проверенное назначение/состояние | Candidate mode | Что сайт может читать | Что не импортировать автоматически |
|---|---|---|---|---|
| `wellbeing-hq` | операционный HQ: entities/inbox/outbox/current, routes, receipts, registry | `metadata-only` | approved/public-safe status projections, explicit public manifests, immutable locators | inbox/outbox, dispatch/receipts, activation evidence и внутренние документы целиком |
| `wellbeing-log16` | лабораторный knowledge/dialogue проект; уже есть `docs/public/` | `curated-content` | allowlisted `docs/public/**` после status/public gates | внутренние config/src/tests и draft без маркировки/approval |
| `wellbeing-cooperation` | исследовательский корпус по кооперации; source/claim pipeline | `curated-content` | verified/supported cards, public syntheses, speech/public materials после profile gate | источники с `rights_unknown`, unresolved claims, полные third-party originals |
| `wellbeing-experience` | continuity/experience corpus; raw + extracted experience + tests/views | `historical-curated` | специально подготовленные reusable lessons/views после scrubbing/approval | `raw/**`, pathology/history dumps, private/sensitive context |
| `wellbeing-entity-bootstrap` | воспроизводимая инициация/recovery/headers/manifests/profiles | `metadata-only` | public-safe profile summaries, version/status manifests при необходимости | recovery packages, snapshots, внутренние initiation details по умолчанию |
| `wellbeing-archivist` | код и data/query/service layer Архивариуса | `technical-curated` / `metadata-only` | проверенный public status продукта, docs при отдельной редакционной подготовке | internal data/config/state и служебные registry details |
| `wbn2026` | TERA-derived clone development repository; README содержит upstream TERA + примечание о clone development | `technical-curated` | проверенные WBN-specific docs/status, если KOD подтверждает source/branch | upstream README как будто это собственное описание WBN; непроверенные финансовые/technical claims |
| `wbchain-lab` | техническая лаборатория на TERA codebase, ветка `wblab` | `technical-curated` | отдельные verified lab results/status pages | runtime/deploy/config details без SIS review; upstream text как project claim |
| `teraOrigin` | TERA origin/baseline code/docs | `external-reference-only` / technical baseline | locator/version для provenance и сравнений | зеркалирование upstream documentation как собственный материал проекта |
| `wellbeing` | публичный TERA code/doc repository; README фактически upstream TERA description | `external-reference-only` / legacy technical candidate | только после выяснения роли этого repo в current WBN lineage | считать README текущим описанием «БЛАГОПОЛУЧИЯ» |
| `MiroFish` | verified fork of `666ghj/MiroFish`, AGPL-3.0 | `external-reference-only` | ссылки, attribution, project-use note при подтверждении | выдавать fork-код/README за собственную разработку |
| `PromeTorch` | verified fork of `barometech/PromeTorch`, license metadata `NOASSERTION` | `external-reference-only` | locator/attribution после rights check | автоматический reuse/public copy без проверки лицензии |
| `sglang` | verified fork of `sgl-project/sglang`, Apache-2.0 | `external-reference-only` | locator/attribution, dependency/reference info | собственная project authorship claim |
| `HAS` | private; содержимое в текущем GitHub-доступе не прочитано | `exclude-by-default` | ничего до отдельной доступности/authority | любые догадки о содержимом |


## 3. Уже обнаруженный сильный public-source candidate

`wellbeing-log16/docs/public/` фактически содержит:

- `navigation.md`;
- `faq/`;
- `glossary/`;
- `knowledge-base/`;
- `participation/`;
- `project/`;
- `status/`;
- `tasks/`;
- `publication-boundary.md`;
- README/draft materials.

Это означает, что public-web должен уметь подключать **подготовленные public projections из профильных репозиториев**, а не заставлять WEB вручную переписывать их в site repo.

Но README `wellbeing-log16` прямо называет систему лабораторным прототипом, а часть public materials — draft. Поэтому даже путь `docs/public/**` не является автоматическим approval.

## 4. Candidate architecture: source registry в site repo

В отдельном public-web repository стоит иметь versioned allowlist, например концептуально:

```yaml
sources:
  - repo: puev5691/wellbeing-log16
    mode: curated-content
    allow:
      - docs/public/**
    deny:
      - docs/public/root-readme-backups/**
    owner: LOG16/profile-owner
    required_gates:
      - semantic_status
      - public_legal
      - editorial

  - repo: puev5691/wellbeing-hq
    mode: metadata-only
    allow:
      - explicit-public-manifests-only
    required_gates:
      - provenance
      - public_legal

  - repo: puev5691/wellbeing-experience
    mode: historical-curated
    allow:
      - explicitly-approved-public-views-only
    deny:
      - raw/**
```

Имена/формат только candidate. Главный принцип: **deny by default, allow by exact repo/path/status contract**.

## 5. Что должен делать scanner

Scanner не должен «копировать всё новое». Его работа:

1. получить список зарегистрированных source repos;
2. проверить immutable head/commit;
3. определить изменения только в allowlisted paths;
4. прочитать source metadata/status;
5. проверить required gates;
6. сформировать candidate import manifest;
7. не публиковать blocked/unknown автоматически;
8. построить preview;
9. после approval выполнить build;
10. после deploy выполнить readback;
11. сохранить source repo + commit/blob → public URL mapping.

## 6. Событийная модель

Для каждого source repo нужен индивидуальный способ обнаружения изменений.

Candidate варианты:

- scheduled pull/check GitHub API;
- explicit repository dispatch/event из source repo;
- PR/merge в public-content path;
- release/tag event для technical project status;
- manual approved manifest.

На первом sandbox безопаснее scheduled/read-only scanner + explicit allowlist: он не требует раздавать write credentials всем source repos.

Event-driven cross-repo dispatch можно добавлять позже, когда KOD/SIS определят credential/authority model.

## 7. Нельзя смешивать `source` и `presentation`

Public-web repository должен хранить для импортированного объекта минимум:

- source repository;
- source path;
- source commit/blob;
- semantic status;
- source owner;
- public/legal state;
- editorial state;
- transformation version;
- public URL;
- publication/readback evidence.

Если source object изменился или superseded, site copy должна либо обновиться, либо явно показывать stale/superseded state. Молчаливое вечное копирование запрещено.

## 8. Особые правила по классам

### HQ

Никогда не делать общий recursive crawl `entities/**`, `routes/**`, `registry/**` для public site. Только специально подготовленные public manifests/projections.

### Experience

`raw/**` — hard deny для automatic public pipeline.

### Cooperation

Source registry и claims требуют различения provenance/rights/status. `rights_unknown` и `unresolved` не должны попадать как утверждённая публичная истина.

### Technical/WBN

Сайт не должен строить network/performance/economic claims непосредственно из README/кода. Требуется профильный verified status artifact.

### External forks

Fork existence может показывать используемые/исследуемые технологии, но authorship и licensing должны сохраняться.

## 9. Следующий Stage B вопрос для KOO/KOD/SIS/ARH

Нужно определить общепроектный `public-export contract`:

- кто имеет право помечать объект exportable;
- где живёт allowlist;
- кто валидирует provenance/status;
- каким immutable событием source object считается готовым к public-web;
- кто снимает/суперседит материал;
- как scanner получает read access;
- как сайт узнаёт об изменениях;
- какие репозитории являются source repos, а какие только references.

## 10. Короткая фиксация опыта

Идея → отдельный сайт должен сканировать не только HQ, а всё профильное GitHub-поле.

Проба → перечислены доступные repositories, прочитаны назначения ключевых repo и проверены root/public структуры.

Результат → обнаружены разные классы источников: operational HQ, public knowledge, research corpus, experience, recovery/bootstrap, technical labs и external forks.

Успех → вместо «сканировать весь GitHub» сформирован безопасный принцип multi-repo allowlist + per-repo mode + provenance.

Неудача/ограничение → private `HAS` не удалось прочитать текущим GitHub-доступом; содержимое не классифицировано.

Фиксация → этот multi-repo source map.

---

created_by: WEB
document_type: multi-repo-public-source-map
status: working-research
purpose: определить безопасный multi-repo ingestion model для отдельного public-web repository
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source