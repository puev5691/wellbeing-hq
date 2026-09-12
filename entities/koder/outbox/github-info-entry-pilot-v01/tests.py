import json, subprocess, sys
from pathlib import Path

base = Path(__file__).resolve().parent
cases = {
    "positive.json": 0,
    "candidate_unknown.json": 2,
    "blocked.json": 2,
    "superseded.json": 2,
    "secret_like.json": 2,
}
failed = []
for name, expected in cases.items():
    cp = subprocess.run([sys.executable, str(base/"validator.py"), str(base/"fixtures"/name)], capture_output=True, text=True)
    try:
        result = json.loads(cp.stdout)
    except Exception:
        failed.append((name, "invalid-json-output", cp.stdout, cp.stderr))
        continue
    if cp.returncode != expected:
        failed.append((name, f"exit {cp.returncode} != {expected}", result))
    if name != "positive.json" and result.get("public_ready") is not False:
        failed.append((name, "negative fixture became public_ready", result))
    if name == "positive.json" and result.get("public_ready") is not True:
        failed.append((name, "positive fixture did not pass", result))
print(f"{len(cases)-len(failed)}/{len(cases)} cases PASS")
if failed:
    print(failed)
    raise SystemExit(1)
