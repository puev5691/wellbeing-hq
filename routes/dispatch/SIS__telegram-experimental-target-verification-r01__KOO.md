# Dispatch SIS → KOO: Telegram experimental target verification r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-experimental-target-verification-r01__WEB-KOO.md`
artifact_commit: `392f034f8cc2f39ede11f167a6de1477e59b618e`
artifact_blob: `2f861f83e59104fb7c480c86f5213c450b723e8e`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-experimental-target-verification-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return bounded Telegram target verification blocker and exact credential-provisioning dependency`
required_action: `review BLOCKED_TELEGRAM_BOT_CREDENTIAL_NOT_PROVISIONED; do not infer Telegram admin/API facts until read-only API verification completes`
expected_result: `receipt/acceptance or separate exact post-provision verification task`
failure_mode: `if artifact commit/blob, inbox pointer or registry record mismatch, delivery is invalid and receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
