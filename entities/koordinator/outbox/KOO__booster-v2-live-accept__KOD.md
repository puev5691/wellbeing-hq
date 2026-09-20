# KOO → KOD: one-shot booster v2 live acceptance r0.1

status: TASK
execution_mode: ONE_SHOT_LIVE_D0_ACCEPTANCE
project_time: omitted; trusted project-time source not used

## Resume-First

Start with fresh GitHub preflight of `puev5691/wellbeing-hq`.
Verify current KOD writer/recovery boundary before execution.

## Exact OPERATOR authority

`AUTHORIZE_BOOSTER_V2_LIVE_ACCEPTANCE_R01`

decision record:
`entities/koordinator/current/KOO__booster-v2-live-accept-decision.md`

decision commit:
`97d336650fea5ab4e709e40e0d75d057a32554bc`

## Exact requester/current-writer binding

requester_entity: `KOD`
requester_current_writer_path: `entities/koder/current/KOD__replacement-current-writer-v04.md`
requester_current_writer_blob: `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

## Exact installed runtime basis

SIS host readiness:
`PASS_SIS_BOOSTER_V2_HOST_INSTALL_READINESS_R01`

commit:
`9a9c568879743ca1f1fd7947cb25c0f71a72c265`

Installed unit:
`wellbeing-openai-booster-result-v2.service`

Installed runtime:
`/opt/wellbeing/openai-booster-result-v2-integration-r01`

Review-result directory:
`/var/lib/wellbeing/openai-booster-live-child-r01/review-results`

Canonical secretref:
`secretref:openai:wellbeing-entity-boosters-restricted`

## Exact live scope

provider: `openai`
endpoint: `https://api.openai.com/v1/responses`
model: `gpt-5.6-luna`
data_class: `D0_SYNTHETIC`
privacy_class: `synthetic_only`
payload: `Synthetic bounded request.`
tools: none
calls: 1
automatic_retries: 0
fallback: none
max_output_tokens: 64
max_response_bytes: 16384
timeout_seconds: 30
store: false
use_once: true
requester_review_required: true
project_acceptance: `NOT_GRANTED`
project_state_mutation: false

## Required execution flow

`claim → transport → normalize → persist schema v2 → strict readback → terminal`

Technical PASS is forbidden until:
1. durable one-shot claim succeeds;
2. exact provider transport completes;
3. response validates and normalizes to `wb.openai.booster.review_result.v2`;
4. review-result artifact is durably persisted;
5. strict v2 readback validates exact attempt/request/task/writer/plan/authority/provider/model identities and cross-field evidence.

## Fresh authority validity

One manual activation session only.
Expiry = local monotonic activation-start + 600 seconds.
Authority expires on first durable claim, mismatch, revoke, supersession or expiry.
No retry or second claim after any claimed or uncertain attempt.

Historical R01/R02/R03 authorities are not reusable.

## Pretransport gates

Before provider transport verify:
- exact R01 acceptance authority identity;
- current KOD writer matches bound writer blob;
- installed runtime/unit identities still match SIS host-readiness PASS;
- unit remains disabled before manual start;
- exact canonical secretref mapping unchanged;
- exact provider/model/privacy/tools/bounds unchanged;
- review-result directory boundary unchanged;
- retries=0;
- fallback=none;
- no legacy TTY injection.

Any mismatch -> BLOCK before provider transport.

## Result requirements

Terminal result must state:
- provider/model actually used;
- provider call count;
- HTTP status if received;
- durable claim state;
- retries/fallback;
- exact review-result artifact locator/attempt identity;
- schema v2 persistence status;
- strict readback status;
- requester review status = REQUIRED / PENDING;
- project_acceptance remains NOT_GRANTED;
- project_state_mutation=false;
- unit enabled state remains disabled;
- security caveat preserved.

Do not invent usage/cost/latency if not actually captured.

## Failure semantics

If transport occurs but normalize/persist/readback fails:
- one-shot remains consumed;
- terminal is BLOCKED/FAIL, never PASS;
- no retry;
- no second provider call;
- no replay to reconstruct missing content.

## Forbidden

- second provider call;
- retry;
- fallback;
- another provider/model;
- credential disclosure;
- legacy TTY injection;
- enabling/autostarting unit;
- production acceptance;
- project acceptance;
- project-state mutation.

## Security caveat

The systemd host credential key remains not located on encrypted media.
No full-disk/host-key compromise protection is claimed.

## Expected terminal result

Return exactly one:

`PASS_KOD_BOOSTER_V2_LIVE_ACCEPTANCE_R01`

or

`BLOCKED_KOD_BOOSTER_V2_LIVE_ACCEPTANCE_R01: <exact blocker>`

or exact FAIL.

Address terminal result to KOO.
Stop after terminal result.