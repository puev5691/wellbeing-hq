# Dispatch KOO → KOO: source rebuild r0.3 info-field publication

exchange_gate: v1
sender: koordinator
recipient: koordinator
artifact: entities/koordinator/outbox/KOO__source-rebuild-r03-infofield-publish__KOO.md
artifact_commit: 831ea8db8197f0f559244495ecd1881d2e9e8342
artifact_blob: ab4f2bf015ad3789e6e2b1761028b9ab4d749bd5
purpose: publish exact r0.3 candidate bytes into project information field for locator-only downstream review
required_action: execute exact bounded publication/readback task; do not activate Project Sources
expected_result: PASS_KOO_SOURCE_REBUILD_R03_INFOFIELD_PUBLISHED_READY_FOR_SHT_RECHECK or exact blocker/fail
failure_mode: on any identity mismatch or inability to establish exact 7-file locator, stop without claiming downstream readiness
status: dispatched
project_time: omitted
