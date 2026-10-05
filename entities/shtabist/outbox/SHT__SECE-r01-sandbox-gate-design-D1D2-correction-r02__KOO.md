# SHT -> KOO: SECE sandbox gate design D1D2 correction R02 result

status: DESIGN_ONLY
implementation: NOT_IMPLEMENTED
activation: NOT_ACTIVE
terminal: PASS_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_READY_FOR_NARROW_REREVIEW
attempt: SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1
project_time: omitted

## Human result
Only SHD defects D1 and D2 were corrected. Historical R01 remains immutable.

D1 now defines a versioned implementation-neutral object-identity confinement contract: strict one-basename grammar, anchored root object identity, relative exclusive/no-follow-equivalent creation, actual created-object identity, same-object continuity, platform-specific hardlink/replacement evidence, and fail-closed behavior when those properties cannot be proved.

D2 binds destructive cleanup to the same root/created-object identities. Path text alone can never authorize delete. Identity drift/ambiguity means NO DELETE; ambiguous cleanup means UNKNOWN with no destructive retry.

## Exact authority/currentness
Authority:
puev5691/wellbeing-hq@48dbe1b9d942c764cd10105264d26a795c0bd13f:
entities/koordinator/outbox/SHT_SECE_sandbox_gate_design_D1D2_correction_R02_authority.md
blob 87ce1458c58493d87fd4568c698562feb67c0313.

Decision gate:
puev5691/wellbeing-hq@cd3db7c6eeb17fa9dca87d2dcfa2367462be1937:
entities/koordinator/outbox/KOO__SECE-sandbox-gate-design-D1D2-correction-R02-decision__OPERATOR.md
blob 6ca4e8df10389fcb8aa003b767d3f8bca73b16ec.

Registry:
puev5691/wellbeing-hq@d384ad49043822da277526c27ab00202f2353065:
entities/koordinator/outbox/SHT_SECE_sandbox_gate_design_D1D2_correction_R02_registry.md
blob 1302d7e1ff82a1756f115551a158410d0933914f.

Accepted frontier:
puev5691/wellbeing-hq@24729f0c89d6608a15ef9b8e2a47b8af952ba7ff:
entities/koordinator/outbox/SHT_SECE_sandbox_gate_design_D1D2_correction_R02_frontier.md
blob 3d7f6717e3ed162464192ecf6f2880591f405d8b
accepted INITIAL_NOT_STARTED_V1.

SHT writer blob a019c21cffeb99bb7c387b8fa95a4629137dc6da CURRENT_WRITER.
Fresh pre-start HEAD 24729f0c89d6608a15ef9b8e2a47b8af952ba7ff.
No competing attempt/supersession found in fresh exact attempt search.

PROCESSING_STARTED:
puev5691/wellbeing-hq@a73a69f104c79444a5ea21bc44e7b96bf995b309:
entities/shtabist/outbox/execution-evidence/SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1__PROCESSING_STARTED_E1.md
blob 8ba91ff5088755524f077c59a2310bc6b729304c.
Readback MATCH.

## Predecessor/review
Predecessor R01 result:
puev5691/wellbeing-hq@5b3b499901e62b22bcb58a1ffb9bcda831940cf3:
entities/shtabist/outbox/SHT__SECE-r01-sandbox-gate-design-r01__KOO.md
blob 3ff6d05645098c128ef374ec20869471658fa8c2.

Historical predecessor package tree:
e5f875af2322f460a2d02af4d47c56e8d2ae2ce9.
NOT MUTATED.

SHD review:
puev5691/wellbeing-hq@2625783e24ded82db905f3abe52f982952f4515c:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-gate-design-r01-review-r01__KOO.md
blob 4ed270080598fbca66c74551a40a37d0b984ef51
terminal NEEDS_REWORK_SHD_SECE_R01_SANDBOX_GATE_DESIGN_R01_REVIEW_R01.

## Corrected successor
Package:
entities/shtabist/outbox/sece-r01-sandbox-gate-design-d1d2-correction-r02/
tree:
84979101d6bd19fd939f978652f03317f6e524b9

Successor semantics:
R01 complete design + this immutable D1/D2 correction overlay.
Unchanged R01 areas are carried by exact blob reference; changed areas are represented by successor files.

Changed files/blobs:
CONFINEMENT-PROFILE.md 3e8e12a95f44db6c18a895d0ed83b69dc4b4ea6e
CLEANUP-IDENTITY.md 3dab9da97c5cfb4a055f5d5967791105a657c231
PRE-EFFECT-ADMISSION.md c0926c3767e377e8e6c5cdbd5af0d063f51f629c
SANDBOX-EFFECT-ADAPTER.md 3f9891aa200224d3365d01cfdb3752243e9cf40c
SANDBOX-EFFECT-CLASS.md f42f7f76bab51890bd4290b6217246776b90e223
OUTCOME-EVIDENCE.md 6e5ad629e775d0ad17082ad88e8a376298eaea3e
ROLLBACK-CLEANUP.md d3f116f08ba51322c5eac933cb6a5a413858e608
G4-AUTHORITY-SHAPE.md aa3b2bac844173430d07aeb70999158c97e87753
MANIFEST.md 330a9c1c968a9fa2f1aa78bc0f2b63b6f598b04f

