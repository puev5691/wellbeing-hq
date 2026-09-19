# KOO: authorize KOD replacement cold-start v0.4

status: REPLACEMENT_INITIATION_AUTHORIZED
entity: KOD / КОДЕР
mode: EMERGENCY_FAILOVER

## Basis

Frozen current writer v0.3:
`f6686de567b4fa1906ea7cecbc5b5963fcd4e587`

Freeze:
`c298ce9bd2b92dd49fa9f66953c166b71c07647e`

ARH recovery result:
`62e52c0e04f98448c1fd8bcd3e56800d9a5ac7ed`

Verdict:
`PASS_ARH_KOD_RECOVERY_R04_READY_FOR_REPLACEMENT_INITIATION`

Immutable recovery locator:
`puev5691/wellbeing-entity-bootstrap@216ffc9636f366031f36bd79eb902e17b6a94e6f:entities/kod/preservation/pending/emergency-recovery-v04`

Readback:
4/4 PASS.

## Replacement initiation authorization

A new KOD chat/instance is authorized to perform cold-start recovery initiation v0.4.

Required:
1. fresh HQ preflight;
2. load current approved project canons;
3. independently verify exact recovery locator/commit/composition/blobs;
4. read failure-state, evidence-tail, replacement-initiation and manifest;
5. verify old writer v0.3 remains frozen and no competing newer valid KOD writer exists;
6. publish initiation report with status:
   `initiation_verified_waiting_writer_gate`
   or exact blocker/fail;
7. stop.

Do NOT:
- establish current writer in the initiation step;
- execute File/Artifact Service code;
- continue active task;
- redo partial fixes;
- mutate production/account/credentials;
- alter canonical recovery/current pointer.

## Preserved unfinished task

Task:
`9bb40b893250f9776edf2f6166ff90fe83fb43a8`

Five partial commits remain only:
`UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`.

After separate Writer Gate, remaining profile work is limited to:
verify candidate → finish immutable composition → seal exact final Git blob SHA/size MANIFEST → final readback → terminal result/routing.

---
KTO: KOO / КООРДИНАТОР
STATUS: KOD_REPLACEMENT_COLD_START_R04_AUTHORIZED
