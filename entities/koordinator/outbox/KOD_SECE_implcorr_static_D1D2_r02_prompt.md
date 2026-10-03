# KOD — SECE r0.1 offline simulator static D1+D2 correction successor r0.2

conveyor_attempt: KOD_SECE_IMPLCORR_STATIC_D1D2_R02_A1
attempt_state: AWAITING_OPERATOR_TRANSFER
execution_evidence_profile: CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01
profile_applicability_reason: CROSS_CHAT_FAILURE_REPLACEMENT_RISK
project_time: omitted

АДРЕСАТ: КОДЕР / KOD

Resume-First.

Выполни ТОЛЬКО NEW bounded correction-only successor for the two static defects identified by the latest independent SHD review.

Do NOT replay/resume predecessor KOD v0.6 work.
Do NOT solve or bypass the independent review execution-environment blocker.
Do NOT activate/use/deploy the simulator.

## Exact OPERATOR authority

ОПЕРАТОР явно разрешил в текущем KOO r1.1 chat:

AUTHORIZE_KOD_SECE_R01_IMPLCORR_STATIC_D1_D2_R02 = YES

Authority scope:
one NEW correction-only successor for exactly the two static defects D1+D2 below.

This authority permits:
- fresh preflight/currentness checks;
- offline local source/test correction inside the immutable candidate lineage;
- package-local tests in KOD's own permitted execution environment;
- publication/readback of one NEW immutable corrected candidate successor and terminal result.

This authority does NOT permit:
- historical task replay;
- simulator activation/use/deployment;
- external host/runtime/filesystem mutation to solve SHD review execution blocker;
- provider/model/API/Telegram calls;
- credential access;
- Project Source/canon mutation;
- role/recovery/current-writer mutation;
- production storage/service mutation;
- automatic SHD rereview.

## Current KOD writer

Verify fresh before substantive work:

puev5691/wellbeing-hq:
entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

writer:
emergency replacement KOD v0.7 current chat instance

Historical predecessor v0.6:
technically unavailable by explicit OPERATOR declaration.

Hard boundary:
unknown later chat-only predecessor work = UNKNOWN / NOT_MATERIALIZED / DO_NOT_RECONSTRUCT / DO_NOT_REPLAY.

## KOO reconciliation basis

puev5691/wellbeing-hq@b79ab5c30e308a3cd7a0c9b6eb73051c18dde941:
entities/koordinator/outbox/KOO__SECE-implcorr-review-r01-reconciliation__OPERATOR.md

blob:
32d7de057b1d91d6dafbe2f25a2b00b5a79e6533

terminal:
PASS_KOO_SECE_IMPLCORR_REVIEW_R01_RECONCILIATION_WAITING_OPERATOR_DECISION

That gate is resolved ONLY for this exact D1+D2 correction by the OPERATOR authority above.

## Exact SHD independent review

puev5691/wellbeing-hq@70fbbe5d98b10b0cc9e631e185c2a9d4dea65734:
entities/shardovik/outbox/SHD__SECE-r01-offline-simulator-implcorr-review-r01__KOO.md

blob:
6b0cd7e57e1b7cf72bddf3992a00738c13d07bc2

terminal:
NEEDS_REWORK_SHD_SECE_R01_OFFLINE_SIMULATOR_IMPLCORR_REVIEW_R01

STATIC_CORRECTED_IMPLEMENTATION_VERDICT:
NEEDS_REWORK

INDEPENDENT_EXECUTION_VERDICT:
BLOCKED_REVIEW_EXECUTION_ENVIRONMENT

The two outcome dimensions MUST remain separate.

This KOD task addresses ONLY the static D1+D2 defects.
It does NOT address the SHD execution-environment blocker.

## Exact predecessor corrected implementation candidate

KOD terminal:

puev5691/wellbeing-hq@47c306b818b8fcbe49ca00250d39a3b6b6a08f45:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-implementation-correction-successor-result__KOO.md

blob:
158d2954b29e8e1155c36db7b68cd6a9d7dcb5f7

terminal:
PASS_KOD_SECE_R01_OFFLINE_SIMULATOR_IMPLEMENTATION_CORRECTION_SUCCESSOR_READY_FOR_INDEPENDENT_REVIEW

Predecessor package:

puev5691/wellbeing-hq@8a07768c58013082ab8e6bcb1d92918b8060ecda:
entities/koder/outbox/sece-r01-offline-simulator-implementation-candidate-correction-successor/

tree:
e019ddb0615bf09c647c44e1dffe6a4c2e14f5a6

package identity:
190e2a8d097d929895090b8f80f75d9c19faca738c45417600da3c7a0de4acfe

status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

This predecessor remains immutable.
Create a NEW successor package; do not overwrite it.

## Active execution-evidence profile

Effectivity record:

puev5691/wellbeing-hq@259f4c8dbddc42b4b446ef57fec46f44db1b4e3e:
entities/koordinator/current/CHAT_INFOFIELD_EXECUTION_EVIDENCE_PROFILE_R01.active.md

blob:
079526a9502527fb0be74ffeed087bb3247ebe90

