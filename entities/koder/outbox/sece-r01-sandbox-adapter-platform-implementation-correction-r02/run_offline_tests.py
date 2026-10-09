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

import sece_simulator as mod
from anti_cheat_regression_tests import run_anti_cheat_regression_tests
from architecture_tests import run_architecture_tests
from correction_tests import run_correction_tests
from d1d2_tests import run_d1d2_tests
from schema_minimum_tests import run_schema_minimum_tests
from sece_simulator import (
    ClosedSchemaValidator,
    DependencyScopeResolver,
    Simulator,
    canonical_json,
    contract_id,
    trace_id,
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

def same_sets(a,b):
    return sorted(a)==sorted(b)

def main():
    schema=load("FIXTURE-SCHEMA.json")
    catalog=load("FIXTURE-CATALOG.json")
    trace_schema=load("TRACE-SCHEMA.json")
    cv=load("CONTRACT-ID-TEST-VECTORS.json")
    tv=load("TRACE-ID-TEST-VECTORS.json")

    sim=Simulator(schema,trace_schema)
    fixtures=sim.fixture_loader.load_catalog(catalog)
    family=Counter(f["fixture_family"] for f in fixtures)

    markers={}
    markers["IMPLEMENTATION_CANDIDATE_CREATED"]=True
    markers["SCHEMA_VALIDATION_PASS"]=len(fixtures)==54
    markers["FIXTURE_CATALOG_54_OF_54_VALID"]=(
        len(fixtures)==54
        and len({f["fixture_id"] for f in fixtures})==54
        and family=={"T":15,"CXT":10,"O":10,"P":7,"MUTATION":12}
    )

    # C1 exact reviewed JSON-Schema minimum keyword tests.
    schema_fix=run_schema_minimum_tests(schema)
    markers["REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED"]=schema_fix["REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED"]

    # Input-completeness derivation, actual first, oracle second.
    affected=[f for f in fixtures if f["semantic_input"].get("binding_derivation_input") is not None]
    resolver=DependencyScopeResolver()
    deriv_pass=0
    for f in affected:
        actual=resolver.derive(f["semantic_input"]["binding_derivation_input"],f["semantic_input"])
        expected=f["expected"]
        ok=(
            same_sets(actual["invalidated_bindings"],expected.get("invalidated_bindings",[]))
            and same_sets(actual["recomputed_bindings"],expected.get("recomputed_bindings",[]))
            and same_sets(actual["preserved_bindings"],expected.get("preserved_bindings",[]))
        )
        deriv_pass += int(ok)
    markers["INPUT_COMPLETENESS_EXECUTION_PASS"]=f"{deriv_pass}/{len(affected)}"
    markers["BINDING_DERIVATION_PASS"]=f"{deriv_pass}/{len(affected)}"

    # D2 exact identity vectors.
    base_calc=contract_id(cv["base_contract"])
    identical_calc=contract_id(copy.deepcopy(cv["base_contract"]))
    contract_mut_ok=0
    contract_mut_fail=[]
    for row in cv["semantic_mutation_matrix"]:
        got=contract_id(contract_mutate(cv["base_contract"],row["semantic_field_class"]))
        ok=got==row["contract_id"] and got!=cv["base_contract_id"]
        contract_mut_ok += int(ok)
        if not ok:
            contract_mut_fail.append({"class":row["semantic_field_class"],"got":got,"expected":row["contract_id"]})
    markers["CONTRACT_ID_TEST_VECTORS_PASS"]=(
        base_calc==cv["base_contract_id"]
        and identical_calc==cv["identical_canonical_contract_id"]
        and contract_mut_ok==25
    )

    # D3 exact trace vectors/schema.
    ClosedSchemaValidator(trace_schema).validate(tv["base_trace"])
    trace_base=trace_id(tv["base_trace"])
    trace_same=trace_id(copy.deepcopy(tv["base_trace"]))
    trace_changed=copy.deepcopy(tv["base_trace"])
    trace_changed["recomputed_bindings"]=["B-DELTA-S-CHANGED"]
    trace_changed_id=trace_id(trace_changed)
    markers["TRACE_ID_TEST_VECTORS_PASS"]=(
        trace_base==tv["base_trace_id"]
        and trace_same==tv["identical_canonical_trace_id"]
        and trace_changed_id==tv["changed_recomputed_binding_trace_id"]
        and trace_changed_id!=trace_base
    )
    markers["TRACE_SCHEMA_PASS"]=True

    # All 54 reviewed fixtures.
    results=[sim.run_fixture(f) for f in fixtures]
    passes=Counter(r["family"] for r in results if r["oracle_state"]=="ORACLE_PASS")
    markers["T_FIXTURES_PASS"]=f"{passes['T']}/15"
    markers["CXT_FIXTURES_PASS"]=f"{passes['CXT']}/10"
    markers["O_FIXTURES_PASS"]=f"{passes['O']}/10"
    markers["POSITIVE_CONTROLS_PASS"]=f"{passes['P']}/7"
    markers["PROPERTY_FIXTURES_PASS"]=f"{passes['MUTATION']}/12"
    markers["TOTAL_FIXTURES_PASS"]=f"{sum(passes.values())}/54"

    # C2-C7 direct tests.
    correction=run_correction_tests()
    for key in (
        "CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED",
        "EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED",
        "C1_L6_PROJECTION_BOUNDARY_FIXED",
        "L6_PROJECTION_FIREWALL_ENFORCED",
        "RESULT_CLASSIFIER_FIDELITY_FIXED",
        "NEXT_GATE_RESOLVER_GROUNDING_FIXED",
    ):
        markers[key]=bool(correction[key])

    # D1+D2 integrated/static anti-proxy tests.
    d1d2=run_d1d2_tests()
    for key in ("NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED","STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED","ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION"):
        markers[key]=bool(d1d2[key])

    # C8 strengthened A1-A13.
    architecture=run_architecture_tests()
    markers["ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED"]=architecture["ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED"]

    # Anti-cheat regressions.
    source_text=SRC.read_text()
    anti=run_anti_cheat_regression_tests(source_text,fixtures)
    for key in (
        "ORACLE_SEPARATION_TEST_PASS",
        "NO_FIXTURE_ID_BRANCHING_TEST_PASS",
        "NO_HIDDEN_BINDING_MAPPING_TEST_PASS",
    ):
        markers[key]=bool(anti[key])
    markers["NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS"]=bool(anti["NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS"])
    markers["ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION"]=markers["ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION"] and bool(anti["ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION"])

    # Determinism: same fixture actual/trace twice.
    results2=[sim.run_fixture(f) for f in fixtures]
    markers["DETERMINISM_TESTS_PASS"]=all(
        a["trace_id"]==b["trace_id"] and canonical_json(a["actual"])==canonical_json(b["actual"])
        for a,b in zip(results,results2)
    )

    # Side-effect firewall: trap representative network/process effects while all fixtures execute.
    def forbidden(*a,**k):
        raise AssertionError("side_effect_attempt")
    with mock.patch.object(socket,"socket",side_effect=forbidden), mock.patch.object(subprocess,"Popen",side_effect=forbidden):
        _=[sim.run_fixture(f) for f in fixtures]
    markers["NO_SIDE_EFFECT_TESTS_PASS"]=True

    interfaces=[
        "FixtureLoader","RawContextLoader","SemanticAtomLoader","ContextComposer","CollisionDetector",
        "ContextCorrectionEngine","DependencyScopeResolver","EffectiveContextBuilder","ExecutionContractProjector",
        "ActionAuthorizationValidator","CausalEventValidator","CurrentStateEvidenceResolver","StaticValidator",
        "MultiOutcomeAggregator","RuntimeStepGuardSimulator","ResultClassifier","ContextDeltaBuilder",
        "SuccessorContextBuilder","NextGateResolver","HumanCausalRenderer","TraceRecorder","FixtureOracle",
    ]
    markers["DESIGN_INTERFACE_MAPPING_COMPLETE"]=f"{sum(hasattr(mod,x) for x in interfaces)}/22"

    required=[
        markers["SCHEMA_VALIDATION_PASS"],
        markers["FIXTURE_CATALOG_54_OF_54_VALID"],
        markers["TOTAL_FIXTURES_PASS"]=="54/54",
        markers["CONTRACT_ID_TEST_VECTORS_PASS"],
        markers["TRACE_ID_TEST_VECTORS_PASS"],
        markers["INPUT_COMPLETENESS_EXECUTION_PASS"]=="15/15",
        markers["BINDING_DERIVATION_PASS"]=="15/15",
        markers["REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED"],
        markers["CONTEXT_CORRECTION_ENGINE_FIDELITY_FIXED"],
        markers["EFFECTIVE_CONTEXT_IMPLEMENTATION_FIDELITY_FIXED"],
        markers["C1_L6_PROJECTION_BOUNDARY_FIXED"],
        markers["L6_PROJECTION_FIREWALL_ENFORCED"],
        markers["RESULT_CLASSIFIER_FIDELITY_FIXED"],
        markers["NEXT_GATE_RESOLVER_GROUNDING_FIXED"],
        markers["ARCHITECTURE_ASSERTION_TESTS_STRENGTHENED"]=="13/13",
        markers["ORACLE_SEPARATION_TEST_PASS"],
        markers["NO_FIXTURE_ID_BRANCHING_TEST_PASS"],
        markers["NO_HIDDEN_BINDING_MAPPING_TEST_PASS"],
        markers["NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS"],
        markers["DETERMINISM_TESTS_PASS"],
        markers["NO_SIDE_EFFECT_TESTS_PASS"],
        markers["NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED"],
        markers["STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED"],
        markers["ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION"],
        markers["DESIGN_INTERFACE_MAPPING_COMPLETE"]=="22/22",
    ]

    summary={
        "status":"PASS" if all(required) else "FAIL",
        "runtime":"Python 3.12+ stdlib only",
        "family_counts":dict(family),
        "affected_count":len(affected),
        "contract_mutations_pass":contract_mut_ok,
        "contract_mutation_failures":contract_mut_fail,
        "markers":markers,
        "schema_minimum_tests":schema_fix,
        "correction_tests":correction,
        "architecture_assertions":architecture,
        "anti_cheat":anti,
        "d1d2_tests":d1d2,
        "fixture_failures":[
            {"fixture_id":r["fixture_id"],"mismatches":r["mismatches"]}
            for r in results if r["oracle_state"]!="ORACLE_PASS"
        ],
    }
    print(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
    return 0 if summary["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
