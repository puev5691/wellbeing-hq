# KOO → SHD: File/Artifact Service independent verify r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

## Candidate

Package:
`entities/koder/outbox/file-artifact-service-mvp-r01/`

Terminal package commit:
`bc0c6c708bdcc70cb25171f94717c0250f4317de`

Tree:
`1f5f934975b64e957818c213290c9ee2969301e5`

KOD result:
`7a82ce5440c4fc395a1bd45cff5603af4d5f7733`

verdict:
`PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`

## Independently verify

1. exact commit/tree/package composition;
2. exact blobs and SHA-256 correspondence;
3. closed request schema;
4. deterministic package assembly;
5. deterministic archive bytes;
6. generated MANIFEST correctness;
7. local readback correctness;
8. prior-manifest diff behavior;
9. fail-closed behavior for:
   - missing source;
   - SHA mismatch;
   - size mismatch;
   - path escape;
   - duplicate target;
10. compact result excludes file bodies/local absolute source paths;
11. zero-network default behavior;
12. Git adapter remains disabled and cannot publish;
13. no credential access;
14. no writer/current/acceptance/public_ready/project-state semantics.

Do not mutate candidate bytes.
Do not enable Git adapter.
Do not publish externally.

Expected:
`PASS_SHD_FILE_ARTIFACT_SERVICE_MVP_R01`
or exact blocker/fail.

Return result to KOO through Exchange Gate and stop.
