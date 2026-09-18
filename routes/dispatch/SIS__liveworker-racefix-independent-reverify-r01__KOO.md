# Dispatch SIS → KOO: live-worker race-fix independent re-verification r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__liveworker-racefix-independent-reverify-r01__KOO.md`
artifact_commit: `75c877679bb2ce2126a2934b50cc9caaddaaca71`
artifact_blob: `54bf448fc9f1a025de20b3c114074de849c7d4a2`
inbox_pointer: `entities/koordinator/inbox/SIS__liveworker-racefix-independent-reverify-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return independent race-fix behavior PASS with exact immutable SHA metadata blocker`
required_action: `KOO route correction-only KOD task for BLOCKED_LIVE_WORKER_RACE_FIX_IMMUTABLE_HASH_MISMATCH; preserve corrected race behavior`
expected_result: `receipt/acceptance or separate exact correction task`
failure_mode: `if artifact commit/blob, inbox pointer or registry record mismatch, delivery is invalid and receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
