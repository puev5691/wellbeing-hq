#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Protocol, Any
import hashlib, json, math, re, signal, sqlite3, threading, time, urllib.error, urllib.request

PASS="PASS_ENTITY_RESOURCE_GATEWAY_LIVE_WORKER_RACE_FIX_R01_READY_FOR_REVERIFY"
OPENAI_URL="https://api.openai.com/v1/responses"
ANTHROPIC_URL="https://api.anthropic.com/v1/messages"

class WorkerError(RuntimeError):
    pass
def require(ok, code):
    if not ok: raise WorkerError(code)
def canon(v): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False)
def sha(v): return hashlib.sha256((v if isinstance(v,bytes) else canon(v).encode())).hexdigest()
def bounded_int(v,lo,hi): return type(v) is int and lo<=v<=hi

@dataclass(frozen=True)
class SecretRef:
    provider:str
    locator:str=field(repr=False)
    def __post_init__(self):
        require(self.provider in ("openai","anthropic"),"BLOCKED_CREDENTIAL_REF")
        require(type(self.locator) is str and re.fullmatch(r"secretref:"+self.provider+r":[A-Za-z0-9_.-]{1,64}",self.locator) is not None,"BLOCKED_CREDENTIAL_REF")

@dataclass(frozen=True)
class ResolvedSecret:
    provider:str
    value:str=field(repr=False)
    def __post_init__(self):
        require(self.provider in ("openai","anthropic"),"BLOCKED_CREDENTIAL_VALUE")
        require(type(self.value) is str and 1<=len(self.value)<=4096 and "\n" not in self.value and "\r" not in self.value,"BLOCKED_CREDENTIAL_VALUE")

class CredentialResolver(Protocol):
    def resolve(self, ref:SecretRef)->ResolvedSecret: ...

@dataclass(frozen=True)
class WorkerPolicy:
    timeout_seconds:float=30.0
    max_response_bytes:int=65536
    max_calls:int=1
    automatic_retries:int=0
    def __post_init__(self):
        require(type(self.timeout_seconds) in (int,float) and not isinstance(self.timeout_seconds,bool) and math.isfinite(self.timeout_seconds) and 1<=self.timeout_seconds<=60,"BLOCKED_TIMEOUT_POLICY")
        require(bounded_int(self.max_response_bytes,1,65536),"BLOCKED_RESPONSE_LIMIT")
        require(self.max_calls==1 and self.automatic_retries==0,"BLOCKED_RETRY_POLICY")

@dataclass(frozen=True)
class WorkerPlan:
    request_sha256:str
    plan_sha256:str
    authority_sha256:str
    requester_sha256:str
    provider:str
    model:str
    native_plan_json:str=field(repr=False)
    secret_ref:SecretRef=field(repr=False)
    policy:WorkerPolicy
    valid_until_tick:int
    def __post_init__(self):
        for v in (self.request_sha256,self.plan_sha256,self.authority_sha256,self.requester_sha256):
            require(type(v) is str and re.fullmatch(r"[0-9a-f]{64}",v) is not None,"BLOCKED_PLAN_IDENTITY")
        require(self.provider in ("openai","anthropic") and type(self.model) is str and bool(self.model),"BLOCKED_PROVIDER_MODEL")
        require(type(self.native_plan_json) is str and 1<=len(self.native_plan_json.encode())<=65536,"BLOCKED_PLAN")
        require(type(self.secret_ref) is SecretRef and self.secret_ref.provider==self.provider,"BLOCKED_CREDENTIAL_REF")
        require(type(self.policy) is WorkerPolicy and bounded_int(self.valid_until_tick,1,2**53-1),"BLOCKED_PLAN")

@dataclass(frozen=True)
class WorkerReply:
    provider:str
    model:str
    http_status:int
    body:bytes=field(repr=False)
    request_sha256:str
    plan_sha256:str
    attempt_key:str
    attempts:int=1
    automatic_retries:int=0
    project_acceptance:str=field(default="NOT_GRANTED",init=False)
    caller_writer_changed:bool=field(default=False,init=False)
    project_state_applied:bool=field(default=False,init=False)
    external_dispatch_performed:bool=field(default=False,init=False)
    def redacted(self):
        return {"provider":self.provider,"model":self.model,"http_status":self.http_status,
                "response_sha256":sha(self.body),"response_bytes":len(self.body),
                "request_sha256":self.request_sha256,"plan_sha256":self.plan_sha256,
                "attempt_key":self.attempt_key,"attempts":self.attempts,
                "automatic_retries":self.automatic_retries,"project_acceptance":self.project_acceptance,
                "caller_writer_changed":False,"project_state_applied":False,"external_dispatch_performed":False}

