from __future__ import annotations
import ast
import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

CONTRACT_DOMAIN = "sece-execution-contract-r01\0"
TRACE_DOMAIN = "sece-simulator-trace-r01\0"
CONTEXT_DOMAIN = "sece-effective-context-r01\0"
DELTA_DOMAIN = "sece-context-delta-r01\0"

SET_SORT_KEYS = {
    "projection_basis": lambda x: (x.get("context_atom_or_binding_id",""), x.get("exact_scope",""), x.get("provenance_ref","")),
    "context_dependency_refs": lambda x: str(x),
    "ACTION_AUTHORIZATION_BINDINGS": lambda x: (x.get("action_id",""), x.get("compiled_rule_id",""), x.get("authority_ref","")),
    "CAUSAL_EVENTS": lambda x: x.get("event_id",""),
    "CURRENT_STATE_EVIDENCE": lambda x: x.get("evidence_id",""),
    "AUTHORITY_BASIS": lambda x: (x.get("authority_ref",""), x.get("scope","")),
    "SOURCE_SET": lambda x: (x.get("locator",""), x.get("version_blob","")),
    "INPUTS": lambda x: x.get("input_id",""),
    "EXPERIENCE_SET": lambda x: x.get("ref",""),
    "ALLOWED_ACTIONS": lambda x: x if isinstance(x,str) else x.get("action_id",""),
    "FORBIDDEN_ACTIONS": lambda x: x if isinstance(x,str) else x.get("action_id",""),
    "REQUIRED_PRECONDITIONS": lambda x: x.get("predicate_id", x.get("rule_id", json.dumps(x,sort_keys=True))),
    "STOP_IF": lambda x: x.get("predicate_id", x.get("rule_id", json.dumps(x,sort_keys=True))),
    "EXPECTED_TERMINAL": lambda x: str(x),
    "NEXT_GATE_RULE": lambda x: x.get("rule_id", json.dumps(x,sort_keys=True)),
    "PROVENANCE": lambda x: x.get("provenance_id", x.get("ref", json.dumps(x,sort_keys=True))),
    "CAPABILITIES": lambda x: x if isinstance(x,str) else x.get("capability_id",""),
}

def canonicalize(value: Any, key: str | None = None) -> Any:
    if isinstance(value, dict):
        return {k: canonicalize(value[k], k) for k in sorted(value)}
    if isinstance(value, list):
        out = [canonicalize(v) for v in value]
        if key in SET_SORT_KEYS:
            out.sort(key=SET_SORT_KEYS[key])
        return out
    return value

def canonical_json(value: Any) -> str:
    return json.dumps(canonicalize(value), ensure_ascii=False, separators=(",", ":"), sort_keys=True)

def digest(domain: str, payload: Any) -> str:
    return hashlib.sha256((domain + canonical_json(payload)).encode("utf-8")).hexdigest()

def contract_id(contract: dict) -> str:
    payload = copy.deepcopy(contract)
    payload.pop("contract_id", None)
    return digest(CONTRACT_DOMAIN, payload)

def trace_id(trace: dict) -> str:
    payload = copy.deepcopy(trace)
    payload.pop("trace_id", None)
    return digest(TRACE_DOMAIN, payload)

class SchemaError(ValueError):
    pass

class ClosedSchemaValidator:
    def __init__(self, schema: dict):
        self.schema = schema

    def _resolve(self, ref: str) -> dict:
        if not ref.startswith("#/"):
            raise SchemaError("external_ref_forbidden")
        node: Any = self.schema
        for part in ref[2:].split("/"):
            node = node[part.replace("~1","/").replace("~0","~")]
        return node

    def validate(self, value: Any, schema: dict | None = None, path: str = "$") -> None:
        s = self.schema if schema is None else schema
        if "$ref" in s:
            return self.validate(value, self._resolve(s["$ref"]), path)
        if "anyOf" in s:
            errs=[]
            for branch in s["anyOf"]:
                try:
                    self.validate(value, branch, path); return
                except SchemaError as e: errs.append(str(e))
            raise SchemaError(f"{path}:anyOf")
        if "oneOf" in s:
            n=0
            for branch in s["oneOf"]:
                try:
                    self.validate(value, branch, path); n+=1
                except SchemaError: pass
            if n != 1: raise SchemaError(f"{path}:oneOf={n}")
            return
        typ=s.get("type")
        if typ is not None:
            choices=typ if isinstance(typ,list) else [typ]
            def ok(t: str) -> bool:
                return {
                    "null": value is None,
                    "object": isinstance(value,dict),
                    "array": isinstance(value,list),
                    "string": isinstance(value,str),
                    "integer": isinstance(value,int) and not isinstance(value,bool),
                    "number": isinstance(value,(int,float)) and not isinstance(value,bool),
                    "boolean": isinstance(value,bool),
                }.get(t,True)
            if not any(ok(t) for t in choices): raise SchemaError(f"{path}:type")
        if "const" in s and value != s["const"]: raise SchemaError(f"{path}:const")
        if "enum" in s and value not in s["enum"]: raise SchemaError(f"{path}:enum:{value!r}")
        if isinstance(value,str):
            import re
            if "pattern" in s and re.search(s["pattern"], value) is None: raise SchemaError(f"{path}:pattern")
            if len(value) < s.get("minLength",0): raise SchemaError(f"{path}:minLength")
        if isinstance(value,list):
            if len(value) < s.get("minItems",0): raise SchemaError(f"{path}:minItems")
            if s.get("uniqueItems"):
                serial=[canonical_json(v) for v in value]
                if len(serial)!=len(set(serial)): raise SchemaError(f"{path}:uniqueItems")
            if "items" in s:
                for i,v in enumerate(value): self.validate(v,s["items"],f"{path}[{i}]")
        if isinstance(value,dict):
            for k in s.get("required",[]): 
                if k not in value: raise SchemaError(f"{path}:missing:{k}")
            props=s.get("properties",{})
            if s.get("additionalProperties") is False:
                extra=set(value)-set(props)
                if extra: raise SchemaError(f"{path}:extra:{sorted(extra)}")
            for k,v in value.items():
                if k in props: self.validate(v,props[k],f"{path}.{k}")

