# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__github-info-entry-pilot-r1-crosslayer-review__KOO.md`
artifact_commit: `06f28f1db7d1846561aab56cf93106fcdf66f084`
artifact_blob: `c3d6fe9bf1444305990e2e83daa226a954c597f3`
inbox_pointer: `entities/koordinator/inbox/SHD__github-info-entry-pilot-r1-crosslayer-review__KOO.md`
registry_record: `registry/by-sender/shardovik.jsonl`
purpose: вернуть КООРДИНАТОРУ результат SHD cross-layer verification bounded GitHub information-entry pilot r1
required_action: передать дефект KOD или открыть correction task; не продвигать pilot к public-ready до type-validation fix
expected_result: receipt, KOO acceptance, revision_request, route_to_KOD или rejection
failure_mode: если artifact или inbox_pointer недоступны либо commit/blob не совпадают, delivery не считать выполненной
status: dispatched
project_time: omitted; trusted project-time source not used