from __future__ import annotations

from copy import deepcopy

from correction_tests import action, cse, context, event, fact, build_ec
from sece_simulator import (
    ActionAuthorizationValidator,
    CausalEventValidator,
    ContextComposer,
    ContextDeltaBuilder,
    CurrentStateEvidenceResolver,
    DependencyScopeResolver,
    ExecutionContractProjector,
    MultiOutcomeAggregator,
    ResultClassifier,
    RuntimeStepGuardSimulator,
)

def transitive_binding_input():
    return {
        "changed_source_ids":["ATOM-A"],
        "initial_state":{
            "state_id":"ARCH-A3",
            "schema_version":"SECE_SYNTHETIC_BINDING_STATE_R01",
            "initial_derived_bindings":[
                {"binding_id":"B1","binding_type":"DEPENDENCY","exact_scope":"S","dependencies":["ATOM-A"],"current_state":"ACTIVE","provenance_ref":"TEST","semantic_role":"INVALIDATABLE_DEPENDENT","recomputation_rule_ref":"R1"},
                {"binding_id":"B2","binding_type":"DEPENDENCY","exact_scope":"S","dependencies":["B1"],"current_state":"ACTIVE","provenance_ref":"TEST","semantic_role":"INVALIDATABLE_DEPENDENT","recomputation_rule_ref":"R2"},
                {"binding_id":"B3","binding_type":"OTHER_SYNTHETIC","exact_scope":"U","dependencies":[],"current_state":"ACTIVE","provenance_ref":"TEST","semantic_role":"PRESERVED_UNAFFECTED","recomputation_rule_ref":None},
            ],
            "dependency_edges":[
                {"edge_id":"E1","source_atom_or_evidence_id":"ATOM-A","dependent_binding_id":"B1","exact_scope":"S","relation_type":"DEPENDS_ON","provenance_ref":"TEST"},
                {"edge_id":"E2","source_atom_or_evidence_id":"B1","dependent_binding_id":"B2","exact_scope":"S","relation_type":"DEPENDS_ON","provenance_ref":"TEST"},
            ],
            "scope_index":[
                {"scope_id":"S","atom_ids":["ATOM-A"],"evidence_ids":[],"binding_ids":["B1","B2"],"child_scopes":[]},
                {"scope_id":"U","atom_ids":[],"evidence_ids":[],"binding_ids":["B3"],"child_scopes":[]},
            ],
            "recomputation_rules":[
                {"rule_id":"R1","input_binding_ids":["B1"],"output_binding_id":"B1N","exact_scope":"S","output_binding_type":"DEPENDENCY","output_state":"CURRENT","provenance_ref":"TEST"},
                {"rule_id":"R2","input_binding_ids":["B2"],"output_binding_id":"B2N","exact_scope":"S","output_binding_type":"DEPENDENCY","output_state":"CURRENT","provenance_ref":"TEST"},
            ],
            "provenance_ref":"TEST",
        },
    }

