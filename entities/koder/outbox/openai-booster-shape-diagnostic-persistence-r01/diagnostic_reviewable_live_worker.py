from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import hashlib, importlib.util, sys

WORKER_SHA256="175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3"
RESULT_INTEGRATION_SHA256="6a81a0c08ffd961e3b22d2d1de4948ebce780555cfe40b8c669e96e47cb07751"
RESULT_STORE_SHA256="cd01972b7045d4f84583fb5470d4c0012e09c12b954ea65221107eaa01385d7e"
SHAPE_STORE_SHA256="a63e02aa87961593190a5f194accd5d5beef44f564b8bb631b828010425d58e4"

class ShapeIntegrationError(RuntimeError): pass

def _load(path:Path,expected:str,name:str):
    raw=Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise ShapeIntegrationError("BLOCKED_DEPENDENCY_IDENTITY")
    s=importlib.util.spec_from_file_location(name,path)
    if s is None or s.loader is None: raise ShapeIntegrationError("BLOCKED_DEPENDENCY_IMPORT")
    m=importlib.util.module_from_spec(s); sys.modules[name]=m
    try:s.loader.exec_module(m)
    except Exception: raise ShapeIntegrationError("BLOCKED_DEPENDENCY_IMPORT") from None
    return m

@dataclass(frozen=True)
class Identity:
    task_commit:str
    task_blob:str
    writer_blob:str

class DiagnosticReviewableLiveWorker:
    def __init__(self,*,worker_path:Path,result_integration_path:Path,result_store_path:Path,
                 shape_store_path:Path,ledger_path:Path,shape_dir:Path,result_dir:Path,resolver,client):
        self.worker=_load(worker_path,WORKER_SHA256,"_diag_worker")
        self.result_integration=_load(result_integration_path,RESULT_INTEGRATION_SHA256,"_diag_result_integration")
        self.result_store=_load(result_store_path,RESULT_STORE_SHA256,"_diag_result_store")
        self.shape_store=_load(shape_store_path,SHAPE_STORE_SHA256,"_diag_shape_store")
        self.ledger_path=Path(ledger_path); self.shape_dir=Path(shape_dir); self.result_dir=Path(result_dir)
        self.resolver=resolver; self.client=client

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
            raise ShapeIntegrationError("BLOCKED_PLAN") from None

    def invoke_once_persist_shape_then_normalize(self,plan,identity:Identity,*,now_tick:int):
        local=self._local_plan(plan)
        outer=self
        class ResolverAdapter:
            def resolve(self,ref):
                try:
                    r=outer.resolver.resolve(ref)
                    return outer.worker.ResolvedSecret(r.provider,r.value)
                except Exception:
                    raise outer.worker.WorkerError("BLOCKED_CREDENTIAL_RESOLUTION") from None
        live=self.worker.LiveWorker(self.worker.DurableOneShotLedger(self.ledger_path),ResolverAdapter(),self.client)
        try:
            reply=live.invoke_once(local,now_tick=now_tick)
        except self.worker.WorkerError as exc:
            raise ShapeIntegrationError(str(exc)) from None

        shape=self.shape_store.structural_snapshot(
            body=reply.body,attempt_key=reply.attempt_key,request_sha256=reply.request_sha256,
            task_commit=identity.task_commit,task_blob=identity.task_blob,writer_blob=identity.writer_blob,
            plan_sha256=reply.plan_sha256,authority_sha256=local.authority_sha256,
            provider=reply.provider,model=reply.model,http_status=reply.http_status)
        shape_path=self.shape_dir/(reply.attempt_key+".shape.json")
        try:
            self.shape_store.persist_atomic(shape_path,shape)
            self.shape_store.read_and_validate(
                shape_path,attempt_key=reply.attempt_key,request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,task_blob=identity.task_blob,writer_blob=identity.writer_blob,
                plan_sha256=reply.plan_sha256,authority_sha256=local.authority_sha256,
                provider=reply.provider,model=reply.model)
        except self.shape_store.DiagnosticError as exc:
            raise ShapeIntegrationError("BLOCKED_SHAPE_DIAGNOSTIC_PERSISTENCE:"+str(exc)) from None

        # Current verified v2 normalizer remains unchanged and fail-closed.
        try:
            rec=self.result_store.normalize_openai_result(
                body=reply.body,attempt_key=reply.attempt_key,request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,task_blob=identity.task_blob,writer_blob=identity.writer_blob,
                plan_sha256=reply.plan_sha256,authority_sha256=local.authority_sha256,
                provider=reply.provider,model=reply.model,http_status=reply.http_status,
                provider_calls=reply.attempts,retries=reply.automatic_retries,fallback="none")
            result_path=self.result_dir/(reply.attempt_key+".review.json")
            self.result_store.persist_atomic(result_path,rec)
            self.result_store.read_and_validate(
                result_path,attempt_key=reply.attempt_key,request_sha256=reply.request_sha256,
                task_commit=identity.task_commit,task_blob=identity.task_blob,writer_blob=identity.writer_blob,
                plan_sha256=reply.plan_sha256,authority_sha256=local.authority_sha256,
                provider=reply.provider,model=reply.model)
        except self.result_store.PersistenceError as exc:
            raise ShapeIntegrationError(
                "BLOCKED_REVIEW_RESULT_PERSISTENCE_AFTER_SHAPE_SAVED:"+str(exc)+":shape="+str(shape_path)
            ) from None
        return {"status":"PASS_AFTER_SHAPE_AND_REVIEW_PERSISTENCE","attempt_key":reply.attempt_key,
                "shape_path":str(shape_path),"result_path":str(result_path),"provider_calls":1,
                "retries":0,"fallback":"none","project_acceptance":"NOT_GRANTED",
                "project_state_mutation":False}
