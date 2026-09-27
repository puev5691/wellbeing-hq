# KOO → ARH: independent SHT recovery checksum verification r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: ARH / АРХИВАРИУС
scope: READ_ONLY_INDEPENDENT_RECOVERY_CHECKSUM_VERIFICATION
project_time: omitted

Resume-First.

Exact authority:

puev5691/wellbeing-hq@8e8fb239bbdde93707dc2d328ef603d1343e13fd:
entities/koordinator/outbox/KOO__authorize-ARH-SHT-recovery-checksum-verify-r01__OPERATOR.md

Current ARH writer basis:

puev5691/wellbeing-hq@5fc0c161915b328e9ffea4fb925999c4de192826:
entities/archivarius/current/ARH__replacement-current-writer-r02.md

Exact SHT partial initiation result:

puev5691/wellbeing-hq@d3448524ad51267dd39f724bbf1d3f8852b79173:
entities/shtabist/outbox/SHT__current-instance-initiation-gate-r01-result__KOO.md
blob 31c6383f535ecc464cff0a512122d616396c3f97

Verify only the missing checksum boundary.

## Exact immutable recovery

Repository:
puev5691/wellbeing-entity-bootstrap

Ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

Path:
entities/sht/recovery/current

Independently obtain exact bytes and calculate SHA-256 for:

1. SHT__role-definition-current__SHT.md
expected:
3c93cb22494a5e415b4e8a13ba37cac5d4b5022d9f79f0ce6e2524e62c765297

2. SHT__initiation-current__SHT.md
expected:
34b370bb539fbb9e0bbc23e16040534513f5417bb25a19c244721423ac8b818c

3. SHT__snapshot__SHT.md
expected:
e20b74e75e161f0d7e243061bcc00498df98b07d1dcd2b99754e062ff6fa458a

4. SHT__recovery-manifest__SHT.md
expected:
d2c24ea2a4a97260fe359422c713555ef757f07155aeba407e66c8c72ec7c186

Also verify sha256sums.txt at the same ref:
expected Git blob:
865873ea83327a29262e0d6787c6a5b955631709

Required evidence:
- immutable ref actually used;
- exact file path;
- exact Git blob;
- independently calculated SHA-256;
- expected SHA-256;
- PASS/FAIL per file;
- total 4/4 status;
- no content reconstruction from memory;
- no substitution of Git blob equality for SHA-256 calculation.

Expected terminal:

PASS_ARH_SHT_RECOVERY_CHECKSUM_VERIFY_R01_4_OF_4

or exact FAIL_/BLOCKED_.

If any exact bytes cannot be obtained or independently hashed, STOP with blocker.
Do not infer PASS.

Do NOT:
- modify recovery;
- establish SHT writer;
- execute SHT governance review;
- open/perform Writer Gate;
- live WRITE/CAS;
- deployment;
- trust-root/backend/operator selection;
- credentials;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

After standalone immutable result + exact readback + addressed return to KOO/SHT, STOP.
