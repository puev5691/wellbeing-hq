# Shard gateway adapter candidate r0.1

Standalone non-deploying candidate implementing the exact SIS shard gateway design.

The request contract is typed (`wb.shard_gateway.request.v1`) and hard-coded to `VERIFY`. There is no free-form command field and no caller-supplied absolute path. WRITE requests fail closed with `WRITE_MODE_NOT_AUTHORIZED`.

Immutable host/root mapping:
- mazhor / `MAZHOR_REPO_WELLBEING_HQ` → `/data/wellbeing-lab/repos/wellbeing-hq`
- mazhor / `MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01` → `/data/wellbeing-lab/backups/shd-pre-reinit-v01`
- burzh / `BURZH_REPO_WELLBEING_HQ` → `/home/pev5691/wellbeing-hq`

Burzh archive access is absent until separately verified. Erefia is absent/deferred.

VERIFY operations are exactly the SIS allowlist. Relative paths are normalized fail-closed, symlinks and denied secret/system targets are rejected, output is bounded, per-operation timeout policy is explicit, and concurrency is one per host. Git calls use direct argv construction, not shell interpolation.

There is no automatic cross-host failover. r0.1 does not treat equivalent-object metadata as authority.

Audit output is canonical JSON compatible with `wb.shard_gateway.audit.v1`; it contains metadata only, never file contents or credential values.

## Trust boundary

Future deployment must independently provide the least-privilege `arh-preserve` identity, read-only permissions, stable working directory, minimal environment, audit storage/retention, and service sandboxing.

This package performs no deployment, SSH mutation, users/groups/ACL changes, service/systemd/firewall changes, credential provisioning/read, network listener exposure, WRITE enablement, or shard/repository/archive mutation.

## Limitations

Synthetic tests validate request/path/error/serialization boundaries. They do not prove production host permissions or OS sandbox properties. Filesystem race handling uses before/after identity checks; independent verification should review descriptor-relative/no-follow hardening on target hosts before deployment.

No historical Entity Resource Gateway bytes or authorities are reused.
