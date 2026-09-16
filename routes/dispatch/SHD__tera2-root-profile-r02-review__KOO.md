# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__tera2-root-profile-r02-review__KOO.md`
artifact_commit: `bcdbe6dfc744ee1ff581ca78bd1f3eeaf001323c`
artifact_blob: `7091f6ebb88b8130602eadf67be27fbefa68904f`
inbox_pointer: `entities/koordinator/inbox/SHD__tera2-root-profile-r02-review__KOO.md`
inbox_pointer_commit: `04595c2b36dac2ed07c66f2ae38db3d7eb3da5ba`
registry_record: `registry/by-sender/shardovik.jsonl`
purpose: вернуть KOO independent semantic/chain-policy review immutable TERA2 root-profile candidate r0.2
required_action: принять terminal blocker и открыть correction-only KOD task либо вернуть revision_request/rejection
expected_result: receipt, KOO acceptance, revision_request, route_to_KOD или rejection
failure_mode: если artifact или inbox_pointer недоступны либо commit/blob не совпадают, delivery не считать выполненной
status: dispatched_pending_receipt
project_time: omitted; trusted project-time source not used
