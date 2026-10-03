# r0.2 documentary synthetic fixtures
status: CANDIDATE_NOT_ACTIVE
fixture_status: SYNTHETIC_DOCUMENTARY_CASES_NOT_RUNTIME_TESTS
These are not historical KOD evidence and are not claims of executed PASS.

GAP1
input: synthetic chat instruction; no verified durable task/authority materialization.
attempt: A1 hypothetical.
predicate: task boundary eligibility.
expected: AUTHORITY_NOT_ESTABLISHED / UNKNOWN; no processing eligibility/start.
alternative: if exact authority/task later verified, evaluate fresh; do not reconstruct history.

GAP2
input: synthetic verified task+authority + accepted INITIAL_NOT_STARTED state/current frontier; no PROCESSING_STARTED evidence.
attempt A2.
predicate: start evidence.
expected: PROCESSING_NOT_PROVEN; state frontier INITIAL_NOT_STARTED; start may be requested only after fresh eligibility.
alternative: missing initial-state acceptance/currentness => UNKNOWN, not NOT_STARTED.

GAP3
input: synthetic PROCESSING_STARTED evidence; instance unavailable before checkpoint.
attempt A3.
predicate: crash tail.
expected: post-start extent UNKNOWN; no replay/resume.
alternative: separately evidenced effect/result may narrow UNKNOWN.

GAP4
input: synthetic scoped checkpoint covering prefix P; possible tail T unmaterialized.
attempt A4.
predicate: checkpoint coverage.
expected: P evidenced; T UNKNOWN; overlapping retry/resume blocked pending tail/effect reconciliation.
alternative: verified no-tail/outcome evidence may permit bounded continuation under fresh authority/currentness.

GAP5
input: synthetic verified TERMINAL; no next disposition.
attempt A5.
predicate: terminal vs continuity.
expected: TERMINAL preserved + NEXT_DISPOSITION_MISSING; TERMINAL_COMPLETE_FOR_CONTINUITY=false; no replay.
alternative: later verified disposition makes continuity property complete without changing terminal fact.

GAP6
input: synthetic TERMINAL + verified WAITING_EXACT_TASK disposition.
attempt A6.
predicate: continuity completion.
expected: valid stop; no active next task authority.
alternative: stale/unverified disposition => continuity incomplete.

GAP7
input: synthetic TERMINAL + disposition NEXT_AUTHORIZED_TASK referencing separately verified current task+authority.
attempt A7.
predicate: successor authority independence.
expected: route candidate valid only because independent task authority verifies.
alternative: missing/stale authority => AUTHORITY_NOT_ESTABLISHED; disposition cannot manufacture it.

GAP8
input: synthetic checkpoint then verified supersession.
attempt A8.
predicate: currentness.
expected: no resume; checkpoint historical evidence.
alternative: successor task requires separate authority.

GAP9
input: synthetic inbox/dispatch/activation_requested evidence only.
attempt A9.
predicate: PROCESSING_STARTED evidence.
expected: PROCESSING_NOT_PROVEN / UNKNOWN. Do not label NO unless explicit accepted frontier establishes no recorded start as of that frontier.
alternative: separate valid PROCESSING_STARTED event changes state.

GAP10
input: synthetic REPLACEMENT_WRITER_ESTABLISHED; predecessor task/execution currentness unverified.
attempt A10.
predicate: replacement continuity.
expected: no resume; UNKNOWN_REQUIRES_RECONCILIATION.
alternative: exact current execution evidence + authority/currentness may permit bounded continuation.

All conclusions bind to explicit durable causal evidence, not chronology/chat recollection.