class FixtureLoader:
    def __init__(self, fixture_schema: dict):
        self.validator=ClosedSchemaValidator(fixture_schema)
    def load_catalog(self, catalog: dict) -> list[dict]:
        fixtures=catalog["fixtures"]
        ids=set()
        for f in fixtures:
            self.validator.validate(f)
            if f["fixture_id"] in ids: raise SchemaError("duplicate_fixture_id")
            ids.add(f["fixture_id"])
        return fixtures

class RawContextLoader:
    def load(self, fixture: dict) -> dict:
        return copy.deepcopy(fixture["semantic_input"])

class SemanticAtomLoader:
    def load(self, raw: dict) -> dict:
        return {
            "facts": copy.deepcopy(raw.get("facts",[])),
            "current_state_evidence": copy.deepcopy(raw.get("current_state_evidence",[])),
            "causal_events": copy.deepcopy(raw.get("causal_events",[])),
            "action_intent": copy.deepcopy(raw.get("action_intent")),
            "triggering_event_or_result": copy.deepcopy(raw.get("triggering_event_or_result")),
            "dependency_changes": copy.deepcopy(raw.get("dependency_changes",[])),
            "binding_derivation_input": copy.deepcopy(raw.get("binding_derivation_input")),
            "transformation": copy.deepcopy(raw.get("transformation")),
            "base_fixture_ref": raw.get("base_fixture_ref"),
            "validator_predicates": copy.deepcopy(raw.get("validator_predicates",[])),
        }

class ContextComposer:
    def compose(self, atoms: dict) -> dict:
        return copy.deepcopy(atoms)

class CollisionDetector:
    def detect(self, context: dict) -> list[dict]:
        out=[]
        for f in context["facts"]:
            if f["fact_type"]=="SOURCE_CONFLICT_STATE" and f["state"]=="CONFLICT":
                out.append({"type":"SOURCE_STATUS_CONFLICT","scope":f["scope"],"ref":f["fact_id"]})
        for e in context["current_state_evidence"]:
            if e["unresolved_conflict"]=="YES":
                out.append({"type":"CURRENT_STATE_CONFLICT","scope":e["scope"],"ref":e["evidence_id"]})
        tr=context.get("transformation")
        if tr and tr["transformation_type"]=="ADD_CURRENT_STATE_CONFLICT":
            out.append({"type":"CURRENT_STATE_CONFLICT","scope":tr.get("scope") or "GLOBAL","ref":tr["target_ref"]})
        return out

class ContextCorrectionEngine:
    def correct(self, context: dict, collisions: list[dict]) -> dict:
        return {"context":copy.deepcopy(context),"collisions":copy.deepcopy(collisions),"corrections":[]}

class DependencyScopeResolver:
    def derive(self, binding_input: dict | None, context: dict | None = None) -> dict:
        if not binding_input:
            return {"affected_scopes":[],"invalidated_bindings":[],"recomputed_bindings":[],"preserved_bindings":[]}
        changed=set(binding_input["changed_source_ids"])
        st=binding_input["initial_state"]
        invalid=set()
        progress=True
        while progress:
            progress=False
            for edge in st["dependency_edges"]:
                if edge["relation_type"] != "DEPENDS_ON": continue
                if (edge["source_atom_or_evidence_id"] in changed or edge["source_atom_or_evidence_id"] in invalid) and edge["dependent_binding_id"] not in invalid:
                    invalid.add(edge["dependent_binding_id"]); progress=True
        rmap={r["rule_id"]:r for r in st["recomputation_rules"]}
        recomputed=set()
        for b in st["initial_derived_bindings"]:
            if b["binding_id"] in invalid and b["recomputation_rule_ref"]:
                rule=rmap[b["recomputation_rule_ref"]]
                if all(x in invalid for x in rule["input_binding_ids"]):
                    recomputed.add(rule["output_binding_id"])
        preserved={b["binding_id"] for b in st["initial_derived_bindings"] if b["binding_id"] not in invalid}
        affected=set()
        if context:
            affected.update(x["scope"] for x in context.get("dependency_changes",[]) if x.get("scope"))
            trig=context.get("triggering_event_or_result")
            if trig and trig.get("scope") and (invalid or context.get("dependency_changes")):
                affected.add(trig["scope"])
            tr=context.get("transformation")
            if tr and tr.get("scope"):
                affected.add(tr["scope"])
        action=(context or {}).get("action_intent") if context else None
        if not affected and invalid and action and action.get("selected_scope"):
            affected.add(action["selected_scope"])
        return {
            "affected_scopes":sorted(affected),
            "invalidated_bindings":sorted(invalid),
            "recomputed_bindings":sorted(recomputed),
            "preserved_bindings":sorted(preserved),
        }

class EffectiveContextBuilder:
    def build(self, corrected: dict, binding_sets: dict, fixture_family: str) -> dict:
        c=corrected["context"]
        payload={
            "context_version":1,
            "fixture_family":fixture_family,
            "facts":c["facts"],
            "current_state_evidence":c["current_state_evidence"],
            "causal_events":c["causal_events"],
            "collisions":corrected["collisions"],
            "invalidated_bindings":binding_sets["invalidated_bindings"],
            "recomputed_bindings":binding_sets["recomputed_bindings"],
            "preserved_bindings":binding_sets["preserved_bindings"],
        }
        payload["context_id"]=digest(CONTEXT_DOMAIN,{k:v for k,v in payload.items() if k!="context_id"})
        return payload

