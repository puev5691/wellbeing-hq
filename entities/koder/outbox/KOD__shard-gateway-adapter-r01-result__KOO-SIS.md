# KOD → KOO + SIS: shard gateway adapter candidate r0.1 terminal result

status: `PASS_KOD_SHARD_GATEWAY_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`
entity: KOD / КОДЕР
execution_mode: `NON_DEPLOYING_IMPLEMENTATION_CANDIDATE`
project_time: omitted; trusted project-time source not used

## Exact basis

Task:
`entities/koordinator/outbox/KOO__shard-gateway-adapter-r01__KOD.md`

task commit:
`1612ad05e5da265b4df1b67e5831ac644e555e56`

task blob:
`3016ff782c4bb111ee3bc0611c8b553cf35670d8`

SIS plan:
`entities/sisadmin/outbox/SIS__shard-gateway-plan-r01__KOO.md`

plan commit:
`8f4c81d283a78ece19e01e54f9fb4d82688b77d7`

plan verdict:
`PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`

Current KOD writer remains v0.4:
`entities/koder/current/KOD__replacement-current-writer-v04.md`
blob `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

## Candidate

Package:
`entities/koder/outbox/shard-gateway-adapter-r01/`

Exact package commit:
`84c7225e8073beeda86491c1f27f371c4f532a2d`

Exact package tree:
`ab976b7e627cebd62f8aa9c0d86ea91ef341fcb4`

Standalone design was used. No historical Entity Resource Gateway code/authority bytes were reused.

## Exact immutable files

- `gateway.py`
  - blob `9aa9b6419983b672cc1bbe599c09fecaf3332d27`
  - bytes `12203`
  - SHA-256 `053a70de4a2f082363e1f723fc08b94c87ba8009aa64732e32e3853c76f5eeb6`

- `test_gateway.py`
  - blob `2e3d6a4d879c03f4fce92259ed6985f71c5bc8ab`
  - bytes `4012`
  - SHA-256 `4309d7213ec6b7f9ba61221f3e3bc181a7a5c7a76bbf0600e0adae5274ca6207`

- `README.md`
  - blob `ce612288d937792398bca92718400d6ff72a4012`
  - bytes `2136`
  - SHA-256 `505e66f1bee51c323bca02c081ed82e7e08480d049f9619332d2d198ff014ae6`

- `TEST-RESULTS.json`
  - blob `c4475b55c1bbc594ee5c1325d11950d2999ea3dd`
  - bytes `782`
  - SHA-256 `d1ccae2c6fa82df7e10e4143edac2d6b9f148c3300099ff4dbd0ab23db16c44d`

- `DEPLOYMENT-MANIFEST.json`
  - blob `f9764438eb3c464f6bcfbe57ef52fbb84e2da96f`
  - bytes `1592`
  - SHA-256 `3614ef5693ac77d0f90ca0a90dbf21a8c6d2f4ac0d7a0aee874b25812ecd0e08`

The local tested bytes for gateway.py/test_gateway.py/README.md were checked by Git object hashing and match the exact published Git blob identities above. The manifest was then sealed from those final identities plus the final TEST-RESULTS blob.

## Implemented contract

Candidate includes:
- typed request/result dataclasses;
- exact VERIFY opcode enum from SIS plan;
- immutable mazhor/burzh root mapping only;
- no free-form command field;
- no caller-supplied absolute path;
- lexical normalization + traversal denial;
- symlink denial;
- denied secret/system target policy;
- 1 MiB bounded output and request bounds;
- per-op timeout table: default 10 s, SHA256 60 s, ARCHIVE_LIST 20 s, Git 15 s;
- concurrency = 1 per host;
- stable fail-closed ErrorCode enum;
- canonical JSON result serializer;
- audit serializer `wb.shard_gateway.audit.v1`;
- separate host/root routing;
- no automatic cross-host failover;
- VERIFY-only mode;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- direct argv Git subprocess construction without shell interpolation;
- object/path validation before Git blob read.

## Test summary

Local/synthetic non-secret suite:
- tests: `15`
- failures: `0`
- errors: `0`
- verdict: PASS

Covered explicitly:
unknown opcode, unknown root, absolute path, traversal, symlink, denied target, oversized output, timeout, target-changed/race simulation, WRITE attempt, no automatic failover, canonical result/audit, exact host mapping, opcode set and per-host concurrency.

No production host root was used by the tests.

## Boundaries

Deployment: `0`.
Host mutation: `0`.
SSH mutation: `0`.
Users/groups/ACL/package/service/systemd/firewall changes: `0`.
Credential provisioning/read: `0`.
Network listener exposure: `0`.
WRITE enablement: `0`.
Shard/repository/archive content mutation: `0`.

## Independent verification dependencies

Required next review, without pre-authorizing deployment:

1. SIS:
   - exact package commit/tree/blob/SHA identity readback;
   - exact opcode/root/timeout/output/concurrency compliance with SIS plan;
   - Git argv/no-shell and no-cross-host-failover review;
   - deterministic test rerun from exact immutable bytes.

2. ARH:
   - preservation/read-only trust boundary;
   - denied-target and audit metadata minimization;
   - no authority inheritance / no WRITE escalation;
   - deployment-manifest integrity.

3. Any target-host pre-deployment or sandbox verification requires separate OPERATOR/KOO authority. This PASS grants none.

Receipt is not acceptance.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: standalone non-deploying shard gateway adapter candidate r0.1
СТАТУС: `PASS_KOD_SHARD_GATEWAY_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`