Readback 9/9 MATCH.

Unchanged carried-forward R01 blobs:
SANDBOX-GATE.md 3f9f932410c37e56528cacfb81c6bfc0e1457fc2
AUTHORITY-MODEL.md 5efa3127e538140f2d041b181115675c5a61cb88
UNRESOLVED-EFFECT.md f77bf23ef0fbbaa962c814004626212954fd3fe2
G5-REVIEW.md 776301e1e33055f99a4854621edb40636869c373
G6-TRANSITION.md 7bbf8e1f0a0bbcb7d3bffd4eda0cfb808596a3e0

## D1/D2 closure matrix
D1_RACE_SAFE_PATH_CONFINEMENT: CLOSED
D1_ANCHORED_ROOT_IDENTITY: DEFINED
D1_CREATED_OBJECT_IDENTITY: DEFINED
D1_SAME_OBJECT_CONTINUITY: DEFINED
D1_HARDLINK_REPLACEMENT_BOUNDARY: DEFINED
D1_CONFINEMENT_PROFILE_VERSIONED: YES

D2_FILE_CLEANUP_IDENTITY_BOUND: YES
D2_DIRECTORY_CLEANUP_IDENTITY_BOUND: YES
D2_POST_CLEANUP_IDENTITY_READBACK: YES
D2_AMBIGUOUS_CLEANUP_NO_RETRY: YES

G5_BOUNDARY: PRESERVED
G6_BOUNDARY: PRESERVED
AUTHORITY_SEPARATION: PRESERVED
UNRESOLVED_REPLAY_SAFETY: PRESERVED
DESIGN_STATUS: DESIGN_ONLY / NOT_IMPLEMENTED / NOT_ACTIVE

## D1 key semantics
Leaf is one exact basename only. Empty/absolute/dot/dotdot/separators/alternate namespace escapes/NUL/normalization-changing names are rejected. Future platform profile must enumerate further reserved forms.

Security root is SANDBOX_ROOT_OBJECT_IDENTITY from an already opened/verified directory object or equivalent. Root path is explanatory only after admission.

Create is relative to anchored root, exclusive, no-follow-equivalent, no overwrite, no mutable-parent traversal, no unanchored fallback.

CREATED_SANDBOX_OBJECT_IDENTITY comes from the actual created/open object and is carried through write/stat/readback/hash/outcome/cleanup.

Same-object proof is mandatory. If proof is unavailable before mutation => BLOCKED/NOT_EXECUTED. If lost after possible mutation => UNRESOLVED.

Hardlink/replacement requirement is expressed as a security property with platform evidence profile, not fake universal inode semantics.

## D2 key semantics
Cleanup requires terminal/effect evidence durable, resolved outcome, current anchored root identity, exact created-object identity, ownership and bound cleanup scope.

Immediately before delete, root/parent/object/regular-file/no-reparse/ownership/operation-key identity is revalidated.

Deletion is object-bound/relative to anchored parent. No absolute re-resolution, wildcard, recursive fallback or path-only weaker substitute.

Directory cleanup requires exact directory/parent identity and emptiness/no-foreign-entry proof.

Post-cleanup proves absence through same anchored boundary and unchanged root/parent identity.

Ambiguous cleanup => UNKNOWN, evidence preserved, no destructive retry.

## Remaining UNKNOWNs
Actual sandbox target remains UNKNOWN_LATER_GATE.
Future platform evidence profile implementation is NOT_IMPLEMENTED and must prove R02 semantics.
Future G4 task/attempt NOT_CREATED.
Adapter implementation NOT_IMPLEMENTED.
Adapter/effect authority NOT_CREATED.
Target mutation authority NOT_CREATED.
Evidence carrier/current-version mechanism TO_BE_BOUND.
Writer requirement TO_BE_BOUND_BY_GOVERNING_TASK/RULE.
G5 authority NOT_CREATED.

These remain execution blockers, not D1/D2 design defects.

## Boundaries
No KOD implementation.
No filesystem race experiment.
No sandbox target selected/mutated.
No G4 authority/execution.
No G5 review.
No G6 authority.
No activation/deployment/live effect.
No credentials.
No host/service/storage mutation.
No Project Source/canon mutation.
No role/Recovery/current-writer mutation.
No automatic downstream continuation.

## EXPERIENCE
Idea -> replace pathname safety prose with a persistent object-identity chain.
Probe -> follow the resource from anchored root through create/readback/outcome and then ask whether cleanup can still prove it is deleting that same object.
Result -> D1 and D2 now share one confinement/identity model instead of independent path checks.
Success -> substitution races fail closed without requiring one universal OS syscall.
Lesson -> a filename is a request to resolve an object, not the object's identity; destructive cleanup must prove identity again at the moment it acts.

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
