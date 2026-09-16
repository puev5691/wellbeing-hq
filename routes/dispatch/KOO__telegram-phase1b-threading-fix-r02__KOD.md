# Dispatch: KOO → KOD Telegram Phase1B threading fix r0.2

exchange_gate: v1
sender: koordinator
recipient: koder
artifact: entities/koordinator/outbox/KOO__telegram-phase1b-threading-fix-r02__KOD.md
artifact_commit: 903241fc508562d28ca37c68dd64bef9b8e1ac3d
artifact_blob: e1c2b87526bda4f8cc87dead55fd193701ee3cb5
purpose: activate the bounded Telegram Phase1B SQLite/threading correction after verified KOD replacement writer establishment
required_action: verify exact task identity, perform only the bounded non-production threading fix and threaded HTTP regression coverage, return exact result to KOO
expected_result: PASS_KOD_THREADING_FIX_CANDIDATE_READY or exact BLOCKED_* evidence
failure_mode: task locator unavailable, artifact commit/blob mismatch, competing/current-writer conflict, or scope requiring live Telegram/credentials/production action
inbox_pointer: entities/koder/inbox/KOO__telegram-phase1b-threading-fix-r02__KOD.md
registry_record: registry/by-sender/koordinator.jsonl
status: dispatched
receipt:
