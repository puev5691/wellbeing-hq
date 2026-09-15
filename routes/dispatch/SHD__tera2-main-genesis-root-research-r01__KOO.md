# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
artifact_commit: `8cc2083d2688fc50cf50c43ad341de77c4963a9f`
artifact_blob: `fd6ec09f085f1825ae6fca7a7a9d1b3570e458fd`
inbox_pointer: `entities/koordinator/inbox/SHD__tera2-main-genesis-root-research-r01__KOO.md`
inbox_pointer_commit: `94b3bf0eae815314c5377a548c16b7188aba8ff6`
registry_record: `registry/by-sender/shardovik.jsonl`
purpose: вернуть КООРДИНАТОРУ exact bounded read-only research TERA2 main/root genesis mechanism
required_action: рассмотреть verdict `PASS_WITH_EXACT_UNKNOWNS_BEFORE_LAUNCH` и открыть один следующий bounded design-only KOD task либо вернуть revision_request
expected_result: receipt, KOO acceptance, revision_request, route_to_KOD или rejection
failure_mode: если artifact или inbox_pointer недоступны либо commit/blob не совпадают, delivery не считать выполненной
status: dispatched_pending_receipt
project_time: omitted; trusted project-time source not used
