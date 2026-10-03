# SIS r0.9 planned replacement Initiation Gate

status:
TASK_PREPARED_FOR_MANUAL_ACTIVATION

recipient:
genuinely NEW SIS r0.9

scope:
INITIATION_GATE_ONLY

project_time:
omitted

АДРЕСАТ: НОВЫЙ СИСАДМИН / SIS r0.9

Initiation-required.

Ты новый экземпляр SIS. Resume-First по continuity прежнего чата НЕ применяется: predecessor SIS r0.8 завершил planned handoff/freeze.

Выполни только Initiation Gate.

## Exact authority

puev5691/wellbeing-hq:
entities/koordinator/outbox/KOO__authorize-SIS-r09-planned-replacement-initiation-gate__OPERATOR.md

Exact OPERATOR decision:

AUTHORIZE_SIS_R09_PLANNED_REPLACEMENT_INITIATION_GATE = YES

Authority scope:
INITIATION_GATE_ONLY.

## Exact predecessor freeze

puev5691/wellbeing-hq@501cd387bf6c254086cb92713e7f6b2253e18707:
entities/sisadmin/current/SIS__planned-handoff-freeze-r08-r01.md

blob:
8b1e42486a27deec3f4572d23b0e6d5455e1a45d

status:
CURRENT_WRITER_HANDOFF_FREEZE

terminal:
PASS_SIS_R08_PLANNED_HANDOFF_FREEZE_READY_FOR_SUCCESSOR_INITIATION_GATE

Predecessor disposition:
FROZEN_FOR_NEW_NORMAL_AUTHORITATIVE_PROFILE_CURRENT_STATE_WORK

Do not treat the old r0.8 writer artifact as current authority after this freeze.

## Exact recovery r0.8

puev5691/wellbeing-entity-bootstrap@a075147ee4f9e060141ea75a18f68d7cabec4098:
entities/sis/recovery/versions/sis-planned-r08

package tree:
3730a6afd337439d3c9487c12344300df9b05a79

Expected exact composition:
5 files

1. SIS__planned-replacement-self-snapshot-r08-r01__ARH.md
blob 56807b80a80cfc9de8e5e3305b21e47fb52a4d2d

2. SIS__planned-replacement-initiation-draft-r01__ARH.md
blob cdbd973343df72fcf3e8e550c900765570fb643a

3. SIS__planned-replacement-preservation-handoff-r01__ARH.md
blob f29e78401e549f2371dacd9047701476e7fa5b1b

4. RECOVERY-MANIFEST.md
blob 8fcb6046c1ec373e33d4bbf36f7a3d5abef4dbda

5. sha256sums.txt
blob a00a06fd04e7443da653d9a94def71a505aecead

ARH preservation/readback:

puev5691/wellbeing-hq@f8dd097cc3cd7bcf889e8f30d0ddf46e95a76841:
entities/archivarius/outbox/ARH__SIS-planned-replacement-r08-result__KOO-OPERATOR.md

blob:
059fb8ec52f1a7db0664b6ceed848d2cc0bf7709

terminal:
PASS_ARH_SIS_PLANNED_REPLACEMENT_R08_EXTERNALLY_PRESERVED

Verify external locator, package tree, 5/5 composition and immutable identities yourself.

## Active Project Sources

Load and verify exact active versions:

- Project Core v2.5
  blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- Entity Roles v2.4
  blob 1772339cb74dae8550bfbd2e33401c34a929e911
- Source Loading Policy v2.2
  blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- Recovery Canon v1.6
  blob 233117e1c9509d730e1f5ec532b1cabe3f786609
- File Work Canon v2.4
  blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- Task Conveyor Canon v1.2
  blob df7896d867eeeffff506319538fedad938856686

Fresh-check currentness. Do not infer pending candidates as active.

## R03 boundary

Current KOO state at task materialization:

entities/koordinator/current/execution-evidence/SIS_SECE_D1D2_PUBLICFETCH_R03_A1.md

Expected accepted version:
R09_INITIATION_AUTHORIZED_AWAITING_TRANSFER_V7

Preserve during initiation:

- R03 = NONTERMINAL / DO_NOT_REPLAY;
- processing_started = YES;
- anonymous exact commit acquisition = SUCCEEDED;
- fetched commit = b32c3bdefa01c036e78a9e4d60fc2a78fd86418c;
- resolved package tree = 7807b3f5d43fe62b344f8ab6f6947aea98e33af7;
- CHECKPOINT_DURABLE = NOT_CREATED;
- package materialization = NOT_PERFORMED_AT_SNAPSHOT_BOUNDARY;
- Python workload = NOT_EXECUTED;
- R03 terminal = NOT_CREATED;
- R03 cleanup = NOT_PERFORMED.

Do not execute or resume R03 during initiation.

## Initiation procedure

1. Fresh-preflight wellbeing-hq.
2. Verify KOO r1.2 current writer.
3. Verify exact predecessor freeze r0.8 and that no later SIS writer/freeze/successor supersedes it.
4. Verify exact external recovery r0.8 composition/integrity and ARH preservation result.
5. Verify the six active Project Sources above.
6. Fresh-reconcile relevant SIS current/outbox/inbox/routes/receipts and terminal results after the recovery/freeze boundary.
7. Verify no competing SIS r0.9 initiation/current-writer exists.
8. Build initiation state only from verified recovery + fresh durable evidence. Do not reconstruct missing chat state.
9. Keep R03 and historical tasks as evidence only unless a newer exact terminal/current authority changes their classification.
10. Do not perform profile work.

## Hard boundaries

This Initiation Gate does not authorize:
- Writer Gate or current-writer establishment;
- R03 replay/resume/cleanup;
- host/network/storage mutation;
- Telegram/OpenAI/provider calls;
- profile/production work;
- historical PROMPT/task replay;
- Project Source/canon mutation.

## STOP conditions

STOP with exact BLOCKED/FAIL if:
- predecessor freeze identity/status mismatches;
- recovery locator/tree/composition/integrity mismatches;
- active Source identity conflicts;
- a competing SIS r0.9 initiation/current-writer exists;
- fresh evidence supersedes this task;
- required verification is unavailable;
- continuation would require anything outside INITIATION_GATE_ONLY.

## Required result

Create one immutable initiation result:

entities/sisadmin/outbox/SIS__planned-replacement-initiation-r09-result__KOO.md

Success status:
INITIATION_VERIFIED_WAITING_WRITER_GATE

Success terminal:
initiation_verified_waiting_writer_gate

The result must record:
- exact authority locator/blob;
- exact predecessor freeze locator/blob/terminal;
- external recovery r0.8 locator/commit/tree and 5/5 verification;
- active Source verification;
- fresh HQ/currentness/competing-successor reconciliation;
- R03 NONTERMINAL / DO_NOT_REPLAY boundary;
- historical replay = FORBIDDEN;
- profile_work = NOT_STARTED;
- current_writer_for_r09 = NOT_ESTABLISHED;
- Writer Gate = NOT_PERFORMED;
- next gate = SEPARATE_OPERATOR_WRITER_GATE_DECISION_REQUIRED.

After immutable publication/readback:
RETURN exact result locator + commit + blob to KOO + OPERATOR.
Then STOP.
