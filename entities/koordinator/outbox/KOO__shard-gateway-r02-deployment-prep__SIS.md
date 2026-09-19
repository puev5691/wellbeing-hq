# KOO → SIS: shard gateway adapter r0.2 bounded deployment preparation

status: TASK
execution_mode: BOUNDED_DESIGN_DEPLOYMENT_PREPARATION
deployment_authority: no
host_mutation_authority: no
credential_authority: no
production_acceptance_authority: no
project_time: omitted; trusted project-time source not used

## Current authority

SIS current-writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`

writer establishment commit:
`3ca813a7addb711eb8bf2e017b39517268fa31f0`

writer blob:
`03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

SIS must fresh-verify current-writer and task state before preparation.

## Exact causal chain

KOD corrected candidate:
commit `4fdee73d0d37befc59fb3dd568645569ecc2fa2d`
verdict `PASS_KOD_SHARD_GATEWAY_ADAPTER_R02_READY_FOR_SIS_REVERIFY`.

SIS independent reverify:
`entities/sisadmin/outbox/SIS__shard-gateway-adapter-r02-independent-reverify__KOO-KOD.md`
commit `ed56678fb190c278440aa2bcfa83a258d54daf27`
blob `2dac3107c021deecd409715258bfe39808e2ef3b`
verdict `PASS_SIS_SHARD_GATEWAY_ADAPTER_R02_INDEPENDENT_REVERIFY`.

ARH preservation/read-only review:
`entities/archivarius/outbox/ARH__shard-gateway-adapter-r02-preservation-review__KOO.md`
commit `36b1c3c5c823358e9e32a14a9102d556be431265`
verdict `PASS_ARH_SHARD_GATEWAY_ADAPTER_R02_PRESERVATION_BOUNDARY`.

ARH boundary:
unchanged r0.2 bytes may proceed only to the next bounded design/deployment-preparation gate.
ARH PASS does not create deployment, host-mutation, credential or production-acceptance authority.

## Exact immutable r0.2 candidate

Locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

