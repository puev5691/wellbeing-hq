# KOO → OPERATOR: fresh one-shot OpenAI Entity-booster D0 live decision r0.3

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Fresh verified basis

SIS terminal:
`PASS_SIS_OPENAI_BOOSTER_LIVE_CHILD_PATH_R01_READY`

Verified live-child path exists on `ruvds-xnqc6` and is invokable by the normal KOD-triggered boundary without manual elevation.

Credential value reads/exposure = 0.
Provider calls = 0.
Durable live claim = 0.

## Exact immutable task to authorize

path:
`entities/koordinator/outbox/KOO__openai-booster-d0-live-r01__KOD.md`

commit:
`b988066e0e018627cc24b95f409f3ccd0a416990`

blob:
`691af722274bc51f87d5eeda6e7054d21ee3c9c3`

## Exact requester/current-writer binding

entity: `KOD`
current_writer_path: `entities/koder/current/KOD__replacement-current-writer-v04.md`
current_writer_blob: `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

## Exact execution scope

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

## Exact canonical credential reference

`secretref:openai:wellbeing-entity-boosters-restricted`

Live-child mechanism must remain the exact SIS-verified `LoadCredentialEncrypted` path.
No legacy TTY fallback is authorized.

## Fresh one-shot validity

This is a new authority, separate from R01 and R02.

Validity:
- one manual activation session only;
- runtime expiry = local monotonic activation-start + 600 seconds;
- authority expires on first durable one-shot claim, mismatch, revoke, supersession, or expiry;
- no retry or second claim after any claimed or uncertain attempt.

## Security caveat

The systemd host credential key is not located on encrypted media.
This does not invalidate the current binding/live-child PASS.
It must not be interpreted as protection against full-disk or host-key compromise.

## Decision requested

Authorize exactly one execution of the immutable task above under a fresh R03 authority.

Decision token:

`AUTHORIZE_OPENAI_ENTITY_BOOSTER_D0_LIVE_R03`

## If approved

KOO will:
1. record the fresh R03 authority;
2. re-read the exact task/current writer/live-child state;
3. create a fresh dispatch/inbox binding for KOD;
4. generate the exact manual activation PROMPT containing the new decision commit;
5. permit exactly one bounded provider call if every pretransport gate still matches.

## Not authorized

- second call;
- retry;
- provider/model fallback;
- Anthropic or another provider;
- other payload/model/tools;
- credential disclosure;
- production deployment;
- project acceptance;
- project-state mutation.

---
КТО: KOO / КООРДИНАТОР
СТАТУС: OPERATOR_DECISION_REQUIRED