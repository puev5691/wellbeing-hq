from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path

ADAPTER_SHA256="5d34165c30869d2d12a677093c445115dfc19e410f44a580b9d541eca778fb30"
ADAPTER_BLOB="1e1da64573016c925c1534efede7fd0e32aabd4b"
MAX_REQUEST_BYTES=32768
EXIT_OK=0
EXIT_GATEWAY_REJECTED=20
EXIT_INPUT=64
EXIT_ADAPTER=65
EXIT_AUDIT=70

def canonical(v):
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")

def harness_error(code):
    return {"schema":"wb.shard_gateway.harness_result.v1","ok":False,"error_code":code}

def load_adapter(path:Path):
    try: raw=path.read_bytes()
    except OSError: raise RuntimeError("ADAPTER_UNAVAILABLE") from None
    if hashlib.sha256(raw).hexdigest()!=ADAPTER_SHA256:
        raise RuntimeError("ADAPTER_IDENTITY_MISMATCH")
    spec=importlib.util.spec_from_file_location("_wb_gateway_r02",path)
    if spec is None or spec.loader is None: raise RuntimeError("ADAPTER_IMPORT_FAILED")
    mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod
    try: spec.loader.exec_module(mod)
    except Exception: raise RuntimeError("ADAPTER_IMPORT_FAILED") from None
    return mod

def read_request(path:Path)->bytes:
    try:
        with open(path,"rb") as f: data=f.read(MAX_REQUEST_BYTES+1)
    except OSError: raise RuntimeError("REQUEST_READ_FAILED") from None
    if not data or len(data)>MAX_REQUEST_BYTES: raise RuntimeError("REQUEST_SIZE_INVALID")
    try:
        text=data.decode("utf-8")
        decoder=json.JSONDecoder()
        _,end=decoder.raw_decode(text)
        if text[end:].strip(): raise ValueError
    except Exception: raise RuntimeError("REQUEST_JSON_INVALID") from None
    return data

def safe_request_meta(raw:bytes):
    out={"request_id":"rejected","requester_entity":"unknown","authority_ref":"unknown",
         "host_id":"","operation":"","root_id":"","target_rel":""}
    try:
        o=json.loads(raw.decode("utf-8"))
        if type(o) is not dict: return out
        for k in ("request_id","requester_entity","authority_ref","host_id","operation","root_id"):
            v=o.get(k)
            if type(v) is str and len(v.encode("utf-8"))<=256: out[k]=v
        p=o.get("relative_path")
        if type(p) is str and len(p.encode("utf-8"))<=512: out["target_rel"]=p
    except Exception: pass
    return out

def make_audit(adapter,meta,result,duration_ms):
    rd=adapter.serialize_result(result)
    return {
      "schema":"wb.shard_gateway.audit.v1",
      "request_id":result.request_id or meta["request_id"],
      "requester_entity":meta["requester_entity"],
      "authority_ref":meta["authority_ref"],
      "host_id":result.host_id or meta["host_id"],
      "service_identity":"arh-preserve",
      "mode":"VERIFY",
      "operation":result.operation or meta["operation"],
      "root_id":result.root_id or meta["root_id"],
      "target_rel":result.target_rel or meta["target_rel"],
      "target_digest":result.payload.get("sha256") if result.ok else None,
      "result_digest":hashlib.sha256(rd).hexdigest(),
      "exit_status":0 if result.ok else 1,
      "error_code":result.error_code,
      "duration_ms":int(duration_ms),
      "output_bytes":result.output_bytes,
      "truncated":result.truncated
    }

def main(argv=None):
    p=argparse.ArgumentParser(add_help=True)
    p.add_argument("--adapter",required=True)
    p.add_argument("--request-file",required=True)
    p.add_argument("--audit",required=True)
    ns=p.parse_args(argv)
    try: adapter=load_adapter(Path(ns.adapter))
    except RuntimeError as e:
        sys.stdout.buffer.write(canonical(harness_error(str(e)))+b"\n"); return EXIT_ADAPTER
    try: raw=read_request(Path(ns.request_file))
    except RuntimeError as e:
        sys.stdout.buffer.write(canonical(harness_error(str(e)))+b"\n"); return EXIT_INPUT
    meta=safe_request_meta(raw)
    started=time.monotonic_ns()
    result=adapter.Gateway().execute(raw)
    duration=(time.monotonic_ns()-started)//1_000_000
    audit=make_audit(adapter,meta,result,duration)
    from audit_sink import append_record, AuditSinkError
    try: append_record(Path(ns.audit),audit)
    except AuditSinkError:
        sys.stdout.buffer.write(canonical(harness_error("AUDIT_APPEND_FAILED"))+b"\n"); return EXIT_AUDIT
    sys.stdout.buffer.write(adapter.serialize_result(result)+b"\n")
    return EXIT_OK if result.ok else EXIT_GATEWAY_REJECTED

if __name__=="__main__":
    raise SystemExit(main())
