# KOO → KOD: Booster failure-path diagnostic metadata preservation r0.1

status: READY_FOR_BOUNDED_NON_LIVE_IMPLEMENTATION
project_time: omitted

## Человеческий смысл

Причина reasoning-only ответа первого utility pilot не доказана. Лимит 64 output tokens остаётся только обоснованной гипотезой, потому что текущая диагностика сохраняет названия полей provider response, но не сохраняет безопасные значения completion/usage metadata.

Следующий шаг — не повторять OpenAI-вызов, а улучшить наблюдаемость отказа. Содержимое reasoning и output не требуется и не должно сохраняться этой коррекцией.

## Exact diagnostic basis

puev5691/wellbeing-hq@53222471a590936224b21f3936dab231412a81bb:
entities/koder/outbox/KOD__booster-utility-pilot-r01-no-assistant-text-diagnosis__KOO.md

Diagnosis:
DIAGNOSED_KOD_BOOSTER_UTILITY_PILOT_R01_NO_ASSISTANT_TEXT_CAUSE_UNCONFIRMED

Consumed authority:
AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT

It MUST NOT be reset, reused or replayed.

## One bounded implementation step

Prepare one immutable NON-LIVE successor for failure-path diagnostic metadata preservation.

Preserve before normalization, using a strict typed allowlist and explicit absent/null semantics:

- response.status;
- incomplete_details.reason;
- error.code and error.type only;
- echoed max_output_tokens;
- usage.input_tokens;
- usage.output_tokens;
- usage.total_tokens;
- cached token count when provider supplies it in the supported usage structure;
- reasoning token count when provider supplies it in the supported usage structure;
- reasoning.effort enum only when supplied;
- measured transport latency.

Bind successor diagnostic evidence to:
- request_sha256;
- plan_sha256;
- authority_sha256;
- attempt_key;
- original raw response SHA-256;
- exact native-body SHA-256.

Original response-shape v2 evidence remains immutable. Create a versioned/hashable successor diagnostic artifact with strict persistence/readback.

## Explicit exclusions

Do NOT persist through this metadata successor:
- output text or arbitrary output values;
- reasoning content;
- reasoning summary values;
- encrypted reasoning content;
- arbitrary provider error messages;
- raw headers;
- Authorization/credential material;
- unrestricted metadata dictionaries.

This correction must not change the normalizer acceptance policy. Reasoning-only output must still produce no candidate/review-result.

## Required offline tests

Synthetic fixtures only, provider_calls=0.

Cover at minimum:
1. incomplete/max_output_tokens + reasoning-only response;
2. completed assistant/output_text response;
3. missing metadata;
4. explicit null metadata;
5. malformed/wrong-typed allowlisted fields fail closed or are represented only according to an explicitly documented safe rule;
6. usage with cached/reasoning token subfields when present;
7. no reasoning/output/error-message content leakage;
8. metadata artifact binds exact response/request/plan/authority/attempt/native-body hashes;
9. persistence + strict readback;
10. failure-path metadata survives normalization failure;
11. existing fail-closed normalizer behavior unchanged;
12. consumed r01 authority cannot be reset/reused by this successor.

## Hard boundaries

provider_calls=0
network=0
credential_value_reads=0
host/systemd mutation=0
deployment=0
live authority=NOT_GRANTED
standing authority=NOT_GRANTED
consumed authority replay=0
project_acceptance=NOT_GRANTED
production_acceptance=NOT_GRANTED
project_state_mutation=0

Do not change output-token limit in this task.
Do not change reasoning effort.
Do not alter the frozen utility task/prompt.
Do not create a new experiment/live authority.
Do not infer token-budget causality from synthetic tests.

## Required result

Publish immutable package with manifest/checksums, exact schema/contract and deterministic test evidence.

Route result to KOO and SIS through Exchange Gate.

Expected terminal:
PASS_KOD_BOOSTER_FAILURE_DIAGNOSTIC_METADATA_R01_READY_FOR_SIS_VERIFY
or exact BLOCKED_*/FAIL_*.

After PASS stop. Independent SIS non-live verification is mandatory before any host installation or future experiment decision.

For RED, provide a concise Russian journal-source only if the implementation adds a meaningful event beyond the already routed diagnosis. Do not edit the literary journal directly.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: READY_FOR_BOUNDED_NON_LIVE_IMPLEMENTATION
