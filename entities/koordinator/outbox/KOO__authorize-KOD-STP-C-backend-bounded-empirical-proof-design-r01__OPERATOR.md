# KOO record: authorize KOD STP-C bounded backend empirical proof design r0.1

status: OPERATOR_DOCUMENT_ONLY_PROOF_DESIGN_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR instructed KOO to accept SIS backend candidate comparison r0.1 and authorize only the next bounded empirical-proof design/task.

Exact SIS comparison:
puev5691/wellbeing-hq@9f401ffef3b3d90ec28a2786ec076d87d36f7e74:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-candidate-comparison-r01__KOO.md
blob da9dedea095bc245f03d19b0e595c27740aa3464
terminal PASS_SIS_STP_C_LEDGER_BACKEND_CANDIDATE_COMPARISON_R01_READY_FOR_DECISION_OR_PROOF
gate READY_FOR_BOUNDED_EMPIRICAL_BACKEND_PROOF

Exact requirements profile:
puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md
blob 73ede64f24208419ca339d8d2c2d40b2e3d9670a

Surviving documentary candidates:
- PostgreSQL 18
- FoundationDB 7.4.8
- etcd 3.7
- CockroachDB v26.1/current stable documentation line

Scope:
DOCUMENT_ONLY_BOUNDED_EMPIRICAL_PROOF_HARNESS_DESIGN

Authorized:
- design a backend-neutral non-production proof harness and candidate adapters;
- define exact test cases, fault injection points, observable evidence and PASS/FAIL oracle;
- define candidate-specific setup assumptions only as test inputs, not product selection;
- include CockroachDB corruption/integrity documentary UNKNOWN as a required proof item.

Not authorized:
- install/run any backend;
- create live storage;
- choose a backend winner;
- host mutation;
- credentials/secrets;
- production test;
- deployment;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.
