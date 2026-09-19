# Audit retention plan

status: DESIGN_ONLY

Schema:
`wb.shard_gateway.audit.v1`.

Proposed sink:
`/var/log/wellbeing/shard-gateway/audit-v1.jsonl`
(`PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`).

Required properties:
- append-only logical semantics;
- one canonical JSON event per operation;
- metadata/digests only;
- no raw file contents;
- no credential values or secret-bearing environment;
- bind `authority_ref`, host/root/op/target, result digest, status and duration;
- log rotation/retention must preserve provenance linkage.

Proposed access boundary:
- `arh-preserve` must not receive general write access to `/var/log`;
- preferred deployment integration is a narrowly scoped supervisor/audit writer or pre-opened append-only descriptor dedicated to this sink;
- exact mechanism remains `UNKNOWN_REQUIRES_PREDEPLOY_CHECK` until the execution harness is designed.

Retention proposal:
- rotate by size, not by guessed project time;
- retain current + bounded historical files according to future storage policy;
- immutable digest of rotated segment recorded into project provenance before disposal if disposal is authorized.

Failure rule:
if the audit sink cannot accept the operation record, the gateway operation must fail closed. Successful data result with missing audit record is forbidden.

Current r0.2 adapter serializes audit records but does not itself implement sink persistence. This is part of the execution-harness blocker and must not be silently improvised during deployment.
