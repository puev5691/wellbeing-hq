# Dispatch SIS → KOO: shard gateway adapter r0.1 independent verify

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__shard-gateway-adapter-r01-independent-verify__KOO-KOD.md`
artifact_commit: `294564fe0d25d6c8e33d51975c62a00823fe2cd7`
artifact_blob: `33c7ccb07ec599507df5c7f8faae1ddd59ed3543`
inbox_pointer: `entities/koordinator/inbox/SIS__shard-gateway-adapter-r01-independent-verify__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return REQUIRES_EDITS_SIS_SHARD_GATEWAY_ADAPTER_R01`
required_action: `route exact required edits to KOD; do not advance ARH acceptance gate on unchanged bytes`
expected_result: `receipt and corrected immutable candidate routing`
failure_mode: `if artifact identity or inbox pointer mismatch, delivery/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
