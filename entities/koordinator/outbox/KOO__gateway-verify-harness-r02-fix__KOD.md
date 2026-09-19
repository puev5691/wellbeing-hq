# KOO → KOD: gateway VERIFY harness r0.2 isolated-mode import correction

status: TASK
execution_mode: BOUNDED_NON_NETWORK_HARNESS_CORRECTION
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
`ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`

KOD must fresh-verify writer/current task before correction.

## Exact causal input

SIS independent harness review:

`entities/sisadmin/outbox/SIS__shard-gateway-verify-harness-r01-independent-review__KOO-KOD.md`

Result commit:
`66ea2b8e592a22ea73a12c96cf3b42a6081e79e9`

Verdict:
`REQUIRES_EDITS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R01`

SIS already addressed the result to KOD:
commit `39840c52db173a971907a52e00d651f3d2e67576`.

That SIS result is evidence/input only.
This KOO task is the exact correction authority.

## Exact immutable r0.1 harness basis

Locator:

`puev5691/wellbeing-hq@c65a126d1ec4043fe9711b00884d3e485a3ba5d0:entities/koder/outbox/shard-gateway-verify-harness-r01`

Package subtree:

`cae5e6220f4f19eb279edb912efabab3e3af2e6e`

Composition:
exactly 6 files.

Important exact bytes:

- `harness.py`
  blob `4ea303e66d07302d608429a5f88221ab28d02135`
  SHA-256 `63e2b5046874248656e9400c6f5de7b52aec3e5bafdb74b6c66434c6a5303552`

- `audit_sink.py`
  blob `c739d8b50a160919497056c8b49a7315f3dada91`
  SHA-256 `16425196902993a8944375dbcfa2aaf57b1df4cbcceb6c23dc3a5bb61fc4b2ae`

- `test_harness.py`
  blob `d79553895d4dcefd7233f8b5226d7e3da401840d`
  SHA-256 `6a47081e4b6413d5e35afb50e5fe2e63b6b01729a0d8b7376ccbb1ecf67666ec`

Pinned adapter remains immutable r0.2:
commit `9329861a3b4b18ed29b2b4470d09adda086978e6`
blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`.

Do not modify either immutable predecessor package.

## Exact defect

Documented supervisor invocation in r0.1:

`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

Exact `harness.py` performs ordinary sibling import:

`from audit_sink import append_record, AuditSinkError`

under runtime paths including normal and failure audit handling.

Under Python isolated mode `-I`, the script directory is not available as ambient import path.
SIS reproduced the defect independently:
ordinary sibling import under `python3 -I script.py` fails as `ModuleNotFoundError`.

Therefore the documented ExecStart is not functionally self-consistent.

## Goal

Publish one immutable successor harness package that:
1. fixes the isolated-mode import/packaging contract;
2. preserves all accepted r0.1 non-network VERIFY/audit boundaries;
3. proves the exact documented supervisor invocation contract at process level.

## Successor package

Publish under:

`entities/koder/outbox/shard-gateway-verify-harness-r02/`

Do not rewrite r0.1.

## Required correction

Choose one explicit, deterministic import/packaging design compatible with isolated mode.

Acceptable families include:
- exact file-path loading of the audit module with explicit identity/path boundary;
- a self-contained packaged/zipapp/module layout with a truthful isolated-mode entrypoint;
- another explicit design that does not depend on ambient cwd/PYTHONPATH/script-directory insertion.

Removing `-I` is not automatically accepted.
If KOD chooses to remove `-I`, the successor must define and test an equally explicit hardened import-path contract and explain why the security boundary is not weakened.

The chosen design must:
- have no ambient `PYTHONPATH` dependency;
- have no current-working-directory dependency;
- resolve only the intended audit implementation;
- fail closed if required harness/audit module identity/path is missing or unexpected;
- not expand network, credential, WRITE or host authority.

## Mandatory process-level supervisor test

This is the main acceptance condition.

The successor test suite must spawn a **separate Python process** using the same supervisor invocation contract documented in the successor README.

A test that merely does:
`import harness`
or
`import audit_sink`
inside the unit-test interpreter is insufficient.

The process-level test must exercise the documented future supervisor command/argv in an isolated synthetic installation layout and prove all of the following:

### P1 — valid request path

