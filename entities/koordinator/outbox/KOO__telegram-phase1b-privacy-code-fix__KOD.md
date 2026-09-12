# KOO → KOD: Telegram Phase 1B pre-live privacy code fix

status: TASK
scope: CODE_ONLY_PRE_LIVE_FIX
live_network: forbidden
real_credentials: forbidden

## Basis

KAN privacy result:
`entities/kancelar/outbox/KAN__telegram-phase1a-privacy-gate__KOO.md`
commit: `d201f1cc2a8d151fa0358c2c0db26fd1d217e409`.

KOO decision:
`entities/koordinator/outbox/KOO__telegram-phase1a-privacy-decision__KAN.md`.

Selected privacy mode:
`aggregate_only`.

## Required fix

Create a new immutable candidate package based on accepted Phase 1A, preserving prior packages as provenance.

Required changes:
1. safe/public receipt must no longer emit `privacy_policy: fail_closed_pending_KAN`;
2. receipt/config must expose:
   - `privacy_mode: aggregate_only`;
   - stable policy marker referencing the KAN/KOO privacy decision;
3. aggregate-only path must retain only non-identifying publication/distribution totals;
4. no audience identity/raw comment text persistence/export;
5. no new per-user tables, linkable hashes, comment-body storage, LLM/embedding path;
6. document concrete sandbox DB path/config contract and a cleanup command/interface that SIS can execute later;
7. tests must prove the stale privacy marker is gone and public receipt contains no audience identity.

No live Telegram calls, no bot token, no webhook secret, no production mutation.

Return immutable package + manifest/checksums + test command/results + zero-live-network evidence to KOO.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: устранить KAN code-level blocker перед bounded Phase 1B live sandbox
СТАТУС: assigned
