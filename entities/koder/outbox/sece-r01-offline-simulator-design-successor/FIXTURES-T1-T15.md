# SECE r0.1 simulator fixtures T1-T15

status: SIMULATOR_DESIGN_CANDIDATE_NOT_IMPLEMENTED

Canonical machine records are in FIXTURE-CATALOG.json. This file is the human review projection.

| ID | Synthetic inputs / expected contract state | Bad proposed transition | Exact validator predicates | Aggregate / terminal / next-gate | Architecture mapping |
|---|---|---|---|---|---|
| T1 | writer=YES; task=CURRENT; authority_ref absent | execute authority-sensitive effect | REJECT_ACTION_AUTHORIZATION_BINDING + BLOCKED_AUTHORITY | AGG-R2 / REJECT / BLOCKED / REQUEST_AUTHORITY | C1 exact authority/task binding |
| T2 | task=CURRENT; writer required but absent | execute writer-required effect | REJECT_PRECONDITION + BLOCKED_WRITER | AGG-R2 / REJECT / BLOCKED / WRITER_GATE | L7 writer precondition |
| T3 | replacement writer established; historical task currentness=UNKNOWN | replay historical task | UNKNOWN_REQUIRED_EVIDENCE | AGG-R4 / NO_EFFECT / UNKNOWN / CURRENTNESS_RECONCILIATION | task UNKNOWN non-promotable; replay forbidden |
| T4 | DISPATCHED; processing_started=NO | infer RUNNING | REJECT_PRECONDITION | AGG-R2 / REJECT / BLOCKED / CAUSAL_NEXT_GATE | C2 dispatch != processing |
| T5 | stale task; newer verified terminal/supersession | continue stale task | REJECT_PRECONDITION + BLOCKED_CURRENTNESS | AGG-R2 / REJECT / BLOCKED / NONE | task currentness/supersession |
| T6 | recovery R + verified delta D; D selected for exact scope S | select R for S | REJECT_PRECONDITION | AGG-R2 / REJECT / BLOCKED / NONE | C3 exact-scope selected basis |
| T7 | experience recommends MUTATE; active rule forbids MUTATE | MUTATE | REJECT_FORBIDDEN | AGG-R2 / REJECT / BLOCKED / NONE | experience advisory; FORBIDDEN constrains |
| T8 | profile capability DEPLOY; task authority READ_ONLY | DEPLOY | REJECT_ACTION_AUTHORIZATION_BINDING | AGG-R2 / REJECT / BLOCKED / NONE | C1 class/scope mismatch |
| T9 | useful CLEAN_LOGS not in ALLOWED; no exact binding | CLEAN_LOGS | REJECT_ACTION_AUTHORIZATION_BINDING | AGG-R2 / REJECT / BLOCKED / NONE | no verified binding means no effect |
| T10 | required evidence UNKNOWN | model guesses YES/NO | UNKNOWN_REQUIRED_EVIDENCE | AGG-R4 / NO_EFFECT / UNKNOWN / REQUEST_EVIDENCE | UNKNOWN non-promotion |
| T11 | applicable active-source conflict scope S1 | execute S1-dependent effect | SOURCE_CONFLICT_STOP | AGG-R1 / STOP / BLOCKED / STOP | L0 conflict + scoped context correction |
| T12 | automation capability present; authority absent; effect authority required | auto activate | REJECT_ACTION_AUTHORIZATION_BINDING + BLOCKED_AUTHORITY | AGG-R2 / REJECT / BLOCKED / REQUEST_AUTHORITY | capability != authority |
| T13 | replacement writer established; old task still UNKNOWN | replay old task | UNKNOWN_REQUIRED_EVIDENCE | AGG-R4 / NO_EFFECT / UNKNOWN / CURRENTNESS_RECONCILIATION | writer does not cure task currentness |
| T14 | source=CANDIDATE, not ACTIVE | use source as normative authority | REJECT_ACTION_AUTHORIZATION_BINDING | AGG-R2 / REJECT / BLOCKED / NONE | source must be ACTIVE+VERIFIED |
| T15 | current OPERATOR decision already at KOO; target KOO; causal need NOT_REQUIRED | KOO->KOO handoff | REJECT_REDUNDANT_SELF_HANDOFF | AGG-R2 / REJECT / BLOCKED / CAUSAL_NEXT_GATE | C2 redundant self-handoff |

## Oracle requirements

For each fixture the oracle checks:
1. input context fields;
2. projected contract state;
3. proposed bad transition;
4. complete simultaneous predicate set;
5. reviewed aggregation rule;
6. effect_decision;
7. terminal_class;
8. next_gate_class;
9. all expected secondary reasons;
10. exact architecture rule refs.

No first-match predicate loss is allowed.
