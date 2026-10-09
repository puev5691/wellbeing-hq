from __future__ import annotations
import hashlib,json,re
from typing import Mapping,Any
ADAPTER_ID='EphemeralFileSandboxEffectAdapterR01'; ADAPTER_VERSION='R01'; EFFECT_CLASS='SANDBOX_EPHEMERAL_FILE_CREATE'
CONFINEMENT_ID='SECE_SANDBOX_CONFINEMENT_PROFILE_R02'; CONFINEMENT_VERSION='R02'; CONFINEMENT_BLOB='3e8e12a95f44db6c18a895d0ed83b69dc4b4ea6e'
CLEANUP_ID='OBJECT_BOUND_CLEANUP_R02'; CLEANUP_VERSION='R02'; CLEANUP_BLOB='3dab9da97c5cfb4a055f5d5967791105a657c231'
PLATFORM_ID='LINUX_POSIX_PRIVATE_TMPFS_OPENAT2_STATX_R01'; PLATFORM_VERSION='R01'
ROOT_IDENTITY_CLASS='DIRFD_STATX_DEV_INO_MNT_ID'
CREATED_OBJECT_IDENTITY_CLASS='RETAINED_FD_FSTAT_DEV_INO_MNT_ID'
CLEANUP_BINDING_CLASS='DIRFD_UNLINKAT_PLUS_EXCLUSIVE_NAMESPACE_MUTATION_CONTROL'
SAFE=re.compile(r'^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$')
class SandboxError(ValueError): pass
REQ_CAPS=('private_mount_namespace','attempt_owned_private_tmpfs','no_bind_exposure','no_foreign_writer_access','exclusive_namespace_mutation_control','serialized_effect_executor','anchored_root_dirfd','openat2_relative','resolve_beneath','resolve_no_symlinks','resolve_no_magiclinks','resolve_no_xdev','o_creat','o_excl','o_nofollow','o_cloexec','retained_created_fd','fstat_dev_ino','statx_mount_id','regular_file_proof','link_count_proof','fd_readback','fd_hash','unlinkat_dirfd','pre_unlink_identity_revalidation','post_unlink_anchored_absence','root_identity_revalidation','parent_identity_revalidation','empty_directory_anchored_proof','no_recursive_cleanup')

