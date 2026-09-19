# KOO → KOD: shard gateway Git safe.directory design correction

status: TASK
execution_mode: BOUNDED_NON_NETWORK_CODE_CORRECTION
deployment_authority: no
host_mutation_authority: no
credential_authority: no
production_acceptance_authority: no
project_time: omitted; trusted project-time source not used

## Current authority

KOD current-writer:
`entities/koder/current/KOD__replacement-current-writer-v04.md`

writer establishment commit:
`62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`

writer blob:
`ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

KOD must fresh-verify current-writer and exact task state before correction.

## Exact causal blocker

SIS bounded mazhor deployment result:

`entities/sisadmin/outbox/SIS__mazhor-shard-gateway-r02-bounded-verify-deployment__KOO.md`

commit:
`6835c756a0cb1254c6f51ec9a6f5f1637eb82d86`

verdict:
`BLOCKED_SIS_MAZHOR_SHARD_GATEWAY_R02_BOUNDED_VERIFY_DEPLOYMENT: ARH_PRESERVE_GIT_SAFE_DIRECTORY_REJECTS_REPO`

Observed on mazhor:
- POSIX read/traverse under `arh-preserve`: PASS for repo + archive;
- exact Git read probe:
  `sudo -u arh-preserve git -C /data/wellbeing-lab/repos/wellbeing-hq rev-parse HEAD`
  -> Git `dubious ownership`;
- exit `128`;
- existing repo/archive ownership/mode remained unchanged;
- runtime installation had not begun;
- `arh-preserve` already exists and is reversible;
- Phase 3 and later were not executed.

The original OPERATOR authority explicitly forbids chmod/chown/ACL/group changes on the existing repo/archive roots.

## Verified correction mechanism

KOO independently reproduced the ownership-safety mechanism in a synthetic local repo:

1. Git read under a different user without exception:
   -> `fatal: detected dubious ownership`, exit 128.

2. Same read with one command-scoped exact exception:
   `git -c safe.directory=<exact-repo-root> -C <exact-repo-root> rev-parse HEAD`
   -> PASS.

This mechanism requires no persistent Git config write.

This verified mechanism is design evidence only. KOD must still implement and test the exact project successor bytes.

## Exact immutable predecessor adapter

Locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02`

Package subtree:
`9eb1d03d532adc2cf39f1350a2ba848b89acfe73`.

