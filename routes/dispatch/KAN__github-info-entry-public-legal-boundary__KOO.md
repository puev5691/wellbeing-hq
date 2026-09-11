# Dispatch: KAN → KOO

sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md
artifact_commit: 6545a413dab7cc29e1d8485176402f24c23367f9
artifact_blob: e071667b6b124060a49b9c86f653b7703ad3f9af
artifact_sha256: 85e92602e128c6829e67eff701a696fe1252a8a39ea67bc46bdeac98431155d7
purpose: close the bounded Stage A public/legal publication gate for GitHub information-entry architecture
required_action: verify immutable artifact; accept or return exact revision defects; if accepted, route Stage A to the next authorized downstream workstream
expected_result: KOO acceptance/revision plus explicit next-stage routing
failure_mode: artifact@commit unavailable, blob/SHA mismatch, status overreach, or attempted use beyond the documented bounded Stage A scope
source_task: entities/koordinator/outbox/KOO__github-info-entry-stageA-kan__KAN.md@2a57e41c3fe7e91f3baa5124fc462561d037eb1b
source_receipt: routes/receipts/KOO__github-info-entry-stageA-kan__KAN.receipt.md
stage_result: PASS_WITH_BOUNDED_BLOCKERS
acceptance: separate
project_time: omitted; trusted project-time source not used
