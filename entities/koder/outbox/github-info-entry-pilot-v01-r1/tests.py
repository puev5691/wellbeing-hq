import json, subprocess, sys
from pathlib import Path
base=Path(__file__).resolve().parent
cases={
 "positive.json":0,
 "allowed_conditions_satisfied.json":0,
 "allowed_conditions_unsatisfied.json":2,
 "candidate_unknown.json":2,
 "blocked.json":2,
 "superseded.json":2,
 "secret_like.json":2,
}
failed=[]
for name,expected in cases.items():
    cp=subprocess.run([sys.executable,str(base/"validator.py"),str(base/"fixtures"/name)],capture_output=True,text=True)
    result=json.loads(cp.stdout)
    if cp.returncode!=expected: failed.append((name,cp.returncode,expected,result))
    should_ready=(expected==0)
    if result.get("public_ready") is not should_ready: failed.append((name,"public_ready",result))
    if name=="allowed_conditions_unsatisfied.json" and "legal_conditions_not_satisfied" not in result.get("errors",[]):
        failed.append((name,"missing legal_conditions_not_satisfied",result))
print(f"{len(cases)-len(failed)}/{len(cases)} cases PASS")
if failed:
    print(failed); raise SystemExit(1)
