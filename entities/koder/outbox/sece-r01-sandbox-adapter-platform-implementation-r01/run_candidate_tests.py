from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import run_all_offline_tests
import run_sandbox_adapter_tests

def main() -> int:
    stages=[('R04_BASELINE',run_all_offline_tests.main),('SANDBOX_CANDIDATE',run_sandbox_adapter_tests.main)]
    for name,fn in stages:
        rc=int(fn()); print(f'{name}_EXIT={rc}')
        if rc!=0: return rc
    print('ALL_CANDIDATE_OFFLINE_GATES_PASS=YES')
    return 0
if __name__=='__main__': raise SystemExit(main())
