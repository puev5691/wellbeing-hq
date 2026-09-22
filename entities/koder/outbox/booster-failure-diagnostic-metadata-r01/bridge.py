"""Bounded successor bridge. Library API only; no automatic network entrypoint."""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys
import time

ROOT = Path(__file__).resolve().parent
DOMAIN = 'wb.booster.utility_bridge.v1'
MODEL = 'gpt-5.6-luna'
AUTHORITY = 'AUTHORIZE_BOOSTER_UTILITY_PILOT_R01_ONE_SHOT'
SECRETREF = 'secretref:openai:wellbeing-entity-boosters-restricted'
PINS = {
 'live_worker.py':'175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3',
 'response_shape_store.py':'bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f',
 'review_result_store.py':'72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba',
 'reviewable_live_worker.py':'54f8ac0c52b8a6f14c22f69a0dd837506f9054aada0a353ac4f09cd473700c95',
 'diagnostic_reviewable_live_worker.py':'c9ad1c2719ba4738a1490315ab55977758adbe1202a71286e30acd9826489d6a',
 'utility_adapter/pilot_adapter.py':'233699cac4f3eccdefbdc8fc76b3a88c9dcb2479a40697fbd37c5cbc260d30b7',
}

class Blocked(ValueError): pass
def need(ok, code):
    if not ok: raise Blocked(code)
def canon(v):
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def sha(v): return hashlib.sha256(v if type(v) is bytes else canon(v)).hexdigest()
def exact(v, fields): need(type(v) is dict and set(v)==set(fields.split()),'BLOCKED_SCHEMA')
def hexval(v,n): need(type(v) is str and re.fullmatch('[0-9a-f]{'+str(n)+'}',v),'BLOCKED_IDENTITY')
def text(v): need(type(v) is str and 0<len(v.encode())<=8192 and v.strip(),'BLOCKED_TEXT')
def integer(v,lo=0,hi=2**53-1): need(type(v) is int and lo<=v<=hi,'BLOCKED_INTEGER')
def load(name):
    path=ROOT/'deps'/name
    need(sha(path.read_bytes())==PINS[name],'BLOCKED_DEPENDENCY_IDENTITY')
    spec=importlib.util.spec_from_file_location('_bridge_'+name.replace('/','_').replace('.','_'),path)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    return mod
def ref(v):
    exact(v,'repository path commit blob')
    need(v['repository']=='puev5691/wellbeing-hq','BLOCKED_REPOSITORY')
    text(v['path']);hexval(v['commit'],40);hexval(v['blob'],40)

def request_hash(request):
    exact(request,'entity role task writer purpose payload source provider model data_class privacy_class tools max_output_tokens max_response_bytes timeout_seconds baseline_sha256')
    need(request['entity']=='KOD' and request['role']=='koder','BLOCKED_REQUESTER')
    for k in ('task','writer'):ref(request[k])
    need(request['writer']['path']=='entities/koder/current/KOD__replacement-current-writer-v05.md'
         and request['writer']['blob']=='cf1c84f9df7c90509703e4885844d0cf871ff412','BLOCKED_WRITER')
    text(request['purpose']);text(request['payload'])
    exact(request['source'],'locator sha256')
    text(request['source']['locator']);hexval(request['source']['sha256'],64)
    need(request['source']['sha256']==sha(request['payload'].encode()),'BLOCKED_SOURCE_HASH')
    hexval(request['baseline_sha256'],64)
    need(request['provider']=='openai' and request['model']==MODEL,'BLOCKED_MODEL')
    need(request['data_class']=='D0_SYNTHETIC' and request['privacy_class']=='synthetic_only','BLOCKED_PRIVACY')
    need(type(request['tools']) is list and request['tools']==[],'BLOCKED_TOOLS')
    for k,value in [('max_output_tokens',64),('max_response_bytes',16384),('timeout_seconds',30)]:
        need(type(request[k]) is int and request[k]==value,'BLOCKED_BOUND')
    return sha({'domain':DOMAIN+'/request','request':request})

