# KOO → KOD: integrate verified result persistence v2 into booster runtime

status: TASK
execution_mode: BOUNDED_NON_LIVE_RUNTIME_INTEGRATION
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary before mutation.

## Verified basis

SIS terminal:
`entities/sisadmin/outbox/SIS__openai-booster-result-persistence-r02-reverify__KOO.md`

commit:
`a9b2c084b7e747e66336ff35ed06fcd4f9c76016`

verdict:
`PASS_SIS_OPENAI_BOOSTER_RESULT_PERSISTENCE_R02_REVERIFY`

Verified successor:
`entities/koder/outbox/openai-booster-result-persistence-r02/`

boundary commit:
`b76e385c139a1b2b0ccdf2ff6481aa1062c161a1`

package tree:
`6fcc2f0325256aab96a9c52c913d53875606070f`

## Goal

Build one immutable future runtime-integration candidate that wires the independently verified result-persistence/readback v2 into the existing verified OpenAI booster live-child/live-worker path.

This task is non-live and non-production.

## Reuse required verified components

Reuse, rather than replace, the already verified boundaries where compatible:
- final one-shot live-worker lineage;
- SIS-verified live-child path on `ruvds-xnqc6`;
- canonical systemd `LoadCredentialEncrypted` mechanism;
- exact canonical secretref identity;
- durable one-shot claim semantics;
- exact OpenAI D0 scope binding.

Do not create a competing provider/gateway stack unless a verified incompatibility forces a blocker.

## Integration requirements

Future successful provider execution must not report terminal technical PASS until the reviewable result artifact has been durably persisted and strict v2 readback validation succeeds.

Wire exact schema:
`wb.openai.booster.review_result.v2`

Preserve:
- provider=openai;
- endpoint=`https://api.openai.com/v1/responses`;
- model=`gpt-5.6-luna`;
- D0_SYNTHETIC;
- synthetic_only;
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

Persist review result only after exact provider response validation/normalization and before terminal PASS.

On post-transport persistence/readback failure:
- one-shot remains consumed;
- terminal is BLOCKED/FAIL, never PASS;
- no retry/replay/new provider call;
- existing technical evidence must be preserved without fabricating requester-review success.

## Persistence location and permissions

Define one bounded runtime path for future review-result artifact storage under the existing live-child state boundary where practical.

Require:
- narrow write scope;
- file mode 0600;
- no credential values/Authorization/environment material;
- exact artifact naming/attempt correlation;
- deterministic readback by requester-review code without provider access.

Do not deploy the integration candidate in this task.

## Deterministic integration tests

Using replay/synthetic fixtures only, prove at minimum:
- one-shot success path produces exact schema v2 review artifact;
- terminal PASS occurs only after successful durable persistence + strict readback;
- later requester review reads the artifact with provider_calls delta=0;
- exact attempt/request/task/writer/provider/model/plan/authority correlation survives integration;
- all v2 tamper protections remain effective;
- secret/privacy exclusions remain effective;
- persistence failure after simulated transport keeps one-shot consumed;
- no retry/fallback;
- no project acceptance/state mutation.

## Historical boundary

Historical R03 remains:
- technical correlation PASS;
- requester review BLOCKED;
- project_acceptance NOT_GRANTED;
- missing provider body not reconstructed.

Do not use this integration work to reinterpret historical R03.

## Forbidden

- any live OpenAI/provider call;
- credential read/use/create;
- production deployment;
- canonical secretref mutation;
- billing/account mutation;
- project acceptance;
- project-state mutation;
- new provider-call authority.

## Expected terminal result

Return exactly one:

`PASS_KOD_BOOSTER_RESULT_V2_INTEGRATION_READY_FOR_SIS_VERIFY`

or

`BLOCKED_KOD_BOOSTER_RESULT_V2_INTEGRATION: <exact blocker>`

or exact FAIL.

Terminal result must include:
- immutable integration candidate locator/identity;
- exact reused component identities;
- exact future runtime flow from claim → transport → normalize → persist → strict readback → terminal;
- deterministic integration test results;
- provider calls=0;
- credential accesses=0;
- production deployment=0;
- historical R03 remains BLOCKED/NOT_GRANTED;
- next verifier=SIS.

Address result to KOO and SIS.
Stop after terminal result.