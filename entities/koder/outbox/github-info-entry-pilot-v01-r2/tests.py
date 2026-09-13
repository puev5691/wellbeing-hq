import json, subprocess, sys
from pathlib import Path
base=Path(__file__).resolve().parent
cases={
 "positive.json":(0,None),
 "allowed_conditions_satisfied.json":(0,None),
 "allowed_conditions_unsatisfied.json":(2,"legal_conditions_not_satisfied"),
 "candidate_unknown.json":(2,None),
 "blocked.json":(2,None),
 "superseded.json":(2,None),
 "secret_like.json":(2,None),
 "secret_dependency_string_true.json":(2,"invalid_type:secret_dependency"),
 "legal_conditions_string_true.json":(2,"invalid_type:public_legal_conditions_satisfied"),
 "superseded_by_number.json":(2,"invalid_type:superseded_by"),
 "id_number.json":(2,"invalid_type:id"),
 "unknown_security_key.json":(2,"unknown_key:security_override"),
}
failed=[]
for name,(expected,required_error) in cases.items():
    cp=subprocess.run([sys.executable,str(base/"validator.py"),str(base/"fixtures"/name)],capture_output=True,text=True)
    result=json.loads(cp.stdout)
    if cp.returncode!=expected: failed.append((name,"returncode",cp.returncode,expected,result))
    should_ready=(expected==0)
    if result.get("public_ready") is not should_ready: failed.append((name,"public_ready",result))
    if required_error and required_error not in result.get("errors",[]):
        failed.append((name,"missing_error",required_error,result))
print(f"{len(cases)-len(failed)}/{len(cases)} cases PASS")
if failed:
    print(json.dumps(failed,indent=2,ensure_ascii=False)); raise SystemExit(1)
