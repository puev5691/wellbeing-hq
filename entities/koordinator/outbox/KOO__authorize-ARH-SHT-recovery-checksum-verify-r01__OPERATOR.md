# KOO record: OPERATOR authorizes ARH independent SHT recovery checksum verification r0.1

status: OPERATOR_READ_ONLY_VERIFICATION_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR explicitly instructed KOO to provide the minimum bounded mechanism/task needed to independently calculate and compare SHA-256 for the exact four SHT recovery files at immutable ref b34dd2c....

Scope:
READ_ONLY_INDEPENDENT_RECOVERY_CHECKSUM_VERIFICATION_ONLY

Current ARH writer:
puev5691/wellbeing-hq@5fc0c161915b328e9ffea4fb925999c4de192826:
entities/archivarius/current/ARH__replacement-current-writer-r02.md
status WRITER_ESTABLISHED

Exact SHT initiation partial result:
puev5691/wellbeing-hq@d3448524ad51267dd39f724bbf1d3f8852b79173:
entities/shtabist/outbox/SHT__current-instance-initiation-gate-r01-result__KOO.md
blob 31c6383f535ecc464cff0a512122d616396c3f97
outcome initiation_loaded_external_unverified

Exact recovery:
repository puev5691/wellbeing-entity-bootstrap
ref b34dd2cda94c2f61acc59a5f066c38bd24fdae0c
path entities/sht/recovery/current

Files to independently hash:
- SHT__role-definition-current__SHT.md
  expected SHA-256 3c93cb22494a5e415b4e8a13ba37cac5d4b5022d9f79f0ce6e2524e62c765297
- SHT__initiation-current__SHT.md
  expected SHA-256 34b370bb539fbb9e0bbc23e16040534513f5417bb25a19c244721423ac8b818c
- SHT__snapshot__SHT.md
  expected SHA-256 e20b74e75e161f0d7e243061bcc00498df98b07d1dcd2b99754e062ff6fa458a
- SHT__recovery-manifest__SHT.md
  expected SHA-256 d2c24ea2a4a97260fe359422c713555ef757f07155aeba407e66c8c72ec7c186

sha256sums.txt expected blob:
865873ea83327a29262e0d6787c6a5b955631709

Authorized:
- fetch exact immutable bytes;
- independently calculate SHA-256;
- compare against sha256sums.txt;
- verify exact file/blob/ref identity;
- publish standalone verification result to KOO/SHT.

Not authorized:
- modify recovery;
- create/update SHT current-writer;
- execute SHT governance review;
- Writer Gate;
- live WRITE/CAS;
- deployment;
- trust-root/backend/operator selection;
- credentials;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
