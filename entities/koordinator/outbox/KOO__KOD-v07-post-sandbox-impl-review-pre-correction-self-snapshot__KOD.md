# KOO -> KOD v0.7: post-review pre-correction self-snapshot

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
KOD / КОДЕР v0.7 current writer

attempt:
KOD_V07_POST_SANDBOX_IMPL_REVIEW_PRE_CORRECTION_SELF_SNAPSHOT_R01_A1

scope:
PRESERVATION_SELF_SNAPSHOT_ONLY

project_time:
omitted

Resume-First.

Perform ONLY a current-writer self-snapshot after the completed sandbox implementation R01 and its independent SHD review.

Do NOT implement corrections.
Do NOT mutate candidate af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2.
Do NOT create G4/G5/G6 authority.
Do NOT execute sandbox effects.
Do NOT replay historical tasks/prompts.

## Exact authority

puev5691/wellbeing-hq@1fe9f969f091635795ba0e04b8d8f976e4c50922:
entities/koordinator/outbox/KOD_v07_post_sandbox_impl_review_pre_correction_snapshot_authority.md

blob:
ba42233fb21d9d72189f0e483ec88fd69ae3bd92

status:
CANON_TRIGGER_AUTHORITY_RECORDED

## Registry

puev5691/wellbeing-hq@b87bf5c66375e1fe1d9905413cc48c11087163d9:
entities/koordinator/outbox/KOD_v07_post_sandbox_impl_review_pre_correction_snapshot_registry.md

blob:
bbf0c50ac5e2c797044ec0187eeda124b49d5ce7

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@01715f80f070ec05025d0f618e18ec8c1bbe6b37:
entities/koordinator/outbox/KOD_v07_post_sandbox_impl_review_pre_correction_snapshot_frontier.md

blob:
1995e8d699cbacf8cc58daf83902dd73e6f88b15

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current KOD writer

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

Verify continuity with this exact current KOD v0.7 instance.

If writer changed/superseded or competing preservation exists:
STOP with exact blocker.

## Existing external KOD recovery

puev5691/wellbeing-entity-bootstrap@34650c6b255ad204674b778de8d39910a61ba8f1:
entities/kod/recovery/versions/kod-recovery-v07

tree:
70d9ab5f452541c3fd697b40711be4242e0c6969

classification:
LAST_EXTERNALLY_VERIFIED_KOD_RECOVERY_BEFORE_SANDBOX_IMPLEMENTATION_R01

Do NOT rewrite/delete v07.

No kod-recovery-v08 was found in fresh KOO reconciliation.

## Exact KOD implementation result to preserve

puev5691/wellbeing-hq@c7979afefeb7dc7c33ab24d84039aa374112954e:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-r01__KOO.md

blob:
69a24ea931db365089393c75d13f1ac151593def

terminal:
PASS_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_READY_FOR_INDEPENDENT_REVIEW

candidate:
puev5691/wellbeing-hq@27134205e21ebc44308606de4cb59f7b3b3ed577:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-r01/

tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

candidate:
NOT_ACTIVATED

real_sandbox_effect:
NOT_EXECUTED

G4/G5/G6 authority:
NOT_CREATED

## Exact independent SHD review

puev5691/wellbeing-hq@ab128ba972282ea10ed3ebef51e64bab067036b4:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-adapter-platform-implementation-r01-review-r01__KOO.md

blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

terminal:
NEEDS_REWORK_SHD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_R01_REVIEW_R01

final_verdict:
NEEDS_REWORK_SANDBOX_IMPLEMENTATION_R01

Preserved PASS:
- CANDIDATE_INTEGRITY = PASS;
- OUTCOME_FAIL_CLOSED = PASS;
- NON_LIVE_BOUNDARY = PRESERVED;
- accepted D1/D2 architecture remains valid.

Exact bounded defects to preserve, NOT fix in this task:

D1-A:
canonical sandbox/root binding validation missing.
Need future correction to recompute/validate binding_id and nested root_identity_id and exact implementation constants before EffectIntent/admission/invocation.

D1-B:
CREATED_SANDBOX_OBJECT_IDENTITY omits mandatory no_symlink_reparse_evidence from required fields/output/digest.

D2-A:
cleanup eligibility lacks exact comparisons for:
- state.operation_key == created.operation_key;
- state.owner_attempt_id == created.attempt_id;
- created.root_identity_id == binding.root_identity_id;
- created.sandbox_target_id == binding.root_identity.sandbox_target_id.

