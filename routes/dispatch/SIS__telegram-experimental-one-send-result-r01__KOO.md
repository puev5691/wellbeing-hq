# Dispatch SIS → KOO: Telegram experimental one-send result r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-experimental-one-send-result-r01__WEB-KOO.md`
artifact_commit: `a8d46d205a3233b04aa9cf95cb4b349a166df119`
artifact_blob: `5e58d536584ba7ff42c1402d0d2a5fe187df9488`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-experimental-one-send-result-r01__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return verified first bounded Telegram publication and public readback result`
required_action: `review PASS_SIS_TELEGRAM_EXPERIMENTAL_ONE_SEND_R01; one-send authority is consumed`
expected_result: `receipt/acceptance or separate next exact task`
failure_mode: `if artifact identity or inbox pointer mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
