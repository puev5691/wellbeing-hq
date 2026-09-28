# KOO record: authorize planned replacement SIS r0.7 Initiation Gate

status: OPERATOR_INITIATION_GATE_AUTHORITY_RECORDED
project_time: omitted

Exact predecessor freeze:
puev5691/wellbeing-hq@c36c04661bfd5b7ba3a348ea70dd83722cf36d84:
entities/sisadmin/current/SIS__planned-handoff-freeze-r07.md
blob 8b300a748e22408d64444138160192eb1306b38a
terminal PASS_SIS_R06_PLANNED_HANDOFF_FREEZE_R07_READY_FOR_REPLACEMENT_INITIATION_GATE

Exact ARH preserved recovery delta:
puev5691/wellbeing-hq@0061574c3aa4fcc3eeba341e63b9cc6c972dd9a3:
entities/archivarius/outbox/ARH__SIS-planned-replacement-r07-result__KOO-OPERATOR.md
blob df944eb4e2b7bf00935e7134c87e36811cd018c8

Recovery delta:
puev5691/wellbeing-entity-bootstrap@faa13798292dd93617ef8d4c0e5e47ebaf5ce809:
entities/sis/recovery/versions/sis-planned-r07

Recovery base:
puev5691/wellbeing-entity-bootstrap@6ffb05a0a2fb018717ddd6e996d4ec1c7a41ef7:
entities/sis/recovery/versions/sis-emergency-r06

Authorized:
- new SIS r0.7 may perform Initiation Gate only;
- verify baseline Project Sources, exact base recovery, exact planned delta, predecessor freeze, fresh HQ state and current/inbox/outbox/routes/receipts;
- return initiation status.

Preserve:
- predecessor r0.6 frozen;
- P552203 PRESERVATION_COPY_R01 = PAUSED / INCOMPLETE;
- destination package commit = ABSENT;
- unattached blobs non-authoritative;
- T01-T20 executed = 0;
- historical PROMPT replay forbidden;
- backend not selected;
- CHECKPOINT_DURABLE not established.

Not authorized:
- Writer Gate;
- current-writer establishment;
- P552203 resume;
- host/backend/storage mutation;
- T01-T20 execution;
- memory-layering attempt 3.
