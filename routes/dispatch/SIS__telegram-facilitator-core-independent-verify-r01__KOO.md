# Dispatch SIS → KOO: Telegram facilitator core independent verify r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-facilitator-core-independent-verify-r01__KOO.md`
artifact_commit: `947ea4b76d367774fbc2ae37b61d49e0e89d55bc`
artifact_blob: `7818e0fe67565dbfd0332ccc5b7a5dec601065ee`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-facilitator-core-independent-verify-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return independent bounded verification of exact Telegram facilitator core r0.1 candidate`
required_action: `KOO review PASS_SIS_TELEGRAM_FACILITATOR_CORE_R01; do not infer Telegram runtime integration or production authority`
expected_result: `receipt/acceptance or separate next exact task`
failure_mode: `if artifact commit/blob, inbox pointer or registry record mismatch, delivery is invalid and no receipt/acceptance may be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
