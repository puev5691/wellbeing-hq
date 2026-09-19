# KOO current active queue r0.56

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## OPERATOR deployment authority

Decision:
`AUTHORIZE_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`.

Authority record:
`entities/koordinator/current/KOO__mazhor-gateway-r02-deployment-authority.md`

authority commit:
`0aadf1753e442ff792b2d43f402ad47ebeb984ee`.

Decision gate:
`entities/koordinator/outbox/KOO__shard-gateway-r02-mutation-decision__OPERATOR.md`
commit `43123b47f3ff8351820251a2dbd694b46c0e4d32`.

Selected target:
`mazhor` / `p552203.kvmvps` only.

Selected runtime layout:
`/opt/wb-shard-gateway/`.

This authority excludes burzh/erefia, existing repo/archive permission mutations, credentials, listener exposure, WRITE, failover/replication, boot enablement and production acceptance.

## ACTIVE SLOT 1 — SIS / BOUNDED MAZHOR VERIFY DEPLOYMENT

Owner:
SIS / СИСАДМИН.

SIS current-writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`

writer establishment commit:
`3ca813a7addb711eb8bf2e017b39517268fa31f0`

writer blob:
`03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

Exact task:
`entities/koordinator/outbox/KOO__mazhor-gateway-r02-bounded-deploy__SIS.md`

task commit:
`d1e777e1e29e2847100808fb518884451824dcee`

task blob:
`a3b98d1afd25ddb8858496d7e87f0fc0dd2559f6`.

Dispatch:
`d5f9c682ac85d7f7732d53e8b384590c600b3d67`.

SIS inbox:
`526c1ff205ab07da102f96b1d635cbbcb789399a`.

Sender registry:
`3a53506f00fe9557e11281c8e2d30e9ebe627937`.

Automatic activation boundary:
`51f1948993ae5ebafa584a6c2a53e49ec93b10b6`.

activation_status:
`activation_failed`.

processing_started:
`no`.

operator_manual_ping_required:
`yes`.

State:
`AWAITING_OPERATOR_TRANSFER`.

## Exact runtime basis

Adapter:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

Harness:
`puev5691/wellbeing-hq@01c4f6a336d0ca6d9000d42e5966c4e924f82bbd:entities/koder/outbox/shard-gateway-verify-harness-r02`

SIS rereview PASS:
`ed2974f0f03c12e3dc8dd1364ef6436ad1785bb7`.

OPERATOR transfers activation PROMPT only.
SIS reads immutable runtime bytes directly from the information field.

## Mandatory phased execution

0. fresh read-only predeploy checks;
1. create `arh-preserve` only;
2. verify effective read/traverse access to exact mazhor repo/archive roots;
3. STOP if access insufficient; no chmod/chown/ACL on existing roots;
4. create only authorized gateway-specific paths;
5. install exact 4 runtime files and verify hashes 4/4;
6. publish/readback exact unit candidate and prove INVOCATION equivalence before systemd installation;
7. install oneshot unit, not enabled;
8. create one synthetic non-secret request and audit sink;
9. run exactly one VERIFY smoke, retries=0;
10. verify audit/hash/no-network/no-WRITE/no-repo-mutation/disabled state;
11. rollback on any bounded failure.

## Expected terminal

`PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT`

or

`BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: <exact blocker>`

or

`ROLLED_BACK_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: <exact reason>`

or exact FAIL.

A PASS is not production acceptance.

## EXACT NEXT CAUSAL STATE

`SIS_MAZHOR_GATEWAY_R02_BOUNDED_DEPLOYMENT_AWAITING_OPERATOR_ACTIVATION`

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: state after explicit OPERATOR mutation authority and exact SIS deployment routing
СТАТУС: CURRENT_QUEUE
