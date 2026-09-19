from __future__ import annotations
from contextlib import contextmanager
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Mapping
import errno
import hashlib
import json
import os
import re
import signal
import stat
import subprocess
import tarfile
import threading

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
DENIED_ABSOLUTE_PREFIXES=(
 "/root","/etc","/proc","/sys","/dev","/run","/var/lib","/var/log",
 "/data/wellbeing-lab/secrets","/data/wellbeing-lab/logs","/data/wellbeing-lab/tmp",
 "/home/pev5691/openai-d0-runtime-r01")
DENIED_COMPONENTS=frozenset({".ssh",".gnupg",".aws",".config"})
DENIED_NAMES=("credential","secret","token","private-key")
FULL_COMMIT_RE=re.compile(r"^[0-9a-f]{40}$")

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
 OBJECT_NOT_VALIDATED="OBJECT_NOT_VALIDATED"; REF_NOT_ALLOWED="REF_NOT_ALLOWED"
 BINARY_TEXT_NOT_ALLOWED="BINARY_TEXT_NOT_ALLOWED"; INTERNAL_ERROR="INTERNAL_ERROR"

TIMEOUTS={op:10.0 for op in Opcode}
TIMEOUTS[Opcode.SHA256]=60.0
TIMEOUTS[Opcode.ARCHIVE_LIST]=20.0
for op in (Opcode.GIT_STATUS_PORCELAIN,Opcode.GIT_HEAD,Opcode.GIT_HEAD_TREE,
           Opcode.GIT_LS_TREE,Opcode.GIT_BLOB_META,Opcode.GIT_BLOB_READ_BOUNDED):
    TIMEOUTS[op]=15.0

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
    ok:bool; error_code:str|None; payload:Mapping[str,Any]; output_bytes:int; truncated:bool
    fallback_used:bool=False

def canonical_bytes(v:Any)->bytes:
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")

def parse_request(raw:bytes)->Request:
    if type(raw) is not bytes or not 0<len(raw)<=MAX_REQUEST_BYTES:
        raise GatewayError(ErrorCode.BAD_REQUEST)
    try: obj=json.loads(raw.decode("utf-8"))
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
    if PurePosixPath(p).is_absolute() or p.startswith(("/", "\\")):
        raise GatewayError(ErrorCode.ABSOLUTE_PATH_DENIED)
    parts=p.replace("\\","/").split("/")
    if any(x in ("",".","..") for x in parts): raise GatewayError(ErrorCode.PATH_TRAVERSAL_DENIED)
    lows=[x.lower() for x in parts]
    if any(x in DENIED_COMPONENTS for x in lows): raise GatewayError(ErrorCode.DENIED_TARGET)
    name=lows[-1]
    if name==".env" or any(x in name for x in DENIED_NAMES): raise GatewayError(ErrorCode.DENIED_TARGET)
    return "/".join(parts)

def denied_absolute(p:Path)->bool:
    s=p.as_posix()
    return any(s==x or s.startswith(x+"/") for x in DENIED_ABSOLUTE_PREFIXES) or \
           any(x.lower() in DENIED_COMPONENTS for x in p.parts)

@contextmanager
def wall_deadline(seconds:float):
    if threading.current_thread() is not threading.main_thread() or not hasattr(signal,"setitimer"):
        raise GatewayError(ErrorCode.TIMEOUT)
    previous_handler=signal.getsignal(signal.SIGALRM)
    previous_timer=signal.getitimer(signal.ITIMER_REAL)
    def alarm(_sig,_frame): raise GatewayError(ErrorCode.TIMEOUT)
    signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,float(seconds))
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        signal.signal(signal.SIGALRM,previous_handler)
        if previous_timer!=(0.0,0.0):
            signal.setitimer(signal.ITIMER_REAL,*previous_timer)

def _map_open_error(e:OSError)->GatewayError:
    if e.errno in (errno.ELOOP,): return GatewayError(ErrorCode.SYMLINK_NOT_ALLOWED)
    if e.errno in (errno.ENOENT,errno.ENOTDIR): return GatewayError(ErrorCode.HOST_UNAVAILABLE)
    return GatewayError(ErrorCode.HOST_UNAVAILABLE)

