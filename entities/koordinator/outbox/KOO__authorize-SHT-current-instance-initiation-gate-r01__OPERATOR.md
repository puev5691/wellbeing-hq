# KOO record: OPERATOR authorizes SHT current-instance Initiation Gate r0.1

status: OPERATOR_INITIATION_GATE_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR explicitly instructed KOO to fresh-reconcile SHT continuity/current-writer state under the active recovery canon and provide the minimum bounded recovery/initiation/writer-gate task required to establish whether the existing SHT instance is authorized to produce the pending governance-review result.

Scope:
INITIATION_GATE_ONLY for the existing SHT chat instance.

Purpose:
verify whether this exact existing SHT instance can be initiated against the externally preserved SHT recovery/current package.

Canonical recovery locator to verify:

repository:
puev5691/wellbeing-entity-bootstrap

immutable ref:
b34dd2cda94c2f61acc59a5f066c38bd24fdae0c

path:
entities/sht/recovery/current

Expected files/blobs at that immutable ref:
- SHT__role-definition-current__SHT.md
  blob 2cb8a1bc48dad450f84de478d625d7c667436425
- SHT__initiation-current__SHT.md
  blob eebe4aa896f079217317fefc4e98240856411529
- SHT__snapshot__SHT.md
  blob b3a0771e1adf3ae641f64c7a15b075291051f29b
- SHT__recovery-manifest__SHT.md
  blob 0d58ca9327118d9fd880b1c69b1de3ec6e1080ee
- sha256sums.txt
  blob 865873ea83327a29262e0d6787c6a5b955631709

Historical cold-start report exists only as provenance:
puev5691/wellbeing-entity-bootstrap:
entities/sht/reports/SHT__cold-start-initiation-report__OPR.md
blob 35f657329daa96b87514027f0bd44be37de3a72e

Historical initiation_verified does NOT establish writer authority for the current SHT instance.

Pending profile task to resume only after separate Writer Gate:
puev5691/wellbeing-hq@2b75d5f866586c42750884bc822374c8ea20337a:
entities/koordinator/outbox/KOO__operational-shard-admission-profile-r01-governance-review__SHT.md

Not authorized by this initiation gate:
- Writer Gate;
- current-writer establishment;
- governance review execution;
- live WRITE/CAS;
- deployment;
- trust-root/backend/operator selection;
- credentials;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
