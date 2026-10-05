# R03 effect-sensitive dependency chain

Authoritative policy evidence
-> TrustPolicyBindingResolver
-> bound TrustPolicy
-> RUNTIME_EVIDENCE_RESOLUTION.trust_policy_dependency
-> Effective Context / ExecutionContract dependency
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> current invocation trust_policy_dependency
-> EffectBoundaryVerifier.

Actor/Writer/Recovery evidence
-> ActorExecutionBindingResolver
-> evidence-derived ACTOR_EXECUTION_BINDING
-> RUNTIME_EVIDENCE_RESOLUTION
-> Effective Context / ExecutionContract
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> current invocation actor binding + exact support versions
-> EffectBoundaryVerifier.

Any missing/UNKNOWN/conflict/stale/version mismatch:
NO_EFFECT / NOT_EXECUTED.

C2 canonical intent/admission verification remains unchanged in principle and preserved.
