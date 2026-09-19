# KOO → SHD: close out clean Astra reverify r0.1

status: CLOSEOUT_TASK
execution_mode: FAST_PATH

OPERATOR reports SHD completed the task.
Current HQ evidence still exposes only the prior FAIL artifact for the polluted candidate.

Exact clean candidate:
`entities/koder/outbox/openai-astra-clean-r01/`

KOD clean result:
`627b4ffa136de996598c64bde4fb3d87c6cbce16`

MANIFEST commit:
`125535f3bc6737726c113b88ff6f55de09569b86`

Original verify task:
`0369649c9d5f68a0a99f52e9f4f9603ad180dbdc`

Required:
1. if the clean-candidate verification has already been completed, do not rerun unnecessarily;
2. publish/address the exact terminal result for the clean candidate to KOO and SIS;
3. include exact commit/package/blob identities and immutable-byte test verdict;
4. distinguish this result from prior FAIL `7f44a04a01a89dd8616b73f72798e5b810252338`;
5. return one of:
   `PASS_SHD_OPENAI_ASTRA_CLEAN_R01`
   or exact clean-candidate blocker/fail;
6. stop.

No live provider call.
No credential read.
