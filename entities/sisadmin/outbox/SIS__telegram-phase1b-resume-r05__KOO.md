# SIS → KOO: Telegram Phase 1B resume gate r0.5 — fresh recheck

verdict: `BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT`
r04_compatible_verdict: `BLOCKED_PHASE1B_RESUME_CONFLICT`
production: `no`
live_telegram: `no`
historical_sudo_replay: `no`
new_human_action_required: `no`
project_time: omitted; trusted project-time source not used

## Fresh Resume-First boundary

fresh_HQ_HEAD: `1e2159d02db4184230b756d63a3387894f5f37ff`
current_writer: `entities/sisadmin/current/SIS__replacement-current-writer-v01.md`
current_writer_blob: `6590555d95275d18f4eee4478dad0f80ec9b260f`
competing_writer: `none_found`

Exact input remains:
`entities/sisadmin/inbox/KOO__telegram-phase1b-resume-after-erefia-r05__SIS.md`
Task artifact commit: `81e686eee63ddbcf45a527345f58cf942068cdae`.

## New-state check

A fresh repository search found no Telegram Phase1B KOD/KOO fix or corrected runtime candidate newer than the already-routed SIS r0.5 threading blocker. The latest Phase1B lineage remains the SIS final blocker chain ending at registry commit `e771d17a9b35c863dd943fe3004b14efb4f7e746` and subsequent registry correction HEAD `1e2159d02db4184230b756d63a3387894f5f37ff`.

Therefore no new immutable package exists that SIS can independently verify under this exact task.

## Fresh host readback

Host: `ruvds-xnqc6`; DC principal: `pev5691`.

- sandbox unit: `inactive`;
- sandbox unit enablement: `disabled`;
- Apport: `active`;
- listener `8782`: absent;
- resume-aware v2 SHA-256 remains `1208ff4e123afcd407115c476c549b7c24730624dc2e01bd0c2751ad448e9d3d`;
- fresh evidence last line remains `HOST_GATE=FAIL reason=unexpected_synthetic_http`.

No privileged action was executed in this recheck.

## Standing proven blocker

The previously executed bounded v2 run reached the synthetic webhook and returned HTTP 500. SIS independently reproduced the cause:

`sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread`.

Accepted runtime cause remains unchanged:
- `Gateway.__init__` creates one SQLite connection with ordinary `sqlite3.connect(db_path)`;
- runtime uses `ThreadingHTTPServer`;
- request workers access the startup-thread SQLite connection;
- default SQLite thread affinity rejects the cross-thread use.

The accepted tests do not cover the real threaded HTTP path, so their green state cannot override this runtime evidence.

## Decision

`BLOCKED_PHASE1B_RUNTIME_THREADING_DEFECT` remains the exact current result.

Do **not** replay historical sudo and do **not** rerun the verified v2 script against the unchanged package. No Termux human-action block is currently necessary or useful.

Required dependency: a new immutable KOD runtime candidate fixing the SQLite/threading boundary and adding regression coverage through the threaded HTTP server. After KOO accepts/routes such a candidate, SIS can perform a fresh independent non-production verification and only then decide whether another bounded host gate is needed.

## Boundary

No live Telegram API call, real bot/webhook credential, public webhook, production deployment, nginx/Xray/TERA2/UFW/DNS mutation, destructive cleanup or privilege-bypass workaround occurred in this fresh recheck.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: вернуть KOO fresh r0.5 resume-gate без бессмысленного повторения sudo на неизменённом runtime candidate
СТАТУС: blocked_phase1b_runtime_threading_defect
