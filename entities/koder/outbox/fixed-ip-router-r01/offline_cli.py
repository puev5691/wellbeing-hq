"""Offline fixture interface; this CLI has no network option."""

import argparse
import json
import sys
from pathlib import Path

from router import AdmissionError, offline_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline fixed-IP route plan from synthetic observations")
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--admission", required=True, type=Path)
    parser.add_argument("--observations", required=True, type=Path)
    parser.add_argument("--manual-node", choices=("burzh", "mazhor", "erefia"))
    args = parser.parse_args()
    try:
        result = offline_plan(args.profile, args.admission, args.observations, args.manual_node)
    except (AdmissionError, ValueError, OSError) as exc:
        # Closed error class only. Never echo paths or exception text.
        print(json.dumps({"outcome": "BLOCKED", "reason": type(exc).__name__}), file=sys.stdout)
        return 2
    print(json.dumps(result, sort_keys=True), file=sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
