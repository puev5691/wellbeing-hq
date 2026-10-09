from __future__ import annotations

from copy import deepcopy

from sece_simulator import (
    ActionAuthorizationValidator,
    CollisionDetector,
    ContextCorrectionEngine,
    DependencyScopeResolver,
    EffectiveContextBuilder,
    ExecutionContractProjector,
    MultiOutcomeAggregator,
    NextGateResolver,
    ResultClassifier,
    RuntimeStepGuardSimulator,
)

def fact(fid, typ, state, scope="GLOBAL", value=None, prov="TEST"):
    return {"fact_id":fid,"fact_type":typ,"scope":scope,"state":state,"value_ref":value,"provenance_ref":prov}

def cse(eid, kind="OTHER", scope="GLOBAL", *, selected="NO", relation="INDEPENDENT", target=None, verified="VERIFIED", currentness="CURRENT", conflict="NO"):
    return {
        "evidence_id":eid,
        "evidence_kind":kind,
        "exact_immutable_identity":eid+"-IMMUTABLE",
        "scope":scope,
        "provenance_source":"TEST",
        "verified_state":verified,
        "currentness_state":currentness,
        "relation_to_other_evidence":relation,
        "relation_target_evidence_id":target,
        "selected_current_basis":selected,
        "selection_basis":"TEST",
        "unresolved_conflict":conflict,
        "conflict_set":[],
        "unknown_fields":[],
    }

def event(eid, typ="DECISION", scope="GLOBAL", *, required="NOT_REQUIRED", redundant="NO"):
    return {
        "event_id":eid,
        "event_type":typ,
        "evidence_ref":eid+"-EVIDENCE",
        "causal_parent_event_id":None,
        "lifecycle_evidence_state":"VERIFIED",
        "dispatch_state":"NOT_APPLICABLE",
        "delivery_state":"NOT_APPLICABLE",
        "receipt_state":"NOT_APPLICABLE",
        "processing_started_state":"NOT_APPLICABLE",
        "handoff_recipient":"ENTITY-B" if typ=="HANDOFF" else None,
        "handoff_reason":"TEST" if typ=="HANDOFF" else None,
        "decision_id":eid if typ=="DECISION" else None,
        "decision_owner":"OPERATOR" if typ=="DECISION" else None,
        "decision_recipient":"KOO" if typ=="DECISION" else None,
        "current_decision_state":"CURRENT" if typ=="DECISION" else "NOT_APPLICABLE",
        "proposed_handoff_target":"ENTITY-B" if typ=="HANDOFF" else None,
        "redundant_self_handoff":redundant,
        "causal_requirement_status":required,
        "scope":scope,
        "provenance_ref":"TEST",
    }

def action(aid="A1", cls="EXECUTE", scope="S", transition="EXECUTE_EFFECT", target="OBJ"):
    return {"action_id":aid,"action_class":cls,"selected_scope":scope,"transition_type":transition,"target_ref":target}

def context(*, facts=None, evidence=None, events=None, action_intent=None, dependency_changes=None, binding_input=None, transformation=None):
    return {
        "facts":deepcopy(facts or []),
        "current_state_evidence":deepcopy(evidence or []),
        "causal_events":deepcopy(events or []),
        "action_intent":deepcopy(action_intent),
        "triggering_event_or_result":None,
        "dependency_changes":deepcopy(dependency_changes or []),
        "binding_derivation_input":deepcopy(binding_input),
        "transformation":deepcopy(transformation),
        "base_fixture_ref":None,
        "validator_predicates":[],
    }

def build_ec(ctx):
    detector=CollisionDetector()
    engine=ContextCorrectionEngine()
    collisions=detector.detect(ctx)
    corrected=engine.correct(ctx,collisions)
    bindings=DependencyScopeResolver().derive(ctx.get("binding_derivation_input"),corrected["context"])
    ec=EffectiveContextBuilder().build(corrected,bindings,"DIRECT_TEST")
    return corrected,bindings,ec

