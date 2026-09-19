# Shard gateway VERIFY execution/audit harness r0.1

Non-network one-shot harness around the unchanged verified r0.2 adapter.

## Immutable adapter basis

Required adapter SHA-256:
`5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30`

Required adapter Git blob:
`1e1da64573016c925c1534efede7fd0e32aabd4b`

Source locator:
`puev5691/wellbeing-hq@9329861a3b4b18ed29b2b4470d09adda086978e6:entities/koder/outbox/shard-gateway-adapter-r02/gateway.py`

The harness verifies SHA-256 before importing the adapter and does not modify its bytes.

## Invocation contract

Exactly one request is read from one JSON file named by `--request-file`. Maximum input is 32 KiB. Empty, oversized, invalid or trailing non-whitespace input fails closed.

No stdin protocol, daemon loop, HTTP, TCP/UDP, socket listener or network transport exists.

Candidate future supervisor command:

`/usr/bin/python3 -I -B /opt/wb-shard-gateway/harness.py --adapter /opt/wb-shard-gateway/gateway.py --request-file /run/wb-shard-gateway/request.json --audit /var/log/wb-shard-gateway/audit.jsonl`

This is only a truthful candidate ExecStart. No unit, directory or file is installed by this package.

## Execution semantics

For a valid bounded input the harness invokes exactly one `Gateway.execute(request)`.

Stdout contains exactly one canonical JSON result plus a final newline. No debug text is emitted to stdout.

Exit codes:
- 0: gateway result `ok=true` and audit append+fsync completed;
- 20: gateway result `ok=false` and audit append+fsync completed;
- 64: request file/read/size/JSON framing failure before gateway execution;
- 65: pinned adapter unavailable, identity mismatch or import failure;
- 70: audit append/fsync failure. A gateway success is never reported as process success if audit persistence fails.

## Audit sink

Audit is local-file only, canonical JSONL, one record for every syntactically valid harness invocation after argument parsing; pre-gateway adapter/input failures use a redacted harness-failure audit record. The sink uses `O_APPEND|O_NOFOLLOW`, validates a regular-file descriptor, writes the full record, and fsyncs before successful process completion.

Audit contains metadata/digests only. It does not store request bytes, file payload, credential values, environment dumps, Authorization headers or secret material.

Future deployment must independently enforce directory ownership/permissions and retention. This harness does not claim filesystem immutable/append-only attributes beyond its own O_APPEND write behavior.

## Environment / credentials

Local VERIFY execution requires no credentials. The harness reads no credential files and contains no credential lookup. Future supervisor environment should be minimal, e.g. `PATH=/usr/bin:/bin`, `LC_ALL=C`, with no inherited secret-bearing variables. The verified r0.2 adapter itself supplies a minimal environment to any allowlisted Git subprocess.

## Boundary

No deployment, host/SSH mutation, users/groups/ACL/package/service/firewall changes, credential access/provisioning, listener exposure, WRITE enablement or production-root mutation is performed here.
