# KOO → SIS: independent verify OpenAI booster result persistence/reviewability r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_VERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## Exact KOD terminal result

`entities/koder/outbox/KOD__openai-booster-result-persistence-r01-result__KOO-SIS.md`

commit:
`044343edf17625fbabf743373de3b4e47bcb2830`

blob:
`955f2caa464521b3e27b37a5879413f092e174c1`

verdict:
`PASS_KOD_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01_READY_FOR_INDEPENDENT_VERIFY`

## Exact candidate

`entities/koder/outbox/openai-booster-result-persistence-r01/`

package commit:
`13243aa2a0cf9bc667248c7f8ae7f8e4872898cd`

expected package tree:
`29fbc01f07f337c1d2488b6f278fdab0a23099f0`

Do not trust package metadata without independent readback.

## Authority/process basis

The originating KOO task designated SIS as the next verifier after KOD PASS.
This verification is therefore already covered by the existing approved process/role boundary.
KOD delivery/dispatch metadata does not itself create instruction authority and is not substantive acceptance.

## Current-state reconciliation

Before verification:
- confirm KOD terminal result remains current and not superseded;
- confirm package commit/tree remain the intended immutable candidate;
- confirm historical R03 requester-review blocker remains unchanged;
- confirm no later provider result or project acceptance was created.

Historical R03 body must not be reconstructed.
Historical R03 requester review must not be promoted to PASS.

## Independent verification scope

### 1. Immutable candidate identity

Independently verify:
- exact package composition;
- Git tree;
- Git blobs;
- declared SHA-256 values;
- manifest consistency.

Verify exact reused dependencies:
- final verified live-worker lineage;
- SIS-verified live-child path basis.

### 2. Review-result schema

Inspect `wb.openai.booster.review_result.v1` and independently verify it contains enough bounded information for later substantive D0 requester review:
- exact attempt key;
- request identity;
- task commit/blob;
- writer blob;
- plan/authority identity;
- provider/model;
- HTTP status;
- provider call count;
- retries/fallback;
- response byte count and SHA-256;
- parser/normalization status;
- bounded normalized assistant-text review payload and its own identity;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false;
- provider/gateway writer authority=false.

### 3. Normalized D0 payload equivalence

Verify the normalizer preserves exactly the bounded assistant output needed for D0 requester review.

Confirm:
- exact assistant `message/output_text` content is reviewable;
- unexpected tool/action output fails closed rather than being silently dropped;
- provider/model mismatch fails closed;
- normalization cannot turn malformed/truncated provider data into a valid review payload.

### 4. Exact correlation

Independently verify persisted result correlation to:
- exact attempt;
- request;
- task;
- writer;
- provider;
- model;
- plan;
- authority.

Tamper/mismatch must fail closed.

### 5. Secret/privacy exclusion

Verify persisted review artifacts exclude:
- credential values;
- Authorization headers;
- secret-store value material;
- environment values;
- cookies/tokens;
- unrelated headers;
- unnecessary sensitive provider metadata.

Do not read or use any real credential during this verification.

### 6. Atomic/durable persistence

Independently inspect and test the exact sequence:
same-directory temp 0600 → full write → file fsync → atomic replace → parent-directory fsync → readback identity validation.

Verify fail-closed behavior for:
- write failure;
- file fsync failure;
- rename/replace failure;
- directory fsync failure;
- serialization failure;
- readback/identity mismatch;
- oversized/truncated review payload.

### 7. Post-consumed-one-shot failure semantics

Verify that if provider transport has already happened and result persistence then fails:
- durable one-shot remains consumed;
- result is BLOCKED/FAIL, never false PASS;
- no retry or replay is allowed to reconstruct missing content;
- no second provider call is implied.

### 8. Deterministic non-live tests

Rerun exact immutable test suite with provider calls disabled and credential environment absent.

Required outcomes include:
- synthetic/replay result persists reviewable payload;
- later requester review succeeds from persisted artifact with provider calls delta = 0;
- secret-like material absent;
- persistence failure fail-closed;
- oversized result fail-closed;
- malformed result fail-closed;
- model mismatch fail-closed;
- unexpected tools/actions fail-closed;
- retries=0;
- fallback=none;
- project_acceptance=NOT_GRANTED;
- project-state mutation=false;
- consumed one-shot cannot replay to recover deleted/missing content.

## Historical R03 boundary

The historical R03 result remains:
- technical correlation PASS;
- substantive requester review BLOCKED;
- project acceptance NOT_GRANTED.

This candidate is only for future executions.

## Forbidden

- any OpenAI/provider call;
- credential read/use/create;
- production deployment;
- canonical secretref mutation;
- reuse of consumed R03 authority;
- historical R03 body reconstruction;
- project acceptance;
- project-state mutation.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01_INDEPENDENT_VERIFY`

or

`BLOCKED_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- whether immutable candidate/dependencies match;
- review-result schema result;
- normalized D0 reviewability result;
- correlation result;
- secret/privacy exclusion result;
- atomic persistence/failure-semantics result;
- deterministic test result;
- provider calls = 0;
- credential accesses = 0;
- historical R03 requester review remains BLOCKED / project_acceptance NOT_GRANTED;
- whether KOO may consider the candidate ready for the next development/acceptance step.

Address terminal result to KOO.
Stop after terminal result.