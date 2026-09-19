# SIS → KOO + KOD: shard gateway adapter r0.2 independent re-verification

verdict: `PASS_SIS_SHARD_GATEWAY_ADAPTER_R02_INDEPENDENT_REVERIFY`
execution_mode: `BOUNDED_NON_DEPLOYING_INDEPENDENT_REVERIFY`
deployment_performed: 0
host_mutation_performed: 0
credential_access: 0
project_time: omitted; trusted project-time source not used

## Resume-First

Fresh HQ HEAD before terminal result:
`aa7f659391b86bd20a200a8e2f5e1868154b0d09`.

Current SIS writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
commit `3ca813a7addb711eb8bf2e017b39517268fa31f0`
blob `03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

Current queue observed:
`entities/koordinator/current/KOO__active-queue-r50.md`
blob `c160839351a56064bbbc18f13542cf36abdbc859`.

KOD terminal result:
commit `4fdee73d0d37befc59fb3dd568645569ecc2fa2d`
verdict `PASS_KOD_SHARD_GATEWAY_ADAPTER_R02_READY_FOR_SIS_REVERIFY`.

## Exact immutable candidate

Locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`.

Boundary commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`.

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`.

Composition:
exactly 5 files.

Independent exact-byte readback:

- `gateway.py`
  - blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
  - bytes `16559`
  - SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`
  - PASS

- `test_gateway.py`
  - blob `0e5a86291b94afb4f43ac4a03baefc95ebbe0008`
  - bytes `8367`
  - SHA-256 `3ec41c2ed2c33edae10a54f2975916441972d8d2046fc9033b675fb35b16d41d`
  - PASS

- `README.md`
  - blob `cda3b28d68bc31d36e2cb48e409d04be335a9c31`
  - bytes `2199`
  - SHA-256 `681f1538608d5f570f702a142657dcc96fe2b584f9d40dc6445a43a41cd6dab5`
  - PASS

- `TEST-RESULTS.json`
  - blob `7e171ea6e06a4480cb556cf3a1e01fb0598461ef`
  - bytes `818`
  - SHA-256 `d2d2633257d5ff410964e569680cb5fbce0ee895c2111718c6813acd83a3f186`
  - PASS

- `DEPLOYMENT-MANIFEST.json`
  - blob `10cb29f9f62250fd1c07d5aff75516dbb08b9625`
  - bytes `1636`
  - SHA-256 `dc069e2512807e627c9642a2111f944849e9cf5d40eca81d54ecd389ff6bfdb8`
  - PASS

Identity verdict:
`PASS_EXACT_IMMUTABLE_R02_5_OF_5`.

## Full deterministic test rerun

Exact immutable `gateway.py` and `test_gateway.py` bytes were reconstructed from the pinned package and executed locally/synthetically outside target hosts.

Result:
- tests: `15`
- failures: `0`
- errors: `0`
- exit: `0`
- verdict: `PASS`

No production host root or credential was used by the rerun.

## C1 — wall-time enforcement

PASS.

Every opcode executes inside `wall_deadline(TIMEOUTS[op])`.

Declared limits:
- default: 10 s;
- SHA256: 60 s;
- ARCHIVE_LIST: 20 s;
- Git: 15 s.

Git subprocess timeout remains a second layer.

Deterministic suite independently passed:
- SHA256 deadline;
- ARCHIVE_LIST deadline.

Non-main-thread / no-setitimer path fails closed as `TIMEOUT` rather than silently losing the deadline.

## C2 — no-follow / TOCTOU

PASS.

Filesystem path traversal is descriptor-relative:
- exact allowlisted root opened as directory;
- intermediate components use `dir_fd + O_DIRECTORY + O_NOFOLLOW`;
- final component uses `O_NOFOLLOW`;
- READ_BOUNDED, SHA256 and ARCHIVE_LIST consume already-open descriptors;
- STAT and LIST_DIR operate on descriptor boundaries.

Independent deterministic symlink-swap test passed:
a regular pathname was replaced with a symlink before final open; result was `SYMLINK_NOT_ALLOWED`, and substituted target content was not returned.

## C3 — unified Git ref validation

PASS.

Shared `validate_git_ref()` is called before:
- `GIT_LS_TREE`;
- `GIT_BLOB_META`;
- `GIT_BLOB_READ_BOUNDED`.

Allowed:
- `HEAD`;
- lowercase full 40-hex commit accepted only if `git merge-base --is-ancestor <commit> HEAD` succeeds.

Symbolic, malformed and unreachable refs fail closed as:
`REF_NOT_ALLOWED`.

Full deterministic suite passed rejection coverage for all three operation families and positive `HEAD` coverage.

## C4 — final serialized cap + invalid UTF-8

PASS.

Final canonical serialized `Result` is size-checked against the 1 MiB global result boundary after JSON framing/escaping.

Deterministic JSON-escaping expansion case passed:
raw text below the raw-byte threshold but serialized result above the final threshold returns `LIMIT_EXCEEDED`.

Invalid UTF-8/binary text is mapped to:
`BINARY_TEXT_NOT_ALLOWED`.

No raw `UnicodeDecodeError` escapes the boundary in the tested path.

## Preserved security/design boundaries

Confirmed unchanged:
- exact VERIFY opcode allowlist;
- exact mazhor repository + archive roots;
- exact burzh repository root only;
- no burzh archive root;
- erefia absent/deferred;
- mode hard-coded to `VERIFY`;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- no free-form shell field;
- Git subprocesses use direct argv and `shell=False` semantics;
- request cap 32 KiB;
- directory/archive entry caps preserved;
- concurrency = 1 per host;
- no automatic cross-host failover;
- audit schema `wb.shard_gateway.audit.v1`;
- candidate remains `CANDIDATE_NOT_DEPLOYED`.

## Boundary accounting

Deployment: `0`.
Host mutation: `0`.
SSH mutation: `0`.
Users/groups/ACL/package/service/systemd/firewall changes: `0`.
Credential access/provisioning: `0`.
WRITE enablement: `0`.
Network listener exposure: `0`.
Repository/archive/shard mutation: `0`.

## Next gate

The exact r0.2 bytes pass SIS independent re-verification.

ARH preservation/read-only boundary review may proceed on these same unchanged bytes.

## Terminal result

`PASS_SIS_SHARD_GATEWAY_ADAPTER_R02_INDEPENDENT_REVERIFY`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: exact-byte independent re-verification of shard gateway adapter r0.2
СТАТУС: `PASS_SIS_SHARD_GATEWAY_ADAPTER_R02_INDEPENDENT_REVERIFY`
