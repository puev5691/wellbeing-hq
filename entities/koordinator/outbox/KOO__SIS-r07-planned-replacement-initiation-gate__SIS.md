# KOO → new SIS r0.7: planned replacement Initiation Gate

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: new SIS r0.7
scope: INITIATION_GATE_ONLY
project_time: omitted

Resume-First.

Perform ONLY Initiation Gate.

Exact authority:
puev5691/wellbeing-hq@04a4abf2a32bbca7cea1f114ae141ab2b1b137dc:
entities/koordinator/outbox/KOO__authorize-SIS-r07-planned-replacement-initiation-gate__OPERATOR.md

Exact predecessor freeze:
puev5691/wellbeing-hq@c36c04661bfd5b7ba3a348ea70dd83722cf36d84:
entities/sisadmin/current/SIS__planned-handoff-freeze-r07.md
blob:
8b300a748e22408d64444138160192eb1306b38a

Exact ARH result:
puev5691/wellbeing-hq@0061574c3aa4fcc3eeba341e63b9cc6c972dd9a3:
entities/archivarius/outbox/ARH__SIS-planned-replacement-r07-result__KOO-OPERATOR.md
blob:
df944eb4e2b7bf00935e7134c87e36811cd018c8

Exact recovery delta:
puev5691/wellbeing-entity-bootstrap@faa13798292dd93617ef8d4c0e5e47ebaf5ce809:
entities/sis/recovery/versions/sis-planned-r07

Exact recovery base:
puev5691/wellbeing-entity-bootstrap@6ffb05a0a2fb018717ddd6e996d4ec1c7a41ef7:
entities/sis/recovery/versions/sis-emergency-r06

Load and verify current approved baseline Project Sources:
- project-instructions-core v2.5
- entity-roles-short v2.4
- entity-state-preservation-and-recovery-canon v1.6
- file-work-canon-universal v2.4
- source-loading-policy v2.2
- task-conveyor-canon v1.2 if inter-chat/PROMPT conveyor is used

Then:
1. verify exact base recovery;
2. verify exact planned r0.7 delta composition/integrity;
3. verify predecessor r0.6 freeze exact identity and terminal;
4. fresh-preflight wellbeing-hq;
5. fresh-reconcile SIS current/inbox/outbox/routes/receipts;
6. verify there is no competing successor/current writer r0.7;
7. preserve exactly:

P552203 PRESERVATION_COPY_R01 = PAUSED / INCOMPLETE
destination package commit = ABSENT
T01-T20 executed = 0
unattached blobs = NON_AUTHORITATIVE / NOT_TASK_PROGRESS / NOT_RECOVERY_STATE
historical PROMPT replay = FORBIDDEN
backend selected = NO
CHECKPOINT_DURABLE = NOT_ESTABLISHED

Do NOT resume any profile task from recovery history.

Return one:
- initiation_verified_waiting_writer_gate
- initiation_loaded_external_unverified
- initiation_failed

Do NOT:
- perform Writer Gate;
- establish current-writer;
- resume P552203;
- reuse unattached blobs;
- execute T01-T20;
- mutate host/backend/storage;
- run memory-layering attempt 3.

After immutable initiation result + exact readback + return KOO, STOP.
