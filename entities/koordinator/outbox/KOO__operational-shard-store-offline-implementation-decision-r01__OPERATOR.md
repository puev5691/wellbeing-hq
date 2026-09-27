# KOO → OPERATOR: operational shard store offline implementation/test decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Current basis:
- design passed independent SIS + SHD document reviews;
- store runtime does not yet exist;
- WRITE/CAS is not authorized;
- both reviews identify the next safe causal class as an offline implementation/test candidate.

Proposed exact next step:
KOD builds a versioned offline schema/serialization + operation/CAS/fence state-machine candidate with deterministic vectors and crash/idempotency tests.

Scope must remain:
- synthetic/local test roots only;
- no host deployment;
- no live shard root;
- no gateway WRITE;
- no Commander;
- no secrets;
- no trust-root appointment;
- no operational WRITE/CAS authority;
- no CHECKPOINT_DURABLE;
- no EOM pilot;
- no memory-layering attempt 3.

Expected result:
implementation/test candidate ready for independent SIS + SHD + SHT review.

Exact OPERATOR token:

AUTHORIZE_KOD_OPERATIONAL_SHARD_STORE_OFFLINE_IMPLEMENTATION_TEST_R01

If not approved:
shard line remains at reviewed design stage and no runtime capability is claimed.
