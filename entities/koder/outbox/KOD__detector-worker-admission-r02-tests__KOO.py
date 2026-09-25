#!/usr/bin/env python3
"""Deterministic offline admission tests; supervisor trust is synthetic only."""
import copy, hashlib, json, os
from pathlib import Path
import subprocess, sys, tempfile

WORKER=Path(__file__).with_name("KOD__activation-worker-v03-isolated__KOO.py")
ART="fixtures/artifact.md"; DSP="routes/dispatch/synthetic.md"; INB="entities/synthetic/inbox/synthetic.md"

def j(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sh(*args,cwd):
    p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,check=True,env={"PATH":os.environ["PATH"],"GIT_AUTHOR_DATE":"2000-01-01T00:00:00+0000","GIT_COMMITTER_DATE":"2000-01-01T00:00:00+0000"})
    return p.stdout.strip()
def put(r,path,data):
    p=r/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data)
def commit(r,name):
    sh("git","add",".",cwd=r);sh("git","commit","-qm",name,cwd=r);return sh("git","rev-parse","HEAD",cwd=r)
def ref(r,commit,path): return {"commit":commit,"path":path,"blob":sh("git","rev-parse",f"{commit}:{path}",cwd=r)}
def digest(event,locator):
    keys=("event_id","source_commit","inbox_path","inbox_blob","recipient")
    v={k:event[k] for k in keys}
    v.update({k:locator[k] for k in ("artifact_path","artifact_commit","artifact_blob","dispatch_path","dispatch_commit")})
    return hashlib.sha256(j(v).encode()).hexdigest()
def setup(base):
    r=base/"mirror";r.mkdir();sh("git","init","-q",str(r),cwd=base)
    sh("git","config","user.name","Synthetic Fixture",cwd=r);sh("git","config","user.email","synthetic@example.invalid",cwd=r)
    put(r,ART,"synthetic task\n"); a=commit(r,"artifact")
    loc=dict(artifact_path=ART,artifact_commit=a,artifact_blob=ref(r,a,ART)["blob"],artifact_sha256=hashlib.sha256((r/ART).read_bytes()).hexdigest(),recipient="synthetic",sender="synthetic",exchange_gate="v1",dispatch_path=DSP,dispatch_commit="",inbox_path=INB)
    put(r,DSP,f"sender: synthetic\nrecipient: synthetic\nexchange_gate: v1\nartifact_path: `{ART}`\ninbox_path: `{INB}`\n");loc["dispatch_commit"]=commit(r,"dispatch")
    put(r,INB,"\n".join(f"{k}: {loc[k]}" for k in ("recipient","artifact_path","artifact_commit","artifact_blob","dispatch_path","dispatch_commit"))+"\n")
    put(r,"fixtures/authority.json",j(dict(status="AUTHORIZED",task_id="task-001",recipient="synthetic",source_set_id="operator-approved-fixture-set",superseded=False)))
    rec=dict(entity="synthetic",state="verified",current_writer_state="known_nonwriter",recovery_identity="synthetic-recovery-v1")
    put(r,"fixtures/recovery.json",j(rec))
    put(r,"fixtures/writer.json",j(dict(entity="synthetic",status="CURRENT_WRITER_ESTABLISHED",writer_id="writer-001",superseded=False)))
    for n in range(1,7):put(r,f"fixtures/source{n}.md",f"synthetic trusted source {n}\n")
    e=commit(r,"event-and-admission")
    event=dict(event_id="evt-001",source_commit=e,inbox_path=INB,inbox_blob=ref(r,e,INB)["blob"],recipient="synthetic")
    event["event_digest"]=digest(event,loc)
    adm=dict(task_id="task-001",source_set_id="operator-approved-fixture-set",recovery_identity=rec["recovery_identity"],authority=ref(r,e,"fixtures/authority.json"),recovery=ref(r,e,"fixtures/recovery.json"),writer=ref(r,e,"fixtures/writer.json"),sources=[ref(r,e,f"fixtures/source{n}.md") for n in range(1,7)])
    trust=dict(scope="ISOLATED_SYNTHETIC_R02",admission_version="r02",task_id="task-001",source_set_id=adm["source_set_id"],writer_id="writer-001",authority=adm["authority"],recovery=adm["recovery"],writer=adm["writer"],sources=adm["sources"])
    return r,loc,event,adm,trust,rec
