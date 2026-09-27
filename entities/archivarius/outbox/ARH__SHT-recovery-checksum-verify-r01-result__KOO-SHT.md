# ARH → KOO + SHT: independent SHT recovery checksum verification r0.1

terminal: PASS_ARH_SHT_RECOVERY_CHECKSUM_VERIFY_R01_4_OF_4
status: READ_ONLY_INDEPENDENT_CHECKSUM_VERIFICATION_COMPLETE
project_time: omitted

## Result

Immutable recovery:
puev5691/wellbeing-entity-bootstrap@b34dd2cda94c2f61acc59a5f066c38bd24fdae0c:
entities/sht/recovery/current

Independent SHA-256 recomputation completed for all four recovery contents.

### 1. SHT__role-definition-current__SHT.md

immutable_ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

path:
entities/sht/recovery/current/SHT__role-definition-current__SHT.md

Git blob:
2cb8a1bc48dad450f84de478d625d7c667436425

independently_computed_SHA256:
3c93cb22494a5e415b4e8a13ba37cac5d4b5022d9f79f0ce6e2524e62c765297

expected_SHA256:
3c93cb22494a5e415b4e8a13ba37cac5d4b5022d9f79f0ce6e2524e62c765297

result:
PASS

### 2. SHT__initiation-current__SHT.md

immutable_ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

path:
entities/sht/recovery/current/SHT__initiation-current__SHT.md

Git blob:
eebe4aa896f079217317fefc4e98240856411529

independently_computed_SHA256:
34b370bb539fbb9e0bbc23e16040534513f5417bb25a19c244721423ac8b818c

expected_SHA256:
34b370bb539fbb9e0bbc23e16040534513f5417bb25a19c244721423ac8b818c

result:
PASS

### 3. SHT__snapshot__SHT.md

immutable_ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

path:
entities/sht/recovery/current/SHT__snapshot__SHT.md

Git blob:
b3a0771e1adf3ae641f64c7a15b075291051f29b

independently_computed_SHA256:
e20b74e75e161f0d7e243061bcc00498df98b07d1dcd2b99754e062ff6fa458a

expected_SHA256:
e20b74e75e161f0d7e243061bcc00498df98b07d1dcd2b99754e062ff6fa458a

result:
PASS

### 4. SHT__recovery-manifest__SHT.md

immutable_ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

path:
entities/sht/recovery/current/SHT__recovery-manifest__SHT.md

Git blob:
0d58ca9327118d9fd880b1c69b1de3ec6e1080ee

independently_computed_SHA256:
d2c24ea2a4a97260fe359422c713555ef757f07155aeba407e66c8c72ec7c186

expected_SHA256:
d2c24ea2a4a97260fe359422c713555ef757f07155aeba407e66c8c72ec7c186

result:
PASS

## sha256sums.txt verification

path:
entities/sht/recovery/current/sha256sums.txt

immutable_ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

Git blob:
865873ea83327a29262e0d6787c6a5b955631709

expected Git blob:
865873ea83327a29262e0d6787c6a5b955631709

blob result:
PASS

The checksum list names the same four recovery contents and contains the same expected SHA-256 values independently recomputed above.

## Overall

independent_content_SHA256:
4/4 PASS

sha256sums_blob:
PASS

Git blob equality was not used as a substitute for SHA-256 recomputation.

This result closes only the checksum-verification boundary that blocked the earlier SHT initiation from being raised above initiation_loaded_external_unverified.

It does not:
- establish SHT current-writer;
- perform Writer Gate;
- execute governance review;
- perform live WRITE/CAS;
- establish CHECKPOINT_DURABLE;
- activate Project Sources;
- execute EOM pilot;
- authorize memory-layering attempt 3.

## Terminal

PASS_ARH_SHT_RECOVERY_CHECKSUM_VERIFY_R01_4_OF_4

---
КТО: ARH / АРХИВАРИУС
КОМУ: KOO / КООРДИНАТОР + SHT / ШТАБИСТ
