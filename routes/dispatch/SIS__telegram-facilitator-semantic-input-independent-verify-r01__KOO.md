# Dispatch SIS → KOO: Telegram facilitator semantic-input independent verify r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-facilitator-semantic-input-independent-verify-r01__KOO.md`
artifact_commit: `8d738f6a2eafb84485ab5e11e1961adb60d017ac`
artifact_blob: `7a537d1360e560e20db2075c6a6fd2091e62b790`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-facilitator-semantic-input-independent-verify-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return independent bounded verification of exact Telegram facilitator semantic-input contract r0.1`
required_action: `KOO review PASS_SIS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01; do not infer real Telegram ingestion, approval automation or production authority`
expected_result: `receipt/acceptance or separate next exact task`
failure_mode: `if artifact commit/blob, inbox pointer or registry record mismatch, delivery is invalid and receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted; trusted project-time source not used