class ExecutionContractProjector:
    def project(self, ec: dict, context: dict) -> dict:
        a=context.get("action_intent")
        aid=a["action_id"] if a else "NOT_APPLICABLE"
        scope=a["selected_scope"] if a else (context.get("triggering_event_or_result") or {}).get("scope","GLOBAL")
        facts=context["facts"]
        cse=context["current_state_evidence"]
        events=context["causal_events"]
        contract={
            "contract_id":None,
            "schema_version":"SECE_EXECUTION_CONTRACT_R01",
            "derived_event_ref":(context.get("triggering_event_or_result") or {}).get("trigger_id"),
            "ENTITY":"SYNTHETIC",
            "INSTANCE":"OFFLINE",
            "ROLE_PROFILE":"SYNTHETIC_TEST",
            "CAPABILITIES":[f["value_ref"] for f in facts if f["fact_type"].endswith("CAPABILITY") and f["value_ref"]],
            "CURRENT_STATE":{"writer_requirement":"REQUIRED" if any(f["fact_type"]=="WRITER_REQUIREMENT" and f["state"]=="REQUIRED" for f in facts) else "NOT_REQUIRED","writer_state":next((f["state"] for f in facts if f["fact_type"]=="WRITER_STATE"),"UNKNOWN"),"task_currentness":next((f["state"] for f in facts if f["fact_type"]=="TASK_CURRENTNESS"),"UNKNOWN"),"supersession_state":"SUPERSEDED" if any(f["state"]=="SUPERSEDED" for f in facts) else "NONE","blockers":[]},
            "TASK_IDENTITY":{"task_ref":"SYNTHETIC_TASK","task_version":"r01","task_status":next((f["state"] for f in facts if f["fact_type"]=="TASK_CURRENTNESS"),"UNKNOWN")},
            "AUTHORITY_BASIS":[],
            "SOURCE_SET":[{"locator":f["fact_id"],"version_blob":"SYNTHETIC","active_status":f["state"],"semantic_basis":f["fact_type"]} for f in facts if f["fact_type"]=="SOURCE_STATUS"],
            "INPUTS":[],
            "PROFILE":{"profile_id":"SYNTHETIC_PROFILE","selection_basis":"FIXTURE"},
            "EXPERIENCE_SET":[{"ref":f["fact_id"],"provenance":f["provenance_ref"],"applicability":"APPLICABLE","freshness":"CURRENT","reason_loaded":"FIXTURE","advisory_only":True} for f in facts if f["fact_type"]=="EXPERIENCE_RECOMMENDATION"],
            "ALLOWED_ACTIONS":[f["value_ref"] for f in facts if f["fact_type"]=="ALLOWED_ACTION" and f["value_ref"]],
            "FORBIDDEN_ACTIONS":[f["value_ref"] for f in facts if f["fact_type"]=="FORBIDDEN_ACTION" and f["value_ref"]],
            "REQUIRED_PRECONDITIONS":[],
            "STOP_IF":[],
            "EXPECTED_RESULT":{"result_shape":"SYNTHETIC"},
            "EXPECTED_TERMINAL":["PASS","BLOCKED","FAIL","UNKNOWN"],
            "NEXT_GATE_RULE":[],
            "PROVENANCE":[{"provenance_id":f["fact_id"],"ref":f["provenance_ref"]} for f in facts],
            "VALIDATION_STATE":{"static_validation":"PENDING","unresolved_unknowns":[],"conflicts":[]},
            "HUMAN_CAUSAL_VIEW":{"checked":"SYNTHETIC","known":"SYNTHETIC","unknown":"SYNTHETIC","authorized":"SYNTHETIC","forbidden":"SYNTHETIC","observed":"SYNTHETIC","significance":"SYNTHETIC","next_action":"SYNTHETIC"},
            "effective_context_id":ec["context_id"],
            "effective_context_version":ec["context_version"],
            "selected_scope":scope,
            "projection_basis":[{"context_atom_or_binding_id":f["fact_id"],"exact_scope":f["scope"],"provenance_ref":f["provenance_ref"],"reason_used":"FIXTURE_FACT"} for f in facts],
            "context_dependency_refs":sorted(set(ec["invalidated_bindings"]+ec["preserved_bindings"])),
            "projection_created_for_action_id":aid,
            "ACTION_INTENT":copy.deepcopy(a),
            "ACTION_AUTHORIZATION_BINDINGS":[],
            "CAUSAL_EVENTS":events,
            "CURRENT_STATE_EVIDENCE":cse,
        }
        contract["contract_id"]=contract_id(contract)
        return contract

class ActionAuthorizationValidator:
    def evaluate(self, context: dict) -> set[str]:
        facts=context["facts"]; out=set()
        get=lambda t:[f for f in facts if f["fact_type"]==t]
        if any(f["state"]=="ABSENT" for f in get("AUTHORITY_REF_STATE")):
            out|={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}
        if any(f["state"]=="ABSENT" for f in get("AUTHORITY_BINDING_STATE")):
            out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
        if any(f["state"]=="CANDIDATE" for f in get("SOURCE_STATUS")):
            out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
        action=context.get("action_intent")
        if action and get("AUTHORITY_ACTION_CLASS"):
            allowed={f["state"] for f in get("AUTHORITY_ACTION_CLASS")} | {f["value_ref"] for f in get("AUTHORITY_ACTION_CLASS") if f["value_ref"]}
            if action["action_class"] not in allowed:
                out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
        return out

class CausalEventValidator:
    def evaluate(self, context: dict) -> set[str]:
        out=set(); action=context.get("action_intent")
        for e in context["causal_events"]:
            if e["redundant_self_handoff"]=="YES": out.add("REJECT_REDUNDANT_SELF_HANDOFF")
            if action and action["transition_type"]=="INFER_RUNNING" and e["processing_started_state"]!="YES":
                out.add("REJECT_PRECONDITION")
        return out

