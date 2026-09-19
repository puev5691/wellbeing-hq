# KOO → OPERATOR: shard gateway r0.2 primary mutation/deployment decision gate

status: OPERATOR_DECISION_REQUIRED
decision_executes_mutation: no
deployment_authority_before_decision: no
host_mutation_authority_before_decision: no
credential_authority: no
production_acceptance_authority: no
project_time: omitted; trusted project-time source not used

## Why this gate exists

The implementation/review chain is complete enough to ask for a bounded first host deployment decision.

Exact SIS terminal PASS:
`entities/sisadmin/outbox/SIS__shard-gateway-verify-harness-r02-deployment-prep-rereview__KOO-KOD.md`
commit `ed2974f0f03c12e3dc8dd1364ef6436ad1785bb7`
verdict `PASS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R02_DEPLOYMENT_PREP_REREVIEW`.

This PASS closes the previous execution-harness blocker.
It does not itself authorize mutation or deployment.

## Exact immutable runtime basis

### Adapter r0.2

Locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`

Runtime adapter:
`gateway.py`
blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`.

### VERIFY harness r0.2

Locator:
`puev5691/wellbeing-hq@01c4f6a336d0ca6d9000d42e5966c4e924f82bbd:entities/koder/outbox/shard-gateway-verify-harness-r02`

Package tree:
`ab364437494c51cd0ef25bc8dbb1b426d8d4ccf3`

Exact runtime files:

- `harness.py`
  blob `e94bf8dd0ed78dc53a1b1d6057e213584ae9ace4`
  SHA-256 `69ccf13cb0856e498eb8fea78376a04a5dbb70051fe2e9453d843b38641b6762`;

- `audit_sink.py`
  blob `763d4ae4945e946878a52098ba87df379f4f6762`
  SHA-256 `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;

- `INVOCATION.json`
  blob `193e6cb2c220cb8ed0c0fd73c99e2c98926c12a4`
  SHA-256 `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

SIS independently verified exact harness composition 8/8 and process-level supervisor invocation under `python3 -I -B`.

## Exact reviewed supervisor invocation

Canonical tested argv from `INVOCATION.json`:

`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --audit-module /opt/wb-shard-gateway/audit_sink.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

Minimal environment:
- `PATH=/usr/bin:/bin`;
- `LC_ALL=C`.

Harness import correctness does not depend on cwd.

## Layout conflict resolved only by OPERATOR choice

Historical SIS deployment-prep proposed:
`/opt/wellbeing/shard-gateway/r02/`.

The independently process-tested harness r0.2 contract uses:
`/opt/wb-shard-gateway/`.

KOO does not silently normalize these two layouts.

OPTION A below explicitly selects the **process-tested harness r0.2 layout** as the canonical first-deployment layout.

Choosing the historical layout instead requires a new invocation regeneration/re-test before any host mutation.

## First deployment target

Primary target only:
`mazhor` / host `p552203.kvmvps`.

Verified read-only roots remain:
- repository: `/data/wellbeing-lab/repos/wellbeing-hq`;
- archive: `/data/wellbeing-lab/backups/shd-pre-reinit-v01`.

Fallback `burzh` is NOT included in this decision.
`erefia` remains deferred.

## OPTION A — authorize bounded mazhor VERIFY deployment stage

Decision text:

`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

This explicitly selects:
`/opt/wb-shard-gateway/`
as the canonical runtime layout for this first deployment because it is the exact process-tested harness r0.2 invocation layout.

### Authorized mutations on mazhor only

1. Create system identity:
   `arh-preserve`
   with:
   - no sudo/admin groups;
   - no interactive login shell;
   - no credential material.

2. Create only these new gateway paths:
   - `/opt/wb-shard-gateway`;
   - `/run/wb-shard-gateway`;
   - `/var/lib/wellbeing/shard-gateway`;
   - `/var/log/wb-shard-gateway`.

3. Install only exact immutable runtime bytes:
   - adapter r0.2 `gateway.py`;
   - harness r0.2 `harness.py`;
   - harness r0.2 `audit_sink.py`;
   - harness r0.2 `INVOCATION.json`.

   Exact byte/hash readback is mandatory before execution.

