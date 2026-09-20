# KOO → SIS: verify booster result-v2 runtime integration r0.1

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_VERIFY
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current SIS writer/recovery boundary before execution.

## Exact KOD terminal

`entities/koder/outbox/KOD__booster-result-v2-integration-r01-result__KOO-SIS.md`

commit:
`80fcd7955451c26d3d86cd4333b1322c67ce6044`

blob:
`bfc51826fddaed8f55cd90126c0436a72a88fd50`

verdict:
`PASS_KOD_BOOSTER_RESULT_V2_INTEGRATION_READY_FOR_SIS_VERIFY`

## Exact integration candidate

`entities/koder/outbox/openai-booster-result-v2-integration-r01/`

boundary commit:
`b0779b4215de43ca96888df94835e97e3e15402e`

expected package tree:
`600f4ba691152db74dc5818c85dc822bba000bc3`

Do not trust metadata without independent exact-byte readback.

## Current-state reconciliation

Before verification:
- confirm terminal remains current and not superseded;
- confirm package commit/tree remain exact candidate;
- confirm verified persistence/readback v2 basis remains unchanged;
- confirm verified live-worker/live-child identities remain unchanged;
- confirm no production deployment or provider execution has occurred from this candidate.

## Independent verification scope

### 1. Exact component identities

Independently verify exact candidate composition/tree/blobs/SHA-256 and manifest.

Verify reused exact identities for:
- verified persistence/readback v2;
- final verified one-shot live-worker;
- SIS-verified live-child path.

Confirm no competing provider/gateway/live-worker stack was introduced.

### 2. Future runtime flow

Verify exact candidate flow:

`claim → transport → normalize → persist schema v2 → strict readback → terminal`

Verify terminal technical PASS cannot occur before:
- provider reply has passed exact bounded validation;
- normalization into exact schema v2;
- durable persistence;
- strict v2 readback validation.

Verify post-transport persistence/readback failure yields BLOCKED/FAIL and preserves consumed one-shot with no retry/replay/new provider call.

### 3. Candidate systemd contract

Inspect candidate unit:
`wellbeing-openai-booster-result-v2.service.candidate`

Verify it preserves the existing verified boundary:
- systemd `LoadCredentialEncrypted`;
- exact canonical secretref mapping/object identity;
- normal KOD-triggered invocation design;
- required network capability for exact future HTTPS path;
- narrow state write scope;
- no legacy TTY fallback;
- no unexpected privilege expansion;
- no deployment/install side effect in verification.

### 4. Result path/write boundary

Verify future review-result directory:
`/var/lib/wellbeing/openai-booster-live-child-r01/review-results`

Verify:
- it stays under existing state boundary;
- candidate write scope is not broader than required;
- review artifacts use mode 0600 through verified persistence v2;
- artifact naming/correlation is deterministic;
- later requester review can read exact persisted artifact without provider access;
- no credential/Authorization/environment/cookie/token/secretref-locator material is persisted.

### 5. Inherited v2 protections

Confirm integration reuses exact independently verified v2 persistence/readback bytes where declared.

Re-run or independently reproduce enough of the exact v2 strict/tamper suite to prove integration has not bypassed:
- exact key sets;
- full evidence binding;
- cross-field semantics;
- response_sha256 regression fix;
- plan/authority binding;
- review payload binding;
- tamper fail-closed behavior.

### 6. Integration replay tests

Rerun exact candidate integration tests using replay/synthetic fixtures only.

Expected KOD basis:
- inherited v2: 24/24 PASS;
- integration: 7/7 PASS;
- total: 31/31 PASS.

Verify at minimum:
- success path persists exact schema v2 artifact;
- terminal PASS only after durable persistence + strict readback;
- later requester review succeeds from persisted artifact with provider calls delta=0;
- exact attempt/request/task/writer/provider/model/plan/authority correlation;
- v2 tamper protections remain active;
- secret/privacy exclusion remains active;
- no retries/fallback.

### 7. Post-transport persistence-failure semantics

Independently verify simulated transport followed by persistence/readback failure:
- ledger remains consumed;
- no false PASS;
- no retry/replay;
- no second provider call;
- requester review success is not fabricated.

## Preserved execution bounds

Verify future integration still binds:
- provider=openai;
- endpoint=`https://api.openai.com/v1/responses`;
- model=`gpt-5.6-luna`;
- D0_SYNTHETIC;
- privacy=`synthetic_only`;
- tools=none;
- calls=1;
- retries=0;
- fallback=none;
- max output tokens=64;
- max response bytes=16384;
- timeout=30s;
- use-once;
- requester_review_required=true;
- project_acceptance=NOT_GRANTED;
- project_state_mutation=false.

## Historical R03 boundary

Historical R03 remains:
- technical correlation PASS;
- requester review BLOCKED;
- project_acceptance NOT_GRANTED;
- missing provider body not reconstructed.

Do not reinterpret or promote historical R03.

## Forbidden

- any live provider call;
- credential read/use/create;
- production deployment;
- installing/enabling candidate unit;
- canonical secretref mutation;
- billing/account mutation;
- project acceptance;
- project-state mutation.

## Expected terminal result

Return exactly one:

`PASS_SIS_BOOSTER_RESULT_V2_INTEGRATION_R01_VERIFY`

or

`BLOCKED_SIS_BOOSTER_RESULT_V2_INTEGRATION_R01: <exact blocker>`

or exact FAIL.

Human-facing result must state:
- exact component identity result;
- future runtime flow result;
- systemd contract result;
- result path/write-boundary result;
- inherited v2 protection result;
- integration replay-test result;
- post-transport persistence-failure semantics result;
- provider calls=0;
- credential accesses=0;
- production deployment=0;
- historical R03 requester review remains BLOCKED;
- project_acceptance remains NOT_GRANTED;
- whether candidate is ready for the next development/acceptance step.

Address terminal result to KOO.
Stop after terminal result.