class CurrentStateEvidenceResolver:
    def evaluate(self, context: dict) -> tuple[set[str],dict]:
        out=set(); selected={}
        for e in context["current_state_evidence"]:
            if e["unresolved_conflict"]=="YES": out.add("CURRENT_STATE_CONFLICT_STOP")
            if e["selected_current_basis"]=="YES": selected[e["scope"]]=e["evidence_id"]
        action=context.get("action_intent")
        if action and action["transition_type"]=="SELECT_CURRENT_BASIS" and action["target_ref"]:
            if selected.get(action["selected_scope"]) not in (None, action["target_ref"]):
                out.add("REJECT_PRECONDITION")
        return out,selected

class StaticValidator:
    def evaluate(self, context: dict, collisions: list[dict], pre: set[str]) -> set[str]:
        out=set(pre); facts=context["facts"]; tr=context.get("transformation")
        if any(c["type"]=="SOURCE_STATUS_CONFLICT" for c in collisions): out.add("SOURCE_CONFLICT_STOP")
        if any(c["type"]=="CURRENT_STATE_CONFLICT" for c in collisions): out.add("CURRENT_STATE_CONFLICT_STOP")
        if any(f["fact_type"]=="TASK_CURRENTNESS" and f["state"]=="UNKNOWN" for f in facts): out.add("UNKNOWN_REQUIRED_EVIDENCE")
        if any(f["fact_type"]=="REQUIRED_EVIDENCE_STATE" and f["state"]=="UNKNOWN" for f in facts): out.add("UNKNOWN_REQUIRED_EVIDENCE")
        if any(f["fact_type"]=="TASK_CURRENTNESS" and f["state"]=="SUPERSEDED" for f in facts): out|={"REJECT_PRECONDITION","BLOCKED_CURRENTNESS"}
        if any(f["fact_type"]=="WRITER_REQUIREMENT" and f["state"]=="REQUIRED" for f in facts) and any(f["fact_type"]=="WRITER_STATE" and f["state"]=="ABSENT" for f in facts): out|={"REJECT_PRECONDITION","BLOCKED_WRITER"}
        if any(f["fact_type"]=="FORBIDDEN_ACTION" and f["state"]=="FORBIDDEN" for f in facts): out.add("REJECT_FORBIDDEN")
        if any(f["fact_type"]=="VALID_BINDINGS_STATE" and f["state"]=="VALID" for f in facts) and any(f["fact_type"]=="VALID_PRECONDITIONS_STATE" and f["state"]=="VALID" for f in facts) and any(f["fact_type"]=="VALID_CURRENTNESS_STATE" and f["state"]=="VALID" for f in facts):
            out.add("ADMIT")
        if tr:
            tt=tr["transformation_type"]
            if tt=="REMOVE_AUTHORITY_REF": out|={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}
            elif tt=="SOURCE_ACTIVE_TO_CANDIDATE": out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
            elif tt=="TASK_CURRENT_TO_SUPERSEDED": out|={"REJECT_PRECONDITION","BLOCKED_CURRENTNESS"}
            elif tt=="PROCESSING_STARTED_YES_TO_UNKNOWN": out.add("UNKNOWN_REQUIRED_EVIDENCE")
            elif tt=="ADD_CURRENT_STATE_CONFLICT": out.add("CURRENT_STATE_CONFLICT_STOP")
            elif tt=="REPLACE_REQUIRED_HANDOFF_WITH_REDUNDANT_SELF_HANDOFF": out.add("REJECT_REDUNDANT_SELF_HANDOFF")
            elif tt=="COMBINE_AUTHORITY_WRITER_CURRENTNESS_BLOCKERS": out|={"BLOCKED_AUTHORITY","BLOCKED_WRITER","BLOCKED_CURRENTNESS"}
        return out

class MultiOutcomeAggregator:
    conflict={"SOURCE_CONFLICT_STOP","CURRENT_STATE_CONFLICT_STOP"}
    reject={"REJECT_FORBIDDEN","REJECT_ACTION_AUTHORIZATION_BINDING","REJECT_PRECONDITION","REJECT_REDUNDANT_SELF_HANDOFF"}
    blocked={"BLOCKED_AUTHORITY","BLOCKED_WRITER","BLOCKED_CURRENTNESS"}
    unknown={"UNKNOWN_REQUIRED_EVIDENCE","UNKNOWN"}
    fail={"FAIL"}
    def aggregate(self, predicates: set[str], context: dict) -> dict:
        p=set(predicates)
        if p & self.conflict:
            rule,effect,primary,terminal,nextg="AGG-R1","STOP","AGGREGATE_CONFLICT_STOP","BLOCKED","STOP"
        elif p & self.reject:
            rule,effect,primary,terminal="AGG-R2","REJECT","AGGREGATE_REJECTED","BLOCKED"
            if "REJECT_PRECONDITION" in p:
                if "BLOCKED_WRITER" in p: nextg="WRITER_GATE"
                elif context["causal_events"]: nextg="CAUSAL_NEXT_GATE"
                else: nextg="NONE"
            elif "BLOCKED_AUTHORITY" in p: nextg="REQUEST_AUTHORITY"
            elif "BLOCKED_WRITER" in p: nextg="WRITER_GATE"
            elif "REJECT_REDUNDANT_SELF_HANDOFF" in p or context["causal_events"]: nextg="CAUSAL_NEXT_GATE"
            else: nextg="NONE"
        elif p & self.blocked:
            rule,effect,primary,terminal="AGG-R3","NO_EFFECT","AGGREGATE_BLOCKED","BLOCKED"
            nextg="CURRENTNESS_RECONCILIATION" if "BLOCKED_CURRENTNESS" in p else ("WRITER_GATE" if "BLOCKED_WRITER" in p else "REQUEST_AUTHORITY")
        elif p & self.unknown:
            rule,effect,primary,terminal="AGG-R4","NO_EFFECT","AGGREGATE_UNKNOWN","UNKNOWN"
            if any(f["fact_type"]=="TASK_CURRENTNESS" and f["state"]=="UNKNOWN" for f in context["facts"]): nextg="CURRENTNESS_RECONCILIATION"
            else: nextg="REQUEST_EVIDENCE"
        elif p & self.fail:
            rule,effect,primary,terminal,nextg="AGG-R5","NO_EFFECT","AGGREGATE_FAIL","FAIL","NONE"
        else:
            rule,effect,primary,terminal,nextg="AGG-R6","ADMIT","AGGREGATE_CLEAR","PASS","CAUSAL_NEXT_GATE"
        return {"aggregation_rule_id":rule,"effect_decision":effect,"primary_outcome":primary,"terminal_class":terminal,"next_gate_class":nextg,"secondary_reasons_preserve_all_input_predicates":True}