4. Prepare one exact local systemd oneshot unit candidate:

   unit name:
   `wellbeing-shard-gateway-verify.service`

   required properties:
   - `Type=oneshot`;
   - `User=arh-preserve`;
   - `Group=arh-preserve`;
   - `WorkingDirectory=/var/lib/wellbeing/shard-gateway`;
   - minimal environment only:
     `PATH=/usr/bin:/bin`,
     `LC_ALL=C`;
   - ExecStart must be argv-equivalent to the exact tested `INVOCATION.json` production contract above;
   - no listener/socket;
   - no WRITE;
   - no credential environment;
   - not enabled for boot.

   Before installation, SIS must publish/read back the exact unit candidate as a project artifact and prove ExecStart equivalence to `INVOCATION.json`.

5. Create a bounded synthetic non-secret request file only for deployment verification at:
   `/run/wb-shard-gateway/request.json`.

6. Create/use local append-only audit sink:
   `/var/log/wb-shard-gateway/audit.jsonl`
   under the verified harness fail-closed audit contract.

7. Run one bounded local VERIFY smoke through the installed oneshot unit.

8. Verify after the smoke:
   - exact installed hashes;
   - service executed under `arh-preserve`;
   - canonical result;
   - exactly one expected audit event for the smoke;
   - no credential access;
   - no listener/network exposure;
   - WRITE remains rejected;
   - repositories/archives were not mutated;
   - unit remains disabled/not persistent after smoke.

### Explicitly NOT authorized by OPTION A

- any deployment or mutation on `burzh`;
- any action on `erefia`;
- chmod/chown/ACL/group changes on the existing repository or archive roots;
- any WRITE identity or `shard-write`;
- credential provisioning/read;
- SSH forced-command changes;
- firewall changes;
- listener/socket exposure;
- automatic failover/replication;
- repository/archive/shard writes;
- production acceptance;
- enabling the unit for boot or standing service use.

### Fail-closed predeploy condition

After `arh-preserve` exists, SIS must verify its effective read/traverse access to the exact mazhor repo/archive roots without changing those roots.

If required read-only access is insufficient:
- STOP;
- do not chmod/chown/ACL existing roots;
- report exact blocker to KOO;
- leave only mutations already explicitly created by this authority in a reversible state.

### Rollback

If install/readback/smoke fails:

- stop the new unit if running;
- disable it if any enabled state was accidentally introduced;
- remove only the exact new unit;
- daemon-reload if the unit was installed;
- remove only the exact installed gateway runtime files;
- remove synthetic request;
- remove new gateway directories only when empty/safe;
- remove `arh-preserve` only if no required owned state remains;
- leave repo/archive roots untouched;
- record exact rollback verification.

A successful bounded smoke does NOT equal production acceptance.
After PASS, KOO must fresh-reconcile and form a separate production/standing-use gate if needed.

## OPTION B — keep tested bytes, require layout normalization before mutation

Decision text:

`DEFER_MUTATION_REQUIRE_FINAL_LAYOUT_NORMALIZATION`

Effect:
- no host mutation;
- KOO routes SIS/KOD to reconcile the historical prep path
  `/opt/wellbeing/shard-gateway/r02/`
  with tested harness path
  `/opt/wb-shard-gateway/`;
- regenerated exact deployment/unit artifacts must be independently checked before a new OPERATOR mutation gate.

## OPTION C — defer deployment

Decision text:

`DEFER_SHARD_GATEWAY_R02_DEPLOYMENT`

Effect:
- no host mutation;
- immutable adapter/harness/prep artifacts remain preserved and ready;
- no further deployment action until a new explicit OPERATOR decision.

## OPTION D — reject current deployment design

Decision text:

`REJECT_SHARD_GATEWAY_R02_DEPLOYMENT_DESIGN: <exact reason>`

Effect:
- no host mutation;
- KOO routes only the stated design correction;
- already verified immutable adapter/harness bytes remain provenance unless the exact reason requires code changes.

## Boundary

This decision gate itself performs zero host mutations.

Until OPERATOR chooses OPTION A explicitly:
- deployment = 0;
- host mutation = 0;
- credential access = 0;
- WRITE = 0;
- listener exposure = 0;
- production acceptance = 0.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: exact human mutation/deployment decision after adapter+harness+SIS review chain PASS
СТАТУС: OPERATOR_DECISION_REQUIRED
