from __future__ import annotations
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Protocol, Any
import argparse, hashlib, importlib.util, json, re, sys

BOOSTER_SHA256="c0b64fd44879c6c2395c02f66ee79c641a36c768372513ed35d149289ff2d941"
WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"
OPENAI_URL="https://api.openai.com/v1/responses"
PROVIDER="openai"
D0_PAYLOAD="Synthetic bounded request."
MAX_REQUEST_BYTES=32768
MAX_RESPONSE_BYTES=65536

class PrepError(RuntimeError): pass
def require(ok,code):
    if not ok: raise PrepError(code)
def canon(v): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)
def sha(v): return hashlib.sha256((v if isinstance(v,bytes) else canon(v).encode())).hexdigest()

def load_pinned(path:Path,expected_sha:str,name:str):
    try: raw=path.read_bytes()
    except OSError: raise PrepError("BLOCKED_DEPENDENCY_UNAVAILABLE") from None
    require(hashlib.sha256(raw).hexdigest()==expected_sha,"BLOCKED_DEPENDENCY_IDENTITY")
    spec=importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,"BLOCKED_DEPENDENCY_IMPORT")
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod
    try: spec.loader.exec_module(mod)
    except Exception: raise PrepError("BLOCKED_DEPENDENCY_IMPORT") from None
    return mod

@dataclass(frozen=True)
class LiveAuthority:
    authority_id:str
    entity_id:str
    task_commit:str
    writer_blob:str
    provider:str
    model:str
    privacy_class:str
    data_class:str
    tools:tuple[str,...]
    credential_ref:str=field(repr=False)
    max_output_tokens:int=64
    max_response_bytes:int=16384
    timeout_seconds:float=30.0
    max_calls:int=1
    automatic_retries:int=0
    fallback:str="none"
    use_once:bool=True
    live_execution_authorized:bool=True
    valid_until_tick:int=1
    @property
    def identity(self): return sha(asdict(self))

@dataclass(frozen=True)
class PreparedLivePlan:
    request_sha256:str
    authority_sha256:str
    requester_sha256:str
    provider:str
    model:str
    privacy_class:str
    data_class:str
    tools:tuple[str,...]
    credential_ref:str=field(repr=False)
    native_plan_json:str=field(repr=False)
    timeout_seconds:float=30.0
    max_response_bytes:int=16384
    max_calls:int=1
    automatic_retries:int=0
    fallback:str="none"
    valid_until_tick:int=1
    live_enabled:bool=False
    project_acceptance:str="NOT_GRANTED"
    review_required:bool=True
    @property
    def identity(self): return sha(asdict(self))

class Resolver(Protocol):
    def resolve(self,ref): ...

def validate_live_authority(req,auth:LiveAuthority):
    require(type(auth) is LiveAuthority,"BLOCKED_AUTHORITY_SCHEMA")
    require(auth.live_execution_authorized is True and auth.use_once is True,"BLOCKED_LIVE_EXECUTION_AUTHORITY")
    require(auth.entity_id==req.entity_id and auth.task_commit==req.task_commit and auth.writer_blob==req.writer_blob,"BLOCKED_AUTHORITY_BINDING")
    require(auth.provider==PROVIDER and req.provider==PROVIDER and auth.provider==req.provider,"BLOCKED_PROVIDER_BINDING")
    require(auth.model==req.model and type(auth.model) is str and bool(auth.model),"BLOCKED_MODEL_BINDING")
    require(auth.privacy_class==req.privacy_class=="synthetic_only","BLOCKED_PRIVACY_BOUNDARY")
    require(auth.data_class=="D0_SYNTHETIC","BLOCKED_DATA_CLASS")
    require(auth.tools==req.tools==(),"BLOCKED_TOOL_AUTHORITY")
    require(auth.max_calls==1 and auth.automatic_retries==0 and auth.fallback=="none","BLOCKED_RETRY_FALLBACK_POLICY")
    require(type(auth.max_output_tokens) is int and 1<=auth.max_output_tokens<=64,"BLOCKED_OUTPUT_BOUND")
    require(type(auth.max_response_bytes) is int and 1<=auth.max_response_bytes<=MAX_RESPONSE_BYTES,"BLOCKED_RESPONSE_LIMIT")
    require(type(auth.timeout_seconds) in (int,float) and 1<=auth.timeout_seconds<=60,"BLOCKED_TIMEOUT_POLICY")
    require(type(auth.valid_until_tick) is int and 1<=auth.valid_until_tick<=2**53-1,"BLOCKED_AUTHORITY_EXPIRY")
    require(type(auth.credential_ref) is str and re.fullmatch(r"secretref:openai:[A-Za-z0-9_.-]{1,64}",auth.credential_ref) is not None,"BLOCKED_CREDENTIAL_REF")
    require(req.payload==D0_PAYLOAD,"BLOCKED_D0_PAYLOAD")
    require(req.max_output_tokens==auth.max_output_tokens,"BLOCKED_OUTPUT_BOUND")

def requester_sha(req)->str:
    return sha({"entity_id":req.entity_id,"role":req.role,
                "task":{"path":req.task_path,"commit":req.task_commit,"blob":req.task_blob},
                "writer":{"path":req.writer_path,"commit":req.writer_commit,"blob":req.writer_blob}})

