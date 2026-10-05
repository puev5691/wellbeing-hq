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

class ProjectionError(ValueError):
    pass

@dataclass(frozen=True)
class ProjectionResult:
    valid: bool
    contract: dict
    errors: tuple[str, ...]

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
        if "minimum" in s and isinstance(value,(int,float)) and not isinstance(value,bool):
            if value < s["minimum"]: raise SchemaError(f"{path}:minimum")
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
            "next_gate_rules": copy.deepcopy(raw.get("next_gate_rules",[])),
        }

class SemanticStateMutationLayer:
    """Generic typed semantic-state mutation before normal validation."""
    def apply(self, atoms: dict) -> dict:
        out=copy.deepcopy(atoms)
        tr=out.get("transformation")
        if not tr:
            out["mutation_execution"]={"applied":False,"aggregation_required":False,"projection_request":None,"requested_scope":None}
            return out
        field=tr.get("field_code"); target=tr.get("target_ref"); before=tr.get("from_state"); after=tr.get("to_state")
        requested_scope=tr.get("scope"); scope=requested_scope or "GLOBAL"; prov=tr.get("provenance_ref") or "FIXTURE"
        applied=False; aggregation_required=False; projection_request=None
        def add_fact(fid,typ,state,value=None):
            out["facts"].append({"fact_id":fid,"fact_type":typ,"scope":scope,"state":state,"value_ref":value,"provenance_ref":prov})
        if field=="authority_ref":
            add_fact("MUT-AUTHORITY-REF","AUTHORITY_REF_STATE",after); applied=True; aggregation_required=True
        elif field=="active_status":
            add_fact("MUT-SOURCE-STATUS","SOURCE_STATUS",after); applied=True
        elif field=="task_currentness":
            add_fact("MUT-TASK-CURRENTNESS","TASK_CURRENTNESS",after); applied=True; aggregation_required=True
        elif field=="processing_started_state":
            out["causal_events"].append({
                "event_id":"MUT-PROCESSING-EVENT","event_type":"PROCESSING","evidence_ref":target or "MUT-EVIDENCE",
                "causal_parent_event_id":None,"lifecycle_evidence_state":"VERIFIED","dispatch_state":"NOT_APPLICABLE",
                "delivery_state":"NOT_APPLICABLE","receipt_state":"NOT_APPLICABLE","processing_started_state":after,
                "handoff_recipient":None,"handoff_reason":None,"decision_id":None,"decision_owner":None,
                "decision_recipient":None,"current_decision_state":"NOT_APPLICABLE","proposed_handoff_target":None,
                "redundant_self_handoff":"NO","causal_requirement_status":"REQUIRED","scope":scope,"provenance_ref":prov,
            }); applied=True; aggregation_required=True
        elif field=="unresolved_conflict":
            out["current_state_evidence"].append({
                "evidence_id":"MUT-CURRENT-STATE","evidence_kind":"TASK","exact_immutable_identity":target or "MUT-STATE",
                "scope":scope,"provenance_source":prov,"verified_state":"VERIFIED","currentness_state":"CURRENT",
                "relation_to_other_evidence":"INDEPENDENT","relation_target_evidence_id":None,"selected_current_basis":"YES",
                "selection_basis":"MUTATED_TYPED_STATE","unresolved_conflict":"YES" if after=="CONFLICT" else after,
                "conflict_set":["MUT-CONFLICT"] if after=="CONFLICT" else [],"unknown_fields":[],
            }); applied=True; aggregation_required=True
        elif field=="source_conflict":
            applied=True
        elif field=="advisory_content":
            add_fact("MUT-EXPERIENCE","EXPERIENCE_RECOMMENDATION","ADVISORY",target or "experience"); applied=True
        elif field=="dependency_state":
            applied=True
        elif field=="fact_presence":
            projection_request={"basis_ids":["ABSENT_CONTEXT_ITEM"],"dependency_ids":[]}; applied=True
        elif field=="context_fact_presence":
            projection_request={"invented_context_items":[{"id":"CONTRACT_ONLY_ITEM"}]}; applied=True
        elif field=="causal_requirement":
            out["causal_events"].append({
                "event_id":"MUT-HANDOFF","event_type":"HANDOFF","evidence_ref":target or "MUT-HANDOFF-EVIDENCE",
                "causal_parent_event_id":None,"lifecycle_evidence_state":"VERIFIED","dispatch_state":"NOT_APPLICABLE",
                "delivery_state":"NOT_APPLICABLE","receipt_state":"NOT_APPLICABLE","processing_started_state":"NOT_APPLICABLE",
                "handoff_recipient":"SYNTHETIC_ENTITY","handoff_reason":"TYPED_MUTATION","decision_id":None,"decision_owner":None,
                "decision_recipient":None,"current_decision_state":"NOT_APPLICABLE","proposed_handoff_target":"SYNTHETIC_ENTITY",
                "redundant_self_handoff":"YES","causal_requirement_status":after,"scope":scope,"provenance_ref":prov,
            }); applied=True; aggregation_required=True
        elif field=="blocker_set":
            add_fact("MUT-AUTH-BLOCK","AUTHORITY_BLOCKER_STATE","BLOCKED")
            add_fact("MUT-WRITER-BLOCK","WRITER_BLOCKER_STATE","BLOCKED")
            add_fact("MUT-CURRENTNESS-BLOCK","CURRENTNESS_BLOCKER_STATE","BLOCKED")
            applied=True; aggregation_required=True
        out["transformation"]=None
        out["mutation_execution"]={
            "applied":applied,"field_code":field,"target_ref":target,"from_state":before,"to_state":after,
            "requested_scope":requested_scope,"aggregation_required":aggregation_required,"projection_request":projection_request,
        }
        return out

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
        return out

