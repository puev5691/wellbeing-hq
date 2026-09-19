# Service/supervisor candidate

status: BLOCKED_PENDING_EXECUTION_HARNESS
installed: no

## Required service properties

Future service user:
`User=arh-preserve`.

Stable working directory:
`WorkingDirectory=/var/lib/wellbeing/shard-gateway`
(`PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`).

Minimal environment proposal:
`PATH=/usr/bin:/bin`
`LC_ALL=C`
No inherited credential variables.

Security intent:
- VERIFY only;
- no WRITE;
- no network listener;
- no automatic cross-host failover;
- one concurrent operation per host;
- fail closed;
- no restart storm; restart only on abnormal harness failure and only after an implementation defines a persistent process.

## Exact ExecStart status

A functional exact `ExecStart` CANNOT be truthfully specified for unchanged r0.2.

Reason: exact package contains `gateway.py` as a library and tests/docs/manifest only. It has no CLI/main request loop and no audit-sink writer.

The superficially possible argv:

`/usr/bin/python3 /opt/wellbeing/shard-gateway/r02/gateway.py`

is explicitly REJECTED as a deployment candidate because it merely loads definitions and exits without processing gateway requests.

## Required KOD successor boundary

Before a systemd/supervisor unit can be accepted, KOD must publish an immutable execution harness defining:
- exact bounded request input contract;
- exact invocation of `Gateway.execute`;
- canonical result emission;
- `wb.shard_gateway.audit.v1` emission and fail-closed sink behavior;
- no credential inheritance;
- no listener by default;
- no WRITE;
- exit/error semantics suitable for supervision.

Only after that immutable harness is independently verified can an exact `ExecStart=[argv]` and restart/resource policy be finalized.
