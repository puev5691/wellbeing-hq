# KOO → OPERATOR: operational shard store design decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Human meaning:
File/Artifact Service r0.2 is now independently verified.

The next convergence step is to design the actual operational shard store/CAS/fence/trust layer.

Existing shard gateway r0.3 remains READ/VERIFY-only.
No WRITE/CAS/store authority exists.

Proposed bounded next step:
authorize KOD to prepare a design-only operational shard store contract covering:
- immutable operational records;
- CAS current pointer;
- writer fence;
- task/entity binding;
- idempotency;
- retention/expiry as explicit unknown/policy inputs;
- fail-closed shard loss/Git mismatch;
- promotion boundary to File/Artifact Service and canonical GitHub;
- no authority semantics;
- no deployment;
- no shard WRITE;
- no EOM pilot;
- no memory-layering attempt 3.

After KOD design, route it to SIS + SHD for independent review.

Exact OPERATOR token to approve:

AUTHORIZE_KOD_OPERATIONAL_SHARD_STORE_CAS_FENCE_TRUST_DESIGN_R01_DOCUMENT_ONLY

This token authorizes design/document work only.
It does not authorize implementation, deployment, WRITE, host mutation, CHECKPOINT_DURABLE, EOM pilot or memory-layering attempt 3.

terminal:
PASS_KOO_OPERATIONAL_SHARD_STORE_DESIGN_GATE_WAITING_OPERATOR
