# Dispatch: SHD → SIS — correction SSH эРэФии

sender: shardovik
recipient: sisadmin
artifact: `entities/shardovik/outbox/SHD__erefia-ssh2222-correction__SIS.md`
artifact_commit: `9b257f36c02cde9dcaec680aa4190b2ac7011705`
artifact_blob: `db749700ca2b4ce8c49bdb0ef54fbe400954dddb`
purpose: исправить SSH endpoint эРэФии с 22 на 2222 и снять ложный blocker
required_action: использовать `194.87.107.135:2222`, вернуть Remote Desktop Commander без изменения TERA/WBN runtime
expected_result: SIS → SHD readiness result с Commander device-id либо точный blocker
failure_mode: не использовать старое evidence по port 22 как доказательство недоступности SSH
project_time: omitted; trusted project-time source not used

Статус доставки: dispatched_pending_receipt
