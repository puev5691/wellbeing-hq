"""Common local checks; candidate source must be reviewed before import."""
import ast
import importlib.util
import json
from pathlib import Path
import sys
import time

def check(path):
    source=Path(path).read_text()
    tree=ast.parse(source)
    forbidden=(ast.Import,ast.ImportFrom,ast.Global,ast.Nonlocal)
    assert not any(isinstance(n,forbidden) for n in ast.walk(tree))
    calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call)]
    assert all(isinstance(n.func,ast.Attribute) and n.func.attr=='append' for n in calls)
    spec=importlib.util.spec_from_file_location('candidate',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    cases=json.loads(Path(__file__).with_name('task.json').read_text())['cases'];rows=[]
    for value,expected in cases:
        original=value;result=mod.runs(value)
        exact=result==[tuple(x) for x in expected]
        valid=type(result) is list and all(type(x) is tuple and len(x)==2 and type(x[0]) is str and len(x[0])==1 and type(x[1]) is int and 1<=x[1]<=3 for x in result)
        roundtrip=valid and ''.join(c*n for c,n in result)==value
        greedy=valid and all(result[i-1][0]!=result[i][0] or result[i-1][1]==3 for i in range(1,len(result)))
        rows.append(dict(input=value,result=result,exact=exact,valid=valid,roundtrip=roundtrip,greedy=greedy,input_unchanged=original==value))
    return {'cases':rows,'passed':sum(all(row[k] for k in ('exact','valid','roundtrip','greedy','input_unchanged')) for row in rows),'total':len(rows),'source_policy':'reviewed_local_no_imports_no_external_calls'}

if __name__=='__main__':
    start=time.monotonic_ns();out=check(sys.argv[1]);out['check_duration_ns']=time.monotonic_ns()-start
    print(json.dumps(out,ensure_ascii=False,indent=2))
