"""Common local checks; candidate source must be reviewed before import."""
import ast
import signal
from types import SimpleNamespace
from source_policy import review, PURE
import json
from pathlib import Path
import sys
import time

def _check(path):
    source=Path(path).read_text()
    tree=ast.parse(source)
    review(tree)
    # Only statically reviewed function definition; no candidate top-level effects.
    ns={'__builtins__':dict(PURE)}
    exec(compile(tree,str(path),'exec'),ns,ns)
    mod=SimpleNamespace(runs=ns['runs'])
    cases=json.loads(Path(__file__).with_name('task.json').read_text())['cases'];rows=[]
    for value,expected in cases:
        original=value;result=mod.runs(value)
        exact=result==[tuple(x) for x in expected]
        valid=type(result) is list and all(type(x) is tuple and len(x)==2 and type(x[0]) is str and len(x[0])==1 and type(x[1]) is int and 1<=x[1]<=3 for x in result)
        roundtrip=valid and ''.join(c*n for c,n in result)==value
        greedy=valid and all(result[i-1][0]!=result[i][0] or result[i-1][1]==3 for i in range(1,len(result)))
        rows.append(dict(input=value,result=result,exact=exact,valid=valid,roundtrip=roundtrip,greedy=greedy,input_unchanged=original==value))
    return {'cases':rows,'passed':sum(all(row[k] for k in ('exact','valid','roundtrip','greedy','input_unchanged')) for row in rows),'total':len(rows),'source_policy':'STATIC_REVIEW_PURE_BUILTINS_LOCAL_LIST_ONLY'}

def check(path):
    # Bound CPU time for reviewed loops; this is not a general hostile-code sandbox.
    if signal.getitimer(signal.ITIMER_REAL)[0]:
        raise RuntimeError('BLOCKED_EXISTING_TIMER')
    def expired(signum,frame):raise TimeoutError('BLOCKED_CHECK_DEADLINE')
    old=signal.signal(signal.SIGALRM,expired)
    signal.setitimer(signal.ITIMER_REAL,2)
    try:return _check(path)
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        signal.signal(signal.SIGALRM,old)

if __name__=='__main__':
    start=time.monotonic_ns();out=check(sys.argv[1]);out['check_duration_ns']=time.monotonic_ns()-start
    print(json.dumps(out,ensure_ascii=False,indent=2))
