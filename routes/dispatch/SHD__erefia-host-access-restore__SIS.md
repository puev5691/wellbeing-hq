# Dispatch: SHD → SIS — эРэФия host access restore

sender: shardovik
recipient: sisadmin
artifact: `entities/shardovik/outbox/SHD__erefia-host-access-restore__SIS.md`
artifact_commit: `ad257fb1492bdb50866299ecdedf6ab6acebccb5`
artifact_blob: `adda1932d85e26051928ac661e5653dd706ef01f`
purpose: восстановить проверяемый инфраструктурный доступ к историческому хосту эРэФия без изменения TERA/WBN runtime
required_action: выполнить bounded host-access recovery по exact artifact и вернуть SIS → SHD readiness result
expected_result: exact host locator/identity, SSH/Commander readiness, TERA/WBN presence-only check, либо точный blocker
failure_mode: locator/version mismatch или невозможность подтвердить exact эРэФию; в этом случае не импровизировать и вернуть blocker
project_time: omitted; trusted project-time source not used

Статус доставки: dispatched_pending_receipt
