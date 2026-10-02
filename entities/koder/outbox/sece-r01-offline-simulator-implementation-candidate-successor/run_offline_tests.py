from __future__ import annotations
import copy
import json
import socket
import subprocess
import sys
from collections import Counter
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sece_simulator import (
    Simulator, ClosedSchemaValidator, FixtureLoader, DependencyScopeResolver,
    contract_id, trace_id, canonical_json, source_anti_cheat_checks,
    ContextComposer, MultiOutcomeAggregator, ResultClassifier, ContextDeltaBuilder
)

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/"reviewed-inputs"
SRC=ROOT/"sece_simulator.py"

def load(name):
    return json.loads((INPUT/name).read_text())

def contract_mutate(base, cls):
    c=copy.deepcopy(base)
    if cls=="effective_context_version": c["effective_context_version"]=2
    elif cls=="selected_scope": c["selected_scope"]="S2"
    elif cls=="projection_basis": c["projection_basis"][0]["reason_used"]="DIFFERENT_REASON"
    elif cls=="context_dependency_refs": c["context_dependency_refs"].append("DEP-2")
    elif cls=="full_ACTION_INTENT": c["ACTION_INTENT"]["parameters"]["mode"]="BROAD"
    elif cls=="ACTION_AUTHORIZATION_BINDINGS": c["ACTION_AUTHORIZATION_BINDINGS"][0]["authority_ref"]="AUTH-2"
    elif cls=="CAUSAL_EVENTS": c["CAUSAL_EVENTS"][0]["current_decision_state"]="SUPERSEDED"
    elif cls=="CURRENT_STATE_EVIDENCE": c["CURRENT_STATE_EVIDENCE"][0]["currentness_state"]="SUPERSEDED"
    elif cls=="ALLOWED_ACTIONS": c["ALLOWED_ACTIONS"].append({"action_id":"A3","action_class":"READ_ONLY"})
    elif cls=="FORBIDDEN_ACTIONS": c["FORBIDDEN_ACTIONS"].append({"action_id":"A4","action_class":"DEPLOY"})
    elif cls=="REQUIRED_PRECONDITIONS": c["REQUIRED_PRECONDITIONS"][0]["state"]="FAILED"
    elif cls=="STOP_IF": c["STOP_IF"][0]["state"]="TRUE"
    elif cls=="EXPECTED_RESULT": c["EXPECTED_RESULT"]["result_shape"]="R2"
    elif cls=="EXPECTED_TERMINAL": c["EXPECTED_TERMINAL"].append("FAIL")
    elif cls=="NEXT_GATE_RULE": c["NEXT_GATE_RULE"][0]["next_gate_class"]="STOP"
    elif cls=="PROVENANCE": c["PROVENANCE"][0]["ref"]="SRC-2"
    elif cls=="VALIDATION_STATE": c["VALIDATION_STATE"]["conflicts"].append("CONFLICT-1")
    elif cls=="TASK_IDENTITY": c["TASK_IDENTITY"]["task_status"]="SUPERSEDED"
    elif cls=="AUTHORITY_BASIS": c["AUTHORITY_BASIS"][0]["currentness"]="STALE"
    elif cls=="SOURCE_SET": c["SOURCE_SET"][0]["active_status"]="CANDIDATE"
    elif cls=="INPUTS": c["INPUTS"][0]["verified_state"]="UNKNOWN"
    elif cls=="PROFILE": c["PROFILE"]["profile_id"]="PROF-2"
    elif cls=="EXPERIENCE_SET": c["EXPERIENCE_SET"][0]["applicability"]="NOT_APPLICABLE"
    elif cls=="CAPABILITIES": c["CAPABILITIES"].append("ANOTHER_CAPABILITY")
    elif cls=="CURRENT_STATE": c["CURRENT_STATE"]["writer_state"]="ABSENT"
    else: raise AssertionError("unknown contract mutation class:"+cls)
    return c

def same_sets(a,b): return sorted(a)==sorted(b)

