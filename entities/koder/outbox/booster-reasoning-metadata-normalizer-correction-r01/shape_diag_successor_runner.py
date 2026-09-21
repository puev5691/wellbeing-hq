#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, sys

DIAG_INTEGRATION_SHA256="ab9e254a34151ed53e36160c4d63ff0b361774f8340bbfc34c56594e550b0deb"
SHAPE_STORE_SHA256="bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f"
RESULT_INTEGRATION_SHA256="54f8ac0c52b8a6f14c22f69a0dd837506f9054aada0a353ac4f09cd473700c95"
RESULT_STORE_SHA256="72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba"
WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"

SECRETREF="secretref:openai:wellbeing-entity-boosters-restricted"
OBJECT="openai-wellbeing-entity-boosters-restricted"
TASK_COMMIT="c751b3e22c4df45ec74aed995096516ecee8a689"
TASK_BLOB="ce56ff61413af96494b3332b35684008eac2684e"
WRITER_BLOB="cf1c84f9df7c90509703e4885844d0cf871ff412"
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
    try:s.loader.exec_module(m)
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

def execute(*,invocation_path,worker_path,diag_integration_path,result_integration_path,
            result_store_path,shape_store_path,ledger_path,shape_dir,result_dir,
            resolver=None,client=None,now_tick=1):
    o=read_invocation(invocation_path)
    worker=load_pinned(worker_path,WORKER_SHA256,"_successor_worker")
    diag=load_pinned(diag_integration_path,DIAG_INTEGRATION_SHA256,"_successor_diag")
    result_integration=load_pinned(result_integration_path,RESULT_INTEGRATION_SHA256,"_successor_result_integration")
    result_store=load_pinned(result_store_path,RESULT_STORE_SHA256,"_successor_result_store")
    shape_store=load_pinned(shape_store_path,SHAPE_STORE_SHA256,"_successor_shape_store")

    if o["mode"]=="SENTINEL":
        d=os.environ.get("CREDENTIALS_DIRECTORY")
        need(bool(d) and (Path(d)/OBJECT).is_file(),"BLOCKED_CREDENTIAL_OBJECT")
        return {
          "schema":"wb.openai.booster.shape_diag_successor.sentinel.v1",
          "status":"READY",
          "credential_loaded_for_child":True,
          "credential_value_read":False,
          "provider_calls":0,
          "shape_schema":shape_store.SCHEMA,
          "review_schema":result_store.SCHEMA,
          "shape_dir":str(shape_dir),
          "result_dir":str(result_dir),
          "project_acceptance":"NOT_GRANTED",
          "production_acceptance":"NOT_GRANTED"
        }

    plan=make_plan(worker,o)
    resolver=resolver or SystemdCredentialResolver(worker)
    client=client or worker.BoundedUrllibClient()
    identity=diag.Identity(TASK_COMMIT,TASK_BLOB,WRITER_BLOB)
    rw=diag.DiagnosticReviewableLiveWorker(
        worker_path=Path(worker_path),
        result_integration_path=Path(result_integration_path),
        result_store_path=Path(result_store_path),
        shape_store_path=Path(shape_store_path),
        ledger_path=Path(ledger_path),
        shape_dir=Path(shape_dir),
        result_dir=Path(result_dir),
        resolver=resolver,
        client=client)
    try:
        out=rw.invoke_once_persist_shape_then_normalize(plan,identity,now_tick=now_tick)
    except diag.ShapeIntegrationError as exc:
        raise E(str(exc)) from None
    need(out.get("status")=="PASS_AFTER_SHAPE_AND_REVIEW_PERSISTENCE","BLOCKED_SUCCESSOR_RESULT")
    return {
      "schema":"wb.openai.booster.shape_diag_successor.result.v1",
      "status":"PASS_AFTER_SHAPE_AND_REVIEW_PERSISTENCE",
      "attempt_key":out["attempt_key"],
      "shape_path":out["shape_path"],
      "shape_snapshot_sha256":out["shape_snapshot_sha256"],
      "result_path":out["result_path"],
      "provider":"openai","model":MODEL,"provider_calls":1,
      "retries":0,"fallback":"none","requester_review_required":True,
      "project_acceptance":"NOT_GRANTED","production_acceptance":"NOT_GRANTED",
      "project_state_mutation":False,"provider_writer_authority":False,"gateway_writer_authority":False
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--worker",required=True)
    ap.add_argument("--diag-integration",required=True)
    ap.add_argument("--result-integration",required=True)
    ap.add_argument("--result-store",required=True)
    ap.add_argument("--shape-store",required=True)
    ap.add_argument("--invocation",required=True)
    ap.add_argument("--ledger",required=True)
    ap.add_argument("--shape-dir",required=True)
    ap.add_argument("--result-dir",required=True)
    ns=ap.parse_args()
    try:
        out=execute(invocation_path=ns.invocation,worker_path=ns.worker,
            diag_integration_path=ns.diag_integration,result_integration_path=ns.result_integration,
            result_store_path=ns.result_store,shape_store_path=ns.shape_store,
            ledger_path=ns.ledger,shape_dir=ns.shape_dir,result_dir=ns.result_dir)
        print(canon(out)); return 0
    except Exception as exc:
        code=str(exc) if isinstance(exc,E) else "BLOCKED_SHAPE_DIAG_SUCCESSOR_WIRING"
        print(canon({"schema":"wb.openai.booster.shape_diag_successor.result.v1",
                     "status":"BLOCKED","terminal_status":code,
                     "project_acceptance":"NOT_GRANTED","production_acceptance":"NOT_GRANTED",
                     "project_state_mutation":False}))
        return 20

if __name__=="__main__": raise SystemExit(main())
