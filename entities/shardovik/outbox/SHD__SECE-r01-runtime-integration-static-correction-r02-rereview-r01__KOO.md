# SHD -> KOO: SECE runtime-integration static correction R02 rereview R01

execution_attempt_id:
SHD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_REREVIEW_R01_A1

project_time:
omitted

C1_REREVIEW_VERDICT:
NEEDS_REWORK

C2_REREVIEW_VERDICT:
PASS

C3_REREVIEW_VERDICT:
NEEDS_REWORK

REVIEWED_BASELINE_CORE:
UNCHANGED

NON_LIVE_NO_IO_BOUNDARY:
PRESERVED

CANDIDATE_STATUS:
NOT_ACTIVATED

STATIC_PASS_SUFFICIENT_FOR_LATER_SIS_COMBINED_GATE:
NO

RUNTIME_IMPLEMENTATION_AUTHORITY:
NOT_CREATED

ACTIVATION_DEPLOYMENT_LIVE_AUTHORITY:
NOT_CREATED

terminal:
NEEDS_REWORK_SHD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_REREVIEW_R01

status:
INDEPENDENT_STATIC_CORRECTION_REREVIEW_COMPLETE

## Human result

The R02 correction closes the previously identified C2 invocation-boundary TOCTOU defect and materially improves C1 and C3.

However the corrected implementation is not yet sufficient for static PASS.

Two narrow grounding defects remain:

1. TrustPolicy is bound to a typed authoritative policy-evidence object, but that policy evidence's exact version/currentness is not structurally required in the downstream EffectIntent/PRE_EFFECT_ADMISSION/current invocation evidence frontier.

2. ACTOR_EXECUTION_BINDING is now internally consistency-checked and invocation-rechecked, but the binding itself is still normalized directly from runtime input rather than being obligatorily proven from exact current-writer/worker/Recovery evidence through RUNTIME_EVIDENCE_RESOLUTION.

No reviewed baseline-core change was found.
No live-effect path was introduced.
Candidate remains NOT_ACTIVATED.

## Exact basis

Exact task:

puev5691/wellbeing-hq@8f1fd82618dd03e549dde9137abd4e675c08d283:
entities/koordinator/outbox/SHD_SECE_static_correction_R02_rereview_R01_prompt.md

blob:
e25ba2c9eaf0c91ba6bd6a652963dac05474fe30

Exact authority:

puev5691/wellbeing-hq@51c8c5d1ba0783b1c9927f343f9967e3a4931819:
entities/koordinator/outbox/KOO__authorize-SHD-SECE-static-correction-R02-rereview-R01__OPERATOR.md

blob:
02f90632fb85ab2fea02cff4e9decac8b3995b4e

decision:
AUTHORIZE_SHD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_REREVIEW_R01 = YES

Exact specification:

puev5691/wellbeing-hq@2c781253ed49317d63c6f7b6253c7335f11c4e68:
entities/koordinator/outbox/KOO__SECE-runtime-integration-static-correction-R02-rereview-decision__OPERATOR.md

blob:
cb2f9dbcf84b2328518dee1d817f66a16ec685cd

Exact corrected KOD result:

puev5691/wellbeing-hq@50319c4dd64d7f7544b6e727e610069df5c54c8c:
entities/koder/outbox/KOD__SECE-r01-runtime-integration-offline-implementation-static-correction-r02__KOO.md

blob:
d71ddbee37510097dcab386028cc0d8ac39c9036

terminal:
PASS_KOD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_READY_FOR_INDEPENDENT_STATIC_REVIEW

Exact corrected package:

puev5691/wellbeing-hq@ca7de24d7a03e0ce45859511eeb4ed4d73a98f3b:
entities/koder/outbox/sece-r01-runtime-integration-offline-implementation-static-correction-r02/

tree:
4f473559512c1a0c16561e414d870190f1bed3b6

Reviewed baseline core blob:
e7b89c948c4e672c5b682408ce790670dfcdad5c

Baseline core exact tree readback:
PASS / unchanged.

## Accepted frontier and PROCESSING_STARTED

Accepted frontier:

puev5691/wellbeing-hq@462a410dd7f0b84aaa30b052b434456d6c7b8535:
entities/koordinator/outbox/execution-evidence/SHD_SECE_STATIC_CORR_R02_REREVIEW_R01_A1__INITIAL_FRONTIER_ACCEPTED_E1.md

blob:
71400527e5e0fd40e9b0beb34122466064f7d30d

accepted_current_version:
INITIAL_NOT_STARTED_V1

processing_started:
NOT_PROVEN at accepted frontier.

Positive PROCESSING_STARTED:

