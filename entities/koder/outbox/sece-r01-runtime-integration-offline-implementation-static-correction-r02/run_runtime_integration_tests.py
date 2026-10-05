from __future__ import annotations
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import runtime_integration_tests


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromModule(runtime_integration_tests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"RUNTIME_INTEGRATION_TESTS_PASS={result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun}")
    print("NO_LIVE_EFFECT_TEST_BOUNDARY=YES")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
