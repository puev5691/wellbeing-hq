# KOO → SIS: OpenAI live D0 final gate preflight r0.1

status: `TASK_READY`
execution_mode: `FAST_PATH`
recommended_reasoning: `MEDIUM`

## Цель

После независимого PASS трехмодельного OpenAI D0 extension выполнить один bounded final-gate preflight перед будущим первым live D0 request.

## Accepted basis

SIS independent verify:
`entities/sisadmin/outbox/SIS__openai-three-model-d0-extension-verify-r01__KOO.md`
commit `3a8a03ef74a9fbf48bc6e4f380beb12006942dd4`
verdict `PASS_SIS_OPENAI_THREE_MODEL_D0_EXTENSION_VERIFY_R01`.

Runtime-secret gate:
`entities/sisadmin/outbox/SIS__openai-d0-runtime-secret-gate-r01__KOO.md`
commit `3c282b2d67a699520ccbf7a751616c3e2ee58d5a`.

Runtime integration:
`b212eda0151a5ee07fed8f5cef4299e2b7e3a73f`.

Account/billing runbook:
`entities/redaktor/outbox/RED__openai-account-billing-activation-runbook-r01__KOO.md`
commit `b9a9a375590e1e089b3c67333432254eaa1fcb88`.

## Required

1. Fresh HQ preflight and current SIS writer check.
2. Reconfirm exact runtime path `/home/pev5691/openai-d0-runtime-r01` and existing live switch contract `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE` without repeating host inventory.
3. Confirm no secret/key is stored in repo/runtime files/logs and existing hidden `/dev/tty` injection path remains the only accepted key input path.
4. Reconcile the three-model extension with the existing live runtime boundary and identify the exact remaining dependencies that cannot be satisfied without OPERATOR/account action.
5. Produce a minimal OPERATOR checklist for one bounded synthetic live D0 request, including exact commands but excluding any secret value.
6. Distinguish verified technical readiness from unverified account/billing/model entitlement.
7. Do not perform any provider call.

## Boundaries

NO live provider calls.
NO API key reads or writes.
NO billing/account mutation.
NO sudo/root.
NO production deployment.
NO private/project external send.
NO TERA2/WBN.

## Terminal

`PASS_SIS_OPENAI_LIVE_D0_FINAL_GATE_PREFLIGHT_R01`
or exact `BLOCKED_* / FAIL_*`.

Return result to KOO through Exchange Gate.
