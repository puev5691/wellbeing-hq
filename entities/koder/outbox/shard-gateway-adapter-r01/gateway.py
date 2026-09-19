from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Mapping
import hashlib, json, os, stat, subprocess, threading

SCHEMA_REQUEST="wb.shard_gateway.request.v1"
SCHEMA_RESULT="wb.shard_gateway.result.v1"
SCHEMA_AUDIT="wb.shard_gateway.audit.v1"
MODE="VERIFY"
SERVICE_IDENTITY="arh-preserve"
MAX_REQUEST_BYTES=32768
MAX_OUTPUT_BYTES=1048576
MAX_DIR_ENTRIES=1000
MAX_ARCHIVE_ENTRIES=10000
HOST_ROOTS={
 "mazhor":{
  "MAZHOR_REPO_WELLBEING_HQ":"/data/wellbeing-lab/repos/wellbeing-hq",
  "MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01":"/data/wellbeing-lab/backups/shd-pre-reinit-v01"},
 "burzh":{"BURZH_REPO_WELLBEING_HQ":"/home/pev5691/wellbeing-hq"}}
ARCHIVE_ROOTS=frozenset({"MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01"})
DENIED_ABSOLUTE_PREFIXES=("/root","/etc","/proc","/sys","/dev","/run","/var/lib","/var/log",
 "/data/wellbeing-lab/secrets","/data/wellbeing-lab/logs","/data/wellbeing-lab/tmp",
 "/home/pev5691/openai-d0-runtime-r01")
DENIED_COMPONENTS=frozenset({".ssh",".gnupg",".aws",".config"})
DENIED_NAMES=("credential","secret","token","private-key")

class Opcode(str,Enum):
 STAT="STAT"; LIST_DIR="LIST_DIR"; READ_BOUNDED="READ_BOUNDED"; SHA256="SHA256"
 ARCHIVE_LIST="ARCHIVE_LIST"; GIT_STATUS_PORCELAIN="GIT_STATUS_PORCELAIN"; GIT_HEAD="GIT_HEAD"
 GIT_HEAD_TREE="GIT_HEAD_TREE"; GIT_LS_TREE="GIT_LS_TREE"; GIT_BLOB_META="GIT_BLOB_META"
 GIT_BLOB_READ_BOUNDED="GIT_BLOB_READ_BOUNDED"

class ErrorCode(str,Enum):
 OP_NOT_ALLOWED="OP_NOT_ALLOWED"; ROOT_NOT_ALLOWED="ROOT_NOT_ALLOWED"; HOST_NOT_ALLOWED="HOST_NOT_ALLOWED"
 ABSOLUTE_PATH_DENIED="ABSOLUTE_PATH_DENIED"; PATH_TRAVERSAL_DENIED="PATH_TRAVERSAL_DENIED"
 SYMLINK_NOT_ALLOWED="SYMLINK_NOT_ALLOWED"; DENIED_TARGET="DENIED_TARGET"; LIMIT_EXCEEDED="LIMIT_EXCEEDED"
 TIMEOUT="TIMEOUT"; TARGET_CHANGED="TARGET_CHANGED"; HOST_UNAVAILABLE="HOST_UNAVAILABLE"
 WRITE_MODE_NOT_AUTHORIZED="WRITE_MODE_NOT_AUTHORIZED"; BAD_REQUEST="BAD_REQUEST"
 NOT_REGULAR_FILE="NOT_REGULAR_FILE"; NOT_DIRECTORY="NOT_DIRECTORY"
 ARCHIVE_ROOT_REQUIRED="ARCHIVE_ROOT_REQUIRED"; GIT_ROOT_REQUIRED="GIT_ROOT_REQUIRED"
 OBJECT_NOT_VALIDATED="OBJECT_NOT_VALIDATED"; INTERNAL_ERROR="INTERNAL_ERROR"

TIMEOUTS={op:10 for op in Opcode}
TIMEOUTS[Opcode.SHA256]=60; TIMEOUTS[Opcode.ARCHIVE_LIST]=20
for op in (Opcode.GIT_STATUS_PORCELAIN,Opcode.GIT_HEAD,Opcode.GIT_HEAD_TREE,Opcode.GIT_LS_TREE,Opcode.GIT_BLOB_META,Opcode.GIT_BLOB_READ_BOUNDED): TIMEOUTS[op]=15

