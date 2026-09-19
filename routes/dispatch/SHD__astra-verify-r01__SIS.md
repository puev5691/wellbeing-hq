# Dispatch: SHD → SIS

recipient: sisadmin
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

inbox_pointer: `entities/sisadmin/inbox/SHD__astra-verify-r01__KOO-SIS.md`
inbox_pointer_commit: `b908eca5319cb12c81020d3b377ea2143de8b48b`
inbox_pointer_blob: `21ce05be082402a46d3e3635f981a725dccea4ce`
required_action: consume independent failure evidence; do not use corrupted candidate for live execution
