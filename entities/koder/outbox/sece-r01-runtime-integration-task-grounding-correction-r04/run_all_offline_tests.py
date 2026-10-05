from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import fixture_runner
import package_gate_tests
import run_offline_tests
import run_runtime_integration_tests


def main() -> int:
    steps = [
        ("PACKAGE_GATE", package_gate_tests.main),
        ("BASELINE_OFFLINE", run_offline_tests.main),
        ("BASELINE_FIXTURES", fixture_runner.main),
        ("RUNTIME_INTEGRATION", run_runtime_integration_tests.main),
    ]
    for name, fn in steps:
        rc = int(fn())
        print(f"{name}_EXIT={rc}")
        if rc != 0:
            return rc
    print("ALL_OFFLINE_INTEGRATION_GATES_PASS=YES")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
