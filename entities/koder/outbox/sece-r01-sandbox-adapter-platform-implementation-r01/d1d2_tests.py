from __future__ import annotations
from copy import deepcopy
import inspect
from correction_tests import cse
from sece_simulator import CollisionDetector, ContextCorrectionEngine, SemanticStateMutationLayer, Simulator, StaticValidator

def rule(rid="NGR-1", active="ACTIVE", current="CURRENT", conflict="NONE", supersession="NONE"):
    return {"rule_id":rid,"source_ref":"RULE-SOURCE-"+rid,"active_status":active,"currentness":current,"scope":"GLOBAL",
      "next_gate_class":"CAUSAL_NEXT_GATE","required_result_verification":"VERIFIED","required_event_type":"EVENT",
      "required_evidence_id":"NG-E","recipient":"ENTITY-B","task_ref":"TASK-B","conflict_status":conflict,
      "supersession_state":supersession,"provenance":["RULE-SOURCE-"+rid]}

def fixture(rules):
    return {"fixture_id":"D1-E2E","fixture_family":"T","description":"D1 direct e2e",
      "semantic_input":{"facts":[],"current_state_evidence":[cse("NG-E","TASK","GLOBAL",selected="YES")],"causal_events":[],
        "action_intent":None,"triggering_event_or_result":{"trigger_id":"RESULT-1","trigger_type":"EVENT","verification_state":"VERIFIED","scope":"GLOBAL","provenance_ref":"TEST"},
        "next_gate_rules":deepcopy(rules)},"expected":{},"provenance":["D1D2_TEST"]}

def predicate_for_mutation(t):
    m=SemanticStateMutationLayer()
    atoms={"facts":[],"current_state_evidence":[],"causal_events":[],"action_intent":None,"triggering_event_or_result":None,
      "dependency_changes":[],"binding_derivation_input":None,"transformation":deepcopy(t),"base_fixture_ref":None,"validator_predicates":[],"next_gate_rules":[]}
    state=m.apply(atoms); collisions=CollisionDetector().detect(state); corrected=ContextCorrectionEngine().correct(state,collisions)
    return StaticValidator().evaluate(corrected["context"],collisions,set()), corrected["context"]

def run_d1d2_tests():
    sim=Simulator({"type":"object"},{"type":"object"})
    grounded=sim.run_fixture(fixture([rule()]))["actual"]["next_gate_decision"]
    missing=sim.run_fixture(fixture([]))["actual"]["next_gate_decision"]
    inactive=sim.run_fixture(fixture([rule(active="INACTIVE")]))["actual"]["next_gate_decision"]
    superseded=sim.run_fixture(fixture([rule(current="SUPERSEDED",supersession="SUPERSEDED")]))["actual"]["next_gate_decision"]
    ambiguous=sim.run_fixture(fixture([rule("NGR-1"),rule("NGR-2")]))["actual"]["next_gate_decision"]
    raw=fixture([rule()])["semantic_input"]; atoms=sim.atom_loader.load(raw); mutated=sim.mutator.apply(atoms); composed=sim.composer.compose(mutated)
    collisions=sim.collision.detect(composed); corrected=sim.correction.correct(composed,collisions)
    bindings=sim.scope.derive(composed.get("binding_derivation_input"),corrected["context"]); ec=sim.ec_builder.build(corrected,bindings,"T")
    raw["next_gate_rules"][0]["recipient"]="INJECTED-AFTER-BUILD"; contract=sim.projector.project(ec,None).contract
    agg={"next_gate_class":"CAUSAL_NEXT_GATE","aggregation_rule_id":"AGG-R6"}
    result={"result_id":"RESULT-1","state":"PASS","event_or_result":{"event_id":"RESULT-1","event_type":"EVENT","verification_state":"VERIFIED"}}
    after_build=sim.nextgate.resolve(agg,result,contract,ec)
    base={"transformation_type":"LABEL-A","target_ref":"task","field_code":"task_currentness","scope":None,"from_state":"CURRENT","to_state":"SUPERSEDED","provenance_ref":"TEST"}
    alt=deepcopy(base); alt["transformation_type"]="LABEL-B"; p1,c1=predicate_for_mutation(base); p2,c2=predicate_for_mutation(alt)
    static_src=inspect.getsource(StaticValidator); simulator_src=inspect.getsource(Simulator); mutator_src=inspect.getsource(SemanticStateMutationLayer)
    return {
      "d1_grounded":grounded["candidate"]=={"recipient":"ENTITY-B","task_ref":"TASK-B","rule_id":"NGR-1"},
      "d1_missing_no_route":missing["candidate"] is None,"d1_inactive_no_route":inactive["candidate"] is None,
      "d1_superseded_no_route":superseded["candidate"] is None,"d1_ambiguous_stop":ambiguous["candidate"] is None,
      "d1_post_build_metadata_cannot_inject":after_build["candidate"]=={"recipient":"ENTITY-B","task_ref":"TASK-B","rule_id":"NGR-1"},
      "d2_label_independent_predicates":p1==p2=={"REJECT_PRECONDITION","BLOCKED_CURRENTNESS"},
      "d2_label_removed_before_core":c1.get("transformation") is None and c2.get("transformation") is None,
      "d2_static_no_label_proxy":"transformation_type" not in static_src,"d2_simulator_no_label_proxy":"transformation_type" not in simulator_src,
      "d2_mutator_no_label_proxy":"transformation_type" not in mutator_src,
      "NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED": grounded["candidate"] is not None and missing["candidate"] is None and inactive["candidate"] is None and superseded["candidate"] is None and ambiguous["candidate"] is None and after_build["candidate"]=={"recipient":"ENTITY-B","task_ref":"TASK-B","rule_id":"NGR-1"},
      "STATICVALIDATOR_TRANSFORMATION_PROXY_REMOVED":"transformation_type" not in static_src and p1==p2,
      "ANTICHEAT_COVERS_STATICVALIDATOR_AND_ORCHESTRATION":"transformation_type" not in static_src and "transformation_type" not in simulator_src and "transformation_type" not in mutator_src,
    }
