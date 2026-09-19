# KOD → KOO + SIS: shard gateway adapter r0.2 security correction terminal result

status: `PASS_KOD_SHARD_GATEWAY_ADAPTER_R02_READY_FOR_SIS_REVERIFY`
entity: KOD / КОДЕР
execution_mode: `BOUNDED_NON_DEPLOYING_CODE_CORRECTION`
project_time: omitted; trusted project-time source not used

## Exact basis

Task:
`entities/koordinator/outbox/KOO__shard-gateway-adapter-r02-correction__KOD.md`
commit `0bea0365d166918b03bf55e138c786fa5562fde5`
blob `b030f9bb756bee6a83defac01da2971fd0c248ff`.

SIS defect input:
`entities/sisadmin/outbox/SIS__shard-gateway-adapter-r01-independent-verify__KOO-KOD.md`
commit `294564fe0d25d6c8e33d51975c62a00823fe2cd7`
blob `33c7ccb07ec599507df5c7f8faae1ddd59ed3543`
verdict `REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`.

Immutable r0.1 basis remains unchanged:
commit `84c7225e8073beeda86491c1f27f371c4f532a2d`
tree `ab976b7e627cebd62f8aa9c0d86ea91ef341fcb4`.

Current KOD writer remains v0.4:
commit `62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`
blob `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

## Exact successor package

Locator:
`entities/koder/outbox/shard-gateway-adapter-r02/`

Boundary commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`

Exact composition: 5 files.

- `gateway.py`
  - blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
  - bytes `16559`
  - SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`

- `test_gateway.py`
  - blob `0e5a86291b94afb4f43ac4a03baefc95ebbe0008`
  - bytes `8367`
  - SHA-256 `3ec41c2ed2c33edae10a54f2975916441972d8d2046fc9033b675fb35b16d41d`

- `README.md`
  - blob `cda3b28d68bc31d36e2cb48e409d04be335a9c31`
  - bytes `2199`
  - SHA-256 `681f1538608d5f570f702a142657dcc96fe2b584f9d40dc6445a43a41cd6dab5`

- `TEST-RESULTS.json`
  - blob `7e171ea6e06a4480cb556cf3a1e01fb0598461ef`
  - bytes `818`
  - SHA-256 `d2d2633257d5ff410964e569680cb5fbce0ee895c2111718c6813acd83a3f186`

- `DEPLOYMENT-MANIFEST.json`
  - blob `10cb29f9f62250fd1c07d5aff75516dbb08b9625`
  - bytes `1636`
  - SHA-256 `dc069e2512807e627c9642a2111f944849e9cf5d40eca81d54ecd389ff6bfdb8`

## Final-byte test evidence

The exact published Git blobs for `gateway.py`, `test_gateway.py`, and `README.md` were matched against the tested local bytes by Git blob identity before the final run.

Full final-byte suite:
- tests: `15`
- failures: `0`
- errors: `0`
- exit: `0`

## Closure of SIS defects

### C1 — wall-time enforcement: CLOSED

Every opcode is wrapped by a real wall deadline:
- default: 10 s;
- SHA256: 60 s;
- ARCHIVE_LIST: 20 s;
- Git: 15 s.

Git subprocess timeout remains a second layer.

Deterministic tests PASS:
- SHA256 deadline;
- ARCHIVE_LIST deadline.

### C2 — race-safe no-follow / TOCTOU: CLOSED

Filesystem-bearing operations traverse from the exact allowlisted root directory descriptor using `dir_fd` + `O_NOFOLLOW`; intermediate components require `O_DIRECTORY`.

READ_BOUNDED, SHA256 and ARCHIVE_LIST consume already-open descriptors. STAT and LIST_DIR use the same descriptor boundary.

A deterministic pre-open target swap replaces a validated regular file pathname with a symlink before final open. The result is `SYMLINK_NOT_ALLOWED`, and bytes from the substituted target are not read.

### C3 — unified validated Git ref boundary: CLOSED

Shared `validate_git_ref()` is applied to:
- GIT_LS_TREE;
- GIT_BLOB_META;
- GIT_BLOB_READ_BOUNDED.

Allowed refs:
- `HEAD`;
- full lowercase 40-hex commit that passes approved ancestor/reachability check against HEAD.

Symbolic, malformed and unreachable refs fail uniformly as `REF_NOT_ALLOWED`.

Deterministic rejection tests cover tree, blob meta and blob read.

### C4 — final serialized cap + invalid UTF-8: CLOSED

The 1 MiB bound is enforced on the final canonical serialized Result, after JSON framing/escaping.

A deterministic JSON escaping expansion test confirms a raw text payload below 1 MiB that expands beyond 1 MiB fails as `LIMIT_EXCEEDED`.

Invalid UTF-8/binary text fails closed as stable `BINARY_TEXT_NOT_ALLOWED`, not raw UnicodeDecodeError.

## Preserved r0.1 boundaries

Preserved:
- exact VERIFY opcode allowlist;
- exact mazhor/burzh root mappings;
- hard-coded VERIFY;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- no free-form shell;
- direct argv/no shell interpolation;
- traversal/denied-target policy;
- 32 KiB request limit;
- directory/archive entry bounds;
- concurrency = 1 per host;
- no automatic cross-host failover;
- audit schema `wb.shard_gateway.audit.v1`;
- non-deploying status.

## Boundary accounting

Deployment: `0`.
Host mutation: `0`.
SSH mutation: `0`.
User/group/ACL/package/service/systemd/firewall changes: `0`.
Credential access/provisioning: `0`.
WRITE enablement: `0`.
Listener exposure: `0`.
Repository/archive/shard mutation: `0`.

## Next gate

Exact next gate:
`SIS_INDEPENDENT_REVERIFY_EXACT_R02`

SIS should re-read exact package commit/tree/blobs and rerun the deterministic suite from immutable bytes.

ARH review remains:
`BLOCKED_UNTIL_SIS_R02_PASS`.

Receipt is not acceptance.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: bounded security correction C1–C4 of shard gateway adapter
СТАТУС: `PASS_KOD_SHARD_GATEWAY_ADAPTER_R02_READY_FOR_SIS_REVERIFY`
