# KOO → OPERATOR: booster v2 one-shot live capability acceptance gate r0.1

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Fresh verified basis

SIS host-readiness terminal:
`PASS_SIS_BOOSTER_V2_HOST_INSTALL_READINESS_R01`

commit:
`9a9c568879743ca1f1fd7947cb25c0f71a72c265`

Installed runtime/unit identities match the independently verified immutable integration candidate.

Host state:
- unit loaded;
- unit disabled;
- unit inactive;
- ordinary KOD-triggered sentinel invocation PASS;
- provider calls = 0;
- credential value reads/exposure = 0;
- prior invocation and ledger restored unchanged.

## Purpose of next step

Perform exactly one fresh bounded live acceptance call through the installed booster-v2 runtime to validate the complete future path:

`claim → transport → normalize → persist schema v2 → strict readback → terminal`

and then make the persisted review-result available for a separate requester-review step without any repeat provider call.

## Proposed exact live scope

requester_entity: `KOD`
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

## Exact installed capability to use

Installed unit:
`wellbeing-openai-booster-result-v2.service`

Canonical credential reference:
`secretref:openai:wellbeing-entity-boosters-restricted`

Credential mechanism:
`systemd LoadCredentialEncrypted`

Review-result schema:
`wb.openai.booster.review_result.v2`

Review-result directory:
`/var/lib/wellbeing/openai-booster-live-child-r01/review-results`

## Fresh authority semantics

This must be a new authority, independent of historical R01/R02/R03.

Historical R03:
- consumed;
- non-reusable;
- requester review remains BLOCKED;
- project_acceptance remains NOT_GRANTED.

Fresh acceptance authority must:
- apply to one manual activation session only;
- expire at local monotonic activation-start + 600 seconds;
- expire immediately on first durable claim, mismatch, revoke, supersession or timeout;
- forbid retry/second claim after claimed or uncertain attempt.

## Acceptance evidence required from the single call

Future KOD terminal must prove:
- exact provider/model/scope match;
- provider call count = 1;
- retries = 0;
- fallback = none;
- durable claim consumed;
- exact schema-v2 review artifact persisted;
- strict readback PASS;
- terminal technical PASS occurs only after persistence/readback;
- requester review remains REQUIRED / PENDING until separately performed;
- project_acceptance remains NOT_GRANTED;
- no project-state mutation.

## Explicitly forbidden

- second provider call;
- retry;
- provider/model fallback;
- Anthropic or another provider;
- credential disclosure;
- legacy TTY injection;
- unit enablement/autostart;
- production acceptance;
- project acceptance;
- project-state mutation.

## Security caveat

The systemd host credential key remains not located on encrypted media.
No full-disk or host-key compromise protection is claimed.

## Decision requested

`AUTHORIZE_BOOSTER_V2_LIVE_ACCEPTANCE_R01`

Approval authorizes only the one bounded call above.
After a successful technical terminal, requester review and any project-level acceptance remain separate subsequent gates.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED