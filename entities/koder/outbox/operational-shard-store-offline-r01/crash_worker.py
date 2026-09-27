#!/usr/bin/env python3
"""Only called by the synthetic crash-injection test subprocess."""
import sys
from pathlib import Path
from offline_store import OfflineStore, parse, sha
from test_offline_store import NS, admission

sandbox, root, kind, stage, op, raw_hex, payload_hex = sys.argv[1:8]
raw, payload = bytes.fromhex(raw_hex), bytes.fromhex(payload_hex)
store = OfflineStore(Path(root), Path(sandbox))
if kind == "put":
    store.put(raw, payload, op, admission(), injection=stage)
elif kind == "cas":
    store.cas(NS, None, sha(raw), op, admission(), injection=stage)
elif kind == "cas-successor":
    expected = parse(bytes.fromhex(sys.argv[8]))
    store.cas(NS, expected, sha(raw), op, admission(2, "writer-b"), injection=stage)
else:
    raise SystemExit("BAD_TEST_OPERATION")
raise SystemExit("FAULT_NOT_REACHED")
