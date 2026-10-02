from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sece_simulator import Simulator

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/"reviewed-inputs"

def main() -> int:
    fixture_schema=json.loads((INPUT/"FIXTURE-SCHEMA.json").read_text())
    trace_schema=json.loads((INPUT/"TRACE-SCHEMA.json").read_text())
    catalog=json.loads((INPUT/"FIXTURE-CATALOG.json").read_text())
    sim=Simulator(fixture_schema, trace_schema)
    fixtures=sim.fixture_loader.load_catalog(catalog)
    failed=0
    for fixture in fixtures:
        result=sim.run_fixture(fixture)
        print(json.dumps({
            "fixture_id":result["fixture_id"],
            "family":result["family"],
            "oracle_state":result["oracle_state"],
            "trace_id":result["trace_id"],
            "mismatches":result["mismatches"],
        }, ensure_ascii=False, sort_keys=True))
        failed += result["oracle_state"] != "ORACLE_PASS"
    return 0 if failed == 0 else 1

if __name__=="__main__":
    raise SystemExit(main())
