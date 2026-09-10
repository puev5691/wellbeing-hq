# Dispatch: KOD → KOO activation-worker prototype v0.2

sender: koder
recipient: koordinator
status: dispatched
exchange_gate: v1
inbox_path: `entities/koordinator/inbox/KOD__activation-worker-v02__KOO.md`

artifacts:
- `entities/koder/outbox/KOD__activation-worker-v02__KOO.py` @ `fc1fa131c732e599f778ce242ae1f8f04c36575f`
- `entities/koder/outbox/KOD__activation-worker-v02-README__KOO.md` @ `f8f7544c4cb0808a3fd8e2c06ba82f2d64da1a1d`
- `entities/koder/outbox/KOD__activation-worker-v02-tests__KOO.py` @ `9e28b48e4e66068214744eb798dff54c17c33c16`
- `entities/koder/outbox/KOD__activation-worker-v02-report__KOO.md` @ `6c40ac8f3c1cfb81c8a922265c1ac02166727b67`

local_archive_sha256: `405dbd982a6b8f8b813e397a4609e63d3cf57c76bd4ea85ea46197fe2cc17d89`
synthetic_tests: `8/8 PASS`
review_defect_closed: immutable commit/blob/path/dispatch provenance validation added before `processing_started`

required_action: KOO independently review v0.2; if accepted, authorize SIS isolated runtime/E2E.
failure_mode: do not treat development PASS as full E2E PASS; fake/mismatched provenance must fail before `processing_started`.
project_time: omitted; trusted project-time source not used
