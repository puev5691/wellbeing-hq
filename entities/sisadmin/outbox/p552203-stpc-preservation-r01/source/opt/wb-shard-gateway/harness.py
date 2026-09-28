from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

ADAPTER_SHA256="9c443bbfb45c5804a7f375ea42904f99de98b2b07ffe86e53a67d5483166e881"
ADAPTER_BLOB="d42e58060365c4b996bf87c81f3e3eb2ad684ceb"
AUDIT_SHA256="5e50e09f01eec3ec5daf8063c4100837375ae89f91f4dda67a5a63990e9e4d88"
MAX_REQUEST_BYTES=32768
EXIT_OK=0
EXIT_GATEWAY_REJECTED=20
EXIT_INPUT=64
EXIT_ADAPTER=65
EXIT_AUDIT_MODULE=66
EXIT_AUDIT=70

def canonical(v):
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")

def harness_error(code):
    return {"schema":"wb.shard_gateway.harness_result.v2","ok":False,"error_code":code}

def _load_pinned(path:Path,expected_sha:str,module_name:str,error_prefix:str):
    try:
        raw=path.read_bytes()
    except OSError:
        raise RuntimeError(error_prefix+"_UNAVAILABLE") from None
    if hashlib.sha256(raw).hexdigest()!=expected_sha:
        raise RuntimeError(error_prefix+"_IDENTITY_MISMATCH")
    spec=importlib.util.spec_from_file_location(module_name,path)
    if spec is None or spec.loader is None:
        raise RuntimeError(error_prefix+"_IMPORT_FAILED")
    mod=importlib.util.module_from_spec(spec)
    sys.modules[module_name]=mod
    try:
        spec.loader.exec_module(mod)
    except Exception:
        raise RuntimeError(error_prefix+"_IMPORT_FAILED") from None
    return mod

def load_adapter(path:Path):
    return _load_pinned(path,ADAPTER_SHA256,"_wb_gateway_r03","ADAPTER")

def load_audit(path:Path):
    mod=_load_pinned(path,AUDIT_SHA256,"_wb_audit_sink_r02","AUDIT_MODULE")
    if not hasattr(mod,"append_record") or not hasattr(mod,"AuditSinkError"):
        raise RuntimeError("AUDIT_MODULE_IMPORT_FAILED")
    return mod

def read_request(path:Path)->bytes:
    try:
        with open(path,"rb") as f:
            data=f.read(MAX_REQUEST_BYTES+1)
    except OSError:
        raise RuntimeError("REQUEST_READ_FAILED") from None
    if not data or len(data)>MAX_REQUEST_BYTES:
        raise RuntimeError("REQUEST_SIZE_INVALID")
    try:
        text=data.decode("utf-8")
        decoder=json.JSONDecoder()
        _,end=decoder.raw_decode(text)
        if text[end:].strip():
            raise ValueError
    except Exception:
        raise RuntimeError("REQUEST_JSON_INVALID") from None
    return data

def safe_request_meta(raw:bytes):
    out={"request_id":"rejected","requester_entity":"unknown","authority_ref":"unknown",
         "host_id":"","operation":"","root_id":"","target_rel":""}
    try:
        obj=json.loads(raw.decode("utf-8"))
        if type(obj) is not dict:
            return out
        for key in ("request_id","requester_entity","authority_ref","host_id","operation","root_id"):
            value=obj.get(key)
            if type(value) is str and len(value.encode("utf-8"))<=256:
                out[key]=value
        rel=obj.get("relative_path")
        if type(rel) is str and len(rel.encode("utf-8"))<=512:
            out["target_rel"]=rel
    except Exception:
        pass
    return out

def make_audit(adapter,meta,result,duration_ms):
    raw_result=adapter.serialize_result(result)
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
      "result_digest":hashlib.sha256(raw_result).hexdigest(),
      "exit_status":0 if result.ok else 1,
      "error_code":result.error_code,
      "duration_ms":int(duration_ms),
      "output_bytes":result.output_bytes,
      "truncated":result.truncated
    }

def make_failure_audit(code):
    raw=canonical(harness_error(code))
    return {"schema":"wb.shard_gateway.audit.v1","request_id":"rejected","requester_entity":"unknown",
      "authority_ref":"unknown","host_id":"","service_identity":"arh-preserve","mode":"VERIFY",
      "operation":"","root_id":"","target_rel":"","target_digest":None,
      "result_digest":hashlib.sha256(raw).hexdigest(),"exit_status":1,"error_code":code,
      "duration_ms":0,"output_bytes":len(raw),"truncated":False}

def emit_error(code):
    sys.stdout.buffer.write(canonical(harness_error(code))+b"\n")

def main(argv=None):
    parser=argparse.ArgumentParser(add_help=True)
    parser.add_argument("--adapter",required=True)
    parser.add_argument("--audit-module",required=True)
    parser.add_argument("--request-file",required=True)
    parser.add_argument("--audit",required=True)
    ns=parser.parse_args(argv)
    try:
        audit_mod=load_audit(Path(ns.audit_module))
    except RuntimeError as exc:
        emit_error(str(exc))
        return EXIT_AUDIT_MODULE
    def fail_with_audit(code,exit_code):
        try:
            audit_mod.append_record(Path(ns.audit),make_failure_audit(code))
        except audit_mod.AuditSinkError:
            emit_error("AUDIT_APPEND_FAILED")
            return EXIT_AUDIT
        emit_error(code)
        return exit_code
    try:
        adapter=load_adapter(Path(ns.adapter))
    except RuntimeError as exc:
        return fail_with_audit(str(exc),EXIT_ADAPTER)
    try:
        raw=read_request(Path(ns.request_file))
    except RuntimeError as exc:
        return fail_with_audit(str(exc),EXIT_INPUT)
    meta=safe_request_meta(raw)
    started=time.monotonic_ns()
    result=adapter.Gateway().execute(raw)
    duration=(time.monotonic_ns()-started)//1_000_000
    record=make_audit(adapter,meta,result,duration)
    try:
        audit_mod.append_record(Path(ns.audit),record)
    except audit_mod.AuditSinkError:
        emit_error("AUDIT_APPEND_FAILED")
        return EXIT_AUDIT
    sys.stdout.buffer.write(adapter.serialize_result(result)+b"\n")
    return EXIT_OK if result.ok else EXIT_GATEWAY_REJECTED

if __name__=="__main__":
    raise SystemExit(main())
