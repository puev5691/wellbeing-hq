# R03 grounding correction map

## C1-R
- TrustPolicy now retains verified/current/conflict state as binding material.
- RUNTIME_EVIDENCE_RESOLUTION emits trust_policy_dependency containing:
  evidence_id, exact locator, exact version/blob, binding_id, verified/currentness/conflict state, authority source and provenance.
- ReviewedSeceCoreAdapter binds the dependency into Effective Context and ExecutionContract identities.
- ContractCompilerFacade preserves it.
- EffectIntent preserves it.
- PRE_EFFECT_ADMISSION preserves it and adds policy evidence/version to expected current frontier.
- EffectBoundaryVerifier requires current policy dependency and rejects version/currentness/conflict/binding changes.
- policy change requires new resolution/revalidation before effect eligibility.

## C3-R
- RuntimeInputAdapter now transports actor_execution_binding_claim only; it does not create an authoritative actor binding.
- ActorExecutionBindingResolver derives the binding from exact evidence.
- evidence support covers actor instance/role/mode, current-writer ref/state, writer requirement, mutation/effect class, writer/worker authority, Recovery, freeze, handoff and replacement.
- each support requires exact scope, authoritative source class, VERIFIED/CURRENT, conflict NONE, immutable identity/version and provenance.
- missing support => grounding UNKNOWN; conflicting support => grounding CONFLICT.
- actor binding identity includes supporting evidence refs/versions/locators and grounding digest.
- RUNTIME_EVIDENCE_RESOLUTION carries the derived binding and evidence versions.
- contract, intent, admission and invocation frontier preserve those identities/versions.
- actor_effect_eligibility rejects any non-RESOLVED grounding.

## C2
PASS boundary preserved.
Canonical intent/admission checks and invocation-time revalidation remain in EffectBoundaryVerifier.
Only C1-R/C3-R dependency data was added to the same verifier.
