# Dispatch KOO → KOD: shard gateway adapter r0.2 correction

exchange_gate: v1
sender: koordinator
recipient: koder
artifact: entities/koordinator/outbox/KOO__shard-gateway-adapter-r02-correction__KOD.md
artifact_commit: 0bea0365d166918b03bf55e138c786fa5562fde5
artifact_blob: b030f9bb756bee6a83defac01da2971fd0c248ff
purpose: bounded correction of four SIS security/contract defects on immutable shard gateway adapter r0.1
required_action: produce immutable r0.2 successor package under exact task boundaries
expected_result: PASS_KOD_SHARD_GATEWAY_ADAPTER_R02_READY_FOR_SIS_REVERIFY or exact blocker/fail
failure_mode: if KOD writer, SIS result identity, r0.1 package identity, or task authority mismatches, stop and return exact blocker
status: dispatched
project_time: omitted
