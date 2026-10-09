from __future__ import annotations
from typing import Mapping
from sandbox_profile import *
from sandbox_profile import _dig

class EphemeralFileSandboxEffectAdapterR01:
 def pre_effect(self,binding,current,frontier,prior='NONE'):
  ok,r=runtime_binding_verdict(binding,current,frontier)
  if prior=='UNRESOLVED':ok=False;r+=['UNRESOLVED_PRIOR_EFFECT']
  return {'classification':'READY_FOR_PRIMITIVE_INVOCATION' if ok else 'NOT_EXECUTED','reasons':sorted(set(r)),'real_effect_executed':False,'primitive_plan':self.plan(binding) if ok else None}
 def plan(self,b): return [{'step':'ROOT','primitive':'fstat/statx(root_dirfd)'},{'step':'CREATE','primitive':'openat2(root_dirfd, exact_leaf, O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC, RESOLVE_BENEATH|RESOLVE_NO_SYMLINKS|RESOLVE_NO_MAGICLINKS|RESOLVE_NO_XDEV)'},{'step':'IDENTITY','primitive':'retained fd + fstat/statx dev+ino+mount-id'},{'step':'READBACK','primitive':'write/read/hash retained fd'},{'step':'OUTCOME','primitive':'evidence classification only'}]
 def classify(self,o):
  if o.get('effect_attempted') is not True:return 'UNRESOLVED' if o.get('mutation_possible') else 'NOT_EXECUTED'
  if o.get('mutation_possible') and not o.get('created_identity_proven'):return 'UNRESOLVED'
  need=('created_identity_proven','same_object_write','same_object_stat','same_object_readback','same_object_hash','regular_file_proven','no_symlink_reparse_proven','non_replacement_proven','payload_digest_match','length_match')
  if all(o.get(k) is True for k in need):return 'EVIDENCED_SUCCESS'
  return 'EVIDENCED_FAILURE' if o.get('observed_failure_evidence') and not o.get('mutation_possible') else 'UNRESOLVED'
 def created_identity(self,o,b):
  need=('operation_key','attempt_id','stable_object_identity','open_reference_class','ownership_evidence','creation_evidence','payload_digest','expected_length','maximum_length','hardlink_replacement_evidence','no_symlink_reparse_evidence')
  miss=[k for k in need if not o.get(k)]
  if miss: raise SandboxError('CREATED_IDENTITY_MISSING:'+','.join(miss))
  x={'created_identity_id':None,'operation_key':o['operation_key'],'attempt_id':o['attempt_id'],'sandbox_target_id':b['root_identity']['sandbox_target_id'],'confinement_id':CONFINEMENT_ID,'confinement_version':CONFINEMENT_VERSION,'root_identity_id':b['root_identity_id'],'exact_leaf_name':b['exact_leaf_name'],'stable_object_identity':o['stable_object_identity'],'open_reference_class':o['open_reference_class'],'object_type':'REGULAR_FILE','ownership_evidence':o['ownership_evidence'],'creation_evidence':o['creation_evidence'],'no_symlink_reparse_evidence':o['no_symlink_reparse_evidence'],'payload_digest':o['payload_digest'],'expected_length':o['expected_length'],'maximum_length':o['maximum_length'],'platform_id':PLATFORM_ID,'hardlink_replacement_evidence':o['hardlink_replacement_evidence']}
  x['created_identity_id']=_dig({k:v for k,v in x.items() if k!='created_identity_id'}); return x

class ObjectBoundCleanupR02:
 def eligibility(self,*,binding,created,state,platform):
  if state.get('effect_outcome')=='UNRESOLVED' or state.get('post_mutation_identity_ambiguity'):return {'classification':'UNRESOLVED','reasons':['UNRESOLVED_IDENTITY_OR_OUTCOME']}
  r=[]
  if not state.get('terminal_effect_evidence_durable'):r+=['TERMINAL_EVIDENCE_NOT_DURABLE']
  if state.get('effect_outcome') not in ('EVIDENCED_SUCCESS','EVIDENCED_FAILURE','NOT_EXECUTED'):r+=['EFFECT_OUTCOME_MISSING']
  if not created:r+=['CREATED_OBJECT_IDENTITY_MISSING']
  if state.get('root_identity_id')!=binding.get('root_identity_id'):r+=['ROOT_IDENTITY_CHANGED']
  if state.get('parent_identity_unchanged') is not True:r+=['PARENT_IDENTITY_UNKNOWN']
  if created and state.get('current_leaf_identity')!=created.get('stable_object_identity'):r+=['CURRENT_LEAF_IDENTITY_MISMATCH']
  if created and state.get('operation_key')!=created.get('operation_key'):r+=['CLEANUP_OPERATION_KEY_MISMATCH']
  if created and state.get('owner_attempt_id')!=created.get('attempt_id'):r+=['CLEANUP_OWNER_ATTEMPT_MISMATCH']
  if created and created.get('root_identity_id')!=binding.get('root_identity_id'):r+=['CREATED_ROOT_IDENTITY_MISMATCH']
  if created and created.get('sandbox_target_id')!=(binding.get('root_identity') or {}).get('sandbox_target_id'):r+=['CREATED_SANDBOX_TARGET_MISMATCH']
  for k in ('leaf_regular_file','no_symlink_reparse_substitution','cleanup_scope_separately_bound'):
   if state.get(k) is not True:r+=['CLEANUP_PROOF_MISSING:'+k]
  if state.get('confinement_version')!=CONFINEMENT_VERSION:r+=['CONFINEMENT_VERSION_MISMATCH']
  pv=platform_verdict(platform); r+=pv['reasons']
  unknown={'EFFECT_OUTCOME_MISSING','CREATED_OBJECT_IDENTITY_MISSING','PARENT_IDENTITY_UNKNOWN'}
  if r:return {'classification':'UNKNOWN' if all(x in unknown for x in r) else 'BLOCKED','reasons':sorted(set(r))}
  return {'classification':'ELIGIBLE','reasons':[],'primitive_plan':['revalidate root/parent','verify current leaf identity under anchored dirfd','unlinkat(anchored_dirfd, exact_leaf, 0)','prove anchored absence and unchanged root/parent']}
 def post_cleanup(self,e):
  if e.get('cleanup_transport_ambiguous'):return 'UNKNOWN'
  return 'PASS' if all(e.get(k) is True for k in ('exact_leaf_absent','root_identity_unchanged','parent_identity_unchanged','no_unexpected_sibling_parent_mutation')) else 'UNKNOWN'
