# KOO -> ARH: KOD external recovery v09 preservation

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
ARH / АРХИВАРИУС current writer

attempt:
ARH_KOD_V09_EXTERNAL_RECOVERY_R01_A1

scope:
EXTERNAL_RECOVERY_PRESERVATION_AND_READBACK_ONLY

project_time:
omitted

Resume-First.

Perform ONLY external preservation of the exact current KOD v0.7 post-R02 self-snapshot into a NEW immutable KOD recovery successor v09, followed by integrity verification, immutable readback and recovery-registry accounting.

Do NOT perform SHD rereview.
Do NOT implement corrections.
Do NOT mutate R01 or R02 candidates.
Do NOT create or infer G4/G5/G6 authority.
Do NOT execute sandbox effects.
Do NOT select a sandbox target.
Do NOT change KOD writer-state.
Do NOT replay historical tasks/prompts.

## Exact authority

puev5691/wellbeing-hq@891dda087cb1d5356e2fe0eca460b36c31919a01:
entities/koordinator/outbox/ARH_KOD_v09_external_recovery_authority.md

blob:
b7cbf62e2ee61f94cc83293f8fa250983a3f9d4b

status:
OPERATOR_TASK_AUTHORITY_RECORDED

## Registry

puev5691/wellbeing-hq@b2ee8d00fa1470615a4426ba40ee2b429821b4a7:
entities/koordinator/outbox/ARH_KOD_v09_external_recovery_registry.md

blob:
73225d00e1e67e48ba5e0093b9467b0941a54134

state:
INITIAL_NOT_STARTED

## Accepted frontier

puev5691/wellbeing-hq@83e7c9549faeb6a8f38016055a6ef61f4e4b6487:
entities/koordinator/outbox/ARH_KOD_v09_external_recovery_frontier.md

blob:
c4715622b4cd050f114247f7e51de27fb40d309d

accepted_state:
INITIAL_NOT_STARTED_V1

start_proven:
NO

## Current ARH writer

entities/archivarius/current/ARH__replacement-current-writer-r03.md

blob:
3df64956a5ec4a21e11a4f469abaf91a1e4fd092

status:
WRITER_ESTABLISHED

If ARH writer changed/superseded or competing KOD v09 preservation exists:
STOP with exact blocker.

## Exact KOD self-snapshot

puev5691/wellbeing-hq@821253d38d2e041969b342cd6593cc69c7626fca:
entities/koder/outbox/KOD__v07-post-sandbox-impl-correction-r02-self-snapshot__KOO-ARH.md

blob:
660e50013d0d92f06901b7c46c3cc4c78f067941

terminal:
PASS_KOD_V07_POST_SANDBOX_IMPL_CORRECTION_R02_SELF_SNAPSHOT_R01_READY_FOR_ARH_EXTERNAL_RECOVERY_V09

immutable_readback:
PASS

This exact file is authoritative KOD self-state authored by the current KOD writer.
Preserve exact bytes/reference.
Do NOT rewrite or reconstruct substantive KOD self-state.

## Current KOD writer

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

## Previous external KOD recovery

puev5691/wellbeing-entity-bootstrap@63429caedcf4dd454a4de1f72aa50517fd8d2c42:
entities/kod/recovery/versions/kod-recovery-v08

tree:
5d88470c8b1cf9ea5a1bcc790baab1c52e649105

disposition:
STALE_RELATIVE_TO_LATER_SANDBOX_IMPLEMENTATION_CORRECTION_R02

Do NOT rewrite or delete v08.

## Target successor

Repository:
puev5691/wellbeing-entity-bootstrap

Create exactly one NEW immutable successor:

entities/kod/recovery/versions/kod-recovery-v09

Before publication verify target path does NOT already exist.

If v09 or competing v09 result/registry appears:
STOP with exact conflict.

## Active Project Sources

source-set:
R07

Activation blob:
0751a00489dd8f3f4ac5feeda900a22ade1b3f99

Required active identities:
- Project Core v2.5: a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- Entity Roles v2.4: 1772339cb74dae8550bfbd2e33401c34a929e911
- File Work Canon v2.4: e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- Source Loading Policy v2.2: 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- Recovery Canon v1.6: 233117e1c9509d730e1f5ec532b1cabe3f786609
- Task Conveyor Canon v1.2: df7896d867eeeffff506319538fedad938856686

Task Conveyor v1.3:
NOT_ACTIVE

## Exact R02 state to preserve

R02 result:

puev5691/wellbeing-hq@36e2d03c17063722c7c0a72ab6ef56f26b1a1d9b:
entities/koder/outbox/KOD__SECE-r01-sandbox-adapter-platform-implementation-correction-r02__KOO.md

blob:
bcf282a0e69a2e1272ca885be379798423a76e57

terminal:
PASS_KOD_SECE_R01_SANDBOX_ADAPTER_PLATFORM_IMPLEMENTATION_CORRECTION_R02_READY_FOR_INDEPENDENT_REREVIEW

R02 successor:

puev5691/wellbeing-hq@1752adb514e3bfa772ef22e25804f2b8ef7636b8:
entities/koder/outbox/sece-r01-sandbox-adapter-platform-implementation-correction-r02/

tree:
65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade

file_count:
58

Preserve exact verified state:
- D1-A PASS_STATIC_PURE_MOCK
- D1-B PASS_STATIC_PURE_MOCK
- D2-A PASS_STATIC_PURE_MOCK
- P1 PASS_STATIC_PURE_MOCK
- syntax_py_compile PASS
- pure_mock_tests 38/38 PASS
- predecessor relevant sandbox tests 22/22 PRESERVED_PASS
- new correction negative/static-order tests 16/16 PASS
- TEST-SUMMARY exact R02
- test evidence hygiene PASS
- R01 predecessor tree af63918a1c82c41d5ea1a04bbdced5dfb4b30aa2 immutable PASS
- R04 runtime blob e0626e3088b7f364604d1fb5e12c2b2b511c3987 unchanged PASS
- reviewed core blob e7b89c948c4e672c5b682408ce790670dfcdad5c unchanged PASS
- candidate NOT_ACTIVATED
- real sandbox effect NOT_EXECUTED
- sandbox target UNKNOWN / NOT_SELECTED
- real target behavior UNKNOWN
- R02 combined-runtime PASS NOT_INFERRED
- independent SHD R02 rereview NOT_PERFORMED / NOT_AUTHORIZED
- G4/G5/G6 authority NOT_CREATED
- hidden/unwritten KOD state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED

## Mandatory PROCESSING_STARTED

Before substantive preservation:

1. fresh-check authority/registry/frontier;
2. verify current ARH writer;
3. verify exact KOD self-snapshot;
4. verify current KOD writer;
5. verify v08 exists and v09 absent;
6. verify no competing ARH v09 attempt/result/registry;
7. verify source-set r07;
8. verify exact R02 result/tree;
9. verify R01 predecessor identity and R04/core identities;
10. verify SHD R02 rereview authority/result absent;
11. verify G4/G5/G6 authority absent.

Then create:

entities/archivarius/outbox/execution-evidence/ARH_KOD_V09_EXTERNAL_RECOVERY_R01_A1__PROCESSING_STARTED_E1.md

Bind at minimum:

attempt:
ARH_KOD_V09_EXTERNAL_RECOVERY_R01_A1

authority_blob:
b7cbf62e2ee61f94cc83293f8fa250983a3f9d4b

frontier_commit:
83e7c9549faeb6a8f38016055a6ef61f4e4b6487

frontier_blob:
c4715622b4cd050f114247f7e51de27fb40d309d

accepted_state:
INITIAL_NOT_STARTED_V1

source_snapshot_commit:
821253d38d2e041969b342cd6593cc69c7626fca

source_snapshot_blob:
660e50013d0d92f06901b7c46c3cc4c78f067941

source_writer_blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

previous_recovery_ref:
63429caedcf4dd454a4de1f72aa50517fd8d2c42

R02_result_blob:
bcf282a0e69a2e1272ca885be379798423a76e57

R02_candidate_tree:
65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade

target_path:
entities/kod/recovery/versions/kod-recovery-v09

Immutable-readback PROCESSING_STARTED.

Only then perform preservation.

## Required v09 recovery package

Build one standalone immutable package under:

entities/kod/recovery/versions/kod-recovery-v09

Required functions/files:

1. exact copy:
KOD__v07-post-sandbox-impl-correction-r02-self-snapshot__KOO-ARH.md

2. exact copy:
KOD__replacement-current-writer-v07.md

3. ROLE-IDENTITY.md

4. SOURCES.md

5. TASK-STATE.md

