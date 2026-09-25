# КОДЕР → КОО: synthetic detector → worker v0.2, матрица r0.1

status: BLOCKED_KOD_DETECTOR_WORKER_R01_EVENT_AUTHORITY_INTERFACE
scope: offline synthetic fixture only; no real Entity activation

## Основание и способ проверки

Exact KOO task: `puev5691/wellbeing-hq@f76b05052916b8014cb34f949e9f19db2131edc5:entities/koordinator/outbox/KOO__autonomous-conveyor-detector-worker-isolated-probe-r01__KOD-OPERATOR.md`, blob `0295e1511a292ae1e686284352a0ae614f91415f`.

Preflight: HQ HEAD `f76b05052916b8014cb34f949e9f19db2131edc5`, tree `b6f36b1e25dfb6a1cc9f970808ed636397574c2a`; current KOD writer v0.5 blob `cf1c84f9df7c90509703e4885844d0cf871ff412`; six approved Project Sources loaded from local approved copies under `mlprep/sources/`. No competing version of this probe observed at preflight.

The fixture creates a new local Git repository with synthetic artifact, dispatch and inbox commits; models detector selection using Git `diff --name-only`; reads the exact worker v0.2 bytes from its existing outbox file, Git blob `c680878806fd2fb6d20df8b6e8938d3f3ead5053`; invokes it with a read-only Git provider interface and a synthetic handler. A local mirror has no project data, network or project credentials. Fixed Git dates make the output deterministic. Evidence is the published `RESULTS.json`; raw case evidence exists transiently inside the local temporary fixture and is summarized there. `PYTHONDONTWRITEBYTECODE=1` was set. This test changes no production path.

`TEST_EXECUTED` means the invocation occurred. It does not imply a passing integration criterion. `DESIGN_ONLY/UNKNOWN` denotes an absent, untested or unverifiable safety property.

| Case | Expected safety result | Actual offline observation | Classification |
|---|---|---|---|
| 1 exact event/artifact/dispatch | Exact event binding and synthetic handler invocation | Detector model sees changed inbox path; worker checks immutable artifact and dispatch, returns `result_dispatched` and synthetic result. It does **not** receive detector commit/event digest. | TEST_EXECUTED for artifact/dispatch/handler; event-to-worker identity binding UNKNOWN |
| 2 commit/blob mismatch | Stop before handler | Modified blob: exit 21, `activation_failed`, `artifact_blob_mismatch`, no marker | TEST_EXECUTED PASS for blob mismatch; separate commit mismatch covered by earlier SIS worker tests, not this probe |
| 3 wrong recipient/dispatch | Stop before handler | Modified recipient: exit 21, `activation_failed`, `dispatch_recipient_mismatch`, no marker | TEST_EXECUTED PASS for this mutation; wrong dispatch path variant not executed |
| 4 duplicate event same digest | No second handler | First invocation succeeds; second identical immutable item returns exit 23, `immutable_item_already_processed_explicit_retry_required`, no second result | TEST_EXECUTED for worker item dedupe; external event digest not read, event dedupe UNKNOWN |
| 5 duplicate event ID, changed digest | Detect collision and block | Altered external event digest, but worker receives neither ID nor digest; second same immutable item returns generic exit 23. No collision check. | TEST_EXECUTED invocation; required collision behavior DESIGN_ONLY/UNKNOWN |
| 6 missing exact task authority | Stop before handler | No authority field supplied; worker returns `result_dispatched`, synthetic handler invoked | TEST_EXECUTED FAIL; missing interface |
| 7 missing approved source or recovery ref | Stop before handler | Missing recovery identity: exit 22 and `recovery_missing_fields:recovery_identity`; missing approved source ref: worker returns `result_dispatched`, synthetic handler invoked | TEST_EXECUTED PASS only for recovery field; source obligation FAIL/UNKNOWN |
| 8 unavailable Git provider | Stop before handler | Invalid local provider path: exit 21, `provider_unavailable_or_unreadable`, no marker | TEST_EXECUTED PASS |
| 9 handler failure | Record failure and signal failure to supervisor | Marker `processing_failed`, handler_exit 9, no result, but worker process exit is **0** because `main()` return value is ignored in `__main__` | TEST_EXECUTED PARTIAL; supervisor exit-code signal FAIL |
| 10 worker marker, no externally observed Entity | Do not infer actual Entity processing | Local `processing_started` marker followed by `result_dispatched` for synthetic handler; no Entity instance observation exists | TEST_EXECUTED for local marker; real `processing_started` UNKNOWN / NOT_ESTABLISHED |

## Causal blocker and minimal correction candidate

The accepted worker accepts `locator`, `artifact`, `recovery`, `git-repo`, state/evidence/result and handler command. Locator schema has no `event_id`, `event_digest`, detector `event_commit`, exact task authority identity, or approved source set. Hence no verifiable binding from detector event through task authority/source admission to worker. A wrapper that merely passes current fields would bypass required checks. The local demonstration positively shows absent authority and source still invoke handler. The detector workflow itself does not call this worker and continues to record `activation_failed / processing_started=no`.

Minimal **PROPOSED**, not implemented: define a versioned detector-event envelope with immutable source commit, inbox path/blob, recipient, event ID/digest; add exact task authority and mandatory approved source/recovery identities in an independently verifiable admission contract; bind these to worker activation ID and persistent dedupe key, reject duplicate ID with changed digest, fail closed before handler for missing/mismatched references. Specify supervisor-visible nonzero exit for handler failure, and external Entity instance observation as a separate gate before real `processing_started`. Then independently check each missing/changed field and actual transport boundary in an authorized successor isolated probe. No automatic resume authority follows from this proposal.

The worker contract gap is a blocker to a ten-case integration PASS. Exact terminal: `BLOCKED_KOD_DETECTOR_WORKER_R01_EVENT_AUTHORITY_INTERFACE`. Durable checkpoint, actual Entity processing, Fast Memory, automatic chat resume and project acceptance are not established. Memory-layering attempt 3 remains `NOT_AUTHORIZED`.
