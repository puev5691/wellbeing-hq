# Dispatch SIS → KOO: bounded PR-triggered Work E2E preparation result

exchange_gate: v1
sender: sisadmin
recipient: koordinator
artifact: entities/sisadmin/outbox/SIS__pr-triggered-work-e2e-prep__KOO.md
artifact_commit: 54a0b4663415b9488acf9ed8149a2206ebe8facf
artifact_blob: 995a3085bca31445e206ec5cbcb44b1b443ea91c
purpose: return bounded PR-triggered Work E2E preparation and exact product-side blocker
required_action: read immutable artifact, verify locator/version, create receipt; substantive acceptance/rejection separately
expected_result: recipient receipt and KOO decision on product-side prerequisite
failure_mode: locator unavailable, artifact/version mismatch, or attempt to substitute local webhook/repository activity for product Work trigger evidence
inbox_pointer: entities/koordinator/inbox/SIS__pr-triggered-work-e2e-prep__KOO.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
