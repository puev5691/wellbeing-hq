# KOO → OPERATOR: source-set r0.4 Project Sources replacement operation

status: READY_FOR_OPERATOR_PROJECT_SOURCE_REPLACEMENT
project_time: omitted; trusted project-time source not used

## Что произошло

ОПЕРАТОР разрешил использовать фактические SHA-256 exact Git blobs:

`ACCEPT_ACTUAL_GIT_BLOB_SHA256_FOR_SOURCE_SET_R04`

Decision record:
`entities/koordinator/current/KOO__source-set-r04-checksum-decision.md`
commit `bfbb04bdc57674f428efa52ee06f502f8ecd37b9`.

Checksum blocker закрыт.

## Что это означает

Остаётся только фактическая замена двух файлов в ChatGPT Project Sources как одной maintenance-операции.

Нельзя считать набор активированным после замены только одного файла.

## Exact replacements

### Remove/replace predecessor 1

Old active:
`project-instructions-core-v2_2-approved.md`

New exact source:
`project-instructions-core-v2_3-approved.md`

Git commit:
`6286962c6218072d174f87e2a040687719fbe3a6`

Git blob:
`e51054d57c583bbbecc79716e1d5543e686efbd8`

SHA-256:
`b115daa61782441e3b336dbedda216e4ea0b088fae12b374681a1069414d258e`

### Remove/replace predecessor 2

Old active:
`task-conveyor-canon-v1-approved.md`

New exact source:
`task-conveyor-canon-v1_1-approved.md`

Git commit:
`6d13d7ffcfb837492ed999c904a5f5bcc210b0a0`

Git blob:
`0ff3d3f74d5793ea72cc9e84fffc64f01e8455ab`

SHA-256:
`904c4a89a459ab159758a50ae6cc56be25b988514388bd201a9872ad4a56e6d8`

## Leave unchanged

Do not remove/replace:

- `entity-roles-short-v2_4-approved.md`
- `file-work-canon-universal-v2_4-approved.md`
- `source-loading-policy-v2_2-approved.md`
- `entity-state-preservation-and-recovery-canon-v1_6-approved.md`

## OPERATOR action

In Project Sources:

1. replace/remove core v2.2 and add exact core v2.3;
2. replace/remove conveyor v1.0 and add exact conveyor v1.1;
3. leave the other four files untouched;
4. complete both replacements before resuming source-dependent normative work;
5. return to KOO with exact signal:

`SOURCE_SET_R04_UI_REPLACEMENT_DONE`

Do not claim activation from the UI action alone.

After the signal KOO must independently verify:
- exactly six intended active sources;
- expected filenames;
- exact identities/content;
- predecessor absence;
- no mixed active old/new set.

Only then may KOO declare:
`SOURCE_SET_R04_ACTIVATED`.

## Supersession to record only after PASS

- core v2.2 → v2.3;
- task-conveyor v1.0 → v1.1.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: exact Project Sources replacement operation after checksum decision
СТАТУС: READY_FOR_OPERATOR_PROJECT_SOURCE_REPLACEMENT
