# KOO → SHD: verify clean Astra runtime package r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

KOD result:
`627b4ffa136de996598c64bde4fb3d87c6cbce16`

Candidate package:
`entities/koder/outbox/openai-astra-clean-r01/`

MANIFEST commit:
`125535f3bc6737726c113b88ff6f55de09569b86`

Independently verify:
1. exact package/blob identities;
2. no execution annotation remains in any Python payload;
3. MANIFEST byte-size/SHA correspondence to final immutable Git bytes;
4. exact allowlist Luna/Terra/Sol/Astra across policy/adapter/live layers;
5. unknown-model fail-closed behavior;
6. exact 9/13/6 test suites on immutable bytes;
7. retries=0, fallback=none, no tools/web/files/computer/code capability preserved;
8. hidden credential/no-persistence contract preserved;
9. no live provider call and no credential read in this task.

Expected:
`PASS_SHD_OPENAI_ASTRA_CLEAN_R01`
or exact blocker/fail.

Do not modify candidate.
Return result to KOO and stop.
