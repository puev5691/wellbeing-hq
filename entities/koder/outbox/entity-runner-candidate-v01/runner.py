#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,os,time,urllib.error,urllib.request
API_BASE="https://api.anthropic.com"
ANTHROPIC_VERSION="2023-06-01"
ANTHROPIC_BETA="managed-agents-2026-04-01"
KNOWN_STATUSES={"idle","running","rescheduling","terminated"}
class RunnerError(RuntimeError): pass
def required_env(name):
    value=os.environ.get(name,"").strip()
    if not value: raise RunnerError(f"missing_required_env:{name}")
    return value
def safe_event(kind,**fields):
    print(json.dumps({"event":kind,**fields},sort_keys=True,separators=(",",":")),flush=True)
def request_json(method,path,api_key,body=None):
    data=None if body is None else json.dumps(body,separators=(",",":")).encode()
    req=urllib.request.Request(API_BASE+path,method=method,data=data,headers={"x-api-key":api_key,"anthropic-version":ANTHROPIC_VERSION,"anthropic-beta":ANTHROPIC_BETA,"content-type":"application/json","user-agent":"wellbeing-hq-entity-runner-candidate/0.1"})
    try:
        with urllib.request.urlopen(req,timeout=30) as resp: raw=resp.read()
    except urllib.error.HTTPError as exc:
        raise RunnerError(f"provider_http_error:{exc.code}") from None
    except urllib.error.URLError:
        raise RunnerError("provider_transport_error") from None
    try: decoded=json.loads(raw)
    except json.JSONDecodeError: raise RunnerError("provider_invalid_json") from None
    if not isinstance(decoded,dict): raise RunnerError("provider_unexpected_payload")
    return decoded
def validate_budget(value):
    if not value.isdigit() or not (1<=int(value)<=500): raise RunnerError("budget_cents_must_be_integer_1_to_500")
    return value
def create_session(api_key,agent_id,environment_id,task,budget):
    return request_json("POST","/v1/sessions",api_key,{"agent":agent_id,"environment_id":environment_id,"budget":{"type":"limit","max_list_cost":{"amount":budget,"currency":"USD"}},"initial_events":[{"type":"user.message","content":[{"type":"text","text":task}]}],"metadata":{"project":"wellbeing-hq","candidate":"entity-runner-v01","purpose":"bounded-non-production-e2e"}})
def get_session(api_key,session_id): return request_json("GET",f"/v1/sessions/{session_id}",api_key)
def main():
    p=argparse.ArgumentParser(); p.add_argument("--task",required=True); p.add_argument("--timeout",type=int,default=180); p.add_argument("--poll",type=int,default=5); p.add_argument("--budget-cents",default="25"); p.add_argument("--validate-only",action="store_true"); a=p.parse_args()
    if not 10<=a.timeout<=900: raise RunnerError("timeout_must_be_10_to_900")
    if not 1<=a.poll<=60: raise RunnerError("poll_must_be_1_to_60")
    budget=validate_budget(a.budget_cents); api_key=required_env("ANTHROPIC_API_KEY"); agent_id=required_env("ANTHROPIC_AGENT_ID"); environment_id=required_env("ANTHROPIC_ENVIRONMENT_ID")
    if a.validate_only:
        safe_event("validation_pass",provider="claude_managed_agents",api_base=API_BASE,anthropic_version=ANTHROPIC_VERSION,beta=ANTHROPIC_BETA,budget_cents=budget); return 0
    session=create_session(api_key,agent_id,environment_id,a.task,budget); session_id,status=session.get("id"),session.get("status")
    if not isinstance(session_id,str) or not session_id: raise RunnerError("provider_missing_session_id")
    if status not in KNOWN_STATUSES: raise RunnerError("provider_unknown_session_status")
    safe_event("processing_started",provider="claude_managed_agents",session_id=session_id,status=status)
    deadline=time.monotonic()+a.timeout; last=None
    while time.monotonic()<deadline:
        current=get_session(api_key,session_id); s=current.get("status")
        if s not in KNOWN_STATUSES: raise RunnerError("provider_unknown_session_status")
        if s!=last: safe_event("lifecycle",session_id=session_id,status=s); last=s
        if s=="idle": safe_event("processing_completed",session_id=session_id,status=s); return 0
        if s=="terminated": safe_event("processing_failed",session_id=session_id,status=s); return 2
        time.sleep(a.poll)
    safe_event("processing_failed",session_id=session_id,status="timeout"); return 3
if __name__=="__main__":
    try: raise SystemExit(main())
    except RunnerError as exc:
        safe_event("runner_failed",error=str(exc)); raise SystemExit(1)
