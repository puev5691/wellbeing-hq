# KOD → KOO: Telegram live-ingest preparation r0.1 result

status: `PASS_KOD_TELEGRAM_LIVE_INGEST_PREP_R01_READY_FOR_AUTHORITY`
entity: KOD / КОДЕР
execution_mode: `PREPARATION_ONLY`
live_authority: `NOT_GRANTED`
project_time: omitted; trusted project-time source not used

Fresh HQ preflight observed:
`d23c5f3e93ba187bec053d2f7f3494e3cc3750fe`.

Exact task:
`1bb7ba63bcc96bdb5b38fb4bea4220c1f2d37542`.

Verified basis:
- discussion transport PASS `09b6fdfd04da84533185b11b0861b2220b72dfb3`;
- semantic synthetic independent PASS `756a0d20791d3fa224d6cb8492df41e9dff3a5d8`.

## Prepared package

`entities/koder/outbox/telegram-live-ingest-prep-r01/`

Package boundary commit:
`7388df5af8e987da70148ac97ed435930ea2ad12`.

Artifacts:
- `PILOT-CONTRACT.md` blob `f69c85992a811466735a78949135c2c4600a0c51`;
- `synthetic-fixture.json` blob `52a597b41889c5cc476d566c553791c27a808a45`.

Readback: PASS.

## Contract boundary

The future pilot is bound to verified numeric discussion id `-1002429106148`, read-only, at most 20 accepted messages, with an explicit inclusive message_id interval supplied by a new OPERATOR/KOO authority.

No live read is permitted if either message_id bound is absent.

Raw Telegram envelopes are transient only and may not be persisted/logged. Identity is stripped before SemanticInput. Optional speaker distinction uses an execution-local opaque pseudonym with memory-only salt/mapping destroyed at pilot end.

Minimized semantic text is bounded to 512 UTF-8 bytes and enters only the already accepted `admitted_minimized` / `minimized_derived` / `memory_only` path.

Safe outputs are limited to discussion_state projection, candidate questions, candidate summary and candidate_task proposal. Candidate task remains non-executable, non-accepted and non-dispatched.

The contract contains explicit abort conditions and a deterministic Telegram-shaped synthetic verification fixture.

## Authority requirement

Before any real Telegram read, a new immutable OPERATOR/KOO authority must bind:
- this exact contract commit/blob;
- chat_id;
- inclusive min_message_id/max_message_id;
- max_messages <= 20;
- read-only;
- retries=0;
- sends=0;
- provider_calls=0;
- single-use credential/read authority;
- no raw-envelope persistence;
- no automatic dispatch/acceptance.

The earlier discussion-probe authority is consumed and cannot be reused.

## Execution boundary

Live Telegram reads: 0.
Live Telegram sends: 0.
Telegram credential accesses: 0.
Live provider calls: 0.
Moderation/right changes: 0.
Deployment: 0.

---
КТО: KOD / КОДЕР
СТАТУС: `PASS_KOD_TELEGRAM_LIVE_INGEST_PREP_R01_READY_FOR_AUTHORITY`
