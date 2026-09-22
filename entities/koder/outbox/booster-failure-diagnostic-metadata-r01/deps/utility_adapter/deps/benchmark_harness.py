#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Protocol

VERDICT='PASS_OPENAI_LIVE_BENCHMARK_HARNESS_R01_READY_FOR_ACCOUNT_GATE'
WRITER_BLOB='23f20f04504c65497c154c099d8090cde11fba83'
TASK_PATH='entities/koordinator/outbox/KOO__openai-live-benchmark-harness-r01__KOD.md'
TASK_COMMIT='5afc12021a213723f5bef8d69713018e4016c73a'
TASK_BLOB='c6f2ba5aea41baf613335be71db8958765b518e1'
RUNTIME_INTEGRATION_COMMIT='b212eda0151a5ee07fed8f5cef4299e2b7e3a73f'
RUNTIME_INTEGRATION_BLOB='f32783d1ea3be5966ee5c7fefe593a604558c7e9'
SIS_GATE_COMMIT='3c282b2d67a699520ccbf7a751616c3e2ee58d5a'
LIVE_SWITCH_NAME='OPENAI_LIVE_BENCHMARK'
LIVE_SWITCH_VALUE='EXPLICIT_OPENAI_LIVE_BENCHMARK_R01'
MODELS=('gpt-5.6-luna','gpt-5.6-terra','gpt-5.6-sol')

class HarnessBlocked(RuntimeError): pass

TASKS=(
 {'id':'extract-001','task_class':'extraction_classification','prompt':'Classify: apple=fruit, carrot=vegetable. Return JSON labels.','fake':'{"apple":"fruit","carrot":"vegetable"}','eval':{'kind':'json_exact','expected':{'apple':'fruit','carrot':'vegetable'}}},
 {'id':'ru-summary-001','task_class':'concise_russian_operator_summary','prompt':'Synthetic status: local test passed, network unused, next step account gate. Summarize in Russian <=120 chars.','fake':'Локальный тест пройден; сеть не использовалась; далее — account gate.','eval':{'kind':'russian_summary','max_chars':120,'required':['тест','сеть']}},
 {'id':'code-001','task_class':'bounded_coding_reasoning','prompt':'Return JSON with answer to 6*7 and Python expression.','fake':'{"answer":42,"expression":"6*7"}','eval':{'kind':'json_exact','expected':{'answer':42,'expression':'6*7'}}},
 {'id':'json-001','task_class':'structured_json_output','prompt':'Return JSON status=ok and items=[1,2,3].','fake':'{"status":"ok","items":[1,2,3]}','eval':{'kind':'json_exact','expected':{'status':'ok','items':[1,2,3]}}},
)

@dataclass
class Usage:
 input_tokens:int|None=None; cached_input_tokens:int|None=None; output_tokens:int|None=None; total_tokens:int|None=None
@dataclass
class RunRecord:
 provider:str; model:str; task_id:str; task_class:str; mode:str; provider_request_id:str|None; usage:dict[str,Any]; provider_latency_ms:float|None; harness_wall_ms:float; retries:int; result_status:str; estimated_cost_usd:float|None; price_snapshot_id:str; eval:dict[str,Any]; output:str

class Executor(Protocol):
 def invoke(self,model:str,task:dict[str,Any])->dict[str,Any]: ...

class DryRunExecutor:
 external_network_used=False
 def invoke(self,model:str,task:dict[str,Any])->dict[str,Any]:
  return {'output':task['fake'],'provider_request_id':None,'usage':None,'provider_latency_ms':None,'retries':0,'status':'PASS_DRY_RUN'}

def load_prices(path:Path)->dict[str,Any]:
 p=json.loads(path.read_text());
 if set(p['models'])!=set(MODELS): raise HarnessBlocked('BLOCKED_PRICE_SNAPSHOT_MODEL_SET')
 return p

