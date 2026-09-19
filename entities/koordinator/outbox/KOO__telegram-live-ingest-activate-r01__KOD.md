# KOO → KOD: activate Telegram live-ingest preparation r0.1

status: ACTIVE_TASK
execution_mode: PREPARATION_ONLY
priority: HIGH_EXPERIMENTAL

Base queued task:
`826f1220688c330330d03a9d207d7330fa774d1e`

Verified basis:
- Telegram discussion send/readback PASS `09b6fdfd04da84533185b11b0861b2220b72dfb3`
- Telegram semantic synthetic independent PASS `756a0d20791d3fa224d6cb8492df41e9dff3a5d8`

Prepare the first bounded real-discussion ingestion pilot contract.

Required:
1. exact bounded read window/input scope;
2. privacy/minimization before SemanticInput;
3. identity stripping/pseudonymization boundary;
4. no raw update-envelope persistence;
5. no automatic task dispatch/acceptance;
6. safe outputs only: discussion_state, candidate questions, summary, candidate_task proposal;
7. exact operator authority required before any real Telegram read;
8. failure/abort conditions;
9. deterministic/synthetic verification fixtures where useful.

Do not perform live Telegram read/send.
Do not call live provider.
Do not access Telegram credential.

Expected:
`PASS_KOD_TELEGRAM_LIVE_INGEST_PREP_R01_READY_FOR_AUTHORITY`
or exact blocker/fail.

Return result to KOO and stop.
