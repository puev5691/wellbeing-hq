#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib, json, tarfile, io, gzip, shutil

PASS="PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY"

class ServiceError(RuntimeError): pass
def require(ok, code):
    if not ok: raise ServiceError(code)
def sha256_bytes(data:bytes)->str: return hashlib.sha256(data).hexdigest()
def canon(obj)->bytes: return (json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()

@dataclass(frozen=True)
class InputIdentity:
    source_id:str
    source_path:str
    target_path:str
    sha256:str
    size:int
    def __post_init__(self):
        require(type(self.source_id) is str and self.source_id,"BAD_INPUT_ID")
        require(type(self.source_path) is str and self.source_path and not self.source_path.startswith("/") and ".." not in Path(self.source_path).parts,"BAD_SOURCE_PATH")
        require(type(self.target_path) is str and self.target_path and not self.target_path.startswith("/") and ".." not in Path(self.target_path).parts,"BAD_TARGET_PATH")
        require(type(self.sha256) is str and len(self.sha256)==64 and all(c in "0123456789abcdef" for c in self.sha256),"BAD_SHA256")
        require(type(self.size) is int and not isinstance(self.size,bool) and self.size>=0,"BAD_SIZE")

@dataclass(frozen=True)
class PackageRequest:
    request_id:str
    package_id:str
    inputs:tuple[InputIdentity,...]
    prior_manifest_path:str|None=None
    create_archive:bool=True
    git_adapter_enabled:bool=False
    def __post_init__(self):
        require(type(self.request_id) is str and self.request_id,"BAD_REQUEST_ID")
        require(type(self.package_id) is str and self.package_id,"BAD_PACKAGE_ID")
        require(type(self.inputs) is tuple and len(self.inputs)>0,"BAD_INPUTS")
        targets=[x.target_path for x in self.inputs]
        require(len(targets)==len(set(targets)),"DUPLICATE_TARGET")
        require(self.git_adapter_enabled is False,"GIT_ADAPTER_DISABLED")

class GitAdapter:
    enabled=False
    def publish(self,*_args,**_kwargs):
        raise ServiceError("GIT_ADAPTER_DISABLED")

def parse_request(data:bytes)->PackageRequest:
    try: obj=json.loads(data.decode("utf-8"))
    except Exception: raise ServiceError("BAD_REQUEST_JSON") from None
    require(type(obj) is dict and set(obj)=={"schema","request_id","package_id","inputs","prior_manifest_path","create_archive","git_adapter_enabled"},"BAD_REQUEST_SCHEMA")
    require(obj["schema"]=="file-artifact-service-request-r01","BAD_REQUEST_SCHEMA")
    require(type(obj["inputs"]) is list,"BAD_INPUTS")
    inputs=[]
    for x in obj["inputs"]:
        require(type(x) is dict and set(x)=={"source_id","source_path","target_path","sha256","size"},"BAD_INPUT_SCHEMA")
        inputs.append(InputIdentity(**x))
    return PackageRequest(obj["request_id"],obj["package_id"],tuple(inputs),obj["prior_manifest_path"],obj["create_archive"],obj["git_adapter_enabled"])

def _read_verified(base:Path, ident:InputIdentity)->bytes:
    p=base/ident.source_path
    require(p.is_file(),"SOURCE_MISSING")
    data=p.read_bytes()
    require(len(data)==ident.size,"SOURCE_SIZE_MISMATCH")
    require(sha256_bytes(data)==ident.sha256,"SOURCE_HASH_MISMATCH")
    return data

def _manifest(package_id, inventory):
    return {"schema":"file-artifact-manifest-r01","package_id":package_id,"files":inventory,
            "authority_semantics":"none","project_state_semantics":"none","canonical_state":"not_claimed"}

def _archive_bytes(package_dir:Path, names:list[str])->bytes:
    raw=io.BytesIO()
    with tarfile.open(fileobj=raw,mode="w",format=tarfile.PAX_FORMAT) as tf:
        for rel in sorted(names):
            data=(package_dir/rel).read_bytes()
            ti=tarfile.TarInfo(rel);ti.size=len(data);ti.mtime=0;ti.uid=0;ti.gid=0;ti.uname="";ti.gname="";ti.mode=0o644
            tf.addfile(ti,io.BytesIO(data))
    out=io.BytesIO()
    with gzip.GzipFile(filename="",mode="wb",fileobj=out,mtime=0) as gz: gz.write(raw.getvalue())
    return out.getvalue()

def package_diff(old_manifest:dict|None,new_manifest:dict)->dict:
    old={x["path"]:x for x in (old_manifest or {}).get("files",[])}
    new={x["path"]:x for x in new_manifest["files"]}
    return {"added":sorted(set(new)-set(old)),"removed":sorted(set(old)-set(new)),
            "changed":sorted(p for p in set(old)&set(new) if old[p]["sha256"]!=new[p]["sha256"] or old[p]["size"]!=new[p]["size"]),
            "unchanged":sorted(p for p in set(old)&set(new) if old[p]["sha256"]==new[p]["sha256"] and old[p]["size"]==new[p]["size"])}

def execute(request_bytes:bytes, source_root:Path, output_root:Path)->dict:
    req=parse_request(request_bytes)
    package_dir=output_root/"package"
    if package_dir.exists(): shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True)
    inventory=[]
    for ident in sorted(req.inputs,key=lambda x:x.target_path):
        data=_read_verified(source_root,ident)
        dst=package_dir/ident.target_path;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(data)
        inventory.append({"path":ident.target_path,"sha256":sha256_bytes(data),"size":len(data),"source_id":ident.source_id})
    manifest=_manifest(req.package_id,inventory)
    manifest_bytes=canon(manifest)
    (package_dir/"MANIFEST.json").write_bytes(manifest_bytes)
    old=None
    if req.prior_manifest_path:
        p=source_root/req.prior_manifest_path
        require(p.is_file(),"PRIOR_MANIFEST_MISSING")
        try: old=json.loads(p.read_text(encoding="utf-8"))
        except Exception: raise ServiceError("BAD_PRIOR_MANIFEST") from None
    diff=package_diff(old,manifest)
    (output_root/"diff.json").write_bytes(canon(diff))
    names=[x["path"] for x in inventory]+["MANIFEST.json"]
    archive_sha=None
    if req.create_archive:
        arch=_archive_bytes(package_dir,names)
        (output_root/"package.tar.gz").write_bytes(arch);archive_sha=sha256_bytes(arch)
    readback=[]
    for rel in sorted(names):
        data=(package_dir/rel).read_bytes();readback.append({"path":rel,"sha256":sha256_bytes(data),"size":len(data)})
    readback_obj={"schema":"file-artifact-readback-r01","files":readback}
    (output_root/"readback.json").write_bytes(canon(readback_obj))
    result={"verdict":PASS,"request_id":req.request_id,"package_id":req.package_id,
            "files":len(inventory),"manifest_sha256":sha256_bytes(manifest_bytes),
            "archive_sha256":archive_sha,"diff":diff,"git_adapter":"disabled",
            "authority_semantics":"none","project_state_semantics":"none"}
    (output_root/"result.json").write_bytes(canon(result))
    return result

if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument("--request",type=Path,required=True);ap.add_argument("--source-root",type=Path,required=True);ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args();print(json.dumps(execute(a.request.read_bytes(),a.source_root,a.out),sort_keys=True))