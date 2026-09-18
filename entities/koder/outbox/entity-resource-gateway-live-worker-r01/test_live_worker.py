#!/usr/bin/env python3
import hashlib,json,os,signal,sqlite3,tempfile,threading,time,unittest
from dataclasses import dataclass, asdict
from pathlib import Path
from types import ModuleType,SimpleNamespace
import sys
if hasattr(os,"geteuid") and os.geteuid()==0: raise SystemExit("BLOCKED_ROOT_EXECUTION")
BASE=Path(__file__).resolve().parent
m=ModuleType("_live_worker_subject");m.__file__=str(BASE/"live_worker.py");sys.modules[m.__name__]=m
exec(compile((BASE/"live_worker.py").read_bytes(),m.__file__,"exec"),m.__dict__)
SECRET="".join(["TEST","_NON","SECRET"])
def h(x): return hashlib.sha256(x.encode()).hexdigest()
class Resolver:
    def __init__(self): self.calls=0; self.refs=[]
    def resolve(self,ref):
        self.calls+=1;self.refs.append(ref.locator);return m.ResolvedSecret(ref.provider,SECRET)
class Client:
    def __init__(self,status=200,body=None,delay=0): self.calls=0;self.status=status;self.body=body;self.delay=delay;self.auth_seen=False
    def request(self,**kw):
        self.calls+=1
        self.auth_seen=kw["headers"].get("authorization","").endswith(SECRET)
        if self.delay: time.sleep(self.delay)
        return self.status,self.body if self.body is not None else json.dumps({"model":"gpt-5.6-luna"}).encode()
def op_plan(model="gpt-5.6-luna"):
    native={"method":"POST","url":m.OPENAI_URL,"headers":{"content-type":"application/json"},
            "body":{"model":model,"input":"Synthetic bounded request.","max_output_tokens":64,"store":False,"tools":[],"tool_choice":"none","parallel_tool_calls":False},
            "credential_ref":{"source":"environment","environment_variable":"OPENAI_API_KEY"},"network_execution_enabled":False,
            "transport_mode":"mock_only","request_hash":"0"*64}
    return m.WorkerPlan(h("req"),h("plan"),h("auth"),h("requester"),"openai",model,json.dumps(native),
                        m.SecretRef("openai","secretref:openai:test-slot"),m.WorkerPolicy(),100)
def an_plan(model="synthetic-model-for-contract-test"):
    native={"method":"POST","url":m.ANTHROPIC_URL,"headers":[["anthropic-version","2023-06-01"],["content-type","application/json"]],
            "body":{"model":model,"max_tokens":64,"messages":[{"role":"user","content":"Synthetic bounded request."}]},
            "auth_header":"Authorization","auth_prefix":"Bearer ","auth_reference":"secretref:anthropic:test-slot","credential_resolved":False}
    return m.WorkerPlan(h("req2"),h("plan2"),h("auth2"),h("requester2"),"anthropic",model,json.dumps(native),
                        m.SecretRef("anthropic","secretref:anthropic:test-slot"),m.WorkerPolicy(),100)
