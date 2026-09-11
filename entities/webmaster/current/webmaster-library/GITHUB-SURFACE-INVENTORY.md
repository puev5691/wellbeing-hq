# WEB: фактический inventory GitHub-поверхности wellbeing-hq

## Назначение

Этот документ фиксирует проверенное текущее состояние GitHub-возможностей репозитория `puev5691/wellbeing-hq` как вход для будущего Stage B information-entry architecture.

Это не решение о включении/выключении функций, не production architecture и не Project Source.

## 1. Репозиторий

repository: puev5691/wellbeing-hq
visibility: public
default_branch: main
archived: false
disabled: false
homepage: not set
repository license metadata: none

README определяет назначение репозитория как:

> Операционный репозиторий проекта: постоянные адреса Сущностей, рабочие входы/выходы, handoff и receipts.

README также прямо говорит, что этот репозиторий не заменяет active Project Sources, recovery-репозиторий или wellbeing-experience.

README blob: 3abde8a828bc6e688ec29cedc5d3286ecac153f6

## 2. GitHub feature state

| Feature | Verified state | Architectural meaning |
|---|---|---|
| Issues | enabled | может использоваться как task/contributor layer после отдельного дизайна |
| Projects | enabled | потенциальный roadmap/work layer |
| Wiki | enabled | потенциальный documentation layer; содержимое отдельно не классифицировано этой проверкой |
| Pages | disabled | `wellbeing-hq` сейчас не является GitHub Pages site |
| Discussions | disabled | community/discussion layer сейчас не включён |
| Repository homepage | not set | нет назначенной внешней landing URL в metadata |
| Repository license metadata | none | нельзя трактовать публичность репозитория как общую open-source/open-content лицензию |

Факт enabled/disabled не является решением сохранить состояние. Любое settings change требует отдельного разрешённого шага.

## 3. Текущая корневая структура

Проверены:

- `.github/`;
- `ENTITY-MAP.md`;
- `EXCHANGE-GATE.md`;
- `FILE-EXCHANGE-PROTOCOL.md`;
- `README.md`;
- `ROUTING.md`;
- `entities/`;
- `ops/`;
- `registry/`;
- `routes/`;
- `templates/`.

По структуре и README репозиторий явно ориентирован на внутренний операционный транспорт/координацию проекта, а не на внешний информационный вход для широкой аудитории.

## 4. Community / public-entry files

В `.github/` на момент проверки присутствует только каталог `workflows/`.

Не обнаружены в проверенной root/.github структуре:

- CONTRIBUTING;
- CODE_OF_CONDUCT;
- SUPPORT;
- SECURITY;
- issue templates;
- pull request template;
- community health profile files.

Это не означает, что такие материалы не существуют где-либо ещё в проекте. Вывод только о текущей проверенной структуре `wellbeing-hq`.

## 5. GitHub Actions state

В `.github/workflows/` фактически присутствуют два workflow:

1. `entity-activation-detector.yml`;
2. `exchange-gate.yml`.

То есть Actions уже используется как операционный механизм проекта.

Это подтверждает техническую пригодность GitHub Actions как части будущего information-entry/publishing sandbox, но существующие workflow нельзя автоматически считать publishing pipeline.

## 6. WEB working observation

### Candidate conclusion, не decision

Использовать сам `wellbeing-hq` как будущую публичную витрину выглядит рискованно и организационно неестественно, потому что:

- repository purpose уже определён как операционный транспортный слой;
- в нём живут inbox/outbox/dispatch/receipts/activation evidence и иные служебные объекты;
- KAN Stage A result вводит public/legal ограничения на operational evidence, personal data, secrets, unknown/conflict и rights basis;
- публичная navigation не должна смешивать operational evidence с approved/current public content;
- отсутствие общей license metadata требует отдельной rights-policy.

Поэтому для Stage B стоит сравнить минимум два варианта:

### Option A: separate public-web repository

Отдельный репозиторий для Pages/content/Wiki-facing public layer, который получает только разрешённые и классифицированные материалы/metadata из HQ через контролируемый pipeline.

Плюсы-кандидаты:

- separation of concerns;
- ниже риск случайно экспонировать operational field;
- проще licensing/community/public navigation;
- проще sandbox/preview/deploy boundary;
- понятнее внешний contributor experience.

### Option B: public layer inside wellbeing-hq

Отдельный каталог/branch/site build внутри HQ.

Потенциальные преимущества:

- меньше репозиториев;
- прямая близость к operational evidence.

Потенциальные риски:

- смешение public и operational контуров;
- сложнее фильтрация и permissions;
- выше цена ошибки publication pipeline;
- труднее объяснить внешний information architecture.

Выбор между вариантами не сделан. Это предмет будущего WEB Stage B после KOO/KAN/SIS/RED boundaries.

## 7. Что нужно проверить в Stage B

- фактическое содержимое/ценность GitHub Wiki;
- допустим ли отдельный public repository и кто имеет authority его создать;
- community files и contributor policy;
- Pages deployment model;
- preview/staging strategy;
- public metadata/schema contract;
- route из approved/current sources к public layer;
- update/supersede/delete behavior;
- доступ к public analytics без privacy violation;
- необходимость Discussions;
- связь Issues/Projects с public roadmap;
- license/right policy до маркировки open-source/open-content.

## 8. Короткая фиксация опыта

Идея → проверить, что GitHub уже реально предоставляет проекту до проектирования новой витрины.

Проба → сверены repository metadata, root tree, `.github`, workflows и README.

Результат → HQ является public operational transport repo; Wiki/Issues/Projects включены, Pages/Discussions выключены, общей license metadata нет, community layer почти не оформлен.

Успех → выявлен важный architectural candidate: отдельный public-web repository может быть безопаснее и чище, чем превращение `wellbeing-hq` в сайт.

Ограничение → это working observation, не архитектурное решение; Wiki content и SIS/KAN/KOO authority gates ещё требуют отдельной проверки.

Фиксация → этот inventory в WEB current library.

---

created_by: WEB
document_type: github-surface-inventory
status: working-research
purpose: зафиксировать фактическое состояние GitHub-поверхности wellbeing-hq для будущего Stage B information-entry architecture
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source