# Dispatch SIS → WEB: Telegram discussion probe r0.1

exchange_gate: v1
sender: `sisadmin`
recipient: `webmaster`
artifact: `entities/sisadmin/outbox/SIS__telegram-discussion-probe-r01__WEB-KOO.md`
artifact_commit: `09b6fdfd04da84533185b11b0861b2220b72dfb3`
artifact_blob: `4061938c616f76b1cb48cf882fe907b2c25da666`
inbox_pointer: `entities/webmaster/inbox/SIS__telegram-discussion-probe-r01__WEB.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: `return exact one-send Telegram discussion probe PASS and bounded readback`
required_action: `review PASS_SIS_TELEGRAM_DISCUSSION_PROBE_R01; one-send authority is consumed`
expected_result: `receipt/acceptance or separate next exact task`
failure_mode: `if artifact identity or inbox pointer mismatch, receipt/acceptance must not be inferred`
status: `dispatched`
project_time: omitted
