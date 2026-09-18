#!/usr/bin/env python3
"""Запускать локально под обычным пользователем, без сети/секретов.
python3 -I -B candidate/test_executor.py --deps deps
"""
import argparse
from dataclasses import asdict, replace
import hashlib
import json
import math
import os
from pathlib import Path
import sys
from types import ModuleType
import unittest

parser=argparse.ArgumentParser()
parser.add_argument("--deps",type=Path,default=Path(__file__).resolve().parent.parent/"deps")
args=parser.parse_args()
DEPS=args.deps.resolve(); BASE=Path(__file__).resolve().parent
if hasattr(os,"geteuid") and os.geteuid()==0:
    raise SystemExit("BLOCKED_ROOT_EXECUTION")
counters={"network_attempts":0,"process_attempts":0,"write_attempts":0,"denied_reads":0}
stdlib=Path(os.__file__).resolve().parent
deps_names={"gateway.py","policy.py","openai_adapter.py","live_transport.py",
            "orchestrator-mvp-r01.py","anthropic-provider-compatible-adapter-r01.py"}
allowed={BASE/"executor_prep.py",Path(__file__).resolve(),*(DEPS/n for n in deps_names)}
def audit(event,values):
    if event.startswith("socket."):
        counters["network_attempts"]+=1;raise RuntimeError("NETWORK_DENIED")
    if event.startswith("subprocess.") or event in {"os.system","os.exec","os.fork","os.posix_spawn"}:
        counters["process_attempts"]+=1;raise RuntimeError("PROCESS_DENIED")
    if event in {"os.remove","os.rmdir","os.mkdir","os.rename","os.chmod","os.chown",
                 "os.link","os.symlink","os.truncate"}:
        counters["write_attempts"]+=1;raise RuntimeError("WRITE_DENIED")
    if event=="open":
        name,mode,flags=values
        if type(name) is int:return
        if ((type(mode) is str and any(x in mode for x in "wax+")) or
            (type(flags) is int and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))):
            counters["write_attempts"]+=1;raise RuntimeError("WRITE_DENIED")
        path=Path(name).resolve()
        if path not in allowed and not (path.is_relative_to(stdlib) and "site-packages" not in path.parts):
            counters["denied_reads"]+=1;raise RuntimeError("READ_DENIED")
sys.addaudithook(audit)
p=ModuleType("_executor_prep_subject");p.__file__=str(BASE/"executor_prep.py");sys.modules[p.__name__]=p
exec(compile((BASE/"executor_prep.py").read_bytes(),p.__file__,"exec"),p.__dict__)
HASHES_BEFORE={name:hashlib.sha256((DEPS/name).read_bytes()).hexdigest() for name in deps_names}
SOURCE_HASH=hashlib.sha256((BASE/"executor_prep.py").read_bytes()).hexdigest()
OUTPUT="Synthetic bounded response."

