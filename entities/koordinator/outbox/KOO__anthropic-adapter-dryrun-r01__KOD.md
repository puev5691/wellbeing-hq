# KOO → KOD: Anthropic adapter dry-run r0.1

status: `TASK_ACTIVE`
execution_mode: `FAST_PATH`
recommended_reasoning: `MEDIUM`
production: `no`
live_provider_calls: `no`

## Цель

Подготовить bounded provider adapter для Anthropic в существующем multi-model orchestrator contour, без live API вызовов и без credentials.

## Основания

Использовать как архитектурные зависимости:
- `entities/koder/outbox/orchestrator-runtime-integration-r01.py` commit `b212eda0151a5ee07fed8f5cef4299e2b7e3a73f`;
- `entities/koder/outbox/openai-three-model-d0-extension-r01/` как пример fail-closed provider boundary, но не копировать OpenAI-specific semantics;
- `entities/redaktor/outbox/RED__anthropic-account-billing-activation-runbook-r01__KOO.md` commit `68fd91d7876564a6e00fb0b2461a1e512839cf2d` только для account/secret boundary, не как API implementation source.

## Требуется

1. Определить минимальный Anthropic adapter contract для synthetic dry-run.
2. Сохранить provider-neutral RequestEnvelope/ResponseEnvelope и lifecycle orchestrator.
3. Explicit model selection, без model substitution и silent fallback.
4. Tools/network/private-data deny-by-default до отдельного authority.
5. Secret reference only, без ключей в repo/files/logs/telemetry.
6. Dry-run sentinel transport без внешней сети.
7. Unknown/unsupported model или capability → fail before transport.
8. Telemetry должна различать provider/model/reasoning/tool boundary и не содержать secret material.
9. Минимальные self-tests.
10. Вернуть immutable candidate + terminal report для независимой проверки.

## Границы

Не выполнять:
- live Anthropic calls;
- account creation или billing;
- API-key handling;
- production deployment;
- project/private external send;
- fallback на OpenAI или Google;
- TERA2/WBN.

## FAST_PATH

Target <=12 tool calls.
Target <=8 GitHub/source reads.
One initial preflight.
One short prewrite reconciliation.
Stop when terminal evidence is sufficient.

## Terminal

`PASS_ANTHROPIC_ADAPTER_DRYRUN_R01_READY_FOR_REVIEW`

или exact `BLOCKED_* / FAIL_*`.

Вернуть KOO через Exchange Gate.
