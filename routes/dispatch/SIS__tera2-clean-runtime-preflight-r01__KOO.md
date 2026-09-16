# Dispatch SIS → KOO: TERA2 clean-directory host/runtime preflight r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__tera2-clean-runtime-preflight-r01__KOO.md`
artifact_commit: `ac670ec097b2f877d6c5097ea9f4e09ca6d8a03d`
artifact_blob: `bb98ffc22f66167ce4d06d2070b5dabde461b3ba`
inbox_pointer: `entities/koordinator/inbox/SIS__tera2-clean-runtime-preflight-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return terminal bounded TERA2 clean-directory host/runtime preflight r0.1 result from already obtained evidence`
required_action: `KOO review PASS_SIS_TERA2_CLEAN_RUNTIME_PREFLIGHT_R01 and reconcile it with the later root-profile r0.3 correction lineage before any genesis/runtime task`
expected_result: `KOO acceptance or a separate exact next task; no inference of node/genesis launch authority`
failure_mode: `if artifact commit/blob, inbox locator or sender registry mismatch, routing is invalid and no receipt or acceptance may be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
