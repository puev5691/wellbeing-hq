# KOO record: authorize SIS STP-C ledger backend candidate comparison r0.1

status: OPERATOR_DOCUMENT_ONLY_COMPARISON_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR instructed KOO to accept the completed SIS backend requirements profile and determine the next separately authorized backend candidate comparison/review step.

Exact requirements profile:
puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md
blob 73ede64f24208419ca339d8d2c2d40b2e3d9670a
terminal PASS_SIS_STP_C_LEDGER_BACKEND_REQUIREMENTS_R01_READY_FOR_CANDIDATE_COMPARISON
gate READY_FOR_BACKEND_CANDIDATE_COMPARISON_GATE

Scope:
DOCUMENT_ONLY_BACKEND_CANDIDATE_DISCOVERY_AND_COMPARISON

Authorized:
- identify a bounded, technically plausible candidate set;
- use current primary/official documentation for candidate capabilities;
- compare candidates only against the approved requirements matrix;
- mark unsupported/unknown claims UNKNOWN;
- identify disqualifiers and evidence gaps;
- produce decision-ready comparison for KOO/OPERATOR;
- if no candidate is yet adequately evidenced, return blocker/evidence tasks instead of selecting by intuition.

Not authorized:
- install/test live backends;
- create live storage;
- choose/deploy a backend as active;
- host mutation;
- credentials/secrets;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
