# Permissions matrix

status: DESIGN_ONLY

| Host | Object | Verified current state | Future `arh-preserve` requirement | Forbidden | Mutation authority |
|---|---|---|---|---|---|
| mazhor | `/data/wellbeing-lab/repos/wellbeing-hq` | dir 0775, owner/group `shd:shd` | read/traverse only | write/delete/chmod/chown/admin/credentials | recursive effective access: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`; changes require authority |
| mazhor | `/data/wellbeing-lab/backups/shd-pre-reinit-v01` | dir 0775, owner/group `shd:shd` | read/traverse only | write/delete/extract-to-host/admin/credentials | recursive effective access: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`; changes require authority |
| burzh | `/home/pev5691/wellbeing-hq` | dir 0775, owner/group `pev5691:pev5691` | read/traverse only | write/delete/chmod/chown/admin/credentials | recursive effective access: `UNKNOWN_REQUIRES_PREDEPLOY_CHECK`; changes require authority |
| both | `/opt/wellbeing/shard-gateway/r02` | absent | read/execute installed immutable code | source modification by service identity | create/install requires authority |
| both | `/etc/wellbeing/shard-gateway/verify.json` | parent proposal absent | read only | write/credential material | create/install requires authority |
| both | `/var/lib/wellbeing/shard-gateway` | not checked as existing; proposed | stable cwd, no project data | arbitrary project writes | create/ownership requires authority |
| both | `/var/log/wellbeing/shard-gateway/audit-v1.jsonl` | parent proposal absent | audit append via separately defined sink boundary | read project contents, credential logging | create/permissions/retention requires authority |

Read-only host check confirmed `arh-preserve` account is absent on both targets.

No ACL/chmod/chown/group mutation was performed.

The gateway service identity must not join sudo/admin groups and must not receive repository/archive write permissions.
