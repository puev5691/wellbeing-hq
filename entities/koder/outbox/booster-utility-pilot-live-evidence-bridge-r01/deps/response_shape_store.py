from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib,json,os,re,stat,uuid

SCHEMA="wb.openai.booster.response_shape_diag.v2"
MAX_BODY_BYTES=16384
HEX64=re.compile(r"^[0-9a-f]{64}$")
HEX40=re.compile(r"^[0-9a-f]{40}$")
TOP_KEYS=frozenset({
 "schema","snapshot_sha256","provider","model","attempt_key","request_sha256","task_commit","task_blob",
 "writer_blob","plan_sha256","authority_sha256","http_status","response_bytes","response_sha256",
 "top_level_keys","output_count","output_items","requester_review_required","project_acceptance",
 "project_state_mutation","provider_writer_authority","gateway_writer_authority"
})
EVIDENCE_KEYS=TOP_KEYS-{"snapshot_sha256"}
ITEM_KEYS=frozenset({"index","type","keys","classification","role","content_count","content_items"})
CONTENT_KEYS=frozenset({"index","type","keys","classification"})
CLASSIFICATIONS=frozenset({
 "assistant_text","benign_metadata_or_reasoning_container","tool_action_request","tool_action_output","unknown"
})

class DiagnosticError(RuntimeError): pass
def need(v,c):
    if not v: raise DiagnosticError(c)
def canonical(v:Any)->bytes:
    try:return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    except Exception: raise DiagnosticError("BLOCKED_DIAG_SERIALIZATION") from None
def sha(v:bytes)->str:return hashlib.sha256(v).hexdigest()
def h64(v): return type(v) is str and HEX64.fullmatch(v) is not None
def h40(v): return type(v) is str and HEX40.fullmatch(v) is not None
def canonical_evidence(snapshot:dict)->bytes:
    need(type(snapshot) is dict,"BLOCKED_DIAG_SCHEMA")
    need(set(snapshot)==TOP_KEYS or set(snapshot)==EVIDENCE_KEYS,"BLOCKED_DIAG_SCHEMA_KEYS")
    evidence={k:snapshot[k] for k in EVIDENCE_KEYS}
    return canonical(evidence)
def snapshot_identity(snapshot:dict)->str:
    return sha(canonical_evidence(snapshot))

def classify_output_item(item:dict)->str:
    t=item.get("type")
    if t=="message": return "assistant_text" if item.get("role")=="assistant" else "unknown"
    if t in ("reasoning","reasoning_summary","metadata"): return "benign_metadata_or_reasoning_container"
    if t in ("function_call","tool_call","computer_call","web_search_call","file_search_call"): return "tool_action_request"
    if t in ("function_call_output","tool_call_output","computer_call_output"): return "tool_action_output"
    return "unknown"

def classify_content_item(c:dict)->str:
    t=c.get("type")
    if t=="output_text": return "assistant_text"
    if t in ("reasoning_text","summary_text","metadata"): return "benign_metadata_or_reasoning_container"
    if t in ("tool_call","function_call"): return "tool_action_request"
    if t in ("tool_result","function_call_output"): return "tool_action_output"
    return "unknown"

def structural_snapshot(*,body:bytes,attempt_key:str,request_sha256:str,task_commit:str,task_blob:str,
                        writer_blob:str,plan_sha256:str,authority_sha256:str,provider:str,model:str,
                        http_status:int)->dict:
    need(type(body) is bytes and 0<len(body)<=MAX_BODY_BYTES,"BLOCKED_DIAG_BODY_BOUND")
    need(h64(attempt_key) and h64(request_sha256) and h64(plan_sha256) and h64(authority_sha256),
         "BLOCKED_DIAG_IDENTITY")
    need(h40(task_commit) and h40(task_blob) and h40(writer_blob),"BLOCKED_DIAG_IDENTITY")
    need(provider=="openai" and type(model) is str and bool(model),"BLOCKED_DIAG_PROVIDER_MODEL")
    need(type(http_status) is int,"BLOCKED_DIAG_HTTP_STATUS")
    try: obj=json.loads(body.decode("utf-8"))
    except Exception: raise DiagnosticError("BLOCKED_DIAG_MALFORMED_JSON") from None
    need(type(obj) is dict,"BLOCKED_DIAG_RESPONSE_OBJECT")
    output=obj.get("output",[])
    need(type(output) is list,"BLOCKED_DIAG_OUTPUT_NOT_LIST")
    items=[]
    for i,item in enumerate(output):
        need(type(item) is dict,"BLOCKED_DIAG_ITEM_NOT_OBJECT")
        entry={"index":i,"type":item.get("type") if type(item.get("type")) is str else None,
               "keys":sorted(item.keys()),"classification":classify_output_item(item),
               "role":None,"content_count":None,"content_items":[]}
        if item.get("type")=="message":
            entry["role"]=item.get("role") if type(item.get("role")) is str else None
            content=item.get("content",[])
            need(type(content) is list,"BLOCKED_DIAG_CONTENT_NOT_LIST")
            entry["content_count"]=len(content)
            for j,c in enumerate(content):
                need(type(c) is dict,"BLOCKED_DIAG_CONTENT_NOT_OBJECT")
                entry["content_items"].append({
                    "index":j,
                    "type":c.get("type") if type(c.get("type")) is str else None,
                    "keys":sorted(c.keys()),
                    "classification":classify_content_item(c)
                })
        items.append(entry)
    evidence={
      "schema":SCHEMA,"provider":"openai","model":model,"attempt_key":attempt_key,
      "request_sha256":request_sha256,"task_commit":task_commit,"task_blob":task_blob,
      "writer_blob":writer_blob,"plan_sha256":plan_sha256,"authority_sha256":authority_sha256,
      "http_status":http_status,"response_bytes":len(body),"response_sha256":sha(body),
      "top_level_keys":sorted(obj.keys()),"output_count":len(output),"output_items":items,
      "requester_review_required":True,"project_acceptance":"NOT_GRANTED",
      "project_state_mutation":False,"provider_writer_authority":False,"gateway_writer_authority":False
    }
    evidence["snapshot_sha256"]=snapshot_identity(evidence)
    return evidence

