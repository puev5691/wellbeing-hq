# Predeploy checklist

status: DESIGN_ONLY

Every check is read-only until an explicit mutation gate is approved.

## Immutable artifact

- [ ] read exact adapter commit `9329861a3b4b18ed29b2b4470d09adda086978e6`;
- [ ] confirm subtree `9eb1d03d532adc2cf39f1350a2ba848b89acfe73`;
- [ ] confirm exact 5-file blobs;
- [ ] confirm future execution-harness immutable identity separately.

## Host identity

mazhor expected: `p552203.kvmvps`.
burzh expected: `ruvds-xnqc6`.

- [ ] verify hostname, OS, Python executable/version, systemd availability.

Current read-only observation: Python `/usr/bin/python3` version 3.12.3 and `/usr/bin/systemctl` present on both.

## Root identity/access

- [ ] mazhor repo exists at exact path;
- [ ] mazhor archive exists at exact path;
- [ ] burzh repo exists at exact path;
- [ ] no burzh archive mapping;
- [ ] inspect effective recursive read/traverse access as intended service identity after account creation is separately authorized;
- [ ] prove no write access.

Current top-level modes are verified 0775, but effective recursive service access is `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`.

## Service account and directories

- [ ] `arh-preserve` exact account identity and groups;
- [ ] no sudo/admin group;
- [ ] executable/config/cwd/audit directories exact identity;
- [ ] ownership/modes match approved matrix.

Current read-only observation: `arh-preserve` absent on mazhor and burzh. Proposed /opt, /etc and audit directories were absent at checked exact paths.

## Burzh stale-cwd

- [ ] execute authorized read-only command with explicit stable cwd;
- [ ] no `getcwd` warning.

Current observation: Remote Desktop Commander on burzh still emits stale-cwd/getcwd warnings even when command requests `cd /tmp`; root cause remains `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`.

## Conflicts/listeners

- [ ] no existing shard/wellbeing gateway service with same unit/socket;
- [ ] no proposed listener port in use if a later listener is separately authorized.

Current read-only observation found no matching shard/wellbeing listener. Burzh has unrelated disabled `wellbeing-telegram-phase1b-sandbox.service`; do not modify it.

## Audit

- [ ] exact sink integration defined by verified execution harness;
- [ ] append-only/fail-closed behavior tested;
- [ ] rotation/retention authority approved.

## Rollback

- [ ] exact installed file list and hashes;
- [ ] exact service/account/permission changes authorized;
- [ ] reversal commands prepared before mutation;
- [ ] repository/archive roots excluded from rollback deletion.

## Secret-bearing environment

- [ ] inspect service environment declarations and environment variable names only;
- [ ] no token/secret/password/API-key/private-key variable;
- [ ] no credential files.

## Authority

Every mutation must cite the exact future OPERATOR/KOO authority artifact. No generic deployment approval is inferred.
