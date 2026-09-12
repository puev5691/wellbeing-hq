# Dispatch KOO → OPERATOR: source-loading-policy v2.1 approval

sender: koordinator
recipient: operator
status: dispatched
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__source-loading-policy-v2_1-approval__OPERATOR.md`
artifact_commit: `b15a9250e72e7bb5da4efabd027fa4e43386022e`
artifact_blob: `7a0bef645c33ada72952f89b13f088856dc69202`

inbox_locator: `entities/operator/inbox/KOO__source-loading-policy-v2_1-approval__OPERATOR.md`
inbox_commit: `244c226c7b588a67815e446ec31fd74794bdb63e`
inbox_blob: `7b620521506fb7940dbccac30223c577c737a0be`

required_action: explicit approval/rejection of exact candidate revision
failure_mode: do not claim active Project Source replacement without explicit approval and verified activation
project_time: omitted; trusted project-time source not used