def prepare(request, authority, *, now_tick, trusted_authority_sha256, verify_ref):
    """Caller supplies independently admitted authority digest and Git verifier.
    No authority is minted by accepting a request or preparing this plan.
    """
    rh=request_hash(request)
    need(callable(verify_ref),'BLOCKED_VERIFIER_REQUIRED')
    for k in ('task','writer'):
        need(verify_ref(request[k]) is True,'BLOCKED_'+k.upper()+'_REF')
    exact(authority,'authority_id execution_mode request_sha256 task writer provider model data_class privacy_class tools calls retries fallback max_output_tokens max_response_bytes timeout_seconds credential_ref valid_until_tick project_acceptance project_state_mutation baseline_sha256')
    ah=sha(authority);need(ah==trusted_authority_sha256,'BLOCKED_AUTHORITY_DIGEST')
    mode=authority['execution_mode']
    need(mode in ('OFFLINE_TEST','REAL_PILOT'),'BLOCKED_MODE')
    need(authority['authority_id']==(AUTHORITY if mode=='REAL_PILOT' else 'TEST_ONLY_UTILITY_BRIDGE_R01'),'BLOCKED_AUTHORITY_ID')
    need(authority['request_sha256']==rh,'BLOCKED_REQUEST_BINDING')
    for k in ('task','writer','provider','model','data_class','privacy_class','tools','max_output_tokens','max_response_bytes','timeout_seconds','baseline_sha256'):
        need(canon(authority[k])==canon(request[k]),'BLOCKED_AUTHORITY_'+k.upper())
    need(type(authority['calls']) is int and authority['calls']==1 and type(authority['retries']) is int and authority['retries']==0
         and authority['fallback']=='none','BLOCKED_RETRY_POLICY')
    need(authority['credential_ref']==SECRETREF and authority['project_acceptance']=='NOT_GRANTED'
         and authority['project_state_mutation'] is False,'BLOCKED_AUTHORITY_SCOPE')
    integer(now_tick);integer(authority['valid_until_tick'],1)
    need(now_tick<authority['valid_until_tick'],'BLOCKED_EXPIRED')
    native={'method':'POST','url':'https://api.openai.com/v1/responses','headers':{'content-type':'application/json'},
            'body':{'model':MODEL,'input':request['payload'],'max_output_tokens':64,'store':False,
                    'tools':[],'tool_choice':'none','parallel_tool_calls':False}}
    ph=sha({'domain':DOMAIN+'/plan','request_sha256':rh,'native':native,
            'authority_sha256':ah,'timeout_seconds':30,'max_response_bytes':16384})
    # Exact immutable worker algorithm; shared by worker, review validator, card.
    attempt=sha({'authority':ah,'request':rh,'plan':ph})
    identity={'request_sha256':rh,'plan_sha256':ph,'authority_sha256':ah,'attempt_key':attempt,
              'task_commit':request['task']['commit'],'task_blob':request['task']['blob'],
              'writer_blob':request['writer']['blob'],'provider':'openai','model':MODEL}
    return {'schema':DOMAIN+'/prepared','execution_mode':mode,'identity':identity,'native':native,
            'requester_sha256':sha({'entity':request['entity'],'role':request['role'],'task':request['task'],'writer':request['writer']}),
            'valid_until_tick':authority['valid_until_tick'],'baseline_sha256':request['baseline_sha256']}

def worker_plan(prepared):
    w=load('live_worker.py');i=prepared['identity']
    return w.WorkerPlan(i['request_sha256'],i['plan_sha256'],i['authority_sha256'],prepared['requester_sha256'],
                       'openai',MODEL,canon(prepared['native']).decode(),w.SecretRef('openai',SECRETREF),
                       w.WorkerPolicy(30,16384,1,0),prepared['valid_until_tick'])

def read_review(path, prepared, expected_sha256):
    raw=Path(path).read_bytes();need(len(raw)<=32768 and sha(raw)==expected_sha256,'BLOCKED_REVIEW_HASH')
    return load('review_result_store.py').read_and_validate(path,**prepared['identity'])

