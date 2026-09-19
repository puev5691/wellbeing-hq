# Shard gateway adapter r0.3 Git safe.directory correction

Successor of immutable adapter r0.2. This revision changes only the Git invocation policy required by the mazhor Phase-2 blocker plus deterministic regression evidence.

## Command-scoped Git safety

Every Git subprocess is constructed as:

`git -c safe.directory=<exact-allowlisted-repo-root> <existing-read-only-git-args...>`

The safe.directory value is taken only from the immutable `HOST_ROOTS[host_id][root_id]` mapping after request host/root validation. It is never accepted from request fields or environment, never uses `*`, and archive roots cannot enter the Git path.

The prefix is applied to all Git paths:
- status;
- rev-parse HEAD;
- HEAD tree;
- merge-base ancestor validation;
- ls-tree;
- blob metadata;
- blob bounded read.

No global/system/repository Git configuration is written. No HOME or GIT_CONFIG_* variables are used. Subprocess environment remains exactly `PATH=/usr/bin:/bin`, `LC_ALL=C`. Git is invoked by direct argv without shell interpolation.

## Preserved boundary

VERIFY-only, exact opcode/root allowlists, no burzh archive, erefia deferred, WRITE rejection, no-follow/TOCTOU hardening, ref validation, output/UTF-8 bounds, timeouts, no automatic failover and audit schema are unchanged from r0.2.

No deployment, host mutation, permissions/config mutation, service-user change, systemd change, credentials, listener/network, WRITE or production acceptance is performed by this package.

Different-uid real-identity confirmation remains for SIS resume on mazhor under the existing `arh-preserve` identity.
