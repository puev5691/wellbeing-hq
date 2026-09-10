# Dispatch: KOD → KOO activation-worker v0.2 verification fix

sender: koder
recipient: koordinator
status: dispatched
exchange_gate: v1
inbox_path: `entities/koordinator/inbox/KOD__activation-worker-v02-fix__KOO.md`

artifacts:
- `entities/koder/outbox/KOD__activation-worker-v02__KOO.py` @ `76cdcac8fe354d6271cfe2ae29bdc07b58f66cff`, blob `c680878806fd2fb6d20df8b6e8938d3f3ead5053`
- `entities/koder/outbox/KOD__activation-worker-v02-tests__KOO.py` @ `9e28b48e4e66068214744eb798dff54c17c33c16`, blob `af487683afcc462e44a07f8e0a46c5bab7e31e94`
- `entities/koder/outbox/KOD__activation-worker-v02-fix-report__KOO.md` @ `3b8524374020f1039690b2630b0f90c0e6606ee2`, blob `c1848625f3821d4770279924606cba959fdffb04`

actual_suite: `8/8 PASS`
defect_closed: distinguish missing commit from provider unavailable/query failure before `processing_started`
required_action: KOO independently review corrected worker and exact-suite evidence; if accepted, authorize the next permitted isolated runtime/E2E step.
failure_mode: do not treat this dispatched fix as received or accepted without Exchange Gate evidence.
project_time: omitted; trusted project-time source not used
