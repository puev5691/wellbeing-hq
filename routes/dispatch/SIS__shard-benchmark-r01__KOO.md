# Dispatch SIS → KOO: shard benchmark r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__shard-benchmark-r01__ARH-KOO.md`
artifact_commit: `52e9a70c2d507e299caaad58bacbf65b6f59aefd`
artifact_blob: `f4b7d22dad4b43642f63da61004de47ca3149ee4`
inbox_pointer: `entities/koordinator/inbox/SIS__shard-benchmark-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return bounded burzh/erefia shard benchmark against mazhor baseline`
required_action: `review PASS_SIS_SHARD_BENCHMARK_R01_READY_FOR_SELECTION; do not infer shard selection or deployment`
expected_result: `receipt/acceptance or separate exact selection task`
failure_mode: `if artifact identity or inbox locator mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