class PrepTests(unittest.TestCase):
    def setUp(self):
        self.boundary=p.ExecutorPreparation(DEPS);self.g=self.boundary.g
        self.requester=self.g.Requester("KOD","coder",
            self.g.ArtifactRef("puev5691/wellbeing-hq",
                "entities/koordinator/outbox/KOO__entity-resource-gateway-live-executor-prep-r01__KOD.md",
                "b847321faad85bd0e74bdac9bfd5234d7aa23ae9","364eab08cbc98da4b59f3a69fc79e46d9d289e83"),
            self.g.ArtifactRef("puev5691/wellbeing-hq",
                "entities/koder/current/KOD__replacement-current-writer-v03.md",
                "f6686de567b4fa1906ea7cecbc5b5963fcd4e587","bfeff738de2759248307dd52433c77139624fb54"))
    def request(self,provider="openai",model=None):
        return self.g.EntityRequest("req-preparation-synthetic-001",self.requester,
            "Проверить синтетическую границу исполнителя.",provider,
            model or ("gpt-5.6-luna" if provider=="openai" else self.g.ANTHROPIC_MODEL),
            "D0_SYNTHETIC","synthetic_only",("text",),(),False,
            (self.g.SourceRef("fixture://executor/preparation",self.g.D0_SHA256),),
            self.g.D0_TEXT,self.g.AcceptancePolicy())
    def plan(self,req,policy=None):
        return self.boundary.prepare(req,p.CredentialReference(req.provider,
            "secretref:"+req.provider+":unresolved-fixture"),policy)
    def authority(self,req,plan,mode="SIMULATION"):
        # Несуществующая тестовая ссылка, не настоящая публикация разрешения.
        source=self.g.ArtifactRef("synthetic-fixture/authority",
            "tests/fixture-one-call.md","1"*40,"2"*40)
        return p.LIVE_EXECUTION_AUTHORITY(source,req.requester,req.identity,plan.identity,
            req.provider,req.model,plan.credential,plan.policy,10,30,mode)
    def verifier(self,expected):
        fingerprint=p.digest(asdict(expected))
        def verify(a,plan,now):
            if p.digest(asdict(a))!=fingerprint:return None
            return p.VerifiedAdmission(fingerprint,a.request_sha256,a.plan_sha256,
                p.digest(asdict(a.requester)),p.digest(asdict(a.source)),a.mode,a.valid_until_tick)
        return verify
    def port(self,req,*,status=200,text=OUTPUT,model=None,elapsed=0.0,failure=False):
        model=model or req.model
        if req.provider=="openai":
            body={"object":"response","id":"resp_fixture","model":model,"status":"completed",
                "output":[{"type":"message","role":"assistant",
                           "content":[{"type":"output_text","text":text}]}],
                "usage":{"input_tokens":10,"output_tokens":4,"total_tokens":14}}
        else:
            body={"id":"msg_fixture","type":"message","role":"assistant","model":model,
                "content":[{"type":"text","text":text}],"stop_reason":"end_turn",
                "stop_sequence":None,"usage":{"input_tokens":10,"output_tokens":4}}
        replay=self.g.ReplayResponse(req.identity,req.provider,status,self.g.canonical(body))
        return p.ReplayPort(replay,elapsed_seconds=elapsed,failure=failure)
    def invoke(self,req,plan=None,authority=None,port=None,**kwargs):
        plan=self.plan(req) if plan is None else plan
        authority=self.authority(req,plan) if authority is None else authority
        port=self.port(req) if port is None else port
        return self.boundary.execute_once(req,plan,mode="SIMULATION",authority=authority,
            verifier=self.verifier(authority),now_tick=10,port=port,**kwargs)
    def reject(self,code,fn):
        with self.assertRaises(p.PreparationError) as err:fn()
        self.assertEqual(str(err.exception),code)
    def test_exact_dependency_loaders(self):
        self.assertEqual(self.g.PINS,{n:p.blob((DEPS/n).read_bytes()) for n in self.g.PINS})
        self.assertEqual(p.blob((DEPS/"gateway.py").read_bytes()),p.GATEWAY_BLOB)
        self.assertEqual(p.blob((DEPS/"live_transport.py").read_bytes()),p.LIVE_TRANSPORT_BLOB)
    def test_openai_plan_matches_verified_transport(self):
        req=self.request();plan=self.plan(req);native=json.loads(plan.native_plan_json)
        self.boundary.live.validate_blueprint(native)
        self.assertEqual(native["body"]["model"],req.model)
        self.assertEqual(native["body"]["input"],req.payload)
        self.assertFalse(native["body"]["store"] or native["network_execution_enabled"])
        self.assertEqual(native["credential_ref"]["environment_variable"],"OPENAI_API_KEY")
        self.assertEqual(native["headers"],{"content-type":"application/json"})
    def test_runtime_identity_switch_secret_contract(self):
        plan=self.plan(self.request());b=dict(plan.binding)
        self.assertEqual(b["runtime_root"],"/home/pev5691/openai-d0-runtime-r01")
        self.assertEqual(b["wrapper_sha256"],p.WRAPPER_SHA256)
        self.assertEqual(b["technical_gate_commit"],p.OPENAI_FINAL_GATE)
        self.assertEqual((b["switch_name"],b["switch_value"]),("OPENAI_LIVE_D0","EXPLICIT_D0_LIVE"))
        self.assertEqual(b["preset_OPENAI_API_KEY"],"reject")
    def test_anthropic_native_plan(self):
        req=self.request("anthropic");plan=self.plan(req);native=json.loads(plan.native_plan_json)
        self.assertEqual(native["url"],"https://api.anthropic.com/v1/messages")
        self.assertEqual(native["method"],"POST")
        self.assertEqual(native["body"],{"model":req.model,"max_tokens":64,
                                       "messages":[{"role":"user","content":req.payload}]})
        self.assertFalse(native["credential_resolved"])
        self.assertEqual(native["auth_reference"],plan.credential.locator)
        self.assertEqual(dict(plan.binding)["transport_boundary"],"RequestPlan->HTTPReply")
    def test_no_live_default_before_any_executor(self):
        req=self.request();plan=self.plan(req);port=self.port(req)
        self.reject("BLOCKED_NO_LIVE_DEFAULT",lambda:self.boundary.execute_once(req,plan,port=port))
        self.assertEqual(port.calls,0)
    def test_missing_authority_no_attempt(self):
        req=self.request();plan=self.plan(req);port=self.port(req)
        self.reject("BLOCKED_LIVE_EXECUTION_AUTHORITY",lambda:self.boundary.execute_once(
            req,plan,mode="SIMULATION",port=port,now_tick=10))
        self.assertEqual(port.calls,0)
    def test_missing_verifier_no_attempt(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan);port=self.port(req)
        self.reject("BLOCKED_AUTHORITY_UNVERIFIED",lambda:self.boundary.execute_once(
            req,plan,mode="SIMULATION",authority=a,port=port,now_tick=10))
        self.assertEqual(port.calls,0)
    def test_false_boolean_exception_or_nonbool_verifier(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        def broken(*_):raise RuntimeError("DO_NOT_ECHO_DIAGNOSTIC")
        for verify in (lambda *_:True,lambda *_:1,lambda *_:None,broken):
            self.reject("BLOCKED_AUTHORITY_UNVERIFIED",lambda:self.boundary.execute_once(
                req,plan,mode="SIMULATION",authority=a,verifier=verify,now_tick=10,port=self.port(req)))
    def test_authority_binding_all_fields(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        variants={"request_sha256":"0"*64,"plan_sha256":"0"*64,"provider":"anthropic",
                  "model":"other","data_class":"D1_PROJECT",
                  "credential":p.CredentialReference("openai","secretref:openai:other"),
                  "policy":p.ExecutionPolicy(timeout_seconds=15),
                  "requester":replace(req.requester,role="other")}
        for key,value in variants.items():
            with self.subTest(key=key):
                bad=replace(a,**{key:value})
                self.reject("BLOCKED_AUTHORITY_BINDING",lambda:self.boundary.execute_once(
                    req,plan,mode="SIMULATION",authority=bad,verifier=self.verifier(bad),
                    now_tick=10,port=self.port(req)))
    def test_changed_request_entity_role_task_writer_purpose_sources(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        variants=[replace(req,purpose="Другая подзадача."),
                  replace(req,requester=replace(req.requester,entity_id="LIB")),
                  replace(req,requester=replace(req.requester,role="other")),
                  replace(req,requester=replace(req.requester,task=replace(req.requester.task,blob="0"*40))),
                  replace(req,requester=replace(req.requester,writer=replace(req.requester.writer,commit="0"*40))),
                  replace(req,sources=(self.g.SourceRef("fixture://different",self.g.D0_SHA256),))]
        for bad in variants:
            self.reject("BLOCKED_PLAN_BINDING",lambda:self.boundary.execute_once(
                bad,plan,mode="SIMULATION",authority=a,verifier=self.verifier(a),now_tick=10,port=self.port(req)))
    def test_non_authority_kind_or_mode(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        self.reject("BLOCKED_LIVE_EXECUTION_AUTHORITY",lambda:self.invoke(
            req,plan,replace(a,kind="merely-a-plan")))
        self.reject("BLOCKED_AUTHORITY_MODE",lambda:self.invoke(req,plan,replace(a,mode="LIVE")))
    def test_expiry_and_not_before(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        for now in (9,30,31):
            self.reject("BLOCKED_AUTHORITY_EXPIRED",lambda:self.boundary.execute_once(
                req,plan,mode="SIMULATION",authority=a,verifier=self.verifier(a),now_tick=now,port=self.port(req)))
        self.reject("BLOCKED_AUTHORITY_TIME",lambda:self.boundary.execute_once(
            req,plan,mode="SIMULATION",authority=a,now_tick=True))
    def test_bad_source_or_multi_call_budget(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        self.reject("BLOCKED_AUTHORITY_SOURCE",lambda:self.invoke(
            req,plan,replace(a,source=replace(a.source,commit="main"))))
        for calls in (0,2,True):
            self.reject("BLOCKED_AUTHORITY_BUDGET",lambda:self.invoke(req,plan,replace(a,max_calls=calls)))
    def test_expired_or_mismatched_attestation(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        good=self.verifier(a)(a,plan,10)
        for key,val in (("authority_sha256","0"*64),("requester_sha256","0"*64),
                        ("decision_source_sha256","0"*64),("mode","LIVE"),("valid_until_tick",10),
                        ("valid_until_tick",31),("valid_until_tick",True)):
            self.reject("BLOCKED_AUTHORITY_UNVERIFIED",lambda:self.boundary.execute_once(req,plan,
                mode="SIMULATION",authority=a,verifier=lambda *_:replace(good,**{key:val}),
                now_tick=10,port=self.port(req)))
    def test_three_openai_models_simulated(self):
        for n,model in enumerate(sorted(self.boundary.modules["policy.py"].MODELS)):
            req=self.request(model=model);plan=self.plan(req);a=self.authority(req,plan)
            a=replace(a,source=replace(a.source,path=f"tests/call-{n}.md"))
            res=self.invoke(req,plan,a)
            self.assertIs(type(res),self.g.ResourceResult)
            self.assertEqual((res.provider_used,res.model_used),("openai",model))
            self.assertEqual(res.payload,OUTPUT)
    def test_anthropic_simulated(self):
        req=self.request("anthropic");res=self.invoke(req)
        self.assertIs(type(res),self.g.ResourceResult)
        self.assertEqual(res.model_used,req.model)
        self.assertEqual(res.payload,OUTPUT)
    def test_result_acceptance_authority_and_original_request(self):
        req=self.request();original=self.g.canonical(asdict(req));res=self.invoke(req)
        self.assertEqual(res.project_acceptance,"NOT_GRANTED")
        self.assertEqual(res.execution_mode,"synthetic_no_network")
        self.assertEqual(res.routing_status,"not_started")
        self.assertFalse(any((res.caller_writer_changed,res.provider_writer_authority,
                             res.gateway_writer_authority,res.project_state_applied,res.external_dispatch_performed)))
        self.assertEqual(self.g.canonical(asdict(req)),original)
        self.assertTrue(self.g.verify_result(res,req,res.identity))
    def test_same_authority_no_second_attempt(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan);port=self.port(req)
        self.invoke(req,plan,a,port)
        self.reject("BLOCKED_AUTHORITY_ALREADY_CONSUMED",lambda:self.invoke(req,plan,a,port))
        self.assertEqual(port.calls,1)
    def test_shared_ledger_budget_across_boundaries(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan);self.invoke(req,plan,a)
        ledger=self.boundary.ledger
        self.boundary=p.ExecutorPreparation(DEPS,ledger);self.g=self.boundary.g
        # Новый экземпляр типов: восстановить тот же проверочный requester без наследования класса.
        old=asdict(req.requester)
        self.requester=self.g.Requester(old["entity_id"],old["role"],
            self.g.ArtifactRef(**old["task"]),self.g.ArtifactRef(**old["writer"]))
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        self.reject("BLOCKED_AUTHORITY_ALREADY_CONSUMED",lambda:self.invoke(req,plan,a))
    def test_timeout_consumes_authority_without_retry(self):
        req=self.request();plan=self.plan(req,p.ExecutionPolicy(timeout_seconds=1))
        a=self.authority(req,plan);port=self.port(req,elapsed=1.0)
        res=self.invoke(req,plan,a,port)
        self.assertEqual(res.blocker,"BLOCKED_EXECUTION_TIMEOUT")
        self.assertEqual(res.payload,"")
        self.reject("BLOCKED_AUTHORITY_ALREADY_CONSUMED",lambda:self.invoke(req,plan,a,port))
        self.assertEqual(port.calls,1)
    def test_failure_consumes_authority_without_diagnostic_echo(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan);port=self.port(req,failure=True)
        res=self.invoke(req,plan,a,port)
        self.assertEqual(res.blocker,"BLOCKED_EXECUTOR_FAILURE")
        self.assertNotIn("UNTRUSTED_EXECUTOR_DIAGNOSTIC",res.to_bytes().decode())
        self.reject("BLOCKED_AUTHORITY_ALREADY_CONSUMED",lambda:self.invoke(req,plan,a,port))
    def test_http_error_is_not_retried(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan);port=self.port(req,status=429)
        res=self.invoke(req,plan,a,port)
        self.assertEqual(res.technical_status,"blocked")
        self.assertEqual(port.calls,1)
        self.reject("BLOCKED_AUTHORITY_ALREADY_CONSUMED",lambda:self.invoke(req,plan,a,port))
    def test_response_model_mismatch(self):
        req=self.request();res=self.invoke(req,port=self.port(req,model="wrong-model"))
        self.assertEqual(res.blocker,"BLOCKED_MODEL_UNAVAILABLE")
        self.assertEqual(res.payload,"")
    def test_result_acceptance_hash_preserved(self):
        req=replace(self.request(),acceptance=self.g.AcceptancePolicy(expected_output_sha256="0"*64))
        res=self.invoke(req)
        self.assertEqual(res.blocker,"BLOCKED_RESULT_CHECK")
        self.assertEqual(res.project_acceptance,"NOT_GRANTED")
    def test_credentials_never_resolved(self):
        def forbidden(*_,**__):raise AssertionError("CREDENTIAL_OR_LIVE_FUNCTION_USED")
        self.boundary.live.EnvironmentSecretReader.read=forbidden
        self.boundary.live.InjectedSecretReader.read=forbidden
        self.boundary.live.UrllibExecutor.request=forbidden
        self.boundary.live.OpenAIResponsesLiveTransport.run_live=forbidden
        res=self.invoke(self.request())
        self.assertEqual(res.technical_status,"completed")
        self.assertNotIn("secretref:",res.to_bytes().decode())
    def test_credential_reference_only(self):
        for val in ("NOT_A_REFERENCE","Bearer TEST_SENTINEL","secretref:anthropic:slot",
                    "secretref:openai:slot\n","secretref:openai:"):
            self.reject("BLOCKED_CREDENTIAL_REFERENCE",lambda:p.CredentialReference("openai",val))
        cred=p.CredentialReference("openai","secretref:openai:unresolved")
        self.assertNotIn(cred.locator,repr(cred))
    def test_policy_finite_bounds_and_zero_retry(self):
        for timeout in (0,61,float("nan"),float("inf"),True,"30"):
            self.reject("BLOCKED_TIMEOUT_POLICY",lambda:p.ExecutionPolicy(timeout_seconds=timeout))
        for kw in ({"max_attempts":2},{"automatic_retries":1},{"max_attempts":True}):
            self.reject("BLOCKED_RETRY_POLICY",lambda:p.ExecutionPolicy(**kw))
        for size in (0,65537,True):
            self.reject("BLOCKED_RESPONSE_BOUND",lambda:p.ExecutionPolicy(max_response_bytes=size))
    def test_privacy_tools_payload_and_external_send_unchanged(self):
        req=self.request()
        for kw in ({"payload":"UNAPPROVED_PAYLOAD"},{"privacy_class":"private"},{"data_class":"D1_PROJECT"},
                   {"tools":("shell",)},{"external_send_allowed":True},{"capabilities":("web",)}):
            self.reject("BLOCKED_REQUEST_POLICY",lambda:self.plan(replace(req,**kw)))
    def test_unknown_model_and_provider_no_fallback(self):
        for provider in ("openai","anthropic"):
            req=self.request(provider,model="unknown")
            self.reject("BLOCKED_MODEL_UNAVAILABLE",lambda:self.plan(req))
        req=replace(self.request(),provider="google")
        self.reject("BLOCKED_CREDENTIAL_REFERENCE",lambda:self.boundary.prepare(
            req,p.CredentialReference("openai","secretref:openai:slot")))
    def test_plan_tamper_rejected(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        for bad in (replace(plan,native_plan_json="{}"),replace(plan,binding=()),
                    replace(plan,request_sha256="0"*64)):
            self.reject("BLOCKED_PLAN_BINDING",lambda:self.invoke(req,bad,a))
    def test_wrong_replay_or_arbitrary_executor(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan)
        self.reject("BLOCKED_NONNETWORK_PORT_REQUIRED",lambda:self.invoke(req,plan,a,object()))
        port=self.port(req);port.reply=replace(port.reply,request_sha256="0"*64)
        self.reject("BLOCKED_REPLAY_BINDING",lambda:self.invoke(req,plan,a,port))
        self.assertEqual(self.boundary.ledger.count,0)
    def test_response_limit_before_attempt(self):
        req=self.request();plan=self.plan(req,p.ExecutionPolicy(max_response_bytes=1))
        a=self.authority(req,plan);port=self.port(req)
        self.reject("BLOCKED_REPLAY_BINDING",lambda:self.invoke(req,plan,a,port))
        self.assertEqual(port.calls,0)
    def test_live_flag_not_enough_even_with_valid_simulation(self):
        req=self.request();plan=self.plan(req);a=self.authority(req,plan);port=self.port(req)
        self.reject("BLOCKED_AUTHORITY_MODE",lambda:self.boundary.execute_once(req,plan,mode="LIVE",
            authority=a,verifier=self.verifier(a),now_tick=10,port=port,live_switch="EXPLICIT_D0_LIVE"))
        self.assertEqual(port.calls,0)
    def test_live_no_switch_and_no_installed_port(self):
        for provider in ("openai","anthropic"):
            req=self.request(provider);plan=self.plan(req);a=self.authority(req,plan,"LIVE");port=self.port(req)
            if provider=="openai":
                self.reject("BLOCKED_OPENAI_LIVE_SWITCH",lambda:self.boundary.execute_once(req,plan,mode="LIVE",
                    authority=a,verifier=self.verifier(a),now_tick=10,port=port))
            self.reject("BLOCKED_LIVE_ATTACHMENT_REQUIRED",lambda:self.boundary.execute_once(req,plan,mode="LIVE",
                authority=a,verifier=self.verifier(a),now_tick=10,port=port,live_switch="EXPLICIT_D0_LIVE"))
            self.assertEqual(port.calls,0)
            self.assertEqual(self.boundary.ledger.count,0)
    def test_port_can_not_elevate_live_authority(self):
        class EvilPort:
            network_capable=True
            calls=0
            def invoke_once(self,*_):
                self.calls+=1;raise AssertionError("SHOULD_NOT_RUN")
        req=self.request();plan=self.plan(req);a=self.authority(req,plan,"LIVE");port=EvilPort()
        self.reject("BLOCKED_LIVE_ATTACHMENT_REQUIRED",lambda:self.boundary.execute_once(req,plan,mode="LIVE",
            authority=a,verifier=self.verifier(a),now_tick=10,port=port,live_switch="EXPLICIT_D0_LIVE"))
        self.assertEqual(port.calls,0)
    def test_unknown_mode_closed(self):
        self.reject("BLOCKED_EXECUTION_MODE",lambda:self.boundary.execute_once(self.request(),None,mode="AUTO"))
    def test_preparation_determinism_and_redaction(self):
        req=self.request();a=self.plan(req);b=self.plan(req)
        self.assertEqual(a.identity,b.identity)
        self.assertNotIn(req.payload,repr(a))
        self.assertNotIn("secretref:",json.dumps(a.redacted()))
        self.assertFalse(a.redacted()["live_enabled"])
    def test_upstream_checks_without_real_transport(self):
        mvp=self.boundary.modules["orchestrator-mvp-r01.py"]
        ant=self.boundary.modules["anthropic-provider-compatible-adapter-r01.py"]
        self.assertEqual(mvp.self_test()["count"],7)
        self.assertEqual(ant.self_test(mvp)["assertions"],231)
    def test_dependencies_and_candidate_unchanged(self):
        self.assertEqual(HASHES_BEFORE,{name:hashlib.sha256((DEPS/name).read_bytes()).hexdigest() for name in deps_names})
        self.assertEqual(SOURCE_HASH,hashlib.sha256((BASE/"executor_prep.py").read_bytes()).hexdigest())
        self.assertFalse(any(counters.values()))

if __name__=="__main__":
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(PrepTests))
    good=result.wasSuccessful() and not any(counters.values())
    print(json.dumps({"verdict":p.PASS if good else "FAIL_EXECUTOR_PREPARATION_TESTS",
        "test_methods":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),
        "skipped":len(result.skipped),"operation_counters":counters,
        "uid":os.geteuid(),"provider_api_calls":0,"credential_reads":0,
        "live_executor_installed":False,"upstream_mvp_checks":7,"upstream_anthropic_assertions":231,
        "review":"pending_independent_verify"},sort_keys=True))
    raise SystemExit(0 if good else 1)
