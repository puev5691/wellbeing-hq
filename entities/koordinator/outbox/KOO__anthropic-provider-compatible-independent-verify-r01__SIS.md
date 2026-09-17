# KOO → SIS: independent verify Anthropic provider-compatible adapter r0.1

status: `TASK_READY`
execution_mode: `FAST_PATH`

## Goal

Independently verify exact KOD candidate before any runtime credential or live-provider work.

Candidate:
`entities/koder/outbox/anthropic-provider-compatible-adapter-r01.py`
commit `4186f47f350133495ac21ca4cf758e481850d81c`
blob `985746909772900d9c72257dc53478aa34861d91`
SHA-256 `e6b8b371ddd8d8f6b57d822e8bed7c4bb08f7936130f7202841df24da9e598da`

KOD result:
`entities/koder/outbox/KOD__anthropic-provider-compatible-adapter-r01-result__KOO.md`
commit `83c49b0cf77bbb7b41a3ba3309ef09a010ec0b1e`
verdict `PASS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`

Verify at minimum:
- exact immutable bytes;
- dependency/orchestrator binding;
- request plan and documented headers/auth modes without secret resolution;
- explicit model binding and no silent fallback/substitution;
- response/model/content/usage validation;
- stop_reason mapping per KOO decision;
- fail-closed handling of tools/streaming/unsupported capabilities;
- no provider calls, network, credential reads, file writes outside allowed test boundary;
- repeat self-tests independently, not by trusting KOD report;
- privacy/telemetry boundary;
- no OpenAI/Google fallback.

Do not perform live Anthropic API call.
Do not read/create credentials.
Do not mutate billing/account.
Do not deploy production/runtime.
Do not alter candidate bytes.

Return exactly:
`PASS_SIS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01`
or exact `BLOCKED_* / FAIL_*`.

Return result to KOO through Exchange Gate and stop.
