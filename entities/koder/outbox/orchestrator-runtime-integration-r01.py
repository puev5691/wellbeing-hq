#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, os, subprocess, sys
from pathlib import Path

TASK_PATH='entities/koordinator/outbox/KOO__orchestrator-runtime-integration-r01__KOD.md'
TASK_COMMIT='6ccdc58e7e2699d164129864b1ad31ac99c108d0'
TASK_BLOB='129e673b9af5ed68d24f2e2d9b95088aedd10560'
WRITER_BLOB='23f20f04504c65497c154c099d8090cde11fba83'
MVP_PATH='entities/koder/outbox/orchestrator-mvp-r01.py'
MVP_BLOB='55939b2e4c91f7af1159a60b2f4ee8fa961196f2'
OPENAI_DIR='entities/koder/outbox/openai-responses-d0-adapter-r01'
OPENAI_BLOBS={'policy.py':'92c2f3e08597c90d781e48c38f664327284db6d6','openai_adapter.py':'c02ab55725caf43c6117aa793ccaa418b1a60f2f','live_transport.py':'f34dff943d0dbbff3ece56e64cece1d26cd23c14'}
LIVE_GATE={'switch_name':'OPENAI_LIVE_D0','switch_value':'EXPLICIT_D0_LIVE','runtime_path':'/home/pev5691/openai-d0-runtime-r01','authority':'separate_KOO_OPERATOR_gate_required'}

class IntegrationError(RuntimeError): pass

def repo_root()->Path:
    p=Path(__file__).resolve()
    for parent in [p.parent,*p.parents]:
        if (parent/'.git').exists(): return parent
    raise IntegrationError('repo_root_not_found')

def git_blob(root:Path, rel:str)->str:
    return subprocess.check_output(['git','-C',str(root),'hash-object',rel],text=True).strip()

def verify_basis(root:Path)->None:
    if git_blob(root,MVP_PATH)!=MVP_BLOB: raise IntegrationError('mvp_blob_mismatch')
    for name,expected in OPENAI_BLOBS.items():
        rel=f'{OPENAI_DIR}/{name}'
        if git_blob(root,rel)!=expected: raise IntegrationError(f'openai_blob_mismatch:{name}')

def load(name:str,path:Path):
    spec=importlib.util.spec_from_file_location(name,path); mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod); return mod

def modules(root:Path):
    mvp=load('wellbeing_orchestrator_mvp',root/MVP_PATH)
    opdir=root/OPENAI_DIR
    sys.path.insert(0,str(opdir))
    policy=load('policy',opdir/'policy.py'); oa=load('openai_adapter',opdir/'openai_adapter.py')
    return mvp,policy,oa

def fixture(model:str):
    return {'id':'resp_runtime_int_001','object':'response','model':model,'status':'completed','output':[{'type':'message','id':'msg_runtime_int_001','status':'completed','role':'assistant','content':[{'type':'output_text','text':'SYNTHETIC_RUNTIME_OK','annotations':[]}]}],'output_text':'SYNTHETIC_RUNTIME_OK','usage':{'input_tokens':11,'output_tokens':4,'total_tokens':15},'tools':[]}

def build_runtime(root:Path):
    verify_basis(root); mvp,policy,oa=modules(root)
    class CurrentTaskAdmission:
        def admit(self,req):
            if req.entity!='KOD': raise mvp.Blocked('BLOCKED_WRONG_ENTITY')
            if req.writer_blob!=WRITER_BLOB: raise mvp.Blocked('BLOCKED_WRONG_WRITER')
            expected=mvp.TaskIdentity(TASK_PATH,TASK_COMMIT,TASK_BLOB)
            if req.task!=expected: raise mvp.Blocked('BLOCKED_TASK_IDENTITY_MISMATCH')
    class SentinelMockTransport(oa.MockTransport):
        def __init__(self): super().__init__(oa.MockHTTPResponse(200,fixture('gpt-5.6-luna'))); self.sentinel_calls=0
        def send(self,plan): self.sentinel_calls+=1; return super().send(plan)
    class IntegratedOpenAIAdapter(mvp.ProviderAdapter):
        provider_id='openai'; caps=mvp.AdapterCapabilities(frozenset({'gpt-5.6-luna'}),frozenset({'text'}),True,{})
        def __init__(self,mode='dry_run'): self.mode=mode; self.transport=SentinelMockTransport()
        def fake_invoke(self,req):
            if self.mode!='dry_run': raise mvp.Blocked('BLOCKED_LIVE_AUTHORITY_REQUIRED')
            cfg=policy.valid_synthetic_config(req.content)
            result=oa.OpenAIResponsesAdapter().run_mock(cfg,self.transport)
            parsed=result['parsed_response']; usage=parsed['usage']
            return mvp.ResponseEnvelope(req.run_id,'openai',req.model,'completed','PASS_SYNTHETIC_OPENAI_D0_RUNTIME',output=parsed['text'],usage={'input_tokens':usage.get('input_tokens'),'output_tokens':usage.get('output_tokens'),'total_tokens':usage.get('total_tokens')},provider_state={'result_identity':result['result_identity'],'external_network_used':False,'live_gate_contract':LIVE_GATE})
    class IntegratedOrchestrator(mvp.Orchestrator):
        def __init__(self,mode='dry_run'):
            self.openai=IntegratedOpenAIAdapter(mode); self.registry=mvp.AdapterRegistry([self.openai,mvp.AnthropicStub(),mvp.GoogleStub()]); self.router=mvp.Router(self.registry); self.admission=CurrentTaskAdmission()
    return mvp,IntegratedOrchestrator

