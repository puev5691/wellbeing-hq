from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Protocol

RUNTIME_DOMAIN = "sece-runtime-integration-r01\0"
RESOLUTION_DOMAIN = "sece-runtime-evidence-resolution-r01\0"
ACTOR_BINDING_DOMAIN = "sece-actor-execution-binding-r01\0"
INTENT_DOMAIN = "sece-effect-intent-r01\0"
ADMISSION_DOMAIN = "sece-pre-effect-admission-r01\0"
OUTCOME_DOMAIN = "sece-effect-outcome-r01\0"
RESULT_DOMAIN = "sece-runtime-result-r01\0"

SENSITIVE_FACT_CLASSES = {
    "AUTHORITY",
    "TASK_CURRENTNESS",
    "WRITER",
    "CURRENT_STATE",
    "SOURCE_CURRENTNESS",
    "RECOVERY_STATE",
    "OUTCOME",
}


def canonicalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: canonicalize(value[k]) for k in sorted(value)}
    if isinstance(value, list):
        return [canonicalize(v) for v in value]
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(canonicalize(value), ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def digest(domain: str, value: Any) -> str:
    return hashlib.sha256((domain + canonical_json(value)).encode("utf-8")).hexdigest()


def identity(domain: str, value: Mapping[str, Any], id_field: str) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop(id_field, None)
    return digest(domain, payload)


class RuntimeBoundaryError(ValueError):
    pass


class RuntimeInputAdapter:
    """Transport/normalize only. It never upgrades authority/currentness/writer/task facts."""

    REQUIRED = {
        "entity_ref", "instance_ref", "role", "evidence_items", "requested_facts",
        "actor_execution_binding", "proposed_action", "active_source_refs", "immutable_inputs",
        "unknowns", "conflicts",
    }

    def normalize(self, raw: Mapping[str, Any]) -> dict[str, Any]:
        missing = self.REQUIRED - set(raw)
        if missing:
            raise RuntimeBoundaryError(f"runtime_input_missing:{sorted(missing)}")
        evidence = copy.deepcopy(list(raw["evidence_items"]))
        for item in evidence:
            if item.get("derived_positive_fact_ids"):
                raise RuntimeBoundaryError("adapter_may_not_assert_derived_positive_fact")
            if item.get("adapter_asserted_positive") is True:
                raise RuntimeBoundaryError("adapter_may_not_assert_positive_runtime_fact")
        envelope = {
            "envelope_id": None,
            "entity_ref": str(raw["entity_ref"]),
            "instance_ref": str(raw["instance_ref"]),
            "role": str(raw["role"]),
            "active_source_refs": copy.deepcopy(list(raw["active_source_refs"])),
            "evidence_items": evidence,
            "requested_facts": copy.deepcopy(list(raw["requested_facts"])),
            "actor_execution_binding": normalize_actor_binding(raw["actor_execution_binding"]),
            "immutable_inputs": copy.deepcopy(list(raw["immutable_inputs"])),
            "profile": copy.deepcopy(raw.get("profile")),
            "capabilities": copy.deepcopy(list(raw.get("capabilities", []))),
            "experience": copy.deepcopy(list(raw.get("experience", []))),
            "causal_events": copy.deepcopy(list(raw.get("causal_events", []))),
            "human_input": copy.deepcopy(list(raw.get("human_input", []))),
            "unknowns": copy.deepcopy(list(raw["unknowns"])),
            "conflicts": copy.deepcopy(list(raw["conflicts"])),
            "proposed_action": copy.deepcopy(dict(raw["proposed_action"])),
        }
        envelope["envelope_id"] = identity(RUNTIME_DOMAIN, envelope, "envelope_id")
        return envelope


@dataclass(frozen=True)
class TrustPolicy:
    """Explicit policy binding; presence of a source class alone is never sufficient."""

    policy_ref: str
    allowed_source_classes: Mapping[str, tuple[str, ...]]
    required_trust_basis_prefixes: tuple[str, ...] = ()

    def allows(self, item: Mapping[str, Any], requested_fact: Mapping[str, Any]) -> bool:
        fact_class = str(requested_fact["semantic_fact_class"])
        allowed = set(self.allowed_source_classes.get(fact_class, ()))
        if item.get("source_class") not in allowed:
            return False
        trust_ref = str(item.get("trust_basis_ref") or "")
        if not trust_ref:
            return False
        if self.required_trust_basis_prefixes and not any(
            trust_ref.startswith(prefix) for prefix in self.required_trust_basis_prefixes
        ):
            return False
        return True


class RuntimeEvidenceResolver:
    REQUIRED_EVIDENCE_FIELDS = {
        "evidence_id", "evidence_kind", "exact_immutable_locator", "exact_version_or_blob",
        "exact_scope", "source_class", "trust_basis_ref", "verified_state", "currentness_state",
        "semantic_fact_class", "conflict_state", "selected_basis_relation", "provenance_chain",
        "semantic_value", "unknown_fields",
    }

    def _support_exact(self, item: Mapping[str, Any], req: Mapping[str, Any]) -> bool:
        return (
            item.get("semantic_fact_class") == req.get("semantic_fact_class")
            and item.get("exact_scope") == req.get("exact_scope")
            and item.get("semantic_value") == req.get("semantic_value")
        )

    def _admissible(self, item: Mapping[str, Any], req: Mapping[str, Any], policy: TrustPolicy) -> tuple[bool, str | None]:
        missing = self.REQUIRED_EVIDENCE_FIELDS - set(item)
        if missing:
            return False, "MALFORMED_EVIDENCE"
        if not item.get("exact_immutable_locator") or not item.get("exact_version_or_blob"):
            return False, "MISSING_IMMUTABLE_IDENTITY"
        if item.get("verified_state") != "VERIFIED":
            return False, "UNVERIFIED"
        if req.get("required_currentness") == "CURRENT" and item.get("currentness_state") != "CURRENT":
            return False, "NOT_CURRENT"
        if item.get("conflict_state") != "NONE":
            return False, "CONFLICT"
        if not item.get("provenance_chain"):
            return False, "INCOMPLETE_PROVENANCE"
        if not policy.allows(item, req):
            return False, "TRUST_POLICY_REJECT"
        if not self._support_exact(item, req):
            return False, "SCOPE_OR_VALUE_MISMATCH"
        return True, None

    def resolve(self, envelope: Mapping[str, Any], policy: TrustPolicy) -> dict[str, Any]:
        evidence = list(envelope["evidence_items"])
        selected: list[dict[str, Any]] = []
        unknown: list[dict[str, Any]] = []
        conflicts: list[dict[str, Any]] = []
        rejected: list[dict[str, Any]] = []

        for req in envelope["requested_facts"]:
            supporters = [item for item in evidence if self._support_exact(item, req)]
            admissible: list[dict[str, Any]] = []
            reasons: list[dict[str, Any]] = []
            for item in supporters:
                ok, reason = self._admissible(item, req, policy)
                if ok:
                    admissible.append(item)
                else:
                    reasons.append({"evidence_id": item.get("evidence_id"), "reason": reason})
            competing_values = {
                canonical_json(item.get("semantic_value"))
                for item in evidence
                if item.get("semantic_fact_class") == req.get("semantic_fact_class")
                and item.get("exact_scope") == req.get("exact_scope")
                and item.get("verified_state") == "VERIFIED"
                and item.get("currentness_state") == "CURRENT"
                and item.get("conflict_state") == "NONE"
                and policy.allows(item, req)
            }
            if len(competing_values) > 1:
                conflicts.append({
                    "fact_id": req["fact_id"],
                    "semantic_fact_class": req["semantic_fact_class"],
                    "exact_scope": req["exact_scope"],
                    "evidence_ids": sorted(item["evidence_id"] for item in evidence if item.get("semantic_fact_class") == req.get("semantic_fact_class") and item.get("exact_scope") == req.get("exact_scope")),
                })
                continue
            if admissible:
                item = sorted(admissible, key=lambda x: x["evidence_id"])[0]
                selected.append({
                    "fact_id": req["fact_id"],
                    "semantic_fact_class": req["semantic_fact_class"],
                    "semantic_value": copy.deepcopy(req["semantic_value"]),
                    "exact_scope": req["exact_scope"],
                    "evidence_id": item["evidence_id"],
                    "trust_basis_ref": item["trust_basis_ref"],
                    "provenance_chain": copy.deepcopy(item["provenance_chain"]),
                    "exact_immutable_locator": item["exact_immutable_locator"],
                    "exact_version_or_blob": item["exact_version_or_blob"],
                })
            else:
                unknown.append({
                    "fact_id": req["fact_id"],
                    "semantic_fact_class": req["semantic_fact_class"],
                    "exact_scope": req["exact_scope"],
                    "state": "ABSENT" if not supporters else "UNKNOWN",
                    "reasons": reasons,
                })
                rejected.extend({"fact_id": req["fact_id"], **r} for r in reasons)

        verdict = "RESOLVED"
        if conflicts:
            verdict = "CONFLICT"
        elif unknown:
            verdict = "PARTIAL_UNKNOWN"
        resolution = {
            "resolution_id": None,
            "input_evidence_ids": sorted(item["evidence_id"] for item in evidence),
            "selected_fact_bindings": selected,
            "unknown_fact_bindings": unknown,
            "conflict_sets": conflicts,
            "rejected_inference_attempts": rejected,
            "resolution_verdict": verdict,
            "provenance_digest": digest(RESOLUTION_DOMAIN, [
                {"evidence_id": item["evidence_id"], "trust_basis_ref": item.get("trust_basis_ref"), "provenance_chain": item.get("provenance_chain", [])}
                for item in sorted(evidence, key=lambda x: x["evidence_id"])
            ]),
            "trust_policy_ref": policy.policy_ref,
        }
        resolution["resolution_id"] = identity(RESOLUTION_DOMAIN, resolution, "resolution_id")
        return resolution


def normalize_actor_binding(binding: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "actor_instance_ref", "actor_role", "actor_execution_mode", "current_writer_ref",
        "current_writer_state", "writer_requirement", "authoritative_state_mutation_required",
        "effect_mutation_class", "worker_effect_authority_ref", "writer_authority_ref",
        "recovery_state_ref", "freeze_state", "handoff_state", "replacement_state",
        "recovery_evidence_refs", "binding_provenance",
    }
    missing = required - set(binding)
    if missing:
        raise RuntimeBoundaryError(f"actor_binding_missing:{sorted(missing)}")
    out = copy.deepcopy(dict(binding))
    out["binding_id"] = identity(ACTOR_BINDING_DOMAIN, out, "binding_id")
    return out


def actor_effect_eligibility(binding: Mapping[str, Any], effect_class: str) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    mode = binding["actor_execution_mode"]
    writer_req = binding["writer_requirement"]
    authoritative = binding["authoritative_state_mutation_required"]
    if writer_req == "UNKNOWN" or authoritative == "UNKNOWN":
        reasons.append("UNKNOWN_WRITER_OR_MUTATION_REQUIREMENT")
    if binding["freeze_state"] != "CLEAR" or binding["handoff_state"] not in ("NONE",) or binding["replacement_state"] not in ("NONE",):
        reasons.append("RECOVERY_FREEZE_HANDOFF_REPLACEMENT_NOT_CLEAR")
    if mode == "CURRENT_WRITER":
        if binding["current_writer_state"] != "CURRENT" or not binding["current_writer_ref"]:
            reasons.append("CURRENT_WRITER_EVIDENCE_MISSING")
        if writer_req == "REQUIRED" and not binding["writer_authority_ref"]:
            reasons.append("WRITER_AUTHORITY_MISSING")
    elif mode == "WORKER_READ_ONLY":
        if writer_req == "REQUIRED":
            reasons.append("WORKER_CANNOT_SATISFY_WRITER_REQUIRED")
        if effect_class == "AUTHORITATIVE_CURRENT_STATE_WRITE":
            reasons.append("WORKER_CANNOT_AUTHORITATIVE_STATE_WRITE")
        if effect_class != "READ_ONLY_ANALYSIS" and not binding["worker_effect_authority_ref"]:
            reasons.append("WORKER_EFFECT_AUTHORITY_MISSING")
    else:
        reasons.append("ACTOR_EXECUTION_MODE_NOT_ELIGIBLE")
    return not reasons, reasons


class CoreCompiler(Protocol):
    def compile(self, envelope: Mapping[str, Any], resolution: Mapping[str, Any], actor_binding: Mapping[str, Any]) -> Mapping[str, Any]: ...


class ContractCompilerFacade:
    """Binds runtime evidence + actor identity to one deterministic core contract."""

    def __init__(self, compiler: CoreCompiler):
        self.compiler = compiler

    def compile(self, envelope: Mapping[str, Any], resolution: Mapping[str, Any], actor_binding: Mapping[str, Any]) -> dict[str, Any]:
        if resolution["resolution_verdict"] in ("CONFLICT", "INVALID"):
            raise RuntimeBoundaryError("runtime_resolution_not_compilable")
        compiled = copy.deepcopy(dict(self.compiler.compile(envelope, resolution, actor_binding)))
        for key in ("effective_context_id", "effective_context_version", "contract_id", "aggregation"):
            if key not in compiled:
                raise RuntimeBoundaryError(f"core_compile_missing:{key}")
        compiled["runtime_evidence_resolution_id"] = resolution["resolution_id"]
        compiled["actor_execution_binding"] = copy.deepcopy(dict(actor_binding))
        compiled["actor_execution_binding_id"] = actor_binding["binding_id"]
        return compiled


class ReviewedSeceCoreAdapter:
    """Lazy adapter to the reviewed SECE core shipped beside this module.

    The adapter only invokes deterministic semantic components. RuntimeInputAdapter and
    RuntimeEvidenceResolver remain the authority/provenance boundary.
    """

    def __init__(self, core_module: Any):
        self.core = core_module

    def _fact_from_binding(self, binding: Mapping[str, Any]) -> dict[str, Any] | None:
        value = binding["semantic_value"]
        if isinstance(value, Mapping) and {"fact_id", "fact_type", "scope", "state", "value_ref", "provenance_ref"}.issubset(value):
            return copy.deepcopy(dict(value))
        return None

    def compile(self, envelope: Mapping[str, Any], resolution: Mapping[str, Any], actor_binding: Mapping[str, Any]) -> Mapping[str, Any]:
        core = self.core
        facts = [f for f in (self._fact_from_binding(b) for b in resolution["selected_fact_bindings"]) if f]
        raw = {
            "facts": facts,
            "current_state_evidence": [],
            "causal_events": copy.deepcopy(list(envelope.get("causal_events", []))),
            "action_intent": copy.deepcopy(dict(envelope["proposed_action"])),
            "triggering_event_or_result": None,
            "dependency_changes": [],
            "binding_derivation_input": None,
            "transformation": None,
            "base_fixture_ref": None,
            "validator_predicates": [],
            "next_gate_rules": [],
        }
        atoms = core.SemanticAtomLoader().load(raw)
        composed = core.ContextComposer().compose(atoms)
        collisions = core.CollisionDetector().detect(composed)
        corrected = core.ContextCorrectionEngine().correct(composed, collisions)
        binding_sets = core.DependencyScopeResolver().derive(None, corrected["context"])
        ec = core.EffectiveContextBuilder().build(corrected, binding_sets, "RUNTIME_INTEGRATION_R01")
        ec = copy.deepcopy(ec)
        ec["runtime_evidence_resolution_id"] = resolution["resolution_id"]
        ec["actor_execution_binding"] = copy.deepcopy(dict(actor_binding))
        ec["context_id"] = core.digest(core.CONTEXT_DOMAIN, {k: v for k, v in ec.items() if k != "context_id"})
        projection = core.ExecutionContractProjector().project(ec, raw["action_intent"])
        contract = copy.deepcopy(projection.contract)
        contract["RUNTIME_EVIDENCE_RESOLUTION_REF"] = resolution["resolution_id"]
        contract["ACTOR_EXECUTION_BINDING"] = copy.deepcopy(dict(actor_binding))
        contract["contract_id"] = core.contract_id(contract)
        predicates: set[str] = set()
        if projection.valid:
            predicates |= core.ActionAuthorizationValidator().evaluate(contract)
            predicates |= core.CausalEventValidator().evaluate(contract)
            current, _ = core.CurrentStateEvidenceResolver().evaluate(contract)
            predicates |= current
            predicates = core.StaticValidator().evaluate(corrected["context"], collisions, predicates)
        aggregation = core.MultiOutcomeAggregator().aggregate(predicates, corrected["context"]) if projection.valid else {
            "aggregation_rule_id": "RUNTIME-PROJECTION-INVALID",
            "effect_decision": "NO_EFFECT",
            "primary_outcome": "AGGREGATE_BLOCKED",
            "terminal_class": "BLOCKED",
            "next_gate_class": "STOP",
            "secondary_reasons_preserve_all_input_predicates": True,
            "secondary_reasons": [{"predicate_id": e} for e in projection.errors],
        }
        return {
            "effective_context_id": ec["context_id"],
            "effective_context_version": ec["context_version"],
            "contract_id": contract["contract_id"],
            "contract": contract,
            "projection_valid": projection.valid,
            "projection_errors": list(projection.errors),
            "predicates": sorted(predicates),
            "aggregation": aggregation,
        }


class EffectIntentEmitter:
    def emit(self, envelope: Mapping[str, Any], resolution: Mapping[str, Any], compiled: Mapping[str, Any], actor_binding: Mapping[str, Any], *, adapter_class: str, required_outcome_evidence_mode: str) -> dict[str, Any] | None:
        if resolution["resolution_verdict"] != "RESOLVED":
            return None
        agg = compiled["aggregation"]
        if not compiled.get("projection_valid", True) or agg.get("effect_decision") != "ADMIT":
            return None
        action = envelope["proposed_action"]
        by_class: dict[str, list[str]] = {}
        for binding in resolution["selected_fact_bindings"]:
            by_class.setdefault(binding["semantic_fact_class"], []).append(binding["evidence_id"])
        contract = compiled.get("contract", {})
        intent = {
            "intent_id": None,
            "intent_state": "PRE_EFFECT_INTENT",
            "contract_id": compiled["contract_id"],
            "effective_context_id": compiled["effective_context_id"],
            "effective_context_version": compiled["effective_context_version"],
            "action_id": action["action_id"],
            "action_class": action["action_class"],
            "selected_scope": action["selected_scope"],
            "action_target_identity": action.get("target_ref"),
            "action_parameters": copy.deepcopy(action.get("parameters", {})),
            "runtime_evidence_resolution_id": resolution["resolution_id"],
            "required_evidence_ids": sorted(resolution["input_evidence_ids"]),
            "authority_evidence_refs": sorted(by_class.get("AUTHORITY", [])),
            "task_evidence_refs": sorted(by_class.get("TASK_CURRENTNESS", [])),
            "writer_evidence_refs": sorted(by_class.get("WRITER", [])),
            "recovery_evidence_refs": sorted(set(by_class.get("RECOVERY_STATE", []) + list(actor_binding.get("recovery_evidence_refs", [])))),
            "current_state_evidence_refs": sorted(by_class.get("CURRENT_STATE", [])),
            "input_version_refs": sorted((str(x.get("input_id")), str(x.get("version"))) for x in envelope.get("immutable_inputs", [])),
            "source_provenance_refs": sorted(str(x) for x in envelope.get("active_source_refs", [])),
            "required_preconditions": copy.deepcopy(contract.get("REQUIRED_PRECONDITIONS", [])),
            "stop_if": copy.deepcopy(contract.get("STOP_IF", [])),
            "validation_state": copy.deepcopy(contract.get("VALIDATION_STATE", {})),
            "aggregation": copy.deepcopy(compiled["aggregation"]),
            "actor_execution_binding_id": actor_binding["binding_id"],
            "actor_execution_binding": copy.deepcopy(dict(actor_binding)),
            "effect_adapter_class": adapter_class,
            "required_outcome_evidence_mode": required_outcome_evidence_mode,
        }
        intent["intent_payload_digest"] = digest(INTENT_DOMAIN, {
            "action_id": intent["action_id"], "action_class": intent["action_class"],
            "scope": intent["selected_scope"], "target": intent["action_target_identity"],
            "parameters": intent["action_parameters"],
        })
        intent["intent_id"] = identity(INTENT_DOMAIN, intent, "intent_id")
        return intent


class PreEffectRevalidator:
    def revalidate(
        self,
        intent: Mapping[str, Any],
        compiled: Mapping[str, Any],
        actor_binding: Mapping[str, Any],
        *,
        current_evidence_versions: Mapping[str, str],
        expected_evidence_versions: Mapping[str, str],
        adapter_class: str,
        adapter_authority: Mapping[str, Any] | None,
        prior_effect_state: str,
    ) -> dict[str, Any]:
        reasons: list[str] = []
        if intent["contract_id"] != compiled["contract_id"]:
            reasons.append("CONTRACT_ID_MISMATCH")
        if intent["effective_context_id"] != compiled["effective_context_id"] or intent["effective_context_version"] != compiled["effective_context_version"]:
            reasons.append("EFFECTIVE_CONTEXT_MISMATCH")
        if intent["actor_execution_binding_id"] != actor_binding["binding_id"]:
            reasons.append("ACTOR_BINDING_CHANGED")
        if intent["effect_adapter_class"] != adapter_class:
            reasons.append("ADAPTER_CLASS_MISMATCH")
        if prior_effect_state == "UNRESOLVED":
            reasons.append("UNRESOLVED_PRIOR_EFFECT")
        for ref, expected in expected_evidence_versions.items():
            if current_evidence_versions.get(ref) != expected:
                reasons.append("EVIDENCE_FRONTIER_CHANGED:" + ref)
        if not adapter_authority:
            reasons.append("ADAPTER_AUTHORITY_MISSING")
        else:
            if adapter_authority.get("state") != "CURRENT":
                reasons.append("ADAPTER_AUTHORITY_NOT_CURRENT")
            if adapter_authority.get("adapter_class") != adapter_class:
                reasons.append("ADAPTER_AUTHORITY_CLASS_MISMATCH")
            if intent["action_class"] not in set(adapter_authority.get("action_classes", [])):
                reasons.append("ADAPTER_AUTHORITY_ACTION_CLASS_MISMATCH")
            if intent["selected_scope"] not in set(adapter_authority.get("scopes", [])):
                reasons.append("ADAPTER_AUTHORITY_SCOPE_MISMATCH")
        eligible, actor_reasons = actor_effect_eligibility(actor_binding, actor_binding["effect_mutation_class"])
        if not eligible:
            reasons.extend(actor_reasons)

        verdict = "ADMIT_EFFECT_NOW" if not reasons else "NO_EFFECT_BLOCKED"
        if any("UNKNOWN" in r for r in reasons):
            verdict = "NO_EFFECT_UNKNOWN"
        admission = {
            "admission_id": None,
            "intent_id": intent["intent_id"],
            "contract_id": intent["contract_id"],
            "effective_context_id": intent["effective_context_id"],
            "effective_context_version": intent["effective_context_version"],
            "action_id": intent["action_id"],
            "action_class": intent["action_class"],
            "selected_scope": intent["selected_scope"],
            "action_target_identity": intent["action_target_identity"],
            "intent_payload_digest": intent["intent_payload_digest"],
            "authority_evidence_refs": copy.deepcopy(intent["authority_evidence_refs"]),
            "task_evidence_refs": copy.deepcopy(intent["task_evidence_refs"]),
            "writer_worker_evidence_refs": copy.deepcopy(intent["writer_evidence_refs"]),
            "recovery_freeze_handoff_evidence_refs": copy.deepcopy(intent["recovery_evidence_refs"]),
            "input_version_refs": copy.deepcopy(intent["input_version_refs"]),
            "current_state_evidence_refs": copy.deepcopy(sorted(current_evidence_versions.items())),
            "source_provenance_refs": copy.deepcopy(intent["source_provenance_refs"]),
            "actor_execution_binding_id": actor_binding["binding_id"],
            "prior_effect_state_refs": [prior_effect_state],
            "adapter_class": adapter_class,
            "adapter_authority_ref": None if not adapter_authority else adapter_authority.get("authority_ref"),
            "adapter_effect_class_scope": None if not adapter_authority else {
                "action_classes": sorted(adapter_authority.get("action_classes", [])),
                "scopes": sorted(adapter_authority.get("scopes", [])),
            },
            "expected_current_evidence_versions": copy.deepcopy(sorted(expected_evidence_versions.items())),
            "revalidation_verdict": verdict,
            "revalidation_reason_ids": sorted(set(reasons)),
            "admission_basis_digest": digest(ADMISSION_DOMAIN, {
                "intent_id": intent["intent_id"],
                "frontier": sorted(current_evidence_versions.items()),
                "adapter_authority": adapter_authority,
                "actor_binding_id": actor_binding["binding_id"],
            }),
            "predecessor_current_evidence_identities": copy.deepcopy(sorted(current_evidence_versions.items())),
            "provenance": ["OFFLINE_RUNTIME_INTEGRATION_R01"],
        }
        admission["admission_id"] = identity(ADMISSION_DOMAIN, admission, "admission_id")
        return admission


class EffectAdapter(Protocol):
    def execute(self, intent: Mapping[str, Any], admission: Mapping[str, Any]) -> Mapping[str, Any]: ...


class NonLiveEffectAdapter:
    """Default implementation boundary: never performs a world-facing effect."""

    adapter_class = "NON_LIVE_EFFECT_ADAPTER"

    def execute(self, intent: Mapping[str, Any], admission: Mapping[str, Any]) -> Mapping[str, Any]:
        if admission.get("intent_id") != intent.get("intent_id"):
            return {"adapter_status": "NOT_EXECUTED", "reason": "INTENT_ADMISSION_MISMATCH", "effect_attempted": False}
        if admission.get("revalidation_verdict") != "ADMIT_EFFECT_NOW":
            return {"adapter_status": "NOT_EXECUTED", "reason": admission.get("revalidation_verdict"), "effect_attempted": False}
        if admission.get("adapter_class") != intent.get("effect_adapter_class"):
            return {"adapter_status": "NOT_EXECUTED", "reason": "ADAPTER_CLASS_MISMATCH", "effect_attempted": False}
        return {"adapter_status": "NOT_EXECUTED", "reason": "NON_LIVE_BOUNDARY", "effect_attempted": False}


class MockEffectAdapter:
    """Test-only adapter. It returns the caller-provided synthetic observation, never I/O."""

    def __init__(self, adapter_class: str, observation: Mapping[str, Any]):
        self.adapter_class = adapter_class
        self.observation = copy.deepcopy(dict(observation))

    def execute(self, intent: Mapping[str, Any], admission: Mapping[str, Any]) -> Mapping[str, Any]:
        if admission.get("intent_id") != intent.get("intent_id") or admission.get("revalidation_verdict") != "ADMIT_EFFECT_NOW":
            return {"adapter_status": "NOT_EXECUTED", "reason": "FAIL_CLOSED", "effect_attempted": False}
        if admission.get("adapter_class") != self.adapter_class or intent.get("effect_adapter_class") != self.adapter_class:
            return {"adapter_status": "NOT_EXECUTED", "reason": "ADAPTER_CLASS_MISMATCH", "effect_attempted": False}
        return {
            "adapter_status": "MOCK_OBSERVATION_AVAILABLE",
            "effect_attempted": False,
            "mock_observation": copy.deepcopy(self.observation),
        }


class EffectOutcomeRecorder:
    def record(self, intent: Mapping[str, Any], admission: Mapping[str, Any], adapter_result: Mapping[str, Any], *, outcome_evidence: list[Mapping[str, Any]], policy: TrustPolicy) -> dict[str, Any]:
        status = "NOT_EXECUTED"
        evidence_refs: list[str] = []
        if adapter_result.get("adapter_status") == "MOCK_OBSERVATION_AVAILABLE":
            obs = adapter_result.get("mock_observation", {})
            desired = obs.get("outcome")
            req = {
                "fact_id": "OUTCOME-" + intent["intent_id"][:16],
                "semantic_fact_class": "OUTCOME",
                "semantic_value": desired,
                "exact_scope": intent["selected_scope"],
                "required_currentness": "CURRENT",
            }
            envelope = {
                "evidence_items": copy.deepcopy(outcome_evidence),
                "requested_facts": [req],
            }
            resolution = RuntimeEvidenceResolver().resolve(envelope, policy)
            if resolution["resolution_verdict"] == "RESOLVED" and resolution["selected_fact_bindings"]:
                status = "EVIDENCED_SUCCESS" if desired == "SUCCESS" else "EVIDENCED_FAILURE"
                evidence_refs = [resolution["selected_fact_bindings"][0]["evidence_id"]]
            else:
                status = "UNRESOLVED"
        record = {
            "outcome_id": None,
            "intent_id": intent["intent_id"],
            "admission_id": admission["admission_id"],
            "outcome_state": status,
            "effect_attempted": bool(adapter_result.get("effect_attempted", False)),
            "evidence_refs": evidence_refs,
            "adapter_status": adapter_result.get("adapter_status"),
            "adapter_reason": adapter_result.get("reason"),
        }
        record["outcome_id"] = identity(OUTCOME_DOMAIN, record, "outcome_id")
        return record


class RuntimeResultFixator:
    def fix(self, envelope: Mapping[str, Any], resolution: Mapping[str, Any], compiled: Mapping[str, Any], intent: Mapping[str, Any] | None, admission: Mapping[str, Any] | None, outcome: Mapping[str, Any] | None, *, next_gate_candidate: Mapping[str, Any] | None = None) -> dict[str, Any]:
        result = {
            "result_id": None,
            "envelope_id": envelope["envelope_id"],
            "resolution_id": resolution["resolution_id"],
            "contract_id": compiled["contract_id"],
            "effect_decision": compiled["aggregation"].get("effect_decision"),
            "intent_id": None if intent is None else intent["intent_id"],
            "admission_id": None if admission is None else admission["admission_id"],
            "outcome_id": None if outcome is None else outcome["outcome_id"],
            "outcome_state": "NOT_EXECUTED" if outcome is None else outcome["outcome_state"],
            "unknown_fact_ids": sorted(x["fact_id"] for x in resolution["unknown_fact_bindings"]),
            "conflict_fact_ids": sorted(x["fact_id"] for x in resolution["conflict_sets"]),
            "next_gate_candidate": copy.deepcopy(next_gate_candidate),
            "candidate_requires_external_task_authority": next_gate_candidate is not None,
        }
        result["result_id"] = identity(RESULT_DOMAIN, result, "result_id")
        return result


class RuntimeHumanExplanationAdapter:
    """Pure projection of machine result. No new status inference."""

    def render(self, result: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "checked_contract": result["contract_id"],
            "effect_decision": result["effect_decision"],
            "effect_outcome": result["outcome_state"],
            "unknown_fact_ids": copy.deepcopy(result["unknown_fact_ids"]),
            "conflict_fact_ids": copy.deepcopy(result["conflict_fact_ids"]),
            "next_gate_candidate": copy.deepcopy(result["next_gate_candidate"]),
            "next_gate_requires_external_authority": bool(result["candidate_requires_external_task_authority"]),
        }