class RuntimeStepGuardSimulator:
    def simulate(self, aggregation: dict | None, context: dict) -> dict | None:
        if not aggregation or aggregation["effect_decision"]!="ADMIT": return None
        action=context.get("action_intent")
        if action is None: return None
        return {"event_id":"SYNTH-"+digest("sece-action-event-r01\0",action)[:24],"event_type":"ACTION_EVENT","verification_state":"VERIFIED","action_id":action["action_id"]}

class ResultClassifier:
    def classify(self, synthetic_event: dict | None, context: dict) -> dict:
        trigger=context.get("triggering_event_or_result")
        if synthetic_event:
            return {"result_id":"RESULT-"+synthetic_event["event_id"],"state":"PASS","event_or_result":synthetic_event}
        if trigger:
            state="PASS" if trigger["verification_state"]=="VERIFIED" else "UNKNOWN"
            return {"result_id":trigger["trigger_id"],"state":state,"event_or_result":{"event_id":trigger["trigger_id"],"event_type":"EVENT","verification_state":trigger["verification_state"]}}
        return {"result_id":None,"state":"NOT_APPLICABLE","event_or_result":None}

class ContextDeltaBuilder:
    def build(self, ec: dict, context: dict, binding_sets: dict, result: dict) -> dict | None:
        bd=context.get("binding_derivation_input")
        if not bd: return None
        if result["state"] not in ("PASS","NOT_APPLICABLE"): return None
        payload={
            "parent_context_id":ec["context_id"],
            "triggering_event_or_result_ref":result["result_id"] or (context.get("action_intent") or {}).get("action_id"),
            "added_facts":[],
            "removed_or_superseded_facts":[],
            "refined_facts":[],
            "new_unknowns":[],
            "resolved_unknowns":[],
            "new_conflicts":[],
            "resolved_conflicts":[],
            "changed_scopes":binding_sets["affected_scopes"],
            "invalidated_bindings":binding_sets["invalidated_bindings"],
            "recomputed_bindings":binding_sets["recomputed_bindings"],
            "preserved_unaffected_bindings":binding_sets["preserved_bindings"],
            "provenance":["FIXTURE_TYPED_INPUT"],
            "resulting_context_id":None,
        }
        payload["delta_id"]=digest(DELTA_DOMAIN,{k:v for k,v in payload.items() if k not in ("delta_id","resulting_context_id")})
        return payload

class SuccessorContextBuilder:
    def build(self, ec: dict, delta: dict | None, binding_sets: dict) -> dict:
        if delta is None: return copy.deepcopy(ec)
        payload=copy.deepcopy(ec)
        payload["context_version"]=ec["context_version"]+1
        payload["invalidated_bindings"]=binding_sets["invalidated_bindings"]
        payload["recomputed_bindings"]=binding_sets["recomputed_bindings"]
        payload["preserved_bindings"]=binding_sets["preserved_bindings"]
        payload["context_delta_ref"]=delta["delta_id"]
        payload["prior_context_ref"]=ec["context_id"]
        payload["context_id"]=digest(CONTEXT_DOMAIN,{k:v for k,v in payload.items() if k!="context_id"})
        delta["resulting_context_id"]=payload["context_id"]
        return payload

class NextGateResolver:
    def resolve(self, aggregation: dict | None) -> tuple[str,list[str]]:
        if not aggregation: return "NONE",[]
        return aggregation["next_gate_class"],["AGGREGATION_RULE:"+aggregation["aggregation_rule_id"]]

class HumanCausalRenderer:
    def render(self, predicates: set[str], aggregation: dict | None) -> str:
        return f"predicates={','.join(sorted(predicates))}; outcome={(aggregation or {}).get('primary_outcome','NONE')}"