def run_architecture_tests() -> dict:
    out={}

    # A1 compatible lines coexist.
    composer=ContextComposer()
    c=context(facts=[
        fact("F1","ALLOWED_ACTION","ALLOWED","S1","READ"),
        fact("F2","FORBIDDEN_ACTION","FORBIDDEN","S2","MUTATE"),
    ])
    composed=composer.compose(c)
    out["A1"]=len(composed["facts"])==2 and {f["fact_id"] for f in composed["facts"]}=={"F1","F2"}

    # A2 local conflict preserves unrelated scope.
    c2=context(facts=[
        fact("CF","SOURCE_CONFLICT_STATE","CONFLICT","S1"),
        fact("OK","ALLOWED_ACTION","ALLOWED","S2","READ"),
    ])
    corrected,_,ec2=build_ec(c2)
    out["A2"]=(
        corrected["changed_scopes"]==["S1"]
        and any(f["fact_id"]=="OK" and f["scope"]=="S2" for f in corrected["context"]["facts"])
        and any(f["fact_id"]=="OK" for f in ec2["semantic_atoms"])
    )

    # A3/A4 direct transitive dependency closure and stale-binding removal.
    bi=transitive_binding_input()
    ctx3=context(binding_input=bi,action_intent=action(scope="S"))
    bs=DependencyScopeResolver().derive(bi,ctx3)
    out["A3"]=bs["invalidated_bindings"]==["B1","B2"] and bs["recomputed_bindings"]==["B1N","B2N"] and bs["preserved_bindings"]==["B3"]
    out["A4"]=not(set(bs["invalidated_bindings"]) & set(bs["preserved_bindings"])) and {"B1","B2"}.issubset(set(bs["invalidated_bindings"]))

    projector=ExecutionContractProjector()

    # A5 projector itself rejects invented context facts.
    base_ctx=context(facts=[fact("F","ALLOWED_ACTION","ALLOWED","S","READ")],action_intent=action())
    _,_,base_ec=build_ec(base_ctx)
    invented=projector.project(base_ec,base_ctx["action_intent"],{"invented_context_items":[{"id":"NOT_IN_CONTEXT"}]})
    out["A5"]=not invented.valid and any(x.startswith("INVENTED_CONTEXT_ITEM:") for x in invented.errors)

    # A6 ACTION_INTENT alone creates neither authority binding nor effect.
    intent_only=context(action_intent=action())
    _,_,intent_ec=build_ec(intent_only)
    intent_proj=projector.project(intent_ec,intent_only["action_intent"])
    auth_pred=ActionAuthorizationValidator().evaluate(intent_proj.contract)
    agg=MultiOutcomeAggregator().aggregate(auth_pred,intent_only)
    effect=RuntimeStepGuardSimulator().simulate(agg,intent_proj.contract)
    out["A6"]=intent_ec["authority_bindings"]==[] and effect is None

    # A7 profile/experience/capability mutations do not create authority.
    variants=[
        context(facts=[fact("P","PROFILE_CAPABILITY","PRESENT","S","READ")],action_intent=action()),
        context(facts=[fact("E","EXPERIENCE_RECOMMENDATION","ADVISORY","S","READ")],action_intent=action()),
        context(facts=[fact("C","AUTOMATION_CAPABILITY","AVAILABLE","S","AUTO")],action_intent=action()),
    ]
    out["A7"]=all(build_ec(v)[2]["authority_bindings"]==[] for v in variants)

    # A8 C1/C2/C3 projected and consumed, not class-existence proxies.
    c1ctx=context(facts=[fact("AUTH","AUTHORITY_BINDING_STATE","PRESENT","S","AUTH-1")],action_intent=action())
    _,_,c1ec=build_ec(c1ctx)
    c1contract=projector.project(c1ec,c1ctx["action_intent"]).contract
    c1_ok=len(c1contract["ACTION_AUTHORIZATION_BINDINGS"])==1 and ActionAuthorizationValidator().evaluate(c1contract)==set()

    c2ctx=context(events=[event("H1","HANDOFF","S",required="NOT_REQUIRED",redundant="YES")],action_intent=action(cls="HANDOFF",transition="HANDOFF"))
    _,_,c2ec=build_ec(c2ctx)
    c2contract=projector.project(c2ec,c2ctx["action_intent"]).contract
    c2_ok=len(c2contract["CAUSAL_EVENTS"])==1 and "REJECT_REDUNDANT_SELF_HANDOFF" in CausalEventValidator().evaluate(c2contract)

    c3ctx=context(evidence=[cse("CS1","TASK","S",selected="YES",conflict="YES")],action_intent=action())
    _,_,c3ec=build_ec(c3ctx)
    c3contract=projector.project(c3ec,c3ctx["action_intent"]).contract
    c3_pred,_=CurrentStateEvidenceResolver().evaluate(c3contract)
    c3_ok=len(c3contract["CURRENT_STATE_EVIDENCE"])==1 and "CURRENT_STATE_CONFLICT_STOP" in c3_pred
    out["A8"]=c1_ok and c2_ok and c3_ok

    # A9 aggregation remains local and cannot mutate EFFECTIVE_CONTEXT.
    before=deepcopy(c1ec)
    _=MultiOutcomeAggregator().aggregate({"BLOCKED_AUTHORITY","BLOCKED_WRITER"},c1ctx)
    out["A9"]=before==c1ec

    # A10 simultaneous reasons remain explicit.
    reasons={"BLOCKED_AUTHORITY","BLOCKED_WRITER","BLOCKED_CURRENTNESS"}
    a10=MultiOutcomeAggregator().aggregate(reasons,intent_only)
    out["A10"]={r["predicate_id"] for r in a10["secondary_reasons"]}==reasons

    # A11 no bad predicate set may yield ADMIT.
    bad_sets=[
        {"SOURCE_CONFLICT_STOP"},{"CURRENT_STATE_CONFLICT_STOP"},{"REJECT_FORBIDDEN"},
        {"REJECT_ACTION_AUTHORIZATION_BINDING"},{"REJECT_PRECONDITION"},{"BLOCKED_AUTHORITY"},
        {"BLOCKED_WRITER"},{"BLOCKED_CURRENTNESS"},{"UNKNOWN_REQUIRED_EVIDENCE"},{"FAIL"},
    ]
    out["A11"]=all(MultiOutcomeAggregator().aggregate(s,intent_only)["effect_decision"]!="ADMIT" for s in bad_sets)

    # A12 unverified/UNKNOWN/conflicted event cannot mutate successor context.
    delta_ctx=context(binding_input=transitive_binding_input(),action_intent=action(scope="S"))
    corrected12,bs12,ec12=build_ec(delta_ctx)
    contract12=projector.project(ec12,delta_ctx["action_intent"]).contract
    classifier=ResultClassifier(); delta_builder=ContextDeltaBuilder()
    states=[]
    for verification in ("UNVERIFIED","UNKNOWN","CONFLICT"):
        obs={"event_id":"OBS-"+verification,"event_type":"EVENT","verification_state":verification,"result_shape":"SYNTHETIC","state":"PASS","terminal_class":"PASS"}
        rr=classifier.classify(obs,contract12)
        states.append(rr["state"]=="UNKNOWN" and delta_builder.build(ec12,corrected12["context"],bs12,rr) is None)
    out["A12"]=all(states)

    # A13 Task Conveyor/Recovery/current-writer evidence is external evidence, never an authority generator.
    boundary_variants=[
        context(facts=[fact("T","TASK_CURRENTNESS","CURRENT","S")],action_intent=action()),
        context(facts=[fact("W","WRITER_STATE","CURRENT_ESTABLISHED","S")],action_intent=action()),
        context(evidence=[cse("R","RECOVERY","S",selected="YES")],action_intent=action()),
    ]
    out["A13"]=all(build_ec(v)[2]["authority_bindings"]==[] for v in boundary_variants)

    out["ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED"]=f"{sum(bool(out[f'A{i}']) for i in range(1,14))}/13"
    return out
