# Dispatch SIS → KOO: Telegram experimental target verification r0.3

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-experimental-target-verification-r03__WEB-KOO.md`
artifact_commit: `977a482936a8c0b4ad809c1b718048b1903fec9e`
artifact_blob: `00da9ebc0f54da9dea07437fb6f50808d7f53381`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-experimental-target-verification-r03__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return final bounded Telegram target mapping PASS before any send`
required_action: `review PASS_SIS_TELEGRAM_EXPERIMENTAL_TARGET_API_MAPPING_R01; no send authority is implied`
expected_result: `receipt/acceptance or separate exact send task`
failure_mode: `if artifact identity, inbox pointer or registry record mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
