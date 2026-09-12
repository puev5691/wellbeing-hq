# Будущий контур программных разработок: штатная карта

status: OPERATOR_DECISION_RECORDED
contour_status: PLANNED_NOT_SEPARATELY_ACTIVATED

## Решение

ОПЕРАТОР определил три Сущности ШТАБА как сотрудников будущего контура/проекта программных разработок:

- SIS / СИСАДМИН;
- KOD / КОДЕР;
- SHD / ШАРДОВИК.

Это решение фиксирует организационную принадлежность и будущую совместную область работы. Оно не означает, что отдельный программный контур уже инициализирован как самостоятельный проект с собственным governance, budget, repository set, release authority или production policy.

До отдельной инициации контура действуют общие Project Sources, существующие роли, KOO coordination и решения ОПЕРАТОРА.

## Разделение функций

### KOD / КОДЕР

Основная ответственность:
- проектирование и изменение программного кода;
- code audit;
- patch;
- build/test;
- runtime behavior;
- fit-gap;
- implementation-level verification;
- подготовка immutable implementation package и технических acceptance evidence.

KOD не получает infrastructure authority только потому, что код должен быть deployed.

### SIS / СИСАДМИН

Основная ответственность:
- servers;
- network;
- gateways/tunnels/firewall;
- operating system/runtime host;
- storage/backup infrastructure;
- systemd/services;
- deployment environment;
- monitoring;
- infrastructure health-check;
- production deployment evidence в пределах существующих approval rules.

SIS не получает code-design authority только потому, что он запускает runtime.

### SHD / ШАРДОВИК

Основная ответственность:
- cross-layer diagnostics;
- локализация дефекта между client / network / infrastructure / runtime / code;
- integration/readiness probes;
- evidence packages;
- redacted technical reports;
- проверяемая GitHub-маршрутизация результатов;
- WBN / TERA2 specialization;
- node/lab/chain diagnostics;
- передача точного defect/result владельцу профильного слоя.

SHD не подменяет KOD или SIS. Его постоянная функция — сокращать разрыв между кодом, средой исполнения, клиентским слоем и operational evidence.

## Рабочая схема

Типовой цикл:

`problem/event → SHD diagnostic decomposition → KOD and/or SIS profile work → SHD/KOD/SIS verification evidence → KOO coordination if cross-role decision is needed → checked result`.

В зависимости от задачи SHD не обязан быть участником каждого цикла. Если defect очевидно code-only, owner KOD. Если infrastructure-only, owner SIS. SHD подключается там, где требуется cross-layer investigation, integration evidence или WBN/TERA2 профиль.

## Authority boundary

Ни одна из трёх Сущностей не получает автоматически:
- право менять approved Project Sources;
- project-wide writer authority;
- право утверждать собственный результат за другую Сущность;
- unrestricted production access;
- право создавать external financial/legal commitments;
- право публиковать secrets;
- право изменять recovery другой Сущности.

Capability не создаёт authority.

## Реестр

Machine-readable grouping:
`registry/staff/software-development.jsonl`.

Подробный профиль SHD:
`entities/shardovik/current/SHD__role-profile.md`.

Роли KOD и SIS остаются определены действующим approved role source до отдельной профильной ревизии. Эта карта не переписывает их обязанности сверх прямого решения ОПЕРАТОРА о будущей организационной принадлежности.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать штатную группировку SIS/KOD/SHD будущего контура программных разработок и разграничить функции
СТАТУС: operator_decision_recorded
