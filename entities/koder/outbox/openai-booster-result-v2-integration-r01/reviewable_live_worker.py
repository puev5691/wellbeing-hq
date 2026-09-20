from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import hashlib, importlib.util, sys

WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"
STORE_SHA256="cd01972b7045d4f84583fb5470d4c0012e09c12b954ea65221107eaa01385d7e"

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
        self.worker=_load(worker_path,WORKER_SHA256,"_reviewable_live_worker_r02")
        self.store=_load(store_path,STORE_SHA256,"_review_result_store_r02")
        self.ledger_path=Path(ledger_path)
        self.result_dir=Path(result_dir)
        self.resolver=resolver
        self.client=client

    def _local_plan(self,plan):
        try:
            return self.worker.WorkerPlan(
                plan.request_sha256,plan.plan_sha256,plan.authority_sha256,plan.requester_sha256,
                plan.provider,plan.model,plan.native_plan_json,
                self.worker.SecretRef(plan.secret_ref.provider,plan.secret_ref.locator),
                self.worker.WorkerPolicy(plan.policy.timeout_seconds,plan.policy.max_response_bytes,
                                         plan.policy.max_calls,plan.policy.automatic_retries),
                plan.valid_until_tick)
        except Exception:
            raise IntegrationError("BLOCKED_PLAN") from None

    def invoke_once_and_persist(self,plan,identity:ResultIdentity,*,now_tick:int):
        local_plan=self._local_plan(plan)
        if local_plan.provider!="openai":
            raise IntegrationError("BLOCKED_PROVIDER_MISMATCH")
        expected_attempt=self.worker.sha({"authority":local_plan.authority_sha256,
                                          "request":local_plan.request_sha256,
                                          "plan":local_plan.plan_sha256})
        outer=self
        class ResolverAdapter:
            def resolve(self,ref):
                try:
                    resolved=outer.resolver.resolve(ref)
                    return outer.worker.ResolvedSecret(resolved.provider,resolved.value)
                except Exception:
                    raise outer.worker.WorkerError("BLOCKED_CREDENTIAL_RESOLUTION") from None
        live=self.worker.LiveWorker(self.worker.DurableOneShotLedger(self.ledger_path),ResolverAdapter(),self.client)
        try:
            reply=live.invoke_once(local_plan,now_tick=now_tick)
        except self.worker.WorkerError as exc:
            raise IntegrationError(str(exc)) from None
        if reply.attempt_key!=expected_attempt or reply.request_sha256!=local_plan.request_sha256:
            raise IntegrationError("BLOCKED_RESULT_IDENTITY_MISMATCH")
        try:
            record=self.store.normalize_openai_result(
                body=reply.body,
                attempt_key=reply.attempt_key,
                request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,
                task_blob=identity.task_blob,
                writer_blob=identity.writer_blob,
                plan_sha256=reply.plan_sha256,
                authority_sha256=local_plan.authority_sha256,
                provider=reply.provider,
                model=reply.model,
                http_status=reply.http_status,
                provider_calls=reply.attempts,
                retries=reply.automatic_retries,
                fallback="none")
            target=self.result_dir/(reply.attempt_key+".review.json")
            self.store.persist_atomic(target,record)
            self.store.read_and_validate(
                target,attempt_key=reply.attempt_key,request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,task_blob=identity.task_blob,writer_blob=identity.writer_blob,
                plan_sha256=reply.plan_sha256,authority_sha256=local_plan.authority_sha256,
                provider=reply.provider,model=reply.model)
        except self.store.PersistenceError as exc:
            raise IntegrationError("BLOCKED_REVIEW_RESULT_PERSISTENCE:"+str(exc)) from None
        return {
          "schema":"wb.openai.booster.reviewable_live_result.v2",
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
