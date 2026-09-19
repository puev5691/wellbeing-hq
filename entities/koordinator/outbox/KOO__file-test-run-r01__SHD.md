# KOO → SHD: exact File Service test execution r0.1

status: TASK
execution_mode: FAST_PATH
priority: UNBLOCK_KOD

KOD blocker:
`1cf36a0bf268fe6a2f28781fc78b7008ca6aeed6`

status:
`BLOCKED_FILE_ARTIFACT_SERVICE_FIX_R01_TEST_EXECUTION_ENV_UNAVAILABLE`

Current KOD writer v0.4:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

Narrow KOD sealing task:
`615c30b86756713669c1c6f5a7018db26d5d7b38`

## Exact candidate bytes to execute

Read exact Git blobs from current HQ paths for the unfinished candidate:
- file_service.py blob `a47492ecbd91ee09d33cf6a377580ea1c3d1d250`
- test_file_service.py blob `fe68b9c4a201b94db25eab26fcb6fbae20e1cb60`

Candidate path:
`entities/koder/outbox/file-artifact-service-fix-r01/`

## Required

1. fetch exact immutable Git blob bytes by blob identity;
2. materialize only those exact bytes into an isolated temporary execution directory;
3. run the exact test suite unchanged;
4. no network access;
5. no Git publication;
6. no credentials;
7. no candidate modification;
8. record:
   - command;
   - interpreter/runtime identity;
   - exit code;
   - tests/failures/errors/skipped;
   - SHA-256 of executed file_service.py;
   - SHA-256 of executed test_file_service.py;
   - stdout/stderr SHA-256;
9. verify the executed bytes correspond exactly to the Git blobs above;
10. return terminal result:
   `PASS_SHD_FILE_SERVICE_EXACT_TEST_RUN_R01`
   or exact blocker/fail.

This task supplies execution evidence only. It does not accept/seal the package and does not alter KOD writer state.

Return result to KOO and KOD through Exchange Gate and stop.