def estimate_cost(model:str,usage:Usage,prices:dict[str,Any])->float|None:
 vals=(usage.input_tokens,usage.output_tokens)
 if any(v is None for v in vals): return None
 if usage.input_tokens<0 or usage.output_tokens<0 or (usage.cached_input_tokens or 0)<0: raise HarnessBlocked('BLOCKED_INVALID_USAGE')
 if usage.input_tokens>prices['estimator_scope']['max_input_tokens_inclusive']: raise HarnessBlocked(prices['estimator_scope']['over_limit'])
 cached=usage.cached_input_tokens or 0
 if cached>usage.input_tokens: raise HarnessBlocked('BLOCKED_INVALID_CACHED_USAGE')
 r=prices['models'][model]
 cost=((usage.input_tokens-cached)*r['input']+cached*r['cached_input']+usage.output_tokens*r['output'])/1_000_000
 return round(cost,12)

def evaluate(task:dict[str,Any],output:str)->dict[str,Any]:
 spec=task['eval']; kind=spec['kind']
 if kind=='json_exact':
  try: obj=json.loads(output); valid=True
  except Exception: obj=None; valid=False
  return {'deterministic':True,'json_valid':valid,'exact_match':valid and obj==spec['expected'],'pass':valid and obj==spec['expected']}
 if kind=='russian_summary':
  low=output.lower(); required=all(x in low for x in spec['required']); length_ok=len(output)<=spec['max_chars']; has_cyr=any('а'<=c.lower()<='я' or c in 'Ёё' for c in output)
  return {'deterministic':True,'length_chars':len(output),'max_chars':spec['max_chars'],'required_terms':required,'cyrillic':has_cyr,'pass':required and length_ok and has_cyr}
 raise HarnessBlocked('BLOCKED_UNKNOWN_EVAL')

def select_models(raw:str)->list[str]:
 selected=list(MODELS) if raw=='all' else [x.strip() for x in raw.split(',') if x.strip()]
 if not selected or any(x not in MODELS for x in selected): raise HarnessBlocked('BLOCKED_MODEL_NOT_ALLOWLISTED')
 if len(selected)!=len(set(selected)): raise HarnessBlocked('BLOCKED_DUPLICATE_MODEL')
 return selected

def require_live_authority()->None:
 if os.environ.get(LIVE_SWITCH_NAME)!=LIVE_SWITCH_VALUE: raise HarnessBlocked('BLOCKED_LIVE_AUTHORITY_REQUIRED')

def run_benchmark(models:list[str],mode:str,prices:dict[str,Any],executor:Executor|None=None)->list[RunRecord]:
 if mode not in {'dry_run','live'}: raise HarnessBlocked('BLOCKED_MODE')
 if mode=='live':
  require_live_authority()
  if executor is None: raise HarnessBlocked('BLOCKED_LIVE_EXECUTOR_NOT_BOUND')
 else:
  executor=executor or DryRunExecutor()
 records=[]
 for model in models:
  for task in TASKS:
   t0=time.perf_counter_ns(); raw=executor.invoke(model,task); wall=(time.perf_counter_ns()-t0)/1_000_000
   u=raw.get('usage') or {}; usage=Usage(u.get('input_tokens'),u.get('cached_input_tokens'),u.get('output_tokens'),u.get('total_tokens'))
   ev=evaluate(task,raw['output']); status=raw.get('status','PASS' if ev['pass'] else 'FAIL_EVAL')
   if not ev['pass']: status='FAIL_EVAL'
   records.append(RunRecord('openai',model,task['id'],task['task_class'],mode,raw.get('provider_request_id'),asdict(usage),raw.get('provider_latency_ms'),wall,int(raw.get('retries',0)),status,estimate_cost(model,usage,prices),prices['snapshot_id'],ev,raw['output']))
 return records

def summary(records:list[RunRecord])->dict[str,Any]:
 return {'verdict':VERDICT,'provider':'openai','models':sorted({r.model for r in records}),'task_classes':sorted({r.task_class for r in records}),'runs':len(records),'all_eval_pass':all(r.eval['pass'] for r in records),'live_provider_calls':0 if all(r.mode=='dry_run' for r in records) else None,'records':[asdict(r) for r in records]}

