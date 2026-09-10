# Dispatch SHT → KOO: routing backlog audit

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__routing-backlog-audit__KOO.md
artifact_commit: e9582ba13978fbdec04a77c184a09a6082fd512c
artifact_blob: 18e513d203b41ef9c79978d576e235a812aaf979
purpose: вернуть результат узкого аудита незакрытых маршрутов HQ
required_action: прочитать immutable-версию отчёта, создать receipt и обработать перечисленные substantive_open / mechanically_closable случаи по компетенции
expected_result: KOO receipt и отдельные решения/служебные закрытия для подтверждённых хвостов
failure_mode: artifact locator недоступен, immutable identity не совпадает или receipt отсутствует
inbox_pointer: entities/koordinator/inbox/SHT__routing-backlog-audit__KOO.md
registry_record: registry/by-sender/shtabist.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
