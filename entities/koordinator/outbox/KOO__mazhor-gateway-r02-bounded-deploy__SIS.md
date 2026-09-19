# KOO → SIS: execute bounded mazhor shard gateway r0.2 VERIFY deployment

status: TASK
execution_mode: BOUNDED_MAZHOR_VERIFY_DEPLOYMENT
production_acceptance_authority: no
credential_authority: no
write_authority: no
burzh_authority: no
erefia_authority: no
project_time: omitted; trusted project-time source not used

## Current authority

SIS current-writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`

writer establishment commit:
`3ca813a7addb711eb8bf2e017b39517268fa31f0`

writer blob:
`03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

SIS must fresh-verify current-writer and exact task/authority before any host mutation.

## Exact OPERATOR authority

Authority record:
`entities/koordinator/current/KOO__mazhor-gateway-r02-deployment-authority.md`

authority commit:
`0aadf1753e442ff792b2d43f402ad47ebeb984ee`

Decision:
`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

Decision gate:
`entities/koordinator/outbox/KOO__shard-gateway-r02-mutation-decision__OPERATOR.md`
commit `43123b47f3ff8351820251a2dbd694b46c0e4d32`.

No authority outside the selected OPTION A scope may be inferred.

## Exact reviewed runtime basis

### Adapter r0.2

Locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`

Runtime file:
`gateway.py`
blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`.

### Harness r0.2

Locator:
`puev5691/wellbeing-hq@01c4f6a336d0ca6d9000d42e5966c4e924f82bbd:entities/koder/outbox/shard-gateway-verify-harness-r02`

Package tree:
`ab364437494c51cd0ef25bc8dbb1b426d8d4ccf3`

Required runtime files:
- `harness.py`
  blob `e94bf8dd0ed78dc53a1b1d6057e213584ae9ace4`
  SHA-256 `69ccf13cb0856e498eb8fea78376a04a5dbb70051fe2e9453d843b38641b6762`;
- `audit_sink.py`
  blob `763d4ae4945e946878a52098ba87df379f4f6762`
  SHA-256 `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;