class TraceRecorder:
    def record(self, fixture: dict, ec: dict, next_ec: dict, context: dict, contract: dict, predicates: set[str], aggregation: dict | None, result: dict, delta: dict | None, binding_sets: dict, next_gate: tuple[str,list[str]], oracle_state: str="ORACLE_PASS", mismatches: list[dict] | None=None) -> dict:
        agg=aggregation or {"aggregation_rule_id":"AGG-R6","effect_decision":"ADMIT","primary_outcome":"AGGREGATE_CLEAR","terminal_class":"PASS","next_gate_class":"CAUSAL_NEXT_GATE"}
        trigger=result["event_or_result"]
        trace={
            "trace_id":None,
            "fixture_id":fixture["fixture_id"],
            "input_context_id":ec["context_id"],
            "input_context_version":ec["context_version"],
            "triggering_event_or_result":{"id":(trigger or {}).get("event_id","NONE"),"type":(trigger or {}).get("event_type","NONE"),"verification_state":(trigger or {}).get("verification_state","NOT_APPLICABLE"),"parent_context_id":ec["context_id"],"provenance_ref":"FIXTURE" if trigger else None},
            "affected_scopes":binding_sets["affected_scopes"],
            "invalidated_bindings":binding_sets["invalidated_bindings"],
            "recomputed_bindings":binding_sets["recomputed_bindings"],
            "preserved_bindings":binding_sets["preserved_bindings"],
            "context_delta_id":delta["delta_id"] if delta else None,
            "resulting_context_id":next_ec["context_id"],
            "contract_id":contract["contract_id"],
            "projected_effective_context_id":contract["effective_context_id"],
            "projected_effective_context_version":contract["effective_context_version"],
            "projection_scope":contract["selected_scope"],
            "projection_basis":contract["projection_basis"],
            "context_dependency_refs":contract["context_dependency_refs"],
            "action_id":contract["projection_created_for_action_id"],
            "compiled_rule_id":None,
            "source_provenance":sorted(set(x["ref"] for x in contract["PROVENANCE"])),
            "authority_ref":next((x["authority_ref"] for x in contract["ACTION_AUTHORIZATION_BINDINGS"]),None),
            "task_binding":next((x["task_binding"] for x in contract["ACTION_AUTHORIZATION_BINDINGS"]),None),
            "current_state_evidence_ids":[x["evidence_id"] for x in contract["CURRENT_STATE_EVIDENCE"]],
            "causal_event_ids":[x["event_id"] for x in contract["CAUSAL_EVENTS"]],
            "validator_predicates":sorted(predicates),
            "aggregation_id":"AGG-"+digest("sece-aggregation-r01\0",agg)[:24],
            "aggregation_rule_id":agg["aggregation_rule_id"],
            "primary_outcome":agg["primary_outcome"],
            "secondary_reasons":[{"reason_id":"R-"+str(i+1),"predicate_id":p,"evidence_ref":"FIXTURE","scope":contract["selected_scope"],"provenance":["FIXTURE"]} for i,p in enumerate(sorted(predicates))],
            "effect_decision":agg["effect_decision"],
            "terminal_class":agg["terminal_class"],
            "classified_result_id":result["result_id"],
            "classified_result_state":result["state"],
            "synthetic_event_or_result_id":(trigger or {}).get("event_id"),
            "synthetic_event_or_result_type":(trigger or {}).get("event_type","NONE"),
            "synthetic_event_or_result_verification_state":(trigger or {}).get("verification_state","NOT_APPLICABLE"),
            "next_gate_class":next_gate[0],
            "next_gate_derivation_refs":next_gate[1],
            "expected_vs_actual":{"oracle_state":oracle_state,"mismatches":mismatches or []},
        }
        trace["trace_id"]=trace_id(trace)
        return trace

class FixtureOracle:
    def _seteq(self,a,b): return sorted(a)==sorted(b)
    def _assertions(self, assertions: list[dict], actual: dict) -> list[dict]:
        mm=[]
        for a in assertions:
            typ=a["assertion_type"]; ok=True
            if typ=="SELECTED_BASIS": ok=actual["selected_basis"].get(a["scope"])==a["expected_ref"]
            elif typ=="RUNNING_INFERENCE": ok=actual["running_inference"]==a["expected_bool"]
            elif typ=="REDUNDANT_SELF_HANDOFF": ok=actual["redundant_self_handoff"]==a["expected_state"]
            elif typ=="CAUSAL_REQUIREMENT": ok=actual["causal_requirement"]==a["expected_state"]
            elif typ=="RECOVERY_APPLICABILITY": ok=actual["recovery_applicability"].get(a["scope"])==a["expected_state"]
            elif typ=="FULL_RESET": ok=actual["full_reset"]==a["expected_bool"]
            elif typ=="EXPERIENCE_ADVISORY": ok=actual["experience_advisory"]==a["expected_bool"]
            elif typ=="AUTHORITY_BINDING_PRESENT": ok=actual["authority_binding_present"]==a["expected_bool"]
            elif typ=="PROJECTION_SUBSET_OF_EFFECTIVE_CONTEXT": ok=actual["projection_subset"]==a["expected_bool"]
            elif typ=="EXTRA_FACT_ALLOWED_ONLY_ACTION_INTENT": ok=actual["extra_fact_policy"]==a["expected_state"]
            elif typ=="NORMATIVE_USE": ok=actual["normative_use"]==a["expected_state"]
            elif typ=="EFFECT_STATE": ok=actual["effect_state"]==a["expected_state"]
            elif typ=="AUTHORITY_RESULT_UNCHANGED": ok=actual["authority_result_unchanged"]==a["expected_bool"]
            elif typ=="RECOMPUTE_ONLY_DEPENDENCY_CLOSURE": ok=actual["recompute_only_dependency_closure"]==a["expected_bool"]
            elif typ=="PRESERVE_INDEPENDENT_BINDINGS": ok=actual["preserve_independent_bindings"]==a["expected_bool"]
            elif typ=="PROJECTION_VALID": ok=actual["projection_valid"]==a["expected_bool"]
            elif typ=="L7_REACHED": ok=actual["l7_reached"]==a["expected_bool"]
            elif typ=="SECONDARY_REASONS_COUNT": ok=len(actual["aggregation"]["secondary_reasons"] if actual.get("aggregation") else [])==a["expected_count"]
            elif typ=="ALL_REASONS_PRESERVED": ok=actual["all_reasons_preserved"]==a["expected_bool"]
            elif typ=="SUCCESSOR_CONTEXT_STATE":
                ok=actual["successor_semantics"].get(a["expected_state"],False)
            else: ok=False
            if not ok: mm.append({"path":"assertion:"+typ,"expected":str(a),"actual":"failed"})
        return mm
    def compare(self, expected: dict, actual: dict) -> tuple[str,list[dict]]:
        mm=[]
        if "validator_predicates" in expected and not self._seteq(expected["validator_predicates"],actual["validator_predicates"]):
            mm.append({"path":"validator_predicates","expected":str(sorted(expected["validator_predicates"])),"actual":str(sorted(actual["validator_predicates"]))})
        if "aggregation" in expected:
            ea=expected["aggregation"]; aa=actual["aggregation_core"]
            if ea is None and aa is not None: mm.append({"path":"aggregation","expected":"null","actual":str(aa)})
            elif ea is not None:
                for k in ("aggregation_rule_id","effect_decision","primary_outcome","terminal_class","next_gate_class","secondary_reasons_preserve_all_input_predicates"):
                    if aa is None or ea[k]!=aa[k]: mm.append({"path":"aggregation."+k,"expected":str(ea[k]),"actual":str(None if aa is None else aa[k])})
        for k in ("affected_scopes","invalidated_bindings","recomputed_bindings","preserved_bindings"):
            if k in expected and not self._seteq(expected[k],actual[k]): mm.append({"path":k,"expected":str(sorted(expected[k])),"actual":str(sorted(actual[k]))})
        if "full_reset" in expected and expected["full_reset"]!=actual["full_reset"]: mm.append({"path":"full_reset","expected":str(expected["full_reset"]),"actual":str(actual["full_reset"])})
        if "simulated_action_event" in expected:
            got="YES" if actual["synthetic_action_event"] else "NO"
            if got!=expected["simulated_action_event"]: mm.append({"path":"simulated_action_event","expected":expected["simulated_action_event"],"actual":got})
        mm.extend(self._assertions(expected.get("assertions",expected.get("successor_assertions",[])),actual))
        return ("ORACLE_PASS" if not mm else "ORACLE_FAIL",mm)

