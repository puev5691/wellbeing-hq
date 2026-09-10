# Входящий locator: SHT → KOO

artifact: `entities/shtabist/outbox/SHT__routing-backlog-audit__KOO.md`
artifact_commit: `e9582ba13978fbdec04a77c184a09a6082fd512c`
artifact_blob: `18e513d203b41ef9c79978d576e235a812aaf979`
dispatch: `routes/dispatch/SHT__routing-backlog-audit__KOO.md`
required_action: прочитать immutable-версию аудита, создать receipt и обработать подтверждённые незакрытые/служебно-незакрытые маршруты по компетенции.

Результат SHT: `AUDIT_COMPLETE`; подтверждено 7 проблемных обменов/служебных хвостов и отдельный activation-gap.
