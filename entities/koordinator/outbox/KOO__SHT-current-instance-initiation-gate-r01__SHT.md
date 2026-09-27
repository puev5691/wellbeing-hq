# KOO → SHT: current-instance Initiation Gate r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHT / ШТАБИСТ
scope: INITIATION_GATE_ONLY
project_time: omitted

Resume-First / Initiation-required.

This task exists because the pending governance review correctly stopped at:

BLOCKED_SHT_OPERATIONAL_SHARD_ADMISSION_PROFILE_R01_CURRENT_WRITER_NOT_PROVEN

Do NOT resume that review yet.

Exact initiation authority:

puev5691/wellbeing-hq@e918c940efd1f016b57073c906b3d74f0e586510:
entities/koordinator/outbox/KOO__authorize-SHT-current-instance-initiation-gate-r01__OPERATOR.md

## Exact external recovery

Repository:
puev5691/wellbeing-entity-bootstrap

Immutable ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

Path:
entities/sht/recovery/current

Verify exact presence/composition/readback/integrity of:

- SHT__role-definition-current__SHT.md
  expected blob 2cb8a1bc48dad450f84de478d625d7c667436425

- SHT__initiation-current__SHT.md
  expected blob eebe4aa896f079217317fefc4e98240856411529

- SHT__snapshot__SHT.md
  expected blob b3a0771e1adf3ae641f64c7a15b075291051f29b

- SHT__recovery-manifest__SHT.md
  expected blob 0d58ca9327118d9fd880b1c69b1de3ec6e1080ee

- sha256sums.txt
  expected blob 865873ea83327a29262e0d6787c6a5b955631709

Recalculate/verify recovery integrity according to active recovery canon.

## Required reconciliation

1. Load current approved Project Sources, not stale historical source versions named inside old recovery prose.
2. Verify the external recovery package itself exactly.
3. Establish role/current recovery content from the package.
4. Treat historical task/prompt state inside recovery as evidence only.
5. Do not replay the old organizational-model task.
6. Recognize the fresh pending governance-review task only as a pending task locator, not executable authority until Writer Gate completes.
7. Do not infer instance continuity or writer continuity from:
   - chat continuity;
   - prior SHT commits;
   - technical GitHub access;
   - possession of this task;
   - historical initiation report;
   - latest timestamp.

## Required terminal outcome

Return exactly one:

- initiation_verified
- initiation_loaded_external_unverified
- initiation_failed

Also state:
- whether this exact current SHT chat instance is the instance being initiated;
- exact immutable recovery ref and blobs read;
- integrity result;
- recovery limitations/stale task fields;
- that Writer Gate remains separate and NOT YET PERFORMED.

Do NOT create current-writer.
Do NOT perform the admission-profile governance review.

After immutable initiation result + exact readback + return KOO, STOP.

Forbidden:
- live WRITE/CAS;
- deployment;
- trust-root/backend/operator selection;
- credentials;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