def _dig(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def leaf_verdict(n):
 r=[]
 if not isinstance(n,str): return False,['LEAF_NOT_STRING']
 if n in ('','.','..'): r+=['LEAF_EMPTY_OR_DOT']
 if '/' in n or '\\' in n:r+=['LEAF_SEPARATOR']
 if '\x00' in n:r+=['LEAF_NUL']
 if ':' in n:r+=['LEAF_NAMESPACE_COLON']
 if not SAFE.fullmatch(n):r+=['LEAF_OUTSIDE_SAFE_PROFILE_GRAMMAR']
 return not r,sorted(set(r))

class LinuxPosixProfileR01:
 required_caps={k:True for k in REQ_CAPS}
 def validate(self,e): return platform_verdict(e)

def platform_verdict(e:Mapping[str,Any]):
 r=[]
 exact=(('profile_id',PLATFORM_ID),('profile_version',PLATFORM_VERSION),('verified_state','VERIFIED'),('currentness_state','CURRENT'),('conflict_state','NONE'),('filename_encoding','UTF-8'),('namespace_isolation_class','PRIVATE_ATTEMPT_OWNED_TMPFS_MOUNT_NAMESPACE'),('root_identity_class',ROOT_IDENTITY_CLASS),('created_object_identity_class',CREATED_OBJECT_IDENTITY_CLASS),('cleanup_binding_class',CLEANUP_BINDING_CLASS))
 for k,v in exact:
  if e.get(k)!=v:r.append('PLATFORM_'+k.upper()+'_MISMATCH')
 if not e.get('supporting_evidence_versions'):r.append('PLATFORM_EVIDENCE_VERSIONS_MISSING')
 if not e.get('provenance'):r.append('PLATFORM_PROVENANCE_MISSING')
 caps=e.get('capabilities') or {}
 r += ['PLATFORM_CAPABILITY_UNPROVEN:'+k for k in REQ_CAPS if caps.get(k) is not True]
 return {'verdict':'PASS' if not r else 'BLOCKED','reasons':sorted(set(r))}

def root_identity(r):
 need=('sandbox_target_id','environment_instance_id','owner_attempt_id','stable_root_object_identity','expected_parent_identity','currentness_evidence_version','supporting_evidence_versions')
 miss=[k for k in need if not r.get(k)]
 reasons=['ROOT_FIELD_MISSING:'+k for k in miss]
 if r.get('object_type')!='DIRECTORY':reasons+=['ROOT_NOT_DIRECTORY']
 if r.get('verified_state')!='VERIFIED' or r.get('currentness_state')!='CURRENT' or r.get('conflict_state')!='NONE':reasons+=['ROOT_NOT_VERIFIED_CURRENT_CLEAR']
 if not r.get('ownership_evidence'):reasons+=['ROOT_OWNERSHIP_UNPROVEN']
 if not r.get('isolation_evidence'):reasons+=['ROOT_ISOLATION_UNPROVEN']
 if r.get('platform_evidence_profile_id')!=PLATFORM_ID:reasons+=['ROOT_PLATFORM_EVIDENCE_PROFILE_ID_MISMATCH']
 out=dict(r); out['identity_verdict']='PASS' if not reasons else 'BLOCKED'; out['identity_reasons']=sorted(set(reasons)); out['root_identity_id']=_dig({k:out.get(k) for k in sorted(out) if k!='root_identity_id'}); return out

def canonical_root_identity_verdict(value):
 if not isinstance(value,Mapping): return False,['ROOT_IDENTITY_MAPPING_MISSING'],None
 payload=dict(value); supplied=payload.pop('root_identity_id',None); payload.pop('identity_verdict',None); payload.pop('identity_reasons',None)
 recomputed=root_identity(payload); reasons=list(recomputed['identity_reasons'])
 if supplied!=recomputed['root_identity_id']:reasons+=['ROOT_IDENTITY_ID_NONCANONICAL']
 if value.get('identity_verdict')!='PASS':reasons+=['ROOT_IDENTITY_VERDICT_NOT_PASS']
 if list(value.get('identity_reasons') or []):reasons+=['ROOT_IDENTITY_REASONS_NOT_CLEAR']
 return not reasons,sorted(set(reasons)),recomputed

def canonical_binding_verdict(binding):
 if not isinstance(binding,Mapping):return False,['SANDBOX_BINDING_MISSING']
 r=[]
 exact={'effect_class':EFFECT_CLASS,'adapter_id':ADAPTER_ID,'adapter_version':ADAPTER_VERSION,'confinement_id':CONFINEMENT_ID,'confinement_version':CONFINEMENT_VERSION,'confinement_blob':CONFINEMENT_BLOB,'cleanup_id':CLEANUP_ID,'cleanup_version':CLEANUP_VERSION,'cleanup_blob':CLEANUP_BLOB,'platform_id':PLATFORM_ID,'platform_version':PLATFORM_VERSION,'created_object_identity_requirement':'MANDATORY','same_object_continuity_requirement':'MANDATORY','hardlink_replacement_evidence_requirement':'MANDATORY','currentness_state':'CURRENT','conflict_state':'NONE'}
 for k,v in exact.items():
  if binding.get(k)!=v:r+=['SANDBOX_BINDING_CONSTANT_MISMATCH:'+k]
 if not binding.get('adapter_blob'):r+=['SANDBOX_ADAPTER_BLOB_MISSING']
 if not binding.get('platform_blob'):r+=['SANDBOX_PLATFORM_BLOB_MISSING']
 _,leaf_reasons=leaf_verdict(binding.get('exact_leaf_name')); r+=leaf_reasons
 root=binding.get('root_identity'); root_ok,root_reasons,recomputed_root=canonical_root_identity_verdict(root); r+=root_reasons
 if root_ok and binding.get('root_identity_id')!=recomputed_root['root_identity_id']:r+=['SANDBOX_BINDING_ROOT_ID_MISMATCH']
 support=binding.get('supporting_evidence_versions')
 if not isinstance(support,Mapping) or not support:r+=['SANDBOX_SUPPORTING_EVIDENCE_VERSIONS_MISSING']
 supplied=binding.get('binding_id'); expected=_dig({k:v for k,v in binding.items() if k!='binding_id'})
 if supplied!=expected:r+=['SANDBOX_BINDING_ID_NONCANONICAL']
 return not r,sorted(set(r))

def build_binding(*,leaf,root,platform,adapter_blob,platform_blob):
 _,lr=leaf_verdict(leaf); pv=platform_verdict(platform); ri=root_identity(root); rs=lr+pv['reasons']+ri['identity_reasons']
 if rs: raise SandboxError('BINDING_BLOCKED:'+','.join(sorted(set(rs))))
 ev={**{str(k):str(v) for k,v in platform['supporting_evidence_versions'].items()},**{str(k):str(v) for k,v in root['supporting_evidence_versions'].items()}}
 b={'binding_id':None,'effect_class':EFFECT_CLASS,'adapter_id':ADAPTER_ID,'adapter_version':ADAPTER_VERSION,'adapter_blob':adapter_blob,'confinement_id':CONFINEMENT_ID,'confinement_version':CONFINEMENT_VERSION,'confinement_blob':CONFINEMENT_BLOB,'cleanup_id':CLEANUP_ID,'cleanup_version':CLEANUP_VERSION,'cleanup_blob':CLEANUP_BLOB,'platform_id':PLATFORM_ID,'platform_version':PLATFORM_VERSION,'platform_blob':platform_blob,'platform_verdict':'PASS','root_identity':ri,'root_identity_id':ri['root_identity_id'],'exact_leaf_name':leaf,'created_object_identity_requirement':'MANDATORY','same_object_continuity_requirement':'MANDATORY','hardlink_replacement_evidence_requirement':'MANDATORY','supporting_evidence_versions':dict(sorted(ev.items())),'currentness_state':'CURRENT','conflict_state':'NONE'}
 b['binding_id']=_dig({k:v for k,v in b.items() if k!='binding_id'}); ok,reasons=canonical_binding_verdict(b)
 if not ok: raise SandboxError('BINDING_NONCANONICAL:'+','.join(reasons))
 return b

def runtime_binding_verdict(admitted,current,frontier):
 if not isinstance(admitted,Mapping):return False,['SANDBOX_BINDING_MISSING']
 if not isinstance(current,Mapping):return False,['CURRENT_SANDBOX_BINDING_MISSING']
 r=[]; aok,ar=canonical_binding_verdict(admitted); cok,cr=canonical_binding_verdict(current)
 if not aok:r += ['ADMITTED_'+x for x in ar]
 if not cok:r += ['CURRENT_'+x for x in cr]
 if current.get('currentness_state')!='CURRENT':r+=['SANDBOX_BINDING_NOT_CURRENT']
 if current.get('conflict_state')!='NONE':r+=['SANDBOX_BINDING_CONFLICT']
 for k in ('binding_id','effect_class','adapter_id','adapter_version','adapter_blob','confinement_id','confinement_version','confinement_blob','cleanup_id','cleanup_version','cleanup_blob','platform_id','platform_version','platform_blob','root_identity_id','exact_leaf_name'):
  if current.get(k)!=admitted.get(k):r+=['SANDBOX_BINDING_CHANGED:'+k]
 av=dict(admitted.get('supporting_evidence_versions',{})); cv=dict(current.get('supporting_evidence_versions',{}))
 if av!=cv:r+=['SANDBOX_SUPPORTING_EVIDENCE_VERSIONS_CHANGED']
 r += ['SANDBOX_EVIDENCE_FRONTIER_CHANGED:'+k for k,v in av.items() if frontier.get(k)!=v]
 return not r,sorted(set(r))
