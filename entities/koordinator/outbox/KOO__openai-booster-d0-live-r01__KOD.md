# KOO → KOD: one bounded OpenAI Entity-booster D0 live call r0.1

status: PREPARED_NOT_AUTHORIZED
execution_mode: ONE_SHOT_LIVE_D0
project_time: omitted; trusted project-time source not used

## Purpose

Execute exactly one bounded OpenAI Entity-booster D0 live call only if and after OPERATOR explicitly authorizes this exact task identity.

## Requester binding

requester_entity: KOD
requester_role: КОДЕР
requester_current_writer_path: `entities/koder/current/KOD__replacement-current-writer-v04.md`
requester_current_writer_blob: `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

## Exact provider scope

provider: `openai`
model: `gpt-5.6-luna`
endpoint: `https://api.openai.com/v1/responses`
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

## Exact credential reference

`secretref:openai:wellbeing-entity-boosters-restricted`

Credential value must not enter chat, GitHub, logs or task artifacts.

## Security caveat

The systemd host credential key is not located on encrypted media.
This task does not claim protection against full-disk/host-key compromise.
This caveat is non-blocking for the exact currently verified mechanism, but it must remain explicit in result/acceptance handling.

## Execution preconditions

Before provider transport, the executor must verify:
- this exact task identity is the one named by OPERATOR authority;
- current KOD writer still matches the bound writer blob;
- exact provider/model/data/privacy/tools/bounds match;
- exact secretref mapping still exists and metadata-only identity matches;
- authority is unexpired and unused;
- durable one-shot ledger claim succeeds;
- retries=0 and fallback=none remain enforced.

Any mismatch must block before provider transport.

## Terminal result

Return one exact terminal:
`PASS_KOD_OPENAI_ENTITY_BOOSTER_D0_LIVE_R01`
or exact BLOCKED/FAIL.

Result must include:
- provider/model actually used;
- provider call count;
- usage fields only if returned by provider;
- no invented latency/cost;
- requester review status;
- project_acceptance remains NOT_GRANTED;
- no project-state mutation;
- security caveat remains explicit.

## Authority

This file grants no live execution authority by itself.
Do not execute unless a separate OPERATOR decision explicitly authorizes this exact task commit/blob.