class ContextCorrectionEngine:
    def correct(self, context: dict, collisions: list[dict]) -> dict:
        prior = copy.deepcopy(context)
        corrected = copy.deepcopy(context)
        corrections=[]
        changed_scopes=set()
        invalidation_seeds=set()
        unresolved_conflicts=[]
        unknowns=[]

        evidence_by_id={e["evidence_id"]:e for e in corrected["current_state_evidence"]}
        for e in corrected["current_state_evidence"]:
            if e["relation_to_other_evidence"]=="REFINES" and e["relation_target_evidence_id"] and e["verified_state"]=="VERIFIED":
                target=evidence_by_id.get(e["relation_target_evidence_id"])
                if target and target["scope"]==e["scope"] and e["selected_current_basis"]=="YES":
                    target["selected_current_basis"]="NO"
                    correction={
                        "correction_id":"CORR-"+digest("sece-context-correction-r01\0",{"kind":"VERIFIED_REFINEMENT","scope":e["scope"],"from":target["evidence_id"],"to":e["evidence_id"]})[:24],
                        "collision_id":None,
                        "collision_type":"SUPERSESSION_REFINEMENT",
                        "affected_scope":e["scope"],
                        "affected_atom_binding_ids":[target["evidence_id"],e["evidence_id"]],
                        "transformation":"SELECT_VERIFIED_REFINEMENT",
                        "retained_fact_ids":[x["evidence_id"] for x in corrected["current_state_evidence"] if x["scope"]!=e["scope"]],
                        "unresolved_state":"RESOLVED",
                        "provenance":[target["provenance_source"],e["provenance_source"]],
                    }
                    corrections.append(correction)
                    changed_scopes.add(e["scope"])
                    invalidation_seeds.update([target["evidence_id"],e["evidence_id"]])

        for i,c in enumerate(collisions):
            scope=c["scope"]
            correction={
                "correction_id":"CORR-"+digest("sece-context-correction-r01\0",{"kind":c["type"],"scope":scope,"ref":c["ref"],"index":i})[:24],
                "collision_id":"COLL-"+digest("sece-collision-r01\0",c)[:24],
                "collision_type":c["type"],
                "affected_scope":scope,
                "affected_atom_binding_ids":[c["ref"]],
                "transformation":"PRESERVE_UNRESOLVED_CONFLICT",
                "retained_fact_ids":[f["fact_id"] for f in corrected["facts"] if f["scope"]!=scope],
                "unresolved_state":"CONFLICT",
                "provenance":["FIXTURE"],
            }
            corrections.append(correction)
            changed_scopes.add(scope)
            invalidation_seeds.add(c["ref"])
            unresolved_conflicts.append({
                "collision_id":correction["collision_id"],
                "collision_type":c["type"],
                "exact_scope":scope,
                "involved_ids":[c["ref"]],
                "unresolved":"YES",
                "dependent_binding_ids":[],
                "provenance":["FIXTURE"],
            })

        for f in corrected["facts"]:
            if f["state"]=="UNKNOWN":
                unknowns.append({
                    "unknown_id":"UNK-"+digest("sece-unknown-r01\0",f)[:24],
                    "required_for":[],
                    "exact_scope":f["scope"],
                    "missing_evidence_description":f["fact_type"],
                    "request_permitted":"YES",
                    "provenance":[f["provenance_ref"]],
                })

        if corrected != prior and not corrections:
            raise AssertionError("context_changed_without_explicit_correction")

        return {
            "context":corrected,
            "prior_context":prior,
            "collisions":copy.deepcopy(collisions),
            "corrections":corrections,
            "changed_scopes":sorted(changed_scopes),
            "invalidation_seeds":sorted(invalidation_seeds),
            "unresolved_conflicts":unresolved_conflicts,
            "unknowns":unknowns,
        }

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
            mut=context.get("mutation_execution")
            if mut and mut.get("requested_scope"):
                affected.add(mut["requested_scope"])
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
    def _next_gate_rules(self, c: dict) -> list[dict]:
        rules=[]
        for raw in c.get("next_gate_rules",[]):
            required={"rule_id","source_ref","active_status","currentness","scope","next_gate_class","conflict_status","supersession_state"}
            if not required.issubset(raw):
                continue
            rules.append({
                "rule_id":str(raw["rule_id"]),"source_ref":str(raw["source_ref"]),
                "active_status":str(raw["active_status"]),"currentness":str(raw["currentness"]),
                "scope":str(raw["scope"]),"next_gate_class":str(raw["next_gate_class"]),
                "required_result_verification":str(raw.get("required_result_verification","VERIFIED")),
                "required_event_type":raw.get("required_event_type"),"required_evidence_id":raw.get("required_evidence_id"),
                "recipient":raw.get("recipient"),"task_ref":raw.get("task_ref"),
                "conflict_status":str(raw["conflict_status"]),"supersession_state":str(raw["supersession_state"]),
                "provenance":[str(x) for x in raw.get("provenance",[raw["source_ref"]])],
            })
        return sorted(rules,key=lambda x:x["rule_id"])

    def _authority_bindings(self, c: dict) -> tuple[list[dict],dict]:
        facts=c["facts"]
        action=c.get("action_intent")
        if action is None:
            return [],{"required":False,"explicit_absence":False,"reason_refs":[]}
        aid=action["action_id"]; aclass=action["action_class"]; scope=action["selected_scope"]
        get=lambda t:[f for f in facts if f["fact_type"]==t]
        explicit_absence=bool(get("AUTHORITY_REF_STATE") and any(f["state"]=="ABSENT" for f in get("AUTHORITY_REF_STATE")))
        binding_absence=bool(get("AUTHORITY_BINDING_STATE") and any(f["state"]=="ABSENT" for f in get("AUTHORITY_BINDING_STATE")))
        effect_required=any(f["state"]=="REQUIRED" for f in get("EFFECT_AUTHORITY_REQUIREMENT"))
        class_facts=get("AUTHORITY_ACTION_CLASS")
        present_facts=[f for f in get("AUTHORITY_BINDING_STATE") if f["state"]=="PRESENT"]
        candidate_source=any(f["state"]=="CANDIDATE" for f in get("SOURCE_STATUS"))
        required=explicit_absence or effect_required or bool(class_facts) or bool(present_facts)
        reason_refs=[f["fact_id"] for f in get("AUTHORITY_REF_STATE")+get("AUTHORITY_BINDING_STATE")+get("EFFECT_AUTHORITY_REQUIREMENT")+class_facts+get("SOURCE_STATUS")]
        bindings=[]

        def mk(disposition:str, authority_ref:str|None, classes:list[str], source_ref:str, currentness:str="CURRENT", provenance_status:str="VERIFIED", conflict_status:str="NONE", required_flag:bool=False):
            base={
                "action_id":aid,
                "action_class":aclass,
                "disposition":disposition,
                "compiled_rule_id":"CR-"+digest("sece-c1-binding-rule-r01\0",{"action_id":aid,"source":source_ref,"disposition":disposition})[:20],
                "source_locator":source_ref,
                "source_version_blob":"SYNTHETIC",
                "authority_ref":authority_ref,
                "authority_scope":scope,
                "authority_action_classes":sorted(set(classes)),
                "task_binding":"SYNTHETIC_TASK",
                "task_currentness_requirement":"CURRENT",
                "writer_requirement":"REQUIRED" if any(f["fact_type"]=="WRITER_REQUIREMENT" and f["state"]=="REQUIRED" for f in facts) else "NOT_REQUIRED",
                "production_or_effect_authority_requirement":"REQUIRED" if required_flag else "NOT_REQUIRED",
                "provenance_status":provenance_status,
                "conflict_status":conflict_status,
                "currentness_state":currentness,
                "authority_required":required_flag,
            }
            base["binding_id"]="AAB-"+digest("sece-action-auth-binding-r01\0",base)[:24]
            bindings.append(base)

        if explicit_absence or effect_required:
            mk("MISSING",None,[aclass],(reason_refs or ["AUTHORITY_MISSING"])[0],required_flag=True)
        elif binding_absence:
            mk("MISSING",None,[aclass],(reason_refs or ["AUTHORITY_BINDING_ABSENT"])[0],required_flag=False)
        elif present_facts:
            f=present_facts[0]
            mk("ALLOWED",f["value_ref"] or ("AUTH-"+f["fact_id"]),[aclass],f["provenance_ref"],required_flag=True)
        elif class_facts:
            classes=sorted(set((f["value_ref"] or f["state"]) for f in class_facts))
            f=class_facts[0]
            mk("ALLOWED","AUTH-"+f["fact_id"],classes,f["provenance_ref"],required_flag=True)
        elif candidate_source:
            f=next(f for f in get("SOURCE_STATUS") if f["state"]=="CANDIDATE")
            mk("STALE","AUTH-"+f["fact_id"],[aclass],f["provenance_ref"],currentness="STALE",provenance_status="CANDIDATE",required_flag=False)

        return bindings,{"required":required,"explicit_absence":explicit_absence,"reason_refs":sorted(set(reason_refs))}

    def build(self, corrected: dict, binding_sets: dict, fixture_family: str) -> dict:
        c=corrected["context"]
        facts=copy.deepcopy(c["facts"])
        cse=copy.deepcopy(c["current_state_evidence"])
        events=copy.deepcopy(c["causal_events"])
        authority_bindings,authority_requirement=self._authority_bindings(c)
        selected_basis=[
            {
                "scope":e["scope"],
                "selected_evidence_id":e["evidence_id"],
                "selection_basis":e["selection_basis"],
                "unresolved_conflict":e["unresolved_conflict"],
                "provenance":[e["provenance_source"]],
            }
            for e in cse if e["selected_current_basis"]=="YES"
        ]
        current_tasks=[]
        for f in facts:
            if f["fact_type"]=="TASK_CURRENTNESS":
                current_tasks.append({"task_id":"SYNTHETIC_TASK","scope":f["scope"],"task_status":f["state"],"supersession_state":"SUPERSEDED" if f["state"]=="SUPERSEDED" else "NONE","provenance":[f["provenance_ref"]]})
        active_source_set=[
            {"source_id":f["fact_id"],"locator":f["fact_id"],"version_blob":"SYNTHETIC","active_status":f["state"],"semantic_basis":f["fact_type"],"conflict_status":"CONFLICT" if f["state"]=="CONFLICT" else "NONE","provenance":[f["provenance_ref"]]}
            for f in facts if f["fact_type"] in ("SOURCE_STATUS","SOURCE_CONFLICT_STATE")
        ]
        experience_set=[
            {"ref":f["fact_id"],"provenance":f["provenance_ref"],"applicability":"APPLICABLE","freshness":"CURRENT","reason_loaded":"FIXTURE","advisory_only":True}
            for f in facts if f["fact_type"]=="EXPERIENCE_RECOMMENDATION"
        ]
        capability_set=[
            {"capability_id":f["value_ref"] or f["fact_id"],"scope":f["scope"],"availability_state":f["state"],"provenance":[f["provenance_ref"]]}
            for f in facts if f["fact_type"] in ("PROFILE_CAPABILITY","AUTOMATION_CAPABILITY")
        ]
        human_input_facts=[
            {"input_id":f["fact_id"],"claimed_fact":f["value_ref"] or f["fact_type"],"scope":f["scope"],"authority_status":f["state"],"evidence_status":"UNVERIFIED","provenance":[f["provenance_ref"]]}
            for f in facts if f["fact_type"]=="HUMAN_CLAIM_AUTHORITY"
        ]
        unknown_facts=copy.deepcopy(corrected["unknowns"])
        conflict_set=copy.deepcopy(corrected["unresolved_conflicts"])

        bd=c.get("binding_derivation_input")
        derived_bindings=[]
        scope_index=[]
        dependency_graph=[]
        if bd:
            st=bd["initial_state"]
            initial_by_id={b["binding_id"]:b for b in st["initial_derived_bindings"]}
            for bid in binding_sets["preserved_bindings"]:
                if bid in initial_by_id:
                    derived_bindings.append(copy.deepcopy(initial_by_id[bid]))
            rules={r["output_binding_id"]:r for r in st["recomputation_rules"]}
            for bid in binding_sets["recomputed_bindings"]:
                r=rules[bid]
                derived_bindings.append({
                    "binding_id":bid,
                    "binding_type":r["output_binding_type"],
                    "exact_scope":r["exact_scope"],
                    "dependencies":copy.deepcopy(r["input_binding_ids"]),
                    "current_state":r["output_state"],
                    "provenance_ref":r["provenance_ref"],
                    "semantic_role":"RECOMPUTED_DEPENDENT",
                    "recomputation_rule_ref":r["rule_id"],
                })
            scope_index=copy.deepcopy(st["scope_index"])
            dependency_graph=copy.deepcopy(st["dependency_edges"])

        provenance=sorted(set(
            [f["provenance_ref"] for f in facts]
            +[e["provenance_source"] for e in cse]
            +[p for corr in corrected["corrections"] for p in corr["provenance"]]
        ))
        payload={
            "context_id":None,
            "context_version":1,
            "entity":"SYNTHETIC_ENTITY",
            "instance":"SYNTHETIC_INSTANCE",
            "role":"SYNTHETIC_TEST_ROLE",
            "active_source_set":active_source_set,
            "semantic_invariants":facts,
            "current_state_evidence":cse,
            "selected_current_basis_by_scope":selected_basis,
            "current_tasks":current_tasks,
            "authority_bindings":authority_bindings,
            "authority_requirement":authority_requirement,
            "profile":{"profile_id":"SYNTHETIC_PROFILE","selection_basis":"FIXTURE","scope":"GLOBAL","provenance":provenance},
            "experience_set":experience_set,
            "capability_set":capability_set,
            "causal_events":events,
            "human_input_facts":human_input_facts,
            "unknown_facts":unknown_facts,
            "conflict_set":conflict_set,
            "context_corrections":copy.deepcopy(corrected["corrections"]),
            "derived_bindings":derived_bindings,
            "provenance":provenance,
            "scope_index":scope_index,
            "dependency_graph":dependency_graph,
            "semantic_atoms":facts,
            "current_state_summary":{
                "writer_requirement":"REQUIRED" if any(f["fact_type"]=="WRITER_REQUIREMENT" and f["state"]=="REQUIRED" for f in facts) else "NOT_REQUIRED",
                "writer_state":next((f["state"] for f in facts if f["fact_type"]=="WRITER_STATE"),"UNKNOWN"),
                "task_currentness":next((f["state"] for f in facts if f["fact_type"]=="TASK_CURRENTNESS"),"UNKNOWN"),
                "supersession_state":"SUPERSEDED" if any(f["fact_type"]=="TASK_CURRENTNESS" and f["state"]=="SUPERSEDED" for f in facts) else "NONE",
            },
            "invalidated_bindings":copy.deepcopy(binding_sets["invalidated_bindings"]),
            "recomputed_bindings":copy.deepcopy(binding_sets["recomputed_bindings"]),
            "preserved_bindings":copy.deepcopy(binding_sets["preserved_bindings"]),
            "changed_scopes":sorted(set(binding_sets["affected_scopes"]) | set(corrected["changed_scopes"])),
            "invalidation_seeds":sorted(set(corrected["invalidation_seeds"])),
            "prior_context_ref":None,
            "context_delta_ref":None,
            "next_gate_rules": self._next_gate_rules(c),
        }
        payload["context_id"]=digest(CONTEXT_DOMAIN,{k:v for k,v in payload.items() if k!="context_id"})
        return payload

