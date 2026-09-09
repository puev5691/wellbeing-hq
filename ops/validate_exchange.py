#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DISPATCH_DIR = ROOT / "routes" / "dispatch"
REQUIRED = {
    "sender", "recipient", "artifact", "artifact_commit", "purpose",
    "required_action", "expected_result", "failure_mode",
    "inbox_pointer", "registry_record", "status"
}

FIELD_RE = re.compile(r"^([a-z_]+):\s*(.*?)\s*$")


def parse_gate(path: Path):
    fields = {}
    enabled = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line == "exchange_gate: v1":
            enabled = True
            continue
        m = FIELD_RE.match(line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip('`')
    return enabled, fields


def fail(msg, errors):
    errors.append(msg)


def check_dispatch(path: Path, errors):
    enabled, f = parse_gate(path)
    if not enabled:
        return

    missing = sorted(k for k in REQUIRED if not f.get(k))
    if missing:
        fail(f"{path.relative_to(ROOT)}: missing fields {', '.join(missing)}", errors)
        return

    sender = f["sender"]
    recipient = f["recipient"]
    artifact = ROOT / f["artifact"]
    inbox_pointer = ROOT / f["inbox_pointer"]
    registry = ROOT / f["registry_record"]

    expected_prefix = f"entities/{sender}/outbox/"
    if not f["artifact"].startswith(expected_prefix):
        fail(f"{path.name}: artifact must be under {expected_prefix}", errors)
    if not artifact.is_file():
        fail(f"{path.name}: artifact not found: {f['artifact']}", errors)

    inbox_prefix = f"entities/{recipient}/inbox/"
    if not f["inbox_pointer"].startswith(inbox_prefix):
        fail(f"{path.name}: inbox_pointer must be under {inbox_prefix}", errors)
    if not inbox_pointer.is_file():
        fail(f"{path.name}: inbox pointer not found: {f['inbox_pointer']}", errors)

    reg_expected = f"registry/by-sender/{sender}.jsonl"
    if f["registry_record"] != reg_expected:
        fail(f"{path.name}: registry_record must be {reg_expected}", errors)
    if not registry.is_file():
        fail(f"{path.name}: registry missing: {reg_expected}", errors)
    else:
        found = False
        for n, line in enumerate(registry.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception as e:
                fail(f"{reg_expected}:{n}: invalid JSON: {e}", errors)
                continue
            if rec.get("dispatch") == str(path.relative_to(ROOT)):
                found = True
        if not found:
            fail(f"{path.name}: no sender-registry record points to this dispatch", errors)

    if f["status"] in {"received", "accepted", "rejected"}:
        receipt = f.get("receipt")
        if not receipt:
            fail(f"{path.name}: status={f['status']} requires receipt field", errors)
        elif not (ROOT / receipt).is_file():
            fail(f"{path.name}: receipt not found: {receipt}", errors)


def main():
    errors = []
    checked = 0
    if DISPATCH_DIR.exists():
        for path in sorted(DISPATCH_DIR.glob("*.md")):
            enabled, _ = parse_gate(path)
            if enabled:
                checked += 1
                check_dispatch(path, errors)

    if errors:
        print("EXCHANGE_GATE=FAIL")
        for e in errors:
            print(f"- {e}")
        return 1

    print(f"EXCHANGE_GATE=PASS checked={checked}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