def open_root_fd(root:Path)->int:
    root=root.resolve(strict=True)
    if denied_absolute(root): raise GatewayError(ErrorCode.DENIED_TARGET)
    try: return os.open(root,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
    except OSError as e: raise _map_open_error(e) from None

def open_relative_fd(root:Path,rel:str,*,want_dir:bool=False)->tuple[int,str]:
    rel=normalize_relative(rel)
    fd=open_root_fd(root)
    if rel=="": return fd,rel
    parts=rel.split("/")
    try:
        for part in parts[:-1]:
            try: nfd=os.open(part,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW,dir_fd=fd)
            except OSError as e: raise _map_open_error(e) from None
            os.close(fd); fd=nfd
        flags=os.O_RDONLY|os.O_NOFOLLOW|(os.O_DIRECTORY if want_dir else 0)
        try: nfd=os.open(parts[-1],flags,dir_fd=fd)
        except OSError as e: raise _map_open_error(e) from None
        os.close(fd)
        return nfd,rel
    except Exception:
        try: os.close(fd)
        except OSError: pass
        raise

class Concurrency:
    def __init__(self): self.locks={h:threading.BoundedSemaphore(1) for h in HOST_ROOTS}
CONCURRENCY=Concurrency()

def _bounded(data:bytes,limit:int)->bytes:
    if len(data)>min(limit,MAX_OUTPUT_BYTES): raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
    return data

def _decode_text(data:bytes)->str:
    try: return data.decode("utf-8")
    except UnicodeDecodeError: raise GatewayError(ErrorCode.BINARY_TEXT_NOT_ALLOWED) from None

def serialize_result(r:Result)->bytes: return canonical_bytes(asdict(r))

def _final_result(req:Request,op:Opcode,target_rel:str,payload:Mapping[str,Any])->Result:
    result=Result(SCHEMA_RESULT,req.request_id,req.host_id,MODE,op.value,req.root_id,target_rel,
                  True,None,payload,0,False)
    size=len(serialize_result(result))
    result=Result(**{**asdict(result),"output_bytes":size})
    final=serialize_result(result)
    if len(final)!=size:
        result=Result(**{**asdict(result),"output_bytes":len(final)})
        final=serialize_result(result)
    if len(final)>MAX_OUTPUT_BYTES: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
    return result

def validate_git_ref(run:Callable[...,bytes],root:Path,ref:str|None,timeout:float)->str:
    ref="HEAD" if ref is None else ref
    if ref=="HEAD": return ref
    if type(ref) is not str or not FULL_COMMIT_RE.fullmatch(ref):
        raise GatewayError(ErrorCode.REF_NOT_ALLOWED)
    try: run(["git","merge-base","--is-ancestor",ref,"HEAD"],root,timeout,64)
    except GatewayError:
        raise GatewayError(ErrorCode.REF_NOT_ALLOWED) from None
    return ref

class Gateway:
    def __init__(self,root_provider:Callable[[str,str],Path]|None=None):
        self.root_provider=root_provider or (lambda h,r:Path(HOST_ROOTS[h][r]))
    def execute(self,raw:bytes)->Result:
        req=None
        try:
            req=parse_request(raw); op=Opcode(req.operation)
            with CONCURRENCY.locks[req.host_id]:
                with wall_deadline(TIMEOUTS[op]):
                    payload,target_rel=self._execute(req,op)
                    return _final_result(req,op,target_rel,payload)
        except GatewayError as e:
            rid=req.request_id if req else "rejected"
            host=req.host_id if req else ""
            opv=req.operation if req else ""
            root=req.root_id if req else ""
            rel=""
            if req:
                try: rel=normalize_relative(req.relative_path)
                except GatewayError: rel=""
            return Result(SCHEMA_RESULT,rid,host,MODE,opv,root,rel,False,e.code.value,{},0,False)

    def _execute(self,req:Request,op:Opcode)->tuple[Mapping[str,Any],str]:
        root=self.root_provider(req.host_id,req.root_id)
        rel=normalize_relative(req.relative_path)
        if op==Opcode.STAT:
            fd,_=open_relative_fd(root,rel)
            try:
                st=os.fstat(fd)
                typ="file" if stat.S_ISREG(st.st_mode) else "directory" if stat.S_ISDIR(st.st_mode) else "other"
                return {"type":typ,"size":st.st_size,"mode":stat.S_IMODE(st.st_mode)},rel
            finally: os.close(fd)
        if op==Opcode.LIST_DIR:
            fd,_=open_relative_fd(root,rel,want_dir=True)
            try:
                names=sorted(os.listdir(fd))
                if len(names)>MAX_DIR_ENTRIES: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
                return {"entries":names},rel
            finally: os.close(fd)
        if op==Opcode.READ_BOUNDED:
            fd,_=open_relative_fd(root,rel)
            try: return {"text":_decode_text(self._read_fd(fd,req.max_output_bytes))},rel
            finally: os.close(fd)
        if op==Opcode.SHA256:
            fd,_=open_relative_fd(root,rel)
            try: return {"sha256":self._sha_fd(fd)},rel
            finally: os.close(fd)
        if op==Opcode.ARCHIVE_LIST:
            if req.root_id not in ARCHIVE_ROOTS: raise GatewayError(ErrorCode.ARCHIVE_ROOT_REQUIRED)
            fd,_=open_relative_fd(root,rel)
            try:
                st=os.fstat(fd)
                if not stat.S_ISREG(st.st_mode): raise GatewayError(ErrorCode.NOT_REGULAR_FILE)
                with os.fdopen(os.dup(fd),"rb",closefd=True) as fh:
                    try:
                        with tarfile.open(fileobj=fh,mode="r:*") as tf:
                            names=[m.name for m in tf.getmembers()]
                    except tarfile.TarError: raise GatewayError(ErrorCode.BAD_REQUEST) from None
                if len(names)>MAX_ARCHIVE_ENTRIES: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
                return {"entries":names},rel
            finally: os.close(fd)
        return self._git(req,op,root),rel

    def _read_fd(self,fd:int,limit:int)->bytes:
        st=os.fstat(fd)
        if not stat.S_ISREG(st.st_mode): raise GatewayError(ErrorCode.NOT_REGULAR_FILE)
        data=bytearray()
        while len(data)<=limit:
            chunk=os.read(fd,min(65536,limit+1-len(data)))
            if not chunk: break
            data.extend(chunk)
        return _bounded(bytes(data),limit)

    def _sha_fd(self,fd:int)->str:
        st=os.fstat(fd)
        if not stat.S_ISREG(st.st_mode): raise GatewayError(ErrorCode.NOT_REGULAR_FILE)
        h=hashlib.sha256()
        while True:
            chunk=os.read(fd,65536)
            if not chunk: break
            h.update(chunk)
        return h.hexdigest()

    def _run(self,argv,cwd,timeout,limit):
        try:
            cp=subprocess.run(argv,cwd=str(cwd),stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,
                              stderr=subprocess.DEVNULL,env={"PATH":"/usr/bin:/bin","LC_ALL":"C"},
                              timeout=timeout,check=False)
        except subprocess.TimeoutExpired: raise GatewayError(ErrorCode.TIMEOUT) from None
        if cp.returncode: raise GatewayError(ErrorCode.HOST_UNAVAILABLE)
        return _bounded(cp.stdout,limit)

    def _git(self,req:Request,op:Opcode,root:Path)->Mapping[str,Any]:
        if "REPO_" not in req.root_id: raise GatewayError(ErrorCode.GIT_ROOT_REQUIRED)
        t=TIMEOUTS[op]; lim=req.max_output_bytes
        if op==Opcode.GIT_STATUS_PORCELAIN:
            return {"status":_decode_text(self._run(["git","status","--porcelain=v1","--untracked-files=no"],root,t,lim))}
        if op==Opcode.GIT_HEAD:
            return {"head":_decode_text(self._run(["git","rev-parse","HEAD"],root,t,lim)).strip()}
        if op==Opcode.GIT_HEAD_TREE:
            return {"tree":_decode_text(self._run(["git","rev-parse","HEAD^{tree}"],root,t,lim)).strip()}
        ref=validate_git_ref(self._run,root,req.git_ref,t)
        if op==Opcode.GIT_LS_TREE:
            return {"tree":_decode_text(self._run(["git","ls-tree","-r",ref],root,t,lim))}
        if op in (Opcode.GIT_BLOB_META,Opcode.GIT_BLOB_READ_BOUNDED):
            if not req.git_object or not req.relative_path:
                raise GatewayError(ErrorCode.OBJECT_NOT_VALIDATED)
            if not FULL_COMMIT_RE.fullmatch(req.git_object):
                raise GatewayError(ErrorCode.OBJECT_NOT_VALIDATED)
            rel=normalize_relative(req.relative_path)
            ent=_decode_text(self._run(["git","ls-tree",ref,"--",rel],root,t,lim)).strip().split()
            if len(ent)<3 or ent[1]!="blob" or ent[2]!=req.git_object:
                raise GatewayError(ErrorCode.OBJECT_NOT_VALIDATED)
            size=int(_decode_text(self._run(["git","cat-file","-s",req.git_object],root,t,64)))
            if op==Opcode.GIT_BLOB_META:
                return {"object":req.git_object,"type":"blob","size":size}
            if size>lim: raise GatewayError(ErrorCode.LIMIT_EXCEEDED)
            return {"object":req.git_object,
                    "text":_decode_text(self._run(["git","cat-file","blob",req.git_object],root,t,lim))}
        raise GatewayError(ErrorCode.OP_NOT_ALLOWED)

def serialize_audit(req:Request,r:Result,duration_ms:int)->bytes:
    return canonical_bytes({
        "schema":SCHEMA_AUDIT,"request_id":r.request_id,"requester_entity":req.requester_entity,
        "authority_ref":req.authority_ref,"host_id":req.host_id,"service_identity":SERVICE_IDENTITY,
        "mode":MODE,"operation":req.operation,"root_id":req.root_id,
        "target_rel":normalize_relative(req.relative_path),
        "target_digest":r.payload.get("sha256") if r.ok else None,
        "result_digest":hashlib.sha256(serialize_result(r)).hexdigest(),
        "exit_status":0 if r.ok else 1,"error_code":r.error_code,
        "duration_ms":int(duration_ms),"output_bytes":r.output_bytes,"truncated":r.truncated})
