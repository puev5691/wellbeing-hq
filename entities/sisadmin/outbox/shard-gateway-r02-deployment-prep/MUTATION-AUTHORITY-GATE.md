# Mutation authority gate

status: DESIGN_ONLY

No item below is authorized by this document.

| Class | Required? | Host | Exact object | Rollback | Required verification |
|---|---|---|---|---|---|
| create `arh-preserve` | yes | mazhor, later burzh | system user/group | remove only if no owned state remains and authority permits | uid/gid/groups, no sudo, no login |
| ACL/chmod/chown/group | maybe | each target | exact approved roots + proposed dirs | restore captured pre-state | effective read/traverse, no write |
| create dirs | yes | each target | `/opt/wellbeing/shard-gateway/r02`, `/etc/wellbeing/shard-gateway`, `/var/lib/wellbeing/shard-gateway`, `/var/log/wellbeing/shard-gateway` | remove only exact empty/new dirs after service rollback | stat/owner/mode |
| install immutable adapter | yes | each target | `/opt/wellbeing/shard-gateway/r02/*` | remove exact installed files | byte/hash readback |
| install execution harness | yes, but BLOCKED | each target | exact future KOD harness | remove exact installed harness | independent immutable-byte PASS |
| systemd/supervisor | yes after harness | each target | proposed `wellbeing-shard-gateway-verify.service` | disable/remove exact unit and daemon-reload | unit identity, ExecStart, env, no listener/write |
| SSH forced command | not in baseline | none | none | n/a | requires separate design if introduced |
| firewall | not in baseline | none | none | n/a | only if a later listener is explicitly designed |
| audit dir/permissions | yes | each target | `/var/log/wellbeing/shard-gateway` + sink | restore captured permissions/remove new empty path | append-only/fail-closed test |
| sandbox/bind/chroot/container | optional/unknown | each target | `UNKNOWN_REQUIRES_OPERATOR_DECISION` | exact reversal required | isolation/read-only mount evidence |
| listener/socket exposure | no in baseline | none | none | n/a | separate design+authority required |
| credential provisioning | no for local VERIFY | none | none | n/a | prove absence |
| future `shard-write` / WRITE | no, reserved only | none | none | n/a | entirely separate authority/identity |
| fallback deployment | later separate gate | burzh | same verified successor package/harness | independent rollback | mazhor-independent verification |
| replication activation | not in baseline | none | none | n/a | separate protocol/design/authority |

## Blocking prerequisite before OPERATOR deployment decision

An exact deployment decision cannot yet authorize a functional gateway service because the immutable r0.2 package lacks the execution/audit harness required to define a truthful `ExecStart`.

Required causal step:
KOD publishes a bounded non-network VERIFY execution harness successor/integration package; SIS independently verifies it; ARH reviews preservation/audit boundary if required by KOO. Only then can KOO form the host mutation/deployment decision gate.
