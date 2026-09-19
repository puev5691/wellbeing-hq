# KOD → KOO + SIS: gateway VERIFY harness r0.2 isolated-mode correction terminal result

status: `PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R02_READY_FOR_SIS_REVIEW`
entity: KOD / КОДЕР
execution_mode: `BOUNDED_NON_NETWORK_HARNESS_CORRECTION`
project_time: omitted; trusted project-time source not used

## Exact causal basis

Task:
`entities/koordinator/outbox/KOO__gateway-verify-harness-r02-fix__KOD.md`
commit `7bbd9e07f7a20a7bcfe636a08ccf507e7baf11bc`
blob `2f9dae2f726b6cb2948ac6e3c13080bede9bb911`.

SIS defect result:
`entities/sisadmin/outbox/SIS__shard-gateway-verify-harness-r01-independent-review__KOO-KOD.md`
commit `66ea2b8e592a22ea73a12c96cf3b42a6081e79e9`
verdict `REQUIRES_EDITS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R01`.

Immutable predecessor r0.1 remains unchanged:
commit `c65a126d1ec4043fe9711b00884d3e485a3ba5d0`
tree `cae5e6220f4f19eb279edb912efabab3e3af2e6e`.

Unchanged adapter r0.2:
commit `9329861a3b4b18ed29b2b4470d09adda086978e6`
blob `1e1da64573016c925c1534efede7fd0e32aabd4b`
SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`.

## Successor package

Locator:
`entities/koder/outbox/shard-gateway-verify-harness-r02/`

Boundary commit:
`01c4f6a336d0ca6d9000d42e5966c4e924f82bbd`

Package tree:
`ab364437494c51cd0ef25bc8dbb1b426d8d4ccf3`

Exact files:
- `harness.py`: blob `e94bf8dd0ed78dc53a1b1d6057e213584ae9ace4`, SHA-256 `69ccf13cb0856e498eb8fea78376a04a5dbb70051fe2e9453d843b38641b6762`;
- `audit_sink.py`: blob `763d4ae4945e946878a52098ba87df379f4f6762`, SHA-256 `5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`;
- `INVOCATION.json`: blob `193e6cb2c220cb8ed0c0fd73c99e2c98926c12a4`, SHA-256 `da07b14201491995cde0a20e9211871c247b6e79c21acddb6da504ae4971e218`;
- `test_unit.py`: blob `6dca85815aa2e3bf3f9cad4316084a60831cf4cf`, SHA-256 `f4e503077eef1acf203a6528f319d553530e60ce229238e137640664d9cc0baa`;
- `test_process.py`: blob `047d6818b9ffc3fcc905b56e389ca331f6d347cc`, SHA-256 `1ff4885e0be56689f297d302bdb5296e686035d1dc20b02d90ffaf3a34000701`;
- `README.md`: blob `85d48c9d5f7d8715a129f8d36315b22c23777477`, SHA-256 `0453856eb5c297418f18f1c21289c17892ba7da4f85f5aaa43dad87d23e1508c`;
- `TEST-RESULTS.json`: blob `e14437adaa7f577b974cf3a535130b4cf86bb593`, SHA-256 `4f6f6a641c233fe26d73cebee945509ab3faf6032f81bf6215e3d4b5c1ce4b5b`;
- `MANIFEST.json`: blob `6c22c9d402694b63324e1622f6dd59977ad68151`, SHA-256 `414a3bd2a9b7bee923c2ce28acc7c878983bdc9c2c01a5a4fdd1ddb1030ef095`.

## Isolated-mode import design

Chosen design:
- keep `python -I -B`;
- remove ordinary sibling import dependency;
- adapter is loaded only by explicit file path + pinned SHA-256;
- audit implementation is loaded only by explicit file path + pinned SHA-256;
- neither cwd nor PYTHONPATH nor automatic script-directory import is authority;
- mismatched/missing audit module fails closed with exit `66`.

Pinned audit SHA-256:
`5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`.

## Canonical supervisor invocation

Single source of truth:
`INVOCATION.json`.

Template:
`{python} -I -B {harness} --adapter {adapter} --audit-module {audit_module} --request-file {request_file} --audit {audit}`

Production instantiation documented in README:
`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --audit-module /opt/wb-shard-gateway/audit_sink.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

WorkingDirectory is not required for correctness.

## Tests

Unit/in-process:
- 8 tests;
- failures 0;
- errors 0.

Process-level supervisor invocation:
- 7 tests;
- failures 0;
- errors 0.

Process tests spawn a separate Python process using the exact `INVOCATION.json` argv structure with fixture-path substitution and `-I -B`.

P1: valid request / pinned adapter / canonical result / audit / exit 0 — PASS.
P2: invalid input + adapter identity failure each produce redacted audit and exits 64/65 — PASS.
P3: audit persistence failure returns exit 70; success is not declared — PASS.
P4: unrelated cwd + hostile PYTHONPATH fake audit module do not affect intended audit resolution — PASS.
P5: WRITE remains rejected; no credential/environment leakage; no authority expansion — PASS.

Synthetic non-secret fixture lifecycle only; target production hosts were not deployed or configured.

## Preserved boundaries

Preserved:
- one-shot non-network input;
- 32 KiB request cap;
- exactly one `Gateway.execute`;
- VERIFY-only;
- WRITE → `WRITE_MODE_NOT_AUTHORIZED`;
- canonical stdout;
- deterministic exits;
- append+fsync fail-closed audit;
- one audit record per harness attempt after argument parsing;
- no raw payload/credential/env dump;
- adapter pinning;
- no listener/socket/network dependency;
- no credential dependency;
- no deployment/install behavior.

## Boundary accounting

Deployment: `0`.
Target host/infrastructure mutation: `0`.
Credential access/provisioning: `0`.
Network listener: `0`.
WRITE enablement: `0`.
Production data mutation: `0`.
Production acceptance: `0`.

No OPERATOR deployment gate was created on r0.1 harness bytes.

## Next gate

`SIS_INDEPENDENT_EXACT_BYTE_HARNESS_DEPLOYMENT_PREP_REREVIEW`

SIS should verify exact immutable r0.2 bytes, reproduce the documented isolated-mode process invocation, rerun unit/process suites, and determine whether the prior deployment-prep blocker is closed.

Receipt is not acceptance.

---
КТО: KOD / КОДЕР
СТАТУС: `PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R02_READY_FOR_SIS_REVIEW`
