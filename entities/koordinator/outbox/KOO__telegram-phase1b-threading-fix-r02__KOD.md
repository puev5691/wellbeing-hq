# KOO → KOD: Telegram Phase1B threading fix r0.2

status: `READY_FOR_KOD_EXECUTION`
dispatch_status: `prepared_for_dispatch`
production: `no`
live_telegram: `no`
credentials: `no`
destructive_cleanup: `no`

## Authority and dependency state

Replacement KOD current-writer is established:
`entities/koder/current/KOD__replacement-current-writer-v02.md`
commit `56db550005d6ed6956ba1bf753f3cb24ca295cc3`
status `CURRENT_WRITER_ESTABLISHED`.

The previous r0.1 task remains provenance only:
`entities/koordinator/outbox/KOO__telegram-phase1b-threading-fix-r01__KOD.md`
status there was `BLOCKED_PENDING_KOD_WRITER_ESTABLISHMENT`.

This r0.2 artifact is the current task that removes only that resolved writer dependency.

## Exact defect basis

SIS result:
`entities/sisadmin/outbox/SIS__telegram-phase1b-resume-r05__KOO.md`
commit `078e747a940dcc47fd6a2ee917842e52a6ddd5fb`
verdict `BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT`.

Confirmed cause:
- `Gateway.__init__` creates a SQLite connection with ordinary `sqlite3.connect(db_path)`;
- runtime uses `ThreadingHTTPServer`;
- request worker threads access the startup-thread SQLite connection;
- default SQLite thread affinity raises `sqlite3.ProgrammingError`;
- existing accepted tests do not cover the real threaded HTTP path.

## Exact scope

Perform Resume-First and prepare one immutable non-production corrected runtime candidate that:

1. fixes the SQLite/threading boundary without weakening privacy, storage or cleanup constraints;
2. adds regression coverage through the real threaded HTTP server path, not only direct same-thread calls;
3. preserves the no-persistent-raw-Telegram-update boundary, audience identity boundary and raw comment-text boundary;
4. preserves the exact cleanup contract;
5. does not perform live Telegram calls, public webhook exposure, deployment, privileged host mutation, credentials handling or production execution;
6. does not replay historical sudo or unchanged SIS host-gate work;
7. publishes the corrected package with immutable commit/blob identity and test evidence;
8. returns an exact result to KOO through the current Exchange Gate.

## Required verification

Before modification:
- fresh GitHub-preflight `puev5691/wellbeing-hq`;
- confirm this exact input from KOD inbox and KOD current-writer state;
- locate the currently accepted Telegram Phase1B package lineage and do not silently substitute another package.

After modification:
- run the relevant test suite including threaded HTTP regression coverage;
- verify privacy/storage cleanup boundaries remain intact;
- provide exact changed files/package identity, test commands and results;
- distinguish code-level PASS from any future SIS runtime/host verification.

## Result boundary

Expected terminal result to KOO:
- `PASS_KOD_THREADING_FIX_CANDIDATE_READY`, or
- exact `BLOCKED_*` with concrete evidence.

A KOD PASS does not authorize live Telegram send or production deployment. The next independent verifier remains SIS after KOO acceptance/routing.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: активировать первый профильный KOD lane после завершения replacement writer gate
СТАТУС: ready_for_kod_execution_r02
