# Dispatch KOO → SIS: bounded mazhor shard gateway r0.2 VERIFY deployment

exchange_gate: v1
sender: koordinator
recipient: sisadmin
artifact: entities/koordinator/outbox/KOO__mazhor-gateway-r02-bounded-deploy__SIS.md
artifact_commit: d1e777e1e29e2847100808fb518884451824dcee
artifact_blob: a3b98d1afd25ddb8858496d7e87f0fc0dd2559f6
purpose: execute exact OPERATOR-authorized bounded VERIFY deployment on mazhor only
required_action: perform phased deployment with mandatory predeploy/access/unit-equivalence/smoke/rollback gates
expected_result: PASS_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT or exact blocker/rollback/fail
failure_mode: stop fail-closed on authority/input/host/precondition/access/hash/unit/audit mismatch; no permissions changes on existing repo/archive roots
status: dispatched
project_time: omitted
