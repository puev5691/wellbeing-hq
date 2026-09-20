#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, sys

INTEGRATION_SHA256="6a81a0c08ffd961e3b22d2d1de4948ebce780555cfe40b8c669e96e47cb07751"
STORE_SHA256="cd01972b7045d4f84583fb5470d4c0012e09c12b954ea65221107eaa01385d7e"
WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"
SECRETREF="secretref:openai:wellbeing-entity-boosters-restricted"
OBJECT="openai-wellbeing-entity-boosters-restricted"
TASK_COMMIT="b988066e0e018627cc24b95f409f3ccd0a416990"
TASK_BLOB="691af722274bc51f87d5eeda6e7054d21ee3c9c3"
WRITER_BLOB="ba08fe21d0b01cf1f7f5f3e181cd4af4cdfc5391"
MODEL="gpt-5.6-luna"
PAYLOAD="Synthetic bounded request."
ENDPOINT="https://api.openai.com/v1/responses"

class E(RuntimeError): pass
def need(v,c):
    if not v: raise E(c)
def canon(v): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)
def digest(v): return hashlib.sha256(canon(v).encode()).hexdigest()

def load_pinned(path,expected,name):
    raw=Path(path).read_bytes()
    need(hashlib.sha256(raw).hexdigest()==expected,"BLOCKED_DEPENDENCY_IDENTITY")
    s=importlib.util.spec_from_file_location(name,path)
    need(s is not None and s.loader is not None,"BLOCKED_DEPENDENCY_IMPORT")
    m=importlib.util.module_from_spec(s); sys.modules[name]=m
    try: s.loader.exec_module(m)
    except Exception: raise E("BLOCKED_DEPENDENCY_IMPORT") from None
    return m

def read_invocation(path):
    o=json.loads(Path(path).read_text())
    exact={"task_commit":TASK_COMMIT,"task_blob":TASK_BLOB,"writer_blob":WRITER_BLOB,
           "provider":"openai","model":MODEL,"privacy_class":"synthetic_only","data_class":"D0_SYNTHETIC",
           "tools":[],"credential_ref":SECRETREF,"calls":1,"retries":0,"fallback":"none",
           "max_output_tokens":64,"max_response_bytes":16384,"timeout_seconds":30,
           "payload":PAYLOAD,"project_acceptance":"NOT_GRANTED","project_state_mutation":False}
    for k,v in exact.items(): need(o.get(k)==v,"BLOCKED_SCOPE_"+k.upper())
    need(o.get("mode") in ("SENTINEL","LIVE"),"BLOCKED_MODE")
    need(isinstance(o.get("authority_id"),str) and o["authority_id"],"BLOCKED_AUTHORITY_ID")
    return o

def make_plan(worker,o):
    body={"model":MODEL,"input":PAYLOAD,"max_output_tokens":64,"store":False,
          "tools":[],"tool_choice":"none","parallel_tool_calls":False}
    native={"method":"POST","url":ENDPOINT,"headers":{"content-type":"application/json"},"body":body}
    req=digest({"task_commit":TASK_COMMIT,"task_blob":TASK_BLOB,"writer_blob":WRITER_BLOB,"payload":PAYLOAD})
    ps=digest(native); auth=digest({"authority_id":o["authority_id"],"scope":o})
    requester=digest({"entity":"KOD","task_commit":TASK_COMMIT,"writer_blob":WRITER_BLOB})
    return worker.WorkerPlan(req,ps,auth,requester,"openai",MODEL,canon(native),
        worker.SecretRef("openai",SECRETREF),worker.WorkerPolicy(30.0,16384,1,0),2**53-2)

class SystemdCredentialResolver:
    def __init__(self,worker): self.worker=worker
    def resolve(self,ref):
        need(ref.provider=="openai" and ref.locator==SECRETREF,"BLOCKED_SECRETREF_MISMATCH")
        d=os.environ.get("CREDENTIALS_DIRECTORY"); need(bool(d),"BLOCKED_CREDENTIAL_DIRECTORY")
        p=Path(d)/OBJECT; need(p.is_file(),"BLOCKED_CREDENTIAL_OBJECT")
        value=p.read_text()
        need(bool(value) and "\n" not in value and "\r" not in value,"BLOCKED_CREDENTIAL_VALUE")
        return self.worker.ResolvedSecret("openai",value)

