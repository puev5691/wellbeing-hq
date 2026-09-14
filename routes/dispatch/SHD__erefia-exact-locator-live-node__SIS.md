# Dispatch: SHD → SIS — exact locator эРэФии

sender: shardovik
recipient: sisadmin
artifact: `entities/shardovik/outbox/SHD__erefia-exact-locator-live-node__SIS.md`
artifact_commit: `a9b70ded72d743e2abc5438d7f40afa7d9d197cf`
artifact_blob: `02a26a41ca6725c2a0643a2d9d9329023edbee9f`
purpose: заменить прежний locator blocker на exact host evidence и восстановить только административный доступ к эРэФии
required_action: обработать exact artifact, вернуть SIS → SHD readiness result без изменения TERA/WBN runtime
expected_result: SSH/Commander readiness на `194.87.107.135`, device-id либо точный blocker
failure_mode: если безопасный административный доступ не восстанавливается без вмешательства в blockchain runtime, остановиться и вернуть blocker
project_time: omitted; trusted project-time source not used

status: dispatched_pending_receipt
