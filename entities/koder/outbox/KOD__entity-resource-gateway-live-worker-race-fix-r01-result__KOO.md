# КОДЕР → КОО: live-worker ledger initialization race fix r0.1

Результат: `PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY`.

Исправлена только гонка SQLite инициализации/claim в durable one-shot ledger. Старый заблокированный candidate сохранён неизменным. Принятые gateway, executor-prep и provider bytes не менялись.

## Основание

Exact task:
`388d3b67d0d2e0de008ca1dd8cef872da46a4338:entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-ledger-race-fix-r01__KOD.md`.

Independent blocker:
`d15b88501d227f778b657af638e86bf028f1948b`,
`BLOCKED_LIVE_WORKER_LEDGER_INIT_RACE`.

Blocked source candidate:
`entities/koder/outbox/entity-resource-gateway-live-worker-r01/`,
commit `cd9f0c7327613ee29f9de54574ca141b557e5d18`,
tree `222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4`.

## New immutable candidate

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-race-fix-r01/`

Commit:
`6880f16459c5424992fcbe2102f0889142fe533a`

Tree:
`81a23900c6437c8a76ee3f45cb451f319f3fdec2`

Key files:
- live_worker.py blob `d276de1050fd54e836ed4fc879eb384dba3aa1f1`, SHA-256 `631ad7e8e5bb12ddfed92d8a8c02c113dfc2b2dde18c848b6c69e739321e6835`;
- test_live_worker.py blob `e9a0d938e0eb7180fdc8336050a38347a477c2ed`, SHA-256 `920023253409bc5bc8d685cb66c51f1dffc05c314ea38700b080e3669c6bdc74`;
- test.stdout.json blob `a7240571a956c4c5a09401e454665dd29b8240c6`, SHA-256 `0917760e5d9f930e03474cc9242198b1f43c4b4a67f9e713a7b638b2eac248ab`;
- test.stderr.txt blob `b3b9054cde58b6c193981993d334a79b586cac19`, SHA-256 `522740d49d8e7aee6eb57c660617d6fb1d2c6172d0a09156107b1bd003810b41`.

## Exact correction

Предыдущий `_connect()` выполнял `PRAGMA journal_mode=WAL` при каждом конструкторе. Два конкурентных конструктора могли столкнуться до intended claim path и выпустить сырой `sqlite3.OperationalError: database is locked`.

Новая граница:
- connection open отделён от WAL/schema initialization;
- SQLite busy/locked внутри init/claim имеет bounded retry;
- после исчерпания retry возвращается только `BLOCKED_LEDGER_BUSY`;
- прочие SQLite operational errors преобразуются в `BLOCKED_LEDGER_ERROR`;
- сырой OperationalError наружу не должен выходить;
- claim сохраняет `BEGIN IMMEDIATE` + PRIMARY KEY;
- reservation commit остаётся до credential resolution и transport;
- duplicate key остаётся `BLOCKED_DUPLICATE_CALL`;
- provider retry/fallback не добавлены.

## Stress evidence

Финальный полный прогон:
- test methods: 31;
- failures: 0;
- errors: 0;
- skipped: 0;
- UID: 1000;
- real provider calls: 0;
- real credential reads: 0;
- production: false.

Новые проверки:
- 40 раундов × 12 concurrent constructor+claim threads;
- 30 раундов × 16 concurrent constructors;
- принудительная SQLite write-lock contention → bounded `BLOCKED_LEDGER_BUSY`;
- 50 restart/replay duplicate attempts после committed reservation.

Во всех stress-проверках raw SQLite lock exception не наблюдался. В каждом constructor+claim раунде ровно один claimant получал success; остальные классифицировались `BLOCKED_DUPLICATE_CALL` либо bounded `BLOCKED_LEDGER_BUSY`.

## Unchanged boundaries

Сохранены:
- restart/replay prevention;
- reservation before credential resolution/transport;
- hard timeout;
- max response bound;
- redirect fail-closed;
- exact provider/model/request-plan binding;
- secret-reference-only resolver interface;
- no credential material in result/files;
- one-call semantics;
- automatic provider retries = 0;
- no provider fallback;
- ResourceResult remains `project_acceptance=NOT_GRANTED`;
- caller writer unchanged;
- no project-state application;
- no external dispatch authority.

## Preflight / write boundary

Fresh preflight HEAD:
`93902ca2ae986ed2fad24da70589640c3eeef4b4`.

KOD writer v0.3 blob:
`bfeff738de2759248307dd52433c77139624fb54`.

Prewrite confirmed target race-fix path absent and accepted bindings unchanged:
- accepted gateway blob `e93ac320468dfeed84a7342b4e9dc5c597f48fc2`;
- executor-prep blob `97031bc1948ec6adfe44bede3c8a219fd0310a44`;
- OpenAI live transport blob `4407a38113b5dd7de8ec30caca29be66a78f0239`;
- Anthropic adapter blob `985746909772900d9c72257dc53478aa34861d91`.

No real provider call, real credential read/create, account/billing mutation, production deployment, Telegram/portal/TERA2 work occurred.

## Next boundary

Independent SIS reverification of this exact package is required. This PASS does not authorize a live call or deployment.

---
КТО: KOD / КОДЕР v0.3
СТАТУС: `PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY`
receipt: not_claimed
acceptance: not_claimed
project_time: omitted
