# KOO → KOD: fix OpenAI booster live-result persistence/reviewability r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_ENGINEERING
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary before mutation.

## Exact blocker basis

`entities/koder/outbox/KOD__openai-booster-d0-r03-requester-review-blocker__KOO.md`

commit:
`fecac6da59aa1ba4648aeb674017b59f037425b8`

blob:
`f4c6d58b1d6d4e683c150561fd42be96366f36c9`

terminal:
`BLOCKED_KOD_OPENAI_ENTITY_BOOSTER_D0_R03_REQUESTER_REVIEW: PROVIDER_RESPONSE_BODY_NOT_PERSISTED_FOR_SUBSTANTIVE_D0_REVIEW`

Verified:
- provider/model/result correlation = PASS;
- exact consumed attempt correlation = PASS;
- technical bounded-result integrity = PASS;
- semantic/content usability = NOT_VERIFIABLE_FROM_PERSISTED_EVIDENCE;
- provider calls during review = 0;
- R03 authority consumed/non-reusable;
- project_acceptance = NOT_GRANTED;
- project-state mutation = false.

## Goal

Fix future live-result persistence/reviewability so that a bounded provider result can be substantively reviewed after a one-shot execution without any repeat provider call.

Do not change the current historical R03 result and do not attempt to reconstruct its missing provider body.

## Required design

Create one exact candidate that, for future bounded live executions, persists a reviewable result artifact separate from credentials and authority state.

The persisted result must contain only what is needed for requester review and correlation.

### Minimum required persisted fields

- schema/version;
- exact attempt key;
- exact request/task/writer identity;
- provider actually used;
- model actually used;
- HTTP status;
- provider call count;
- retries/fallback state;
- bounded provider response body or a bounded normalized review payload sufficient for substantive D0 review;
- response byte count;
- response SHA-256;
- parser/normalization status;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false;
- provider/gateway writer authority=false.

### Response-body boundary

Persist the minimum reviewable content needed for D0 requester review.

For this D0 path, prefer a normalized bounded text/output representation rather than indiscriminate full raw provider envelope persistence, if the exact provider parser can prove semantic equivalence for the review purpose.

If raw envelope persistence is technically necessary, bound it strictly and redact/exclude fields not needed for review.

Do not persist:
- credential values;
- Authorization headers;
- secret-store paths containing values;
- environment values;
- cookies/tokens;
- unrelated request headers;
- any provider-side identifier that is unnecessary for bounded review, unless exact correlation requires it.

### Size and safety

Preserve the existing max provider response bound.
Add a separate persisted review-payload size bound if smaller/safer.
Fail closed if the result cannot be persisted safely and atomically.

Persistence must be atomic/durable enough that a successful one-shot technical result cannot be reported PASS while leaving requester review impossible.

Define exact failure semantics for:
- provider success but review payload persistence failure;
- truncated/oversized review payload;
- malformed provider body;
- model mismatch;
- write/fsync/rename failure;
- result identity mismatch.

### One-shot / authority boundaries

Do not weaken:
- durable claim before provider transport;
- calls=1;
- retries=0;
- fallback=none;
- exact provider/model/task/writer/privacy/tools binding;
- canonical secretref handling;
- no legacy TTY fallback;
- requester review required;
- project_acceptance=NOT_GRANTED;
- no project-state mutation.

### Existing live-child path

Reuse the verified SIS live-child path and exact final live-worker where possible.
Do not create a competing execution stack unless an exact incompatibility requires it.

### Deterministic non-live tests

Add tests proving at minimum:
- successful synthetic/replay provider result persists reviewable payload;
- persisted payload correlates to exact attempt/request/task/writer/provider/model;
- requester review can be performed later with zero provider calls;
- credential-like material is absent from persisted result;
- persistence failure prevents a false reviewable PASS;
- oversized result fails closed;
- malformed result fails closed;
- model mismatch fails closed;
- no retry/fallback;
- project_acceptance remains NOT_GRANTED;
- no project-state mutation;
- consumed one-shot cannot be replayed to regenerate missing content.

## Historical R03 result boundary

The completed R03 provider result remains:
- technically correlated PASS;
- requester substantive review BLOCKED;
- project-level acceptance NOT_GRANTED.

This task must not retroactively promote that result.

## Forbidden

- any new OpenAI/provider call;
- reuse of consumed R03 authority;
- credential read/use/create;
- canonical secretref change;
- billing/account mutation;
- production deployment;
- project acceptance;
- project-state mutation;
- inventing/reconstructing the missing historical provider body.

## Expected terminal result

Return exactly one:

`PASS_KOD_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01_READY_FOR_INDEPENDENT_VERIFY`

or

`BLOCKED_KOD_OPENAI_BOOSTER_RESULT_PERSISTENCE_R01: <exact blocker>`

or exact FAIL.

Terminal result must include:
- candidate locator/identity;
- reused components;
- exact persisted review-result schema;
- persistence failure semantics;
- deterministic test results;
- provider calls = 0;
- credential accesses = 0;
- next verifier = SIS.

Address result to KOO and SIS.
Stop after terminal result.