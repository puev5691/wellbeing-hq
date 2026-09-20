from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib, json, os, re, stat, uuid

SCHEMA="wb.openai.booster.review_result.v1"
MAX_PROVIDER_BODY_BYTES=16384
MAX_REVIEW_TEXT_BYTES=8192

class PersistenceError(RuntimeError): pass

def require(ok:bool,code:str):
    if not ok: raise PersistenceError(code)

def canonical(v:Any)->bytes:
    try:
        return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")
    except Exception:
        raise PersistenceError("BLOCKED_RESULT_SERIALIZATION") from None

def sha256_bytes(v:bytes)->str:
    return hashlib.sha256(v).hexdigest()

def _extract_review_text(obj:dict,expected_model:str)->str:
    require(obj.get("model")==expected_model,"BLOCKED_MODEL_MISMATCH")
    output=obj.get("output")
    require(type(output) is list and output,"BLOCKED_PROVIDER_RESPONSE")
    parts=[]
    for item in output:
        require(type(item) is dict,"BLOCKED_PROVIDER_RESPONSE")
        require(item.get("type")=="message","BLOCKED_UNEXPECTED_PROVIDER_ACTION")
        role=item.get("role")
        require(role=="assistant","BLOCKED_UNEXPECTED_PROVIDER_ACTION")
        content=item.get("content")
        require(type(content) is list and content,"BLOCKED_PROVIDER_RESPONSE")
        for c in content:
            require(type(c) is dict,"BLOCKED_PROVIDER_RESPONSE")
            require(c.get("type")=="output_text","BLOCKED_UNEXPECTED_PROVIDER_ACTION")
            text=c.get("text")
            require(type(text) is str,"BLOCKED_PROVIDER_RESPONSE")
            parts.append(text)
    text="\n".join(parts)
    require(bool(text.strip()),"BLOCKED_EMPTY_REVIEW_PAYLOAD")
    data=text.encode("utf-8")
    require(len(data)<=MAX_REVIEW_TEXT_BYTES,"BLOCKED_REVIEW_PAYLOAD_TOO_LARGE")
    return text

def normalize_openai_result(*,body:bytes,attempt_key:str,request_sha256:str,task_commit:str,
                            task_blob:str,writer_blob:str,provider:str,model:str,http_status:int,
                            provider_calls:int,retries:int,fallback:str)->dict:
    require(type(body) is bytes and 0<len(body)<=MAX_PROVIDER_BODY_BYTES,"BLOCKED_RESPONSE_TOO_LARGE")
    require(re.fullmatch(r"[0-9a-f]{64}",attempt_key or "") is not None,"BLOCKED_RESULT_IDENTITY")
    require(re.fullmatch(r"[0-9a-f]{64}",request_sha256 or "") is not None,"BLOCKED_RESULT_IDENTITY")
    require(re.fullmatch(r"[0-9a-f]{40}",task_commit or "") is not None,"BLOCKED_RESULT_IDENTITY")
    require(re.fullmatch(r"[0-9a-f]{40}",task_blob or "") is not None,"BLOCKED_RESULT_IDENTITY")
    require(re.fullmatch(r"[0-9a-f]{40}",writer_blob or "") is not None,"BLOCKED_RESULT_IDENTITY")
    require(provider=="openai","BLOCKED_PROVIDER_MISMATCH")
    require(type(model) is str and bool(model),"BLOCKED_MODEL_MISMATCH")
    require(http_status==200,"BLOCKED_HTTP_STATUS")
    require(provider_calls==1 and retries==0 and fallback=="none","BLOCKED_RETRY_FALLBACK_POLICY")
    try:
        obj=json.loads(body.decode("utf-8"))
    except Exception:
        raise PersistenceError("BLOCKED_MALFORMED_PROVIDER_RESPONSE") from None
    require(type(obj) is dict,"BLOCKED_MALFORMED_PROVIDER_RESPONSE")
    text=_extract_review_text(obj,model)
    raw_sha=sha256_bytes(body)
    text_bytes=text.encode("utf-8")
    return {
      "schema":SCHEMA,
      "attempt_key":attempt_key,
      "request_sha256":request_sha256,
      "task_commit":task_commit,
      "task_blob":task_blob,
      "writer_blob":writer_blob,
      "provider":"openai",
      "model":model,
      "http_status":200,
      "provider_calls":1,
      "retries":0,
      "fallback":"none",
      "response_bytes":len(body),
      "response_sha256":raw_sha,
      "parser_status":"NORMALIZED_ASSISTANT_TEXT_EXACT_FROM_OUTPUT_MESSAGES",
      "review_payload":{"kind":"assistant_text","text":text,"bytes":len(text_bytes),"sha256":sha256_bytes(text_bytes)},
      "requester_review_required":True,
      "project_acceptance":"NOT_GRANTED",
      "project_state_mutation":False,
      "provider_writer_authority":False,
      "gateway_writer_authority":False
    }