class T(unittest.TestCase):
    def ledger(self): 
        d=tempfile.TemporaryDirectory(); self.addCleanup(d.cleanup); return m.DurableOneShotLedger(Path(d.name)/"ledger.sqlite")
    def worker(self,plan,client=None):
        r=Resolver();c=client or Client(body=json.dumps({"model":plan.model}).encode());return m.LiveWorker(self.ledger(),r,c),r,c
    def test_openai_success(self):
        p=op_plan();w,r,c=self.worker(p);x=w.invoke_once(p,now_tick=1);self.assertEqual((x.provider,x.model,x.project_acceptance),("openai",p.model,"NOT_GRANTED"));self.assertTrue(c.auth_seen);self.assertEqual(r.calls,1)
    def test_anthropic_success(self):
        p=an_plan();w,r,c=self.worker(p,Client(body=json.dumps({"model":p.model}).encode()));x=w.invoke_once(p,now_tick=1);self.assertEqual(x.model,p.model);self.assertTrue(c.auth_seen)
    def test_restart_safe_duplicate(self):
        d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);path=Path(d.name)/"x.sqlite";p=op_plan();r=Resolver();c=Client()
        m.LiveWorker(m.DurableOneShotLedger(path),r,c).invoke_once(p,now_tick=1)
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_DUPLICATE_CALL"):m.LiveWorker(m.DurableOneShotLedger(path),r,Client()).invoke_once(p,now_tick=1)
    def test_atomic_competing_claim(self):
        d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);path=Path(d.name)/"x.sqlite";key=h("k");out=[]
        def f():
            try:m.DurableOneShotLedger(path).claim(key,h("r"),h("p"),h("a"));out.append("ok")
            except m.WorkerError as e:out.append(str(e))
        a=threading.Thread(target=f);b=threading.Thread(target=f);a.start();b.start();a.join();b.join()
        self.assertEqual(sorted(out),["BLOCKED_DUPLICATE_CALL","ok"])
    def test_hard_timeout(self):
        p=op_plan();p=m.WorkerPlan(p.request_sha256,p.plan_sha256,h("timeout"),p.requester_sha256,p.provider,p.model,p.native_plan_json,p.secret_ref,m.WorkerPolicy(timeout_seconds=1),p.valid_until_tick)
        w,r,c=self.worker(p,Client(delay=2))
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_HARD_TIMEOUT"):w.invoke_once(p,now_tick=1)
        self.assertEqual(c.calls,1)
    def test_oversize(self):
        p=op_plan();p=m.WorkerPlan(p.request_sha256,h("small"),h("over"),p.requester_sha256,p.provider,p.model,p.native_plan_json,p.secret_ref,m.WorkerPolicy(max_response_bytes=8),100)
        w,_,c=self.worker(p,Client(body=b"x"*9))
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_RESPONSE_TOO_LARGE"):w.invoke_once(p,now_tick=1)
        self.assertEqual(c.calls,1)
    def test_redirect(self):
        p=op_plan();w,_,c=self.worker(p,Client(status=302,body=b""))
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_REDIRECT"):w.invoke_once(p,now_tick=1)
    def test_model_mismatch(self):
        p=op_plan();w,_,_=self.worker(p,Client(body=json.dumps({"model":"wrong"}).encode()))
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_MODEL_MISMATCH"):w.invoke_once(p,now_tick=1)
    def test_stale(self):
        p=op_plan();w,_,c=self.worker(p)
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_STALE_AUTHORITY"):w.invoke_once(p,now_tick=100)
        self.assertEqual(c.calls,0)
    def test_bad_endpoint(self):
        p=op_plan();o=json.loads(p.native_plan_json);o["url"]="https://example.invalid"
        p=m.WorkerPlan(p.request_sha256,p.plan_sha256,p.authority_sha256,p.requester_sha256,p.provider,p.model,json.dumps(o),p.secret_ref,p.policy,100)
        w,_,c=self.worker(p)
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_ENDPOINT_BINDING"):w.invoke_once(p,now_tick=1)
        self.assertEqual(c.calls,0)
    def test_bad_model_binding(self):
        p=op_plan();o=json.loads(p.native_plan_json);o["body"]["model"]="other"
        p=m.WorkerPlan(p.request_sha256,p.plan_sha256,p.authority_sha256,p.requester_sha256,p.provider,p.model,json.dumps(o),p.secret_ref,p.policy,100)
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_MODEL_BINDING"):m.parse_native(p)
    def test_secret_ref_only_and_redaction(self):
        p=op_plan();self.assertNotIn("secretref:",repr(p));w,r,c=self.worker(p);x=w.invoke_once(p,now_tick=1)
        dump=json.dumps(x.redacted());self.assertNotIn(SECRET,dump);self.assertNotIn("secretref:",dump);self.assertEqual(r.refs,["secretref:openai:test-slot"])
    def test_bad_secret_ref(self):
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_CREDENTIAL_REF"):m.SecretRef("openai","raw-key")
    def test_no_retry_on_429(self):
        p=op_plan();w,_,c=self.worker(p,Client(status=429,body=b"{}"));x=w.invoke_once(p,now_tick=1);self.assertEqual(x.http_status,429);self.assertEqual(c.calls,1);self.assertEqual(x.automatic_retries,0)
    def test_no_retry_after_error(self):
        p=op_plan();w,_,c=self.worker(p,Client(status=500,body=b"{}"));x=w.invoke_once(p,now_tick=1);self.assertEqual(c.calls,1);self.assertEqual(x.http_status,500)
    def test_fail_closed_redirect_handler(self): self.assertIsNone(m.FailClosedRedirect().redirect_request(None,None,None,None,None,None))
    def test_resource_boundary(self):
        ok=SimpleNamespace(project_acceptance="NOT_GRANTED",caller_writer_changed=False,project_state_applied=False,external_dispatch_performed=False,gateway_writer_authority=False,provider_writer_authority=False,routing_status="not_started")
        self.assertIs(m.enforce_resource_result_boundary(ok),ok)
        with self.assertRaisesRegex(m.WorkerError,"FAIL_RESOURCE_RESULT_AUTHORITY"):m.enforce_resource_result_boundary(SimpleNamespace(**{**ok.__dict__,"project_acceptance":"GRANTED"}))
    def test_bind_prepared_exact(self):
        @dataclass(frozen=True)
        class R: entity_id:str="KOD"; role:str="coder"
        cred=SimpleNamespace(provider="openai",locator="secretref:openai:test-slot")
        pol=SimpleNamespace(timeout_seconds=30,max_response_bytes=65536,max_attempts=1,automatic_retries=0)
        prepared=SimpleNamespace(live_enabled=False,request_sha256=h("req"),identity=h("plan"),requester=R(),provider="openai",model="gpt-5.6-luna",credential=cred,policy=pol,native_plan_json=op_plan().native_plan_json)
        admission=SimpleNamespace(mode="LIVE",request_sha256=prepared.request_sha256,plan_sha256=prepared.identity,requester_sha256=m.sha(asdict(prepared.requester)),authority_sha256=h("auth"),valid_until_tick=50)
        wp=m.bind_prepared(prepared,admission,now_tick=1);self.assertEqual((wp.provider,wp.model),(prepared.provider,prepared.model))
    def test_bind_rejects_simulation(self):
        @dataclass(frozen=True)
        class R: entity_id:str="KOD"; role:str="coder"
        prepared=SimpleNamespace(live_enabled=False,request_sha256=h("r"),identity=h("p"),requester=R(),provider="openai",model="gpt-5.6-luna",credential=SimpleNamespace(locator="secretref:openai:x"),policy=SimpleNamespace(timeout_seconds=30,max_response_bytes=10,max_attempts=1,automatic_retries=0),native_plan_json=op_plan().native_plan_json)
        admission=SimpleNamespace(mode="SIMULATION",request_sha256=prepared.request_sha256,plan_sha256=prepared.identity,requester_sha256=m.sha(asdict(prepared.requester)),authority_sha256=h("a"),valid_until_tick=50)
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_AUTHORITY_MODE"):m.bind_prepared(prepared,admission,now_tick=1)
    def test_policy_no_retries(self):
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_RETRY_POLICY"):m.WorkerPolicy(max_calls=2)
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_RETRY_POLICY"):m.WorkerPolicy(automatic_retries=1)
    def test_timeout_bounds(self):
        for v in (0,61,float("nan"),True):
            with self.assertRaises(m.WorkerError):m.WorkerPolicy(timeout_seconds=v)
    def test_response_limit_bounds(self):
        for v in (0,65537,True):
            with self.assertRaises(m.WorkerError):m.WorkerPolicy(max_response_bytes=v)
    def test_sqlite_row_consumed_before_resolve_failure(self):
        class Bad: 
            def resolve(self,_): raise RuntimeError("secret-ish")
        d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);ledger=m.DurableOneShotLedger(Path(d.name)/"x.sqlite");p=op_plan()
        with self.assertRaisesRegex(m.WorkerError,"BLOCKED_CREDENTIAL_RESOLUTION"):m.LiveWorker(ledger,Bad(),Client()).invoke_once(p,now_tick=1)
        self.assertEqual(ledger.count(),1)
    def test_no_secret_in_reply_repr(self):
        p=op_plan();x=self.worker(p)[0].invoke_once(p,now_tick=1);self.assertNotIn(SECRET,repr(x));self.assertNotIn(SECRET,json.dumps(x.redacted()))
    def test_worker_reply_invariants(self):
        p=op_plan();x=self.worker(p)[0].invoke_once(p,now_tick=1);self.assertEqual(x.project_acceptance,"NOT_GRANTED");self.assertFalse(x.caller_writer_changed or x.project_state_applied or x.external_dispatch_performed)
    def test_concrete_client_class_not_used(self):
        self.assertEqual(m.BoundedUrllibClient.calls,0)
    def test_zero_network_by_monkeypatch(self):
        import socket
        old=socket.socket
        def deny(*a,**k): raise AssertionError("NETWORK_FORBIDDEN")
        socket.socket=deny
        try:
            p=op_plan();x=self.worker(p)[0].invoke_once(p,now_tick=1);self.assertEqual(x.http_status,200)
        finally: socket.socket=old

if __name__=="__main__":
    r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
    print(json.dumps({"verdict":m.PASS if r.wasSuccessful() else "FAIL_LIVE_WORKER_TESTS","test_methods":r.testsRun,"failures":len(r.failures),"errors":len(r.errors),"skipped":len(r.skipped),"real_provider_calls":0,"real_credential_reads":0,"production":False,"uid":os.geteuid()},sort_keys=True))
    raise SystemExit(0 if r.wasSuccessful() else 1)