class GatewayError(RuntimeError):
 def __init__(self,code:ErrorCode): super().__init__(code.value); self.code=code

@dataclass(frozen=True)
class Request:
 schema:str; request_id:str; requester_entity:str; authority_ref:str; host_id:str; mode:str
 operation:str; root_id:str; relative_path:str=""; git_ref:str|None=None; git_object:str|None=None
 max_output_bytes:int=MAX_OUTPUT_BYTES; fallback_host_id:str|None=None; equivalent_object_ref:str|None=None

@dataclass(frozen=True)
class Result:
 schema:str; request_id:str; host_id:str; mode:str; operation:str; root_id:str; target_rel:str
 ok:bool; error_code:str|None; payload:Mapping[str,Any]; output_bytes:int; truncated:bool; fallback_used:bool=False

def canonical_bytes(v:Any)->bytes:
 return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()

def parse_request(raw:bytes)->Request:
 if type(raw) is not bytes or not 0<len(raw)<=MAX_REQUEST_BYTES: raise GatewayError(ErrorCode.BAD_REQUEST)
 try: obj=json.loads(raw.decode())
 except Exception: raise GatewayError(ErrorCode.BAD_REQUEST) from None
 if type(obj) is not dict: raise GatewayError(ErrorCode.BAD_REQUEST)
 allowed=set(Request.__dataclass_fields__)
 if set(obj)-allowed:
  if any(k in obj for k in ("command","cmd","shell")): raise GatewayError(ErrorCode.OP_NOT_ALLOWED)
  raise GatewayError(ErrorCode.BAD_REQUEST)
 try: req=Request(**obj)
 except Exception: raise GatewayError(ErrorCode.BAD_REQUEST) from None
 if req.mode=="WRITE": raise GatewayError(ErrorCode.WRITE_MODE_NOT_AUTHORIZED)
 if req.schema!=SCHEMA_REQUEST or req.mode!=MODE: raise GatewayError(ErrorCode.BAD_REQUEST)
 if req.host_id not in HOST_ROOTS: raise GatewayError(ErrorCode.HOST_NOT_ALLOWED)
 if req.root_id not in HOST_ROOTS[req.host_id]: raise GatewayError(ErrorCode.ROOT_NOT_ALLOWED)
 try: Opcode(req.operation)
 except ValueError: raise GatewayError(ErrorCode.OP_NOT_ALLOWED) from None
 if type(req.max_output_bytes) is not int or isinstance(req.max_output_bytes,bool) or not 1<=req.max_output_bytes<=MAX_OUTPUT_BYTES:
  raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
 if req.fallback_host_id is not None: raise GatewayError(ErrorCode.HOST_UNAVAILABLE)
 return req

def normalize_relative(p:str)->str:
 if type(p) is not str or "\x00" in p: raise GatewayError(ErrorCode.BAD_REQUEST)
 if p=="": return ""
 if PurePosixPath(p).is_absolute() or p.startswith(("/", "\\")): raise GatewayError(ErrorCode.ABSOLUTE_PATH_DENIED)
 parts=p.replace("\\","/").split("/")
 if any(x in ("",".","..") for x in parts): raise GatewayError(ErrorCode.PATH_TRAVERSAL_DENIED)
 lows=[x.lower() for x in parts]
 if any(x in DENIED_COMPONENTS for x in lows): raise GatewayError(ErrorCode.DENIED_TARGET)
 name=lows[-1]
 if name==".env" or any(x in name for x in DENIED_NAMES): raise GatewayError(ErrorCode.DENIED_TARGET)
 return "/".join(parts)

def denied_absolute(p:Path)->bool:
 s=p.as_posix()
 return any(s==x or s.startswith(x+"/") for x in DENIED_ABSOLUTE_PREFIXES) or any(x.lower() in DENIED_COMPONENTS for x in p.parts)

