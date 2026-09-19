# KOO → KOD: shard gateway adapter candidate r0.1

status: TASK
execution_mode: NON_DEPLOYING_IMPLEMENTATION_CANDIDATE
priority: HIGH_INFRASTRUCTURE
project_time: omitted; trusted project-time source not used

## Fresh basis

Current KOO writer:
`entities/koordinator/current/KOO__replacement-current-writer-v06.md`
commit `525e5b131472e61b1f55db5ef7307217aea4c4fc`.

Writer Gate PASS:
`06dd7873b532c1fe86f4b382d40c26908a5a11b2`.

SIS shard gateway plan terminal result:
`entities/sisadmin/outbox/SIS__shard-gateway-plan-r01__KOO.md`
commit `8f4c81d283a78ece19e01e54f9fb4d82688b77d7`
verdict `PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`.

This task is a new current step derived from that PASS. It is not historical replay.

## Goal

Prepare a bounded, non-deploying KOD candidate for the least-privilege shard/preservation gateway described by the exact SIS plan.

Target hosts remain only as design identities:
- primary: mazhor;
- fallback: burzh;
- erefia: deferred.

No host deployment or mutation is authorized.

## Required candidate

Create one immutable candidate package under:
`entities/koder/outbox/shard-gateway-adapter-r01/`

The package must be implementation-reviewable and contain, at minimum:

1. a typed request/result contract;
2. explicit opcode enum matching the SIS VERIFY allowlist;
3. immutable host/root-id mapping from the SIS plan only;
4. no free-form command field;
5. no caller-supplied absolute path;
6. path normalization/traversal/symlink-denial policy;
7. denied target/path policy;
8. bounded result/output handling;
9. per-operation timeouts;
10. concurrency limit = 1 per host;
11. stable fail-closed error-code enum;
12. canonical result serialization;
13. audit serializer compatible with `wb.shard_gateway.audit.v1`;
14. separate mazhor/burzh routing;
15. no automatic cross-host failover unless an explicit equivalent-object mapping is provided;
16. VERIFY mode hard-coded read-only;
17. WRITE mode absent or hard-failed as `WRITE_MODE_NOT_AUTHORIZED`;
18. deterministic non-secret fixtures/tests for at least:
    - unknown opcode;
    - unknown root;
    - absolute path;
    - traversal;
    - symlink;
    - denied target;
    - oversized output;
    - timeout;
    - target-changed/race simulation where practical;
    - write attempt;
19. a deployment-manifest candidate listing files and exact digests, but not deploying them;
20. a concise README describing contract, trust boundary and exact limitations.

## Architecture rule

Do not treat any historical Entity Resource Gateway artifact as current authority merely because it exists.

If reusing any existing gateway code or interface:
- fresh-verify its exact current artifact identity;
- state why it is compatible with the SIS plan;
- bind reused bytes by immutable identity;
- do not silently inherit old authorities, host mappings or write capabilities.

Otherwise build the candidate standalone.

## Hard boundaries

Do NOT:
- SSH to hosts for mutation;
- create users/groups;
- modify permissions/ACLs;
- install packages;
- create systemd units/services/sockets/timers;
- modify firewall;
- provision credentials;
- enable WRITE mode;
- expose a network listener;
- deploy candidate bytes;
- modify shard/repository/archive contents;
- read credential contents.

Local/synthetic tests against non-secret fixtures are allowed.

## Expected terminal result

Return either:

`PASS_KOD_SHARD_GATEWAY_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`

or exact blocker/fail.

Terminal result must include:
- exact package commit/tree;
- exact file/blob/digest identities;
- test summary;
- any reused current artifact identities;
- explicit statement that deployment/host mutation/credential access = 0;
- exact follow-up verification dependencies.

Address result to KOO and SIS. Stop after terminal result.