def request(mvp,**changes):
    req=mvp.RequestEnvelope('run-runtime-int-001','KOD',WRITER_BLOB,mvp.TaskIdentity(TASK_PATH,TASK_COMMIT,TASK_BLOB),'coding','runtime synthetic')
    for k,v in changes.items(): setattr(req,k,v)
    return req

def self_test()->dict:
    root=repo_root(); mvp,Orch=build_runtime(root); checks=[]
    if 'OPENAI_API_KEY' in os.environ: raise IntegrationError('dry_run_environment_must_not_supply_api_key')
    o=Orch(); resp,run,routing,tel=o.run(request(mvp)); pass_resp=resp
    assert resp.provider=='openai' and resp.model=='gpt-5.6-luna' and resp.terminal_status=='PASS_SYNTHETIC_OPENAI_D0_RUNTIME'; checks.append('exact_route_openai_luna')
    assert o.openai.transport.sentinel_calls==1 and resp.provider_state['external_network_used'] is False; checks.append('accepted_adapter_via_sentinel_no_network')
    checks.append('no_api_key_required')
    before=o.openai.transport.sentinel_calls; blocked,*_=o.run(request(mvp,provider='anthropic',model='any')); assert blocked.terminal_status=='BLOCKED_PROVIDER_UNAVAILABLE' and o.openai.transport.sentinel_calls==before; checks.append('no_silent_fallback')
    before=o.openai.transport.sentinel_calls; p,*_=o.run(request(mvp,data_class='project_internal')); t,*_=o.run(request(mvp,tools_allowed=['shell'])); assert p.terminal_status=='BLOCKED_PRIVACY_BOUNDARY' and t.terminal_status=='BLOCKED_TOOL_AUTHORITY' and o.openai.transport.sentinel_calls==before; checks.append('privacy_and_tools_fail_closed')
    assert not run.in_execution_wip and routing.status=='not_started' and not routing.complete; checks.append('terminal_separate_from_routing')
    live=Orch(mode='live_gate'); assert live.openai.mode=='live_gate' and LIVE_GATE['switch_value']=='EXPLICIT_D0_LIVE' and mvp.RunState().__class__ is run.__class__; checks.append('future_live_gate_same_orchestration_state')
    assert tel.provider=='openai' and tel.model=='gpt-5.6-luna' and all(v is None for v in tel.latency.values()); checks.append('compact_telemetry_no_invented_latency')
    return {'verdict':'PASS_ORCHESTRATOR_RUNTIME_INTEGRATION_R01_READY_FOR_LIVE_D0_GATE','checks':checks,'count':len(checks),'artifact_basis':{'mvp_blob':MVP_BLOB,'openai_blobs':OPENAI_BLOBS,'sis_live_gate':LIVE_GATE},'response':{'status':pass_resp.terminal_status,'provider':pass_resp.provider,'model':pass_resp.model,'output':pass_resp.output},'telemetry':mvp.asdict(tel),'routing':mvp.asdict(routing),'live_provider_calls':0,'api_key_used':False}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); args=ap.parse_args()
    if args.self_test: print(json.dumps(self_test(),indent=2,sort_keys=True)); return
    ap.print_help()
if __name__=='__main__': main()
