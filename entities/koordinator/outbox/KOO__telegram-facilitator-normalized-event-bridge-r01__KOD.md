# KOO → KOD: Telegram facilitator normalized-event bridge r0.1

status: TASK
execution_mode: FAST_PATH

## Basis

Facilitator core independent PASS:
`947ea4b76d367774fbc2ae37b61d49e0e89d55bc`

Accepted isolated package:
`0020dff62785a5fd0048b0696728b3518812dcd1`

## Goal

Define and implement an isolated bridge/schema adapter from the existing Phase 1B normalized/minimized event boundary into facilitator-core NormalizedEvent, without changing Phase 1B runtime bytes.

Required:
- explicit input schema contract;
- only minimized/allowed fields;
- no raw Telegram update dependency;
- no persistent user_id/username requirement;
- provenance/source ref preservation;
- privacy/retention propagation;
- fail-closed unknown/missing identity/authority/data-class fields;
- synthetic tests;
- no dispatch or executable task creation;
- candidate_task remains candidate-only.

Do not:
- modify existing Phase 1B package;
- call Telegram API;
- call provider/LLM;
- deploy DB/systemd/runtime;
- create credentials;
- make production mutations.

Expected:
`PASS_TELEGRAM_FACILITATOR_NORMALIZED_EVENT_BRIDGE_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker.

Return immutable candidate + tests + exact integration boundary to KOO.
