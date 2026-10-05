# C1-C3 static correction map

## C1
- added TrustPolicyBindingResolver;
- policy evidence must carry exact immutable locator/version, authoritative source class, VERIFIED/CURRENT, conflict NONE and provenance;
- policy evidence semantic payload must bind exact policy_ref/config digest;
- RuntimeEvidenceResolver rejects a TrustPolicy whose authoritative binding no longer validates;
- resolution records trust_policy_binding_id and evidence_id.

## C2
- PreEffectRevalidator verifies canonical intent payload digest and intent identity;
- adapter authority now requires exact immutable identity/version, VERIFIED/CURRENT and non-conflict;
- admission binds adapter authority snapshot digest/version;
- EffectAdapter signature now requires invocation_evidence;
- EffectBoundaryVerifier recomputes intent and admission identities at invocation;
- it compares exact evidence frontier, current adapter authority, current actor/Recovery binding and current prior-effect state;
- any mismatch/stale/UNKNOWN/conflict => NOT_EXECUTED.

## C3
- actor_binding_consistency rejects contradictory authoritative mutation / writer requirement / effect class semantics;
- actor_effect_eligibility consumes those consistency failures;
- invocation boundary normalizes and rechecks current actor binding and Recovery/freeze/handoff/replacement state.

Reviewed baseline core:
UNCHANGED.