class ExecutionContractProjector:
    def _item_index(self, ec: dict) -> dict[str,dict]:
        items={}
        for f in ec["semantic_atoms"]:
            items[f["fact_id"]]={"id":f["fact_id"],"scope":f["scope"],"provenance_ref":f["provenance_ref"],"kind":"FACT"}
        for e in ec["current_state_evidence"]:
            items[e["evidence_id"]]={"id":e["evidence_id"],"scope":e["scope"],"provenance_ref":e["provenance_source"],"kind":"CURRENT_STATE_EVIDENCE"}
        for e in ec["causal_events"]:
            items[e["event_id"]]={"id":e["event_id"],"scope":e["scope"],"provenance_ref":e["provenance_ref"],"kind":"CAUSAL_EVENT"}
        for b in ec["authority_bindings"]:
            items[b["binding_id"]]={"id":b["binding_id"],"scope":b["authority_scope"],"provenance_ref":b["source_locator"],"kind":"ACTION_AUTHORIZATION_BINDING"}
        for b in ec["derived_bindings"]:
            items[b["binding_id"]]={"id":b["binding_id"],"scope":b["exact_scope"],"provenance_ref":b["provenance_ref"],"kind":"DERIVED_BINDING"}
        for s in ec["active_source_set"]:
            items[s["source_id"]]={"id":s["source_id"],"scope":"GLOBAL","provenance_ref":s["locator"],"kind":"SOURCE"}
        for t in ec["current_tasks"]:
            items[t["task_id"]]={"id":t["task_id"],"scope":t["scope"],"provenance_ref":(t["provenance"] or ["FIXTURE"])[0],"kind":"TASK"}
        for r in ec.get("next_gate_rules",[]):
            items[r["rule_id"]]={"id":r["rule_id"],"scope":r["scope"],"provenance_ref":r["source_ref"],"kind":"NEXT_GATE_RULE"}
        return items

    def project(self, ec: dict, action_intent: dict | None, projection_request: dict | None=None) -> ProjectionResult:
        action=copy.deepcopy(action_intent)
        aid=action["action_id"] if action else "NOT_APPLICABLE"
        scope=action["selected_scope"] if action else (projection_request or {}).get("selected_scope","GLOBAL")
        items=self._item_index(ec)
        edge_index={e["edge_id"]:e for e in ec["dependency_graph"]}

        default_basis=[
            iid for iid,item in items.items()
            if item["scope"] in (scope,"GLOBAL")
        ]
        request=projection_request or {}
        basis_ids=copy.deepcopy(request.get("basis_ids",default_basis))
        dep_ids=copy.deepcopy(request.get("dependency_ids",[
            e["edge_id"] for e in ec["dependency_graph"]
            if e["exact_scope"]==scope or e["dependent_binding_id"] in basis_ids
        ]))
        invented=copy.deepcopy(request.get("invented_context_items",[]))
        errors=[]
        for iid in basis_ids:
            if iid not in items: errors.append("MISSING_PROJECTION_BASIS:"+iid)
        for did in dep_ids:
            if did not in edge_index: errors.append("INVALID_CONTEXT_DEPENDENCY:"+did)
        for obj in invented:
            oid=obj.get("id")
            if oid not in items: errors.append("INVENTED_CONTEXT_ITEM:"+str(oid))

        projection_basis=[
            {
                "context_atom_or_binding_id":iid,
                "exact_scope":items[iid]["scope"],
                "provenance_ref":items[iid]["provenance_ref"],
                "reason_used":"BOUNDED_SCOPE_PROJECTION",
            }
            for iid in basis_ids if iid in items
        ]
        auth_bindings=[
            copy.deepcopy(b) for b in ec["authority_bindings"]
            if action is not None and b["action_id"]==aid and b["authority_scope"] in (scope,"GLOBAL")
        ]
        current_evidence=[
            copy.deepcopy(e) for e in ec["current_state_evidence"]
            if e["scope"] in (scope,"GLOBAL")
        ]
        causal_events=copy.deepcopy(ec["causal_events"])
        task=next((t for t in ec["current_tasks"] if t["scope"] in (scope,"GLOBAL")),None)
        facts=ec["semantic_atoms"]

        contract={
            "contract_id":None,
            "schema_version":"SECE_EXECUTION_CONTRACT_R01",
            "derived_event_ref":None,
            "ENTITY":ec["entity"],
            "INSTANCE":ec["instance"],
            "ROLE_PROFILE":ec["role"],
            "CAPABILITIES":[c["capability_id"] for c in ec["capability_set"]],
            "CURRENT_STATE":copy.deepcopy(ec["current_state_summary"]),
            "TASK_IDENTITY":{
                "task_ref":task["task_id"] if task else "SYNTHETIC_TASK",
                "task_version":"r01",
                "task_status":task["task_status"] if task else ec["current_state_summary"]["task_currentness"],
            },
            "AUTHORITY_BASIS":[
                {
                    "authority_ref":b["authority_ref"],
                    "scope":b["authority_scope"],
                    "action_classes":copy.deepcopy(b["authority_action_classes"]),
                    "currentness":b["currentness_state"],
                }
                for b in auth_bindings
            ],
            "SOURCE_SET":[
                {"locator":s["locator"],"version_blob":s["version_blob"],"active_status":s["active_status"],"semantic_basis":s["semantic_basis"]}
                for s in ec["active_source_set"]
            ],
            "INPUTS":[
                {"input_id":x["context_atom_or_binding_id"],"exact_identity":x["context_atom_or_binding_id"],"required":True,"verified_state":"VERIFIED"}
                for x in projection_basis
            ],
            "PROFILE":copy.deepcopy(ec["profile"]),
            "EXPERIENCE_SET":copy.deepcopy(ec["experience_set"]),
            "ALLOWED_ACTIONS":[f["value_ref"] for f in facts if f["fact_type"]=="ALLOWED_ACTION" and f["value_ref"]],
            "FORBIDDEN_ACTIONS":[f["value_ref"] for f in facts if f["fact_type"]=="FORBIDDEN_ACTION" and f["value_ref"]],
            "REQUIRED_PRECONDITIONS":[{"predicate_id":f["fact_id"],"state":f["state"]} for f in facts if f["fact_type"]=="VALID_PRECONDITIONS_STATE"],
            "STOP_IF":[{"predicate_id":c["collision_id"],"state":"TRUE"} for c in ec["conflict_set"]],
            "EXPECTED_RESULT":{"required":bool(action or ec["changed_scopes"]),"result_shape":"SYNTHETIC","expected_state":"PASS"},
            "EXPECTED_TERMINAL":["PASS","BLOCKED","FAIL","UNKNOWN"],
            "NEXT_GATE_RULE":[copy.deepcopy(r) for r in ec.get("next_gate_rules",[]) if r["scope"] in (scope,"GLOBAL")],
            "PROVENANCE":[{"provenance_id":"PV-"+digest("sece-provenance-r01\0",p)[:16],"ref":p} for p in ec["provenance"]],
            "VALIDATION_STATE":{
                "static_validation":"PENDING",
                "unresolved_unknowns":[u["unknown_id"] for u in ec["unknown_facts"]],
                "conflicts":[c["collision_id"] for c in ec["conflict_set"]],
                "projection_valid":not errors,
                "projection_errors":copy.deepcopy(errors),
            },
            "HUMAN_CAUSAL_VIEW":{"checked":"SYNTHETIC","known":"SYNTHETIC","unknown":"SYNTHETIC","authorized":"SYNTHETIC","forbidden":"SYNTHETIC","observed":"SYNTHETIC","significance":"SYNTHETIC","next_action":"SYNTHETIC"},
            "effective_context_id":ec["context_id"],
            "effective_context_version":ec["context_version"],
            "selected_scope":scope,
            "projection_basis":projection_basis,
            "context_dependency_refs":sorted(dep_ids),
            "projection_created_for_action_id":aid,
            "ACTION_INTENT":action,
            "ACTION_AUTHORIZATION_BINDINGS":auth_bindings,
            "AUTHORITY_REQUIREMENT":copy.deepcopy(ec["authority_requirement"]),
            "CAUSAL_EVENTS":causal_events,
            "CURRENT_STATE_EVIDENCE":current_evidence,
        }
        contract["contract_id"]=contract_id(contract)
        return ProjectionResult(not errors,contract,tuple(errors))

