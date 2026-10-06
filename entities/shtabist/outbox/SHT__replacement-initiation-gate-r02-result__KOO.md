# SHT -> KOO: replacement Initiation Gate r0.2 result

primary_outcome:
initiation_failed

failure_class:
START_BOUNDARY_PROCESSING_EVIDENCE_INSTANCE_BINDING_CONFLICT

entity:
SHT / ШТАБИСТ

exact_new_SHT_chat_instance:
this current new SHT chat

attempt:
SHT_REPLACEMENT_INITIATION_GATE_R02_A1

project_time:
omitted

## Human result

This new SHT chat completed the mandatory pre-start reconciliation but did not cross into substantive Initiation Gate verification.

The exact authority, registry and accepted frontier matched the instructed immutable identities. The predecessor remains CURRENT_WRITER and no Writer Gate or profile work was performed.

At the required PROCESSING_STARTED write boundary, this instance attempted to create the exact evidence path, but GitHub rejected the create because that path already existed. Fresh readback showed that the existing file was created in commit 5c73b03649363d982de29ea887a5f5216e03e344 and its exact bytes differ from the bytes submitted by this instance. Therefore the existing evidence cannot be safely attributed to this exact current chat instance.

Because Initiation is instance-specific and the exact attempt lineage permits no guessed ownership or duplicate execution, substantive recovery verification was stopped. This result does not claim recovery corruption; it records an unresolved execution/start provenance conflict.

## Exact pre-start authority

authority:
puev5691/wellbeing-hq@02988890e944936317185380faf79f288b2ca9de:
entities/koordinator/outbox/KOO__authorize-SHT-replacement-initiation-gate-r02__OPERATOR.md

authority_blob:
a86a2da93f4a83a7fbc626f6dd6d9f3134f9ca13

authority_verdict:
PASS_EXACT

registry:
puev5691/wellbeing-hq@98cbb9646056907c29283b10f4ad81a25914bc81:
entities/koordinator/outbox/SHT_replacement_initiation_gate_R02_registry.md

registry_blob:
40b19129edd575869ed1b94cd0eb7a5b5e244934

registry_state:
INITIAL_NOT_STARTED

registry_verdict:
PASS_EXACT

accepted_frontier:
puev5691/wellbeing-hq@82e63db72a828df8afe81210ea06f63dd2951fd1:
entities/koordinator/outbox/SHT_replacement_initiation_gate_R02_frontier.md

frontier_blob:
8f0cd4dbba32a8a9c9fdc8ada88c617d8b61b5aa

accepted_state:
INITIAL_NOT_STARTED_V1

frontier_start_proven:
NO

frontier_verdict:
PASS_EXACT

## PROCESSING_STARTED evidence conflict

existing_processing_started:
puev5691/wellbeing-hq@5c73b03649363d982de29ea887a5f5216e03e344:
entities/shtabist/outbox/execution-evidence/SHT_REPLACEMENT_INITIATION_GATE_R02_A1__PROCESSING_STARTED_E1.md

existing_processing_started_blob:
d2cf63b0650a4185d9088fd0f09028d44bbcc78f

existing_processing_started_status:
PROCESSING_STARTED / YES

existing_evidence_frontier_binding:
PASS_EXACT_82e63db72a828df8afe81210ea06f63dd2951fd1__8f0cd4dbba32a8a9c9fdc8ada88c617d8b61b5aa

immutable_readback:
PASS

current_instance_creation_attempt:
FAILED_PATH_ALREADY_EXISTS

current_instance_submitted_bytes_equal_existing_bytes:
NO

processing_started_instance_binding:
UNKNOWN_CONFLICT

## Recovery target

exact_recovery_locator:
puev5691/wellbeing-entity-bootstrap@c23b2304ca0ea4f4b62e9e451e39c69cfb1817c5:
entities/sht/recovery/versions/sht-recovery-r02

expected_package_tree:
f561246223a48ac885d7baae383898cc8e89af16

composition_verdict:
NOT_PERFORMED_DUE_START_BOUNDARY_CONFLICT

git_blob_verification_verdict:
NOT_PERFORMED_DUE_START_BOUNDARY_CONFLICT

sha256_verification_verdict:
NOT_PERFORMED_DUE_START_BOUNDARY_CONFLICT

recovery_manifest_verdict:
NOT_PERFORMED_DUE_START_BOUNDARY_CONFLICT

sha256sums_verdict:
NOT_PERFORMED_DUE_START_BOUNDARY_CONFLICT

recovery_corruption_claim:
NONE

## Active Project Sources

source_set_basis:
entities/koordinator/outbox/KOO__source-set-r07-activation-result__OPERATOR.md

source_set_basis_blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

source_set_basis_status:
PASS_KOO_SOURCE_SET_R07_ACTIVATED

source_set_superseding_activation_found_in_prestart_search:
NO

active_source_verification_verdict:
PRESTART_BASIS_PASS__INDIVIDUAL_SOURCE_IDENTITY_RECHECK_NOT_PERFORMED_DUE_START_BOUNDARY_CONFLICT

## Predecessor writer

predecessor_writer:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md

predecessor_writer_blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

writer_generation:
SHT-CURRENT-INSTANCE-R01

predecessor_writer_status:
CURRENT_WRITER

predecessor_writer_mutation:
NONE

## Preserved state

profile_continuation:
PAUSED_BY_OPERATOR

D1D2_attempt:
SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1

D1D2_state:
COMPLETED_PASS

D1D2_terminal:
PASS_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_READY_FOR_NARROW_REREVIEW

narrow_rereview:
NOT_STARTED / NOT_AUTHORIZED

historical_replay:
NONE

hidden_or_unwritten_predecessor_state:
UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Boundaries

Writer_Gate:
NOT_PERFORMED

current_writer_created:
NO

profile_work:
NOT_PERFORMED

SECE_continuation:
NOT_PERFORMED

narrow_rereview_execution:
NOT_PERFORMED

Project_Source_canon_mutation:
NONE

production_live_effect:
NONE

provider_API_Telegram_effect:
NONE

automatic_downstream_continuation:
NONE

## Exact blocker

blocker:
The positive PROCESSING_STARTED artifact for the same exact attempt appeared at the required write boundary with bytes different from those submitted by this exact current chat. Its instance ownership cannot be proven from available evidence. Continuing would risk duplicate/competing execution of one exact Initiation Gate attempt.

minimum_verifiable_next_step:
KOO must fresh-reconcile commit 5c73b03649363d982de29ea887a5f5216e03e344 and determine whether that PROCESSING_STARTED evidence belongs to this exact activation lineage or to a competing SHT instance. Do not authorize Writer Gate or profile continuation from this result.

terminal:
FAIL_SHT_REPLACEMENT_INITIATION_GATE_R02_START_EVIDENCE_INSTANCE_BINDING_CONFLICT
