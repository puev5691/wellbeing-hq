# KOO → KOD: prepare OpenAI Entity booster live-capable path r0.1

status: TASK
priority: P0
execution_mode: BOUNDED_NON_LIVE_ENGINEERING
project_time: omitted; trusted project-time source not used

## OPERATOR authority

Decision:
`AUTHORIZE_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01`

Decision record:
`entities/koordinator/current/KOO__openai-booster-live-path-prep-decision.md`

decision commit:
`d33d44ae593443a94029868692de83f787202654`.

This authority allows preparation only.
It does NOT authorize any live provider call.

## Resume-First

Start with fresh GitHub preflight of:
`puev5691/wellbeing-hq`.

Verify current KOD writer/recovery boundary before mutation.

## Verified basis

Entity booster r0.2 independent SIS PASS:
`entities/sisadmin/outbox/SIS__entity-booster-runtime-r02-independent-verify__KOO.md`
commit `b0b858d18ef518fa336d3eea9441b392922697c3`
verdict `PASS_SIS_ENTITY_BOOSTER_RUNTIME_R02_INDEPENDENT_VERIFY`.

Booster package:
`puev5691/wellbeing-hq@4ac08228960c2bbb8aa00bf607a0f0bdb13485f3:entities/koder/outbox/entity-booster-runtime-r02`

Final live-worker independent PASS:
commit `18af0b778d5b30f15c20da989a39006f503dcff3`.

OpenAI readiness evidence already established in HQ:
- dedicated project/account/prepaid readiness;
- restricted project credential provisioned outside project artifacts;
- Luna/Terra/Sol/Astra entitlement evidence.

Fresh preflight must independently resolve the exact current evidence artifacts/identities before using them.

## Goal

Build one live-capable OpenAI integration candidate that connects the verified Entity-facing booster r0.2 contract to the already verified live-worker contract without weakening either boundary.

The candidate must remain non-live and must prove only readiness for a later separately authorized one-shot D0 call.

## Required work

### 1. Exact composition

Reuse verified components where possible.

The path should be conceptually:

`EntityRequest/booster authority → live-execution gate → verified live-worker request plan → OpenAI /v1/responses → bounded ResourceResult → requesting Entity review`

Do not create a second competing gateway/orchestrator.

### 2. Separate live authority object

Design an explicit live execution authority object/contract that binds at minimum:
- exact requester Entity;
- exact task identity;
- exact writer identity;
- provider = OpenAI;
- exact model;
- data/privacy class;
- tools = none for first D0 path;
- one request only;
- retries = 0;
- fallback = none;
- bounded input/output;
- exact expiry/use-once semantics if applicable;
- exact restricted credential reference identifier, never credential value.

Absence or mismatch must fail closed before credential resolution/transport.

### 3. Credential boundary

Do not read or use any real credential in this task.

Implement/test only the secret-reference resolver interface and failure behavior.

Credential material must never appear in:
- GitHub;
- logs;
- result payloads;
- exceptions;
- fixtures;
- test output.

### 4. Live-worker integration

Preserve verified live-worker guarantees:
- durable one-shot ledger;
- exactly-one claimant;
- retries=0;
- no provider fallback;
- hard timeout;
- max response/read bound;
- redirect fail-closed;
- exact OpenAI endpoint/method contract;
- reservation before real credential resolution/transport for the live path;
- no repeated live attempt after uncertain/claimed state unless a separately authorized recovery policy exists.

Resolve carefully any distinction between booster pre-admission checks and live-worker reservation ordering. Document the final invariant.

### 5. Non-live deterministic proof

Provide deterministic tests with no network and no credential access proving:
- valid exact live authority can reach the mocked/sentinel live-worker boundary;
- missing live authority blocked;
- wrong Entity blocked;
- wrong task/writer blocked;
- wrong provider/model blocked;
- tools not-none blocked;
- privacy/data-class mismatch blocked;
- duplicate authority/request blocked;
- resolver failure blocks without transport;
- redirect/retry/fallback remain disabled;
- provider response malformed/oversized/mismatched blocks;
- result still has project_acceptance=NOT_GRANTED;
- requesting Entity review remains required;
- no writer/project-state mutation.

### 6. Future one-call D0 profile

Produce one exact candidate profile for the later decision gate, but do not execute it.

Use:
- provider OpenAI;
- minimal already-entitled model: Luna unless fresh evidence identifies a safer/more appropriate smallest option;
- D0 synthetic payload only;
- one call;
- retries=0;
- fallback=none;
- no tools;
- bounded output;
- no project-state mutation;
- requester Entity review after result.

Include the exact fields KOO must bind in the future live decision.

### 7. Readiness result

State explicitly:
- whether candidate is technically ready for independent SIS verification;
- what exact external facts remain before a live call;
- whether restricted credential reference is verifiably present without reading its value;
- whether a new separate LIVE_EXECUTION_AUTHORITY decision remains required.

## Forbidden

- live OpenAI/provider call;
- Anthropic live work;
- real credential read/use/create;
- credential disclosure;
- billing/account mutation;
- production deployment;
- automation;
- Project Sources changes;
- project acceptance;
- provider/gateway writer authority.

## Expected terminal result

Return exactly one:

`PASS_KOD_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01_READY_FOR_SIS_VERIFY`

or

`BLOCKED_KOD_OPENAI_ENTITY_BOOSTER_LIVE_PATH_PREP_R01: <exact blocker>`

or exact FAIL.

Terminal result must include:
- candidate locator/identity;
- reused exact components;
- test results;
- future D0 profile;
- live calls = 0;
- credential accesses = 0;
- next verifier = SIS.

Address result to KOO and SIS.
Stop after terminal result.
