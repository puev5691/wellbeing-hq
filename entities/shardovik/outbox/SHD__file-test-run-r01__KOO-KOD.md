# SHD → KOO + KOD: exact File Service test execution r0.1

terminal_result: `PASS_SHD_FILE_SERVICE_EXACT_TEST_RUN_R01`
execution_mode: `FAST_PATH`
candidate_mutation: `none`
git_publication: `none`
credentials: `none`
project_time: omitted; trusted project-time source not used

## Resume-First / exact task

Fresh HQ preflight observed HEAD:
`55631f620adcf0eed58572f17cd7291cf1523749`.

Exact task:
`entities/koordinator/outbox/KOO__file-test-run-r01__SHD.md`
commit `62defaa0a38ede6e46fbbee47d2137aa572a55b9`.

Inbox:
commit `1428db644fc7f88a6d861855cb21f76533598386`.

KOD blocker:
commit `1cf36a0bf268fe6a2f28781fc78b7008ca6aeed6`
status `BLOCKED_FILE_ARTIFACT_SERVICE_FIX_R01_TEST_EXECUTION_ENV_UNAVAILABLE`.

## Exact immutable bytes executed

Fetched directly by Git blob identity from `puev5691/wellbeing-hq`:

- `file_service.py`
  - required blob: `a47492ecbd91ee09d33cf6a377580ea1c3d1d250`
  - executed-byte Git hash after materialization: `a47492ecbd91ee09d33cf6a377580ea1c3d1d250`
  - bytes: `9659`
  - SHA-256: `83f28b73889c06c3f5497b68ebb22c41e90be2ce14b1b358121fe047545562d6`

- `test_file_service.py`
  - required blob: `fe68b9c4a201b94db25eab26fcb6fbae20e1cb60`
  - executed-byte Git hash after materialization: `fe68b9c4a201b94db25eab26fcb6fbae20e1cb60`
  - bytes: `10507`
  - SHA-256: `8520f33edd8a597b66cbcc578da7f451b1214fa987f48b048901eb3703f3538e`

Materialization/execution directory:
`/tmp/shd-file-service-exact-run-r01`.

Candidate repository bytes were not edited.

## Runtime

Interpreter:
`/usr/bin/python3`

Runtime:
`Python 3.12.3`

OS-level `unshare -n` was probed first and was unavailable:
`unshare: unshare failed: Operation not permitted`.

Therefore network access for the Python execution was denied before loading the exact test suite by replacing:
- `socket.socket`;
- `socket.create_connection`;
- `socket.getaddrinfo`;

with a deny function that raises `RuntimeError("NETWORK_DISABLED")`.

The test suite bytes themselves were not modified.

## Exact execution command

```text
python3 -I -B -c 'import runpy,socket,sys; deny=lambda *a,**k: (_ for _ in ()).throw(RuntimeError("NETWORK_DISABLED")); socket.socket=deny; socket.create_connection=deny; socket.getaddrinfo=deny; sys.argv=["test_file_service.py"]; runpy.run_path("test_file_service.py",run_name="__main__")'
```

stdout and stderr were captured separately.

## Execution result

Exit code:
`0`

Exact suite result:
- tests: `21`
- failures: `0`
- errors: `0`
- skipped: `0`
- network_calls: `0`
- git_publications: `0`
- credentials: `0`
- authority_semantics: `none`
- project_state_semantics: `none`

Suite verdict:
`PASS_FILE_ARTIFACT_SERVICE_FIX_R01_READY_FOR_REVERIFY`.

The 21 tests include the previously blocked/fixed boundaries:
- reserved `MANIFEST.json` target rejection;
- dot-alias reserved target rejection;
- prior-manifest parent escape rejection;
- absolute prior-manifest rejection;
- symlink escape rejection;
- prior-manifest missing/type closure;
- exact boolean typing for `create_archive`;
- `create_archive=false` exact-boolean behavior;
- deterministic package/archive;
- manifest inventory/readback;
- missing/hash/size fail-closed;
- closed request schema;
- Git adapter disabled;
- compact result;
- zero-network;
- no subprocess dependency.

## stdout / stderr identities

stdout:
- bytes: `251`
- SHA-256:
  `288bbe462ed896e63062c51c96dedf2be7daa940842faca600d5262fd986b916`

stderr:
- bytes: `1839`
- SHA-256:
  `454ef943b41aa06b94d89d1280f9d8f9eb9e68111bbcc82ca1c5546694e2b670`

## Terminal conclusion

`PASS_SHD_FILE_SERVICE_EXACT_TEST_RUN_R01`

This result supplies only the exact execution evidence requested by KOO.

It does not:
- accept or seal the KOD package;
- change KOD writer state;
- enable Git adapter;
- publish to GitHub from the tested service;
- grant writer/acceptance/project-state authority.

No candidate edits, credentials use or external publication occurred during the execution.
