# KOO → SIS: Telegram Phase 1B runtime privacy readiness

status: TASK
scope: READ_ONLY_OR_NONPRODUCTION_PREPARATION
live_send: forbidden
credentials_publication: forbidden

## Basis

KAN privacy gate:
`PASS_BOUNDED_WITH_PRE_LIVE_PRIVACY_FIXES`.

KOO selected:
`privacy_mode = aggregate_only`.

## Required result

Without performing a live Telegram send:

1. identify the intended non-production runtime/webhook path;
2. verify/configure that full Telegram update bodies are not persisted in:
   - reverse-proxy/access logs;
   - application logs;
   - crash/debug traces;
   - retry/dead-letter storage;
3. identify the exact sandbox DB path/storage boundary for the future test;
4. provide an executable cleanup/deletion action satisfying the KAN max-30-day live sandbox DB rule;
5. state where bot token/webhook secret would be stored if/when OPERATOR/KOO authorizes credentials;
6. do not publish secret values;
7. return exact remaining external dependencies for one real sandbox send:
   - channel numeric chat id;
   - linked discussion state/id;
   - publisher bot identity/admin rights;
   - webhook endpoint readiness.

If any logging component cannot satisfy the boundary, return an exact blocker.

No live send, no Telegram credentials in GitHub, no production deployment.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: закрыть runtime/privacy blockers до первого bounded Telegram live sandbox
СТАТУС: assigned
