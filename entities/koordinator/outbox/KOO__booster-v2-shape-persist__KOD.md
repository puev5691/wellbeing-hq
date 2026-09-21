# KOO → KOD: add safe pre-normalization response-shape diagnostics r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_DIAGNOSTIC_ARCHITECTURE
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary before mutation.

## Exact blocker basis

`entities/koder/outbox/KOD__booster-v2-provider-shape-diag-r01-blocker__KOO-SIS.md`

commit:
`21ff483e7d08fed6467462cbb87eb2d9ad4aa477`

blob:
`ef0a311569113a9f032594efa6bb1ae7b3b11866`

terminal:
`BLOCKED_KOD_BOOSTER_V2_PROVIDER_SHAPE_DIAG_R01: EXACT_PROVIDER_OUTPUT_ITEM_SHAPE_NOT_PRESERVED_IN_EXISTING_EVIDENCE`

## Goal

Build one immutable non-live diagnostic architecture candidate that, for future separately authorized live attempts, safely persists enough pre-normalization provider response-shape evidence to diagnose parser failures without requiring a second provider call.

Do not change the current historical consumed attempt and do not guess its missing shape.

## Required diagnostic evidence

Persist a bounded structural snapshot before review-result normalization.

At minimum capture:
- provider/model;
- attempt key;
- request/task/writer/plan/authority correlation identities;
- HTTP status;
- response byte count and SHA-256;
- top-level provider-response key set;
- exact `output[]` item count;
- for each output item: exact item `type` and exact key set;
- for message items: exact role and exact content item count;
- for each message content item: exact content `type` and exact key set;
- enough bounded classification data to distinguish assistant text, benign metadata/reasoning container, tool/action request, tool/action output, unknown item.

## Privacy/content boundary

By default persist structure, not unrestricted provider content.

Do NOT persist:
- credential values;
- Authorization headers;
- environment variables;
- cookies/tokens;
- secretref values beyond approved locator identity already present in task metadata;
- arbitrary full raw provider body unless a later separately authorized diagnostic design explicitly requires it.

If a tiny content excerpt is required for type disambiguation, it must be separately justified and bounded; otherwise omit content entirely.

## Failure ordering

For future live execution, diagnostic shape persistence must occur after provider JSON validation but before review-result normalization.

Required future order:
`claim → transport → JSON parse → persist diagnostic shape → normalize → persist review-result v2 → strict readback → terminal`

If diagnostic persistence fails after transport:
- one-shot remains consumed;
- terminal BLOCKED/FAIL;
- no retry;
- no second provider call;
- no parser guess.

If review normalization fails:
- diagnostic shape artifact remains available for later non-live diagnosis;
- review-result artifact may be absent;
- technical PASS remains forbidden.

## Atomic/durable semantics

Use bounded atomic persistence comparable to verified result persistence:
- same-directory temp;
- mode 0600;
- complete write;
- file fsync;
- atomic replace;
- parent-directory fsync;
- strict readback/identity validation.

## Schema

Define an exact versioned diagnostic schema with exact allowed key sets and fail-closed readback.

Unknown/unexpected diagnostic fields must not be silently ignored.

## Runtime integration boundary

Integrate with the existing installed booster-v2 architecture conceptually, but do not deploy in this task.

Preserve:
- canonical secretref handling;
- durable one-shot claim before provider transport;
- calls=1;
- retries=0;
- fallback=none;
- tools=none;
- exact provider/model/task/writer/privacy bounds;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

## Deterministic tests

Using synthetic/replay fixtures only, prove at minimum:
- message/output_text-only response produces diagnostic shape + normal review artifact;
- response with extra benign-looking non-message item produces diagnostic shape even if normalizer blocks;
- response with tool/action item produces diagnostic shape and normalizer still blocks;
- response with unknown item type produces diagnostic shape and normalizer blocks;
- malformed JSON produces no false diagnostic PASS;
- diagnostic persistence failure keeps one-shot consumed in simulated post-transport path;
- tamper of diagnostic type/key-set evidence fails readback;
- credential-like material absent;
- provider calls=0;
- credential accesses=0.

## Historical boundary

Historical consumed live acceptance remains BLOCKED.
Do not reconstruct its missing provider body/output shape.
Do not promote requester review or project acceptance.

## Forbidden

- any live provider call;
- credential read/use/create;
- production deployment;
- parser correction based on guess;
- broad allowlisting of reasoning/tool/metadata types without evidence;
- project acceptance;
- project-state mutation.

## Expected terminal

Return exactly one:

`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01_READY_FOR_SIS_VERIFY`

or

`BLOCKED_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R01: <exact blocker>`

or exact FAIL.

Terminal result must include:
- immutable candidate locator/identity;
- diagnostic schema;
- future failure ordering;
- atomic/readback semantics;
- deterministic test results;
- provider calls=0;
- credential accesses=0;
- next verifier=SIS.

Address result to KOO and SIS.
Stop after terminal result.