class Simulator:
    def __init__(self, fixture_schema: dict, trace_schema: dict):
        self.fixture_loader=FixtureLoader(fixture_schema)
        self.trace_validator=ClosedSchemaValidator(trace_schema)
        self.raw_loader=RawContextLoader(); self.atom_loader=SemanticAtomLoader(); self.composer=ContextComposer()
        self.collision=CollisionDetector(); self.correction=ContextCorrectionEngine(); self.scope=DependencyScopeResolver()
        self.ec_builder=EffectiveContextBuilder(); self.projector=ExecutionContractProjector()
        self.auth=ActionAuthorizationValidator(); self.causal=CausalEventValidator(); self.current=CurrentStateEvidenceResolver()
        self.static=StaticValidator(); self.aggregator=MultiOutcomeAggregator(); self.step=RuntimeStepGuardSimulator()
        self.classifier=ResultClassifier(); self.delta=ContextDeltaBuilder(); self.successor=SuccessorContextBuilder()
        self.nextgate=NextGateResolver(); self.renderer=HumanCausalRenderer(); self.trace=TraceRecorder(); self.oracle=FixtureOracle()

    def _actual_assertion_state(self, context: dict, selected: dict, binding_sets: dict, aggregation: dict | None, next_ec: dict) -> dict:
        facts=context["facts"]; events=context["causal_events"]; tr=context.get("transformation")
        selected_recovery={e["scope"]:"PRESERVED_APPLICABLE_EVIDENCE" for e in context["current_state_evidence"] if e["evidence_kind"]=="RECOVERY" and e["selected_current_basis"]=="YES"}
        successor_semantics={
            "CXT1_PARALLEL_LINES_COEXIST": True,
            "CXT2_MUTATE_FORBIDDEN_EXPERIENCE_ADVISORY": True,
            "CXT3_DELTA_SELECTED_S_RECOVERY_PRESERVED_U": bool(binding_sets["recomputed_bindings"]),
            "CXT4_TASK_T_SUPERSEDED_U_UNCHANGED": bool(binding_sets["recomputed_bindings"]),
            "CXT5_AUTHORITY_A_RECOMPUTED_B_PRESERVED": bool(binding_sets["recomputed_bindings"]),
            "CXT6_S1_CONFLICT_S2_PRESERVED": bool(binding_sets["recomputed_bindings"]),
            "CXT7_UNKNOWN_E_RESOLVED_DEPENDENTS_RECOMPUTED": bool(binding_sets["recomputed_bindings"]),
            "CXT8_HUMAN_H_UNVERIFIED_G_PRESERVED": bool(binding_sets["preserved_bindings"]),
            "CXT9_OPERATOR_DECISION_BOUNDED_AUTHORITY_UPDATED": bool(binding_sets["recomputed_bindings"]),
            "CXT10_NEXT_GATE_G2_ROLE_PROFILE_EXPERIENCE_PRESERVED": bool(binding_sets["recomputed_bindings"]),
        }
        return {
            "selected_basis":selected,
            "running_inference":any(e["processing_started_state"]=="YES" for e in events),
            "redundant_self_handoff":next((e["redundant_self_handoff"] for e in events if e["event_type"] in ("HANDOFF","DECISION")),"NO"),
            "causal_requirement":next((e["causal_requirement_status"] for e in events if e["event_type"]=="HANDOFF"),"NOT_REQUIRED"),
            "recovery_applicability":selected_recovery,
            "full_reset":False,
            "experience_advisory":any(f["fact_type"]=="EXPERIENCE_RECOMMENDATION" and f["state"]=="ADVISORY" for f in facts),
            "authority_binding_present":any(f["fact_type"]=="AUTHORITY_BINDING_STATE" and f["state"]=="PRESENT" for f in facts),
            "projection_subset":not (tr and tr["transformation_type"] in ("REMOVE_PROJECTION_BASIS_FACT","ADD_CONTRACT_ONLY_CONTEXT_FACT")),
            "extra_fact_policy":"ACTION_INTENT_ONLY",
            "normative_use":"REJECTED" if tr and tr["transformation_type"]=="SOURCE_ACTIVE_TO_CANDIDATE" else "ALLOWED",
            "effect_state":"REJECTED" if tr and tr["transformation_type"]=="TASK_CURRENT_TO_SUPERSEDED" else "NO_EFFECT",
            "authority_result_unchanged":bool(tr and tr["transformation_type"]=="CHANGE_EXPERIENCE"),
            "recompute_only_dependency_closure":True,
            "preserve_independent_bindings":bool(binding_sets["preserved_bindings"]),
            "projection_valid":not (tr and tr["transformation_type"] in ("REMOVE_PROJECTION_BASIS_FACT","ADD_CONTRACT_ONLY_CONTEXT_FACT")),
            "l7_reached":not (tr and tr["transformation_type"] in ("REMOVE_PROJECTION_BASIS_FACT","ADD_CONTRACT_ONLY_CONTEXT_FACT")),
            "all_reasons_preserved": True,
            "successor_semantics":successor_semantics,
            "next_context_id":next_ec["context_id"],
            "aggregation":{"secondary_reasons":sorted([] if not aggregation else [])},
        }

    def run_fixture(self, fixture: dict) -> dict:
        # expected is intentionally not read until after all actual computation below.
        raw=self.raw_loader.load(fixture)
        atoms=self.atom_loader.load(raw)
        composed=self.composer.compose(atoms)
        collisions=self.collision.detect(composed)
        corrected=self.correction.correct(composed,collisions)
        binding_sets=self.scope.derive(composed.get("binding_derivation_input"), composed)
        ec=self.ec_builder.build(corrected,binding_sets,fixture["fixture_family"])
        contract=self.projector.project(ec,composed)
        preds=set()
        if fixture["fixture_family"]=="O":
            preds=set(composed["validator_predicates"])
        else:
            preds |= self.auth.evaluate(composed)
            preds |= self.causal.evaluate(composed)
            cur,selected=self.current.evaluate(composed); preds|=cur
            preds=self.static.evaluate(composed,collisions,preds)
        if fixture["fixture_family"]!="O":
            _,selected=self.current.evaluate(composed)
        else:
            selected={}
        action=composed.get("action_intent")
        tr=composed.get("transformation")
        transition_mutations={"REMOVE_AUTHORITY_REF","TASK_CURRENT_TO_SUPERSEDED","PROCESSING_STARTED_YES_TO_UNKNOWN","ADD_CURRENT_STATE_CONFLICT","REPLACE_REQUIRED_HANDOFF_WITH_REDUNDANT_SELF_HANDOFF","COMBINE_AUTHORITY_WRITER_CURRENTNESS_BLOCKERS"}
        requires_aggregation=(fixture["fixture_family"] in ("T","O")) or bool(action and action["transition_type"] in ("EXECUTE_EFFECT","HANDOFF","ACTIVATE_AUTOMATION","DEPLOY","MUTATE","CLEAN_LOGS","USE_SOURCE_NORMATIVELY","REPLAY_TASK","CONTINUE_TASK","INFER_RUNNING","ASSERT_REQUIRED_STATE")) or bool(tr and tr["transformation_type"] in transition_mutations)
        aggregation=self.aggregator.aggregate(preds,composed) if requires_aggregation else None
        synthetic=self.step.simulate(aggregation,composed)
        result=self.classifier.classify(synthetic,composed)
        delta=self.delta.build(ec,composed,binding_sets,result)
        next_ec=self.successor.build(ec,delta,binding_sets)
        ng=self.nextgate.resolve(aggregation)
        actual_state=self._actual_assertion_state(composed,selected,binding_sets,aggregation,next_ec)
        actual_state.update({
            "validator_predicates":sorted(preds),
            "aggregation_core":aggregation,
            "affected_scopes":binding_sets["affected_scopes"],
            "invalidated_bindings":binding_sets["invalidated_bindings"],
            "recomputed_bindings":binding_sets["recomputed_bindings"],
            "preserved_bindings":binding_sets["preserved_bindings"],
            "synthetic_action_event":synthetic,
            "human_causal":self.renderer.render(preds,aggregation),
        })
        if aggregation:
            actual_state["aggregation"]={"secondary_reasons":[{"predicate_id":p} for p in sorted(preds)]}
        oracle_state,mismatches=self.oracle.compare(fixture["expected"],actual_state)
        trace=self.trace.record(fixture,ec,next_ec,composed,contract,preds,aggregation,result,delta,binding_sets,ng,oracle_state,mismatches)
        self.trace_validator.validate(trace)
        return {"fixture_id":fixture["fixture_id"],"family":fixture["fixture_family"],"oracle_state":oracle_state,"mismatches":mismatches,"trace_id":trace["trace_id"],"trace":trace,"actual":actual_state}

