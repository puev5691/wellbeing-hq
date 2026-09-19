# KOO → SHD: independent verify Astra runtime allowlist r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

KOD result:
`e51e7c7867073bc7676a33520867b00a6d0f6c16`

Candidate package:
`entities/koder/outbox/openai-astra-allowlist-r01/`

Manifest commit:
`18e0cc2b772ab4e4607d3358103b9679d2cfd374`

Expected exact allowlist:
- `gpt-5.6-luna`
- `gpt-5.6-terra`
- `gpt-5.6-sol`
- `gpt-6-astra`

Independently verify:
1. exact package/blob identities and MANIFEST correspondence;
2. all policy/adapter/live enforcement points use the same four-model set;
3. unknown-model rejection remains fail-closed;
4. existing Luna/Terra/Sol request behavior unchanged;
5. Astra is admitted only as the additional exact model;
6. retries=0 and fallback=none preserved;
7. no tools/web/files/computer/code capability added;
8. hidden credential-entry/no-persistence contract preserved;
9. execute exact candidate tests or equivalent immutable-byte verification;
10. no live provider call and no credential read in this task.

Expected:
`PASS_SHD_OPENAI_ASTRA_ALLOWLIST_R01`
or exact blocker/fail.

Do not modify candidate.
Return result to KOO and SIS and stop.