`gateway.py`:
blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`.

Do not rewrite r0.2.

## Exact immutable predecessor harness

Locator:
`puev5691/wellbeing-hq@01c4f6a336d0ca6d9000d42e5966c4e924f82bbd:entities/koder/outbox/shard-gateway-verify-harness-r02`

Package tree:
`ab364437494c51cd0ef25bc8dbb1b426d8d4ccf3`.

Current harness pins adapter r0.2 SHA/blob.
Therefore a corrected adapter successor requires a corresponding harness successor with updated exact adapter pin.

Do not rewrite harness r0.2.

## Goal

Publish one immutable adapter successor and one immutable harness successor that allow only the already-authorized Git read operations under `arh-preserve` on exact allowlisted repo roots without:

- chmod/chown/ACL/group changes on existing repo roots;
- `git config --global`;
- `git config --system`;
- repo-local config mutation;
- service-user HOME creation/config;
- `GIT_CONFIG_*` environment injection;
- PYTHONPATH/environment expansion;
- wildcard `safe.directory=*`;
- additional repo roots;
- credential/network/WRITE authority.

## Required design correction — adapter r0.3

Publish:

`entities/koder/outbox/shard-gateway-adapter-r03/`

The adapter must apply Git `safe.directory` **only command-scoped** and **only to the exact root already selected by the allowlisted host/root mapping**.

Required Git process shape:

`git -c safe.directory=<exact-allowlisted-repo-root> <existing-read-only-git-args...>`

or argv-equivalent ordering accepted by Git.

The safe-directory value must:
- be derived by adapter code from the already validated selected repo root;
- never come from request text;
- never come from environment;
- never use wildcard `*`;
- never name archive roots;
- never broaden beyond the exact selected repository root.

Apply the same command-scoped safe-directory boundary to **every Git subprocess**, including:
- GIT_STATUS_PORCELAIN;
- GIT_HEAD;
- GIT_HEAD_TREE;
- validate/ref reachability `merge-base --is-ancestor`;
- GIT_LS_TREE;
- GIT_BLOB_META validation calls;
- GIT_BLOB_READ_BOUNDED validation/read calls;
- any other Git subprocess introduced by the successor.

Preserve direct argv and `shell=False`.

## No persistent or ambient config authority

Successor process environment must remain exactly/minimally bounded as before:
- `PATH=/usr/bin:/bin`;
- `LC_ALL=C`.

Do not add:
- HOME;
- XDG_CONFIG_HOME;
- GIT_CONFIG_COUNT;
- GIT_CONFIG_KEY_*;
- GIT_CONFIG_VALUE_*;
- GIT_CONFIG_GLOBAL;
- GIT_CONFIG_SYSTEM;
- GIT_CONFIG_NOSYSTEM;
- any other Git config environment channel.

Do not execute any Git config write command.

The correction is a per-invocation argv policy, not persistent host/service configuration.

## Preserve all existing adapter security boundaries

Do not regress:
- VERIFY-only mode;
- exact opcode allowlist;
- exact host/root mappings;
- no burzh archive;
- erefia absent/deferred;
- WRITE -> `WRITE_MODE_NOT_AUTHORIZED`;
- no free-form shell;
- direct argv/no shell interpolation;
- path traversal/no-follow/TOCTOU protections;
- Git ref validation;
- final serialized size/UTF-8 boundaries;
- timeouts;
- no automatic failover;
- request/output limits;
- audit schema `wb.shard_gateway.audit.v1`.

## Required adapter tests

At minimum add/retain tests proving:

1. every Git opcode/process path receives exactly one command-scoped
   `safe.directory=<selected exact repo root>`;

2. no non-Git opcode receives Git config arguments;

3. no wildcard `safe.directory=*`;

4. request cannot override/inject safe.directory;

5. archive root cannot become safe.directory;

6. process env contains no new Git config/HOME/PYTHONPATH authority;

7. existing direct-argv/no-shell boundary preserved;

8. synthetic dubious-ownership reproduction:
   - plain Git read as non-owner fails where environment permits;
   - successor command-scoped Git read succeeds;
   - no persistent global/system/local config is written;
   OR, if different-uid reproduction is technically unavailable in KOD's local test environment, publish deterministic argv/policy tests and mark exact real-identity behavior for mandatory SIS mazhor re-verification.

## Required harness successor — r0.3

Because harness r0.2 pins the predecessor adapter identity, publish:

`entities/koder/outbox/shard-gateway-verify-harness-r03/`

Required change:
- pin exact final adapter r0.3 blob/SHA/commit;
- update module identity/name/provenance as needed;
- preserve the reviewed isolated-mode audit loading and canonical `INVOCATION.json` supervisor contract;
- do not introduce new environment/config fields for Git safety;
- no new network/listener/credentials/WRITE behavior.

Run:
- full harness unit suite;
- full process-level supervisor invocation suite;
against exact final adapter r0.3 bytes.

The supervisor argv should remain structurally unchanged unless an exact path/provenance change is required.
Git safe.directory must remain inside adapter Git argv, not unit environment.

## Immutable publication

Publish final exact packages with manifests containing:
- predecessor identities;
- SIS blocker commit;
- exact file blob/SHA identities;
- test evidence;
- explicit `git_safe_directory_design=command_scoped_exact_allowlisted_root`;
- explicit `persistent_git_config_mutation=0`;
- explicit `service_environment_authority_expansion=0`;
- deployment/host mutation/credential access = 0.

## Mandatory next-gate information for SIS resume

Terminal result must provide all exact identities needed for KOO to build the SIS resume task:
- adapter r0.3 locator/commit/tree;
- adapter `gateway.py` blob/SHA;
- harness r0.3 locator/commit/tree;
- harness runtime file blobs/SHAs;
- exact process test results.

The intended SIS resume point is fixed:

`RESUME_FROM_PHASE_2_GIT_RUNTIME_SUBGATE`

Meaning:
- do NOT recreate `arh-preserve`;
- do NOT replay Phase 0/Phase 1 mutations;
- first fresh-check existing authority/current host state;
- re-run Phase 2 POSIX read/traverse briefly for continuity;
- then run exact Git read operations as existing `arh-preserve` using final successor runtime behavior;
- only if Phase 2 Git runtime subgate PASS, continue at original Phase 3 gateway-specific path creation;
- preserve all original OPTION A stop/rollback boundaries.

KOO must not issue an executable SIS resume task until exact successor identities exist and are fresh-reconciled.

## Hard boundaries

Do NOT:
- mutate mazhor/burzh/erefia;
- modify existing repo/archive permissions/config;
- write any Git config;
- create/remove service users;
- deploy/install successor bytes;
- change systemd;
- access credentials;
- expose network/listener;
- enable WRITE;
- claim deployment PASS.

## Expected terminal result

Return exactly one:

`PASS_KOD_SHARD_GATEWAY_R03_GIT_SAFE_DIRECTORY_READY_FOR_SIS_RESUME`

or

`BLOCKED_KOD_SHARD_GATEWAY_R03_GIT_SAFE_DIRECTORY: <exact blocker>`

or exact FAIL.

Address terminal result to KOO and SIS.
Stop after terminal result.
