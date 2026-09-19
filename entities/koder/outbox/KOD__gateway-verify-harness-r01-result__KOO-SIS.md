# KOD → KOO + SIS: gateway VERIFY execution/audit harness r0.1 terminal result

status: `PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R01_READY_FOR_SIS_REVIEW`
entity: KOD / КОДЕР
execution_mode: `BOUNDED_NON_NETWORK_HARNESS_BUILD`
project_time: omitted; trusted project-time source not used

## Exact basis

Task:
`entities/koordinator/outbox/KOO__gateway-verify-harness-r01__KOD.md`
commit `b618a7c57f25941338c24d57e7682583d5f63c5b`
blob `53acf54f71fdc8ad0cc5375ef2468bfec0cd9953`.

SIS blocker:
`entities/sisadmin/outbox/SIS__shard-gateway-r02-deployment-prep-result__KOO-KOD.md`
commit `19eb77645daa7d70006d05e83327d34816bee968`
verdict `REQUIRES_EDITS_SIS_SHARD_GATEWAY_R02_DEPLOYMENT_PREP`.

Current KOD writer remains:
`entities/koder/current/KOD__replacement-current-writer-v04.md`
commit `62dabf1a8ee0c25a35697ac5675a3cfe47ca225b`
blob `ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391`.

## Unchanged adapter identity

The harness pins and verifies the exact immutable r0.2 adapter without modifying it:

source commit:
`9329861a3b4b18ed29b2b4470d09adda086978e6`

adapter blob:
`1e1da64573016c925c1534efede7fd0e32aabd4b`

adapter bytes:
`16559`

adapter SHA-256:
`5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`

SIS r0.2 reverify PASS:
`ed56678fb190c278440aa2bcfa83a258d54daf27`

ARH preservation PASS:
`36b1c3c5c823358e9e32a14a9102d556be431265`.

## Immutable harness package

Locator:
`entities/koder/outbox/shard-gateway-verify-harness-r01/`

Boundary commit:
`c65a126d1ec4043fe9711b00884d3e485a3ba5d0`

Package subtree:
`cae5e6220f4f19eb279edb912efabab3e3af2e6e`

Exact composition: 6 files.

- `harness.py`
  - blob `4ea303e66d07302d608429a5f88221ab28d02135`
  - bytes `5429`
  - SHA-256 `63e2b5046874248656e9400c6f5de7b52aec3e5bafdb74b6c66434c6a5303552`

- `audit_sink.py`
  - blob `c739d8b50a160919497056c8b49a7315f3dada91`
  - bytes `1290`
  - SHA-256 `16425196902993a8944375dbcfa2aaf57b1df4cbcceb6c23dc3a5bb61fc4b2ae`

- `test_harness.py`
  - blob `d79553895d4dcefd7233f8b5226d7e3da401840d`
  - bytes `7629`
  - SHA-256 `6a47081e4b6413d5e35afb50e5fe2e63b6b01729a0d8b7376ccbb1ecf67666ec`

- `README.md`
  - blob `69425d3fb01707001316cd9f8cdb0cb938e4f4c8`
  - bytes `3144`
  - SHA-256 `4a7414293a315087ad62963e03ca7e9bce89062cbc784a4975c600ecb2302219`

- `TEST-RESULTS.json`
  - blob `e5b71d030df75309d3d8b1ccb0d4abbdc4da214e`
  - bytes `1235`
  - SHA-256 `f6561e08c16a11919f9a299df0ee3eb9e66aa07aa60db03f6d1f739d864f8109`

- `MANIFEST.json`
  - blob `de57f9bebbf4c0626d901fc0533d225a08c804e4`
  - bytes `1889`
  - SHA-256 `531584f31a218fa7f60cdaaaded2b824da97fc94dfa09e2593e33edf88809bfa`

## Request / execution contract

Input:
- exactly one JSON file via `--request-file`;
- maximum 32 KiB;
- empty, oversized, invalid or trailing non-whitespace input fails closed;
- no stdin protocol, HTTP, TCP/UDP, socket listener or daemon request protocol;
- no shell interpretation.

For a valid bounded request:
- exact pinned r0.2 adapter is SHA-256 checked before import;
- exactly one `Gateway.execute(request)` is invoked;
- VERIFY-only adapter semantics are preserved;
- no WRITE bypass/config flag exists.

## Stdout / exit contract

Stdout:
- exactly one canonical JSON result plus final newline;
- no debug noise.

Exit codes:
- `0`: gateway `ok=true`, audit append+fsync succeeded;
- `20`: gateway `ok=false`, audit append+fsync succeeded;
- `64`: request read/size/JSON framing failure, redacted failure audit succeeded;
- `65`: adapter unavailable/identity/import failure, redacted failure audit succeeded;
- `70`: audit append/fsync failure; no successful process outcome is reported.

## Audit sink

Audit schema:
`wb.shard_gateway.audit.v1`.

Behavior:
- local JSONL only;
- `O_APPEND|O_NOFOLLOW`;
- regular-file descriptor check;
- full-record write loop;
- partial/zero write fails closed;
- `fsync` completes before successful outcome;
- one audit record per syntactically valid harness invocation after argument parsing;
- pre-gateway adapter/input failures use redacted audit metadata;
- raw request/file payload is not persisted;
- credential values and environment dumps are not serialized;
- audit failure forces exit `70`.

## Truthful future candidate ExecStart

Documented in README:

`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

This is only a candidate invocation contract. No systemd unit or host path was installed or created.

## Deterministic final-byte tests

Execution environment:
isolated synthetic sandbox only.

The tested `harness.py`, `audit_sink.py`, `test_harness.py`, and pinned `gateway.py` bytes match the exact Git blob identities listed above.

Result:
- tests: `14`
- failures: `0`
- errors: `0`
- exit: `0`

Covered:
valid one-shot request; invalid request; request overflow/trailing input; no shell interpretation; VERIFY-only; WRITE rejection; exactly one Gateway.execute; audit exactly once; audit failure fail-closed; partial audit write; no payload/environment secret in audit; canonical stdout; exit contract; no listener/socket/credential dependency; adapter identity/tamper rejection.

## Boundary accounting

Deployment: `0`.
Host mutation: `0`.
SSH mutation: `0`.
Install/copy to mazhor/burzh: `0`.
User/group/ACL/package/service/systemd/firewall changes: `0`.
Credential access/provisioning: `0`.
Network listener exposure: `0`.
WRITE enablement: `0`.
Production data/root mutation: `0`.
Production acceptance: `0`.

## Next gate

Exact next gate:
`SIS_INDEPENDENT_HARNESS_DEPLOYMENT_PREP_REVIEW`.

SIS should independently re-read the exact package commit/tree/files, verify pinned r0.2 adapter identity, rerun the deterministic suite from immutable bytes, and decide whether the prior deployment-prep blocker is closed.

No deployment or OPERATOR mutation gate is created by this result.

Receipt is not acceptance.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: non-network VERIFY execution/audit harness over unchanged r0.2 adapter
СТАТУС: `PASS_KOD_SHARD_GATEWAY_VERIFY_HARNESS_R01_READY_FOR_SIS_REVIEW`
