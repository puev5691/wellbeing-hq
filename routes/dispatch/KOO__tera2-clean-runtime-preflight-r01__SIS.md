# Dispatch: KOO → SIS / TERA2 clean-directory host/runtime preflight r0.1

exchange_gate: v1
sender: koordinator
recipient: sisadmin
artifact: entities/koordinator/outbox/KOO__tera2-clean-runtime-preflight-r01__SIS.md
artifact_commit: b7f493389bf69b385a691b53bf5dc87cfb0342f0
artifact_blob: f3ba07266b72a2bad5f4d799313bbe3ed5b3f2c2
purpose: bounded non-production/non-privileged host/runtime feasibility check for future clean TERA2 root genesis experiment
required_action: verify exact candidate and clean host boundary without node/genesis start or DATA/DB mutation
expected_result: PASS_SIS_TERA2_CLEAN_RUNTIME_PREFLIGHT_R01 or exact BLOCKED_/FAIL_ evidence
failure_mode: task/package identity mismatch, host collision, privilege requirement, unavailable prerequisite evidence, or unauthorized scope expansion
inbox_pointer: entities/sisadmin/inbox/KOO__tera2-clean-runtime-preflight-r01__SIS.md
registry_record: registry/by-sender/koordinator.jsonl
status: dispatched
receipt:
