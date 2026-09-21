from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib, json, os, re, stat, uuid

SCHEMA="wb.openai.booster.review_result.v2"
PARSER_STATUS="NORMALIZED_ASSISTANT_TEXT_EXACT_FROM_RESPONSE_EVIDENCE"
MAX_PROVIDER_BODY_BYTES=16384
MAX_REVIEW_TEXT_BYTES=8192
HEX64=re.compile(r"^[0-9a-f]{64}$")
HEX40=re.compile(r"^[0-9a-f]{40}$")
TOP_KEYS=frozenset({
 "schema","attempt_key","request_sha256","task_commit","task_blob","writer_blob",
 "plan_sha256","authority_sha256","provider","model","http_status","provider_calls",
 "retries","fallback","response_evidence","response_bytes","response_sha256",
 "parser_status","review_payload","requester_review_required","project_acceptance",
 "project_state_mutation","provider_writer_authority","gateway_writer_authority"
})
EVIDENCE_KEYS=frozenset({"model","output"})
REVIEW_KEYS=frozenset({"kind","text","bytes","sha256"})

class PersistenceError(RuntimeError): pass
def require(ok:bool,code:str):
    if not ok: raise PersistenceError(code)
def canonical(v:Any)->bytes:
    try: return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")
    except Exception: raise PersistenceError("BLOCKED_RESULT_SERIALIZATION") from None
def sha256_bytes(v:bytes)->str: return hashlib.sha256(v).hexdigest()
def _is_int(v): return type(v) is int
def _hex64(v): return type(v) is str and HEX64.fullmatch(v) is not None
def _hex40(v): return type(v) is str and HEX40.fullmatch(v) is not None

def _extract_review_text(evidence:dict,expected_model:str)->str:
    require(type(evidence) is dict and set(evidence)==EVIDENCE_KEYS,"BLOCKED_RESPONSE_EVIDENCE_SCHEMA")
    require(evidence["model"]==expected_model,"BLOCKED_MODEL_MISMATCH")
    output=evidence["output"]
    require(type(output) is list and output,"BLOCKED_PROVIDER_RESPONSE")
    parts=[]
    for item in output:
        require(type(item) is dict and set(item)=={"type","role","content"},"BLOCKED_PROVIDER_RESPONSE")
        require(item["type"]=="message" and item["role"]=="assistant","BLOCKED_UNEXPECTED_PROVIDER_ACTION")
        content=item["content"]
        require(type(content) is list and content,"BLOCKED_PROVIDER_RESPONSE")
        for c in content:
            require(type(c) is dict and set(c)=={"type","text"},"BLOCKED_PROVIDER_RESPONSE")
            require(c["type"]=="output_text","BLOCKED_UNEXPECTED_PROVIDER_ACTION")
            require(type(c["text"]) is str,"BLOCKED_PROVIDER_RESPONSE")
            parts.append(c["text"])
    text="\n".join(parts)
    require(bool(text.strip()),"BLOCKED_EMPTY_REVIEW_PAYLOAD")
    require(len(text.encode("utf-8"))<=MAX_REVIEW_TEXT_BYTES,"BLOCKED_REVIEW_PAYLOAD_TOO_LARGE")
    return text

def _normalize_evidence(obj:dict,expected_model:str)->dict:
    require(type(obj) is dict,"BLOCKED_MALFORMED_PROVIDER_RESPONSE")
    require(obj.get("model")==expected_model,"BLOCKED_MODEL_MISMATCH")
    output=obj.get("output")
    require(type(output) is list and output,"BLOCKED_PROVIDER_RESPONSE")
    normalized=[]
    for item in output:
        require(type(item) is dict,"BLOCKED_PROVIDER_RESPONSE")
        require(item.get("type")=="message" and item.get("role")=="assistant","BLOCKED_UNEXPECTED_PROVIDER_ACTION")
        content=item.get("content")
        require(type(content) is list and content,"BLOCKED_PROVIDER_RESPONSE")
        norm_content=[]
        for c in content:
            require(type(c) is dict and c.get("type")=="output_text" and type(c.get("text")) is str,
                    "BLOCKED_UNEXPECTED_PROVIDER_ACTION")
            norm_content.append({"type":"output_text","text":c["text"]})
        normalized.append({"type":"message","role":"assistant","content":norm_content})
    evidence={"model":expected_model,"output":normalized}
    _extract_review_text(evidence,expected_model)
    return evidence

def normalize_openai_result(*,body:bytes,attempt_key:str,request_sha256:str,task_commit:str,
                            task_blob:str,writer_blob:str,plan_sha256:str,authority_sha256:str,
                            provider:str,model:str,http_status:int,provider_calls:int,retries:int,
                            fallback:str)->dict:
    require(type(body) is bytes and 0<len(body)<=MAX_PROVIDER_BODY_BYTES,"BLOCKED_RESPONSE_TOO_LARGE")
    require(_hex64(attempt_key) and _hex64(request_sha256) and _hex64(plan_sha256) and _hex64(authority_sha256),
            "BLOCKED_RESULT_IDENTITY")
    require(_hex40(task_commit) and _hex40(task_blob) and _hex40(writer_blob),"BLOCKED_RESULT_IDENTITY")
    require(provider=="openai","BLOCKED_PROVIDER_MISMATCH")
    require(type(model) is str and bool(model),"BLOCKED_MODEL_MISMATCH")
    require(type(http_status) is int and http_status==200,"BLOCKED_HTTP_STATUS")
    require(provider_calls==1 and retries==0 and fallback=="none","BLOCKED_RETRY_FALLBACK_POLICY")
    try: obj=json.loads(body.decode("utf-8"))
    except Exception: raise PersistenceError("BLOCKED_MALFORMED_PROVIDER_RESPONSE") from None
    evidence=_normalize_evidence(obj,model)
    text=_extract_review_text(evidence,model)
    evidence_bytes=canonical(evidence)
    text_bytes=text.encode("utf-8")
    return {
      "schema":SCHEMA,"attempt_key":attempt_key,"request_sha256":request_sha256,
      "task_commit":task_commit,"task_blob":task_blob,"writer_blob":writer_blob,
      "plan_sha256":plan_sha256,"authority_sha256":authority_sha256,
      "provider":"openai","model":model,"http_status":200,"provider_calls":1,
      "retries":0,"fallback":"none","response_evidence":evidence,
      "response_bytes":len(evidence_bytes),"response_sha256":sha256_bytes(evidence_bytes),
      "parser_status":PARSER_STATUS,
      "review_payload":{"kind":"assistant_text","text":text,"bytes":len(text_bytes),"sha256":sha256_bytes(text_bytes)},
      "requester_review_required":True,"project_acceptance":"NOT_GRANTED",
      "project_state_mutation":False,"provider_writer_authority":False,"gateway_writer_authority":False
    }