class DurableOneShotLedger:
    """Restart-safe one-shot ledger with bounded SQLite lock handling.

    WAL/schema initialization and claim-time lock contention never leak raw sqlite3
    OperationalError. Duplicate keys map to BLOCKED_DUPLICATE_CALL; bounded lock
    exhaustion maps to BLOCKED_LEDGER_BUSY.
    """
    BUSY_RETRIES=50
    BUSY_SLEEP_SECONDS=0.01

    def __init__(self,path:Path):
        self.path=Path(path)
        self._init()

    @staticmethod
    def _is_busy(exc:BaseException)->bool:
        text=str(exc).lower()
        return "locked" in text or "busy" in text

    def _open(self):
        try:
            c=sqlite3.connect(str(self.path),timeout=5,isolation_level=None)
            c.execute("PRAGMA busy_timeout=5000")
            return c
        except sqlite3.OperationalError as exc:
            if self._is_busy(exc):
                raise WorkerError("BLOCKED_LEDGER_BUSY") from None
            raise WorkerError("BLOCKED_LEDGER_ERROR") from None

    def _retry_sqlite(self, fn):
        last_busy=False
        for _ in range(self.BUSY_RETRIES):
            try:
                return fn()
            except sqlite3.OperationalError as exc:
                if not self._is_busy(exc):
                    raise WorkerError("BLOCKED_LEDGER_ERROR") from None
                last_busy=True
                time.sleep(self.BUSY_SLEEP_SECONDS)
        if last_busy:
            raise WorkerError("BLOCKED_LEDGER_BUSY")
        raise WorkerError("BLOCKED_LEDGER_ERROR")

    def _init(self):
        c=self._open()
        try:
            self._retry_sqlite(lambda: c.execute("PRAGMA journal_mode=WAL").fetchone())
            self._retry_sqlite(lambda: c.execute("PRAGMA synchronous=FULL"))
            self._retry_sqlite(lambda: c.execute(
                "CREATE TABLE IF NOT EXISTS attempts (attempt_key TEXT PRIMARY KEY, "
                "request_sha256 TEXT NOT NULL, plan_sha256 TEXT NOT NULL, "
                "authority_sha256 TEXT NOT NULL, state TEXT NOT NULL CHECK(state='consumed'))"))
        finally:
            c.close()

    def claim(self,key,request_sha,plan_sha,authority_sha):
        require(all(type(x) is str and re.fullmatch(r"[0-9a-f]{64}",x)
                    for x in (key,request_sha,plan_sha,authority_sha)),
                "BLOCKED_LEDGER_IDENTITY")
        c=self._open()
        try:
            try:
                self._retry_sqlite(lambda: c.execute("BEGIN IMMEDIATE"))
                try:
                    c.execute("INSERT INTO attempts VALUES (?,?,?,?, 'consumed')",
                              (key,request_sha,plan_sha,authority_sha))
                except sqlite3.IntegrityError:
                    c.execute("ROLLBACK")
                    raise WorkerError("BLOCKED_DUPLICATE_CALL") from None
                c.execute("COMMIT")
            except WorkerError:
                try:
                    if c.in_transaction:
                        c.execute("ROLLBACK")
                except sqlite3.Error:
                    pass
                raise
            except sqlite3.OperationalError as exc:
                try:
                    if c.in_transaction:
                        c.execute("ROLLBACK")
                except sqlite3.Error:
                    pass
                if self._is_busy(exc):
                    raise WorkerError("BLOCKED_LEDGER_BUSY") from None
                raise WorkerError("BLOCKED_LEDGER_ERROR") from None
        finally:
            c.close()

    def count(self):
        c=self._open()
        try:
            try:
                return self._retry_sqlite(lambda: c.execute(
                    "SELECT COUNT(*) FROM attempts").fetchone()[0])
            except sqlite3.Error:
                raise WorkerError("BLOCKED_LEDGER_ERROR") from None
        finally:
            c.close()

