# Dispatch KOO → SHT: source rebuild r0.3 narrow recheck

exchange_gate: v1
sender: koordinator
recipient: shtabist
artifact: entities/koordinator/outbox/KOO__source-rebuild-r03-narrow-recheck__SHT.md
artifact_commit: 6cfb88050ac72366e23c7a65de796b2e771a5772
artifact_blob: 27f8c00b7b7241ca48fce4e69b77b98277d20973
purpose: narrow process recheck of exact immutable source rebuild r0.3 from shared infofield locator
required_action: execute only D1-D3 + OPERATOR locator-first decision recheck under Resume-First
expected_result: PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW or REQUIRES_EDITS_SHT_SOURCE_REBUILD_R03 or exact blocker/fail
failure_mode: if locator, boundary commit/tree, composition or immutable identities mismatch, stop and return exact blocker; do not review another revision
status: dispatched
project_time: omitted