Preserve confirmed current state only:
- exact R02 result/tree/verdicts/tests;
- R01 immutable proof;
- R04 runtime/core unchanged proof;
- candidate NOT_ACTIVATED;
- real sandbox effect NOT_EXECUTED;
- sandbox target UNKNOWN / NOT_SELECTED;
- R02 combined runtime PASS NOT_INFERRED;
- SHD R02 rereview NOT_PERFORMED / NOT_AUTHORIZED;
- G4/G5/G6 authority NOT_CREATED;
- hidden/unwritten state UNKNOWN / MUST_NOT_BE_RECONSTRUCTED.

6. KOD__recovery-initiation-boundary-v09.md
ARH-owned procedural recovery metadata only.

7. RECOVERY-LINEAGE.md
Bind v08 predecessor, current KOD writer and exact self-snapshot.

8. RECOVERY-MANIFEST.md

9. SHA256SUMS.txt

Do not create unrelated reports.

## Integrity requirements

Before publication:
- final composition fixed;
- provenance verified;
- SHA-256 from final bytes;
- Git blob identities where applicable;
- no secrets/credentials/private keys.

SHA256SUMS covers every non-checksum file.

## External publication

Publish exactly to:

puev5691/wellbeing-entity-bootstrap:
entities/kod/recovery/versions/kod-recovery-v09

Record:
- publication commit/ref;
- exact version path;
- package tree;
- composition;
- external blobs;
- SHA-256 identities.

## Immutable readback

After publication independently read back v09 and verify:
- path -> tree;
- exact composition;
- source self-snapshot external equality;
- current-writer external equality;
- manifest/tree match;
- independently recomputed SHA256SUMS PASS;
- no missing/extra unexplained files;
- no current-state conflict.

Publication alone is NOT PASS.

## Recovery registry

Create:

entities/archivarius/current/recovery-registry/ARH__KOD-recovery-v09.md

Include:
- source self-snapshot locator/blob;
- KOD writer locator/blob/status;
- predecessor v08 immutable locator/tree/stale disposition;
- new v09 locator/ref/path/tree;
- composition/integrity/readback;
- R02 result/tree/verdicts/tests;
- R01 immutable proof;
- R04/core unchanged proof;
- candidate/effect/target state;
- R02 combined runtime PASS NOT_INFERRED;
- SHD R02 rereview authority/result NOT_CREATED;
- G4/G5/G6 authority NOT_CREATED;
- KOD writer mutation NONE;
- historical replay NONE.

Fresh-readback registry.

## Success classification

Return:

EXTERNALLY_PRESERVED_READBACK_PASS

only if all integrity/readback/currentness checks pass.

On PASS classify v09 as:

CURRENT_EXTERNAL_RECOVERY_BASIS_FOR_KOD_V07_POST_SANDBOX_IMPLEMENTATION_CORRECTION_R02

Do NOT infer SHD rereview, combined runtime PASS or G4/G5/G6 authority.

## Required standalone ARH result

Create:

entities/archivarius/outbox/ARH__KOD-v09-external-recovery__KOO-KOD.md

Expected PASS terminal:

PASS_ARH_KOD_V09_EXTERNAL_RECOVERY

Include exact attempt, authority/registry/frontier, PROCESSING_STARTED, source snapshot, current KOD writer, predecessor v08 disposition, v09 locator/ref/path/tree, package integrity/readback, recovery registry, R02 state, unknowns and boundaries.

## Hard boundaries

Do NOT:
- perform SHD rereview;
- implement additional correction;
- mutate R01/R02 candidates;
- infer or execute R02 combined runtime PASS;
- create G4/G5/G6 authority;
- execute sandbox effect;
- select target;
- mutate KOD writer-state;
- replay historical tasks/prompts;
- mutate Project Sources/canons;
- perform deployment/live/provider/API/Telegram effects;
- automatically continue downstream.

## Mandatory return to KOO

After durable result + immutable readback, return one final copy-paste block beginning:

АДРЕСАТ: КООРДИНАТОР / KOO

Resume-First.

Include:
- exact ARH attempt;
- result locator/commit/blob;
- terminal;
- PROCESSING_STARTED locator/blob;
- v09 recovery locator/ref/path/tree;
- composition/checksum/readback;
- registry locator/commit/blob;
- current KOD writer;
- v08 disposition;
- R02 result/tree/verdicts/tests;
- R01 immutable proof;
- R04/core unchanged proof;
- candidate/effect/target state;
- combined runtime status;
- SHD rereview authority/result status;
- G4/G5/G6 status;
- exact blockers/UNKNOWNs.

Include exact line:

Fresh-reconcile this exact ARH KOD v09 recovery result. Do not infer SHD rereview, R02 combined-runtime PASS, or G4/G5/G6 authority.

End:

STOP.

After that block add nothing.