class HardDeadline:
    def __init__(self,seconds): self.seconds=float(seconds); self.old=None
    def __enter__(self):
        require(threading.current_thread() is threading.main_thread() and hasattr(signal,"setitimer"),"BLOCKED_HARD_TIMEOUT_UNAVAILABLE")
        def handler(_s,_f): raise TimeoutError()
        self.old=signal.signal(signal.SIGALRM,handler); signal.setitimer(signal.ITIMER_REAL,self.seconds); return self
    def __exit__(self,*_):
        signal.setitimer(signal.ITIMER_REAL,0)
        if self.old is not None: signal.signal(signal.SIGALRM,self.old)

class HTTPClient(Protocol):
    calls:int
    def request(self,*,method:str,url:str,headers:dict[str,str],body:bytes,timeout:float,max_bytes:int)->tuple[int,bytes]: ...

class FailClosedRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs): return None

class BoundedUrllibClient:
    """Concrete future network client. Not used by the zero-network tests."""
    calls=0
    def __init__(self): self.calls=0; self.opener=urllib.request.build_opener(FailClosedRedirect())
    def request(self,*,method,url,headers,body,timeout,max_bytes):
        self.calls+=1
        req=urllib.request.Request(url=url,data=body,headers=headers,method=method)
        try:
            with self.opener.open(req,timeout=timeout) as r:
                status=int(getattr(r,"status",200)); data=r.read(max_bytes+1)
        except urllib.error.HTTPError as e:
            status=int(e.code); data=e.read(max_bytes+1)
        require(not 300<=status<400,"BLOCKED_REDIRECT")
        require(len(data)<=max_bytes,"BLOCKED_RESPONSE_TOO_LARGE")
        return status,data

def parse_native(plan:WorkerPlan):
    try: obj=json.loads(plan.native_plan_json)
    except Exception: raise WorkerError("BLOCKED_NATIVE_PLAN") from None
    require(type(obj) is dict,"BLOCKED_NATIVE_PLAN")
    if plan.provider=="openai":
        require(obj.get("method")=="POST" and obj.get("url")==OPENAI_URL,"BLOCKED_ENDPOINT_BINDING")
        body=obj.get("body"); headers=obj.get("headers")
        require(type(body) is dict and body.get("model")==plan.model,"BLOCKED_MODEL_BINDING")
        require(headers=={"content-type":"application/json"},"BLOCKED_HEADER_BINDING")
        require("authorization" not in headers and "x-api-key" not in headers,"BLOCKED_CREDENTIAL_VALUE_IN_PLAN")
        return "POST",OPENAI_URL,dict(headers),canon(body).encode()
    require(obj.get("method")=="POST" and obj.get("url")==ANTHROPIC_URL,"BLOCKED_ENDPOINT_BINDING")
    body=obj.get("body"); headers=dict(obj.get("headers") or [])
    require(type(body) is dict and body.get("model")==plan.model,"BLOCKED_MODEL_BINDING")
    require(headers.get("content-type")=="application/json" and headers.get("anthropic-version")=="2023-06-01","BLOCKED_HEADER_BINDING")
    require("authorization" not in {k.lower() for k in headers} and "x-api-key" not in {k.lower() for k in headers},"BLOCKED_CREDENTIAL_VALUE_IN_PLAN")
    return "POST",ANTHROPIC_URL,headers,canon(body).encode()

