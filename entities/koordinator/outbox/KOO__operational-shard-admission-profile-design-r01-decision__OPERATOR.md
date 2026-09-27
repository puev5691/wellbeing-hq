# KOO → OPERATOR: operational shard admission profile design r0.1 decision

status: WAITING_OPERATOR_DECISION
project_time: omitted

Human decision:
authorize one document-only SIS design task for the next shard-store admission layer.

Purpose:
prepare a concrete decision package for:
- SupervisorTrustProfile owner/issuer;
- WriterFenceAttestation / epoch attestor;
- revocation/currentness/freshness mechanism;
- candidate backend class and store owner/operator;
- isolation boundary;
- retention/GC policy fields;
- failure behavior when canonical authority is unavailable;
- exact conditions that would later be required before any bounded live admission.

This task must compare options and leave unresolved choices explicit.
It must NOT deploy or activate anything.

Exact reviewed offline basis:
puev5691/wellbeing-hq@9faa1ede62460fdcc073e48fd13b10f93027e957:
entities/koder/outbox/operational-shard-store-offline-r02
tree 8c5cb47ce3267dac4b1810e93cf993a35a3a0492

Independent PASS basis:
SIS @92038724366a4fb7e54c2e3014b70445bf28ae16
SHD @a76dfcea52627cbe73fe8b29abc152c3b3f25404
SHT @79a351255020a4a94b007117abefbb087bb59880

Exact OPERATOR token:

AUTHORIZE_SIS_OPERATIONAL_SHARD_ADMISSION_PROFILE_DESIGN_R01_DOCUMENT_ONLY

If approved:
KOO issues one bounded SIS document-only task.

If not approved:
r0.2 remains an independently reviewed offline synthetic candidate only.

This decision does NOT authorize:
- live WRITE/CAS;
- deployment;
- backend/trust-root appointment;
- host mutation;
- production admission;
- CHECKPOINT_DURABLE;
- EOM pilot;
- memory-layering attempt 3.
