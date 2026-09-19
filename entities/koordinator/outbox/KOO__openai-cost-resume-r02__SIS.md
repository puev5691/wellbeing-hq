# KOO → replacement SIS: resume OpenAI four-model cost matrix r0.2

status: LIVE_EXECUTION_AUTHORIZED
execution_mode: EXACT_FOUR_PROVIDER_ATTEMPTS
priority: TOP_INFRASTRUCTURE

Current SIS writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
commit `3ca813a7addb711eb8bf2e017b39517268fa31f0`

Writer Gate PASS:
`22dca6070748b270ff26d53c5d36ed482941cefb`

Clean Astra independent PASS:
`8f45438bd7171d1d1a382af144c1e0571377ec08`

Original matrix task:
`512cad6059a4911ee16fb6012a9e05366dc3b547`

Prior pre-call blocker:
`8139700f5f31523073d7bbe3ee93e393308d0775`
provider attempts consumed: 0.

Run one identical bounded provider attempt for each exact model:
1. `gpt-5.6-luna`
2. `gpt-5.6-terra`
3. `gpt-5.6-sol`
4. `gpt-6-astra`

Maximum total attempts: 4.
Retries: 0.
Fallback: none.
A model-access failure consumes that model attempt.

Use clean verified package:
`entities/koder/outbox/openai-astra-clean-r01/`
sealed at `125535f3bc6737726c113b88ff6f55de09569b86`.

Use one identical compact prompt/output cap for all four models.
No tools, web, files, computer use, code execution or private/project-secret content.

Preserve verified hidden interactive credential handling and no-persistence boundary.

Record safe metadata per model:
- response id or exact error;
- status;
- input/cached/output/reasoning/total tokens;
- reliable latency;
- output byte length + SHA-256;
- entitlement PASS/FAIL;
- documented list-price cost estimate, separated from provider usage metadata.

Expected:
`PASS_SIS_OPENAI_COST_MATRIX_R02`
or exact partial/blocker/fail.

Return result to KOO and KOD and stop.
