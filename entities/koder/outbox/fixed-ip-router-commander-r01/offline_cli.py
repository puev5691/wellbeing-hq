"""Synthetic/local selection CLI. No Remote Desktop Commander invocation."""

import argparse
import json
from pathlib import Path

from integration import offline_fixture_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline operator-assisted Commander selection fixture")
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--mapping-sha256", required=True)
    parser.add_argument("--fixture", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = offline_fixture_plan(args.mapping, args.mapping_sha256, args.fixture)
    except (ValueError, OSError, TypeError):
        print(json.dumps({"outcome": "CONTROL_PATH_EXECUTION_BLOCKED", "reason": "INVALID_OFFLINE_INPUT"}))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
