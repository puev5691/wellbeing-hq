from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
from types import ModuleType
from typing import Any
import argparse, hashlib, importlib.util, json, re, sys

VERSION="entity-booster-runtime-r02"
GATEWAY_SHA256="703f9e4a72ab043063ff74f636ec6c3fa85de1a8fc8b89ac1859623f46a17d7a"
LIVE_WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"
MAX_INPUT_BYTES=32768
MAX_RESULT_BYTES=16384
ALLOWED_PROVIDERS=frozenset({"openai","anthropic"})

class BoosterError(RuntimeError): pass

def canonical(v:Any)->bytes:
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")
def sha(v:Any)->str:
    return hashlib.sha256(v if isinstance(v,bytes) else canonical(v)).hexdigest()
def require(ok:bool,code:str):
    if not ok: raise BoosterError(code)

def load_pinned(path:Path,expected_sha:str,name:str):
    try: raw=path.read_bytes()
    except OSError: raise BoosterError("BLOCKED_DEPENDENCY_UNAVAILABLE") from None
    require(hashlib.sha256(raw).hexdigest()==expected_sha,"BLOCKED_DEPENDENCY_IDENTITY")
    spec=importlib.util.spec_from_file_location(name,path)
    require(spec is not None and spec.loader is not None,"BLOCKED_DEPENDENCY_IMPORT")
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod
    try: spec.loader.exec_module(mod)
    except Exception: raise BoosterError("BLOCKED_DEPENDENCY_IMPORT") from None
    return mod

@dataclass(frozen=True)
class Authority:
    authority_id:str
    mode:str
    entity_id:str
    task_commit:str
    writer_blob:str
    provider:str
    model:str
    privacy_class:str
    tools:tuple[str,...]
    live_execution_authorized:bool=False
    @property
    def identity(self): return sha(asdict(self))

@dataclass(frozen=True)
class BoosterRequest:
    request_id:str
    entity_id:str
    role:str
    task_path:str
    task_commit:str
    task_blob:str
    writer_path:str
    writer_commit:str
    writer_blob:str
    purpose:str
    provider:str
    model:str
    privacy_class:str
    tools:tuple[str,...]
    payload:str
    source_locator:str
    source_sha256:str
    max_output_tokens:int=64

@dataclass(frozen=True)
class BoosterResult:
    schema:str
    request_id:str
    request_sha256:str
    provider:str
    model:str
    technical_status:str
    terminal_status:str
    blocker:str|None
    output:str
    usage:tuple[tuple[str,int],...]
    project_acceptance:str="NOT_GRANTED"
    review_required:bool=True
    caller_writer_changed:bool=False
    gateway_writer_authority:bool=False
    provider_writer_authority:bool=False
    project_state_applied:bool=False
    external_dispatch_performed:bool=False
    live_provider_calls:int=0
    credential_reads:int=0

def parse_input(raw:bytes):
    require(type(raw) is bytes and 0<len(raw)<=MAX_INPUT_BYTES,"BLOCKED_INPUT_SIZE")
    try: obj=json.loads(raw.decode("utf-8"))
    except Exception: raise BoosterError("BLOCKED_INPUT_JSON") from None
    require(type(obj) is dict and set(obj)=={"request","authority","replay"},"BLOCKED_INPUT_SCHEMA")
    r=obj["request"]; a=obj["authority"]; replay=obj["replay"]
    require(type(r) is dict and type(a) is dict and type(replay) is dict,"BLOCKED_INPUT_SCHEMA")
    expected_r=set(BoosterRequest.__dataclass_fields__)
    expected_a=set(Authority.__dataclass_fields__)
    require(set(r)==expected_r and set(a)==expected_a,"BLOCKED_INPUT_SCHEMA")
    try:
        r=dict(r); r["tools"]=tuple(r["tools"])
        a=dict(a); a["tools"]=tuple(a["tools"])
        req=BoosterRequest(**r); auth=Authority(**a)
    except Exception: raise BoosterError("BLOCKED_INPUT_SCHEMA") from None
    require(type(replay.get("http_status")) is int and set(replay)=={"http_status","body"} and type(replay["body"]) is dict,"BLOCKED_REPLAY_SCHEMA")
    return req,auth,replay