def validate(snapshot:dict,*,expected_snapshot_sha256:str,**expected)->None:
    need(type(snapshot) is dict and set(snapshot)==TOP_KEYS,"BLOCKED_DIAG_SCHEMA_KEYS")
    need(snapshot["schema"]==SCHEMA,"BLOCKED_DIAG_SCHEMA")
    need(h64(expected_snapshot_sha256),"BLOCKED_DIAG_EXPECTED_SNAPSHOT_IDENTITY")
    need(h64(snapshot["snapshot_sha256"]),"BLOCKED_DIAG_SNAPSHOT_SHA")
    actual=snapshot_identity(snapshot)
    need(snapshot["snapshot_sha256"]==actual,"BLOCKED_DIAG_SNAPSHOT_TAMPER")
    need(actual==expected_snapshot_sha256,"BLOCKED_DIAG_SNAPSHOT_IDENTITY_MISMATCH")
    for k,v in expected.items(): need(snapshot.get(k)==v,"BLOCKED_DIAG_IDENTITY_MISMATCH")
    need(snapshot["provider"]=="openai" and type(snapshot["model"]) is str,"BLOCKED_DIAG_PROVIDER_MODEL")
    need(type(snapshot["http_status"]) is int,"BLOCKED_DIAG_HTTP_STATUS")
    need(type(snapshot["response_bytes"]) is int and snapshot["response_bytes"]>0,"BLOCKED_DIAG_RESPONSE_BYTES")
    need(h64(snapshot["response_sha256"]),"BLOCKED_DIAG_RESPONSE_SHA")
    need(type(snapshot["top_level_keys"]) is list and all(type(x) is str for x in snapshot["top_level_keys"]),
         "BLOCKED_DIAG_TOP_KEYS")
    need(type(snapshot["output_count"]) is int and snapshot["output_count"]==len(snapshot["output_items"]),
         "BLOCKED_DIAG_OUTPUT_COUNT")
    for idx,item in enumerate(snapshot["output_items"]):
        need(type(item) is dict and set(item)==ITEM_KEYS,"BLOCKED_DIAG_ITEM_SCHEMA")
        need(item["index"]==idx and type(item["keys"]) is list and item["classification"] in CLASSIFICATIONS,
             "BLOCKED_DIAG_ITEM_IDENTITY")
        need(all(type(x) is str for x in item["keys"]),"BLOCKED_DIAG_ITEM_KEYS")
        if item["type"]=="message":
            need(type(item["content_count"]) is int and item["content_count"]==len(item["content_items"]),
                 "BLOCKED_DIAG_CONTENT_COUNT")
            for j,c in enumerate(item["content_items"]):
                need(type(c) is dict and set(c)==CONTENT_KEYS,"BLOCKED_DIAG_CONTENT_SCHEMA")
                need(c["index"]==j and type(c["keys"]) is list and c["classification"] in CLASSIFICATIONS,
                     "BLOCKED_DIAG_CONTENT_IDENTITY")
                need(all(type(x) is str for x in c["keys"]),"BLOCKED_DIAG_CONTENT_KEYS")
        else:
            need(item["role"] is None and item["content_count"] is None and item["content_items"]==[],
                 "BLOCKED_DIAG_NONMESSAGE_CONTENT")
    need(snapshot["requester_review_required"] is True and snapshot["project_acceptance"]=="NOT_GRANTED",
         "FAIL_DIAG_AUTHORITY")
    need(snapshot["project_state_mutation"] is False and snapshot["provider_writer_authority"] is False
         and snapshot["gateway_writer_authority"] is False,"FAIL_DIAG_AUTHORITY")

def persist_atomic(path:Path,snapshot:dict)->None:
    data=canonical(snapshot)+b"\n"; path=Path(path); path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    tmp=path.parent/("."+path.name+".tmp."+uuid.uuid4().hex); fd=None
    try:
        fd=os.open(tmp,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
        need(stat.S_ISREG(os.fstat(fd).st_mode),"BLOCKED_DIAG_NOT_REGULAR")
        off=0
        while off<len(data):
            n=os.write(fd,data[off:]); need(type(n) is int and n>0,"BLOCKED_DIAG_WRITE"); off+=n
        need(off==len(data),"BLOCKED_DIAG_WRITE")
        os.fsync(fd); os.close(fd); fd=None
        os.replace(tmp,path)
        dfd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
        try: os.fsync(dfd)
        finally: os.close(dfd)
    except DiagnosticError: raise
    except OSError: raise DiagnosticError("BLOCKED_DIAG_PERSISTENCE") from None
    finally:
        if fd is not None:
            try: os.close(fd)
            except OSError: pass
        try:
            if tmp.exists(): tmp.unlink()
        except OSError: pass

def read_and_validate(path:Path,*,expected_snapshot_sha256:str,**expected)->dict:
    try: raw=Path(path).read_bytes()
    except OSError: raise DiagnosticError("BLOCKED_DIAG_READ") from None
    try: obj=json.loads(raw.decode())
    except Exception: raise DiagnosticError("BLOCKED_DIAG_READ_MALFORMED") from None
    validate(obj,expected_snapshot_sha256=expected_snapshot_sha256,**expected)
    return obj
