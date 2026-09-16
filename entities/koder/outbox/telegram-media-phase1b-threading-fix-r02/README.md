# Telegram Media Gateway Phase 1B threading fix r0.2

Status: bounded non-production candidate, credential-free, no live Telegram/network use.

Purpose: fix the SIS-confirmed SQLite/thread-affinity defect in the accepted Phase1B privacy lineage without changing privacy, storage, cleanup or live-authority boundaries.

Source package:
`entities/koder/outbox/telegram-media-phase1b-privacy-v01/` @ `cd81bbd98a4be334388f95ea948427d91fa82a05`.

Changes:
- SQLite connection is opened with `check_same_thread=False` only after requiring `sqlite3.threadsafety == 3` (serialized SQLite mode);
- a build/runtime without serialized SQLite support fails closed with `sqlite_serialized_threading_required`;
- regression coverage now traverses a real local `ThreadingHTTPServer` worker path and calls `Gateway.ingest_update()` from the request thread;
- aggregate-only privacy receipt and schema constraints remain unchanged;
- sandbox DB path contract remains `/var/lib/wellbeing/telegram-phase1b-sandbox/gateway.sqlite3`;
- cleanup command and confirmation token remain byte-identical to the accepted source package.

Verification:
- `python3 -m py_compile gateway.py test_gateway.py cleanup_sandbox.py test_cleanup.py`;
- `python3 -m unittest -v` -> 24/24 PASS, including threaded HTTP regression.

No live Telegram send, public webhook, deployment, credentials work, production mutation, sudo or host-gate replay is part of this package.

KOD code-level PASS does not replace independent SIS runtime/host verification.
