#!/usr/bin/env python3
import argparse, hashlib, json, sys
from pathlib import Path

REQUIRED_FIELDS = (
    "experience_id","task_or_episode","context_refs","trigger_or_symptom",
    "initial_hypothesis","failed_attempts","observed_result","working_resolution",
    "evidence_refs","lesson","next_time_behavior","prohibited_repeat",
    "applicability_boundary","freshness","confidence","behavior_test_candidate",
    "supersedes",
)

def sha256(b): return hashlib.sha256(b).hexdigest()

def load(path):
    raw=Path(path).read_bytes()
    cards=[]; errors=[]
    for lineno,line in enumerate(raw.splitlines(),1):
        if not line.strip(): continue
        try: obj=json.loads(line)
        except Exception as e:
            errors.append({"line":lineno,"error":"invalid_json"})
            continue
        if not isinstance(obj,dict):
            errors.append({"line":lineno,"error":"not_json_object"})
            continue
        missing=[k for k in REQUIRED_FIELDS if k not in obj]
        if missing: errors.append({"line":lineno,"error":"missing_required_fields","fields":missing})
        cards.append(obj)
    ids=[c.get("experience_id") for c in cards if "experience_id" in c]
    dup=sorted({x for x in ids if ids.count(x)>1})
    if dup: errors.append({"error":"duplicate_experience_id","ids":dup})
    return raw,cards,errors

def canonical(obj):
    return json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":"))

def compare(a,b):
    ra,ca,ea=load(a); rb,cb,eb=load(b)
    out={"left":{"sha256":sha256(ra),"cards":len(ca),"errors":ea},
         "right":{"sha256":sha256(rb),"cards":len(cb),"errors":eb}}
    if ra==rb and not ea and not eb:
        out.update(classification="byte_exact",diff=[]); return out,0
    if ea or eb:
        out.update(classification="structural_mismatch",diff=[]); return out,1
    ma={c["experience_id"]:c for c in ca}; mb={c["experience_id"]:c for c in cb}
    ida, idb=set(ma),set(mb)
    diff=[]
    for x in sorted(ida-idb): diff.append({"experience_id":x,"kind":"missing_right"})
    for x in sorted(idb-ida): diff.append({"experience_id":x,"kind":"missing_left"})
    for x in sorted(ida&idb):
        A,B=ma[x],mb[x]
        fields=sorted(set(A)|set(B))
        changes=[]
        for f in fields:
            if A.get(f)!=B.get(f):
                changes.append({"field":f,"left":A.get(f),"right":B.get(f)})
        if changes: diff.append({"experience_id":x,"kind":"field_mismatch","changes":changes})
    if not diff:
        out.update(classification="semantic_equal",diff=[]); return out,0
    if ida!=idb or len(ca)!=len(cb): cls="structural_mismatch"
    else: cls="content_mismatch"
    out.update(classification=cls,diff=diff); return out,1

def main(argv=None):
    p=argparse.ArgumentParser(description="Continuity v2 deterministic JSONL verifier")
    p.add_argument("left"); p.add_argument("right")
    args=p.parse_args(argv)
    try: out,rc=compare(args.left,args.right)
    except OSError:
        print(json.dumps({"classification":"structural_mismatch","error":"input_unreadable"},sort_keys=True)); return 2
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(",",":")))
    return rc

if __name__=="__main__": raise SystemExit(main())
