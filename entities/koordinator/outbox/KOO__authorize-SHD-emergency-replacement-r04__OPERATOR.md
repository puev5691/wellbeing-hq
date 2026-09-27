# KOO record: OPERATOR authorizes emergency replacement SHD r0.4

status: OPERATOR_EMERGENCY_REPLACEMENT_AUTHORITY_RECORDED
project_time: omitted

OPERATOR statement:
current SHD chat is no longer usable; initiate a new SHD.

Effect:
- previous authoritative SHD writer is frozen for new authoritative profile/current-state work by emergency replacement authority;
- inability of the old chat to publish self-freeze does not block replacement;
- predecessor remains immutable provenance/evidence only;
- this authority permits cold-start initiation of one replacement SHD instance from exact preserved recovery r0.3;
- this authority does NOT itself establish the replacement as current-writer.

Predecessor writer:
puev5691/wellbeing-hq@85260a61784e9aec33784c5d50cfbc3bfceab19b:
entities/shardovik/current/SHD__replacement-initiation-current-writer.md
blob 88473e85feab1ae5482ff33268ca488abc42f8a4

Canonical recovery:
puev5691/wellbeing-entity-bootstrap@eb9bfffe382aa17495a3d3297ed6b1acbd2593a9:
entities/shd/recovery/versions/shd-recovery-r03

ARH preservation result:
puev5691/wellbeing-hq@3b24d36a6b823ed4fd70b448c456b89e9a4188ef:
entities/archivarius/outbox/ARH__SHD-self-preservation-r03-result__SHD-OPERATOR.md
blob c5665b775188f5c9e7a5d71a49ca30d5f76ab3f5
terminal PASS_ARH_SHD_SELF_PRESERVATION_R03_EXTERNALLY_PRESERVED

Preserved boundaries:
- no historical task replay;
- no TERA/WBN mutation;
- no host/deployment/credential mutation;
- no memory-layering attempt 3;
- no current-writer transfer before separate Writer Gate.