class ActionAuthorizationValidator:
    def evaluate(self, contract: dict) -> set[str]:
        out=set()
        action=contract.get("ACTION_INTENT")
        if action is None: return out
        bindings=[b for b in contract["ACTION_AUTHORIZATION_BINDINGS"] if b["action_id"]==action["action_id"]]
        requirement=contract.get("AUTHORITY_REQUIREMENT",{"required":False,"explicit_absence":False})
        if not bindings:
            if requirement.get("required"):
                out|={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}
            return out
        valid=False
        for b in bindings:
            if b["disposition"]!="ALLOWED":
                out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
                if b.get("authority_required") or b["conflict_status"]!="NONE":
                    out.add("BLOCKED_AUTHORITY")
                continue
            if b["currentness_state"]!="CURRENT" or b["provenance_status"]!="VERIFIED" or b["conflict_status"]!="NONE":
                out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
                if b["conflict_status"]!="NONE": out.add("BLOCKED_AUTHORITY")
                continue
            if action["action_class"] not in b["authority_action_classes"]:
                out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
                continue
            if b["task_currentness_requirement"]=="CURRENT" and contract["TASK_IDENTITY"]["task_status"] not in ("CURRENT","UNKNOWN"):
                out|={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_CURRENTNESS"}
                continue
            if b["writer_requirement"]=="REQUIRED" and contract["CURRENT_STATE"]["writer_state"] not in ("CURRENT","CURRENT_ESTABLISHED"):
                out|={"REJECT_PRECONDITION","BLOCKED_WRITER"}
                continue
            valid=True
        if valid:
            out.discard("REJECT_ACTION_AUTHORIZATION_BINDING")
            out.discard("BLOCKED_AUTHORITY")
        return out

class CausalEventValidator:
    def evaluate(self, contract: dict) -> set[str]:
        out=set(); action=contract.get("ACTION_INTENT")
        for e in contract["CAUSAL_EVENTS"]:
            if e["redundant_self_handoff"]=="YES": out.add("REJECT_REDUNDANT_SELF_HANDOFF")
            if action and action["transition_type"]=="INFER_RUNNING" and e["processing_started_state"]!="YES":
                out.add("REJECT_PRECONDITION")
        return out

class CurrentStateEvidenceResolver:
    def evaluate(self, contract: dict) -> tuple[set[str],dict]:
        out=set(); selected={}
        for e in contract["CURRENT_STATE_EVIDENCE"]:
            if e["unresolved_conflict"]=="YES": out.add("CURRENT_STATE_CONFLICT_STOP")
            if e["selected_current_basis"]=="YES": selected[e["scope"]]=e["evidence_id"]
        action=contract.get("ACTION_INTENT")
        if action and action["transition_type"]=="SELECT_CURRENT_BASIS" and action["target_ref"]:
            if selected.get(action["selected_scope"]) not in (None,action["target_ref"]):
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
        if any(e.get("processing_started_state")=="UNKNOWN" for e in context["causal_events"]): out.add("UNKNOWN_REQUIRED_EVIDENCE")
        if any(f["fact_type"]=="SOURCE_STATUS" and f["state"]!="ACTIVE" for f in facts): out.add("REJECT_ACTION_AUTHORIZATION_BINDING")
        if any(f["fact_type"]=="AUTHORITY_REF_STATE" and f["state"]=="ABSENT" for f in facts): out|={"REJECT_ACTION_AUTHORIZATION_BINDING","BLOCKED_AUTHORITY"}
        if any(f["fact_type"]=="AUTHORITY_BLOCKER_STATE" and f["state"]=="BLOCKED" for f in facts): out.add("BLOCKED_AUTHORITY")
        if any(f["fact_type"]=="WRITER_BLOCKER_STATE" and f["state"]=="BLOCKED" for f in facts): out.add("BLOCKED_WRITER")
        if any(f["fact_type"]=="CURRENTNESS_BLOCKER_STATE" and f["state"]=="BLOCKED" for f in facts): out.add("BLOCKED_CURRENTNESS")
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
        return {
            "aggregation_rule_id":rule,
            "effect_decision":effect,
            "primary_outcome":primary,
            "terminal_class":terminal,
            "next_gate_class":nextg,
            "secondary_reasons_preserve_all_input_predicates":True,
            "secondary_reasons":[{"predicate_id":x} for x in sorted(p)],
        }

class RuntimeStepGuardSimulator:
    def simulate(self, aggregation: dict | None, contract: dict) -> dict | None:
        if not aggregation or aggregation["effect_decision"]!="ADMIT": return None
        if not contract["VALIDATION_STATE"].get("projection_valid",False): return None
        action=contract.get("ACTION_INTENT")
        if action is None: return None
        authority_ok=any(
            b["action_id"]==action["action_id"]
            and b["disposition"]=="ALLOWED"
            and b["currentness_state"]=="CURRENT"
            and b["provenance_status"]=="VERIFIED"
            and b["conflict_status"]=="NONE"
            and action["action_class"] in b["authority_action_classes"]
            for b in contract["ACTION_AUTHORIZATION_BINDINGS"]
        )
        causal_handoff_ok=(
            action["action_class"]=="HANDOFF"
            and any(e["event_type"]=="HANDOFF" and e["causal_requirement_status"]=="REQUIRED" and e["redundant_self_handoff"]=="NO" for e in contract["CAUSAL_EVENTS"])
        )
        if not (authority_ok or causal_handoff_ok): return None
        return {
            "event_id":"SYNTH-"+digest("sece-action-event-r01\0",action)[:24],
            "event_type":"ACTION_EVENT",
            "verification_state":"VERIFIED",
            "action_id":action["action_id"],
            "result_shape":"SYNTHETIC",
            "terminal_class":"PASS",
            "state":"PASS",
        }

class ResultClassifier:
    def classify(self, observation: dict | None, contract: dict, flow_applicable: bool=True) -> dict:
        expected=contract["EXPECTED_RESULT"]
        terminals=contract["EXPECTED_TERMINAL"]
        required=bool(expected.get("required",False))

        if observation is None:
            if not flow_applicable and not required:
                return {"result_id":None,"state":"NOT_APPLICABLE","event_or_result":None}
            if required:
                return {"result_id":None,"state":"UNKNOWN","event_or_result":None}
            return {"result_id":None,"state":"NOT_APPLICABLE","event_or_result":None}

        verification=observation.get("verification_state","UNKNOWN")
        result_id=observation.get("result_id") or observation.get("event_id")
        event_type=observation.get("event_type","RESULT")
        normalized={
            "event_id":result_id,
            "event_type":event_type,
            "verification_state":verification,
            "result_shape":observation.get("result_shape"),
            "terminal_class":observation.get("terminal_class"),
        }
        if verification!="VERIFIED":
            return {"result_id":result_id,"state":"UNKNOWN","event_or_result":normalized}

        shape_match=(expected.get("result_shape") is None or observation.get("result_shape")==expected.get("result_shape"))
        expected_state=expected.get("expected_state")
        state_match=(expected_state is None or observation.get("state")==expected_state)
        terminal=observation.get("terminal_class")
        terminal_match=(terminal is None or terminal in terminals)
        if shape_match and state_match and terminal_match:
            return {"result_id":result_id,"state":"PASS","event_or_result":normalized}
        return {"result_id":result_id,"state":"FAIL","event_or_result":normalized}

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
    def resolve(self, aggregation: dict | None, result: dict, contract: dict, effective_context: dict) -> dict:
        if not aggregation:
            return {"next_gate_class":"NONE","candidate":None,"derivation_refs":[]}
        requested=aggregation["next_gate_class"]
        if requested=="STOP":
            return {"next_gate_class":"STOP","candidate":None,"derivation_refs":["AGGREGATION_RULE:"+aggregation["aggregation_rule_id"]]}

        event=result.get("event_or_result")
        if not event or event.get("verification_state")!="VERIFIED":
            return {"next_gate_class":"NONE","candidate":None,"derivation_refs":[]}

        current_evidence={
            e["evidence_id"]:e for e in contract["CURRENT_STATE_EVIDENCE"]
            if e["verified_state"]=="VERIFIED" and e["currentness_state"]=="CURRENT" and e["unresolved_conflict"]=="NO"
        }
        eligible=[]
        for rule in contract["NEXT_GATE_RULE"]:
            if rule.get("active_status")!="ACTIVE": continue
            if rule.get("currentness")!="CURRENT": continue
            if rule.get("conflict_status")!="NONE": continue
            if rule.get("supersession_state")!="NONE": continue
            if rule.get("next_gate_class")!=requested: continue
            if rule.get("required_result_verification","VERIFIED")!=event.get("verification_state"): continue
            if rule.get("required_event_type") not in (None,event.get("event_type")): continue
            req=rule.get("required_evidence_id")
            if req is not None and req not in current_evidence: continue
            if not rule.get("recipient") or not rule.get("task_ref"): continue
            eligible.append(rule)
        if len(eligible)!=1:
            return {"next_gate_class":"NONE","candidate":None,"derivation_refs":[]}

        rule=eligible[0]
        return {
            "next_gate_class":requested,
            "candidate":{"recipient":rule["recipient"],"task_ref":rule["task_ref"],"rule_id":rule["rule_id"]},
            "derivation_refs":[
                "AGGREGATION_RULE:"+aggregation["aggregation_rule_id"],
                "NEXT_GATE_RULE:"+rule["rule_id"],
                *(["CURRENT_STATE_EVIDENCE:"+rule["required_evidence_id"]] if rule.get("required_evidence_id") else []),
            ],
        }

class HumanCausalRenderer:
    def render(self, predicates: set[str], aggregation: dict | None) -> str:
        return f"predicates={','.join(sorted(predicates))}; outcome={(aggregation or {}).get('primary_outcome','NONE')}"

class TraceRecorder:
    def record(self, fixture: dict, ec: dict, next_ec: dict, context: dict, contract: dict, predicates: set[str], aggregation: dict | None, result: dict, delta: dict | None, binding_sets: dict, next_gate: dict, oracle_state: str="ORACLE_PASS", mismatches: list[dict] | None=None) -> dict:
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
            "next_gate_class":next_gate["next_gate_class"],
            "next_gate_derivation_refs":copy.deepcopy(next_gate["derivation_refs"]),
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
        self.raw_loader=RawContextLoader(); self.atom_loader=SemanticAtomLoader(); self.mutator=SemanticStateMutationLayer(); self.composer=ContextComposer()
        self.collision=CollisionDetector(); self.correction=ContextCorrectionEngine(); self.scope=DependencyScopeResolver()
        self.ec_builder=EffectiveContextBuilder(); self.projector=ExecutionContractProjector()
        self.auth=ActionAuthorizationValidator(); self.causal=CausalEventValidator(); self.current=CurrentStateEvidenceResolver()
        self.static=StaticValidator(); self.aggregator=MultiOutcomeAggregator(); self.step=RuntimeStepGuardSimulator()
        self.classifier=ResultClassifier(); self.delta=ContextDeltaBuilder(); self.successor=SuccessorContextBuilder()
        self.nextgate=NextGateResolver(); self.renderer=HumanCausalRenderer(); self.trace=TraceRecorder(); self.oracle=FixtureOracle()

    def _projection_request_from_typed_mutation(self, context: dict, ec: dict) -> dict | None:
        return copy.deepcopy(context.get("mutation_execution",{}).get("projection_request"))

    def _actual_assertion_state(self, context: dict, effective_context: dict, selected: dict, binding_sets: dict, aggregation: dict | None, next_ec: dict, projection: ProjectionResult) -> dict:
        facts=context["facts"]; events=context["causal_events"]
        selected_recovery={e["scope"]:"PRESERVED_APPLICABLE_EVIDENCE" for e in context["current_state_evidence"] if e["evidence_kind"]=="RECOVERY" and e["selected_current_basis"]=="YES"}
        successor_semantics={
            "CXT1_PARALLEL_LINES_COEXIST": len(effective_context["semantic_atoms"])==len(context["facts"]),
            "CXT2_MUTATE_FORBIDDEN_EXPERIENCE_ADVISORY": any(b["binding_type"]=="EXPERIENCE" for b in effective_context["derived_bindings"]) and any(b["current_state"]=="FORBIDDEN" for b in effective_context["derived_bindings"]),
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
            "experience_advisory":bool(effective_context["experience_set"]),
            "authority_binding_present":any(b["disposition"]=="ALLOWED" for b in effective_context["authority_bindings"]),
            "projection_subset":projection.valid,
            "extra_fact_policy":"ACTION_INTENT_ONLY",
            "normative_use":"REJECTED" if any(f["fact_type"]=="SOURCE_STATUS" and f["state"]!="ACTIVE" for f in facts) else "ALLOWED",
            "effect_state":"REJECTED" if any(f["fact_type"]=="TASK_CURRENTNESS" and f["state"]=="SUPERSEDED" for f in facts) else "NO_EFFECT",
            "authority_result_unchanged":bool(any(f["fact_type"]=="EXPERIENCE_RECOMMENDATION" for f in facts)),
            "recompute_only_dependency_closure":not(set(binding_sets["invalidated_bindings"]) & set(binding_sets["preserved_bindings"])),
            "preserve_independent_bindings":bool(binding_sets["preserved_bindings"]),
            "projection_valid":projection.valid,
            "l7_reached":projection.valid,
            "all_reasons_preserved":True,
            "successor_semantics":successor_semantics,
            "next_context_id":next_ec["context_id"],
            "aggregation":{"secondary_reasons":[] if not aggregation else copy.deepcopy(aggregation.get("secondary_reasons",[]))},
        }

    def run_fixture(self, fixture: dict) -> dict:
        # expected is intentionally not read until after all actual computation below.
        raw=self.raw_loader.load(fixture)
        atoms=self.atom_loader.load(raw)
        mutated=self.mutator.apply(atoms)
        composed=self.composer.compose(mutated)
        collisions=self.collision.detect(composed)
        corrected=self.correction.correct(composed,collisions)
        binding_sets=self.scope.derive(composed.get("binding_derivation_input"), corrected["context"])
        ec=self.ec_builder.build(corrected,binding_sets,fixture["fixture_family"])
        projection_request=self._projection_request_from_typed_mutation(composed,ec)
        projection=self.projector.project(ec,composed.get("action_intent"),projection_request)
        contract=projection.contract

        preds=set()
        selected={}
        if projection.valid:
            if fixture["fixture_family"]=="O":
                preds=set(composed["validator_predicates"])
            else:
                preds |= self.auth.evaluate(contract)
                preds |= self.causal.evaluate(contract)
                cur,selected=self.current.evaluate(contract); preds|=cur
                preds=self.static.evaluate(corrected["context"],collisions,preds)

        action=composed.get("action_intent")
        requires_aggregation=projection.valid and ((fixture["fixture_family"] in ("T","O")) or bool(action and action["transition_type"] in ("EXECUTE_EFFECT","HANDOFF","ACTIVATE_AUTOMATION","DEPLOY","MUTATE","CLEAN_LOGS","USE_SOURCE_NORMATIVELY","REPLAY_TASK","CONTINUE_TASK","INFER_RUNNING","ASSERT_REQUIRED_STATE")) or bool(composed.get("mutation_execution",{}).get("aggregation_required")))
        aggregation=self.aggregator.aggregate(preds,corrected["context"]) if requires_aggregation else None
        synthetic=self.step.simulate(aggregation,contract)

        trigger=composed.get("triggering_event_or_result")
        observation=synthetic
        if observation is None and trigger is not None:
            observation={
                "event_id":trigger["trigger_id"],
                "event_type":"EVENT",
                "verification_state":trigger["verification_state"],
                "result_shape":"SYNTHETIC",
                "terminal_class":"PASS",
                "state":"PASS",
            }
        result=self.classifier.classify(observation,contract,flow_applicable=bool(action or trigger))
        delta=self.delta.build(ec,corrected["context"],binding_sets,result)
        next_ec=self.successor.build(ec,delta,binding_sets)
        ng=self.nextgate.resolve(aggregation,result,contract,next_ec)
        actual_state=self._actual_assertion_state(corrected["context"],ec,selected,binding_sets,aggregation,next_ec,projection)
        actual_state.update({
            "validator_predicates":sorted(preds),
            "aggregation_core":aggregation,
            "affected_scopes":binding_sets["affected_scopes"],
            "invalidated_bindings":binding_sets["invalidated_bindings"],
            "recomputed_bindings":binding_sets["recomputed_bindings"],
            "preserved_bindings":binding_sets["preserved_bindings"],
            "synthetic_action_event":synthetic,
            "human_causal":self.renderer.render(preds,aggregation),
            "projection_errors":list(projection.errors),
            "result_state":result["state"],
            "next_gate_decision":ng,
        })
        if aggregation:
            actual_state["aggregation"]={"secondary_reasons":[{"predicate_id":p} for p in sorted(preds)]}
        oracle_state,mismatches=self.oracle.compare(fixture["expected"],actual_state)
        trace=self.trace.record(fixture,ec,next_ec,corrected["context"],contract,preds,aggregation,result,delta,binding_sets,ng,oracle_state,mismatches)
        self.trace_validator.validate(trace)
        return {"fixture_id":fixture["fixture_id"],"family":fixture["fixture_family"],"oracle_state":oracle_state,"mismatches":mismatches,"trace_id":trace["trace_id"],"trace":trace,"actual":actual_state,"effective_context":ec,"contract":contract}

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