def resolve_no_symlink(root:Path,rel:str)->Path:
 rel=normalize_relative(rel); root=root.resolve(strict=True)
 if denied_absolute(root): raise GatewayError(ErrorCode.DENIED_TARGET)
 cur=root
 if rel:
  for part in rel.split("/"):
   cur=cur/part
   try: st=os.lstat(cur)
   except FileNotFoundError: raise GatewayError(ErrorCode.HOST_UNAVAILABLE) from None
   if stat.S_ISLNK(st.st_mode): raise GatewayError(ErrorCode.SYMLINK_NOT_ALLOWED)
 real=cur.resolve(strict=True)
 if real!=root and root not in real.parents: raise GatewayError(ErrorCode.PATH_TRAVERSAL_DENIED)
 if denied_absolute(real): raise GatewayError(ErrorCode.DENIED_TARGET)
 return real

class Concurrency:
 def __init__(self): self.locks={h:threading.BoundedSemaphore(1) for h in HOST_ROOTS}
CONCURRENCY=Concurrency()

def _bounded(data:bytes,limit:int)->bytes:
 if len(data)>min(limit,MAX_OUTPUT_BYTES): raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
 return data

def _ident(st): return (st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns)

class Gateway:
 def __init__(self,root_provider:Callable[[str,str],Path]|None=None):
  self.root_provider=root_provider or (lambda h,r:Path(HOST_ROOTS[h][r]))
 def execute(self,raw:bytes)->Result:
  try:
   req=parse_request(raw); op=Opcode(req.operation)
   with CONCURRENCY.locks[req.host_id]: payload=self._execute(req,op)
   return Result(SCHEMA_RESULT,req.request_id,req.host_id,MODE,op.value,req.root_id,normalize_relative(req.relative_path),True,None,payload,len(canonical_bytes(payload)),False)
  except GatewayError as e:
   return Result(SCHEMA_RESULT,"rejected","",MODE,"","","",False,e.code.value,{},0,False)
 def _execute(self,req,op):
  root=self.root_provider(req.host_id,req.root_id); target=resolve_no_symlink(root,req.relative_path)
  if op==Opcode.STAT:
   st=os.lstat(target); return {"type":("file" if stat.S_ISREG(st.st_mode) else "directory" if stat.S_ISDIR(st.st_mode) else "other"),"size":st.st_size,"mode":stat.S_IMODE(st.st_mode)}
  if op==Opcode.LIST_DIR:
   if not target.is_dir(): raise GatewayError(ErrorCode.NOT_DIRECTORY)
   names=sorted(x.name for x in target.iterdir())
   if len(names)>MAX_DIR_ENTRIES: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
   _bounded(canonical_bytes({"entries":names}),req.max_output_bytes); return {"entries":names}
  if op==Opcode.READ_BOUNDED: return {"text":self._read(target,req.max_output_bytes).decode("utf-8")}
  if op==Opcode.SHA256: return {"sha256":self._sha(target)}
  if op==Opcode.ARCHIVE_LIST:
   if req.root_id not in ARCHIVE_ROOTS: raise GatewayError(ErrorCode.ARCHIVE_ROOT_REQUIRED)
   import tarfile
   if not target.is_file(): raise GatewayError(ErrorCode.NOT_REGULAR_FILE)
   try:
    with tarfile.open(target,"r:*") as tf: names=[m.name for m in tf.getmembers()]
   except tarfile.TarError: raise GatewayError(ErrorCode.BAD_REQUEST) from None
   if len(names)>MAX_ARCHIVE_ENTRIES: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
   _bounded(canonical_bytes({"entries":names}),req.max_output_bytes); return {"entries":names}
  return self._git(req,op,root)
 def _read(self,target,limit):
  s1=os.lstat(target)
  if not stat.S_ISREG(s1.st_mode): raise GatewayError(ErrorCode.NOT_REGULAR_FILE)
  with open(target,"rb") as f: data=f.read(limit+1); s2=os.fstat(f.fileno())
  if _ident(s1)!=_ident(s2): raise GatewayError(ErrorCode.TARGET_CHANGED)
  return _bounded(data,limit)
 def _sha(self,target):
  s1=os.lstat(target)
  if not stat.S_ISREG(s1.st_mode): raise GatewayError(ErrorCode.NOT_REGULAR_FILE)
  h=hashlib.sha256()
  with open(target,"rb") as f:
   for c in iter(lambda:f.read(65536),b""): h.update(c)
   s2=os.fstat(f.fileno())
  if _ident(s1)!=_ident(s2): raise GatewayError(ErrorCode.TARGET_CHANGED)
  return h.hexdigest()
 def _run(self,argv,cwd,timeout,limit):
  try: cp=subprocess.run(argv,cwd=str(cwd),stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,env={"PATH":"/usr/bin:/bin","LC_ALL":"C"},timeout=timeout)
  except subprocess.TimeoutExpired: raise GatewayError(ErrorCode.TIMEOUT) from None
  if cp.returncode: raise GatewayError(ErrorCode.HOST_UNAVAILABLE)
  return _bounded(cp.stdout,limit)
 def _git(self,req,op,root):
  if "REPO_" not in req.root_id: raise GatewayError(ErrorCode.GIT_ROOT_REQUIRED)
  t=TIMEOUTS[op]; lim=req.max_output_bytes
  if op==Opcode.GIT_STATUS_PORCELAIN: return {"status":self._run(["git","status","--porcelain=v1","--untracked-files=no"],root,t,lim).decode()}
  if op==Opcode.GIT_HEAD: return {"head":self._run(["git","rev-parse","HEAD"],root,t,lim).decode().strip()}
  if op==Opcode.GIT_HEAD_TREE: return {"tree":self._run(["git","rev-parse","HEAD^{tree}"],root,t,lim).decode().strip()}
  if op==Opcode.GIT_LS_TREE:
   ref=req.git_ref or "HEAD"
   if ref!="HEAD":
    if not (len(ref)==40 and all(c in "0123456789abcdef" for c in ref)): raise GatewayError(ErrorCode.BAD_REQUEST)
    self._run(["git","merge-base","--is-ancestor",ref,"HEAD"],root,t,64)
   return {"tree":self._run(["git","ls-tree","-r",ref],root,t,lim).decode()}
  if op in (Opcode.GIT_BLOB_META,Opcode.GIT_BLOB_READ_BOUNDED):
   if not req.git_object or not req.git_ref or not req.relative_path: raise GatewayError(ErrorCode.OBJECT_NOT_VALIDATED)
   if not (len(req.git_object)==40 and all(c in "0123456789abcdef" for c in req.git_object)): raise GatewayError(ErrorCode.OBJECT_NOT_VALIDATED)
   ent=self._run(["git","ls-tree",req.git_ref,"--",normalize_relative(req.relative_path)],root,t,lim).decode().strip().split()
   if len(ent)<3 or ent[1]!="blob" or ent[2]!=req.git_object: raise GatewayError(ErrorCode.OBJECT_NOT_VALIDATED)
   size=int(self._run(["git","cat-file","-s",req.git_object],root,t,64))
   if op==Opcode.GIT_BLOB_META: return {"object":req.git_object,"type":"blob","size":size}
   if size>lim: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
   return {"object":req.git_object,"text":self._run(["git","cat-file","blob",req.git_object],root,t,lim).decode()}
  raise GatewayError(ErrorCode.OP_NOT_ALLOWED)

def serialize_result(r:Result)->bytes: return canonical_bytes(asdict(r))
def serialize_audit(req:Request,r:Result,duration_ms:int)->bytes:
 return canonical_bytes({"schema":SCHEMA_AUDIT,"request_id":r.request_id,"requester_entity":req.requester_entity,
 "authority_ref":req.authority_ref,"host_id":req.host_id,"service_identity":SERVICE_IDENTITY,"mode":MODE,
 "operation":req.operation,"root_id":req.root_id,"target_rel":normalize_relative(req.relative_path),
 "target_digest":r.payload.get("sha256") if r.ok else None,"result_digest":hashlib.sha256(serialize_result(r)).hexdigest(),
 "exit_status":0 if r.ok else 1,"error_code":r.error_code,"duration_ms":int(duration_ms),
 "output_bytes":r.output_bytes,"truncated":r.truncated})
