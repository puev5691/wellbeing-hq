# KOO → OPERATOR/VOL: emergency failover authority for replacement VOL

status: EMERGENCY_FAILOVER_AUTHORIZED_FOR_INITIATION_ONLY
entity: VOL / ВОЛОНТЁР
project_time: omitted

## Human meaning

ОПЕРАТОР сообщил, что прежний VOL-чат полностью выработал ресурс и не способен самостоятельно выполнить предусмотренные recovery/checkpoint процедуры.

Это закрывает ранее сохранённую неопределённость VOL writer availability для цели аварийного failover.

Failure-state:
FAILURE_STATE_VOL_CURRENT_WRITER_UNAVAILABLE_OR_UNVERIFIABLE

Причина:
PREDECESSOR_VOL_CHAT_RESOURCE_EXHAUSTED_CANNOT_COMPLETE_SELF_RECOVERY_CHECKPOINT

Этот artifact разрешает только аварийную initiation нового physical VOL по последнему independently verified recovery с обязательной fresh reconciliation позднего HQ-delta.

Он НЕ назначает нового current-writer. Writer Gate остаётся отдельным последующим действием.

## Prior independent triage

ARH triage:
puev5691/wellbeing-hq@997fe4b020afe2a14c95313a9bf5c97862be00f5:
entities/archivarius/outbox/ARH__vol-continuity-recovery-triage-r01__KOO.md

blob:
ff8bff197112ce9e7f4d8a6086dc72b72a7afbde

terminal:
PASS_ARH_VOL_CONTINUITY_RECOVERY_TRIAGE_R01_WITH_BOUNDARIES

ARH established:
- VOL_CURRENT_WRITER = UNKNOWN_NOT_VERIFIED;
- VOL_WRITER_AVAILABILITY = UNKNOWN at that earlier boundary;
- latest independently verified recovery is preserved;
- that recovery is STALE_FOR_DIRECT_TASK_REPLAY;
- emergency replacement requires explicit failure-state and failover authority if writer becomes proven unavailable/unverifiable.

The present OPERATOR statement supplies that missing failover condition.

## Last independently verified recovery

Immutable recovery commit:
puev5691/wellbeing-entity-bootstrap@f6ff070313caff5d7b5d12779d4bb8d8eb0eec01:
entities/vol/recovery/current/

Manifest:
entities/vol/recovery/current/VOL_recovery-manifest_VOL.md
blob e2c1547b826fc0f5cae5f58e80838f2a068dcc8b

Initiation:
entities/vol/recovery/current/VOL_initiation-current_VOL.md
blob 2b1989ed1c6434cad437af4052686b7c956d07fe

Historical independent ARH verification:
puev5691/wellbeing-hq@25f5f38a8cca0a65be02979089b107e598827944:
entities/archivarius/outbox/ARH__VOL-emergency-recovery-verification__VOL.md
blob 1d8370e3fa052dd7b01a430458855ae38abd8eab
status PRESERVATION_CHECKPOINT_VERIFIED

Historical recovery byte verification:
6/6 PASS

## Staleness boundary

The recovery above is valid recovery evidence but NOT current operational state.

It predates later VOL work in HQ, including later COOP successors, architecture/activation work, hybrid-interaction research, P5 evidence and prospective measurement protocol.

Therefore:
- recovery may seed identity/role/recovery procedure;
- historical active-task statements must NOT be replayed;
- interrupted constitution stress-test is historical evidence only;
- all later HQ VOL results must be freshly reconciled before profile execution;
- UNKNOWN remains UNKNOWN;
- no current task priority may be inferred from recovery chronology.

## Exhausted-chat context candidate

Context-only preservation:
puev5691/wellbeing-hq@9465a7f5971a33a49326090b395645730d172111:
entities/koordinator/evidence/VOL__exhausted-chat-context-candidate__CONTEXT_ONLY.md

blob:
9dc84eedc0e4cc1256f4d1e72c28c300aa2b76e5

Original uploaded candidate SHA-256 observed by KOO:
887b99fbe884f0965e5418d7ea42fca4bd8ebb3ac8167d78fc1df3cf6a73ce6e

Disposition:
CONTEXT_ONLY / NOT_AUTHORITY / NOT_RECOVERY / NOT_VOL_SELF_SNAPSHOT

It may help identify conversation context and unresolved research ideas, but it must not establish identity, writer-state, task authority, publication status or recovery currentness.

## Current approved Project Sources for replacement initiation

New VOL must load current approved sources, not silently rely on old recovery's historical source-version list:

- project-instructions-core v2.5 — blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- entity-roles-short v2.4 — blob 1772339cb74dae8550bfbd2e33401c34a929e911
- entity-state-preservation-and-recovery-canon v1.6 — blob 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work-canon-universal v2.4 — blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading-policy v2.2 — blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor-canon v1.2 — blob df7896d867eeeffff506319538fedad938856686

If any current source identity/effectivity differs at actual initiation time, replacement VOL must stop and reconcile instead of guessing.

## Authorized replacement action

Authorized now:
1. create/open a new physical VOL chat;
2. perform cold-start initiation only;
3. verify current approved Project Sources;
4. verify exact immutable old recovery composition/checksums/readback;
5. verify this exact emergency-failover authority;
6. fresh-scan HQ for newer VOL writer/recovery/handoff/failover evidence;
7. reconcile all VOL results newer than recovery boundary;
8. classify old recovery tasks as historical evidence, not replay authority;
9. preserve context-only candidate only as context;
10. return initiation result.

Required initiation outcome:
- initiation_verified_waiting_writer_gate
or exact BLOCKED_* / FAIL_*.

## Not authorized

- establishing new VOL current-writer inside initiation;
- profile execution;
- replaying constitution stress-test;
- replaying any historical task/PROMPT;
- treating later VOL artifacts as accepted/current merely because they are newer;
- production/system actions;
- financial/token/ownership/governance activation;
- Project Sources/canon mutation;
- external service mutation;
- automation mutation;
- memory-layering attempt 3.

Writer Gate must be a separate later decision/action after successful initiation and fresh competing-writer reconciliation.

UNKNOWN remains UNKNOWN.