class LivePath:
    def __init__(self,*,booster_path:Path,worker_path:Path):
        self.booster=load_pinned(booster_path,BOOSTER_SHA256,"_openai_liveprep_booster_r02")
        self.worker=load_pinned(worker_path,WORKER_SHA256,"_openai_liveprep_worker_r01")

    def prepare(self,req,auth:LiveAuthority)->PreparedLivePlan:
        require(type(req) is self.booster.BoosterRequest,"BLOCKED_REQUEST_SCHEMA")
        # Reuse r0.2 request validation with an exact replay-only surrogate authority.
        surrogate=self.booster.Authority(
            "surrogate-r02-validation","REPLAY_ONLY",req.entity_id,req.task_commit,req.writer_blob,
            req.provider,req.model,req.privacy_class,req.tools,False)
        try: self.booster.validate_request(req,surrogate)
        except Exception as exc: raise PrepError(str(exc)) from None
        validate_live_authority(req,auth)
        body={"model":req.model,"input":req.payload,"max_output_tokens":auth.max_output_tokens,
              "store":False,"tools":[],"tool_choice":"none","parallel_tool_calls":False}
        native={"method":"POST","url":OPENAI_URL,"headers":{"content-type":"application/json"},"body":body}
        return PreparedLivePlan(
            sha(asdict(req)),auth.identity,requester_sha(req),PROVIDER,req.model,req.privacy_class,
            "D0_SYNTHETIC",req.tools,auth.credential_ref,canon(native),auth.timeout_seconds,
            auth.max_response_bytes,auth.max_calls,auth.automatic_retries,auth.fallback,
            auth.valid_until_tick,False,"NOT_GRANTED",True)

    def worker_plan(self,prepared:PreparedLivePlan):
        require(type(prepared) is PreparedLivePlan and prepared.live_enabled is False,"BLOCKED_PREPARED_PLAN")
        try:
            return self.worker.WorkerPlan(
                prepared.request_sha256,prepared.identity,prepared.authority_sha256,prepared.requester_sha256,
                prepared.provider,prepared.model,prepared.native_plan_json,
                self.worker.SecretRef("openai",prepared.credential_ref),
                self.worker.WorkerPolicy(prepared.timeout_seconds,prepared.max_response_bytes,
                                         prepared.max_calls,prepared.automatic_retries),
                prepared.valid_until_tick)
        except self.worker.WorkerError as exc: raise PrepError(str(exc)) from None

    def invoke_sentinel(self,prepared:PreparedLivePlan,*,ledger_path:Path,resolver:Resolver,client,now_tick:int):
        plan=self.worker_plan(prepared)
        ledger=self.worker.DurableOneShotLedger(ledger_path)
        worker=self.worker.LiveWorker(ledger,resolver,client)
        try: reply=worker.invoke_once(plan,now_tick=now_tick)
        except self.worker.WorkerError as exc: raise PrepError(str(exc)) from None
        red=reply.redacted()
        require(red["automatic_retries"]==0 and red["attempts"]==1,"FAIL_RETRY_OR_MULTI_CALL")
        require(red["project_acceptance"]=="NOT_GRANTED" and red["caller_writer_changed"] is False and
                red["project_state_applied"] is False and red["external_dispatch_performed"] is False,
                "FAIL_RESULT_AUTHORITY")
        return {"schema":"wb.openai_entity_booster.live_path_sentinel_result.v1",
                "technical_status":"completed","terminal_status":"PASS_SENTINEL_LIVE_WORKER_BOUNDARY",
                "provider":"openai","model":prepared.model,"worker":red,
                "project_acceptance":"NOT_GRANTED","review_required":True,
                "gateway_writer_authority":False,"provider_writer_authority":False,
                "project_state_applied":False,"external_dispatch_performed":False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--booster",required=True); ap.add_argument("--worker",required=True)
    ap.add_argument("--request",required=True); ap.add_argument("--authority",required=True)
    ns=ap.parse_args()
    try:
        b=load_pinned(Path(ns.booster),BOOSTER_SHA256,"_openai_liveprep_booster_cli")
        req_obj=json.loads(Path(ns.request).read_text())
        auth_obj=json.loads(Path(ns.authority).read_text())
        req_obj["tools"]=tuple(req_obj["tools"]); auth_obj["tools"]=tuple(auth_obj["tools"])
        req=b.BoosterRequest(**req_obj); auth=LiveAuthority(**auth_obj)
        prepared=LivePath(booster_path=Path(ns.booster),worker_path=Path(ns.worker)).prepare(req,auth)
        print(canon({"schema":"wb.openai_entity_booster.prepared_live_plan.v1",
                     "request_sha256":prepared.request_sha256,"plan_sha256":prepared.identity,
                     "authority_sha256":prepared.authority_sha256,"provider":prepared.provider,
                     "model":prepared.model,"project_acceptance":"NOT_GRANTED","review_required":True}))
        return 0
    except (PrepError,ValueError,TypeError,OSError) as exc:
        print(canon({"schema":"wb.openai_entity_booster.prepared_live_plan.v1","status":"blocked",
                     "terminal_status":str(exc),"project_acceptance":"NOT_GRANTED","review_required":True}))
        return 20
if __name__=="__main__": raise SystemExit(main())
