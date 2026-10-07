from __future__ import annotations
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import sandbox_adapter_tests


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromModule(sandbox_adapter_tests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    passed = result.testsRun - len(result.failures) - len(result.errors)
    print(f"SANDBOX_ADAPTER_TESTS_PASS={passed}/{result.testsRun}")
    print("REAL_SANDBOX_EFFECT_EXECUTION=NOT_EXECUTED")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