Active semantic profile blob:

db146a594659e48fa0ce51fd9cd81602cf50058e

This NEW attempt uses inter-chat Task Conveyor v1.2 and is profiled because:
CROSS_CHAT_FAILURE_REPLACEMENT_RISK.

Initial durable execution state is materialized separately at:

entities/koordinator/current/execution-evidence/KOD_SECE_IMPLCORR_STATIC_D1D2_R02_A1.md

Do not infer PROCESSING_STARTED from PROMPT publication, dispatch, inbox, activation attempt, readback or initial state.

When substantive correction actually begins, create positive durable PROCESSING_STARTED evidence for this exact attempt, binding the accepted current execution-state version.

Before terminal result, preserve exact attempt identity and do not use last-write-wins.

## Static defect D1 — NEXT_GATE_RULE end-to-end transport

SHD finding:

NextGateResolver itself is substantially corrected and requires:
- aggregation next_gate_class;
- verified result/event;
- ACTIVE CURRENT matching NEXT_GATE_RULE;
- matching verified/current CURRENT_STATE_EVIDENCE when required;
- exact recipient/task_ref;
- exactly one eligible rule.

But ordinary flow does not transport rules end-to-end:

EffectiveContextBuilder
→ ExecutionContractProjector
→ NextGateResolver.

Current defect:
EffectiveContextBuilder does not populate next_gate_rules.

ExecutionContractProjector reads:

ec.get("next_gate_rules", [])

so normal flow receives empty NEXT_GATE_RULE.

The existing passing test manually injects NEXT_GATE_RULE after projection.
That proves only an isolated resolver unit, not the normal pipeline.

### Required D1 correction

Implement a typed, provenance-preserving path whereby applicable NEXT_GATE_RULE evidence enters Effective Context and reaches the L6 contract and NextGateResolver through normal Simulator orchestration.

At minimum preserve for each applicable rule:
- stable rule identity;
- rule source/provenance;
- active/current status;
- scope;
- required next_gate_class;
- verified result/event requirements;
- current-state evidence requirements;
- exact recipient/task_ref only when actually present in active rule evidence;
- conflict/supersession state.

Requirements:
1. EffectiveContextBuilder carries the rule evidence in a reviewed typed structure.
2. Context identity binds this structure.
3. ExecutionContractProjector projects only exact rule evidence from Effective Context.
4. No rule may be invented at L6 or by the resolver.
5. NextGateResolver consumes the projected rule state through ordinary Simulator orchestration.
6. No manual post-projection injection in the end-to-end proof.
7. Historical/superseded/non-active rule cannot route.
8. terminal/result alone cannot route.
9. rule evidence never creates task authority.
10. Task Conveyor authority semantics remain unchanged.

Add direct and end-to-end tests:
- active/current matching rule + verified evidence => grounded candidate;
- missing rule => NONE/UNKNOWN/STOP as reviewed;
- superseded/non-active rule => no route;
- ambiguous multiple eligible rules => conflict/STOP;
- terminal alone => no route;
- raw fixture metadata changed after Effective Context build cannot inject a route.

Return marker:
NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED=YES

## Static defect D2 — StaticValidator transformation proxy / anti-cheat gap

SHD finding:

StaticValidator.evaluate still contains direct transformation_type -> semantic predicate/blocker shortcuts.

Examples include transformation labels such as:
- REMOVE_AUTHORITY_REF;
- SOURCE_ACTIVE_TO_CANDIDATE;
- TASK_CURRENT_TO_SUPERSEDED;
- PROCESSING_STARTED_YES_TO_UNKNOWN;
- ADD_CURRENT_STATE_CONFLICT;
- REPLACE_REQUIRED_HANDOFF_WITH_REDUNDANT_SELF_HANDOFF;
- combined blocker labels.

This means fixture metadata can directly manufacture semantic outcomes instead of mutating state and then letting normal validators derive the outcome.

The existing anti-cheat scan omits StaticValidator and Simulator orchestration.

Therefore:
NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS=YES
is not adequately supported.

### Required D2 correction

Introduce a generic typed mutation/state-transformation layer, or an equivalent reviewed generic mechanism, that:

1. takes a synthetic base semantic state;
2. applies typed mutation to the relevant state/evidence object;
3. produces the mutated semantic state;
4. sends that state through the normal Effective Context / L6 / StaticValidator / guard / classifier / next-gate paths;
5. does NOT map transformation labels directly to validator predicates.

Remove direct transformation_type -> semantic outcome shortcuts from StaticValidator.

StaticValidator must decide from actual post-transformation contract/state only.

Extend anti-cheat coverage to include:
- StaticValidator;
- Simulator orchestration;
- mutation/state-transform layer;
- any path capable of producing validator predicates/blockers.

Tests must prove:
- no transformation label itself is sufficient to create a predicate/blocker;
- equivalent semantic mutation through different fixture metadata yields same validator outcome;
- changing transformation metadata without changing semantic state cannot change core outcome;
- authority/currentness/start/conflict/handoff blockers arise only from mutated semantic state;
- no fixture_id branching;
- no hidden binding-ID parser;
- no oracle leakage;
- no transformation-proxy for core invariants.

