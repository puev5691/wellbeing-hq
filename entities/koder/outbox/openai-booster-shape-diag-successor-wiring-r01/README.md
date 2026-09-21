# Booster v2 shape-diagnostic successor wiring r0.1

Статус: immutable non-live successor candidate. Не установлен на host.

## Что исправлено

Предыдущий host runtime вызывал только review-result v2 path и не знал о response-shape diagnostics r0.2.

Этот successor добавляет executable outer runner, который реально вызывает:

`DiagnosticReviewableLiveWorker`

из independently verified r0.2 diagnostic package.

Future runtime order:

`claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`.

## Runtime layout

Candidate install root:

`/opt/wellbeing/openai-booster-shape-diag-successor-r01`

Fixed state paths:

- invocation:
  `/var/lib/wellbeing/openai-booster-live-child-r01/invocation.json`;
- ledger:
  `/var/lib/wellbeing/openai-booster-live-child-r01/ledger.sqlite`;
- diagnostic shapes:
  `/var/lib/wellbeing/openai-booster-live-child-r01/response-shapes`;
- review results:
  `/var/lib/wellbeing/openai-booster-live-child-r01/review-results`.

All state stays inside the already accepted root:

`/var/lib/wellbeing/openai-booster-live-child-r01`.

## Exact reused components

Final live-worker is not modified:

SHA-256:
`175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`.

Shape diagnostics r0.2 reused byte-identically:
- `diagnostic_reviewable_live_worker.py`
  SHA-256 `b06588123f795a2e8181af0d6b1a4be2e90472c5974bbbab70eb5f7fcb9024be`;
- `response_shape_store.py`
  SHA-256 `bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f`.

Review-result v2 reused byte-identically:
- `reviewable_live_worker.py`
  SHA-256 `6a81a0c08ffd961e3b22d2d1de4948ebce780555cfe40b8c669e96e47cb07751`;
- `review_result_store.py`
  SHA-256 `cd01972b7045d4f84583fb5470d4c0012e09c12b954ea65221107eaa01385d7e`.

## Credential boundary

Canonical mapping is unchanged:

`secretref:openai:wellbeing-entity-boosters-restricted`

→ systemd encrypted credential object:

`/etc/credstore.encrypted/openai-wellbeing-entity-boosters-restricted.cred`.

Candidate unit uses the same `LoadCredentialEncrypted` mapping.

Sentinel readiness checks only that the child credential object exists. It does not read its value.

## Sentinel

Process-level non-live sentinel passed with:
- status READY;
- provider_calls=0;
- credential_value_read=false;
- shape schema v2;
- review schema v2;
- no ledger created;
- no shape file created;
- no review file created.

A synthetic marker `DO_NOT_READ` was placed in the fake credential object during the test. Sentinel did not surface or consume it.

## Systemd contract

Candidate unit:
`wellbeing-openai-booster-shape-diag-successor.service.candidate`.

Properties:
- Type=oneshot;
- User/Group=pev5691;
- exact encrypted credential mapping;
- exact successor ExecStart;
- no listener/socket;
- no credential environment;
- state writes limited to accepted root;
- no restart policy;
- installation/enabling is not performed by this package.

Static unit tests passed 4/4.

The same bytes copied temporarily to a .service filename passed:
`systemd-analyze verify`.

## Deterministic wiring tests

Successor runtime suite passed 5/5.

Verified:
- sentinel zero provider calls / zero credential value reads;
- plain assistant message produces both shape and review artifacts;
- reasoning-like item persists diagnostic shape before unchanged normalizer blocks;
- shape/review artifacts exclude credential-like material;
- exact provider/model/tools/calls/retries/fallback/project bounds remain unchanged.

## Boundaries

During development and verification:
- real provider calls = 0;
- credential value reads = 0;
- host/root/systemd mutation = 0;
- deployment = 0;
- historical authority replay = 0;
- tools = none;
- retries = 0;
- fallback = none;
- project_acceptance = NOT_GRANTED;
- production_acceptance = NOT_GRANTED.

Independent SIS verification is required before any host mutation or live provider call.
