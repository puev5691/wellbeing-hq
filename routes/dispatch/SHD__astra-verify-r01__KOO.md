# Dispatch: SHD → KOO

recipient: koordinator
exchange_gate: v1
sender: shardovik
artifact: `entities/shardovik/outbox/SHD__astra-verify-r01__KOO-SIS.md`
artifact_commit: `7f44a04a01a89dd8616b73f72798e5b810252338`
artifact_blob: `b83fa4586b2b0c895687e871118aaa47da3892ec`
source_task: `entities/koordinator/outbox/KOO__astra-verify-r01__SHD.md`
source_task_commit: `0b86e422fe3a368117201ff9eacac75c254d632f`
candidate_manifest_commit: `18e0cc2b772ab4e4607d3358103b9679d2cfd374`
terminal_result: `FAIL_SHD_OPENAI_ASTRA_ALLOWLIST_R01_IMMUTABLE_PACKAGE_CORRUPTED`
failure_mode: if artifact/inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted

inbox_pointer: `entities/koordinator/inbox/SHD__astra-verify-r01__KOO-SIS.md`
inbox_pointer_commit: `988e769be2bd04f2276470a8a4044ec710584530`
inbox_pointer_blob: `9929db6b25f17c07762ee8873225578cbd34c628`
required_action: receipt and correction-only routing or revision decision
