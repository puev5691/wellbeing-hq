# Telegram Media Gateway Phase 1B privacy fix candidate

Status: candidate, non-production, credential-free, zero-live-network.

Purpose: implement KOO-selected `privacy_mode=aggregate_only` on top of accepted Phase 1A without changing the historical package.

Changes:
- `safe_receipt()` emits `privacy_mode: aggregate_only` and stable policy marker;
- stale `fail_closed_pending_KAN` receipt field is removed;
- retained audience-derived state remains publication/distribution aggregate totals only;
- no user identity, raw comment text, per-user table, identity hash, LLM or embedding path is added;
- runtime contract identifies sandbox DB as `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- cleanup interface deletes only that exact DB path and requires explicit confirmation.

Policy provenance:
- KAN privacy gate commit `d201f1cc2a8d151fa0358c2c0db26fd1d217e409`;
- KOO privacy decision commit `14df7edd91954e92c96e593b4432fd6441f3833a`;
- KOO code-fix task commit `267e7f23a8ba89efc8221f95f38a67b23ef0af5c`.

Exact test command: `python3 -m unittest -v`.

Live Telegram/network calls: forbidden and not implemented by this package. Transport remains dependency-injected; tests use `FakeTransport`.

SIS boundary: before any live sandbox use, SIS still must independently verify request/application logging, host path feasibility/permissions and runtime secret injection. This package grants no credentials, webhook, channel-admin or live-send authority.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: Phase 1B pre-live privacy code fix для режима aggregate_only
СТАТУС: candidate_nonproduction
