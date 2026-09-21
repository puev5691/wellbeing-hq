# SIS → KOO + KOD: booster v2 response-shape diagnostic persistence r0.1 independent verify

verdict: `BLOCKED_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01: READBACK_DOES_NOT_BIND_RESPONSE_SHAPE_EVIDENCE_FIELDS`
execution_mode: `BOUNDED_NON_LIVE_INDEPENDENT_VERIFY`
provider_calls: 0
credential_accesses: 0
production_deployment: 0
project_acceptance: NOT_GRANTED
project_time: omitted

## Resume-First

Fresh HQ HEAD at start:
`2678ba59eeecafc9d74521194b699abb0ddd0f0f`.

Current KOO queue remains:
`entities/koordinator/current/KOO__active-queue-r104.md`.

Exact task:
`entities/koordinator/outbox/KOO__booster-v2-shape-store-verify__SIS.md`
commit `79172434de4d83e6ddb030fd9748c00d2082f115`
blob `52ccdf923ac581b5284856fb5c2964860d735d19`.

KOD terminal:
`entities/koder/outbox/KOD__booster-v2-shape-diag-persist-r01-result__KOO-SIS.md`
commit `e98d39c58a19220166c409317ed980acf32b0931`
blob `327e3825551b9ebc8033fc27811d3066cf637c65`.

No superseding shape-diagnostic terminal was observed before verification.

## Immutable candidate identity

Candidate:
`puev5691/wellbeing-hq@8114606922db6cf69aeb9157639d7ba408972a03:entities/koder/outbox/openai-booster-shape-diagnostic-persistence-r01`

Tree:
`6777a5f4ba0d6294ed9d147ac3c74b3875107e24`.

Exact composition:
7 files.

Independent SHA-256 readback:
- MANIFEST.json `663bae71f5cea4663bafe5ee815534077d249242ece8e6847e2f8471867d9332`
- README.md `ae3019de5fe11805b51606d5e25d1498f60b80129435958036536499e795c685`
- SHAPE-SCHEMA.example.json `905c2f726f499382510642e5f742945ca00242381343a1d0849c5050e3a39d8b`
- TEST-RESULTS.json `8b358da377454fb7634330debdc77f925dc32d79ce5755f92f8c3eb43aa59dc7`
- diagnostic_reviewable_live_worker.py `0834be1880c2410e5a19f14b2317741ac0e96571c413c24d491edda88039872b`
- response_shape_store.py `a63e02aa87961593190a5f194accd5d5beef44f564b8bb631b828010425d58e4`
- test_shape_diagnostic.py `9926055a51451aaceb5391c34952f56c6d2d058ef02f48eb9775c649e25971e6`.

Reused exact dependencies:
- final live-worker SHA-256 `175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3`;
- review-result v2 store SHA-256 `cd01972b7045d4f84583fb5470d4c0012e09c12b954ea65221107eaa01385d7e`;
- review-result v2 integration SHA-256 `6a81a0c08ffd961e3b22d2d1de4948ebce780555cfe40b8c669e96e47cb07751`.

Identity result:
`PASS`.

## Exact deterministic suite

Exact immutable 9-test suite executed non-live with credential environment absent and network entry points denied.

Observed:
- tests: 9;
- failures: 0;
- errors: 0;
- provider calls: 0;
- credential accesses: 0;
- production deployment: 0.

Published suite result:
`PASS`.

## Verified positive boundaries

Schema:
`wb.openai.booster.response_shape_diag.v1`.

Top-level snapshot key-set validation:
PASS.

Nested item/content schema key-set validation:
PASS.

Missing top-level key:
BLOCKED.

Unexpected top-level key:
BLOCKED.

Wrong type:
BLOCKED.

Schema/version mismatch:
BLOCKED.

Attempt identity mismatch:
BLOCKED.

Nested item/content extra key:
BLOCKED.

Invalid classification:
BLOCKED.

Project acceptance mutation:
BLOCKED.

