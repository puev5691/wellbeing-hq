# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__telegram-bridge-ab-identity-attestation-r01-independent-document-review__KOO.md`
artifact_commit: `c641965b9b9d1a3492c191042b5431a48bc2d702`
artifact_blob: `17f3dba23a08968b186a23dcfa5d7db56e2924d1`
inbox_pointer: `entities/koordinator/inbox/SHD__telegram-bridge-ab-identity-attestation-r01-independent-document-review__KOO.md`
inbox_pointer_commit: `2e9e98fc10fd163455dc78751082f77c90e44681`
inbox_pointer_blob: `e81a5550a0e96886b798634bc972b57a3f3ed7ca`
source_task: `entities/koordinator/outbox/KOO__telegram-bridge-ab-identity-attestation-r01-shd-independent-document-review__SHD.md`
source_task_commit: `427b82307bead9cfac192b3b348f79b2c105b44f`
kod_input_commit: `871cb4e411a537ac2b9657a4b32710f88839d7b7`
terminal_result: `PASS_SHD_TELEGRAM_BRIDGE_AB_IDENTITY_ATTESTATION_R01_WITH_BOUNDARIES`
required_action: KOO receipt, reconciliation and OPERATOR governance decision routing
failure_mode: if artifact or inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
