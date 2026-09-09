#!/usr/bin/env python3
import argparse, json, os, stat, sys, urllib.error
from pathlib import Path
from entity_env_server.client import HTTPClient

APPROVED_ENDPOINT="http://127.0.0.1:18081"

class HelperError(Exception): pass

def emit(obj, stream):
    json.dump(obj, stream, ensure_ascii=False, separators=(",",":"), sort_keys=True)
    stream.write("\n")

def load_json(path,label):
    try:
        with Path(path).open("r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HelperError(label+"_not_found")
    except json.JSONDecodeError:
        raise HelperError(label+"_invalid_json")
    except OSError:
        raise HelperError(label+"_unreadable")

def load_credential(path):
    p=Path(path)
    try:
        st=p.lstat()
    except FileNotFoundError:
        raise HelperError("credential_file_not_found")
    except OSError:
        raise HelperError("credential_file_unreadable")
    if stat.S_ISLNK(st.st_mode) or not stat.S_ISREG(st.st_mode):
        raise HelperError("credential_file_must_be_regular")
    if stat.S_IMODE(st.st_mode)!=0o600:
        raise HelperError("credential_file_mode_must_be_0600")
    if st.st_uid!=os.geteuid():
        raise HelperError("credential_file_owner_mismatch")
    obj=load_json(p,"credential_file")
    if not isinstance(obj,dict):
        raise HelperError("credential_file_invalid_shape")
    token=obj.get("token")
    if not isinstance(token,str) or not token:
        raise HelperError("credential_token_missing")
    return token

def parser():
    p=argparse.ArgumentParser()
    p.add_argument("--credential-file",required=True)
    p.add_argument("--url",default=APPROVED_ENDPOINT)
    s=p.add_subparsers(dest="cmd",required=True)
    st=s.add_parser("state"); st.add_argument("--entity-id")
    s.add_parser("inbox")
    au=s.add_parser("audit"); au.add_argument("--limit",type=int,default=100)
    co=s.add_parser("command"); co.add_argument("operation"); co.add_argument("--json-file",required=True)
    return p

def main(argv=None):
    args=parser().parse_args(argv)
    token=None
    try:
        if args.url != APPROVED_ENDPOINT:
            raise HelperError("target_not_approved")
        token=load_credential(args.credential_file)
        c=HTTPClient(APPROVED_ENDPOINT,token)
        if args.cmd=="state":
            path="/api/v1/state"
            if args.entity_id:
                from urllib.parse import urlencode
                path += "?" + urlencode({"entity_id":args.entity_id})
            result=c.get(path)
        elif args.cmd=="inbox":
            result=c.get("/api/v1/inbox")
        elif args.cmd=="audit":
            if args.limit<1:
                raise HelperError("audit_limit_must_be_positive")
            from urllib.parse import urlencode
            result=c.get("/api/v1/audit?"+urlencode({"limit":args.limit}))
        else:
            body=load_json(args.json_file,"command_json")
            if not isinstance(body,dict):
                raise HelperError("command_json_must_be_object")
            result=c.command(args.operation,**body)
        emit(result,sys.stdout)
        return 0
    except HelperError as e:
        emit({"error":str(e)},sys.stderr)
        return 2
    except urllib.error.HTTPError as e:
        emit({"error":"http_error","status":getattr(e,"code",None)},sys.stderr)
        return 3
    except Exception:
        emit({"error":"client_failure"},sys.stderr)
        return 4
    finally:
        token=None

if __name__=="__main__":
    raise SystemExit(main())
