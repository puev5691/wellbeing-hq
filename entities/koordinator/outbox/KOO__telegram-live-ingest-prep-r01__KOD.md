# KOO → KOD: prepare bounded live Telegram ingestion admission r0.1

status: QUEUED_WAITING_ACTIVE_SLOT
priority: HIGH_EXPERIMENTAL

Verified basis:
- real discussion send/readback PASS `09b6fdfd04da84533185b11b0861b2220b72dfb3`
- synthetic semantic independent PASS `756a0d20791d3fa224d6cb8492df41e9dff3a5d8`

Goal:
prepare, but do not yet execute, the first bounded real-discussion ingestion pilot.

Design constraints:
- ingest only explicitly bounded recent discussion material;
- privacy/minimization before SemanticInput;
- no audience-wide identity capture;
- no raw update-envelope persistence;
- no automatic task dispatch/acceptance;
- output only discussion_state + candidate questions/summary/candidate_task proposal;
- exact operator/live authority required before real ingestion.

Expected preparatory result:
`PASS_KOD_TELEGRAM_LIVE_INGEST_PREP_R01_READY_FOR_AUTHORITY`
or exact blocker/fail.

No live Telegram read in this task.
No live provider call.
