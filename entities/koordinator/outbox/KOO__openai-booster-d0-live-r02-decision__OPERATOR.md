# KOO → OPERATOR: fresh one-shot OpenAI Entity-booster D0 live decision r0.2

status: OPERATOR_DECISION_REQUIRED
project_time: omitted; trusted project-time source not used

## Fresh verified basis

SIS terminal:
`PASS_SIS_OPENAI_CANONICAL_SECRETREF_RESOLVER_PATH_R01_READY`

Resolver mechanism:
`systemd LoadCredentialEncrypted` + exact oneshot resolver service + narrow normal-user start permission.

KOD can invoke the bounded resolver path without manual elevated intervention.
Credential value reads/exposure = 0.
Provider calls = 0.

## Exact task to authorize

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

## Exact canonical reference

`secretref:openai:wellbeing-entity-boosters-restricted`

Resolver path must remain the exact SIS-verified canonical systemd path.
No fallback to legacy TTY injection is authorized.

## One-shot expiry

This is a fresh authority, separate from the expired previous activation session.

Validity:
- one manual activation session only;
- runtime expiry = local monotonic activation-start + 600 seconds;
- expires immediately on first durable one-shot claim, mismatch, revoke, supersession, or expiry;
- no retry or second claim after a claimed/uncertain attempt.

## Security caveat

The systemd host credential key is not on encrypted media.
This does not invalidate the current verified resolver/binding PASS.
It must not be interpreted as protection against full-disk or host-key compromise.

## Decision requested

Authorize exactly one execution of the immutable task above under this fresh authority.

Decision token:

`AUTHORIZE_OPENAI_ENTITY_BOOSTER_D0_LIVE_R02`

## If approved

KOO will record the fresh authority, re-read the exact task/current writer/resolver state, address the existing immutable task to KOD, and provide the manual activation PROMPT.

## Not authorized by this gate

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