# SIS → KOO: mazhor shard gateway bounded VERIFY deployment resumed from Phase 2 Git runtime subgate

verdict: `PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`
resume_point: `RESUME_FROM_PHASE_2_GIT_RUNTIME_SUBGATE`
successor_runtime: `adapter r0.3 + harness r0.3`
production_acceptance: no
project_time: omitted; trusted project-time source not used

## Resume authority and continuity

OPERATOR instruction:
continue from fixed point
`RESUME_FROM_PHASE_2_GIT_RUNTIME_SUBGATE`
using KOD terminal result
`c3399397cbaf48230213bf0d189109b2456ab352`.

Existing bounded deployment authority remains:
`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

Authority record commit:
`0aadf1753e442ff792b2d43f402ad47ebeb984ee`.

Target continuity:
`mazhor / p552203.kvmvps`.

Existing service identity retained:
`arh-preserve`
uid `999`, gid `988`, group `arh-preserve` only, shell `/usr/sbin/nologin`.

No Phase 0/Phase 1 mutation was replayed.

## Exact successor runtime basis

KOD terminal:
`entities/koder/outbox/KOD__gateway-r03-git-safe-directory-result__KOO-SIS.md`
commit `c3399397cbaf48230213bf0d189109b2456ab352`
verdict `PASS_KOD_SHARD_GATEWAY_R03_GIT_SAFE_DIRECTORY_READY_FOR_SIS_RESUME`.

Adapter r0.3:
- package commit `9140d2ffe2b2ab983ce4a607447b5cc20f44ec6f`;
- package tree `d38d28d490252030b9a6264e9248dd1a4db26af1`;
- runtime `gateway.py`;
- blob `d42e58060365c4b996bf87c81f3e3eb2ad684ceb`;
- SHA-256 `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`.

Harness r0.3:
- package commit `1f4c8218734ccb2e081e491b92195bf7bedaf1d8`;
- package tree `b6980de1194a7caae528e5c485e14941e07f3fef`;
- `harness.py` SHA-256 `6dbf10acd41105e2491262d6745f4ac9574742ca6a11eb09f933dcaf80ec4465`;
- `audit_sink.py` SHA-256 `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;
- `INVOCATION.json` SHA-256 `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

## Phase 2 Git runtime subgate

POSIX reconfirmation under existing `arh-preserve`:
- repo read/traverse: PASS;
- archive read/traverse: PASS.

Real different-owner Git read under `arh-preserve` using the exact command-scoped correction:

`git -c safe.directory=/data/wellbeing-lab/repos/wellbeing-hq -C /data/wellbeing-lab/repos/wellbeing-hq rev-parse HEAD`

Result:
`22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`
exit `0`.

Git status using the same command-scoped safe.directory policy:
exit `0`;
tracked status output: empty.

Persistent config/environment expansion check:
- no service-user global `safe.directory` entry: PASS;
- `/nonexistent/.gitconfig` absent: PASS;
- no `GIT_CONFIG_*` environment expansion: PASS;
- service runtime environment remains `PATH=/usr/bin:/bin`, `LC_ALL=C`.

Phase 2 Git runtime subgate:
`PASS`.

## Phase 3 gateway-specific paths

Created only:
- `/opt/wb-shard-gateway` mode 0755 root:root;
- `/run/wb-shard-gateway` mode 0700 arh-preserve:arh-preserve;
- `/var/lib/wellbeing/shard-gateway` mode 0700 arh-preserve:arh-preserve;
- `/var/log/wb-shard-gateway` mode 0700 arh-preserve:arh-preserve.

Existing repo/archive ownership/mode/ACL were not changed.

## Phase 4 exact immutable runtime install

Installed:
- `/opt/wb-shard-gateway/gateway.py`;
- `/opt/wb-shard-gateway/harness.py`;
- `/opt/wb-shard-gateway/audit_sink.py`;
- `/opt/wb-shard-gateway/INVOCATION.json`.

Post-install SHA-256:
- gateway.py `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`;
- harness.py `6dbf10acd41105e2491262d6745f4ac9574742ca6a11eb09f933dcaf80ec4465`;
- audit_sink.py `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;
- INVOCATION.json `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`.

Result:
`4/4 exact match`.

## Phase 5 exact unit artifact and argv equivalence

Published unit candidate:

`entities/sisadmin/outbox/mazhor-gateway-r03-deploy/SIS__wellbeing-shard-gateway-verify.service`

artifact commit:
`f5316cacccdae55c8fefab9f27d164dec7cb0f7e`

artifact blob:
`505cbbb6a155efe3c4c59073ddc8f79001e65313`.

Readback: PASS.