def run_correction_tests() -> dict:
    results={}

    # C2: exact-scope correction + explicit unresolved conflict + immutable prior.
    c2ctx=context(facts=[
        fact("F-S1","SOURCE_CONFLICT_STATE","CONFLICT","S1"),
        fact("F-S2","ALLOWED_ACTION","ALLOWED","S2","READ"),
    ])
    before=deepcopy(c2ctx)
    corrected,bindings,ec=build_ec(c2ctx)
    results["c2_prior_immutable"]=c2ctx==before
    results["c2_explicit_correction"]=len(corrected["corrections"])==1 and corrected["corrections"][0]["affected_scope"]=="S1"
    results["c2_s2_preserved"]=any(f["fact_id"]=="F-S2" and f["scope"]=="S2" for f in corrected["context"]["facts"])
    results["c2_unresolved_conflict_explicit"]=len(corrected["unresolved_conflicts"])==1 and corrected["unresolved_conflicts"][0]["unresolved"]=="YES"
    unknown_ctx=context(facts=[fact("UNK","REQUIRED_EVIDENCE_STATE","UNKNOWN","S1")])
    unknown_corrected,_,unknown_ec=build_ec(unknown_ctx)
    results["c2_unknown_preserved"]=len(unknown_corrected["unknowns"])==1 and len(unknown_ec["unknown_facts"])==1
    results["c2_downstream_consumes_corrections"]=ec["context_corrections"]==corrected["corrections"] and ec["conflict_set"]==corrected["unresolved_conflicts"]

    refine_ctx=context(evidence=[
        cse("R","RECOVERY","S",selected="YES",currentness="HISTORICAL"),
        cse("D","VERIFIED_DELTA","S",selected="YES",relation="REFINES",target="R"),
        cse("U","RECOVERY","U",selected="YES"),
    ])
    refine_before=deepcopy(refine_ctx)
    refine_corrected,_,refine_ec=build_ec(refine_ctx)
    byid={x["evidence_id"]:x for x in refine_corrected["context"]["current_state_evidence"]}
    results["c2_verified_refinement_scope_only"]=(
        byid["R"]["selected_current_basis"]=="NO"
        and byid["D"]["selected_current_basis"]=="YES"
        and byid["U"]["selected_current_basis"]=="YES"
        and refine_corrected["changed_scopes"]==["S"]
        and refine_ctx==refine_before
    )
    results["CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED"]=all(results[k] for k in list(results) if k.startswith("c2_"))

    # C3: full reviewed Effective Context shape + deterministic full-context identity.
    c3ctx=context(
        facts=[
            fact("SRC","SOURCE_STATUS","ACTIVE","GLOBAL"),
            fact("TASK","TASK_CURRENTNESS","CURRENT","S"),
            fact("AUTH","AUTHORITY_BINDING_STATE","PRESENT","S","AUTH-1"),
            fact("EXP","EXPERIENCE_RECOMMENDATION","ADVISORY","S","READ"),
            fact("CAP","PROFILE_CAPABILITY","PRESENT","S","READ"),
            fact("HUM","HUMAN_CLAIM_AUTHORITY","UNKNOWN","S","claim"),
        ],
        evidence=[cse("E1","TASK","S",selected="YES")],
        events=[event("EV1","DECISION","S")],
        action_intent=action(),
    )
    _,_,c3ec=build_ec(c3ctx)
    required_fields={
        "context_id","context_version","entity","instance","role","active_source_set","semantic_invariants",
        "current_state_evidence","selected_current_basis_by_scope","current_tasks","authority_bindings","profile",
        "experience_set","capability_set","causal_events","human_input_facts","unknown_facts","conflict_set",
        "context_corrections","derived_bindings","provenance","scope_index","dependency_graph",
        "prior_context_ref","context_delta_ref",
    }
    _,_,c3ec2=build_ec(c3ctx)
    noauth_ctx=context(facts=[
        fact("EXP2","EXPERIENCE_RECOMMENDATION","ADVISORY","S","READ"),
        fact("CAP2","PROFILE_CAPABILITY","PRESENT","S","READ"),
    ],action_intent=action())
    _,_,noauth_ec=build_ec(noauth_ctx)
    results["c3_full_structure"]=required_fields.issubset(c3ec.keys())
    results["c3_deterministic_identity"]=c3ec["context_id"]==c3ec2["context_id"]
    results["c3_field_presence_not_authority"]=noauth_ec["authority_bindings"]==[]
    results["EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED"]=all(results[k] for k in list(results) if k.startswith("c3_"))

    projector=ExecutionContractProjector()
    authv=ActionAuthorizationValidator()

    # C4: C1 comes from EFFECTIVE_CONTEXT -> L6 contract only.
    valid_ctx=context(facts=[
        fact("AUTH-P","AUTHORITY_BINDING_STATE","PRESENT","S","AUTH-1"),
        fact("TASK-C","TASK_CURRENTNESS","CURRENT","S"),
    ],action_intent=action())
    _,_,valid_ec=build_ec(valid_ctx)
    valid_proj=projector.project(valid_ec,valid_ctx["action_intent"])
    valid_pred=authv.evaluate(valid_proj.contract)

    missing_ctx=context(facts=[fact("AUTH-M","AUTHORITY_REF_STATE","ABSENT","S")],action_intent=action())
    _,_,missing_ec=build_ec(missing_ctx)
    missing_proj=projector.project(missing_ec,missing_ctx["action_intent"])
    missing_pred=authv.evaluate(missing_proj.contract)

    stale_ctx=context(facts=[fact("SRC-C","SOURCE_STATUS","CANDIDATE","S")],action_intent=action())
    _,_,stale_ec=build_ec(stale_ctx)
    stale_pred=authv.evaluate(projector.project(stale_ec,stale_ctx["action_intent"]).contract)

    conflicted_ec=deepcopy(valid_ec)
    conflicted_ec["authority_bindings"][0]["conflict_status"]="CONFLICT"
    conflicted_pred=authv.evaluate(projector.project(conflicted_ec,valid_ctx["action_intent"]).contract)

    raw_bypass=deepcopy(missing_ctx)
    raw_bypass["facts"]=[fact("AUTH-R","AUTHORITY_BINDING_STATE","PRESENT","S","AUTH-RAW")]
    bypass_pred=authv.evaluate(projector.project(missing_ec,raw_bypass["action_intent"]).contract)

    valid_agg=MultiOutcomeAggregator().aggregate(valid_pred,valid_ctx)
    valid_effect=RuntimeStepGuardSimulator().simulate(valid_agg,valid_proj.contract)
    results["c4_valid_projected_binding_clear"]="REJECT_ACTION_AUTHORIZATION_BINDING" not in valid_pred and len(valid_proj.contract["ACTION_AUTHORIZATION_BINDINGS"])==1 and valid_agg["effect_decision"]=="ADMIT" and valid_effect is not None
    results["c4_missing_binding_reject_block"]={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}.issubset(missing_pred)
    results["c4_stale_binding_reject"]="REJECT_ACTION_AUTHORIZATION_BINDING" in stale_pred
    results["c4_conflicted_binding_reject_block"]={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}.issubset(conflicted_pred)
    results["c4_raw_fact_cannot_bypass"]={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}.issubset(bypass_pred)
    results["C1_L6_PROJECTION_BOUNDARY_FIXED"]=all(results[k] for k in list(results) if k.startswith("c4_"))

    # C5: projector firewall is enforced by the projector itself.
    valid_projection=projector.project(valid_ec,valid_ctx["action_intent"])
    missing_projection=projector.project(valid_ec,valid_ctx["action_intent"],{"basis_ids":["ABSENT_CONTEXT_ITEM"],"dependency_ids":[]})
    invented_projection=projector.project(valid_ec,valid_ctx["action_intent"],{"invented_context_items":[{"id":"CONTRACT_ONLY_ITEM"}]})
    bad_dep_projection=projector.project(valid_ec,valid_ctx["action_intent"],{"dependency_ids":["NO_SUCH_EDGE"]})
    results["c5_valid_projection"]=valid_projection.valid
    results["c5_missing_basis_rejected"]=not missing_projection.valid and any(x.startswith("MISSING_PROJECTION_BASIS:") for x in missing_projection.errors)
    results["c5_invented_item_rejected"]=not invented_projection.valid and any(x.startswith("INVENTED_CONTEXT_ITEM:") for x in invented_projection.errors)
    results["c5_invalid_dependency_rejected"]=not bad_dep_projection.valid and any(x.startswith("INVALID_CONTEXT_DEPENDENCY:") for x in bad_dep_projection.errors)
    results["L6_PROJECTION_FIREWALL_ENFORCED"]=all(results[k] for k in list(results) if k.startswith("c5_"))

    # C6: result classifier compares actual observation to contract expectations.
    classifier=ResultClassifier()
    rc=deepcopy(valid_proj.contract)
    rc["EXPECTED_RESULT"]={"required":True,"result_shape":"SYNTHETIC","expected_state":"PASS"}
    rc["EXPECTED_TERMINAL"]=["PASS"]
    good={"event_id":"R1","event_type":"RESULT","verification_state":"VERIFIED","result_shape":"SYNTHETIC","state":"PASS","terminal_class":"PASS"}
    bad=deepcopy(good); bad["result_shape"]="OTHER"
    unknown=deepcopy(good); unknown["verification_state"]="UNKNOWN"
    results["c6_pass"]=classifier.classify(good,rc)["state"]=="PASS"
    results["c6_fail"]=classifier.classify(bad,rc)["state"]=="FAIL"
    results["c6_unknown_missing"]=classifier.classify(None,rc,flow_applicable=True)["state"]=="UNKNOWN"
    results["c6_unknown_unverified"]=classifier.classify(unknown,rc)["state"]=="UNKNOWN"
    results["RESULT_CLASSIFIER_FIDELITY_FIXED"]=all(results[k] for k in list(results) if k.startswith("c6_"))

    # C7: exact next gate requires verified result + active current rule + current evidence.
    resolver=NextGateResolver()
    ng_contract=deepcopy(valid_proj.contract)
    ng_contract["CURRENT_STATE_EVIDENCE"]=[cse("NG-E","TASK","S",selected="YES")]
    # Complete normalized typed D1 rule shape. Missing conflict/supersession
    # fields are malformed and must not be normalized inside the resolver.
    ng_contract["NEXT_GATE_RULE"]=[{
        "rule_id":"NGR-1","source_ref":"RULE-SOURCE-NGR-1","active_status":"ACTIVE","currentness":"CURRENT",
        "scope":"S","next_gate_class":"CAUSAL_NEXT_GATE","required_result_verification":"VERIFIED",
        "required_event_type":"RESULT","required_evidence_id":"NG-E","recipient":"ENTITY-B","task_ref":"TASK-B",
        "conflict_status":"NONE","supersession_state":"NONE","provenance":["RULE-SOURCE-NGR-1"]
    }]
    agg={"next_gate_class":"CAUSAL_NEXT_GATE","aggregation_rule_id":"AGG-R6"}
    verified_result={"result_id":"R1","state":"PASS","event_or_result":{"event_id":"R1","event_type":"RESULT","verification_state":"VERIFIED"}}
    grounded=resolver.resolve(agg,verified_result,ng_contract,valid_ec)
    no_rule_contract=deepcopy(ng_contract); no_rule_contract["NEXT_GATE_RULE"]=[]
    no_rule=resolver.resolve(agg,verified_result,no_rule_contract,valid_ec)
    old_rule_contract=deepcopy(ng_contract)
    old_rule_contract["NEXT_GATE_RULE"][0]["currentness"]="SUPERSEDED"
    old_rule_contract["NEXT_GATE_RULE"][0]["supersession_state"]="SUPERSEDED"
    old_rule=resolver.resolve(agg,verified_result,old_rule_contract,valid_ec)
    conflicted_rule_contract=deepcopy(ng_contract)
    conflicted_rule_contract["NEXT_GATE_RULE"][0]["conflict_status"]="CONFLICT"
    conflicted_rule=resolver.resolve(agg,verified_result,conflicted_rule_contract,valid_ec)
    malformed_rule_contract=deepcopy(ng_contract)
    del malformed_rule_contract["NEXT_GATE_RULE"][0]["conflict_status"]
    malformed_rule=resolver.resolve(agg,verified_result,malformed_rule_contract,valid_ec)
    terminal_alone=resolver.resolve(None,verified_result,ng_contract,valid_ec)
    results["c7_grounded_candidate"]=grounded["next_gate_class"]=="CAUSAL_NEXT_GATE" and grounded["candidate"]=={"recipient":"ENTITY-B","task_ref":"TASK-B","rule_id":"NGR-1"}
    results["c7_class_without_rule_no_route"]=no_rule["next_gate_class"]=="NONE" and no_rule["candidate"] is None
    results["c7_historical_rule_no_route"]=old_rule["next_gate_class"]=="NONE" and old_rule["candidate"] is None
    results["c7_conflicted_rule_no_route"]=conflicted_rule["next_gate_class"]=="NONE" and conflicted_rule["candidate"] is None
    results["c7_incomplete_rule_no_route"]=malformed_rule["next_gate_class"]=="NONE" and malformed_rule["candidate"] is None
    results["c7_terminal_alone_no_route"]=terminal_alone["next_gate_class"]=="NONE" and terminal_alone["candidate"] is None
    results["NEXT_GATE_RESOLVER_GROUNDING_FIXED"]=all(results[k] for k in list(results) if k.startswith("c7_"))

    return results
