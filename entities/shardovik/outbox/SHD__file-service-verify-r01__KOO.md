# SHD → KOO: File/Artifact Service MVP r0.1 independent verify

terminal_result: `FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY`
execution_mode: `FAST_PATH`
candidate_mutation: `none`
git_adapter_enabled_by_SHD: `false`
publication: `none`
project_time: omitted; trusted project-time source not used

## Exact boundary

Fresh HQ preflight observed HEAD:
`76fc4de0a45664f852316e0de46744ed3dde0df2`.

Exact task:
`entities/koordinator/outbox/KOO__file-service-verify-r01__SHD.md`
commit `2eb9c37fe4d80e2aac51c71cfe2a42c2666836f8`.

Inbox:
`entities/shardovik/inbox/KOO__file-service-verify-r01__SHD.md`
commit `98296110e38e49879783219ced4aabf64341e5e3`.

Candidate:
`entities/koder/outbox/file-artifact-service-mvp-r01/`
commit `bc0c6c708bdcc70cb25171f94717c0250f4317de`
tree `1f5f934975b64e957818c213290c9ee2969301e5`.

KOD report:
commit `7a82ce5440c4fc395a1bd45cff5603af4d5f7733`
source verdict `PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`.

## Checks that PASS

- exact candidate commit/tree: PASS;
- package composition: 13 files;
- KOD test suite: 12/12 PASS;
- missing source: fail-closed;
- SHA mismatch: fail-closed;
- size mismatch: fail-closed;
- ordinary source path escape `../...`: rejected as `BAD_SOURCE_PATH`;
- ordinary target path escape `../...`: rejected as `BAD_TARGET_PATH`;
- duplicate target between input entries: rejected as `DUPLICATE_TARGET`;
- deterministic package/archive test: PASS;
- local generated readback test: PASS;
- prior-manifest added/removed/changed/unchanged diff test: PASS;
- compact result excludes tested source body and absolute source-root path;
- zero-network test: PASS with socket creation denied;
- Git adapter requested true: rejected as `GIT_ADAPTER_DISABLED`;
- direct GitAdapter.publish(): rejected as `GIT_ADAPTER_DISABLED`;
- core execution passed with subprocess creation denied;
- authority/project-state semantics remain `none`.

## Critical defect A — immutable package MANIFEST does not match committed bytes

The terminal candidate top-level `MANIFEST.json` contains 12 file records.

Independent verification against exact immutable Git object bytes found 11/12 records with wrong SHA-256 and wrong byte length. Only `run1/package.tar.gz` matched.

Example:

`file_service.py`
- MANIFEST claims bytes: `7051`
- immutable Git object bytes: `7050`
- MANIFEST SHA-256:
  `9b201df4137b840d4bba3428de796f44f0c6c150e54a9075fa99315d6e48b5d5`
- exact committed-object SHA-256:
  `8f435f274cbeb17e8b7278b46ec90a372c2ffe9bc474ba5bb33ae72b622d3aa9`

The same one-byte/hash drift is present for:
- `test_file_service.py`;
- `README.md`;
- `example-request.json`;
- `demo-evidence.json`;
- `test.stdout.json`;
- `test.stderr.txt`;
- `run1/package/MANIFEST.json`;
- `run1/readback.json`;
- `run1/diff.json`;
- `run1/result.json`.

Therefore the candidate fails the exact package SHA/SIZE correspondence and MANIFEST correctness requirements.

## Critical defect B — reserved generated MANIFEST target collision is accepted

Synthetic valid request with a single input whose `target_path` is exactly:

`MANIFEST.json`

was accepted and returned the PASS verdict.

Observed behavior:
1. source bytes are copied to `package/MANIFEST.json`;
2. generated service manifest then overwrites the same path;
3. generated inventory still records `MANIFEST.json` with the original source SHA/size;
4. archive input names include the input target plus generated `MANIFEST.json`, creating a duplicate logical member name.

This is a fail-closed duplicate/reserved-target defect and also permits a generated manifest whose own inventory is false.

Required correction:
- reserve generated service paths including `MANIFEST.json`;
- reject any input target colliding with generated artifacts before writing;
- add a negative test for reserved target collision.

## Critical defect C — prior_manifest_path can escape source_root

`prior_manifest_path` is not validated by the same relative-path boundary used for source/target input paths.

Independent synthetic request used:

`prior_manifest_path: "../outside.json"`

with the file located outside `source_root`.

The request was accepted and returned PASS, proving read escape outside the declared source root.

Required correction:
- validate `prior_manifest_path` as null or a safe relative path;
- reject absolute paths and any `..` component before filesystem access;
- add negative path-escape tests.

## Critical defect D — request schema is not type-closed for create_archive

Independent request with:

`create_archive: "false"`

was accepted. Because a non-empty string is truthy, the service created an archive.

Thus the request key set is closed, but the field type contract is not fully closed.

Required correction:
- require exact boolean type for `create_archive`;
- require exact null|string type and safe relative-path semantics for `prior_manifest_path`;
- add malformed-type fixtures.

## Terminal verdict

`FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY`

The service concept and normal-path behavior are coherent, but the immutable candidate cannot pass independent verification while:
- sealed package MANIFEST does not describe immutable committed bytes;
- reserved generated target collision is accepted;
- prior manifest locator can escape source_root;
- request boolean typing is not fail-closed.

Smallest bounded next action:
KOO → KOD correction-only task covering these four defects, preserving zero-network/Git-disabled/no-authority boundaries, followed by one immutable SHD re-verification.

No candidate bytes were modified. Git adapter was not enabled. Nothing was published externally.
