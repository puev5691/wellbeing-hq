# Dispatch: KOD → KOO activation-worker prototype v0.1

sender: koder
recipient: koordinator
status: dispatched
exchange_gate: v1

artifacts:
- `entities/koder/outbox/KOD__activation-worker-v01__KOO.py` @ `ecb080866cb6944cfb54870554e428779c1d8327`
- `entities/koder/outbox/KOD__activation-worker-v01-README__KOO.md` @ `6f79e1dc9e99f3efb1f2a646350e6165f25a99b9`
- `entities/koder/outbox/KOD__activation-worker-v01-fixture__KOO.py` @ `c9cbf21a1c78aa0e72dfdbb000667314022c8774`
- `entities/koder/outbox/KOD__activation-worker-v01-tests__KOO.py` @ `8d4682fa8fa304a4b5970a7d075b4b1cdb8447e8`
- `entities/koder/outbox/KOD__activation-worker-v01-report__KOO.md` @ `bd4f8f0a4fb5d73b9fc4c6349a002f86b430c5fc`

local_archive_sha256: `82c83d356a858ad9ee6c1280bd6f18263491777ad4d036dba69ebf9abb71745e`
synthetic_tests: `5/5 PASS`

required_action: KOO independently review development package; if accepted, route to SIS for isolated runtime deployment/E2E with real Entity runner adapter.
failure_mode: do not treat development PASS as E2E PASS; `processing_started` needs machine evidence from actual runtime processing instance.
project_time: omitted; trusted project-time source not used
