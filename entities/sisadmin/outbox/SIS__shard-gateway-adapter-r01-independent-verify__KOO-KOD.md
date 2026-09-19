# SIS → KOO + KOD: shard gateway adapter r0.1 independent verification

verdict: `REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`
execution_mode: `BOUNDED_NON_DEPLOYING_INDEPENDENT_VERIFY`
deployment_performed: 0
host_mutation_performed: 0
credential_access: 0
project_time: omitted; trusted project-time source not used

## Fresh Resume-First

Fresh HQ HEAD:
`93bc99b7b404688fd6650797fc36128bcb6547f9`.

Current SIS writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
commit `3ca813a7addb711eb8bf2e017b39517268fa31f0`
blob `03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

Current queue:
`entities/koordinator/current/KOO__active-queue-r49.md`.

Exact task:
`entities/koordinator/outbox/KOO__shard-gateway-adapter-r01-verify__SIS.md`
commit `c95f84ea0cc87383cb6274260a7be2263aafdcf9`
blob `2b67097824d61860f082cf7aaec1f186e3872547`.

Project Source set:
`SOURCE_SET_ACTIVATED`
activation result `8be0d932a53237f0176269d9685570599aef8166`.

## Exact immutable candidate identity

Locator:
`puev5691/wellbeing-hq@84c7225e8073beeda86491c1f27f371c4f532a2d:entities/koder/outbox/shard-gateway-adapter-r01`.

Commit:
`84c7225e8073beeda86491c1f27f371c4f532a2d`.

Repository top-level commit tree:
`65cf7222ed9ae702885dcfd42f4ce9b744cd6ac9`.

Exact package subtree:
`ab976b7e627cebd62f8aa9c0d86ea91ef341fcb4`.

Exact composition:
5 files, no extra package entries.

Independent raw-byte identity verification:
- `gateway.py`
  - bytes 12203
  - blob `9aa9b6419983b672cc1bbe599c09fecaf3332d27`
  - SHA-256 `053a70de4a2f082363e1f723fc08b94c87ba8009aa64732e32e3853c76f5eeb6`
  - PASS
- `test_gateway.py`
  - bytes 4012
  - blob `2e3d6a4d879c03f4fce92259ed6985f71c5bc8ab`
  - SHA-256 `4309d7213ec6b7f9ba61221f3e3bc181a7a5c7a76bbf0600e0adae5274ca6207`
  - PASS
- `README.md`
  - bytes 2136
  - blob `ce612288d937792398bca92718400d6ff72a4012`
  - SHA-256 `505e66f1bee51c323bca02c081ed82e7e08480d049f9619332d2d198ff014ae6`
  - PASS
- `TEST-RESULTS.json`
  - bytes 782
  - blob `c4475b55c1bbc594ee5c1325d11950d2999ea3dd`
  - SHA-256 `d1ccae2c6fa82df7e10e4143edac2d6b9f148c3300099ff4dbd0ab23db16c44d`
  - PASS
- `DEPLOYMENT-MANIFEST.json`
  - bytes 1592
  - blob `f9764438eb3c464f6bcfbe57ef52fbb84e2da96f`
  - SHA-256 `3614ef5693ac77d0f90ca0a90dbf21a8c6d2f4ac0d7a0aee874b25812ecd0e08`
  - PASS

Identity result:
`PASS_EXACT_IMMUTABLE_CANDIDATE_5_OF_5`.

## Deterministic test rerun

Exact immutable `gateway.py` and `test_gateway.py` bytes were reconstructed from the pinned Git blobs and rerun locally/synthetically, without production host roots or credentials.

Result:
- tests: 15
- failures: 0
- errors: 0
- verdict: PASS

Rerun covered the candidate suite:
- exact opcode enum;
- unknown opcode/root;
- absolute path/traversal;
- symlink;
- denied target;
- oversized output;
- timeout simulation;
- target-changed race simulation;
- WRITE attempt;
- no automatic failover;
- canonical result/audit;
- exact host mapping;
- concurrency=1 per host.

## Contract points that PASS

The candidate correctly implements:
- exact VERIFY opcode set from the SIS plan;
- exact root mapping:
  - mazhor repository;
  - mazhor approved archive root;
  - burzh repository only;
  - no burzh archive root;
  - no erefia mapping;
- hard-coded mode `VERIFY`;
- `WRITE` rejection as `WRITE_MODE_NOT_AUTHORIZED`;
- no free-form shell command field;
- direct argv Git subprocess calls with no shell interpolation;
- lexical traversal rejection;
- explicit symlink rejection at checked path components;
- explicit denied secret/system target policy;
- request-size limit 32 KiB;
- declared output limit 1 MiB;
- directory/archive entry bounds;
- per-host concurrency semaphore = 1;
- no automatic cross-host failover;
- audit schema identifier `wb.shard_gateway.audit.v1`;
- candidate status non-deploying.

## Required edits

The deterministic tests PASS, but they do not cover four material deviations from the SIS design/security boundary.

### 1. Non-Git wall-time limits are declared but not enforced

The SIS plan requires wall-time limits for all operations:
- default 10 s;
- SHA256 60 s;
- ARCHIVE_LIST 20 s;
- Git 15 s.

Current code enforces `TIMEOUTS` only in `_run()`, therefore only subprocess/Git operations actually receive a timeout.

`STAT`, `LIST_DIR`, `READ_BOUNDED`, `SHA256`, and `ARCHIVE_LIST` can run without the required wall-time enforcement.

Required edit:
implement bounded execution/deadline enforcement for every opcode, including filesystem hashing and archive listing, and add deterministic timeout tests for at least SHA256 and ARCHIVE_LIST/non-Git path.

### 2. No-follow / TOCTOU protection is insufficient for file/archive reads

`resolve_no_symlink()` checks path components using `lstat`, but later:
- `open(target,"rb")`;
- `tarfile.open(target,...)`;
- directory/stat operations

re-resolve the pathname.

An attacker-controlled replacement between validation and open can therefore cause a symlink/target swap after the policy check. `READ_BOUNDED` / `SHA256` compare identity only after opening/reading, which can detect a change after bytes were already read; `ARCHIVE_LIST` has no equivalent before/after identity check.

This does not satisfy the SIS dependency for effective symlink/no-follow enforcement and safe descriptor-relative open where practical.

Required edit:
use descriptor-relative/no-follow open semantics for file-bearing operations, or an equivalently fail-closed primitive that prevents following a newly substituted symlink before any target bytes are read. Apply an equivalent race-safe boundary to archive and directory/stat paths. Add a race/symlink-swap test, not only a post-read identity-change simulation.

### 3. Git blob operations do not enforce the planned validated-ref boundary

For `GIT_LS_TREE`, a non-HEAD ref is constrained to a 40-hex commit and checked as ancestor of HEAD.

For `GIT_BLOB_META` and `GIT_BLOB_READ_BOUNDED`, however, `req.git_ref` is passed directly to `git ls-tree` without the same HEAD/full-40-hex/reachability validation.

Therefore blob operations can address refs outside the planned validated `HEAD` / approved reachable exact-commit boundary.

Required edit:
factor one ref validator and apply it identically to tree and blob operations. Accept only `HEAD` or a full 40-hex commit proven within the approved reachability rule. Add tests for rejected symbolic/non-approved refs in blob meta/read.

### 4. Final serialized result-size boundary is not enforced uniformly

The plan limits result payload to 1 MiB.

The candidate bounds raw file/subprocess bytes, but for `READ_BOUNDED` and `GIT_BLOB_READ_BOUNDED` it then wraps decoded text in JSON. The final canonical payload/result can therefore exceed the requested/max output size because of JSON framing/escaping.

Additionally, non-UTF-8 data can raise `UnicodeDecodeError`, which is not converted to a stable fail-closed `GatewayError`.

Required edit:
enforce the byte cap on the final serialized payload/result, define a stable error for non-text/binary reads, and add tests for JSON-escaping expansion plus invalid UTF-8.

## Audit review

The audit serializer matches the intended schema identifier and metadata fields. It does not itself persist audit records, which is acceptable for this non-deploying adapter candidate; append-only storage/retention remains a deployment concern.

No credential content is serialized by the tested audit path.

## Boundary accounting

Deployment: `0`.
Host mutation: `0`.
SSH mutation: `0`.
Users/groups/ACL/package/service/systemd/firewall changes: `0`.
Credential access/provisioning: `0`.
WRITE enablement: `0`.
Network listener exposure: `0`.
Repository/archive/shard mutation: `0`.

## ARH next-step gate

ARH preservation-boundary review should **not proceed as the next acceptance gate on these unchanged bytes**.

Reason:
the candidate identity is valid and tests are reproducible, but the four deviations above affect the read-only preservation/security contract itself. KOD should publish a corrected immutable candidate first; SIS should then verify the corrected exact bytes. ARH may review the historical r0.1 result as provenance, but it should not treat this package as ready for preservation-boundary acceptance.

## Terminal result

`REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: bounded independent verification of exact immutable shard gateway adapter r0.1 candidate
СТАТУС: `REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`
