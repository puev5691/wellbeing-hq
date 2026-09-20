# KOO → SIS: reverify OpenAI booster result persistence/readback r0.2

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_REVERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## Exact KOD successor terminal

`entities/koder/outbox/KOD__openai-booster-result-persistence-r02-result__KOO-SIS.md`

commit:
`6f0ab0827013329c305d97d9b09f99b8ed5e609c`

blob:
`5c5d92e7113ef8c7a7da33a785174aa0346a36c9`

verdict:
`PASS_KOD_OPENAI_BOOSTER_RESULT_PERSISTENCE_R02_READY_FOR_SIS_REVERIFY`

## Exact successor candidate

`entities/koder/outbox/openai-booster-result-persistence-r02/`

boundary commit:
`b76e385c139a1b2b0ccdf2ff6481aa1062c161a1`

expected package tree:
`6fcc2f0325256aab96a9c52c913d53875606070f`

Do not trust metadata without independent exact-byte readback.

## Exact blocker being corrected

`BLOCKED_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01: READBACK_VALIDATION_DOES_NOT_BIND_RESPONSE_IDENTITY_FIELDS`

Original blocker commit:
`fd312d09bb0ee4a16ed85f7f75d86540e87c9b24`

## Current-state reconciliation

Before reverify:
- confirm successor terminal remains current and not superseded;
- confirm boundary commit/tree remain the intended candidate;
- confirm predecessor r0.1 remains immutable;
- confirm historical R03 requester review remains BLOCKED;
- confirm project_acceptance remains NOT_GRANTED.

## Independent exact-byte verification

### 1. Package identity

Independently verify:
- package composition;
- tree;
- file blobs;
- declared SHA-256;
- manifest consistency;
- successor differs from predecessor only as documented.

### 2. Schema v2 exact key sets

Verify schema:
`wb.openai.booster.review_result.v2`

Verify exact allowed key sets at:
- top level;
- `response_evidence`;
- `review_payload`.

Fail closed on:
- missing required key;
- unexpected extra key;
- wrong type;
- schema/version mismatch.

### 3. Full readback evidence binding

Independently verify exact readback validation of at least:
- response_bytes;
- response_sha256;
- http_status;
- parser_status;
- plan_sha256;
- authority_sha256;
- attempt_key;
- request_sha256;
- task commit/blob;
- writer blob;
- provider;
- model;
- review payload bytes/SHA-256;
- requester_review_required;
- project_acceptance;
- project_state_mutation;
- provider_writer_authority;
- gateway_writer_authority.

### 4. Cross-field semantics

Verify independently:
- response_bytes equals exact canonical UTF-8 JSON byte length of `response_evidence`;
- response_sha256 equals SHA-256 of those same canonical bytes;
- parser_status is exactly allowed value;
- review text is reconstructed from exact response_evidence;
- review_payload text/bytes/SHA-256 match reconstruction;
- plan_sha256 matches exact expected plan identity;
- authority_sha256 matches exact expected authority identity;
- accepted technical semantics require HTTP 200, provider_calls=1, retries=0, fallback=none, project_acceptance=NOT_GRANTED and no project-state/writer authority.

### 5. Per-field tamper reproduction

Independently tamper each field and require exact readback validation failure:
- response_bytes;
- response_sha256;
- http_status;
- parser_status;
- plan_sha256;
- authority_sha256;
- missing required key;
- unexpected extra key;
- wrong type;
- schema/version;
- review payload text/bytes/SHA;
- response_evidence;
- task commit/blob;
- writer blob;
- provider;
- model;
- request identity;
- attempt key;
- authority/result flags;
- calls/retry/fallback.

Also reproduce the exact predecessor defect:
tamper only `response_sha256` after atomic persistence and verify successor `read_and_validate()` blocks it.

### 6. Atomic/durable persistence

Verify unchanged:
- same-directory unique temp;
- mode 0600;
- full write;
- file fsync;
- atomic replace;
- parent-directory fsync;
- strict readback validation.

### 7. Consumed one-shot semantics

Verify:
- post-transport persistence failure leaves one-shot consumed;
- no retry/replay can reconstruct missing content;
- no second provider call is implied or enabled.

### 8. Deterministic suite

Rerun exact immutable successor tests.
Expected KOD basis: 24 tests / 0 failures / 0 errors.

During SIS reverify:
- provider calls = 0;
- credential accesses = 0;
- production deployment = 0.

## Historical R03 boundary

Historical R03 remains:
- technical correlation PASS;
- requester review BLOCKED;
- project_acceptance NOT_GRANTED;
- missing provider body not reconstructed.

Do not promote historical requester review to PASS.

## Forbidden

- any live provider call;
- credential read/use/create;
- production deployment;
- canonical secretref mutation;
- historical R03 body reconstruction;
- project acceptance;
- project-state mutation.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R02_REVERIFY`

or

`BLOCKED_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R02: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- immutable successor/package identity result;
- schema/key-set result;
- full readback binding result;
- per-field tamper results;
- predecessor response_sha256 defect regression result;
- atomic persistence result;
- consumed-one-shot semantics result;
- deterministic test result;
- provider calls=0;
- credential accesses=0;
- historical R03 requester review remains BLOCKED;
- historical R03 project_acceptance remains NOT_GRANTED;
- whether successor is ready for the next development/acceptance step.

Address terminal result to KOO.
Stop after terminal result.