def execute(*,invocation_path,worker_path,integration_path,store_path,ledger_path,result_dir,
            resolver=None,client=None,now_tick=1):
    o=read_invocation(invocation_path)
    worker=load_pinned(worker_path,WORKER_SHA256,"_booster_integ_worker")
    integ=load_pinned(integration_path,INTEGRATION_SHA256,"_booster_result_v2_integration")
    store=load_pinned(store_path,STORE_SHA256,"_booster_result_v2_store")
    if o["mode"]=="SENTINEL":
        d=os.environ.get("CREDENTIALS_DIRECTORY")
        need(bool(d) and (Path(d)/OBJECT).is_file(),"BLOCKED_CREDENTIAL_OBJECT")
        return {"schema":"wb.openai.booster.result_v2_integration.sentinel.v1","status":"READY",
                "credential_loaded_for_child":True,"credential_value_read":False,"provider_calls":0,
                "result_schema":store.SCHEMA,"result_dir":str(result_dir),"project_acceptance":"NOT_GRANTED"}
    plan=make_plan(worker,o)
    resolver=resolver or SystemdCredentialResolver(worker)
    client=client or worker.BoundedUrllibClient()
    identity=integ.ResultIdentity(TASK_COMMIT,TASK_BLOB,WRITER_BLOB)
    rw=integ.ReviewableLiveWorker(worker_path=Path(worker_path),store_path=Path(store_path),
        ledger_path=Path(ledger_path),result_dir=Path(result_dir),resolver=resolver,client=client)
    try:
        out=rw.invoke_once_and_persist(plan,identity,now_tick=now_tick)
    except integ.IntegrationError as exc:
        raise E(str(exc)) from None
    need(out.get("technical_status")=="PASS_PERSISTED_REVIEWABLE_RESULT","BLOCKED_RESULT_NOT_PERSISTED")
    result_path=Path(out["result_path"])
    persisted=store.read_and_validate(result_path,attempt_key=out["attempt_key"],
        request_sha256=plan.request_sha256,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,
        writer_blob=WRITER_BLOB,plan_sha256=plan.plan_sha256,authority_sha256=plan.authority_sha256,
        provider="openai",model=MODEL)
    need(persisted["schema"]=="wb.openai.booster.review_result.v2","BLOCKED_RESULT_SCHEMA")
    return {"schema":"wb.openai.booster.result_v2_integration.result.v1",
            "status":"PASS_TECHNICAL_RESULT_AFTER_DURABLE_V2_READBACK",
            "attempt_key":out["attempt_key"],"result_path":str(result_path),
            "result_schema":persisted["schema"],"provider":"openai","model":MODEL,
            "provider_calls":1,"retries":0,"fallback":"none","requester_review_required":True,
            "project_acceptance":"NOT_GRANTED","project_state_mutation":False,
            "provider_writer_authority":False,"gateway_writer_authority":False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--worker",required=True); ap.add_argument("--integration",required=True)
    ap.add_argument("--store",required=True); ap.add_argument("--invocation",required=True)
    ap.add_argument("--ledger",required=True); ap.add_argument("--result-dir",required=True)
    ns=ap.parse_args()
    try:
        out=execute(invocation_path=ns.invocation,worker_path=ns.worker,integration_path=ns.integration,
            store_path=ns.store,ledger_path=ns.ledger,result_dir=ns.result_dir)
        print(canon(out)); return 0
    except Exception as exc:
        code=str(exc) if isinstance(exc,E) else "BLOCKED_RESULT_V2_INTEGRATION"
        print(canon({"schema":"wb.openai.booster.result_v2_integration.result.v1","status":"BLOCKED",
                     "terminal_status":code,"project_acceptance":"NOT_GRANTED",
                     "project_state_mutation":False}))
        return 20

if __name__=="__main__": raise SystemExit(main())
