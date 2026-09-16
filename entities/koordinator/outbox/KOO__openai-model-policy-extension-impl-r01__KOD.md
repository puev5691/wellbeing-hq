# KOO → KOD: OpenAI three-model D0 policy extension implementation r0.1

status: `READY_FOR_KOD_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Purpose
Implement the exact bounded Luna/Terra/Sol D0 policy/adapter/runtime extension defined by accepted SIS preflight.

## Accepted basis
SIS preflight:
`entities/sisadmin/outbox/SIS__openai-model-policy-extension-preflight-r01__KOO.md`
commit `f495889bd0be11000cbd408be2d05e8cd066cbb8`
verdict `PASS_SIS_OPENAI_MODEL_POLICY_EXTENSION_PREFLIGHT_R01`.

Authoritative benchmark B:
commit `aa36f7a99105d367b6b2cc5038952c428301c7a0`.

Accepted runtime integration:
commit `b212eda0151a5ee07fed8f5cef4299e2b7e3a73f`.

Accepted SIS secret gate:
commit `3c282b2d67a699520ccbf7a751616c3e2ee58d5a`.

## Required bounded changes
1. `policy.py`: immutable allowlist exactly `gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-5.6-sol`; explicit model input; unknown model fail-closed.
2. `openai_adapter.py`: request/response/provenance use exact selected model; no substitution/fallback.
3. runtime integration successor: capabilities exactly three models; sentinel fixture uses request model; selected model propagates unchanged through policy → adapter → response → telemetry.
4. tests: three positive dry-runs; unknown model rejection before transport; response-model mismatch checks; no-fallback assertion; preserve privacy/tool boundaries and zero provider calls.

Do not redesign benchmark harness.
Preserve existing live switch/secret gate.
No provider entitlement claim.

## FAST_PATH
Target <=12 tool calls, <=8 GitHub reads, one initial preflight, one short prewrite reconciliation. Stop after sufficient terminal evidence.

## Hard boundaries
No live provider calls. No API keys. No billing changes. No production deploy. No project/private external send. No TERA2/WBN.

## Expected terminal
`PASS_OPENAI_THREE_MODEL_D0_EXTENSION_R01_READY_FOR_SIS_VERIFY`
or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.
