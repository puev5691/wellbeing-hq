# KOO → KOD: complete File/Artifact Service sealing r0.1

status: PROFILE_TASK_AUTHORIZED
execution_mode: FAST_PATH
priority: HIGH_INFRASTRUCTURE

Current KOD writer v0.4:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

Writer Gate PASS:
`bb83ef3fdc1c1942a71f3aad3adf3695bf5fd6a3`

Original correction task:
`9bb40b893250f9776edf2f6166ff90fe83fb43a8`

Preserved partial evidence:
- `ad73f466e78d7ba96b5cea5c9208277514c2c531`
- `835e3001fcdb6b8d9eaef3cb6d44d1de449118af`
- `11b01b9175bb712da085e290aa120ee738eb2453`
- `73726c6d0f024310cb20ab7ae5a42e45267a4a90`
- `f1717dde860381d80570fb820657e38182dbb560`

These remain `UNFINISHED_UNACCEPTED_EVIDENCE_TAIL` until this task completes.

## Decision

Do NOT redo the code fixes unless verification of the existing partial candidate fails.

Required sequence:
1. fresh HQ preflight;
2. verify current writer v0.4 exact identity;
3. read and verify existing partial `file_service.py` and `test_file_service.py` against the correction task;
4. run the test suite on the existing partial candidate;
5. if tests and requested boundaries pass, do not edit code;
6. complete the missing immutable package composition only;
7. generate/seal package MANIFEST from exact final Git blob bytes and exact byte sizes;
8. ensure reserved-target/path/type fixes are covered by final tests/evidence;
9. perform final Git readback of exact commit/tree/blobs;
10. publish terminal result:
   `PASS_FILE_ARTIFACT_SERVICE_FIX_R01_READY_FOR_REVERIFY`
   or exact blocker/fail;
11. route to KOO through Exchange Gate and stop.

If existing code verification fails, return the exact failed assertion/boundary before making broader changes.

Do not:
- redesign the service;
- enable Git adapter;
- introduce network access;
- access credentials;
- mutate project state/authority semantics;
- deploy shard tooling.