Return marker:
STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED=YES

Return marker:
ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION=YES

## Preserve already-closed corrections

Do not regress prior C1-C8 corrections that SHD statically accepted:
- JSON Schema minimum;
- ContextCorrectionEngine fidelity;
- EffectiveContextBuilder reviewed structure;
- C1/L6 authorization-binding projection;
- L6 projection firewall;
- ResultClassifier fidelity;
- strengthened A1-A13 architecture tests except where D1/D2 need additive coverage;
- side-effect/non-authority boundaries.

Preserve:
- reviewed fixture meanings;
- D2 contract identity semantics;
- D3 trace identity semantics;
- L0-L9 topology;
- generic binding derivation;
- oracle separation;
- no fixture-id branching;
- no hidden binding mapping;
- deterministic canonical identities;
- synthetic-only boundary.

## Required offline tests in KOD environment

Run package-local commands against NEW successor bytes:

python3 -m py_compile <all corrected .py modules>

python3 -I -B run_offline_tests.py

python3 -I -B fixture_runner.py

Add dedicated D1+D2 tests.

Required old gates:
SCHEMA_VALIDATION_PASS=YES
FIXTURE_CATALOG_54_OF_54_VALID=YES
TOTAL_FIXTURES_PASS=54/54
INPUT_COMPLETENESS_EXECUTION_PASS=15/15
BINDING_DERIVATION_PASS=15/15
CONTRACT_ID_TEST_VECTORS_PASS=YES
TRACE_ID_TEST_VECTORS_PASS=YES
TRACE_SCHEMA_PASS=YES
ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED=13/13
ORACLE_SEPARATION_TEST_PASS=YES
NO_FIXTURE_ID_BRANCHING_TEST_PASS=YES
NO_HIDDEN_BINDING_MAPPING_TEST_PASS=YES
NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS=YES
DETERMINISM_TESTS_PASS=YES
NO_SIDE_EFFECT_TESTS_PASS=YES

Required new gates:
NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED=YES
STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED=YES
ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION=YES

## Independent execution-environment blocker

Preserve explicitly:

SHD_INDEPENDENT_EXECUTION_ENVIRONMENT_BLOCKER:
UNCHANGED_EXTERNAL_BLOCKER

Do NOT claim this KOD task solves it.

Do NOT mutate external host/runtime/filesystem to solve it.

KOD self-tests remain KOD evidence only and are not independent SHD execution proof.

## Output

Create one NEW immutable corrected implementation successor package, e.g.:

entities/koder/outbox/sece-r01-offline-simulator-implementation-static-d1d2-r02/

Include only what is needed under File Work v2.4, but at minimum:
- corrected source;
- D1/D2 tests;
- updated anti-cheat tests;
- regression tests;
- correction map;
- test results/summary;
- security/boundary statement;
- exact package identity/checksums if package form is used.

Do not create duplicate paperwork merely for form.

Status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

Create terminal result:

entities/koder/outbox/KOD__SECE-r01-implcorr-static-D1D2-r02__KOO.md

Expected terminal:

PASS_KOD_SECE_R01_IMPLCORR_STATIC_D1D2_R02_READY_FOR_INDEPENDENT_REVIEW

or exact NEEDS_REWORK / BLOCKED / FAIL.

Terminal result must include:
- exact OPERATOR authority;
- fresh preflight HEAD;
- exact KOD v0.7 writer identity;
- positive PROCESSING_STARTED evidence ref for this exact attempt;
- predecessor package identity;
- NEW successor locator/tree/blobs;
- D1 and D2 correction map;
- required old/new test markers;
- explicit preserved external execution blocker;
- status candidate NOT_ACTIVATED;
- no historical replay;
- next gate classification only.

## Fresh preflight / stop conditions

Before substantive work:

1. fetch fresh wellbeing-hq HEAD;
2. verify this PROMPT is current and not superseded;
3. verify KOD v0.7 current-writer exact identity;
4. verify no existing terminal/new successor already performs this exact D1+D2 task;
5. verify SHD NEEDS_REWORK exact result/blob;
6. verify predecessor candidate/tree unchanged;
7. verify active execution-evidence profile/current state;
8. verify OPERATOR authority above has not been withdrawn/replaced;
9. verify no competing execution attempt exists.

If conflict/mismatch:
STOP exact blocker.
Do not infer/reconstruct.

## Hard boundaries

historical task replay:
FORBIDDEN

simulator activation/use/deploy:
FORBIDDEN

external host/runtime mutation:
FORBIDDEN

provider/model/API/Telegram:
FORBIDDEN

credentials:
FORBIDDEN

Project Source/canon mutation:
FORBIDDEN

role/recovery/current-writer mutation:
FORBIDDEN

production storage/service mutation:
FORBIDDEN

automatic SHD rereview:
FORBIDDEN

## Stop after result

After immutable publication/readback and RETURN KOO:
STOP.

Do not activate simulator.
Do not try to solve SHD execution environment blocker.
Do not start SHD rereview without new exact authority.
