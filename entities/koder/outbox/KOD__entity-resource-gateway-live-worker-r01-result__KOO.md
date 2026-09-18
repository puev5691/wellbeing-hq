# КОДЕР → КОО: live-worker r0.1

Результат: `PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01_READY_FOR_INDEPENDENT_VERIFY`.

Создан отдельный кандидат LiveExecutorPort/live-worker. Реальных provider calls, чтения/создания credentials, billing/account mutation и production deployment не выполнялось.

## Immutable candidate

Package:
`entities/koder/outbox/entity-resource-gateway-live-worker-r01/`

Commit:
`cd9f0c7327613ee29f9de54574ca141b557e5d18`

Tree:
`222c75ddb8cb47f1a2b4b601fe49dee4a78d9ce4`

Files:
- `live_worker.py` blob `2e9ddfac78e8a38a413c9e6ee9a938208de2eb89`, SHA-256 `4dcf53cacd0ba20c734fff218fd7b555a86af5244f8359e2c3eda6a0c76fd093`;
- `test_live_worker.py` blob `97f37dd62fee5ef4f3ff5360902e086e72cd9add`, SHA-256 `dc5fb1e12d5b19534b5e967db95559e82de589f719e9a2dfedbc2552a92122ba`;
- `README.md` blob `5ea72ad9ed8e79b4aea8b84d98e415ec5bb19875`;
- `MANIFEST.json` blob `3e60b0b0f90a2d13ceec82c45f7a4d08ff9d4db1`;
- `test-result.json` blob `4d5b43f501ae5872de3b016a6706dcca36649150`.

## Реализовано

- restart-safe durable/atomic one-shot ledger на SQLite: PRIMARY KEY, BEGIN IMMEDIATE, WAL, synchronous=FULL; reservation фиксируется до credential resolution/transport;
- hard timeout через POSIX setitimer, fail-closed вне поддерживаемой main-thread среды;
- max response byte limit;
- redirect handler, который не следует redirect; любой 3xx блокируется;
- точная привязка provider/model/request-plan до egress;
- CredentialResolver принимает только typed secret reference;
- secret value исключён из repr/redacted result/files;
- OpenAI boundary: POST /v1/responses, exact model/body/header binding;
- Anthropic boundary: POST /v1/messages, anthropic-version 2023-06-01, exact model binding;
- one-call semantics, automatic_retries=0;
- attachment guard сохраняет ResourceResult: project_acceptance=NOT_GRANTED, caller writer unchanged, no gateway/provider writer authority, no project-state application, no external dispatch, routing not_started.

## Проверка

Полный rerun после исправления только тестового импорта:
- test methods: 27;
- failures: 0;
- errors: 0;
- skipped: 0;
- UID: 1000;
- real provider calls: 0;
- real credential reads: 0;
- production: false.

Проверены:
restart/replay prevention, конкурентный atomic claim, hard timeout, oversized response, redirect, provider/model mismatch, stale authority, duplicate call, secret-ref boundary, no retry on 429/500, exact prepared/admission attachment и ResourceResult authority boundary.

Первый запуск дал 2 ошибки только из-за отсутствующего import asdict в двух тестах. `live_worker.py` не менялся; исправлен только test file и весь набор повторён успешно.

## Ограничения

Кандидат содержит реальный-capable HTTP client class, но он не вызывался тестами. Live authority этим циклом не выдаётся. Secret resolver implementation отсутствует. SQLite durability относится к локальному FS; ownership/fs durability/deployment location остаются отдельным runtime-вопросом.

Hard deadline основан на POSIX signal и требует main thread; при отсутствии primitive код обязан fail-closed. Redirect policy закрыта. Автоматического retry/fallback нет.

## Источники

Exact task:
`dbe29d49eef74e491ed055e642f1411ff4273bbe:entities/koordinator/outbox/KOO__entity-resource-gateway-live-worker-r01__KOD.md`.

Current KOD writer v0.3 blob:
`bfeff738de2759248307dd52433c77139624fb54`.

Basis:
- gateway independent PASS `fd49601948827cc43e46331ae98ab1f680101c0a`;
- live-executor prep independent PASS `888e9fe64dccc2c12571b246cdf8d754e0df1214`;
- OpenAI technical final gate `787ec5df1878c7ddb0a5f2928c61e265b40959b0`;
- Anthropic adapter independent PASS `d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a`.

Fresh preflight HEAD: `a30059b8efe83c532a440d85a1a38de92820f224`.
Prewrite HEAD: `8717751dd2f5f4751ce4d825f70949096d8ac9a2`.

Accepted gateway/executor-prep/provider blobs matched before publication and were not modified.

## Next boundary

Independent verification of this exact package is required. Do not perform a real provider call, read a real credential or deploy production merely because this candidate passed local zero-network tests.

---
КТО: KOD / КОДЕР v0.3
СТАТУС: `PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_R01_READY_FOR_INDEPENDENT_VERIFY`
receipt: not_claimed
acceptance: not_claimed
project_time: omitted
