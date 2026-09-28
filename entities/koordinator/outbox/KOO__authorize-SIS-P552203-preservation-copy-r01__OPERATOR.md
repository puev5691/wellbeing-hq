# KOO record: authorize SIS P552203 PRESERVATION_COPY_R01

status: OPERATOR_BOUNDED_PRESERVATION_COPY_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR selected:
SELECT_P552203_PRESERVATION_DESTINATION_P1_GITHUB_NONSECRET_PACKAGE

Exact destination decision:
puev5691/wellbeing-hq@c3fdb21353c87cb326761e93516369755ddaee80:
entities/koordinator/outbox/KOO__STP-C-p552203-preservation-destination-P1-selected-r01__OPERATOR.md

Exact source VM:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Exact approved source set:
- /data/wellbeing-lab/backups/shd-pre-reinit-v01
- /data/wellbeing-lab/reports
- /opt/wb-shard-gateway

Exact GitHub destination root:
entities/sisadmin/outbox/p552203-stpc-preservation-r01/

Authorized:
- read source files;
- perform non-secret validation;
- create a preservation package containing approved non-secret source bytes and metadata;
- create checksum/manifest;
- publish package to the exact GitHub destination root;
- exact immutable readback/verification.

Fail-closed:
- if any secret, credential, private key, token, password, or ambiguous sensitive value is found, do NOT publish that file/content;
- return exact blocker;
- do not echo secret values into chat, logs, result files, or GitHub.

Not authorized:
- delete/move/modify source data;
- reset/reimage host;
- create STP-C proof roots;
- stop/remove gateway service/unit;
- inspect/publish /data/wellbeing-lab/secrets contents;
- backend install/run;
- T01-T20 execution;
- live WRITE/CAS;
- CHECKPOINT_DURABLE.