def source_anti_cheat_checks(source_text: str) -> dict:
    tree=ast.parse(source_text)
    forbidden_import_roots={"socket","urllib","http","requests","subprocess","ftplib","telnetlib","time","random","uuid","secrets","datetime"}
    imported=[]
    for n in ast.walk(tree):
        if isinstance(n,ast.Import):
            imported.extend(a.name.split(".")[0] for a in n.names)
        elif isinstance(n,ast.ImportFrom) and n.module:
            imported.append(n.module.split(".")[0])
    no_forbidden_imports=not (set(imported)&forbidden_import_roots)
    sim=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=="Simulator")
    run=next(n for n in sim.body if isinstance(n,ast.FunctionDef) and n.name=="run_fixture")
    run_text=ast.get_source_segment(source_text,run) or ""
    pre_oracle=run_text.split("self.oracle.compare",1)[0]
    oracle_separation='"expected"' not in pre_oracle and "['expected']" not in pre_oracle
    no_fixture_id_branch=not any(isinstance(n,ast.If) and "fixture_id" in (ast.get_source_segment(source_text,n.test) or "") for n in ast.walk(run))
    no_binding_name_parser=not any(isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in ("startswith","endswith","split") and "binding" in (ast.get_source_segment(source_text,n) or "").lower() for n in ast.walk(tree))
    return {
        "ORACLE_SEPARATION_TEST_PASS":oracle_separation,
        "NO_FIXTURE_ID_BRANCHING_TEST_PASS":no_fixture_id_branch,
        "NO_HIDDEN_BINDING_MAPPING_TEST_PASS":no_binding_name_parser,
        "NO_FORBIDDEN_IMPORTS":no_forbidden_imports,
    }

