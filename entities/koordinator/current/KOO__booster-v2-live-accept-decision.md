# OPERATOR decision — booster v2 one-shot live acceptance r0.1

status: OPERATOR_DECISION_RECORDED
decision: AUTHORIZE_BOOSTER_V2_LIVE_ACCEPTANCE_R01
project_time: omitted; trusted project-time source not used

## Exact basis

SIS host readiness:
`PASS_SIS_BOOSTER_V2_HOST_INSTALL_READINESS_R01`

commit:
`9a9c568879743ca1f1fd7947cb25c0f71a72c265`

Installed unit:
`wellbeing-openai-booster-result-v2.service`

Installed runtime:
`/opt/wellbeing/openai-booster-result-v2-integration-r01`

Canonical reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

## Exact live scope

requester_entity: KOD
provider: openai
endpoint: https://api.openai.com/v1/responses
model: gpt-5.6-luna
data_class: D0_SYNTHETIC
privacy_class: synthetic_only
payload: Synthetic bounded request.
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
project_acceptance: NOT_GRANTED
project_state_mutation: false

## Fresh authority semantics

This authority is independent of historical R01/R02/R03.
It is valid for one manual activation session only.
Runtime expiry = local monotonic activation-start + 600 seconds.
It expires on first durable claim, mismatch, revoke, supersession or expiry.
No retry or second claim after any claimed or uncertain attempt.

## Required future flow

`claim → transport → normalize → persist schema v2 → strict readback → terminal`

Technical PASS is forbidden before durable persistence and strict readback.

## Forbidden

- second provider call;
- retry;
- fallback;
- another provider/model;
- credential disclosure;
- legacy TTY injection;
- unit enablement/autostart;
- production acceptance;
- project acceptance;
- project-state mutation.

## Security caveat

The systemd host credential key remains not located on encrypted media.
No full-disk/host-key compromise protection is claimed.