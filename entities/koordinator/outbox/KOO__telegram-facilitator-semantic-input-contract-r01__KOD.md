# KOO → KOD: Telegram facilitator semantic input contract r0.1

status: TASK
execution_mode: FAST_PATH

## Basis

Facilitator core independent PASS:
`947ea4b76d367774fbc2ae37b61d49e0e89d55bc`

Aggregate bridge independent PASS:
`c0ed7057da344bf6b10b0718960c36962b8d9536`

## Problem

Current Phase1B safe_receipt is aggregate-only. It cannot support semantic facilitation of real discussions because it intentionally contains no raw discussion content.

## Goal

Design and implement an isolated semantic-input contract/library that can receive explicitly admitted, minimized discussion excerpts/claims from a future upstream privacy gate and convert them into facilitator-core NormalizedEvent objects.

This task does NOT change Phase1B runtime and does NOT ingest real Telegram data.

Required:
- explicit SemanticInput object/schema;
- content class / purpose / scope / source refs;
- minimized text/excerpt or structured claim field with strict size bounds;
- optional pseudonymous participant reference that is not a Telegram user_id/username;
- privacy class + retention class + expiry;
- exact authority/admission proof binding;
- topic/problem/goal/position/etc remain declared semantic categories supplied or derived only under explicit analysis policy;
- provenance links from semantic object to admitted source;
- fail closed on raw Telegram update, undeclared identity, missing authority, unsupported privacy class;
- synthetic fixtures for discussion threads;
- tests showing facilitator can produce candidate_question/candidate_task from semantic inputs while candidate_task remains non-executable;
- no persistent raw storage requirement.

Do not:
- modify Phase1B;
- call Telegram API;
- call LLM/provider;
- create credentials;
- deploy DB/systemd/runtime;
- authorize publication/dispatch;
- make candidate tasks executable.

Expected:
`PASS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker/fail.

Return immutable candidate + tests + privacy/authority boundary to KOO through Exchange Gate.