class LiveWorker:
    def __init__(self,ledger:DurableOneShotLedger,resolver:CredentialResolver,client:HTTPClient):
        self.ledger,self.resolver,self.client=ledger,resolver,client
    def invoke_once(self,plan:WorkerPlan,*,now_tick:int):
        require(type(plan) is WorkerPlan and bounded_int(now_tick,0,2**53-1),"BLOCKED_PLAN")
        require(now_tick < plan.valid_until_tick,"BLOCKED_STALE_AUTHORITY")
        method,url,headers,body=parse_native(plan)
        attempt_key=sha({"authority":plan.authority_sha256,"request":plan.request_sha256,"plan":plan.plan_sha256})
        self.ledger.claim(attempt_key,plan.request_sha256,plan.plan_sha256,plan.authority_sha256)
        try: secret=self.resolver.resolve(plan.secret_ref)
        except Exception: raise WorkerError("BLOCKED_CREDENTIAL_RESOLUTION") from None
        require(type(secret) is ResolvedSecret and secret.provider==plan.provider,"BLOCKED_CREDENTIAL_RESOLUTION")
        headers=dict(headers)
        if plan.provider=="openai": headers["authorization"]="Bearer "+secret.value
        else: headers["authorization"]="Bearer "+secret.value
        try:
            with HardDeadline(plan.policy.timeout_seconds):
                status,data=self.client.request(method=method,url=url,headers=headers,body=body,
                    timeout=plan.policy.timeout_seconds,max_bytes=plan.policy.max_response_bytes)
        except TimeoutError: raise WorkerError("BLOCKED_HARD_TIMEOUT") from None
        except WorkerError: raise
        except Exception: raise WorkerError("BLOCKED_WORKER_IO") from None
        require(getattr(self.client,"calls",1)==1,"FAIL_RETRY_OR_MULTI_CALL")
        require(type(status) is int and 100<=status<=599,"BLOCKED_HTTP_STATUS")
        require(type(data) is bytes and len(data)<=plan.policy.max_response_bytes,"BLOCKED_RESPONSE_TOO_LARGE")
        require(not 300<=status<400,"BLOCKED_REDIRECT")
        if status==200:
            try: parsed=json.loads(data.decode("utf-8"))
            except Exception: raise WorkerError("BLOCKED_PROVIDER_RESPONSE") from None
            require(type(parsed) is dict and parsed.get("model")==plan.model,"BLOCKED_MODEL_MISMATCH")
        return WorkerReply(plan.provider,plan.model,status,data,plan.request_sha256,plan.plan_sha256,attempt_key)


def bind_prepared(prepared:object, admission:object, *, now_tick:int)->WorkerPlan:
    """Attach only an exact independently admitted preparation object. No authority is minted here."""
    try:
        require(getattr(prepared,"live_enabled") is False,"BLOCKED_PREPARED_PLAN")
        require(getattr(admission,"mode")== "LIVE","BLOCKED_AUTHORITY_MODE")
        require(getattr(admission,"request_sha256")==prepared.request_sha256,"BLOCKED_AUTHORITY_BINDING")
        require(getattr(admission,"plan_sha256")==prepared.identity,"BLOCKED_AUTHORITY_BINDING")
        require(getattr(admission,"requester_sha256")==sha(asdict(prepared.requester)),"BLOCKED_AUTHORITY_BINDING")
        require(bounded_int(now_tick,0,2**53-1) and now_tick < admission.valid_until_tick,"BLOCKED_STALE_AUTHORITY")
        cred=SecretRef(prepared.provider,prepared.credential.locator)
        policy=WorkerPolicy(float(prepared.policy.timeout_seconds),int(prepared.policy.max_response_bytes),
                            int(prepared.policy.max_attempts),int(prepared.policy.automatic_retries))
        return WorkerPlan(prepared.request_sha256,prepared.identity,admission.authority_sha256,
                          admission.requester_sha256,prepared.provider,prepared.model,
                          prepared.native_plan_json,cred,policy,admission.valid_until_tick)
    except WorkerError:
        raise
    except Exception:
        raise WorkerError("BLOCKED_PREPARED_PLAN") from None


def enforce_resource_result_boundary(result:object):
    """Final attachment guard for the accepted gateway ResourceResult; does not construct/accept it."""
    require(getattr(result,"project_acceptance",None)=="NOT_GRANTED","FAIL_RESOURCE_RESULT_AUTHORITY")
    require(getattr(result,"caller_writer_changed",None) is False,"FAIL_RESOURCE_RESULT_AUTHORITY")
    require(getattr(result,"project_state_applied",None) is False,"FAIL_RESOURCE_RESULT_AUTHORITY")
    require(getattr(result,"external_dispatch_performed",None) is False,"FAIL_RESOURCE_RESULT_AUTHORITY")
    require(getattr(result,"gateway_writer_authority",None) is False,"FAIL_RESOURCE_RESULT_AUTHORITY")
    require(getattr(result,"provider_writer_authority",None) is False,"FAIL_RESOURCE_RESULT_AUTHORITY")
    require(getattr(result,"routing_status",None)=="not_started","FAIL_RESOURCE_RESULT_AUTHORITY")
    return result