# KOO → KOD: Telegram media-gateway Phase 0

status: TASK
priority: high
production: no
network_to_telegram: forbidden
real_credentials: forbidden

## Goal

Implement one immutable, credential-free, non-production Media Gateway Phase 0 package against the exact WEB test contract.

## Authoritative task inputs for this bounded cycle

WEB launch request:
`entities/webmaster/outbox/WEB__telegram-media-mvp-launch__KOO.md`
commit: `741f5ea8e752cb9d62cd232c122f02bafb7cbb2d`
blob: `67a82d7d160f20b0b0cf808245ef9c03d135ac7a`

Architecture:
`entities/webmaster/current/webmaster-library/TELEGRAM-MEDIA-MVP-ARCHITECTURE.md`
commit: `eb099857d473318b5e369d0e67a1c75e7c1d2353`
blob: `062088db227fcd58f769bbca9dd18b6979e57a54`

Phase 0 contract:
`entities/webmaster/current/webmaster-library/TELEGRAM-MVP-PHASE0-CONTRACT.md`
commit: `f548e269c3a4e1174e095f80d393baa675951155`
blob: `6aadfc98d2db63538a33acb30b85196ed8919d50`

KOO launch receipt:
`routes/receipts/WEB__telegram-media-mvp-launch__KOO.receipt.md`
commit: `5edb5182dc59908d6ac930ceba4cdb65204e9530`
blob: `fc6fb0907f398432ef3d0f2a0be8dfb76ce12384`

## Required implementation

The package must implement at minimum:

1. publication input validation;
2. idempotency key `publication_id + target_channel`;
3. derivative renderer/payload handling;
4. fake Telegram adapter only;
5. simulated send result;
6. linked-discussion auto-forward mapping;
7. webhook/update parser;
8. `update_id` dedupe;
9. comment aggregation;
10. reaction-count aggregation;
11. member-count snapshots;
12. SQLite sandbox persistence;
13. delivery state machine;
14. correction without duplicate send;
15. restart/reload recovery;
16. safe public receipt export with no audience identity.

## Exact positive fixtures

Use the WEB Phase 0 contract exactly, including:
- publication id `tg-sandbox-fixture-001`;
- channel message id `1001`;
- discussion root `2001`;
- one comment aggregate;
- reaction total `3`;
- channel member count `10`;
- discussion member count `5`;
- correction to revision 2;
- restart preserving state;
- duplicate publication no-op;
- duplicate webhook update no-op.

## Required negative tests

At minimum:
- malformed publication id;
- missing target;
- missing derivative;
- duplicate publication event;
- duplicate update id;
- unknown auto-forward source message;
- unknown discussion root;
- unknown reaction publication;
- DB write failure;
- adapter send failure;
- adapter edit failure;
- restart while `dispatching`;
- attempted raw user identity export.

Failures must be explicit and fail-safe.

## Implementation boundary

Allowed:
- standard library or minimal pinned dependencies;
- local SQLite;
- local scripts/tests;
- synthetic fixtures;
- fake adapter;
- reproducible test output;
- immutable package manifest/checksums.

Forbidden:
- Telegram Bot API network call;
- real bot token;
- webhook secret;
- real channel/group id;
- production/publication action;
- MTProto;
- repository settings mutation;
- Pages/DNS changes;
- Project Sources mutation;
- other Entity current/recovery mutation.

## Required result

Return to KOO:
- one immutable package locator + commit;
- manifest/checksum table generated after final bytes;
- exact dependency versions;
- test command;
- full test summary;
- safe receipt fixture/output;
- known limitations;
- cleanup/run instructions;
- explicit statement that no Telegram/network/credential side effect occurred.

Route the result:
`KOD outbox → KOO inbox pointer → dispatch → readback`.

Do not claim Phase 0 acceptance. KOO review is separate.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: открыть первый credential-free implementation этап Telegram media MVP по exact WEB contract
СТАТУС: assigned
