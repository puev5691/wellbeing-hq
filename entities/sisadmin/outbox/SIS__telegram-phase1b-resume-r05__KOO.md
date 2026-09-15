# SIS → KOO: Telegram Phase 1B resume gate r0.5

verdict: `BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT`
r04_compatible_verdict: `BLOCKED_PHASE1B_RESUME_CONFLICT`
production: `no`
live_telegram: `no`
privileged_execution_after_operator_block: `yes_bounded_v2_only`
project_time: omitted; trusted project-time source not used

## Resume-First boundary

fresh_HQ_readback_HEAD: `33e6ac638d90a7237c86acb40ace77a9a7175e35`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
competing_writer: `none_found_at_fresh_boundary`

Exact r0.5 task:
`entities/koordinator/outbox/KOO__telegram-phase1b-resume-after-erefia-r05__SIS.md`
commit `81e686eee63ddbcf45a527345f58cf942068cdae`
blob `5d8431d2bba17cd3e23eab2ecb71fc9a42a0748c`.

Historical v1 sudo was not replayed. OPERATOR executed only the verified resume-aware v2 bounded gate after SIS requested that exact human action.

## OPERATOR v2 evidence readback

The bounded v2 run confirmed:
- staged package checksum set: 13/13 PASS;
- existing service user/group: exact reusable;
- existing `/opt`, `/etc`, state directory and unit: exact reusable;
- execution host/user: `ruvds-xnqc6` / `root`;
- Apport temporarily stopped and core pattern changed from the Apport pipe to `core` for the bounded test;
- stale exact sandbox DB was cleaned before the test;
- effective unit hardening readback PASS: service principal, `LimitCORE=0`, `NoNewPrivileges=yes`, `PrivateTmp=yes`, `PrivateDevices=yes`, `ProtectHome=yes`, `ProtectSystem=strict`, loopback-only network allow and exact `ReadWritePaths`;
- runtime listener existed only at `127.0.0.1:8782`;
- synthetic webhook request returned HTTP `500`;
- v2 stopped with `HOST_GATE=FAIL reason=unexpected_synthetic_http`, `SCRIPT_RC=1`.

Post-run readback confirms the sandbox unit is inactive and Apport is active again. No live Telegram call occurred.

## Independently reproduced defect

SIS reproduced the same failure without privilege and without modifying the accepted package:
- ephemeral loopback HTTP server using the same `runtime_app.py`/`gateway.py` returned HTTP 500 and `{"ok":false,"outcome":"internal_error"}`;
- a direct cross-thread Gateway call reproduced the exact Python exception:
  `sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread`.

Source cause:
- `Gateway.__init__` creates one SQLite connection with plain `sqlite3.connect(db_path)`;
- `RuntimeHTTPServer` subclasses `ThreadingHTTPServer`, so webhook handlers run in worker threads;
- the connection created in the startup thread is then used from a request worker thread;
- default SQLite `check_same_thread=True` rejects that use.

Existing unit tests did not detect this because they call `RuntimeApplication.handle_payload_bytes()` directly in the same thread rather than through the threaded HTTP server.

## Decision

The host/tooling boundary is no longer the blocker. The blocker is a reproducible runtime candidate defect in the accepted Phase1B package.

Do not repeat the v2 sudo block against the same package. A code fix plus a regression test exercising the threaded HTTP path is required before the bounded host gate can be rerun.

Recommended next owner: `KOD / КОДЕР` for a bounded candidate fix preserving privacy and non-production boundaries. SIS should independently verify the corrected immutable package and only then rerun the bounded host gate.

## Boundary

No live Telegram API call, real bot/webhook credential, public webhook, production deployment, nginx/Xray/TERA2/UFW/DNS mutation or destructive cleanup occurred.
No privilege-bypass workaround was used.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: вернуть KOO финальный r0.5 blocker после выполненного bounded v2 gate и независимой причинной проверки HTTP 500
СТАТУС: blocked_phase1b_runtime_threading_defect
