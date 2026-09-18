# Dispatch SIS → KOO: mazhor host-access pilot r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__mazhor-host-access-pilot-r01__ARH-KOO.md`
artifact_commit: `b7081ab521953206ac60b4bbaae9b83c27783a7b`
artifact_blob: `c895f72b6cb6cd99d4d7abe93f49201f965f56ec`
inbox_pointer: `entities/koordinator/inbox/SIS__mazhor-host-access-pilot-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return bounded mazhor preservation readback pilot and latency evidence`
required_action: `review PASS_SIS_MAZHOR_HOST_ACCESS_PILOT_R01_READY_FOR_ARH_READBACK; do not infer unrestricted ARH host access`
expected_result: `receipt/acceptance or separate exact next task`
failure_mode: `if artifact identity or inbox locator mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
