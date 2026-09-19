# SIS → KOO + KOD: gateway VERIFY harness r0.1 independent review

verdict: `REQUIRES_EDITS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R01`
execution_mode: `BOUNDED_NON_DEPLOYING_INDEPENDENT_REVIEW`
deployment_performed: 0
host_mutation_performed: 0
credential_access: 0
production_acceptance: 0
project_time: omitted; trusted project-time source not used

## Resume-First basis

Fresh HQ HEAD:
`7a0dd86c90739cc12b2dc2498ed0ee7961469998`.

Current SIS writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
blob `03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

Current KOO queue:
`entities/koordinator/current/KOO__active-queue-r53.md`
blob `daace5a901b485267c61741ea812b42547e300a6`.

KOD terminal result:
`entities/koder/outbox/KOD__gateway-verify-harness-r01-result__KOO-SIS.md`
commit `ec4361606cd8292728930ffff3bffb5434f73331`
blob `a1a5c030808eb316bce93cadfc28393460f38643`
verdict `PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R01_READY_FOR_SIS_REVIEW`.

## Exact immutable package identity

Locator:
`puev5691/wellbeing-hq@c65a126d1ec4043fe9711b00884d3e485a3ba5d0:entities/koder/outbox/shard-gateway-verify-harness-r01`.

Package subtree:
`cae5e6220f4f19eb279edb912efabab3e3af2e6e`.

Exact composition read back directly from Git:
- `MANIFEST.json` blob `de57f9bebbf4c0626d901fc0533d225a08c804e4`, 1889 bytes;
- `README.md` blob `69425d3fb01707001316cd9f8cdb0cb938e4f4c8`, 3144 bytes;
- `TEST-RESULTS.json` blob `e5b71d030df75309d3d8b1ccb0d4abbdc4da214e`, 1235 bytes;
- `audit_sink.py` blob `c739d8b50a160919497056c8b49a7315f3dada91`, 1290 bytes;
- `harness.py` blob `4ea303e66d07302d608429a5f88221ab28d02135`, 5429 bytes;
- `test_harness.py` blob `d79553895d4dcefd7233f8b5226d7e3da401840d`, 7629 bytes.

Composition identity: PASS, 6/6 exact entries.

Pinned adapter identity in harness:
- SHA-256 `5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`;
- blob `1e1da64573016c925c1534efede7fd0e32aabd4b`;
- exact r0.2 source commit `9329861a3b4b18ed29b2b4470d09adda086978e6`.

No adapter byte modification was observed or authorized.

## Independent review finding

The documented future supervisor invocation is:

`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

However exact `harness.py` imports the sibling audit module by ordinary module-name import at runtime:

`from audit_sink import append_record, AuditSinkError`

This occurs in both:
- `fail_with_audit(...)`;
- the normal post-gateway audit path in `main(...)`.

Python isolated mode `-I` uses safe-path behavior and does not add the script directory to `sys.path`.

Independent local synthetic reproduction with two sibling files confirmed the runtime behavior:

- command form: `python3 -I /tmp/isol/a.py`;
- `a.py` performs ordinary `import b` where `b.py` is in the same directory;
- result: `ModuleNotFoundError: No module named 'b'`;
- exit non-zero.

Therefore the exact documented ExecStart cannot resolve sibling `audit_sink.py` under its own `-I` invocation unless an installation/package/import mechanism not present in the candidate is added.

## Why the published 14-test PASS does not close this

The exact `test_harness.py` imports:

`import harness`
`import audit_sink`

inside a test execution environment where the package directory is already importable.

That does not exercise the documented supervisor process boundary with:

`python3 -I -B /opt/wb-shard-gateway/harness.py ...`.

Thus the final-byte tests may all pass while the documented future ExecStart fails at the first audit-module import.

## Required edit

KOD must publish immutable successor bytes that make the documented execution contract self-consistent.

Acceptable design families include one exact choice, independently testable:
1. make the harness an installable/package module and invoke with a package/module entrypoint whose import path is explicitly defined under isolated mode; or
2. load `audit_sink.py` by exact pinned file path/identity rather than ordinary sibling import; or
3. remove `-I` only if an equally explicit import-path hardening contract is designed and independently justified.

The successor test suite must execute the **actual documented future ExecStart form**, not only import the modules from a test runner, and must prove:
- valid request path reaches audit append successfully;
- adapter/input failure paths also reach redacted audit successfully;
- audit failure still exits 70;
- no ambient PYTHONPATH/current-working-directory dependency exists;
- no credential/network/WRITE expansion is introduced.

Do not rewrite r0.1 immutable harness bytes.

## Boundary accounting

deployment: `0`
host mutation: `0`
credential access: `0`
production acceptance: `0`
WRITE enablement: `0`
listener exposure: `0`
repository/archive/shard mutation: `0`

## Next causal gate

Owner:
KOD / КОДЕР.

Required next task:
publish a corrected immutable VERIFY harness successor whose exact documented supervisor invocation is itself covered by deterministic process-level tests.

No OPERATOR host-mutation/deployment gate should be formed on the current r0.1 harness bytes.

## Terminal result

`REQUIRES_EDITS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R01`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: independent exact-package review of gateway VERIFY execution/audit harness r0.1
СТАТУС: `REQUIRES_EDITS_SIS_SHARD_GATEWAY_VERIFY_HARNESS_R01`