P1:
Linux/POSIX profile validation does not validate root_identity_class, created_object_identity_class, cleanup_binding_class; root identity does not bind platform_evidence_profile_id to exact platform profile.

Tests/evidence hygiene:
negative tests missing for the above mismatch/forgery cases;
top-level TEST-SUMMARY.json is stale predecessor R04 metadata and must later be corrected or explicitly namespaced.

correction_implementation_authority:
NOT_CREATED

## Mandatory PROCESSING_STARTED

Before substantive self-snapshot:

1. fresh-check authority, registry, frontier;
2. verify current KOD writer;
3. verify no newer KOD writer;
4. verify recovery v07 exists and v08 does not;
5. verify exact KOD implementation result/candidate tree;
6. verify exact SHD review result/blob;
7. verify no KOD correction authority/task/result exists;
8. verify no G4/G5/G6 authority exists;
9. verify candidate remains NOT_ACTIVATED and real effect NOT_EXECUTED;
10. verify active Project Sources current.

Then create:

entities/koder/outbox/execution-evidence/KOD_V07_POST_SANDBOX_IMPL_REVIEW_PRE_CORRECTION_SELF_SNAPSHOT_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
KOD_V07_POST_SANDBOX_IMPL_REVIEW_PRE_CORRECTION_SELF_SNAPSHOT_R01_A1

authority_blob:
ba42233fb21d9d72189f0e483ec88fd69ae3bd92

frontier_commit:
01715f80f070ec05025d0f618e18ec8c1bbe6b37

frontier_blob:
1995e8d699cbacf8cc58daf83902dd73e6f88b15

accepted_state:
INITIAL_NOT_STARTED_V1

KOD_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

previous_recovery_ref:
34650c6b255ad204674b778de8d39910a61ba8f1

candidate_tree:
af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2

SHD_review_commit:
ab128ba972282ea10ed3ebef51e64bab067036b4

SHD_review_blob:
dcd3cd6432256c4ae26ccecd359b95b2964631ee

Immutable-readback PROCESSING_STARTED.

Only then create self-snapshot.

## Required KOD self-snapshot

Create exactly:

entities/koder/outbox/KOD__v07-post-sandbox-impl-review-pre-correction-self-snapshot__KOO-ARH.md

Preserve only verified current state:

- KOD current writer locator/blob/status;
- active approved Project Sources;
- recovery v07 locator/tree and stale-relative-to-later-work classification;
- KOD implementation R01 result/candidate tree;
- candidate NOT_ACTIVATED;
- real sandbox effect NOT_EXECUTED;
- exact SHD review NEEDS_REWORK result;
- exact five bounded correction areas above;
- candidate integrity PASS;
- outcome fail-closed PASS;
- non-live boundary preserved;
- correction implementation authority NOT_CREATED;
- G4/G5/G6 authority NOT_CREATED;
- sandbox target UNKNOWN / NOT_SELECTED;
- historical replay FORBIDDEN;
- hidden/unwritten KOD state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED;
- external KOD recovery v08 NOT_YET_CREATED;
- safe next step = ARH external KOD recovery v08 successor from this exact snapshot.

Do NOT:
- fix code;
- create correction candidate;
- change candidate R01;
- create G4/G5/G6 authority;
- execute sandbox effect;
- select sandbox target;
- mutate external recovery yourself;
- reconstruct hidden/predecessor state.

After publication:
- immutable-readback snapshot;
- return exact locator/commit/blob;
- include PROCESSING_STARTED locator/blob;
- state external ARH recovery v08 = PENDING;
- STOP.

## Mandatory return to KOO

Final response must contain one copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- preservation attempt;
- PROCESSING_STARTED locator/blob;
- self-snapshot locator/commit/blob;
- current KOD writer;
- recovery v07 classification;
- candidate tree/status;
- exact SHD NEEDS_REWORK result;
- bounded defect set;
- correction authority = NOT_CREATED;
- G4/G5/G6 authority = NOT_CREATED;
- external ARH recovery v08 = PENDING;
- exact UNKNOWNs/blockers.

Include exact line:

Fresh-reconcile this exact KOD post-review self-snapshot. Prepare ARH external KOD recovery v08 successor only. Do not infer correction implementation or G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
