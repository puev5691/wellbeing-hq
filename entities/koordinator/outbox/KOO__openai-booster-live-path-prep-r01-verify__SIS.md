# KOO → SIS: independent verify OpenAI Entity booster live-path prep r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_VERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight:
`puev5691/wellbeing-hq`.

Verify current SIS writer/recovery boundary before profile execution.

## Authority basis

OPERATOR decision:
`AUTHORIZE_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01`

Decision record:
`entities/koordinator/current/KOO__openai-booster-live-path-prep-decision.md`

decision commit:
`d33d44ae593443a94029868692de83f787202654`.

That decision explicitly authorizes the sequence:
1. KOD prepares the non-live live-capable OpenAI booster integration;
2. SIS independently verifies the resulting candidate;
3. only after SIS PASS may KOO open a separate OPERATOR gate for one bounded live D0 call.

Therefore this SIS verification already has authority from the OPERATOR decision + approved task-conveyor process + SIS role.

KOD next-verifier metadata is routing/result metadata only and does not create instruction authority.

## Exact KOD terminal result

`entities/koder/outbox/KOD__openai-entity-booster-live-path-prep-r01-result__KOO-SIS.md`

commit:
`43edbbfbf722944c385e815e9d3039a841aaa123`

blob:
`6681e0105c55e0a1f0952afb38eadda2c0fed5fc`

verdict:
`PASS_KOD_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01_READY_FOR_SIS_VERIFY`.

## Exact candidate

`entities/koder/outbox/openai-entity-booster-live-path-prep-r01/`

package commit:
`77541d053882a512bec46a006d8e9f35a68544b8`

expected package tree:
`97c6983d3000a06c0c515248d0619c11de2dec06`.

Do not trust package metadata without independent readback.

## Current-state reconciliation requirement

Before verification:
- confirm the KOD terminal result remains current and not superseded;
- confirm the OPERATOR decision remains current;
- confirm no later authority grants live execution;
- confirm the candidate package commit/tree remain the intended verification target.

If any of these changed, stop with exact blocker.

## Independent verification scope

### 1. Immutable candidate

Independently read exact package bytes and verify:
- package composition;
- Git tree;
- Git blobs;
- declared SHA-256 values;
- manifest consistency.

Verify reused exact components:
- Entity booster runtime r0.2 package and SIS PASS;
- final live-worker package and SIS PASS;
- exact OpenAI readiness evidence referenced by the candidate.

Do not accept KOD metadata alone as proof.

### 2. Deterministic non-live tests

Run the exact immutable candidate test suite in isolated non-live conditions with:
- network connection/name resolution denied where practical;
- real OpenAI/Anthropic credential environment absent;
- no candidate-byte modification.

Independently verify at minimum:
- valid exact live authority reaches mocked/sentinel live-worker boundary only;
- missing authority blocks;
- wrong Entity/task/writer blocks;
- wrong provider/model blocks;
- tools != none blocks;
- privacy/data-class mismatch blocks;
- duplicate/use-once authority blocks;
- resolver failure blocks with transport calls = 0;
- retries remain 0;
- fallback remains none;
- redirect fails closed;
- malformed/oversized/model-mismatched response blocks;
- project_acceptance remains NOT_GRANTED;
- caller writer unchanged;
- no project-state mutation;
- requester Entity review remains required.

### 3. Live-authority contract

Inspect the exact authority object/contract.

Verify it binds at least:
- Entity;
- task identity;
- writer identity;
- provider = OpenAI;
- exact model;
- privacy/data class;
- tools = none for future D0;
- one request only;
- retries = 0;
- fallback = none;
- bounded input/output;
- timeout/expiry/use-once semantics where declared;
- restricted credential reference identifier, never credential value.

Any absent/mismatched required field must fail closed before credential resolution/transport.

Verify this candidate itself does NOT create `LIVE_EXECUTION_AUTHORITY`.

### 4. Credential-reference boundary

No real credential may be read, used or created.

Verify:
- only a reference/resolver contract is present;
- credential value cannot appear in authority object, GitHub, logs, exceptions, results, fixtures or tests;
- resolver failure stops before provider transport;
- exact future secret reference must be separately verified before any live call.

### 5. One-shot/live-worker ordering

Independently verify compatibility between:
- booster pre-admission/authority checks;
- live-worker durable reservation/claim;
- credential resolution;
- provider transport.

The final invariant must preserve:
- invalid/mismatched authority blocked before credential resolution/transport;
- once a valid live attempt reaches claim stage, durable one-shot semantics prevent accidental repeat;
- no automatic retry/fallback after uncertain/claimed execution state unless separately authorized by a future recovery policy.

### 6. FUTURE-D0-PROFILE

Independently verify:
`FUTURE-D0-PROFILE.json`.

Confirm it is profile data only and grants no live authority.

Check that the proposed future first probe is bounded to:
- provider OpenAI;
- one exact already-entitled model;
- D0 synthetic payload;
- one call;
- retries = 0;
- fallback = none;
- tools = none;
- bounded output;
- requester review;
- no project-state mutation;
- project acceptance separate.

If Luna is selected, verify current evidence still supports its entitlement.

### 7. Readiness conclusion

State clearly:
- whether the candidate is technically ready for a later one-call decision gate;
- what exact facts still need to be bound at that future gate;
- whether the restricted credential reference itself has been verified without reading the value;
- whether any technical blocker remains before KOO may present OPERATOR with one exact D0 live-execution decision.

## Publication / delivery / receipt boundary

Treat separately:
- publication;
- dispatch;
- inbox placement;
- receipt;
- independent verification;
- substantive acceptance.

KOD dispatch/addressing to SIS does not itself authorize or prove SIS execution.
Receipt is not substantive acceptance.
This SIS result is an independent technical verification only.

## Forbidden

- live OpenAI/provider call;
- live Anthropic work;
- real credential read/use/create;
- credential value disclosure;
- billing/account mutation;
- production deployment;
- automation/cron;
- Project Sources mutation;
- project acceptance;
- granting live execution authority.

## Expected terminal result

Return exactly one:

`PASS_SIS_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01_INDEPENDENT_VERIFY`

or

`BLOCKED_SIS_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- whether immutable candidate/dependencies match;
- deterministic test result;
- live-authority contract result;
- credential-reference boundary result;
- FUTURE-D0-PROFILE result;
- whether KOO may now open the separate one-call OPERATOR live gate;
- live calls = 0;
- credential accesses = 0.

Address terminal result to KOO.
Stop after terminal result.