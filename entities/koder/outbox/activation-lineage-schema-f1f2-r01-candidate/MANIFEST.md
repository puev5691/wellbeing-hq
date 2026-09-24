# Activation-lineage schema F1/F2 successor candidate

status: CANDIDATE_FOR_SHT_REVIEW
project_time: omitted
base: puev5691/wellbeing-hq@6890803d88b0d582b7baa51a275a488f3de9e6f6:entities/koder/outbox/activation-lineage-schema-v01-candidate
exact_task: puev5691/wellbeing-hq@0d01344f77a32554ad9534ccb2cf0bf5c3d23906:entities/koordinator/outbox/KOO__activation-lineage-schema-f1f2-correction-r01__KOD.md

Composition: schema.json, FIELD-MAP.md, CROSS_RECORD_INVARIANTS.md, TEST-VECTORS.md, TEST-FIXTURES.json, DIFF.patch, TEST-RESULTS.json, MANIFEST.md. Immutable version is package path plus publication commit/tree, not an updated $id. The schema byte diff is exactly DIFF.patch: F2 PROVEN requires local event_claim_verified=true; F1 semantic identifiers must be non-null and non-empty. CROSS_RECORD_INVARIANTS.md is byte-identical to base. FIELD-MAP/TEST-VECTORS clarify only these two changes and their effect on unchanged records.

Existing 24-record set remains immutable: 22 accepted and two historical records A-EVT-01/02 rejected after F1, because both have null experiment_id/task_id. This is a migration/data compatibility blocker, not a reason to weaken F1 or rewrite old evidence in this task. No collection validator, automation, production or canon promotion.