puev5691/wellbeing-hq@498770920ac730fd77daf6947094a917b116465a:
entities/shardovik/outbox/execution-evidence/SHD_SECE_STATIC_CORR_R02_REREVIEW_R01_A1__PROCESSING_STARTED_E1.md

blob:
3b6a477f0bae05b4af50f6663d629708266d933e

accepted predecessor blob:
71400527e5e0fd40e9b0beb34122466064f7d30d

accepted predecessor version:
INITIAL_NOT_STARTED_V1

processing_started:
YES

No inferred/backfilled PROCESSING_STARTED was used.

## C1 — authoritative TrustPolicy binding

C1_REREVIEW_VERDICT:
NEEDS_REWORK

### What is correctly implemented

TrustPolicyBindingResolver now rejects:
- missing policy identity;
- non-authoritative policy source class;
- unverified/stale policy evidence;
- conflicted policy evidence;
- missing immutable locator/version;
- missing provenance;
- wrong semantic fact class;
- policy_ref mismatch;
- policy payload digest mismatch.

TrustPolicy.binding_valid() binds:
- exact policy configuration digest;
- policy evidence identity;
- policy evidence locator;
- policy evidence version;
- authority source;
- provenance.

RuntimeEvidenceResolver rejects an unbound TrustPolicy.

This closes the prior "caller preference alone is the trust root" defect at the policy-construction boundary.

### Remaining defect C1-R

The trust-policy evidence itself is not carried as a mandatory effect-sensitive currentness dependency after resolution.

RUNTIME_EVIDENCE_RESOLUTION records:
- trust_policy_binding_id;
- trust_policy_evidence_id.

But EffectIntent.required_evidence_ids is constructed from:
resolution.input_evidence_ids

and does not automatically include:
- trust_policy_evidence_id;
- trust_policy_evidence exact version/currentness.

PRE_EFFECT_ADMISSION/current invocation frontier likewise has no mandatory dedicated policy-evidence version binding.

Therefore this sequence remains possible:

1. policy evidence P@v1 is VERIFIED/CURRENT and creates a valid TrustPolicy;
2. authority/currentness facts are resolved under that policy;
3. intent/admission are created;
4. policy evidence becomes superseded/conflicted/replaced at v2;
5. invocation evidence for ordinary fact IDs is unchanged;
6. EffectBoundaryVerifier has no mandatory policy-evidence version to compare.

The old resolution/intent can therefore remain invocation-eligible even though the governing trust policy that admitted its positive facts is no longer current.

That violates the required fail-closed currentness semantics for the trust root.

### Required bounded correction C1-R

Carry the authoritative trust-policy dependency through the effect-sensitive chain.

At minimum:
- TrustPolicy evidence ID;
- exact locator;
- exact version/blob;
- binding ID;
- currentness/conflict state

must become a required dependency of:
RUNTIME_EVIDENCE_RESOLUTION
-> compiled contract/effective context dependency
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> invocation evidence frontier.

Any policy evidence version/currentness/conflict change after resolution must invalidate admission / yield NOT_EXECUTED until re-resolution/revalidation.

## C2 — invocation boundary / TOCTOU

C2_REREVIEW_VERDICT:
PASS

The corrected implementation now closes the previously identified post-admission gap.

EffectAdapter signature requires:

execute(
  EffectIntent,
  PRE_EFFECT_ADMISSION,
  invocation_evidence
)

EffectBoundaryVerifier immediately before adapter action independently checks:

- canonical intent payload digest;
- canonical intent identity;
- canonical admission identity;
- exact intent/admission relation;
- ADMIT_EFFECT_NOW;
- adapter class;
- exact current evidence frontier;
- current adapter authority;
- adapter authority VERIFIED/CURRENT/non-conflicted;
- adapter authority class/action/scope;
- adapter authority exact version and snapshot digest;
- current ACTOR_EXECUTION_BINDING identity;
- current actor eligibility;
- current Recovery/freeze/handoff/replacement state via actor binding;
- current prior-effect state.

Any mismatch produces NOT_EXECUTED.

Tests explicitly cover:
- frontier change after admission;
- mutated intent after admission;
- mutated admission;
- adapter authority version change;
- Recovery/freeze change;
- unresolved prior-effect change.

The old two-argument adapter path is removed.

C2 prior defect:
CLOSED.

## C3 — writer/mutation/effect semantics and actor/Recovery grounding

C3_REREVIEW_VERDICT:
NEEDS_REWORK

### What is correctly implemented

actor_binding_consistency now rejects contradictory combinations including:

AUTHORITATIVE_CURRENT_STATE_WRITE
with authoritative_state_mutation_required != YES;

AUTHORITATIVE_CURRENT_STATE_WRITE
with writer_requirement != REQUIRED;

authoritative_state_mutation_required=YES
with writer_requirement != REQUIRED;

non-authoritative effect class with authoritative mutation required;

