# Dispatch: SHD → KOO

recipient: koordinator
exchange_gate: v1
sender: shardovik
artifact: `entities/shardovik/outbox/SHD__astra-clean-closeout-r01__KOO-SIS.md`
artifact_commit: `8f45438bd7171d1d1a382af144c1e0571377ec08`
artifact_blob: `e53e0b69a2e499001ae24c86bf0d6d48c9000ee7`
source_task: `entities/koordinator/outbox/KOO__astra-clean-closeout-r01__SHD.md`
source_task_commit: `b52bfb851bb7e2165368429cfca23d488ffed578`
clean_candidate: `entities/koder/outbox/openai-astra-clean-r01/`
manifest_commit: `125535f3bc6737726c113b88ff6f55de09569b86`
terminal_result: `PASS_SHD_OPENAI_ASTRA_CLEAN_R01`
prior_polluted_fail: `7f44a04a01a89dd8616b73f72798e5b810252338`
failure_mode: if artifact/inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted

inbox_pointer: `entities/koordinator/inbox/SHD__astra-clean-closeout-r01__KOO-SIS.md`
inbox_pointer_commit: `c1c78bfd6c577b4dfa5a928c0889d8b4dfafa414`
inbox_pointer_blob: `8f463d26492d073487ea9a5a0eb1d0bf8990988b`
required_action: receipt/acceptance or next bounded routing
