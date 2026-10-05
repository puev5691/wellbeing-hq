# Runtime integration R02 map

C1 trust root:
authoritative policy evidence -> TrustPolicyBindingResolver -> bound TrustPolicy -> RuntimeEvidenceResolver.

Caller configuration alone is insufficient.

C2 effect path:
EffectIntent -> PreEffectRevalidator -> PRE_EFFECT_ADMISSION -> Current invocation evidence -> EffectBoundaryVerifier -> EffectAdapter.

The adapter cannot execute from stale intent/admission alone.

Invocation evidence includes:
- current evidence versions;
- current adapter authority;
- current ACTOR_EXECUTION_BINDING / Recovery state;
- current prior-effect state.

Canonical intent payload/id and admission id are recomputed at invocation.

C3 actor path:
RuntimeInputAdapter -> normalized ACTOR_EXECUTION_BINDING -> contract -> intent -> admission -> invocation evidence recheck.

Contradictory authoritative-state/write/writer-requirement combinations are fail-closed.

NonLiveEffectAdapter still never performs an external effect.
MockEffectAdapter remains test-only/no-I/O.
