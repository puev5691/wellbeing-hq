from __future__ import annotations
import copy
from typing import Any, Mapping
from runtime_integration import ADMISSION_DOMAIN,INTENT_DOMAIN,EffectBoundaryVerifier,EffectIntentEmitter,PreEffectRevalidator,identity
from sandbox_adapter import ADAPTER_ID,canonical_binding_verdict,runtime_binding_verdict
class SandboxBoundEffectIntentEmitter:
 def emit(self,envelope,resolution,compiled,actor_binding,*,sandbox_effect_binding,required_outcome_evidence_mode):
  if not isinstance(sandbox_effect_binding,Mapping): return None
  canonical_ok,_=canonical_binding_verdict(sandbox_effect_binding)
  if not canonical_ok: return None
  base=EffectIntentEmitter().emit(envelope,resolution,compiled,actor_binding,adapter_class=ADAPTER_ID,required_outcome_evidence_mode=required_outcome_evidence_mode)
  if base is None:return None
  out=copy.deepcopy(base); out['sandbox_effect_binding']=copy.deepcopy(dict(sandbox_effect_binding)); out['sandbox_binding_id']=sandbox_effect_binding.get('binding_id'); out['sandbox_binding_evidence_versions']=copy.deepcopy(dict(sandbox_effect_binding.get('supporting_evidence_versions',{}))); out['intent_id']=identity(INTENT_DOMAIN,out,'intent_id'); return out
class SandboxBoundPreEffectRevalidator:
 def revalidate(self,intent,compiled,actor_binding,*,current_evidence_versions,expected_evidence_versions,adapter_authority,prior_effect_state,current_trust_policy_dependency,current_task_execution_binding,current_sandbox_effect_binding):
  base=PreEffectRevalidator().revalidate(intent,compiled,actor_binding,current_evidence_versions=current_evidence_versions,expected_evidence_versions=expected_evidence_versions,adapter_class=ADAPTER_ID,adapter_authority=adapter_authority,prior_effect_state=prior_effect_state,current_trust_policy_dependency=current_trust_policy_dependency,current_task_execution_binding=current_task_execution_binding)
  out=copy.deepcopy(base); sandbox=intent.get('sandbox_effect_binding'); ok,sandbox_reasons=runtime_binding_verdict(sandbox if isinstance(sandbox,Mapping) else None,current_sandbox_effect_binding,current_evidence_versions); reasons=set(out.get('revalidation_reason_ids',[])); reasons.update(sandbox_reasons)
  if not ok and not reasons:reasons.add('SANDBOX_BINDING_BLOCKED')
  out['revalidation_verdict']='NO_EFFECT_UNKNOWN' if reasons and any('UNKNOWN' in x for x in reasons) else ('NO_EFFECT_BLOCKED' if reasons else 'ADMIT_EFFECT_NOW')
  versions=dict((sandbox or {}).get('supporting_evidence_versions',{})); expected=dict(out.get('expected_current_evidence_versions',[])); expected.update({str(k):str(v) for k,v in versions.items()}); out['sandbox_effect_binding']=copy.deepcopy(dict(sandbox)) if isinstance(sandbox,Mapping) else None; out['sandbox_binding_id']=None if not isinstance(sandbox,Mapping) else sandbox.get('binding_id'); out['sandbox_binding_evidence_versions']=copy.deepcopy(versions); out['expected_current_evidence_versions']=sorted(expected.items()); out['revalidation_reason_ids']=sorted(reasons); out['admission_id']=identity(ADMISSION_DOMAIN,out,'admission_id'); return out
class SandboxBoundEffectBoundaryVerifier:
 def verify(self,intent,admission,invocation_evidence):
  base_ok,base_reasons=EffectBoundaryVerifier().verify(intent,admission,invocation_evidence,ADAPTER_ID); sandbox_ok,sandbox_reasons=runtime_binding_verdict(admission.get('sandbox_effect_binding'),invocation_evidence.get('sandbox_effect_binding'),dict(invocation_evidence.get('current_evidence_versions',{}))); reasons=sorted(set(base_reasons)|set(sandbox_reasons)); return base_ok and sandbox_ok and not reasons,reasons
