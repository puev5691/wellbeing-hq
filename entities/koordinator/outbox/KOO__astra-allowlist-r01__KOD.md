# KOO → KOD: add Astra to verified OpenAI runtime allowlist r0.1

status: TASK
execution_mode: CORRECTION_ONLY
priority: TOP_INFRASTRUCTURE

SIS blocker:
`8139700f5f31523073d7bbe3ee93e393308d0775`

Current verified runtime allowlist:
- `gpt-5.6-luna`
- `gpt-5.6-terra`
- `gpt-5.6-sol`

Required addition only:
- `gpt-6-astra`

## Preserve exactly

Do not redesign request/runtime behavior.
Preserve:
- existing request shape;
- hidden `/dev/tty` credential entry;
- no credential persistence;
- retries=0;
- fallback=none;
- no tools/web/files/code execution;
- same synthetic/live boundary;
- existing Luna/Terra/Sol semantics;
- existing parser/policy behavior except exact Astra admission.

## Required

1. update all model allowlist enforcement points consistently;
2. add/update tests for exact four-model allowlist;
3. reject unknown models exactly as before;
4. build immutable correction package;
5. update manifest/blob/SHA identities;
6. run bounded tests;
7. return:
   `PASS_KOD_OPENAI_ASTRA_ALLOWLIST_R01_READY_FOR_VERIFY`
   or exact blocker/fail.

No live provider call in this task.
No credential read.
Return result to KOO and stop.
