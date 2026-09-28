# KOO → SIS: P552203 PRESERVATION_COPY_R01

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: BOUNDED_NONSECRET_PRESERVATION_COPY_AND_GITHUB_READBACK
project_time: omitted

Resume-First.

Exact authority:
puev5691/wellbeing-hq@d5c32241e96b781e9fc6fbfe9e81e5eb0718405e:
entities/koordinator/outbox/KOO__authorize-SIS-P552203-preservation-copy-r01__OPERATOR.md

Exact VM:
device: 830038a0-232b-4d83-b52d-0e9973126165
hostname: p552203.kvmvps

Exact source set:
- /data/wellbeing-lab/backups/shd-pre-reinit-v01
- /data/wellbeing-lab/reports
- /opt/wb-shard-gateway

Exact GitHub destination root:
entities/sisadmin/outbox/p552203-stpc-preservation-r01/

Do only preservation copy/publication.

Required:

1. Freshly verify source paths and exact VM identity.
2. Inspect source bytes only as needed to classify secret/sensitive risk.
3. FAIL CLOSED if any file contains or plausibly contains:
   - secret/token/password/private key/API key;
   - credential material;
   - ambiguous sensitive runtime value unsuitable for project Git.
4. Never print secret values.
5. For every safe published file preserve:
   - source locator;
   - relative path;
   - byte size;
   - SHA-256;
   - mode/ownership when operationally relevant.
6. Create manifest/checksum file.
7. Publish only safe non-secret bytes to:
   entities/sisadmin/outbox/p552203-stpc-preservation-r01/
8. Obtain immutable commit/tree/file identities.
9. Read back exact published bytes and recompute checksums.
10. Return whether the full approved preservation set is now externally preserved.

Special gateway rule:
- if /opt/wb-shard-gateway/INVOCATION.json or any other gateway file contains sensitive/ambiguous values, do NOT publish it;
- report only the blocked locator and classification, not the value.
- partial preservation does not count as complete preservation of /opt/wb-shard-gateway.

Do NOT:
- touch /data/wellbeing-lab/secrets contents;
- delete/move/modify any source;
- stop/remove services;
- reset/reimage p552203;
- create STP-C proof roots;
- install/run backend;
- execute T01-T20.

Expected terminal:

PASS_SIS_P552203_PRESERVATION_COPY_R01_IMMUTABLE_READBACK_COMPLETE

or exact

BLOCKED_SIS_P552203_PRESERVATION_COPY_R01_<REASON>

After immutable result + exact readback + return KOO, STOP.
