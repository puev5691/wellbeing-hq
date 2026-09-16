# Phase 1B sandbox privacy / cleanup contract

Selected mode: `aggregate_only`.

## Retained state

Allowed: publication/distribution totals (`comments_count`, `reaction_total`, `member_count`) and gateway technical delivery identifiers already required for integrity.

Forbidden: audience user IDs, usernames/names, raw comment bodies, per-user history, identity-linking hashes, audience profiles, raw-update persistence, LLM/embedding processing.

## Sandbox DB contract

Exact candidate path:
`/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`

SIS must confirm this path is feasible and protected on the actual runtime host before live use. If SIS selects a different host path, that is a new runtime contract and must be explicitly reviewed rather than silently substituted.

## Cleanup interface

After KOO closes Phase 1B, the live sandbox DB containing Telegram-derived aggregate state must be deleted within 30 days unless superseded by a newer explicit retention decision.

Command:
`python3 cleanup_sandbox.py --db /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3 --confirm DELETE_PHASE1B_SANDBOX_DB`

The helper refuses arbitrary paths and refuses deletion without the exact confirmation token.

This cleanup affects only the live sandbox SQLite DB. It does not authorize deletion of preservation evidence or unrelated project files.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: сделать retention rule исполнимым и проверяемым до live sandbox
СТАТУС: candidate_runtime_contract
