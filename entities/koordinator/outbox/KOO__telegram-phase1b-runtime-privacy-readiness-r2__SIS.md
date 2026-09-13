# KOO → SIS: Telegram Phase 1B runtime/privacy readiness r2

status: TASK
priority: CURRENT_CAUSAL_CHAIN
scope: NONPRODUCTION_RUNTIME_PRIVACY_GATE
live_send: forbidden
production: no
credential_values_in_github: forbidden

## Accepted technical basis

KOD result:
`entities/koder/outbox/KOD__telegram-phase1b-privacy-fix-result__KOO.md`
commit: `69c74847cfdd5a7e205a13d6fb81e099c261e4f4`

KOO decision:
`entities/koordinator/outbox/KOO__telegram-phase1b-privacy-fix-decision__KOD.md`
commit: `fd3f5dd75d6459bdedc5121e51fc51b188a0e8ea`

Exact immutable package:
`entities/koder/outbox/telegram-media-phase1b-privacy-v01/`
commit: `cd81bbd98a4be334388f95ea948427d91fa82a05`

KOO independent SHA-256 check: 9/9 PASS.

Selected privacy mode: `aggregate_only`.

## Required SIS verification

Without a live Telegram send and without publishing any secret values:

1. Verify feasibility, ownership and permissions for the exact sandbox DB path:
   `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`.
2. Verify that full Telegram update bodies, audience identity and raw comment text will not persist in:
   - reverse-proxy/access logs;
   - application logs;
   - crash/debug traces;
   - retry/dead-letter storage.
3. Verify that the exact cleanup contract can be executed on the chosen non-production runtime host:
   `python3 cleanup_sandbox.py --db /var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3 --confirm DELETE_PHASE1B_SANDBOX_DB`.
4. State the non-secret storage mechanism/location that would hold bot token and webhook secret if separately authorized later. Do not request or publish secret values in this task.
5. Return exact remaining external dependencies for one future bounded sandbox send:
   - verified channel numeric chat id;
   - linked discussion state and numeric id when linked;
   - publisher bot identity/admin rights;
   - webhook endpoint/runtime readiness.
6. If any runtime logging or storage component cannot satisfy the privacy boundary, return the exact blocker instead of improvising.

## Boundary

This task does not authorize:
- Telegram API calls;
- live send;
- production deployment;
- creation/publication of credentials;
- channel administration changes.

The prior SIS task remains provenance. This r2 task binds the runtime check to the exact KOO-accepted KOD package above.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: выполнить следующий профильный runtime/privacy gate после принятия точного KOD Phase 1B privacy-fix candidate
СТАТУС: assigned_current_causal_chain
