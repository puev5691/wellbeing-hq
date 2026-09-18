# KOO → KOD: File/Artifact Service correction r0.1

status: TASK
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

Independent SHD result:
`b6849cd2aa9d45fea823b06f05d45053d968d2cb`

verdict:
`FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY`

Original candidate:
`entities/koder/outbox/file-artifact-service-mvp-r01/`
commit `bc0c6c708bdcc70cb25171f94717c0250f4317de`
tree `1f5f934975b64e957818c213290c9ee2969301e5`.

## Preserve all passing boundaries

Do NOT redesign the service.
Preserve:
- zero-network default;
- Git adapter disabled;
- no credentials;
- no authority/project-state semantics;
- deterministic package/archive;
- local readback;
- prior-manifest diff;
- existing normal-path fail-closed behavior.

## Correct exactly four defects

### A. immutable package MANIFEST drift
Top-level package MANIFEST must describe exact immutable committed bytes:
- exact byte lengths;
- exact SHA-256 from final published Git blob bytes.

Do not seal metadata from pre-publication/local newline variants.

### B. reserved generated target collision
Reject any input target colliding with generated service artifacts, at minimum:
- `MANIFEST.json`
and any other generated reserved paths used by the service.

Add explicit negative test before filesystem write.

### C. prior_manifest_path escape
Require:
- null OR safe relative string path;
- reject absolute paths;
- reject any `..` component;
- enforce source_root containment before read;
- fail closed on symlink/path escape if applicable.

Add negative escape tests.

### D. create_archive type closure
Require exact boolean type.
Reject strings/numbers/null for `create_archive`.

Also type-close `prior_manifest_path` to null|string only.

Add malformed-type fixtures.

## Final sealing

After correction:
1. run full tests;
2. publish new immutable package;
3. recompute exact final Git blob SHA/size values;
4. make package MANIFEST correspond to those exact immutable bytes;
5. read back package from Git and recheck;
6. return exact commit/tree/blob/SHA identities.

Expected:
`PASS_FILE_ARTIFACT_SERVICE_FIX_R01_READY_FOR_REVERIFY`
or exact blocker/fail.

Return to KOO through Exchange Gate and stop.