def case(base,r,loc,event,adm,trust,rec,name,state=None,handler="ok",provider=None):
    d=base/name;d.mkdir();state=state or d/"state"
    for fname,obj in (("locator",loc),("event",event),("admission",adm),("trust",trust),("recovery",rec)):(d/(fname+".json")).write_text(j(obj))
    (d/"artifact.md").write_bytes((r/ART).read_bytes())
    code='import os,sys,pathlib; pathlib.Path(os.environ["WB_RESULT_PATH"]).write_text("synthetic result\\n") if sys.argv[1]=="ok" else None; sys.exit(0 if sys.argv[1]=="ok" else 9)'
    args=[sys.executable,str(WORKER),"--locator",str(d/"locator.json"),"--artifact",str(d/"artifact.md"),"--recovery",str(d/"recovery.json"),"--event",str(d/"event.json"),"--admission",str(d/"admission.json"),"--admission-trust",str(d/"trust.json"),"--git-repo",str(provider or r),"--state-dir",str(state),"--evidence",str(d/"evidence.json"),"--result",str(d/"result.txt"),"--handler",sys.executable,"-c",code,handler]
    p=subprocess.run(args,capture_output=True,text=True,env={"PATH":os.environ["PATH"],"PYTHONDONTWRITEBYTECODE":"1"})
    ev=json.loads((d/"evidence.json").read_text())
    return {"exit":p.returncode,"state":ev["state"],"reason":ev.get("reason"),"handler_exit":ev.get("handler_exit"),"synthetic_result":(d/"result.txt").exists(),"real_entity_observed":False}