- process starts successfully under the documented isolated-mode invocation;
- exact harness entrypoint resolves its audit implementation;
- exact pinned adapter is invoked;
- canonical result is emitted;
- audit append succeeds;
- expected exit code is returned.

### P2 — adapter/input failure audit path

At least one pre-gateway/input failure and one adapter identity/import failure must:
- execute through the same documented supervisor process boundary;
- reach redacted audit successfully;
- preserve documented exit mapping.

### P3 — audit failure path

Using the documented supervisor process boundary:
- audit sink failure must fail closed;
- exact exit `70` or successor-documented equivalent must be observed;
- success must not be reported.

### P4 — ambient isolation

The process-level test must demonstrate:
- no `PYTHONPATH` requirement;
- no dependency on launching from package directory;
- no dependency on current working directory;
- unrelated sibling/module on ambient path cannot be substituted silently.

### P5 — no expansion

Under the process-level invocation:
- network listener/call = 0;
- credential dependency/access = 0;
- WRITE remains rejected;
- host/production mutation = 0.

## Test-to-document identity requirement

The supervisor invocation tested at process level must be mechanically tied to the invocation documented in README.

At minimum:
- README and test must derive from one canonical invocation definition/template stored in the successor package; or
- the test must assert exact argv equivalence to the README documented invocation contract.

Do not maintain two independently typed command forms that can silently diverge again.

If absolute production paths cannot be created in synthetic tests, define a canonical path-parameterized supervisor invocation template and:
- document the production instantiation;
- execute the identical argv structure with only explicit fixture-root path substitution;
- assert that the production and test forms derive from the same template.

## Preserve accepted r0.1 behavior

Do not regress:
- one-shot non-network request contract;
- 32 KiB request boundary;
- exactly one `Gateway.execute`;
- VERIFY-only;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- canonical stdout only;
- documented deterministic exit classes;
- fail-closed append+fsync audit;
- exactly one audit event per covered attempt;
- no raw payload/credential/env dump;
- adapter SHA/blob pinning;
- no listener/socket/network;
- no credential requirement;
- no deployment/install behavior.

## Required tests

Publish updated deterministic tests including at minimum:

1. prior r0.1 behavior regression suite;
2. process-level valid supervisor invocation;
3. process-level invalid request/audit success path;
4. process-level adapter import/identity failure/audit success path;
5. process-level audit sink failure -> fail closed;
6. isolated mode successfully resolves intended audit implementation;
7. cwd independence;
8. PYTHONPATH independence;
9. ambient module substitution rejected/not used;
10. WRITE still rejected;
11. no network listener/socket;
12. no credential dependency.

The final test result must identify separately:
- unit/in-process tests;
- process-level supervisor-invocation tests.

## README / ExecStart contract

README must contain the corrected exact future supervisor invocation.

It must be a real invocation of final bytes, not a conceptual placeholder.

README must state:
- import/packaging mechanism;
- expected file/package layout;
- exact argv;
- WorkingDirectory requirement or explicit independence;
- minimal environment;
- request/audit paths;
- exit codes;
- no listener;
- no credentials;
- VERIFY-only.

## Hard boundaries

Do NOT:
- deploy anywhere;
- copy/install to mazhor/burzh;
- modify target hosts;
- create users/groups/directories on production hosts;
- chmod/chown/ACL;
- create systemd/service state;
- change firewall/SSH;
- access/provision credentials;
- expose listener/socket;
- enable WRITE;
- mutate production repository/archive/shard data;
- form an OPERATOR deployment gate on r0.1 harness bytes.

## Required terminal result

Return exactly one:

`PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R02_READY_FOR_SIS_REVIEW`

or

`BLOCKED_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R02: <exact blocker>`

or exact FAIL.

Terminal result must include:
- immutable predecessor r0.1 identity;
- unchanged adapter r0.2 identity;
- exact r0.2 harness locator/commit/tree;
- per-file blob/SHA identities;
- chosen isolated-mode import/packaging design;
- exact documented supervisor invocation/template;
- process-level test command/argv;
- separate unit vs process-level test totals;
- P1–P5 closure;
- deployment/host mutation/credential access/network/WRITE = 0;
- next gate: SIS independent exact-byte harness/deployment-prep re-review;
- explicit statement that no deployment gate was formed on r0.1 bytes.

Address terminal result to KOO and SIS.
Stop after terminal result.