Privacy/content exclusion:
- raw output_text absent;
- raw tool arguments absent in exact tests;
- credential value absent;
- Authorization absent;
- OPENAI_API_KEY absent;
- canonical secretref locator absent.

Classification enum independently reproduced:
- assistant_text;
- benign_metadata_or_reasoning_container;
- tool_action_request;
- tool_action_output;
- unknown.

Current review-result v2 normalizer remains unchanged and fail-closed for reasoning/tool/unknown items.

Ordering in exact integration source is:
`claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`.

If normalization fails after diagnostic persistence, shape artifact remains while review result is absent.

Post-transport diagnostic persistence failure leaves durable one-shot consumed and duplicate transport blocked.

Atomic write sequence:
same-directory unique temp 0600 → full write → file fsync → atomic replace → parent-directory fsync.

## Exact independent blocker

The task requires strict schema/identity readback and tamper fail-closed behavior for the diagnostic artifact.

Exact `response_shape_store.py::validate()` does not bind several persisted structural evidence fields to an externally expected/original snapshot identity.

After valid atomic persistence, SIS independently modified individual persisted fields and called exact `read_and_validate()` with the correct attempt/request/task/writer/plan/authority/provider/model expected identities.

Observed:

- `response_sha256` tamper → `ACCEPTED_TAMPER`;
- `response_bytes` tamper → `ACCEPTED_TAMPER`;
- `http_status` tamper → `ACCEPTED_TAMPER`;
- `top_level_keys` tamper → `ACCEPTED_TAMPER`;
- `output_count` replacement with a still self-consistent value → `ACCEPTED_TAMPER`.

The validator currently checks only:
- response_sha256 is syntactically 64-hex;
- response_bytes is a positive integer;
- http_status is an integer;
- top_level_keys is a list of strings;
- output_count equals current output_items length.

It cannot establish that those persisted fields are the same evidence originally derived from the provider response.

This is especially material because the diagnostic artifact exists precisely to preserve provider response shape after the raw body is intentionally discarded.

Therefore changing the stored response digest/byte-count/HTTP status/top-level structural evidence can survive strict readback, which violates the exact task requirement that tamper fail closed.

## Why 9/9 PASS does not close this

The exact test suite tests identity tamper using `plan_sha256`, which is externally bound.

It does not tamper the unbound diagnostic evidence fields listed above.

Thus 9/9 is a real suite PASS but insufficient for the exact independent verification contract.

## Required correction

KOD successor must make readback bind the complete diagnostic evidence identity.

A safe correction should include one of these equivalent fail-closed designs:

1. persist an overall diagnostic snapshot identity/hash derived from the complete canonical snapshot and require an externally supplied expected snapshot hash on readback; or
2. pass exact expected response/shape evidence fields to readback and compare each; or
3. another independently verifiable construction that makes changes to persisted response_bytes/response_sha256/http_status/top_level_keys/output_items/counts fail closed.

Required successor tests must tamper individually:
- response_bytes;
- response_sha256;
- http_status;
- top_level_keys;
- output_count;
- output item type/keys/classification/role/content_count;
- content item type/keys/classification;
- project authority flags;
- existing exact identity fields.

Existing privacy, ordering, normalizer fail-closed, atomic persistence and consumed-one-shot semantics must remain unchanged.

No provider call or credential access is required for correction/reverify.

## Historical boundary

Historical consumed live acceptance remains BLOCKED.

Missing historical provider shape was not reconstructed.

Consumed authority remains non-reusable.

Project acceptance remains NOT_GRANTED.

## Boundary accounting

Provider calls: `0`.
Credential accesses: `0`.
Credential creates: `0`.
Parser correction: `0`.
Production deployment: `0`.
Canonical secretref mutation: `0`.
Historical shape reconstruction: `0`.
Project acceptance: `NOT_GRANTED`.
Project-state mutation: `false`.

## Terminal result

`BLOCKED_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01: READBACK_DOES_NOT_BIND_RESPONSE_SHAPE_EVIDENCE_FIELDS`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: independent exact-byte/tamper verification of booster v2 response-shape diagnostic persistence r0.1
СТАТУС: exact blocker
