# Runtime integration map

C1 provenance/trust:
- RuntimeInputAdapter is transport-only and rejects adapter-asserted positive runtime facts.
- TrustPolicy is explicit/injected; source-class presence alone is insufficient.
- RuntimeEvidenceResolver requires exact immutable identity, trust basis, verified/current state where required, non-conflict, exact scope/value and provenance chain.
- missing support => ABSENT/UNKNOWN; competing trusted current values => CONFLICT; no winner-by-order.
- outcome evidence uses the same resolver.

C2 pre-effect admission:
- EffectIntentEmitter binds contract/context/action/scope/target/parameters plus category-specific authority/task/writer/Recovery/current-state/input/source evidence refs.
- PreEffectRevalidator binds one exact current evidence frontier and actor binding into PRE_EFFECT_ADMISSION.
- any evidence-version, actor-binding, adapter-class, authority, prior-effect, contract/context mismatch fails closed.
- PRE_EFFECT_INTENT and PRE_EFFECT_ADMISSION are not outcomes.

C3 actor/writer/Recovery:
- normalize_actor_binding creates deterministic ACTOR_EXECUTION_BINDING identity.
- RuntimeInputAdapter carries the normalized binding.
- ContractCompilerFacade and ReviewedSeceCoreAdapter propagate the same binding into compiled contract state.
- EffectIntent and PRE_EFFECT_ADMISSION carry the same binding identity.
- worker/current-writer eligibility is explicit and fail-closed for UNKNOWN/freeze/handoff/replacement conflicts.

Effect boundary:
- NonLiveEffectAdapter never performs an external effect.
- MockEffectAdapter is test-only and returns synthetic observation only.
- EffectOutcomeRecorder requires separate trusted outcome evidence before EVIDENCED_SUCCESS/EVIDENCED_FAILURE.

Downstream:
- RuntimeResultFixator preserves machine truth.
- RuntimeHumanExplanationAdapter is a pure projection of the fixated result.
- next-gate candidate is explicitly marked as requiring external Task Conveyor/coordination authority.
