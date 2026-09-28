# KOO record: authorize KOD STP-C anti-replay / TOCTOU / effect-binding design r0.1

status: OPERATOR_DOCUMENT_ONLY_DESIGN_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR instructed KOO to accept SIS degraded freshness/currentness correction r0.2 and determine the next already-authorized STP-C design/review step.

Exact freshness/currentness result:
puev5691/wellbeing-hq@ca13d99e6bfe385d184f2e5ebfbe40309bd35e2f:
entities/sisadmin/outbox/SIS__STP-C-degraded-freshness-currentness-design-r02__KOO.md
blob ecbeeda215fd3418503bdf947f79ddc8bbc7c3a8
terminal PASS_SIS_STP_C_DEGRADED_FRESHNESS_CURRENTNESS_DESIGN_R02_RECOVERY_DRIVEN_READY_FOR_KOO

Exact SHD review that required this second boundary:
puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md
terminal PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES

Scope:
DOCUMENT_ONLY_PROTOCOL_CONTRACT_DESIGN

Authorized:
- design exact anti-replay / TOCTOU / effect-binding contract;
- define closed request/evidence fields and invariants;
- define idempotency/replay/conflict semantics;
- bind signing/currentness/quorum/effect checks causally;
- produce decision-ready implementation contract candidate.

Not authorized:
- code implementation;
- key generation;
- credential creation;
- host mutation;
- deployment;
- Fast Gate/profile activation;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
