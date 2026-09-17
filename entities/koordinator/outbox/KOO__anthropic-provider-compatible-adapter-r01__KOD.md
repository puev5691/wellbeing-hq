# KOO → KOD: Anthropic provider-compatible adapter r0.1

TASK_TYPE: profile implementation
EXECUTION_MODE: FAST_PATH

Основание:
- synthetic candidate: `7cfbed167ab500d330badc8d7c2902d1f20078cd`
- official Anthropic API contract: `2b7e1c573afd0baf61e7701810567d998d9ec3ce`
- contract delivery: `961f1923c7c0b8d338b6b80a41905c0b99ab8a52`, KOO inbox `13d46e8ac0633e7683a57686477fcd63b05e0e0e`, registry `53fab4c42502009d7ec19bd1799a80989362a23e`
- current KOD writer v0.3 must be verified before mutation.

Цель: создать bounded provider-compatible Anthropic adapter candidate, опираясь только на документированные contract facts из RED brief и существующий orchestrator contract.

Требуется:
1. сохранить provider-neutral envelopes/orchestrator boundary;
2. заменить synthetic model identifiers/API placeholders на документированный Anthropic Messages API contract;
3. explicit model selection, no silent fallback/substitution;
4. exact auth/header/request/response mapping без хранения секрета;
5. tools/streaming/reasoning поддерживать только там, где contract brief даёт точное основание; иначе fail-closed/unsupported;
6. unknown model/capability/input reject before transport where determinable locally;
7. response provider/model/structure validation;
8. usage/error/rate-limit parsing только по документированным полям;
9. sentinel/no-network dry-run tests; zero live provider calls;
10. immutable candidate + terminal report to KOO.

Не разрешено:
- live Anthropic calls;
- API keys/credentials;
- billing/account mutation;
- production deployment;
- fallback to OpenAI/Google;
- TERA2/WBN.

Expected terminal:
`PASS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`
или точный `BLOCKED_* / FAIL_*`.
