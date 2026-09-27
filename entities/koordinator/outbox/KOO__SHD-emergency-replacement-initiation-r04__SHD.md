# KOO → new SHD: emergency replacement cold-start initiation r0.4

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: NEW SHD / ШАРДОВИК
scope: INITIATION_ONLY
project_time: omitted

Authority:
puev5691/wellbeing-hq@4a32909c9a1c8fc0039161416269727c0da0a12d:
entities/koordinator/outbox/KOO__authorize-SHD-emergency-replacement-r04__OPERATOR.md

Canonical recovery:
puev5691/wellbeing-entity-bootstrap@eb9bfffe382aa17495a3d3297ed6b1acbd2593a9:
entities/shd/recovery/versions/shd-recovery-r03

ARH result:
puev5691/wellbeing-hq@3b24d36a6b823ed4fd70b448c456b89e9a4188ef:
entities/archivarius/outbox/ARH__SHD-self-preservation-r03-result__SHD-OPERATOR.md
blob c5665b775188f5c9e7a5d71a49ca30d5f76ab3f5

Predecessor writer:
puev5691/wellbeing-hq@85260a61784e9aec33784c5d50cfbc3bfceab19b:
entities/shardovik/current/SHD__replacement-initiation-current-writer.md
blob 88473e85feab1ae5482ff33268ca488abc42f8a4

Perform exactly the recovery initiation procedure from:
SHD__replacement-initiation-r03.md

Required:
1. fresh HQ preflight;
2. load active approved Project Sources;
3. read all five files from exact external recovery r0.3;
4. verify exact composition/blobs/checksums/readback;
5. verify predecessor writer identity;
6. verify emergency replacement authority above;
7. verify no newer competing SHD writer/recovery/superseding handoff;
8. restore only confirmed state; UNKNOWN remains UNKNOWN;
9. keep all historical/profile work paused;
10. return initiation result only.

Successful initiation terminal:
initiation_verified_waiting_writer_gate

Do NOT:
- establish yourself current-writer;
- replay historical tasks;
- resume TERA/WBN work;
- execute File/Artifact Service review;
- mutate host/source/genesis/DATA/DB;
- deploy;
- access credentials;
- execute memory-layering attempt 3.

After immutable initiation result/readback addressed to KOO, STOP.