def validate_record(record:dict,*,attempt_key:str,request_sha256:str,task_commit:str,task_blob:str,
                    writer_blob:str,provider:str,model:str)->None:
    require(type(record) is dict and record.get("schema")==SCHEMA,"BLOCKED_RESULT_SCHEMA")
    exact={
      "attempt_key":attempt_key,"request_sha256":request_sha256,"task_commit":task_commit,
      "task_blob":task_blob,"writer_blob":writer_blob,"provider":provider,"model":model
    }
    for k,v in exact.items(): require(record.get(k)==v,"BLOCKED_RESULT_IDENTITY_MISMATCH")
    require(record.get("provider_calls")==1 and record.get("retries")==0 and record.get("fallback")=="none",
            "BLOCKED_RETRY_FALLBACK_POLICY")
    require(record.get("requester_review_required") is True and record.get("project_acceptance")=="NOT_GRANTED",
            "FAIL_RESULT_AUTHORITY")
    require(record.get("project_state_mutation") is False and record.get("provider_writer_authority") is False
            and record.get("gateway_writer_authority") is False,"FAIL_RESULT_AUTHORITY")
    rp=record.get("review_payload")
    require(type(rp) is dict and rp.get("kind")=="assistant_text" and type(rp.get("text")) is str
            and bool(rp["text"].strip()),"BLOCKED_REVIEW_PAYLOAD")
    b=rp["text"].encode("utf-8")
    require(rp.get("bytes")==len(b) and rp.get("sha256")==sha256_bytes(b),"BLOCKED_RESULT_IDENTITY_MISMATCH")
    require(len(b)<=MAX_REVIEW_TEXT_BYTES,"BLOCKED_REVIEW_PAYLOAD_TOO_LARGE")

def persist_atomic(path:Path,record:dict)->None:
    path=Path(path)
    data=canonical(record)+b"\n"
    require(len(data)<=MAX_PROVIDER_BODY_BYTES+MAX_REVIEW_TEXT_BYTES+8192,"BLOCKED_PERSISTED_RESULT_TOO_LARGE")
    path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    temp=path.parent/("."+path.name+".tmp."+uuid.uuid4().hex)
    fd=None
    try:
        fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
        st=os.fstat(fd)
        require(stat.S_ISREG(st.st_mode),"BLOCKED_PERSIST_NOT_REGULAR")
        off=0
        while off<len(data):
            n=os.write(fd,data[off:])
            require(type(n) is int and n>0,"BLOCKED_PERSIST_WRITE")
            off+=n
        require(off==len(data),"BLOCKED_PERSIST_WRITE")
        os.fsync(fd); os.close(fd); fd=None
        os.replace(temp,path)
        dfd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
        try: os.fsync(dfd)
        finally: os.close(dfd)
    except PersistenceError:
        raise
    except OSError:
        raise PersistenceError("BLOCKED_RESULT_PERSISTENCE") from None
    finally:
        if fd is not None:
            try: os.close(fd)
            except OSError: pass
        try:
            if temp.exists(): temp.unlink()
        except OSError: pass

def read_and_validate(path:Path,**identity)->dict:
    try: raw=Path(path).read_bytes()
    except OSError: raise PersistenceError("BLOCKED_PERSISTED_RESULT_UNAVAILABLE") from None
    require(len(raw)>0 and len(raw)<=MAX_PROVIDER_BODY_BYTES+MAX_REVIEW_TEXT_BYTES+8192,
            "BLOCKED_PERSISTED_RESULT_TOO_LARGE")
    try: obj=json.loads(raw.decode("utf-8"))
    except Exception: raise PersistenceError("BLOCKED_PERSISTED_RESULT_MALFORMED") from None
    validate_record(obj,**identity)
    return obj