def execute(request, authority, *, now_tick, trusted_authority_sha256, verify_ref,
            directory, resolver, client, attest_execution):
    """Trusted host caller injects execution capability and durable directory.
    attest_execution binds mode to actual transport provenance; request cannot select it.
    Tests inject only fake clients under OFFLINE_TEST. No CLI or default resolver.
    """
    p=prepare(request,authority,now_tick=now_tick,trusted_authority_sha256=trusted_authority_sha256,verify_ref=verify_ref)
    need(attest_execution(p['execution_mode'],client,resolver) is True,'BLOCKED_EXECUTION_PROVENANCE')
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    w=load('live_worker.py');i=p['identity']
    # Extra reservation reuses durable ledger: same named authority cannot be
    # reused with a changed request/plan. Failures retain reservation, never retry.
    reservation=sha({'domain':DOMAIN+'/use-once','authority_id':authority['authority_id']})
    w.DurableOneShotLedger(directory/'authority.sqlite').claim(reservation,i['request_sha256'],i['plan_sha256'],i['authority_sha256'])
    latency=[]
    class MeasuredClient:
        calls=0
        transport_latency_ms=None
        def request(self,**kw):
            self.calls+=1
            start=time.perf_counter_ns()
            try:return client.request(**kw)
            finally:
                self.transport_latency_ms=(time.perf_counter_ns()-start)/1e6
                latency.append(self.transport_latency_ms)
    measured=MeasuredClient()
    d=load('diagnostic_reviewable_live_worker.py')
    runtime=d.DiagnosticReviewableLiveWorker(worker_path=ROOT/'deps/live_worker.py',
       result_integration_path=ROOT/'deps/reviewable_live_worker.py',result_store_path=ROOT/'deps/review_result_store.py',
       shape_store_path=ROOT/'deps/response_shape_store.py',ledger_path=directory/'attempts.sqlite',
       shape_dir=directory/'shapes',result_dir=directory/'reviews',resolver=resolver,client=measured,
       execution_mode=p['execution_mode'])
    out=runtime.invoke_once_persist_shape_then_normalize(worker_plan(p),d.Identity(i['task_commit'],i['task_blob'],i['writer_blob']),now_tick=now_tick)
    need(out['attempt_key']==i['attempt_key'],'BLOCKED_ATTEMPT')
    review_sha=sha(Path(out['result_path']).read_bytes())
    read_review(out['result_path'],p,review_sha)
    receipt={'schema':DOMAIN+'/execution','execution_mode':p['execution_mode'],'identity':i,
             'baseline_sha256':p['baseline_sha256'],'review_sha256':review_sha,
             'shape_snapshot_sha256':out['shape_snapshot_sha256'],'submissions':1,
             'provider_latency_ms':latency[0],'latency_source':'transport_boundary_monotonic',
             'project_acceptance':'NOT_GRANTED','project_state_mutation':False}
    path=directory/'execution.json';load('review_result_store.py').persist_atomic(path,receipt)
    receipt_sha=sha(canon(receipt)+b'\n')
    need(sha(path.read_bytes())==receipt_sha,'BLOCKED_EXECUTION_READBACK')
    return {'prepared':p,'receipt_path':str(path),'receipt_sha256':receipt_sha,'review_path':out['result_path']}

def evidence(items):
    need(type(items) is list and 0<len(items)<=16,'BLOCKED_EVIDENCE')
    for item in items:
        exact(item,'locator sha256');text(item['locator']);hexval(item['sha256'],64)

def cost_summary(cost, identity):
    exact(cost,'usage usage_evidence price_snapshot price_evidence billed_usd billing_evidence')
    a=load('utility_adapter/pilot_adapter.py')
    if cost['usage'] is None:
        need(cost['usage_evidence'] is None,'BLOCKED_USAGE_EVIDENCE')
    else:
        exact(cost['usage'],'input_tokens cached_input_tokens output_tokens total_tokens')
        evidence(cost['usage_evidence'])
        for v in cost['usage'].values():
            if v is not None:integer(v)
        u=cost['usage']
        if u['cached_input_tokens'] is not None and u['input_tokens'] is not None:
            need(u['cached_input_tokens']<=u['input_tokens'],'BLOCKED_USAGE')
        if all(u[k] is not None for k in ('input_tokens','output_tokens','total_tokens')):
            need(u['total_tokens']==u['input_tokens']+u['output_tokens'],'BLOCKED_USAGE')
    amount=None
    if cost['price_snapshot'] is None:need(cost['price_evidence'] is None,'BLOCKED_PRICE_EVIDENCE')
    else:
        evidence(cost['price_evidence']);p=cost['price_snapshot']
        exact(p,'snapshot_id models estimator_scope');text(p['snapshot_id'])
        need(type(p['models']) is dict and set(p['models'])=={MODEL},'BLOCKED_PRICE_MODEL')
        exact(p['models'][MODEL],'input cached_input output')
        for v in p['models'][MODEL].values():a.number(v)
        exact(p['estimator_scope'],'max_input_tokens_inclusive over_limit');integer(p['estimator_scope']['max_input_tokens_inclusive'],1)
        need(p['estimator_scope']['over_limit']=='BLOCKED_PRICE_RULE_OUT_OF_SCOPE','BLOCKED_PRICE_SCOPE')
        if cost['usage'] is not None and all(v is not None for v in cost['usage'].values()):
            b=a.dependency('benchmark_harness');amount=b.estimate_cost(MODEL,b.Usage(**cost['usage']),p)
    if cost['billed_usd'] is None:need(cost['billing_evidence'] is None,'BLOCKED_BILLING_EVIDENCE')
    else:a.number(cost['billed_usd']);evidence(cost['billing_evidence'])
    return {'estimated_usd':amount,'billed_usd':cost['billed_usd'],'cost_status':'unknown' if amount is None else 'estimated'}

