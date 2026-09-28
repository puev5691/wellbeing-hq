# KOO record: authorize SIS STP-C degraded freshness/currentness design r0.1

status: OPERATOR_DOCUMENT_ONLY_DESIGN_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR instructed KOO to process the completed SHD independent review and determine one next authorized step.

Exact SHD review:
puev5691/wellbeing-hq@342e28309b1aed48505f0feb6eadcd8a9e5808ca:
entities/shardovik/outbox/SHD__STP-C-key-storage-r02-independent-review__KOO.md
blob 6efd2cb71d8ff6be248f1c2abc33ac39ccb4f6fa
terminal PASS_SHD_STP_C_KEY_STORAGE_R02_INDEPENDENT_REVIEW_WITH_BOUNDARIES

Mandatory unresolved boundary selected for this task:
freshness/currentness during prolonged Git outage.

Scope:
DOCUMENT_ONLY_SECURITY_POLICY_DESIGN

Authorized:
- design bounded freshness/currentness policy for degraded signing mode;
- compare policy alternatives;
- define fail-closed behavior;
- preserve distinction between availability and stale-authority risk;
- prepare one decision-ready table for OPERATOR.

Not authorized:
- choose a timeout without evidence;
- activate degraded mode;
- generate keys;
- create credentials;
- host mutation;
- deployment;
- Fast Gate/profile activation;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
