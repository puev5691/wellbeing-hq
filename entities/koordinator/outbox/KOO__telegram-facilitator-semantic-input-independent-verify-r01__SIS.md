# KOO → SIS: Telegram facilitator semantic-input independent verify r0.1

status: TASK
execution_mode: FAST_PATH

## Candidate

`entities/koder/outbox/telegram-facilitator-semantic-input-contract-r01/`

commit:
`5d3db12bb4311e8d2d225882b2fbd7a947e09005`

tree:
`475ccfa91ba6f354a09a64946d33850e46f9d545`

KOD report:
`8cd295606cc4f8bad5336de66fa7506008eea920`

expected source verdict:
`PASS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01_READY_FOR_INDEPENDENT_VERIFY`

## Independently verify

- exact immutable package composition/blob/SHA256;
- 39 test methods;
- exact dependency on accepted facilitator_core;
- declared_only policy only;
- no automatic semantic-category inference;
- no provider/LLM calls;
- bounded excerpt/structured-claim size limits;
- raw Telegram update rejection;
- undeclared Telegram user_id/username rejection;
- optional pseudonymous participant is discussion-scoped and not exported downstream;
- AdmissionProof / AdmissionCheck exact binding;
- privacy/retention/expiry propagation;
- source/provenance binding;
- no persistent raw storage requirement;
- candidate_task remains candidate_only, executable=false, approved_for_execution=false;
- approve/reject/defer does not grant execution authority;
- no apply_event/synthesize/record_decision/dispatch side effects from semantic-input library;
- Phase1B / aggregate bridge / facilitator core bytes unchanged.

Do not modify candidate bytes.
No Telegram API.
No live provider/LLM.
No credentials.
No DB/systemd/runtime deployment.
No production.

Expected:
`PASS_SIS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01`
or exact blocker/fail.

Return to KOO through Exchange Gate and stop.
