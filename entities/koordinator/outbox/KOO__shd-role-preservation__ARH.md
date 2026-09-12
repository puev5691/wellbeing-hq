# KOO → ARH: preservation / recovery после штатной интеграции SHD

status: TASK_FOR_PRESERVATION_REVIEW

## Основание

ОПЕРАТОР утвердил:
- перевод существующей Сущности `SHD / ШАРДОВИК` в штат ШТАБА;
- подробную адаптацию роли после self-report;
- принадлежность SIS / KOD / SHD к будущему контуру/проекту программных разработок.

KOO завершил registry/source/current-role слой адаптации.

## Проверяемые артефакты

### SHD operational role profile

repository: `puev5691/wellbeing-hq`
path: `entities/shardovik/current/SHD__role-profile.md`
commit: `a9a62bf4accbf5a793a620b41d62b48ef9e7522d`
blob: `29df9468da37fb4e9cda0a5912e1f41dffe08a13`

### Staff registry

path: `registry/staff/software-development.jsonl`
commit: `042d3bbf06227166d6227ef8bd3eb50466655450`
blob: `d4d8fa090987bab763d5775fad047dda4d8c181f`

### Future software-development contour map

path: `entities/koordinator/current/KOO__software-development-contour-staff.md`
commit: `0aaa8606b4ebb1e8ad56bbc7a3bcf1fc361700a5`
blob: `5740eaf9e16fd0a24b7faabe4ea46ae66ce7292f`

### ENTITY-MAP

path: `ENTITY-MAP.md`
commit: `9905df6389c85ec476678e2637edc8642d6bb093`
blob: `2df669fa8d24b95fbac1ce340b8253fc40ebb78f`

### Approved role source v2.3

repository: `puev5691/wellbeing-archivist`
path: `docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md`
commit: `4254dd8e1154433b57bc06e1b1eaa1f75531ba57`
blob: `402e229eef44de65f0a2d81a42e446d96c66189c`
SHA-256: `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`

approval record:
`docs/entities/kancelyariya/approved/shd-staff-role-v2_3/OPR__shd-staff-role-approval__ALL.md`
commit: `731a9f949af6fbfae2f9ae5c7ae808227b04596a`

manifest:
`docs/entities/kancelyariya/approved/shd-staff-role-v2_3/manifest.md`
commit: `a700a17ca1b6dc3b7fa98ff6a02b930cb41722b9`
blob: `5998788c24d9d60486f53fce97faf4af0cb4d127`

## Требуемое действие ARH

1. Проверить provenance, placement, immutable identity и отсутствие конфликтующего current source.
2. Зафиксировать source-change в preservation/recovery lineage.
3. Не писать self-snapshot SHD за SHD.
4. Запросить/принять self-state checkpoint current-writer SHD по recovery canon v1.4.
5. После получения SHD self-snapshot проверить manifest/checksums/external locator/readback.
6. Обновить recovery registry/status SHD.
7. Зафиксировать, что старый role v2.2 сохраняется как superseded provenance.
8. Не объявлять physical Project Sources UI replacement выполненной без отдельного evidence.

## Boundary

ARH preservation не создаёт новую роль и не меняет организационное решение ОПЕРАТОРА. Оно проверяет сохранность, provenance и recoverability уже утверждённого role/source change.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: передать ARH source-change и role-change SHD на preservation/recovery проверку
СТАТУС: task_for_preservation_review
