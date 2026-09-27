# KOO record: OPERATOR authorizes operational shard store design r0.1

status: OPERATOR_AUTHORITY_RECORDED
project_time: omitted

Exact OPERATOR token:

AUTHORIZE_KOD_OPERATIONAL_SHARD_STORE_CAS_FENCE_TRUST_DESIGN_R01_DOCUMENT_ONLY

Scope:
design/document only for an operational shard store with CAS/fence/trust semantics.

Authorized:
- design immutable operational record model;
- design CAS current pointer;
- design writer fence and entity/task binding;
- design idempotency and supersession;
- design fail-closed loss/mismatch behavior;
- define retention/expiry as explicit policy inputs/UNKNOWN where not decided;
- define boundary to verified File/Artifact Service r0.2 and canonical GitHub;
- define compatibility/limits with existing shard gateway r0.3 READ/VERIFY;
- return implementation-ready design for independent review.

Not authorized:
- shard WRITE;
- shard store implementation;
- deployment;
- host/Commander mutation;
- EOM pilot;
- memory-layering attempt 3;
- CHECKPOINT_DURABLE;
- Project Sources/canon/current-writer mutation;
- automatic writer transfer.
