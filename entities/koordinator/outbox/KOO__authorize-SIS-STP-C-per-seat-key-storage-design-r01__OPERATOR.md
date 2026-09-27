# KOO record: authorize SIS STP-C per-seat key storage/recovery design r0.1

status: OPERATOR_DOCUMENT_ONLY_DESIGN_AUTHORITY_RECORDED
project_time: omitted

Authority basis:
OPERATOR selected K2 per-seat logically separated custody under OPERATOR control.

Exact selection:
puev5691/wellbeing-hq@c4a2426aeb87c1121c9af9baa4f546ae29556c48:
entities/koordinator/outbox/KOO__STP-C-key-custody-K2-selected__OPERATOR.md

Scope:
DOCUMENT_ONLY_SECURITY_STORAGE_RECOVERY_DESIGN

Authorized:
design candidate storage/recovery/rotation/revocation model for future distinct KOO/KAN/SIS authentication keys.

Not authorized:
- generate keys;
- create credentials;
- read/store secret values;
- choose final product/vendor without evidence;
- deploy;
- host mutation;
- live WRITE/CAS;
- profile activation;
- Fast Gate activation;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
memory-layering attempt 3 remains NOT_AUTHORIZED.
