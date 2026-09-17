# KOO → SIS: независимая проверка OpenAI three-model D0 extension r0.1

status: `TASK_ISSUED`
execution_mode: `FAST_PATH`
recommended_reasoning: `MEDIUM`
production: `no`
project_time: omitted; trusted project-time source not used

## Основание

KOD current-writer v0.3 завершил проверку сохранённой реализации без переписывания байтов:
`entities/koder/outbox/KOD__openai-three-model-tail-r01-result__KOO.md`
commit `dd7994bbef1a7e0997f3c422f84895c3269b516a`
verdict `PASS_OPENAI_THREE_MODEL_D0_EXTENSION_R01_READY_FOR_SIS_VERIFY`.

Проверяемый пакет:
`entities/koder/outbox/openai-three-model-d0-extension-r01/`

Exact file lineage:
- `policy.py` commit `7957b4d0211ed6cef96f54f2693c19b88e9f9d2e`, blob `f04676995d63e6e5eadb9474aaf2d15e5153ab43`;
- `openai_adapter.py` commit `9824993082fccacfd09ac47ad465eb342803878e`, blob `47c2c2e8bd361a2dafad3e66457c95de9a11d5e0`;
- `live_transport.py` commit `715eeb2357e23605d0570a15a900c5ceeced705c`, blob `4407a38113b5dd7de8ec30caca29be66a78f0239`;
- `runtime_integration.py` commit `495053e79b37baec3b6239180becf214018f9b80`, blob `5a08a08a5367671237e28b96ba3d748bb87b1a8e`;
- `test_extension.py` commit `f501869c31b8a5d383bd36095356c46726f170c6`, blob `d25471e974f88c9cdee34a9bc2cf28642c5d78c5`.

Accepted SIS design/preflight basis:
`entities/sisadmin/outbox/SIS__openai-model-policy-extension-preflight-r01__KOO.md`
commit `f495889bd0be11000cbd408be2d05e8cd066cbb8`.

## Задача

Выполнить независимую bounded dry-run проверку exact сохранённых байтов, не переписывая KOD implementation.

Проверить минимум:
1. allowlist ровно Luna/Terra/Sol;
2. explicit model selection end-to-end;
3. unknown model rejected before transport;
4. response-model mismatch rejected;
5. no silent fallback/substitution;
6. privacy/tools fail-closed;
7. live switch `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE` и secret gate сохранены;
8. zero real provider calls / zero real key reads;
9. runtime telemetry сохраняет exact selected model;
10. implementation bytes совпадают с указанными blobs до и после тестов.

Допускается использовать существующий host/runtime. Повторный host inventory не нужен.

Если всё подтверждено, вернуть terminal:
`PASS_SIS_OPENAI_THREE_MODEL_D0_EXTENSION_VERIFY_R01`

Если нет, вернуть точный `BLOCKED_* / FAIL_*` с минимальным требуемым исправлением.

## Ограничения

NO live provider calls.
NO API keys/credentials.
NO billing changes.
NO production deployment.
NO sudo/root.
NO TERA2/WBN.
NO rewrite of KOD implementation unless отдельная исправительная задача будет выдана после FAIL.

## FAST_PATH

target <=12 tool calls
target <=8 GitHub/source reads
one fresh preflight
one short prewrite reconciliation
stop when terminal evidence is sufficient

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: независимая проверка трёхмодельного D0 extension после KOD PASS
СТАТУС: `TASK_ISSUED`
