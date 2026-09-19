# KOO → SIS: shard gateway adapter r0.1 independent verify

status: TASK
execution_mode: BOUNDED_NON_DEPLOYING_INDEPENDENT_VERIFY
project_time: omitted; trusted project-time source not used

## Fresh basis

Current Project Source set:
`SOURCE_SET_ACTIVATED`
activation result commit:
`8be0d932a53237f0176269d9685570599aef8166`.

Current KOO writer:
`entities/koordinator/current/KOO__replacement-current-writer-v06.md`
commit `525e5b131472e61b1f55db5ef7307217aea4c4fc`.

SIS design basis:
`entities/sisadmin/outbox/SIS__shard-gateway-plan-r01__KOO.md`
commit `8f4c81d283a78ece19e01e54f9fb4d82688b77d7`
verdict `PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`.

KOD terminal result:
`entities/koder/outbox/KOD__shard-gateway-adapter-r01__KOO-SIS.md`
commit `abe67edb9fbca9201d4a107761c835a696946591`
verdict `PASS_KOD_SHARD_GATEWAY_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`.

KOD already delivered/addressed that result to SIS:
- inbox/result address commit `999959c2d0e8435368d0d4b96b5409c90383a045`;
- result dispatch commit `8ea148d3731ad0d17fea866b32d857ae79971942`.

Those artifacts are input/evidence only; they did not themselves create this independent-verify task.

## Exact candidate locator

Package:
`entities/koder/outbox/shard-gateway-adapter-r01/`

Boundary commit:
`84c7225e8073beeda86491c1f27f371c4f532a2d`

Boundary tree:
`ab976b7e627cebd62f8aa9c0d86ea91ef341fcb4`

Exact files from KOD terminal result:

- `gateway.py`
  blob `9aa9b6419983b672cc1bbe599c09fecaf3332d27`
  SHA-256 `053a70de4a2f082363e1f723fc08b94c87ba8009aa64732e32e3853c76f5eeb6`

- `test_gateway.py`
  blob `2e3d6a4d879c03f4fce92259ed6985f71c5bc8ab`
  SHA-256 `4309d7213ec6b7f9ba61221f3e3bc181a7a5c7a76bbf0600e0adae5274ca6207`

- `README.md`
  blob `ce612288d937792398bca92718400d6ff72a4012`
  SHA-256 `505e66f1bee51c323bca02c081ed82e7e08480d049f9619332d2d198ff014ae6`

- `TEST-RESULTS.json`
  blob `c4475b55c1bbc594ee5c1325d11950d2999ea3dd`
  SHA-256 `d1ccae2c6fa82df7e10e4143edac2d6b9f148c3300099ff4dbd0ab23db16c44d`

- `DEPLOYMENT-MANIFEST.json`
  blob `f9764438eb3c464f6bcfbe57ef52fbb84e2da96f`
  SHA-256 `3614ef5693ac77d0f90ca0a90dbf21a8c6d2f4ac0d7a0aee874b25812ecd0e08`

Read exact bytes directly from the shared GitHub information field. Do not require OPERATOR to transfer these candidate files.

## Verify

Perform one bounded independent verification:

1. exact package commit/tree/composition identity;
2. exact file/blob/SHA identities;
3. opcode set against SIS plan;
4. host/root mappings against SIS plan:
   - mazhor exact roots;
   - burzh exact repository root;
   - no burzh archive root;
   - erefia absent/deferred;
5. VERIFY hard-coded read-only;
6. WRITE fails closed as `WRITE_MODE_NOT_AUTHORIZED`;
7. no free-form shell command;
8. direct argv/no shell interpolation;
9. path normalization/traversal/symlink/denied-target handling;
10. output/request/time/concurrency limits against SIS plan;
11. no automatic cross-host failover;
12. audit schema compatibility with `wb.shard_gateway.audit.v1`;
13. deterministic test rerun from exact immutable bytes where current tools permit;
14. confirm candidate remains non-deploying.

## Hard boundaries

Do NOT:
- deploy to mazhor/burzh;
- SSH for mutation;
- create users/groups;
- modify ACL/permissions;
- install packages/services;
- change firewall/systemd;
- provision/read credentials;
- enable WRITE;
- expose listener;
- mutate repository/archive/shard content.

Read-only code/artifact inspection and local/synthetic test rerun are permitted.

## Expected terminal result

Return exactly one:

`PASS_SIS_SHARD_GATEWAY_ADAPTER_R01_INDEPENDENT_VERIFY`

or

`REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`

or exact blocker/fail.

Terminal result must include:
- exact immutable candidate identity;
- test rerun summary;
- any deviations from SIS plan;
- explicit deployment/host mutation/credential access = 0;
- whether ARH preservation-boundary review may proceed on unchanged bytes.

Address result to KOO and KOD.
Stop after terminal result.