def validate_request(req:BoosterRequest,auth:Authority):
    atom=lambda x: type(x) is str and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}",x or "") is not None
    h40=lambda x:type(x) is str and re.fullmatch(r"[0-9a-f]{40}",x) is not None
    h64=lambda x:type(x) is str and re.fullmatch(r"[0-9a-f]{64}",x) is not None
    require(atom(req.request_id) and atom(req.entity_id) and atom(req.role),"BLOCKED_REQUEST_SCHEMA")
    require(type(req.task_path) is str and 0<len(req.task_path)<=256 and h40(req.task_commit) and h40(req.task_blob),"BLOCKED_TASK_IDENTITY")
    require(type(req.writer_path) is str and 0<len(req.writer_path)<=256 and h40(req.writer_commit) and h40(req.writer_blob),"BLOCKED_WRITER_IDENTITY")
    require(req.provider in ALLOWED_PROVIDERS and type(req.model) is str and bool(req.model),"BLOCKED_PROVIDER_MODEL")
    require(req.privacy_class=="synthetic_only","BLOCKED_PRIVACY_BOUNDARY")
    require(req.tools==(),"BLOCKED_TOOL_AUTHORITY")
    require(type(req.payload) is str and 0<len(req.payload.encode())<=8192,"BLOCKED_REQUEST_SIZE")
    require(type(req.source_locator) is str and req.source_locator.startswith("fixture://") and h64(req.source_sha256),"BLOCKED_SOURCE_IDENTITY")
    require(type(req.max_output_tokens) is int and 1<=req.max_output_tokens<=1024,"BLOCKED_REQUEST_SIZE")
    require(auth.mode=="REPLAY_ONLY" and auth.live_execution_authorized is False,"BLOCKED_LIVE_EXECUTION_AUTHORITY")
    require(auth.entity_id==req.entity_id and auth.task_commit==req.task_commit and auth.writer_blob==req.writer_blob,"BLOCKED_AUTHORITY_BINDING")
    require(auth.provider==req.provider and auth.model==req.model and auth.privacy_class==req.privacy_class and auth.tools==req.tools,"BLOCKED_AUTHORITY_BINDING")
    require(atom(auth.authority_id),"BLOCKED_AUTHORITY_BINDING")

class Runtime:
    def __init__(self,*,gateway_path:Path,live_worker_path:Path,deps:Path,ledger_path:Path):
        self.gateway=load_pinned(gateway_path,GATEWAY_SHA256,"_booster_gateway_r01")
        self.worker=load_pinned(live_worker_path,LIVE_WORKER_SHA256,"_booster_live_worker_r01")
        self.deps=Path(deps)
        self.ledger=self.worker.DurableOneShotLedger(Path(ledger_path))
        p=self.worker.WorkerPolicy()
        require(p.max_calls==1 and p.automatic_retries==0 and 1<=p.timeout_seconds<=60 and p.max_response_bytes<=65536,"FAIL_WORKER_POLICY")
    def run(self,req:BoosterRequest,auth:Authority,replay:dict)->BoosterResult:
        validate_request(req,auth)
        g=self.gateway
        task=g.ArtifactRef("puev5691/wellbeing-hq",req.task_path,req.task_commit,req.task_blob)
        writer=g.ArtifactRef("puev5691/wellbeing-hq",req.writer_path,req.writer_commit,req.writer_blob)
        requester=g.Requester(req.entity_id,req.role,task,writer)
        source=g.SourceRef(req.source_locator,req.source_sha256,"D0_SYNTHETIC")
        er=g.EntityRequest(req.request_id,requester,req.purpose,req.provider,req.model,
            "D0_SYNTHETIC",req.privacy_class,("text",),req.tools,False,(source,),
            req.payload,g.AcceptancePolicy(max_output_bytes=4096),req.max_output_tokens)
        require(er.identity==sha(asdict(er)),"FAIL_REQUEST_IDENTITY")
        plan_sha=sha({"provider":req.provider,"model":req.model,"privacy":req.privacy_class,
                      "tools":req.tools,"max_output_tokens":req.max_output_tokens,"mode":"REPLAY_ONLY"})
        attempt_key=sha({"authority":auth.identity,"request":er.identity,"plan":plan_sha})
        try:
            self.ledger.claim(attempt_key,er.identity,plan_sha,auth.identity)
        except self.worker.WorkerError as exc:
            raise BoosterError(str(exc)) from None
        gateway=g.Gateway(self.deps,verifier=lambda candidate: candidate.identity==er.identity)
        fixture=g.ReplayResponse(er.identity,req.provider,replay["http_status"],canonical(replay["body"]))
        result=gateway.run(er,fixture)
        try: self.worker.enforce_resource_result_boundary(result)
        except self.worker.WorkerError as exc: raise BoosterError(str(exc)) from None
        out=BoosterResult("wb.entity_booster.result.v2",req.request_id,er.identity,req.provider,req.model,
            result.technical_status,result.terminal_status,result.blocker,result.payload,result.usage)
        raw=canonical(asdict(out))
        require(len(raw)<=MAX_RESULT_BYTES,"BLOCKED_RESULT_BOUND")
        return out

def run_bytes(raw:bytes,*,gateway_path:Path,live_worker_path:Path,deps:Path,ledger_path:Path)->bytes:
    req,auth,replay=parse_input(raw)
    result=Runtime(gateway_path=gateway_path,live_worker_path=live_worker_path,deps=deps,ledger_path=ledger_path).run(req,auth,replay)
    return canonical(asdict(result))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--gateway",required=True); ap.add_argument("--live-worker",required=True)
    ap.add_argument("--deps",required=True); ap.add_argument("--ledger",required=True); ap.add_argument("--request",required=True)
    ns=ap.parse_args()
    raw=Path(ns.request).read_bytes()
    try:
        sys.stdout.buffer.write(run_bytes(raw,gateway_path=Path(ns.gateway),live_worker_path=Path(ns.live_worker),deps=Path(ns.deps),ledger_path=Path(ns.ledger))+b"\n")
        return 0
    except BoosterError as exc:
        sys.stdout.buffer.write(canonical({"schema":"wb.entity_booster.result.v2","technical_status":"blocked","terminal_status":str(exc),"project_acceptance":"NOT_GRANTED","review_required":True})+b"\n")
        return 20
if __name__=="__main__": raise SystemExit(main())
