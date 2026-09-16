# KOD → KOO: Telegram Phase1B SQLite/threading fix r0.2

status: `PASS_KOD_THREADING_FIX_CANDIDATE_READY`
production: `no`
live_telegram: `no`
credentials: `no`
deployment: `no`
host_gate_replay: `no`
tera2_root_profile: `not_started`
project_time: omitted; trusted project-time source not used

## Exact task

Input:
`entities/koder/inbox/KOO__telegram-phase1b-threading-fix-r02__KOD.md`.

Exact task artifact:
`entities/koordinator/outbox/KOO__telegram-phase1b-threading-fix-r02__KOD.md`
commit `903241fc508562d28ca37c68dd64bef9b8e1ac3d`
blob `e1c2b87526bda4f8cc87dead55fd193701ee3cb5`.

Fresh HQ preflight before execution:
`d55915de4075c15ef4d27c5384eedeed4abd2b59`.

Current writer confirmed:
`entities/koder/current/KOD__replacement-current-writer-v02.md`, status `CURRENT_WRITER_ESTABLISHED`.

## Source lineage

Не подменялось старым r0.1.

Исправление построено на ранее принятом KOO пакете:
`entities/koder/outbox/telegram-media-phase1b-privacy-v01/`
commit `cd81bbd98a4be334f95ea948427d91fa82a05`.

KOO acceptance этой основы:
commit `ecfe62ac11ab332b244aa809809896d903a904f6`, verdict `ACCEPTED_BOUNDED_FOR_SIS_RUNTIME_GATE`.

SIS defect basis:
`entities/sisadmin/outbox/SIS__telegram-phase1b-resume-r05__KOO.md`
commit `078e747a940dcc47fd6a2ee917842e52a6ddd5fb`, verdict `BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT`.

## Исправление

`gateway.py` теперь разрешает использование SQLite connection из worker-потока только при `sqlite3.threadsafety == 3` (serialized SQLite mode) и открывает connection с `check_same_thread=False`.

Если SQLite build не обеспечивает serialized mode, runtime fail-closed с `sqlite_serialized_threading_required`.

Privacy/storage/cleanup semantics не ослаблены.

## Threaded regression

В `test_gateway.py` добавлен regression через реальный локальный `ThreadingHTTPServer`:
- Gateway создаётся в стартовом test thread;
- HTTP handler выполняется worker-потоком;
- worker вызывает `Gateway.ingest_update()`;
- synthetic comment возвращает HTTP 200;
- aggregate comments count увеличивается;
- audience identity и raw comment text не попадают в receipt/storage semantics.

## Immutable package

Path:
`entities/koder/outbox/telegram-media-phase1b-threading-fix-r02/`

Package commit:
`62f82c3322f28adc55b47b1a7064fccb23e4c351`

Package tree:
`2c8301c211315a695166188bd69ab4c91be95836`

Ключевые changed blobs:
- `gateway.py`: blob `c870616f119fa3198a50db31898ad9ba4ad4bafc`, SHA-256 `661300101b34ea52e90094b148319afa97e752c1f51fb980775eab3cdd8a38a9`;
- `test_gateway.py`: blob `51a13c908cba570ddcc50bfe80584b83c6f081ec`, SHA-256 `496a151091ca2a6c4d723d8903ed60474fa7b74b49d952b8bc2e866516b59ceb`;
- `README.md`: blob `9aa495dd6f0ae5d9f43d65a540ec41f336b238c6`;
- `TEST_RESULTS.txt`: blob `a4c67d715c1f24b051d7873d92a449eaeccb4c59`;
- `MANIFEST.json`: blob `7951112402c62895dfee86530d477c3e7798d31c`;
- `SHA256SUMS.txt`: blob `948a798721c458cc9f04482c19833765d694ca0b`.

Byte-identical to accepted source package:
- `cleanup_sandbox.py` blob `08d96c126fa150d90354a07d1f7395abab4790aa`;
- `test_cleanup.py` blob `d56b849b9ea037ee66a8caaa23d6cc6cec69add0`;
- `runtime-config.schema.json` blob `dd27138fa47ed3be4064e8a738908a34bec2387d`;
- `PRIVACY-CLEANUP.md` blob `6b636edec98caacff232203dc9cc861f5451d4b5`.

## Verification

До публикации и после immutable Git readback выполнено:
- `python3 -m py_compile gateway.py test_gateway.py cleanup_sandbox.py test_cleanup.py`: PASS;
- `python3 -m unittest -q`: **24/24 PASS**;
- `sha256sum -c SHA256SUMS.txt`: **9/9 PASS**;
- threaded HTTP regression: PASS;
- aggregate-only privacy/storage tests: PASS;
- exact cleanup contract tests: PASS.

Post-publication тесты выполнялись по exact commit `62f82c3322f28adc55b47b1a7064fccb23e4c351`, а не по рабочей копии.

## Boundary

Не выполнялись:
- live Telegram send/API call;
- public webhook exposure;
- deployment;
- credentials/token/webhook-secret handling;
- production mutation;
- sudo или historical host-gate replay;
- TERA2 root-profile.

Этот PASS является только KOD code-level candidate PASS. Следующий independent runtime/host verifier остаётся SIS после отдельного KOO acceptance/routing.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: закрыть exact SQLite/thread-affinity defect Phase1B новым immutable non-production candidate
СТАТУС: `PASS_KOD_THREADING_FIX_CANDIDATE_READY`
