# KOO → SIS: verify booster v2 response-shape diagnostic persistence r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_VERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## Exact KOD terminal

`entities/koder/outbox/KOD__booster-v2-shape-diag-persist-r01-result__KOO-SIS.md`

commit:
`e98d39c58a19220166c409317ed980acf32b0931`

blob:
`327e3825551b9ebc8033fc27811d3066cf637c65`

verdict:
`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01_READY_FOR_SIS_VERIFY`

## Exact immutable candidate

`entities/koder/outbox/openai-booster-shape-diagnostic-persistence-r01/`

boundary commit:
`8114606922db6cf69aeb9157639d7ba408972a03`

expected package tree:
`6777a5f4ba0d6294ed9d147ac3c74b3875107e24`

Do not trust manifest/metadata without independent exact-byte readback.

## Exact blocker basis

`BLOCKED_KOD_BOOSTER_V2_PROVIDER_SHAPE_DIAG_R01: EXACT_PROVIDER_OUTPUT_ITEM_SHAPE_NOT_PRESERVED_IN_EXISTING_EVIDENCE`

blocker commit:
`21ff483e7d08fed6467462cbb87eb2d9ad4aa477`

## Independent verification scope

### 1. Immutable identities

Independently verify:
- package composition/tree/blobs/SHA-256/manifest;
- exact reused one-shot live-worker identity;
- exact reused review-result v2 identities;
- no competing provider/gateway/live-worker stack introduced.

### 2. Diagnostic schema/key sets

Verify exact schema:
`wb.openai.booster.response_shape_diag.v1`

Verify exact allowed key sets and fail-closed behavior for:
- missing required key;
- unexpected extra key;
- wrong type;
- schema/version mismatch;
- identity mismatch.

### 3. Privacy/content exclusion

Verify persisted diagnostics exclude:
- credential values;
- Authorization headers;
- environment variables;
- cookies/tokens;
- canonical secretref locator;
- unrestricted raw provider body;
- raw output_text;
- raw tool arguments.

Diagnostic artifact must preserve structure only unless explicitly and narrowly defined otherwise by exact schema.

### 4. Ordering before normalization

Verify future flow exactly:
`claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`

Verify diagnostic persistence occurs before review normalization and survives later normalization failure.

### 5. Atomic persistence/readback

Independently inspect and test:
- same-directory unique temp;
- mode 0600;
- complete write;
- file fsync;
- atomic replace;
- parent-directory fsync;
- strict schema/identity readback.

Tamper must fail closed.

### 6. Classification semantics

Verify diagnostic classification enum and behavior:
- assistant_text;
- benign_metadata_or_reasoning_container;
- tool_action_request;
- tool_action_output;
- unknown.

Classification is diagnostic only.
It must NOT itself grant parser allowlist or change tools=none semantics.

Verify classification is derived from structural type/key evidence, not from hidden content inference.

### 7. Preserve current normalizer fail-closed

Verify current review-result v2 normalizer remains unchanged/fail-closed for:
- reasoning/metadata item;
- tool/action item;
- unknown item;
until a separately verified parser correction is authorized.

### 8. Post-transport diagnostic persistence failure

Independently verify simulated provider transport followed by diagnostic persistence failure:
- one-shot remains consumed;
- terminal BLOCKED/FAIL;
- no retry/replay;
- no second provider call;
- no fabricated diagnostic or review PASS.

### 9. Replay-only deterministic suite

Rerun exact immutable 9-test suite using synthetic/replay fixtures only.

Expected:
- 9 tests;
- 0 failures;
- 0 errors;
- provider calls=0;
- credential accesses=0;
- deployment=0.

Verify cases include:
- plain assistant output_text;
- extra benign-looking item;
- tool/action item;
- unknown item;
- malformed JSON;
- post-transport diagnostic persistence failure;
- diagnostic tamper;
- write/fsync/rename failure;
- credential/raw-content exclusion.

## Historical boundary

Historical consumed live acceptance remains BLOCKED.
Missing historical response shape is not reconstructed.
Consumed authority remains non-reusable.
Project acceptance remains NOT_GRANTED.

## Forbidden

- live provider call;
- credential read/use/create;
- parser correction;
- production deployment;
- canonical secretref mutation;
- historical shape reconstruction;
- project acceptance;
- project-state mutation.

## Expected terminal

Return exactly one:

`PASS_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01_VERIFY`

or

`BLOCKED_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- immutable candidate identity result;
- schema/key-set result;
- privacy/content exclusion result;
- ordering result;
- atomic/readback result;
- classification-semantics result;
- normalizer fail-closed preservation result;
- post-transport failure-semantics result;
- deterministic tests result;
- provider calls=0;
- credential accesses=0;
- deployment=0;
- whether candidate is ready for the next separately authorized diagnostic-live step.

Address terminal result to KOO.
Stop after terminal result.