def validate_record(record:dict,*,attempt_key:str,request_sha256:str,task_commit:str,task_blob:str,
                    writer_blob:str,plan_sha256:str,authority_sha256:str,provider:str,model:str)->None:
    require(type(record) is dict,"BLOCKED_RESULT_SCHEMA")
    require(set(record)==TOP_KEYS,"BLOCKED_RESULT_KEY_SET")
    require(record["schema"]==SCHEMA,"BLOCKED_RESULT_SCHEMA")
    require(_hex64(record["attempt_key"]) and _hex64(record["request_sha256"]) and
            _hex64(record["plan_sha256"]) and _hex64(record["authority_sha256"]),"BLOCKED_RESULT_IDENTITY")
    require(_hex40(record["task_commit"]) and _hex40(record["task_blob"]) and _hex40(record["writer_blob"]),
            "BLOCKED_RESULT_IDENTITY")
    expected={"attempt_key":attempt_key,"request_sha256":request_sha256,"task_commit":task_commit,
              "task_blob":task_blob,"writer_blob":writer_blob,"plan_sha256":plan_sha256,
              "authority_sha256":authority_sha256,"provider":provider,"model":model}
    for k,v in expected.items(): require(record[k]==v,"BLOCKED_RESULT_IDENTITY_MISMATCH")
    require(record["provider"]=="openai" and type(record["model"]) is str and bool(record["model"]),
            "BLOCKED_PROVIDER_MODEL")
    require(type(record["http_status"]) is int and record["http_status"]==200,"BLOCKED_HTTP_STATUS")
    require(_is_int(record["provider_calls"]) and record["provider_calls"]==1 and
            _is_int(record["retries"]) and record["retries"]==0 and record["fallback"]=="none",
            "BLOCKED_RETRY_FALLBACK_POLICY")
    require(record["parser_status"]==PARSER_STATUS,"BLOCKED_PARSER_STATUS")
    evidence=record["response_evidence"]
    text=_extract_review_text(evidence,record["model"])
    evidence_bytes=canonical(evidence)
    require(_is_int(record["response_bytes"]) and record["response_bytes"]==len(evidence_bytes),
            "BLOCKED_RESPONSE_BYTES_MISMATCH")
    require(_hex64(record["response_sha256"]) and record["response_sha256"]==sha256_bytes(evidence_bytes),
            "BLOCKED_RESPONSE_SHA256_MISMATCH")
    rp=record["review_payload"]
    require(type(rp) is dict and set(rp)==REVIEW_KEYS,"BLOCKED_REVIEW_PAYLOAD_SCHEMA")
    require(rp["kind"]=="assistant_text" and type(rp["text"]) is str and rp["text"]==text,
            "BLOCKED_REVIEW_PAYLOAD")
    text_bytes=text.encode("utf-8")
    require(_is_int(rp["bytes"]) and rp["bytes"]==len(text_bytes) and
            _hex64(rp["sha256"]) and rp["sha256"]==sha256_bytes(text_bytes),
            "BLOCKED_REVIEW_PAYLOAD_IDENTITY")
    require(record["requester_review_required"] is True and record["project_acceptance"]=="NOT_GRANTED",
            "FAIL_RESULT_AUTHORITY")
    require(record["project_state_mutation"] is False and record["provider_writer_authority"] is False and
            record["gateway_writer_authority"] is False,"FAIL_RESULT_AUTHORITY")

def persist_atomic(path:Path,record:dict)->None:
    path=Path(path); data=canonical(record)+b"\n"
    require(len(data)<=MAX_PROVIDER_BODY_BYTES+MAX_REVIEW_TEXT_BYTES+8192,"BLOCKED_PERSISTED_RESULT_TOO_LARGE")
    path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    temp=path.parent/("."+path.name+".tmp."+uuid.uuid4().hex); fd=None
    try:
        fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
        require(stat.S_ISREG(os.fstat(fd).st_mode),"BLOCKED_PERSIST_NOT_REGULAR")
        off=0
        while off<len(data):
            n=os.write(fd,data[off:]); require(type(n) is int and n>0,"BLOCKED_PERSIST_WRITE"); off+=n
        require(off==len(data),"BLOCKED_PERSIST_WRITE")
        os.fsync(fd); os.close(fd); fd=None
        os.replace(temp,path)
        dfd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
        try: os.fsync(dfd)
        finally: os.close(dfd)
    except PersistenceError: raise
    except OSError: raise PersistenceError("BLOCKED_RESULT_PERSISTENCE") from None
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