Boundary commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`

Composition:
exactly 5 files.

No code changes are authorized in this task.
If the deployment-preparation design reveals a code defect, return exact blocker to KOO/KOD instead of editing the candidate.

## Existing SIS infrastructure design basis

Use the existing read-only SIS plan as the baseline:

`entities/sisadmin/outbox/SIS__shard-gateway-plan-r01__KOO.md`
commit `8f4c81d283a78ece19e01e54f9fb4d82688b77d7`
verdict `PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`.

Preserve its confirmed scope:

Primary:
`mazhor`

Fallback:
`burzh`

Deferred:
`erefia`

Read-only service identity:
`arh-preserve`

Future WRITE identity:
`shard-write`
reserved only, not created or enabled.

Root mappings:

- `MAZHOR_REPO_WELLBEING_HQ`
  → `/data/wellbeing-lab/repos/wellbeing-hq`

- `MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01`
  → `/data/wellbeing-lab/backups/shd-pre-reinit-v01`

- `BURZH_REPO_WELLBEING_HQ`
  → `/home/pev5691/wellbeing-hq`

No burzh archive root.
No erefia mapping.

## Goal

Prepare an implementation-ready **deployment-preparation package** for future human-authorized deployment of the exact immutable r0.2 adapter.

This task ends before any host mutation.

The package must make the future mutation gate explicit and executable without rediscovering architecture.

## Required preparation outputs

Create one bounded package under:

`entities/sisadmin/outbox/shard-gateway-r02-deployment-prep/`

Include at least:

### 1. DEPLOYMENT-PLAN.md

Specify:
- primary deployment target mazhor;
- fallback deployment target burzh as a separate future step, not automatic failover;
- erefia deferred;
- exact immutable adapter locator/commit/tree;
- artifact-to-host placement mapping;
- service identity model `arh-preserve`;
- explicit stable WorkingDirectory;
- runtime executable/config paths proposed for each host;
- audit sink path proposed for each host;
- read-only filesystem access model;
- no WRITE entrypoint;
- no listener exposure unless a later explicit design/authority requires one;
- startup/supervisor model proposal;
- preflight, install, verify, rollback stages;
- future production-acceptance criteria.

Do not silently invent an existing host path.
Any proposed new directory must be marked:
`PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`.

### 2. PERMISSIONS-MATRIX.md

For each host and path identify:
- service identity;
- required read/traverse permissions;
- explicitly forbidden write/credential/admin access;
- whether permission change is required;
- whether current state is verified or still unknown.

No ACL/chmod/chown operation may be executed.

### 3. SERVICE-UNIT-CANDIDATE.md or equivalent candidate config

Prepare a non-installed candidate supervisor/systemd definition showing:
- exact ExecStart command/argv;
- explicit WorkingDirectory;
- explicit minimal environment;
- no inherited credential environment;
- service user `arh-preserve`;
- restart/failure behavior appropriate for fail-closed read-only service;
- resource/concurrency limits consistent with SIS plan;
- no WRITE mode;
- no network listener unless exact future design requires it.

This is a design artifact only.

### 4. AUDIT-RETENTION-PLAN.md

Define future append-only audit handling for:
`wb.shard_gateway.audit.v1`

Without creating directories or files on hosts.

Specify:
- proposed audit path;
- ownership/access boundary;
- retention/rotation proposal;
- digest/provenance relation;
- no raw file contents or credentials;
- failure behavior if audit sink unavailable.

### 5. CREDENTIAL-BOUNDARY.md

No credential values.

Define only:
- whether future runtime needs any credential at all for each access mode;
- which credential class would be required if unavoidable;
- who must provision it;
- where it must NOT be stored;
- how the service proves credential absence for local read-only mode;
- explicit statement that this prep package contains no secret material.

### 6. PREDEPLOY-CHECKLIST.md

Create exact pre-deployment checks:
- immutable package identity/readback;
- host identity;
- root existence;
- root ownership/mode observation;
- stale-cwd condition;
- required runtime availability;
- proposed service account absence/presence;
- target directories absence/presence;
- audit destination readiness;
- no conflicting service/listener;
- rollback prerequisites;
- no secret-bearing env;
- exact authority references for every future mutation.

Read-only observation commands may be proposed.
Do not execute mutation commands.

### 7. MUTATION-AUTHORITY-GATE.md

Enumerate every future host mutation requiring explicit OPERATOR authority, aligned with the original SIS plan section 13, including at least:

1. create system user/group `arh-preserve`;
2. any ownership/ACL/mode change;
3. create executable/config directories;
4. install runtime/package/files;
5. create supervisor/systemd unit/socket/timer;
6. configure SSH forced-command/authorized_keys if used;
7. firewall changes if any;
8. create audit directory/retention permissions;
9. bind mount/namespace/chroot/container/sandbox setup if proposed;
10. listener/socket exposure;
11. credential provisioning;
12. any future WRITE identity/mode;
13. fallback/replication activation.

For each item state:
- required/not required under proposed design;
- target host;
- exact object/path/service;
- rollback action;
- verification evidence required after mutation.

This file must be usable by KOO to form one exact OPERATOR decision gate later.

### 8. DEPLOYMENT-PREP-MANIFEST.json or .md

Record:
- exact r0.2 package identity;
- exact preparation artifacts;
- hashes/blobs after publication;
- deployment performed = 0;
- host mutation = 0;
- credential access = 0;
- production acceptance = 0.

## Read-only verification permitted

SIS may use already-available verified information-field evidence.

If current host facts materially affect the plan and a read-only host inspection tool is available, SIS may perform bounded read-only checks only.

No write, installation, user/group creation, permission change, service change, firewall change, credential access or listener exposure is permitted.

If a required fact cannot be verified read-only:
mark it `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`.
Do not guess.

## Hard boundaries

Do NOT:
- deploy r0.2;
- copy/install files to target hosts;
- create `arh-preserve` or `shard-write`;
- change ownership/ACL/mode/group membership;
- create directories on target hosts;
- install packages/runtime;
- create/modify systemd/service/supervisor state;
- change firewall/SSH;
- read/provision credentials;
- expose listener/socket;
- enable WRITE;
- mutate repositories/archives/shard data;
- claim production acceptance.

## Expected terminal result

Return exactly one:

`PASS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP_READY_FOR_OPERATOR_GATE`

or

`REQUIRES_EDITS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP`

or exact blocker/fail.

Terminal result must include:
- exact unchanged r0.2 identity;
- exact deployment-prep package locator/identity;
- summary of proposed primary/fallback deployment architecture;
- list of UNKNOWN predeploy facts;
- exact future mutation classes requiring OPERATOR decision;
- deployment/host mutation/credential access/production acceptance = 0;
- recommendation for the next causal gate only, without performing it.

Address terminal result to KOO.
Stop after terminal result.
