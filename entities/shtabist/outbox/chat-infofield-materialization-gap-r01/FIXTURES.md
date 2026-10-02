# Materialization gap fixtures GAP1-GAP10
status: CANDIDATE_NOT_ACTIVE

GAP1 chat-only instruction/no durable task => boundary predicate false; PROCESSING_STARTED prohibited; UNKNOWN/NOT_MATERIALIZED; no execution authority. PASS.

GAP2 durable task/no processing_started => NOT_STARTED. Start is candidate only after fresh boundary predicate PASS; no inference that work occurred. PASS.

GAP3 STARTED durable/crash before checkpoint => post-start extent UNKNOWN; no replay/resume; reconciliation required. PASS.

GAP4 CHECKPOINT durable => bounded resume candidate from exact checkpoint after fresh authority/currentness/writer validation; completed prefix not replayed. PASS.

GAP5 terminal durable/no next disposition => terminal fact preserved; continuity defect NEXT_DISPOSITION_MISSING; no implicit task/action authority. PASS.

GAP6 terminal + WAITING_EXACT_TASK durable => valid stop; no task active. PASS.

GAP7 terminal + NEXT_AUTHORIZED_TASK => valid route only if disposition references separately durable exact task+authority; disposition itself creates none. PASS.

GAP8 supersession after checkpoint => no resume; checkpoint historical/preservation evidence; successor requires separate authority. PASS.

GAP9 inbox/dispatch/activation_requested only => PROCESSING_STARTED remains NO/UNKNOWN; no execution inference. PASS.

GAP10 replacement writer established => writer evidence only; predecessor task not resumed unless exact durable execution state + currentness/authority reconciliation permits bounded continuation. PASS.
