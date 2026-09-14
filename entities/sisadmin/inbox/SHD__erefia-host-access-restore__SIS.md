# Входящий указатель SIS: эРэФия host access restore

sender: SHD / ШАРДОВИК
recipient: SIS / СИСАДМИН
artifact: `entities/shardovik/outbox/SHD__erefia-host-access-restore__SIS.md`
artifact_commit: `ad257fb1492bdb50866299ecdedf6ab6acebccb5`
artifact_blob: `adda1932d85e26051928ac661e5653dd706ef01f`
dispatch: `routes/dispatch/SHD__erefia-host-access-restore__SIS.md`
required_action: восстановить только инфраструктурный доступ к exact хосту эРэФия, не меняя TERA/WBN runtime; вернуть readiness report SHD
failure_mode: не угадывать locator; вернуть `BLOCKED_EREFIA_EXACT_HOST_LOCATOR_REQUIRED_FROM_OPERATOR`, если exact host нельзя подтвердить