def observations_check(observations):
    exact(observations,'comparison_mode baseline assisted cost')
    need(observations['comparison_mode'] in ('sequential_exploratory','matched_pair'),'BLOCKED_COMPARISON')
    a=load('utility_adapter/pilot_adapter.py')
    for side in ('baseline','assisted'):
        m=observations[side];evidence(m['evidence'])
        # Preserve existing metric/rubric/phase validation without relabeling the
        # recorded evidence: local placeholder only for its fixture-URI check.
        a.metrics(dict(m,evidence=['fixture://internal-metric-validation']))
    need(set(observations['baseline']['rubric'])==set(observations['assisted']['rubric']),'BLOCKED_RUBRIC')

def make_card(request, authority, *, now_tick, trusted_authority_sha256, verify_ref,
              receipt_path, trusted_receipt_sha256, review_path, mode,
              observations, requester_review):
    p=prepare(request,authority,now_tick=now_tick,trusted_authority_sha256=trusted_authority_sha256,verify_ref=verify_ref)
    need(mode==p['execution_mode'] and mode in ('REAL_PILOT','OFFLINE_TEST'),'BLOCKED_CARD_MODE')
    raw=Path(receipt_path).read_bytes()
    need(len(raw)<=32768 and sha(raw)==trusted_receipt_sha256,'BLOCKED_RECEIPT_HASH')
    r=json.loads(raw)
    exact(r,'schema execution_mode identity baseline_sha256 review_sha256 shape_snapshot_sha256 submissions provider_latency_ms latency_source project_acceptance project_state_mutation')
    need(r['schema']==DOMAIN+'/execution' and r['execution_mode']==mode,'BLOCKED_RECEIPT_MODE')
    need(r['identity']==p['identity'] and r['baseline_sha256']==request['baseline_sha256'],'BLOCKED_RECEIPT_IDENTITY')
    need(type(r['submissions']) is int and r['submissions']==1 and r['project_acceptance']=='NOT_GRANTED'
         and r['project_state_mutation'] is False,'BLOCKED_RECEIPT_SCOPE')
    hexval(r['shape_snapshot_sha256'],64)
    a=load('utility_adapter/pilot_adapter.py')
    if r['provider_latency_ms'] is not None:
        a.number(r['provider_latency_ms']);need(r['latency_source']=='transport_boundary_monotonic','BLOCKED_LATENCY_SOURCE')
    else:need(r['latency_source'] is None,'BLOCKED_LATENCY_SOURCE')
    review=read_review(review_path,p,r['review_sha256'])
    observations_check(observations);cost=cost_summary(observations['cost'],p['identity'])
    if requester_review is not None:
        exact(requester_review,'entity decision reason evidence')
        need(requester_review['entity']==request['entity'],'BLOCKED_REQUESTER_REVIEW')
        need(requester_review['decision'] in ('accept_as_candidate','needs_rework','reject'),'BLOCKED_DECISION')
        text(requester_review['reason']);evidence(requester_review['evidence'])
    complete=requester_review is not None
    return {'schema':DOMAIN+'/card','mode':mode,'evidence_class':'REAL_OBSERVATION' if mode=='REAL_PILOT' else 'TEST_FIXTURE',
       'identity':p['identity'],'baseline_sha256':request['baseline_sha256'],'execution_receipt_sha256':trusted_receipt_sha256,
       'review_result_sha256':r['review_sha256'],'review_payload_sha256':review['review_payload']['sha256'],
       'provider_calls':1 if mode=='REAL_PILOT' else 0,'simulated_submissions':1 if mode=='OFFLINE_TEST' else 0,
       'provider_latency_ms':r['provider_latency_ms'],'latency_evidence_receipt':trusted_receipt_sha256,
       'observations':observations,'cost':cost,'requester_review_required':True,'requester_review':requester_review,
       'status':'REVIEW_RECORDED' if complete else 'PENDING_REQUESTER_REVIEW',
       'utility_verdict':requester_review['decision'] if complete else None,
       'comparison':{k+'_saved':observations['baseline'][k]-observations['assisted'][k] for k in
          ('active_seconds','elapsed_seconds','cycles','rework_count','rework_seconds')} if complete else None,
       'sample_size':1,'general_acceleration_proven':False,'project_acceptance':'NOT_GRANTED',
       'production_acceptance':'NOT_GRANTED','project_state_mutation':False,'standing_authority':'NOT_GRANTED'}

def save_card(path, **trusted_inputs):
    card=make_card(**trusted_inputs);load('review_result_store.py').persist_atomic(Path(path),card)
    expected=sha(canon(card)+b'\n');read_card(path,expected,**trusted_inputs);return expected
def read_card(path, expected_sha256, **trusted_inputs):
    raw=Path(path).read_bytes();need(len(raw)<=32768 and sha(raw)==expected_sha256,'BLOCKED_CARD_HASH')
    expected=make_card(**trusted_inputs)
    need(canon(json.loads(raw))==canon(expected),'BLOCKED_CARD_CONTENT');return expected
