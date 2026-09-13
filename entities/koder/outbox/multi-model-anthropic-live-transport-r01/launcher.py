from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path

from policy import PolicyGuard
from anthropic_adapter import build_request_plan
from live_transport import AnthropicLiveTransport, EnvironmentSecretReader, LIVE_SWITCH_ENV, UrllibExecutor, validate_blueprint

def load_config(path:str)->dict:
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data,dict): raise ValueError("config_must_be_object")
    return data

def prepare_plan(config:dict)->dict:
    g=PolicyGuard().evaluate(config)
    plan=build_request_plan(g.normalized)
    validate_blueprint(plan)
    return plan

def default_denied_summary(plan:dict)->dict:
    return {"status":"LIVE_DISABLED_DEFAULT_DENY","provider":"anthropic","model":"claude-sonnet-5","route":plan["url"],"request_hash":plan["request_hash"],"credential_source":"ANTHROPIC_API_KEY","credential_read":False,"external_network_used":False}

def main(argv:list[str]|None=None)->int:
    p=argparse.ArgumentParser()
    p.add_argument("--config",required=True)
    p.add_argument("--live",action="store_true",help="explicitly request the separately authorized D0 live gate")
    p.add_argument("--timeout",type=float,default=30.0)
    a=p.parse_args(argv)
    plan=prepare_plan(load_config(a.config))
    if not a.live:
        print(json.dumps(default_denied_summary(plan),sort_keys=True))
        return 0
    transport=AnthropicLiveTransport(UrllibExecutor(),EnvironmentSecretReader())
    result=transport.run_live(plan,live_switch=os.environ.get(LIVE_SWITCH_ENV),timeout=a.timeout)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as e:
        code=getattr(e,"code",type(e).__name__)
        status=getattr(e,"http_status",None)
        external=getattr(e,"external_network_used",False)
        print(json.dumps({"status":"FAIL_CLOSED","error_code":code,"http_status":status,"external_network_used":external},sort_keys=True),file=sys.stderr)
        raise SystemExit(2)