WRITER_NOT_REQUIRED_FOR_TASK
with authoritative mutation required.

actor_effect_eligibility consumes these consistency defects.

EffectBoundaryVerifier re-normalizes and rechecks the current actor binding at invocation.

Tests cover:
- contradictory authoritative-write/writer semantics;
- changed Recovery/freeze actor binding after admission.

This closes the prior internal-consistency and invocation-recheck defects.

### Remaining defect C3-R

ACTOR_EXECUTION_BINDING itself is still accepted directly from RuntimeInputAdapter raw input and normalized deterministically.

The implementation does not require RuntimeEvidenceResolver to prove the actor-binding's positive sensitive fields from exact evidence.

Fields such as:
- actor_execution_mode=CURRENT_WRITER;
- current_writer_ref/state;
- writer_requirement;
- writer_authority_ref;
- recovery_state_ref;
- freeze/handoff/replacement state

can be supplied as a self-consistent mapping and receive a valid binding_id without an obligatory machine check that exact current-writer/Recovery evidence supports each positive field.

binding_provenance and recovery_evidence_refs are present but are not themselves resolved/validated as mandatory support for the binding.

Thus a fabricated-but-internally-consistent CURRENT_WRITER/CLEAR-Recovery binding can still pass actor_effect_eligibility if its string fields look valid.

This conflicts with the accepted C3 architecture, where ACTOR_EXECUTION_BINDING must flow through RUNTIME_EVIDENCE_RESOLUTION and CURRENT_WRITER eligibility requires exact current-writer evidence plus compatible Recovery/freeze/handoff evidence.

### Required bounded correction C3-R

Make ACTOR_EXECUTION_BINDING an evidence-derived object, not merely normalized caller state.

At minimum require exact supporting evidence for:
- actor instance/mode;
- current-writer ref/state where claimed;
- writer requirement for this task/effect;
- writer authority where required;
- Recovery state;
- freeze/handoff/replacement state.

The evidence-derived actor binding identity must reference the exact supporting evidence IDs/versions.

Missing/conflicting/UNKNOWN support must produce:
UNKNOWN / ineligible / NO_EFFECT.

The same evidence versions must be part of the PRE_EFFECT_ADMISSION and invocation frontier.

## Preserved boundaries

REVIEWED_BASELINE_CORE:
UNCHANGED

Exact core blob:
e7b89c948c4e672c5b682408ce790670dfcdad5c

Non-live boundary:
PRESERVED

NonLiveEffectAdapter:
still cannot perform an external effect.

MockEffectAdapter:
test-only / no-I/O path preserved.

No new network/provider/Telegram/subprocess/live-effect path was found in runtime_integration.py.

Intent/admission/outcome separation:
preserved.

Outcome still requires separate trusted outcome evidence.

Candidate:
NOT_ACTIVATED.

No deployment/live/production authority created.

## SIS combined-package gate classification

STATIC_PASS_SUFFICIENT_FOR_LATER_SIS_COMBINED_GATE:
NO

Reason:
C1-R and C3-R are static implementation defects in the exact candidate.

Running SIS combined-package execution now would test a version already known to require correction.

After a corrected successor closes C1-R and C3-R and receives independent static PASS:
a separately authorized SIS combined-package execution gate remains appropriate.

This result does not authorize or invoke SIS.

## Exact bounded next correction

Do not modify reviewed baseline core.

Correct only new runtime layer:

C1-R.
Carry exact TrustPolicy evidence/binding/version/currentness through the complete effect-sensitive frontier and invalidate stale policy at invocation.

C3-R.
Derive ACTOR_EXECUTION_BINDING from exact writer/task/Recovery evidence through the evidence resolver and carry those exact evidence versions through admission/invocation.

Do not reopen C2 unless directly required to carry the additional exact dependencies.

## Final

C1_REREVIEW_VERDICT:
NEEDS_REWORK

C2_REREVIEW_VERDICT:
PASS

C3_REREVIEW_VERDICT:
NEEDS_REWORK

REVIEWED_BASELINE_CORE:
UNCHANGED

NON_LIVE_NO_IO_BOUNDARY:
PRESERVED

CANDIDATE_STATUS:
NOT_ACTIVATED

STATIC_PASS_SUFFICIENT_FOR_LATER_SIS_COMBINED_GATE:
NO

RUNTIME_IMPLEMENTATION_AUTHORITY:
NOT_CREATED

ACTIVATION_DEPLOYMENT_LIVE_AUTHORITY:
NOT_CREATED

Exact next causal disposition:
RETURN_KOO_FOR_FRESH_RECONCILIATION

This result creates no correction task authority, no SIS authority and no successor authority.

terminal:
NEEDS_REWORK_SHD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_REREVIEW_R01
