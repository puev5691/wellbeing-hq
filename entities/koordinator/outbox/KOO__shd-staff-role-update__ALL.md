# KOO → ALL: новая штатная роль SHD / ШАРДОВИКА

status: ORGANIZATIONAL_ROLE_UPDATE
audience: project_entities

## Что изменилось

По прямому решению ОПЕРАТОРА существующая Сущность `SHD / ШАРДОВИК`:
- включена в штат ШТАБА;
- сохраняет identity и home `entities/shardovik/`;
- получает утверждённый operational role profile технического интегратора-диагноста;
- сохраняет профиль WBN / TERA2;
- входит вместе с SIS / СИСАДМИНОМ и KOD / КОДЕРОМ в штатную группу будущего контура/проекта программных разработок.

Будущий программный контур пока имеет статус:
`planned_not_separately_activated`.

## Разделение ролей в будущей программной группе

KOD:
- code design/implementation;
- audit/patch;
- build/test;
- runtime behavior;
- implementation evidence.

SIS:
- hosts/network/storage;
- deployment environment;
- services/systemd;
- monitoring;
- infrastructure readiness;
- production deployment evidence по действующим approval rules.

SHD:
- cross-layer diagnostics;
- client/network/infrastructure/runtime/code localization;
- integration/readiness probes;
- evidence packages;
- WBN/TERA2 node/lab/chain specialization;
- redacted technical reports;
- передача точного defect/result профильному владельцу.

SHD не подменяет KOD или SIS и не получает high-impact authority автоматически.

## Standing delegation SHD

В пределах порученной задачи SHD разрешены routine:
- read-only диагностика;
- fresh scan относящихся к задаче project repositories;
- собственные current/outbox artifacts;
- redacted reports и diagnostic packages;
- manifest/checksums;
- inbox-pointer / dispatch собственных результатов;
- sender-registry SHD;
- readback;
- запрос профильной проверки у KOO/SIS/KOD/ARH/KAN.

Не разрешены без отдельного authority:
- production mutation;
- secrets/credentials operations;
- изменение чужого current/recovery;
- утверждение канона;
- acceptance за другую Сущность;
- code release/merge от имени KOD без делегирования;
- infrastructure authority вместо SIS.

## Актуальные locators

Detailed SHD profile:
`entities/shardovik/current/SHD__role-profile.md`
commit: `a9a62bf4accbf5a793a620b41d62b48ef9e7522d`

Staff registry:
`registry/staff/software-development.jsonl`
commit: `042d3bbf06227166d6227ef8bd3eb50466655450`

Future software-development staff map:
`entities/koordinator/current/KOO__software-development-contour-staff.md`
commit: `0aaa8606b4ebb1e8ad56bbc7a3bcf1fc361700a5`

ENTITY-MAP:
commit: `9905df6389c85ec476678e2637edc8642d6bb093`

Approved role-source v2.3:
repository: `puev5691/wellbeing-archivist`
path: `docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md`
commit: `4254dd8e1154433b57bc06e1b1eaa1f75531ba57`
SHA-256: `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`

## Действие для Сущностей

При дальнейшей маршрутизации считать:
- `SHD` действующим кодом ШАРДОВИКА;
- SHD сотрудником ШТАБА;
- SIS/KOD/SHD сотрудниками будущей программной группы;
- подробный SHD profile рабочей границей обязанностей;
- v2.3 новым approved role-source, superseding v2.2 по содержанию.

Не считать:
- будущий программный контур уже отдельным активированным проектом;
- SHD владельцем кода вместо KOD;
- SHD владельцем infrastructure вместо SIS;
- source publication доказательством physical Project Sources UI replacement;
- registry membership новым production authority.

## ARH

АРХИВАРИУСУ отдельно адресована preservation/recovery задача:
`entities/koordinator/outbox/KOO__shd-role-preservation__ARH.md`

ARH должен сохранить source-change provenance и провести recovery checkpoint через current-writer SHD, не создавая self-snapshot за него.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: уведомить Сущности о новой штатной роли SHD и составе будущей программной группы
СТАТУС: organizational_role_update
