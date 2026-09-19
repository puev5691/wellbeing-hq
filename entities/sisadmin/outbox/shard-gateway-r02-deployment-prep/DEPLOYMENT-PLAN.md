# Shard gateway r0.2 deployment preparation plan

status: DESIGN_ONLY
deployment_authority: no
host_mutation_authority: no

## Architecture

Primary future target: `mazhor` / host `p552203.kvmvps`.
Fallback future target: `burzh` / host `ruvds-xnqc6`, as a separate explicitly authorized deployment step. No automatic failover.
Deferred: `erefia`.

Exact immutable adapter:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`
subtree `9eb1d03d532adc2cf39f1350a2ba848b89acfe73`.

Read-only service identity: `arh-preserve`.
Future WRITE identity `shard-write` remains reserved and absent.

## Verified target roots

mazhor:
- repo: `/data/wellbeing-lab/repos/wellbeing-hq`;
- archive: `/data/wellbeing-lab/backups/shd-pre-reinit-v01`.

burzh:
- repo: `/home/pev5691/wellbeing-hq`;
- no archive root.

## Proposed placement

The following are proposals only and do not currently exist on either checked host:

- executable/library: `/opt/wellbeing/shard-gateway/r02/` — `PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`;
- config: `/etc/wellbeing/shard-gateway/verify.json` — `PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`;
- stable WorkingDirectory: `/var/lib/wellbeing/shard-gateway` — `PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`;
- audit sink: `/var/log/wellbeing/shard-gateway/audit-v1.jsonl` — `PROPOSED_REQUIRES_HOST_MUTATION_AUTHORITY`.

Python 3.12.3 and systemd tooling were read-only verified on both current targets.

## Deployment stages

1. PREDEPLOY: re-read exact package identity; verify host/root identity, account state, recursive read/traverse capability, Python/runtime behavior, absence of conflicting gateway service/listener, audit design and authority refs.
2. INSTALL: prohibited now. Future gate must authorize identity, directories, exact immutable files and supervisor/audit integration.
3. VERIFY: isolated local VERIFY-mode smoke only; no listener, no WRITE; verify root allowlist, denial paths, audit output and fail-closed behavior.
4. ROLLBACK: stop/disable only the newly authorized gateway integration; remove only exact installed gateway artifacts/account changes covered by that authority; leave repositories/archives untouched.
5. PRODUCTION ACCEPTANCE: separate future gate after target-host verification evidence.

## Deployment blocker found during preparation

The exact r0.2 package is a Python library candidate, not a deployable service/CLI package. It defines `Gateway` and serializers but no executable request loop, CLI entrypoint, stdin/stdout contract, persistent service loop or audit-sink writer.

Therefore a truthful functional `ExecStart` for gateway operation cannot be specified from the unchanged r0.2 bytes. Running `python3 gateway.py` only imports/defines code and exits; it does not provide gateway service behavior.

A deployment harness/entrypoint must be separately designed and published by KOD before installation authority can be formed. It must preserve:
- VERIFY-only mode;
- no network listener unless separately authorized;
- bounded one-request input;
- canonical result output;
- fail-closed audit handling;
- no credential inheritance;
- no WRITE path.

This is a deployment packaging/integration defect. r0.2 adapter bytes are not modified here.