- `INVOCATION.json`
  blob `193e6cb2c220cb8ed0c0fd73c99e2c98926c12a4`
  SHA-256 `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

SIS exact-byte/process rereview:
`ed2974f0f03c12e3dc8dd1364ef6436ad1785bb7`
verdict `PASS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R02_DEPLOYMENT_PREP_REREVIEW`.

## Exact target

Host:
`mazhor` / Remote Desktop Commander device `p552203.kvmvps`.

Existing allowed read-only roots:
- repo `/data/wellbeing-lab/repos/wellbeing-hq`;
- archive `/data/wellbeing-lab/backups/shd-pre-reinit-v01`.

Selected runtime layout:
`/opt/wb-shard-gateway/`.

No mutation on burzh or erefia.

## Phase 0 — fresh predeploy read-only checks

Before mutation, verify and record:
- exact host identity;
- OS/Python/systemd availability;
- exact repo/archive roots exist;
- no conflicting `wellbeing-shard-gateway-verify.service`;
- no conflicting gateway listener/socket;
- current absence/presence of `arh-preserve`;
- current absence/presence of exact deployment paths;
- no secret-bearing environment requirement;
- exact immutable source bytes are retrievable from GitHub.

If a material precondition differs from the reviewed basis and changes safety/rollback:
STOP and return exact blocker before mutation.

## Phase 1 — create bounded service identity

Create only:
`arh-preserve`

Required:
- system service identity;
- no sudo/admin groups;
- no interactive login shell;
- no credential material.

Record uid/gid/groups/shell.

Do not create `shard-write`.

## Phase 2 — mandatory read-only access gate

After identity creation, verify as `arh-preserve` effective read/traverse access to:

- `/data/wellbeing-lab/repos/wellbeing-hq`;
- `/data/wellbeing-lab/backups/shd-pre-reinit-v01`.

This check must not mutate those roots.

If required access is insufficient:
- STOP immediately;
- do NOT chmod/chown/setfacl/change group on existing repo/archive roots;
- do NOT proceed to runtime installation;
- return exact blocker;
- keep any already-created deployment-only state reversible and document it.

## Phase 3 — create only authorized deployment paths

Only after Phase 2 PASS, create:

- `/opt/wb-shard-gateway`;
- `/run/wb-shard-gateway`;
- `/var/lib/wellbeing/shard-gateway`;
- `/var/log/wb-shard-gateway`.

Set ownership/modes only on these newly created gateway-specific paths as needed for the bounded design.
Do not modify existing repo/archive root ownership/modes/ACLs.

## Phase 4 — install exact immutable runtime bytes

Install only:

`/opt/wb-shard-gateway/gateway.py`
from exact adapter blob/SHA above;

`/opt/wb-shard-gateway/harness.py`
from exact harness blob/SHA above;

`/opt/wb-shard-gateway/audit_sink.py`
from exact harness blob/SHA above;

`/opt/wb-shard-gateway/INVOCATION.json`
from exact harness blob/SHA above.

After installation, recompute SHA-256 from host bytes.
Require exact 4/4 match before any execution.

If mismatch:
rollback bounded installed state and return exact blocker.

## Phase 5 — exact unit candidate before installation

Before writing unit to systemd:

1. create exact unit candidate as a project artifact in HQ;
2. read it back;
3. prove its ExecStart argv is mechanically equivalent to the production template in exact installed `INVOCATION.json`.

Unit name:
`wellbeing-shard-gateway-verify.service`

Required properties:
- `Type=oneshot`;
- `User=arh-preserve`;
- `Group=arh-preserve`;
- `WorkingDirectory=/var/lib/wellbeing/shard-gateway`;
- environment exactly/minimally:
  `PATH=/usr/bin:/bin`
  `LC_ALL=C`;
- ExecStart argv-equivalent to:
  `/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --audit-module /opt/wb-shard-gateway/audit_sink.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`;
- no listener/socket;
- no WRITE;
- no credential environment;
- not enabled for boot.

If exact equivalence cannot be proven:
STOP before unit installation.

## Phase 6 — install bounded oneshot unit

Only after unit artifact/readback/equivalence PASS:
- install exact unit;
- daemon-reload as required;
- do not enable it for boot;
- do not create timer/socket;
- verify disabled/not-enabled state before smoke.

## Phase 7 — synthetic non-secret smoke input

Create exactly one bounded synthetic non-secret VERIFY request at:
`/run/wb-shard-gateway/request.json`.

The request must target an allowed read-only operation/object that does not expose private/secret content and does not mutate repo/archive/shard state.

Record request hash and intended expected result before service execution.

## Phase 8 — audit sink

Prepare:
`/var/log/wb-shard-gateway/audit.jsonl`

under the verified harness local append+fsync fail-closed contract.

No credentials or raw secret-bearing payloads may be written.

Record pre-smoke audit state.

## Phase 9 — one bounded systemd VERIFY smoke

Run exactly one smoke via:
`wellbeing-shard-gateway-verify.service`.

Automatic retries:
`0`.

If service fails:
do not run a second automatic smoke.
Capture bounded evidence and enter rollback/blocker flow.

## Phase 10 — mandatory post-smoke verification

Verify and record:
- unit executed under `arh-preserve`;
- exact installed hashes remain 4/4;
- canonical result exists and matches expected bounded operation semantics;
- exact audit delta is consistent with one execution attempt;
- audit schema `wb.shard_gateway.audit.v1`;
- credential access = 0;
- network listener exposure = 0;
- outbound network by gateway = 0 as far as bounded evidence can establish;
- WRITE remains not enabled;
- repository/archive/shard mutation = 0;
- unit remains disabled/not enabled;
- no timer/socket/persistent standing service introduced.

Do not call this production acceptance.

## Rollback conditions

Rollback if:
- immutable readback mismatch;
- unit equivalence failure after any mutation requiring rollback;
- smoke failure;
- audit fail-closed failure;
- unexpected credential/network/WRITE behavior;
- unexpected repo/archive/shard mutation;
- unexpected standing service state.

Rollback only the bounded deployment state:
- stop new unit if active;
- disable if somehow enabled;
- remove exact unit;
- daemon-reload;
- remove exact installed gateway runtime files;
- remove synthetic request;
- remove gateway-specific directories only if empty/safe;
- remove `arh-preserve` only if no required owned state remains;
- leave repo/archive roots untouched.

Record rollback verification.

## Explicitly forbidden

- any burzh mutation;
- any erefia action;
- chmod/chown/ACL/group changes to existing repo/archive roots;
- credential read/provisioning;
- SSH forced-command changes;
- firewall changes;
- listener/socket exposure;
- WRITE/shard-write;
- automatic failover/replication;
- repo/archive/shard write;
- boot enablement or standing service use;
- production acceptance.

## Required terminal result

Return exactly one:

`PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

or

`BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: <exact blocker>`

or

`ROLLED_BACK_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: <exact reason>`

or exact FAIL.

Terminal result must include:
- OPERATOR authority commit;
- host identity;
- exact installed runtime hashes;
- exact unit artifact locator/identity;
- read-only access-gate result;
- smoke request hash;
- service execution result/exit;
- audit delta/result;
- unit enablement state;
- credential/network/WRITE/repo-mutation accounting;
- rollback evidence if applicable;
- explicit statement: production acceptance not granted.

Address terminal result to KOO.
Stop after terminal result.
