# KOO: интеграция SHD / ШАРДОВИКА в штат ШТАБА

status: OPERATIONAL_ADAPTATION_COMPLETE__PRESERVATION_AND_PROJECT_SOURCE_UI_MIGRATION_PENDING

## Решение ОПЕРАТОРА

ОПЕРАТОР утвердил:
- сохранить существующую Сущность `SHD / ШАРДОВИК`;
- оформить SHD как сотрудника ШТАБА;
- после self-report детально определить обязанности и возможности;
- внести SHD в необходимые реестры и источники;
- считать SIS / KOD / SHD сотрудниками будущего контура/проекта программных разработок;
- после адаптации уведомить остальные Сущности, особенно ARH.

Identity существующей Сущности сохранена:
`SHD / ШАРДОВИК → entities/shardovik/`.

## Self-report

artifact:
`entities/shardovik/outbox/SHD__staff-functions-repo-focus__KOO.md`

commit:
`1999e0b45b9e05b6aaf1fb99cab349509c53bc56`

blob:
`cca580d35d475402ee7ec4f12df18cd15a7bb3d9`

Self-report принят как factual/profile input, не как самоназначение authority.

## Выполненная адаптация

### 1. Подробный operational role profile

`entities/shardovik/current/SHD__role-profile.md`

commit:
`a9a62bf4accbf5a793a620b41d62b48ef9e7522d`

blob:
`29df9468da37fb4e9cda0a5912e1f41dffe08a13`

Статус:
`APPROVED_OPERATIONAL_ROLE_PROFILE`.

Зафиксированы:
- technical diagnostics;
- WBN/TERA2 specialization;
- file/evidence discipline;
- GitHub standing delegation для собственных routine outputs;
- routing;
- experience-candidate boundary;
- secret boundary;
- production/high-impact stop conditions;
- разграничение KOD/SIS/SHD.

### 2. Staff registry будущего программного контура

`registry/staff/software-development.jsonl`

commit:
`042d3bbf06227166d6227ef8bd3eb50466655450`

blob:
`d4d8fa090987bab763d5775fad047dda4d8c181f`

Зарегистрированы:
- SIS;
- KOD;
- SHD.

Контур:
`planned_not_separately_activated`.

### 3. Организационная карта будущего программного контура

`entities/koordinator/current/KOO__software-development-contour-staff.md`

commit:
`0aaa8606b4ebb1e8ad56bbc7a3bcf1fc361700a5`

blob:
`5740eaf9e16fd0a24b7faabe4ea46ae66ce7292f`.

### 4. ENTITY-MAP

`ENTITY-MAP.md`

commit:
`9905df6389c85ec476678e2637edc8642d6bb093`

blob:
`2df669fa8d24b95fbac1ce340b8253fc40ebb78f`

Изменено:
- явный код `SHD / ШАРДОВИК`;
- указана future software-development grouping SIS/KOD/SHD;
- указан machine-readable staff registry.

### 5. Approved role source v2.3

Repository:
`puev5691/wellbeing-archivist`

Source:
`docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md`

commit:
`4254dd8e1154433b57bc06e1b1eaa1f75531ba57`

blob:
`402e229eef44de65f0a2d81a42e446d96c66189c`

SHA-256:
`e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`

approval record:
`docs/entities/kancelyariya/approved/shd-staff-role-v2_3/OPR__shd-staff-role-approval__ALL.md`
commit:
`731a9f949af6fbfae2f9ae5c7ae808227b04596a`

manifest:
`docs/entities/kancelyariya/approved/shd-staff-role-v2_3/manifest.md`
commit:
`a700a17ca1b6dc3b7fa98ff6a02b930cb41722b9`

v2.3 supersedes v2.2 by explicit OPERATOR decision.

## Уведомление Сущностей

Broadcast artifact:
`entities/koordinator/outbox/KOO__shd-staff-role-update__ALL.md`

commit:
`2d4046ef5b9ad52130bd00b517efd677180e1b52`

blob:
`10699f80fcec9038b486535cb684626aa605a0c2`

Addressed recipients:
- SIS;
- KOD;
- SHT;
- KAN;
- RED;
- WEB;
- VOL;
- SHD;
- SHK;
- KON.

Multi-recipient dispatch:
`routes/dispatch/KOO__shd-staff-role-update__ALL.md`

commit:
`c8e921da850a7928072f068b46849bf1cc7bbdf1`

ARH получил отдельную actionable preservation-задачу:

`entities/koordinator/outbox/KOO__shd-role-preservation__ARH.md`

artifact commit:
`e2cb937acfed0e0794285b11cec341b8db77c652`

ARH inbox commit:
`c6728547c79f5e60cd1db1b3c6bc234bc97b6365`

ARH dispatch commit:
`b19d0c6c81688327083acf3a70b250ffbb62fbf3`.

ПРОВОДНИК БЛАГОПОЛУЧИЯ не включён в broadcast dispatch, потому что в действующей карте не установлен подтверждённый короткий routing-code/recipient contract. Новый код в рамках этой задачи не выдуман.

## Незавершённые post-conditions

### ARH preservation/recovery

Ещё не доказаны:
- обработка ARH новой preservation-задачи;
- новый self-state checkpoint authoritative current-writer SHD;
- canonical external recovery locator/version SHD по новой роли;
- recovery registry update;
- cold-start/recoverability новой SHD role-state.

ARH обязан не писать self-snapshot за SHD.

### Physical Project Sources migration

Approved v2.3 опубликована и immutable identity проверена.

Но текущая интерфейсная загрузка Project Sources в этом чате всё ещё содержит v2.2. Инструмента для физической замены Project Sources attachment у KOO в этом сеансе нет.

Следовательно:
`content_approval_and_external_publication = complete`
`physical_Project_Sources_UI_replacement = pending_external_user_action_or_supported_tool`

До подтверждения UI replacement новый экземпляр, загрузивший только старый v2.2, может не увидеть новое role-source содержимое без recovery/source-change evidence.

## Итоговая классификация

Operational role integration: `PASS`.

HQ entity/staff registries: `PASS`.

Approved external role-source v2.3 publication/readback: `PASS`.

Addressed notification to operational entities: `PASS_WITH_PROVODNIK_ROUTING_CODE_GAP`.

ARH preservation/recovery closure: `PENDING`.

Physical Project Sources UI migration: `PENDING`.

Separate software-development project/contour activation: `NOT_STARTED_BY_THIS_DECISION`.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: итоговая проверяемая фиксация адаптации SHD как сотрудника ШТАБА
СТАТУС: operational_adaptation_complete_bounded
