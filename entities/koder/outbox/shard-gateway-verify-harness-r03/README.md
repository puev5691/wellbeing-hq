# Shard gateway VERIFY harness r0.3 isolated-mode correction

Successor of immutable r0.1 harness. The r0.1 package is not modified.

## Correction

The r0.1 failure came from ordinary sibling import of `audit_sink` under Python isolated mode. r0.3 removes that dependency. Both adapter and audit implementation are loaded only from explicit file paths using `importlib.util.spec_from_file_location` after SHA-256 identity verification.

Pinned audit implementation SHA-256:
`5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88`

Pinned unchanged adapter:
- blob `d42e58060365c4b996bf87c81f3e3eb2ad684ceb`
- SHA-256 `9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881`
- source commit `9140d2ffe2b2ab983ce4a607447b5cc20f44ec6f`

No `PYTHONPATH`, current working directory, or automatic script-directory import is used for adapter/audit resolution.

## Canonical supervisor invocation

The single source of truth is `INVOCATION.json`. Its argv template is:

`{python} -I -B {harness} --adapter {adapter} --audit-module {audit_module} --request-file {request_file} --audit {audit}`

Production instantiation:

`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --audit-module /opt/wb-shard-gateway/audit_sink.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

`WorkingDirectory` is not required by the harness import contract. Future supervisor may set a stable directory for operational hygiene, but correctness does not depend on it.

Minimal future environment:
- `PATH=/usr/bin:/bin`
- `LC_ALL=C`
- no inherited secret-bearing variables.

## Input, stdout and exit codes

One JSON request file, maximum 32 KiB. No trailing non-whitespace JSON. Exactly one `Gateway.execute` call for a valid request.

Stdout is exactly one canonical JSON result plus newline.

Exit codes:
- 0 success;
- 20 gateway rejection;
- 64 input failure with redacted audit;
- 65 adapter identity/import failure with redacted audit;
- 66 audit-module missing/mismatch/import failure;
- 70 audit persistence failure.

Audit remains local JSONL, `O_APPEND|O_NOFOLLOW`, full-write + fsync before successful outcome. No raw payload, credential values or environment dump.

## Test contract

`test_process.py` reads the exact same `INVOCATION.json` template used above and spawns a separate Python process. Fixture paths substitute only the path placeholders; argv structure and `-I -B` are unchanged. Tests run from an unrelated cwd with a hostile `PYTHONPATH` containing a fake audit module to prove ambient substitution is unused.

Synthetic process fixtures only. No production roots, credentials, network listeners or deployment are used.

## Boundary

VERIFY-only and WRITE rejection remain inherited from the unchanged adapter. No HTTP/TCP/UDP/socket listener, credential dependency, deployment/install behavior, production host mutation or production acceptance is introduced.
