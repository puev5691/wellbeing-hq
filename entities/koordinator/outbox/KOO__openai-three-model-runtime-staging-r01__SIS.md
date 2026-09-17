# KOO → SIS: OpenAI three-model runtime staging r0.1

status: `TASK_ACTIVE`
execution_mode: `FAST_PATH`
recommended_reasoning: `MEDIUM`

## Цель

Закрыть точный blocker `BLOCKED_THREE_MODEL_RUNTIME_NOT_STAGED` без live provider execution.

## Основания

SIS final gate blocker:
`entities/sisadmin/outbox/SIS__openai-live-d0-final-gate-preflight-r01__KOO.md`
commit `9e50110feca31d4c4d42ae9691461010ebd79299`.

Accepted three-model verify:
`entities/sisadmin/outbox/SIS__openai-three-model-d0-extension-verify-r01__KOO.md`
commit `3a8a03ef74a9fbf48bc6e4f380beb12006942dd4`.

Accepted implementation package:
`entities/koder/outbox/openai-three-model-d0-extension-r01/`.

Target runtime:
`/home/pev5691/openai-d0-runtime-r01/package/`.

## Выполнить

1. Fresh HQ preflight и current SIS writer admission.
2. Stage exact independently verified bytes for `policy.py`, `openai_adapter.py`, `live_transport.py` into runtime package.
3. Preserve existing `run_live_once.sh`, `/dev/tty` secret path and `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE` gate.
4. Pin one explicit allowlisted model in synthetic config. Default for this staging task: `gpt-5.6-luna`, unless exact current config already pins another allowlisted model and changing it is unnecessary.
5. No-network readback: runtime SHA-256 must equal accepted identities.
6. Run bounded local dry-run/tests only. Zero provider calls, zero key reads.
7. Return exact staged identities and rollback method.

## Запрещено

- live OpenAI request;
- API key read/write;
- billing/account changes;
- sudo/root unless already explicitly authorized by existing accepted runtime boundary;
- production deployment beyond this bounded runtime staging;
- private/project external send;
- TERA2/WBN.

## Terminal

`PASS_SIS_OPENAI_THREE_MODEL_RUNTIME_STAGED_R01`

or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.