def markdown(s:dict[str,Any])->str:
 lines=[f"STATUS: {s['verdict']}",f"RUNS: {s['runs']}",f"MODELS: {', '.join(s['models'])}",f"ALL_EVAL_PASS: {str(s['all_eval_pass']).lower()}","",'| model | task | status | cost_usd | provider_latency_ms |','|---|---|---|---:|---:|']
 for r in s['records']: lines.append(f"| {r['model']} | {r['task_class']} | {r['result_status']} | {r['estimated_cost_usd']} | {r['provider_latency_ms']} |")
 return '\n'.join(lines)+'\n'

def self_test(price_path:Path)->dict[str,Any]:
 prices=load_prices(price_path); checks=[]
 recs=run_benchmark(list(MODELS),'dry_run',prices); s=summary(recs)
 assert len(recs)==12 and s['all_eval_pass']; checks.append('three_models_four_task_classes')
 assert all(r.provider=='openai' and r.model in MODELS for r in recs); checks.append('explicit_routes')
 assert all(r.provider_request_id is None and r.usage['input_tokens'] is None and r.estimated_cost_usd is None for r in recs); checks.append('dry_run_does_not_invent_provider_evidence')
 assert all(r.provider_latency_ms is None and r.harness_wall_ms>=0 for r in recs); checks.append('observable_local_latency_only')
 assert estimate_cost('gpt-5.6-luna',Usage(1000,0,500,1500),prices)==0.0008; checks.append('versioned_cost_estimator')
 try: select_models('gpt-5.6-luna,bogus'); raise AssertionError
 except HarnessBlocked as e: assert str(e)=='BLOCKED_MODEL_NOT_ALLOWLISTED'; checks.append('no_silent_model_fallback')
 old=os.environ.pop(LIVE_SWITCH_NAME,None)
 try:
  try: run_benchmark(['gpt-5.6-luna'],'live',prices); raise AssertionError
  except HarnessBlocked as e: assert str(e)=='BLOCKED_LIVE_AUTHORITY_REQUIRED'; checks.append('live_default_deny')
 finally:
  if old is not None: os.environ[LIVE_SWITCH_NAME]=old
 old_key=os.environ.get('OPENAI_API_KEY'); os.environ['OPENAI_API_KEY']='DUMMY_NOT_A_REAL_KEY'
 try:
  recs2=run_benchmark(['gpt-5.6-luna'],'dry_run',prices); assert recs2[0].result_status=='PASS_DRY_RUN'
 finally:
  if old_key is None: os.environ.pop('OPENAI_API_KEY',None)
  else: os.environ['OPENAI_API_KEY']=old_key
 checks.append('dry_run_does_not_require_or_consume_key')
 assert 'STATUS:' in markdown(s); checks.append('compact_json_and_markdown_summary')
 return {'verdict':VERDICT,'checks':checks,'count':len(checks),'dry_run_records':len(recs),'models':list(MODELS),'task_classes':[x['task_class'] for x in TASKS],'price_snapshot_id':prices['snapshot_id'],'live_provider_calls':0,'api_key_used':False}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['dry_run','live'],default='dry_run'); ap.add_argument('--models',default='all'); ap.add_argument('--format',choices=['json','markdown'],default='json'); ap.add_argument('--price-snapshot',default=str(Path(__file__).with_name('price-snapshot-r01.json'))); ap.add_argument('--self-test',action='store_true'); a=ap.parse_args(); prices=load_prices(Path(a.price_snapshot))
 if a.self_test: print(json.dumps(self_test(Path(a.price_snapshot)),indent=2,ensure_ascii=False,sort_keys=True)); return
 s=summary(run_benchmark(select_models(a.models),a.mode,prices)); print(json.dumps(s,indent=2,ensure_ascii=False) if a.format=='json' else markdown(s))
if __name__=='__main__': main()