def main():
    with tempfile.TemporaryDirectory(prefix="kod-admission-r02-") as tmp:
        b=Path(tmp);r,L,E,A,T,R=setup(b);results={}
        def add(name,expected,l=None,e=None,a=None,t=None,rec=None,state=None,handler="ok",provider=None):
            got=case(b,r,l or L,e or E,a or A,t or T,rec or R,name,state,handler,provider)
            match=((got["exit"],got["reason"],got["state"]) == expected and got["synthetic_result"] == (expected[0] == 0) and got["real_entity_observed"] is False)
            results[name]={"expected":{"exit":expected[0],"reason":expected[1],"state":expected[2]},"actual":got,"verdict":"PASS" if match else "FAIL","executed":True}
        good=(0,None,"result_dispatched")
        add("01_exact_event",good)
        add("02_blob_mismatch",(21,"artifact_blob_mismatch","activation_failed"),l={**L,"artifact_blob":"0"*40})
        add("02_commit_mismatch",(21,"artifact_commit_not_found","activation_failed"),l={**L,"artifact_commit":"0"*40})
        add("03_wrong_recipient",(21,"dispatch_recipient_mismatch","activation_failed"),l={**L,"recipient":"wrong"})
        add("03_wrong_dispatch",(21,"dispatch_commit_not_found","activation_failed"),l={**L,"dispatch_commit":"0"*40})
        shared=b/"dedupe"
        add("04_initial",good,state=shared)
        add("04_same_id_digest",(23,"duplicate_event_same_digest","activation_failed"),state=shared)
        unknown=b/"unknown";unknown.mkdir()
        key=hashlib.sha256(("task-001|"+E["event_id"]).encode()).hexdigest()
        (unknown/("event-"+key+".json")).write_text(j({"event_id":E["event_id"],"event_digest":E["event_digest"],"state":"reserved_unknown_until_reconciled"})+"\n")
        add("04_interrupted_reservation_unknown",(27,"event_state_unknown_requires_reconcile","activation_failed"),state=unknown)
        put(r,INB,(r/INB).read_text()+"extra: still synthetic\n");e2=commit(r,"changed-inbox-event")
        changed={**E,"source_commit":e2,"inbox_blob":ref(r,e2,INB)["blob"]};changed["event_digest"]=digest(changed,L)
        add("05_same_id_changed_valid_digest",(24,"event_id_digest_conflict","activation_failed"),e=changed,state=shared)
        add("06_missing_authority",(25,"authority_not_trusted","activation_failed"),a={**A,"authority":None})
        add("06_wrong_authority",(25,"authority_not_trusted","activation_failed"),a={**A,"authority":{**A["authority"],"blob":"0"*40}})
        add("07_missing_sources",(25,"approved_source_set_missing_or_untrusted","activation_failed"),a={**A,"sources":[]})
        src=copy.deepcopy(A);src["sources"][0]["blob"]="0"*40
        add("07_wrong_source",(25,"approved_source_set_missing_or_untrusted","activation_failed"),a=src)
        add("07_missing_recovery",(22,"recovery_missing_fields:recovery_identity","activation_failed"),rec={"entity":"synthetic","state":"verified","current_writer_state":"known_nonwriter"})
        add("07_missing_writer",(25,"writer_not_trusted","activation_failed"),a={**A,"writer":None})
        add("08_unavailable_provider",(21,"provider_unavailable_or_unreadable","activation_failed"),provider=b/"unavailable")
        add("09_handler_failure",(30,None,"processing_failed"),handler="fail")
        add("10_local_marker_no_entity",good)
        altered={**E,"event_digest":"0"*64}
        add("event_digest_tamper",(25,"event_digest_mismatch","activation_failed"),e=altered)
        wrong_commit={**E,"source_commit":"0"*40};wrong_commit["event_digest"]=digest(wrong_commit,L)
        add("event_commit_mismatch",(25,"event_commit_missing","activation_failed"),e=wrong_commit)
        wrong_blob={**E,"inbox_blob":"0"*40};wrong_blob["event_digest"]=digest(wrong_blob,L)
        add("event_inbox_blob_mismatch",(25,"event_inbox_blob_mismatch","activation_failed"),e=wrong_blob)
        put(r,INB,(r/INB).read_text().replace(f"artifact_path: {ART}","artifact_path: fixtures/wrong.md"));e3=commit(r,"mismatched-inbox-binding")
        bad_inbox={**E,"source_commit":e3,"inbox_blob":ref(r,e3,INB)["blob"]};bad_inbox["event_digest"]=digest(bad_inbox,L)
        add("event_inbox_binding_mismatch",(25,"event_inbox_binding_mismatch:artifact_path","activation_failed"),e=bad_inbox)
        add("missing_trusted_profile",(25,"trusted_profile_missing_or_invalid","activation_failed"),t={**T,"scope":"UNTRUSTED"})
        put(r,"fixtures/authority.json",j(dict(status="AUTHORIZED",task_id="task-001",recipient="synthetic",source_set_id="operator-approved-fixture-set",superseded=True)))
        e4=commit(r,"superseded-authority");sup=ref(r,e4,"fixtures/authority.json")
        add("superseded_authority",(25,"authority_not_current_or_valid","activation_failed"),a={**A,"authority":sup},t={**T,"authority":sup})
        put(r,"fixtures/writer.json",j(dict(entity="synthetic",status="CURRENT_WRITER_ESTABLISHED",writer_id="writer-001",superseded=True)))
        e5=commit(r,"superseded-writer");sw=ref(r,e5,"fixtures/writer.json")
        add("superseded_writer",(25,"writer_not_current_or_valid","activation_failed"),a={**A,"writer":sw},t={**T,"writer":sw})
        output={"worker_baseline_blob":"c680878806fd2fb6d20df8b6e8938d3f3ead5053","scope":"synthetic_offline_only","cases":results,"passed":sum(x["verdict"]=="PASS" for x in results.values()),"total":len(results)}
        print(json.dumps(output,sort_keys=True,indent=2,ensure_ascii=False))
        if output["passed"] != output["total"]:sys.exit(1)
if __name__=="__main__":main()