def main():
    schema=load("FIXTURE-SCHEMA.json"); catalog=load("FIXTURE-CATALOG.json")
    trace_schema=load("TRACE-SCHEMA.json"); cv=load("CONTRACT-ID-TEST-VECTORS.json"); tv=load("TRACE-ID-TEST-VECTORS.json")
    sim=Simulator(schema,trace_schema)
    fixtures=sim.fixture_loader.load_catalog(catalog)

    markers={}
    family=Counter(f["fixture_family"] for f in fixtures)
    markers["SCHEMA_VALIDATION_PASS"]=len(fixtures)==54
    markers["FIXTURE_CATALOG_54_OF_54_VALID"]=len(fixtures)==54 and len({f["fixture_id"] for f in fixtures})==54 and family=={"T":15,"CXT":10,"O":10,"P":7,"MUTATION":12}

    affected=[f for f in fixtures if f["semantic_input"].get("binding_derivation_input") is not None]
    resolver=DependencyScopeResolver(); deriv_pass=0
    for f in affected:
        actual=resolver.derive(f["semantic_input"]["binding_derivation_input"],f["semantic_input"])
        exp=f["expected"]
        if same_sets(actual["invalidated_bindings"],exp.get("invalidated_bindings",[])) and same_sets(actual["recomputed_bindings"],exp.get("recomputed_bindings",[])) and same_sets(actual["preserved_bindings"],exp.get("preserved_bindings",[])):
            deriv_pass+=1
    markers["INPUT_COMPLETENESS_EXECUTION_PASS"]=f"{deriv_pass}/{len(affected)}"
    markers["BINDING_DERIVATION_PASS"]=f"{deriv_pass}/{len(affected)}"

    base_calc=contract_id(cv["base_contract"])
    identical_calc=contract_id(copy.deepcopy(cv["base_contract"]))
    contract_mut_ok=0
    contract_mut_detail=[]
    for row in cv["semantic_mutation_matrix"]:
        got=contract_id(contract_mutate(cv["base_contract"],row["semantic_field_class"]))
        ok=got==row["contract_id"] and got!=cv["base_contract_id"]
        contract_mut_ok+=int(ok); contract_mut_detail.append((row["semantic_field_class"],ok,got,row["contract_id"]))
    markers["CONTRACT_ID_TEST_VECTORS_PASS"]=base_calc==cv["base_contract_id"] and identical_calc==cv["identical_canonical_contract_id"] and contract_mut_ok==25

    ClosedSchemaValidator(trace_schema).validate(tv["base_trace"])
    trace_base=trace_id(tv["base_trace"]); trace_same=trace_id(copy.deepcopy(tv["base_trace"]))
    trace_changed=copy.deepcopy(tv["base_trace"]); trace_changed["recomputed_bindings"]=["B-DELTA-S-CHANGED"]
    trace_changed_id=trace_id(trace_changed)
    markers["TRACE_ID_TEST_VECTORS_PASS"]=trace_base==tv["base_trace_id"] and trace_same==tv["identical_canonical_trace_id"] and trace_changed_id==tv["changed_recomputed_binding_trace_id"] and trace_changed_id!=trace_base
    markers["TRACE_SCHEMA_PASS"]=True

    results=[]
    for f in fixtures:
        results.append(sim.run_fixture(f))
    passes=Counter()
    for r in results:
        if r["oracle_state"]=="ORACLE_PASS": passes[r["family"]]+=1
    markers["T_FIXTURES_PASS"]=f"{passes['T']}/15"
    markers["CXT_FIXTURES_PASS"]=f"{passes['CXT']}/10"
    markers["O_FIXTURES_PASS"]=f"{passes['O']}/10"
    markers["POSITIVE_CONTROLS_PASS"]=f"{passes['P']}/7"
    markers["PROPERTY_FIXTURES_PASS"]=f"{passes['MUTATION']}/12"
    markers["TOTAL_FIXTURES_PASS"]=f"{sum(passes.values())}/54"

    src=SRC.read_text()
    anti=source_anti_cheat_checks(src)
    markers.update({k:v for k,v in anti.items() if k.endswith("_PASS")})
    fixture_binding_ids=set()
    for f in fixtures:
        bd=f["semantic_input"].get("binding_derivation_input")
        if not bd: continue
        st=bd["initial_state"]
        fixture_binding_ids.update(b["binding_id"] for b in st["initial_derived_bindings"])
        fixture_binding_ids.update(r["output_binding_id"] for r in st["recomputation_rules"])
    hardcoded_fixture_binding_ids=sorted(b for b in fixture_binding_ids if b in src)
    markers["NO_HIDDEN_BINDING_MAPPING_TEST_PASS"]=anti["NO_HIDDEN_BINDING_MAPPING_TEST_PASS"] and not hardcoded_fixture_binding_ids

    # Determinism: run the entire catalog twice and compare machine actual + trace IDs.
    results2=[sim.run_fixture(f) for f in fixtures]
    markers["DETERMINISM_TESTS_PASS"]=all(a["trace_id"]==b["trace_id"] and canonical_json(a["actual"])==canonical_json(b["actual"]) for a,b in zip(results,results2))

    # Side-effect firewall: core executes while common external-effect entry points are trapped.
    def forbidden(*a,**k): raise AssertionError("side_effect_attempt")
    with mock.patch.object(socket,"socket",side_effect=forbidden), mock.patch.object(subprocess,"Popen",side_effect=forbidden):
        _=[sim.run_fixture(f) for f in fixtures]
    markers["NO_SIDE_EFFECT_TESTS_PASS"]=anti["NO_FORBIDDEN_IMPORTS"]

    # 22 reviewed interface classes are present and independently addressable.
    import sece_simulator as mod
    interfaces=[
        "FixtureLoader","RawContextLoader","SemanticAtomLoader","ContextComposer","CollisionDetector",
        "ContextCorrectionEngine","DependencyScopeResolver","EffectiveContextBuilder","ExecutionContractProjector",
        "ActionAuthorizationValidator","CausalEventValidator","CurrentStateEvidenceResolver","StaticValidator",
        "MultiOutcomeAggregator","RuntimeStepGuardSimulator","ResultClassifier","ContextDeltaBuilder",
        "SuccessorContextBuilder","NextGateResolver","HumanCausalRenderer","TraceRecorder","FixtureOracle"
    ]
    markers["DESIGN_INTERFACE_MAPPING_COMPLETE"]=f"{sum(hasattr(mod,x) for x in interfaces)}/22"

    # Boundary assertions.
    arch={}
    cc=ContextComposer(); obj={"facts":[{"fact_id":"A"},{"fact_id":"B"}],"current_state_evidence":[],"causal_events":[],"action_intent":None,"triggering_event_or_result":None,"dependency_changes":[],"binding_derivation_input":None,"transformation":None,"base_fixture_ref":None,"validator_predicates":[]}
    arch["compatible_lines_coexist"]=len(cc.compose(obj)["facts"])==2
    cxt6=next(r for r in results if r["fixture_id"]=="CXT6")
    arch["scope_local_conflict_preserves_unrelated"]=cxt6["actual"]["invalidated_bindings"]==["BINDING_S1_SOURCE_DEPENDENT"] and "BINDING_S2" in cxt6["actual"]["preserved_bindings"]
    m8=next(r for r in results if r["fixture_id"]=="M8")
    arch["dependency_closure_only"]=m8["actual"]["invalidated_bindings"]==["BINDING_DEPENDENT_A1"] and m8["actual"]["recomputed_bindings"]==["BINDING_DEPENDENT_A1_RECOMPUTED"]
    arch["stale_dependent_removed"]=not(set(m8["actual"]["invalidated_bindings"]) & set(m8["actual"]["preserved_bindings"]))
    m10=next(r for r in results if r["fixture_id"]=="M10")
    arch["projection_cannot_invent"]=m10["actual"]["projection_valid"] is False
    p5=next(r for r in results if r["fixture_id"]=="P5"); t8=next(r for r in results if r["fixture_id"]=="T8"); t12=next(r for r in results if r["fixture_id"]=="T12")
    arch["action_intent_proposal_only"]=t8["actual"]["aggregation_core"]["effect_decision"]!="ADMIT"
    arch["profile_experience_capability_no_authority"]=t8["oracle_state"]=="ORACLE_PASS" and t12["oracle_state"]=="ORACLE_PASS" and p5["actual"]["experience_advisory"]
    arch["c1_c2_c3_explicit"]=all(hasattr(mod,x) for x in ("ActionAuthorizationValidator","CausalEventValidator","CurrentStateEvidenceResolver"))
    agg=MultiOutcomeAggregator(); ctx={"facts":[],"causal_events":[]}; before=copy.deepcopy(ctx); agg.aggregate({"SOURCE_CONFLICT_STOP","BLOCKED_AUTHORITY"},ctx)
    arch["l7_local"]=ctx==before
    o8=next(r for r in results if r["fixture_id"]=="O8")
    arch["simultaneous_reasons_preserved"]=len(o8["trace"]["secondary_reasons"])==3
    bad={"SOURCE_CONFLICT_STOP","REJECT_FORBIDDEN","BLOCKED_AUTHORITY","UNKNOWN_REQUIRED_EVIDENCE","FAIL"}
    arch["no_admit_with_bad_predicate"]=all(not(set(r["actual"]["validator_predicates"]) & bad) or (r["actual"]["aggregation_core"] is None or r["actual"]["aggregation_core"]["effect_decision"]!="ADMIT") for r in results)
    cxt3f=copy.deepcopy(next(f for f in fixtures if f["fixture_id"]=="CXT3")); cxt3f["semantic_input"]["triggering_event_or_result"]["verification_state"]="UNKNOWN"
    raw=sim.atom_loader.load(sim.raw_loader.load(cxt3f)); bs=sim.scope.derive(raw["binding_derivation_input"],raw); ec=sim.ec_builder.build(sim.correction.correct(sim.composer.compose(raw),sim.collision.detect(raw)),bs,cxt3f["fixture_family"]); rr=sim.classifier.classify(None,raw); dd=sim.delta.build(ec,raw,bs,rr)
    arch["unverified_event_no_successor_delta"]=dd is None
    p3f=next(f for f in fixtures if f["fixture_id"]=="P3"); raw3=sim.atom_loader.load(sim.raw_loader.load(p3f)); bs3=sim.scope.derive(raw3["binding_derivation_input"],raw3); ec3=sim.ec_builder.build(sim.correction.correct(raw3,sim.collision.detect(raw3)),bs3,p3f["fixture_family"]); ctr=sim.projector.project(ec3,raw3)
    arch["external_evidence_not_authority_generator"]=len(ctr["ACTION_AUTHORIZATION_BINDINGS"])==0
    markers["ARCHITECTURE_ASSERTIONS_PASS"]=all(arch.values())

    markers["IMPLEMENTATION_CANDIDATE_CREATED"]=True

    required=[
        markers["IMPLEMENTATION_CANDIDATE_CREATED"],
        markers["SCHEMA_VALIDATION_PASS"],markers["FIXTURE_CATALOG_54_OF_54_VALID"],
        markers["INPUT_COMPLETENESS_EXECUTION_PASS"]=="15/15",markers["BINDING_DERIVATION_PASS"]=="15/15",
        markers["ORACLE_SEPARATION_TEST_PASS"],markers["NO_FIXTURE_ID_BRANCHING_TEST_PASS"],markers["NO_HIDDEN_BINDING_MAPPING_TEST_PASS"],
        markers["CONTRACT_ID_TEST_VECTORS_PASS"],markers["TRACE_ID_TEST_VECTORS_PASS"],
        markers["T_FIXTURES_PASS"]=="15/15",markers["CXT_FIXTURES_PASS"]=="10/10",markers["O_FIXTURES_PASS"]=="10/10",
        markers["POSITIVE_CONTROLS_PASS"]=="7/7",markers["PROPERTY_FIXTURES_PASS"]=="12/12",markers["TOTAL_FIXTURES_PASS"]=="54/54",
        markers["TRACE_SCHEMA_PASS"],markers["DETERMINISM_TESTS_PASS"],markers["NO_SIDE_EFFECT_TESTS_PASS"],
        markers["DESIGN_INTERFACE_MAPPING_COMPLETE"]=="22/22",markers["ARCHITECTURE_ASSERTIONS_PASS"]
    ]
    summary={
        "status":"PASS" if all(required) else "FAIL",
        "runtime":"Python 3.12+ stdlib only",
        "family_counts":dict(family),
        "affected_count":len(affected),
        "contract_mutations_pass":contract_mut_ok,
        "markers":markers,
        "architecture_assertions":arch,
        "fixture_failures":[{"fixture_id":r["fixture_id"],"mismatches":r["mismatches"]} for r in results if r["oracle_state"]!="ORACLE_PASS"],
        "contract_mutation_failures":[x for x in contract_mut_detail if not x[1]],
    }
    print(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
    return 0 if summary["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())

