# SHD / ШАРДОВИК: план расширения через экспериментальный хостинг-контур

Кратко: этот документ фиксирует рабочее видение SHD по расширению возможностей проекта через связку `ChatGPT / Codex / apps / GitHub / remote host / experimental sandbox`. Это не закупочная директива, не production deployment и не разрешение менять серверы. Цель — подготовить безопасную платформу экспериментов, на которой SHD/KOD/SIS смогут проверять гипотезы без превращения production в учебный полигон.

## 1. Исходная вводная ОПЕРАТОРА

ОПЕРАТОР указал направление:

- выбрать один из хостингов и подготовить платформу для экспериментов;
- настроить формат работы `chatgpt.com`;
- подключить плагины/коннекторы для работы с хостингом и GitHub;
- обеспечить связку хостинга с GitHub;
- рассмотреть инструментарий OpenAI / Codex / Work;
- расширить подписку до Pro и использовать дополнительные возможности;
- расширять задачи и ресурсы постепенно, с проверяемыми шагами.

## 2. Текущая подтверждённая база

Подтверждённые рабочие опоры:

- `GitHub` connector доступен и уже используется для чтения/записи `puev5691/wellbeing-hq` и смежных репозиториев;
- `Remote Desktop Commander` установлен, один сервер/хост `ruvds-xnqc6` виден online;
- SHD имеет standing delegation на routine GitHub placement/dispatch собственных результатов, read-only диагностику и подготовку проверяемых пакетов;
- текущий SHD role profile закрепляет профиль WBN/WBNP/TERA2 diagnostics, cross-layer evidence и техническую интеграцию между KOD/SIS/KOO/ARH;
- текущая WBN/COOP ветка требует read-only проверки upstream/runtime/source parity и exact WBNP locator, но запрещает production mutation из handoff.

## 3. Принцип выбора платформы

Не начинать с production-серверов. Экспериментальный контур должен быть отделён от:

- действующего VPN/Xray контура;
- production-like WBN nodes;
- секретов и credentials;
- пользовательских данных;
- публичных surfaces, которые могут выглядеть как официальный релиз.

Минимальная правильная модель:

```text
ChatGPT Pro / Codex / Apps
        ↓
GitHub information field
        ↓
remote experimental host
        ↓
isolated workspaces / containers / scripts / reports
        ↓
verified artifacts back to GitHub
```

## 4. Рекомендуемый первый хостинг-контур

### 4.1. Немедленный вариант

Использовать уже подключённый `ruvds-xnqc6` только как первый управляемый endpoint для проверки Remote Desktop Commander и shell/file workflow.

Ограничение: не смешивать этот endpoint с production/security-sensitive задачами. Если он уже участвует в VPN/сетевом контуре, использовать его только для low-risk диагностических проверок и подготовки bootstrap-скриптов.

### 4.2. Правильный sandbox-вариант

Создать отдельный `lab-01` VPS/droplet/VM с чистой ОС.

Назначение `lab-01`:

- Codex/ChatGPT-controlled экспериментальный runtime;
- запуск read-only repo analysis;
- сборка и тесты KOD-пакетов;
- WBN/TERA2 source parity checks;
- контейнерные эксперименты;
- генерация отчётов и пакетов;
- никаких production credentials;
- никаких live public deployments без отдельного SIS/KOO approval.

## 5. Плагины и apps

Уже доступны:

- `GitHub` — чтение/запись репозиториев, issues/PR/code review/dispatch artifacts;
- `Remote Desktop Commander` — terminal/filesystem access к авторизованной машине.

Предложены к установке/подключению через ChatGPT UI:

- `DigitalOcean` — droplet as remote Codex workspace;
- `Render` — managed services/logs/metrics/deploys;
- `Railway` — app hosting / troubleshooting / project deployment;
- `Netlify` — static/frontend deployment.

Рабочий вывод SHD:

```text
DigitalOcean или обычный VPS = лучший первый sandbox для shell-first и Codex-like runtime.
Render/Railway = полезны позже для web services/API/demo.
Netlify = полезен позже для статических previews и публичных демонстраций.
```

## 6. Режим permissions

На стартовом этапе не ставить глобальный `full_access` для apps.

Рекомендуемый режим:

- GitHub: read allowed, write actions с явным подтверждением или в рамках установленной project delegation;
- Remote Desktop Commander: только для выделенного sandbox host; production hosts отдельно;
- hosting apps: provisioning/deploy/secrets только после явного ОПЕРАТОР/SIS/KOO approval;
- credentials/API keys: не публиковать в GitHub, хранить только в approved secret boundary;
- destructive actions: запрещены без отдельной задачи и rollback plan.

