# Deployment preparation manifest

status: `PREP_PACKAGE_COMPLETE_WITH_DEPLOYMENT_HARNESS_BLOCKER`

## Immutable adapter basis

locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

boundary_commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`

package_subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`

SIS independent reverify:
`ed56678fb190c278440aa2bcfa83a258d54daf27`

ARH preservation PASS:
`36b1c3c5c823358e9e32a14a9102d556be431265`

## Preparation artifacts

- `DEPLOYMENT-PLAN.md` blob `28f35ba20c0cbe825da352b6750680d507db7448`
- `PERMISSIONS-MATRIX.md` blob `c4d6b951f55489e2f235d01783d6c5f2088e76d4`
- `SERVICE-UNIT-CANDIDATE.md` blob `19b3c16cf7c9a6ea923a90f50232b6e990576928`
- `AUDIT-RETENTION-PLAN.md` blob `c2b9d1af06ebc54205ba285d49201fd9a1247ca8`
- `CREDENTIAL-BOUNDARY.md` blob `ee25ced9f44cdb1121d3205b87600790353588bf`
- `PREDEPLOY-CHECKLIST.md` blob `19b10fea323d5aeadcf90865c24700d9fac24cc0`
- `MUTATION-AUTHORITY-GATE.md` blob `fda538e92d8539d5624753d0ab3061b3299e17c1`

This manifest's own immutable blob and final package subtree are recorded by the terminal SIS result after publication; self-hash is intentionally not recursively embedded.

## Read-only observations

mazhor:
- host `p552203.kvmvps`;
- Python 3.12.3 at `/usr/bin/python3`;
- systemd tooling present;
- `arh-preserve` absent;
- repo top-level mode 0775 owner/group `shd:shd`;
- archive top-level mode 0775 owner/group `shd:shd`;
- proposed /opt, /etc and audit directories absent.

burzh:
- host `ruvds-xnqc6`;
- Python 3.12.3 at `/usr/bin/python3`;
- systemd tooling present;
- `arh-preserve` absent;
- repo top-level mode 0775 owner/group `pev5691:pev5691`;
- proposed /opt, /etc and audit directories absent;
- Remote Desktop Commander stale-cwd/getcwd warning persists.

## Unknowns

- recursive effective read/traverse permissions for future `arh-preserve`: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`;
- exact stale-cwd root cause on burzh: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`;
- exact future audit sink implementation/permissions: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`;
- exact execution harness identity: `BLOCKED_REQUIRES_KOD_SUCCESSOR`;
- future service environment under systemd: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`;
- optional OS sandbox/bind-mount design: `UNKNOWN_REQUIRES_OPERATOR_DECISION`.

## Blocking finding

The exact r0.2 adapter package has no executable gateway request loop/CLI and no persistent audit-sink writer. Therefore no truthful functional service `ExecStart` can be formed from unchanged r0.2 bytes.

Required next causal gate:
`KOD_SHARD_GATEWAY_R02_EXECUTION_HARNESS_DESIGN_AND_IMMUTABLE_CANDIDATE`.

## Boundary accounting

deployment_performed: 0
host_mutation_performed: 0
credential_access: 0
production_acceptance: 0
WRITE_enabled: 0
listener_exposure: 0
repository_archive_shard_mutation: 0