Mechanical comparison of unit `ExecStart` argv with installed exact `INVOCATION.json production`:
`EXECSTART_EQUIVALENT=True`.

Exact ExecStart:
`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --audit-module /opt/wb-shard-gateway/audit_sink.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`.

## Phase 6 systemd oneshot install

Installed exact unit:
`/etc/systemd/system/wellbeing-shard-gateway-verify.service`.

Installed Git blob identity:
`505cbbb6a155efe3c4c59073ddc8f79001e65313`
exact match to project artifact.

Verified before smoke:
- Type=oneshot;
- User=arh-preserve;
- Group=arh-preserve;
- WorkingDirectory=/var/lib/wellbeing/shard-gateway;
- Environment=PATH=/usr/bin:/bin LC_ALL=C;
- enabled state: `disabled`;
- active state: `inactive`;
- no timer/socket created.

## Phase 7 synthetic request

Created exactly one non-secret request:
`/run/wb-shard-gateway/request.json`.

Operation:
`GIT_HEAD`.

Root:
`MAZHOR_REPO_WELLBEING_HQ`.

Request SHA-256:
`e07c7a5e7220b8d8a6c144997fa3798c130c689c3b12466e08f16cd709cf0b39`.

Expected semantics before smoke:
- canonical `wb.shard_gateway.result.v1`;
- `ok=true`;
- operation `GIT_HEAD`;
- returned HEAD equal to current read-only Git HEAD;
- no repository mutation.

Pre-smoke HEAD:
`22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`.

## Phase 8 audit sink

Prepared:
`/var/log/wb-shard-gateway/audit.jsonl`
owned by `arh-preserve`, mode 0600.

Pre-smoke audit state:
empty / 0 records.

## Phase 9 exactly one smoke

Executed exactly once:
`systemctl start wellbeing-shard-gateway-verify.service`.

Automatic retries:
`0`.

systemctl start exit:
`0`.

systemd result:
- Result=success;
- ExecMainCode=0;
- ExecMainStatus=0;
- ActiveState=inactive;
- SubState=dead after oneshot completion.

Canonical result emitted:

- schema `wb.shard_gateway.result.v1`;
- ok `true`;
- operation `GIT_HEAD`;
- payload head `22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`;
- fallback_used `false`.

Result matched pre-smoke expected HEAD exactly.

## Phase 10 post-smoke verification

Audit:
- post-smoke record count: `1`;
- audit delta: `+1`;
- schema: `wb.shard_gateway.audit.v1`;
- request_id: `sis-mazhor-smoke-r03`;
- authority_ref: `0aadf1753e442ff792b2d43f402ad47ebeb984ee`;
- operation: `GIT_HEAD`;
- error_code: null;
- exit_status: 0;
- service_identity: `arh-preserve`.

systemd journal evidence includes process records with:
`_UID=999`
and the unit is configured with
`User=arh-preserve`, `Group=arh-preserve`.

Installed runtime hashes after smoke:
`4/4 exact match`.

Unit state after smoke:
- enabled: `disabled`;
- active: `inactive`;
- timer: not found;
- socket: not found;
- no standing service.

Network evidence:
- matching shard-gateway listener count after smoke: `0`;
- exact runtime has no listener/network dependency;
- smoke operation used local Git only;
- no gateway network expansion was configured.

Credential evidence:
- service environment is only the explicit minimal PATH/LC_ALL contract;
- no credential provisioning/read was performed;
- audit contains no credential/raw secret material.

WRITE:
- not enabled;
- `shard-write` not created.

Repository/archive:
- repo root remains `0775 shd:shd`;
- archive root remains `0775 shd:shd`;
- `arh-preserve` has no root write permission on either root;
- Git HEAD after smoke remains `22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`;
- tracked Git status remains clean;
- repository/archive/shard mutation observed: `0`.

## Rollback

Rollback not invoked because all resumed subgates and the single bounded smoke passed.

No automatic retry occurred.

## Accounting

mazhor bounded runtime install: `1`
smoke attempts: `1`
automatic retries: `0`
burzh mutation: `0`
erefia action: `0`
credential access/provisioning: `0`
listener exposure: `0`
WRITE enablement: `0`
repo/archive/shard mutation: `0`
boot enablement: `0`
standing service: `0`
production acceptance: `no`

## Next causal gate

Bounded mazhor VERIFY deployment succeeded.

This PASS does not authorize production/standing use, boot enablement, burzh deployment, WRITE, credentials, listener exposure or replication.

KOO must fresh-reconcile and decide the next separately authorized gate.

## Terminal result

`PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: resume and complete bounded mazhor shard gateway VERIFY deployment after Git safe.directory correction
СТАТУС: `PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`