## 7. Базовая подготовка `lab-01`

Минимальный состав:

```text
OS: Ubuntu LTS / Debian stable
users: operator/admin + limited automation user
ssh: key-only, no password login
firewall: deny by default, allow SSH only initially
packages: git, curl, jq, python3, python3-venv, nodejs/npm, build-essential
runtime isolation: Docker or Podman
workspace: /data/wellbeing-lab
repos: cloned read-only or token-scoped clones
logs: /data/wellbeing-lab/logs
artifacts: /data/wellbeing-lab/artifacts
secrets: outside repo, mode 600, never committed
```

## 8. GitHub ↔ hosting рабочий контур

Первый безопасный цикл:

1. SHD/KOD/SIS создаёт task locator в `wellbeing-hq`.
2. ChatGPT/Codex читает exact locator.
3. На `lab-01` клонируется нужный repository/ref.
4. Выполняется read-only или bounded test.
5. Результат сохраняется как report/package.
6. Checksum/manifest формируются локально.
7. Redacted artifact публикуется обратно в GitHub.
8. Адресный dispatch отправляется профильной Сущности.

Запрещено на первом этапе:

- auto-deploy в production;
- auto-merge;
- auto-publish public demo;
- хранить токены в repo;
- использовать один и тот же host для secrets, production и экспериментов;
- считать успешный test релизным approval.

## 9. OpenAI / ChatGPT / Codex слой

Рабочая модель после перехода на Pro:

- ChatGPT Project: управляет текущей задачей, источниками, решениями ОПЕРАТОРА и короткими ответами;
- GitHub app: читает/пишет project information field;
- Codex/Work: выполняет длительные code/runtime задачи с GitHub context;
- Remote Desktop Commander: даёт terminal/filesystem на authorised host;
- optional hosting apps: создают или обслуживают sandbox/deployment provider;
- OpenAI API: подключать только для программных агентов/скриптов после отдельного budget/security решения.

Важно: API-ключ OpenAI не нужен для обычной работы ChatGPT/Codex в интерфейсе. Он нужен только если проект будет писать собственные сервисы/агентов, вызывающих OpenAI API из кода.

## 10. Первые задачи на sandbox

Приоритет SHD:

1. `lab-01` bootstrap readiness report.
2. GitHub clone/readback/checksum test.
3. WBN/TERA2 upstream source parity read-only check.
4. Exact WBNP locator scan по подтверждённым репозиториям.
5. COOP fit-gap matrix: concept → existing structure → FIT/PARTIAL/GAP/UNKNOWN → evidence locator.
6. Подготовка candidate runbook для KOD/SIS по sandbox workflow.

## 11. Роли

SIS:
- выбрать/подготовить host;
- firewall/SSH/users/updates/monitoring;
- secret boundary;
- backup/rollback.

KOD:
- определить code/test/build workflow;
- подготовить scripts/tests;
- исправлять code-level defects.

SHD:
- связать symptoms/spec/source/runtime;
- проверить parity/fit-gap;
- подготовить evidence reports;
- не менять production без отдельного authority.

KOO:
- решить provider/resource priority;
- закрепить authority boundary;
- маршрутизировать SIS/KOD/SHD задачи.

ARH:
- проверить preservation/recovery для нового sandbox workflow.

## 12. Рекомендуемый следующий проверяемый шаг

Создать отдельную адресную задачу SIS:

```text
KOO/SIS task: prepare lab-01 sandbox host readiness profile
```

Минимальный результат SIS:

```text
host provider
hostname
OS
SSH access model
firewall state
allowed user
workspace path
installed base packages
secret boundary
Remote Desktop Commander availability
GitHub clone test
rollback/cleanup note
```

После этого SHD сможет выполнить первый профильный read-only pass:

```text
WBN/TERA2 source/runtime parity + WBNP locator scan
```

## 13. Stop conditions

Стоп до исполнения:

- нет отдельного sandbox host или явно разрешённого host scope;
- host содержит production secrets и нет secret boundary;
- непонятно, кто владелец host authority;
- нет GitHub access/token model;
- действие требует billing/provisioning без подтверждения ОПЕРАТОРА;
- действие может изменить production service.

## 14. Статус

```text
status: planning_current
production: not touched
billing/provisioning: not performed
plugins: suggestions issued via ChatGPT UI
remote endpoint observed: ruvds-xnqc6 online
recommended next phase: SIS/KOO sandbox host readiness task
```

---
КТО: SHD / ШАРДОВИК
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: зафиксировать план расширения SHD через экспериментальный хостинг-контур, GitHub, ChatGPT Pro/Codex/apps и remote host
СТАТУС: current_planning