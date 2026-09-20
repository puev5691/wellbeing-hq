from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import hashlib, importlib.util, json, sys

WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"
STORE_SHA256="PLACEHOLDER_STORE_SHA256"

class IntegrationError(RuntimeError): pass

def _load(path:Path,expected:str,name:str):
    try: raw=Path(path).read_bytes()
    except OSError: raise IntegrationError("BLOCKED_DEPENDENCY_UNAVAILABLE") from None
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise IntegrationError("BLOCKED_DEPENDENCY_IDENTITY")
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise IntegrationError("BLOCKED_DEPENDENCY_IMPORT")
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod
    try: spec.loader.exec_module(mod)
    except Exception: raise IntegrationError("BLOCKED_DEPENDENCY_IMPORT") from None
    return mod

@dataclass(frozen=True)
class ResultIdentity:
    task_commit:str
    task_blob:str
    writer_blob:str

class ReviewableLiveWorker:
    def __init__(self,*,worker_path:Path,store_path:Path,ledger_path:Path,result_dir:Path,resolver,client):
        self.worker=_load(worker_path,WORKER_SHA256,"_reviewable_live_worker")
        self.store=_load(store_path,STORE_SHA256,"_review_result_store")
        self.ledger_path=Path(ledger_path)
        self.result_dir=Path(result_dir)
        self.resolver=resolver
        self.client=client

    def invoke_once_and_persist(self,plan,identity:ResultIdentity,*,now_tick:int):
        if not isinstance(plan,self.worker.WorkerPlan):
            raise IntegrationError("BLOCKED_PLAN")
        if plan.provider!="openai":
            raise IntegrationError("BLOCKED_PROVIDER_MISMATCH")
        expected_attempt=self.worker.sha({"authority":plan.authority_sha256,
                                          "request":plan.request_sha256,
                                          "plan":plan.plan_sha256})
        live=self.worker.LiveWorker(self.worker.DurableOneShotLedger(self.ledger_path),self.resolver,self.client)
        try:
            reply=live.invoke_once(plan,now_tick=now_tick)
        except self.worker.WorkerError as exc:
            raise IntegrationError(str(exc)) from None
        if reply.attempt_key!=expected_attempt or reply.request_sha256!=plan.request_sha256:
            raise IntegrationError("BLOCKED_RESULT_IDENTITY_MISMATCH")
        try:
            record=self.store.normalize_openai_result(
                body=reply.body,
                attempt_key=reply.attempt_key,
                request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,
                task_blob=identity.task_blob,
                writer_blob=identity.writer_blob,
                provider=reply.provider,
                model=reply.model,
                http_status=reply.http_status,
                provider_calls=reply.attempts,
                retries=reply.automatic_retries,
                fallback="none")
            record["plan_sha256"]=reply.plan_sha256
            record["authority_sha256"]=plan.authority_sha256
            target=self.result_dir/(reply.attempt_key+".review.json")
            self.store.persist_atomic(target,record)
            persisted=self.store.read_and_validate(
                target,attempt_key=reply.attempt_key,request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,task_blob=identity.task_blob,writer_blob=identity.writer_blob,
                provider=reply.provider,model=reply.model)
            if persisted.get("plan_sha256")!=reply.plan_sha256 or persisted.get("authority_sha256")!=plan.authority_sha256:
                raise self.store.PersistenceError("BLOCKED_RESULT_IDENTITY_MISMATCH")
        except self.store.PersistenceError as exc:
            raise IntegrationError("BLOCKED_REVIEW_RESULT_PERSISTENCE:"+str(exc)) from None
        return {
          "schema":"wb.openai.booster.reviewable_live_result.v1",
          "technical_status":"PASS_PERSISTED_REVIEWABLE_RESULT",
          "attempt_key":reply.attempt_key,
          "result_path":str(target),
          "provider":"openai",
          "model":reply.model,
          "provider_calls":1,
          "retries":0,
          "fallback":"none",
          "requester_review_required":True,
          "project_acceptance":"NOT_GRANTED",
          "project_state_mutation":False,
          "provider_writer_authority":False,
          "gateway_writer_authority":False
        }
