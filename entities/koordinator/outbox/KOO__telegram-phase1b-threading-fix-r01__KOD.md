# KOO → KOD: Telegram Phase1B threading fix r0.1

status: `BLOCKED_PENDING_KOD_WRITER_ESTABLISHMENT`
dispatch_status: `not_dispatched`
production: `no`
live_telegram: `no`

## Dependency

Do not execute until KOO verifies replacement KOD current-writer establishment after explicit OPERATOR decision.

## Exact defect basis

SIS result:
`entities/sisadmin/outbox/SIS__telegram-phase1b-resume-r05__KOO.md`
commit `078e747a940dcc47fd6a2ee917842e52a6ddd5fb`.

Accepted blocker:
`BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT`.

Reproduced cause:
- `Gateway.__init__` creates a SQLite connection with ordinary `sqlite3.connect(db_path)`;
- runtime uses `ThreadingHTTPServer`;
- request worker threads use the startup-thread SQLite connection;
- default SQLite thread affinity raises `sqlite3.ProgrammingError`.

## Future exact scope after unblock

Prepare one immutable non-production candidate that:
1. fixes the SQLite/threading boundary without weakening privacy or storage limits;
2. adds regression coverage through the real threaded HTTP path, not only direct same-thread calls;
3. preserves cleanup contract and no-persistent-raw-update boundaries;
4. performs no live Telegram call, credential handling, public webhook, deployment or production mutation;
5. returns package identity, tests and exact result to KOO.

No historical sudo or SIS host-gate replay belongs to KOD scope.

---
КТО: KOO
ДЛЯ ЧЕГО: заранее зафиксировать следующий KOD lane без преждевременного dispatch
СТАТУС: blocked_pending_kod_writer_establishment
