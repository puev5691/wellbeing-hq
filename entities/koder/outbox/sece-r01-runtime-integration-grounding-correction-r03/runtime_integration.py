from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Protocol

RUNTIME_DOMAIN = "sece-runtime-integration-r01\0"
RESOLUTION_DOMAIN = "sece-runtime-evidence-resolution-r01\0"
ACTOR_BINDING_DOMAIN = "sece-actor-execution-binding-r01\0"
ACTOR_EVIDENCE_DOMAIN = "sece-actor-execution-binding-evidence-r03\0"
INTENT_DOMAIN = "sece-effect-intent-r01\0"
ADMISSION_DOMAIN = "sece-pre-effect-admission-r01\0"
POLICY_BINDING_DOMAIN = "sece-trust-policy-binding-r02\0"
INVOCATION_BOUNDARY_DOMAIN = "sece-effect-invocation-boundary-r02\0"
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
            "actor_execution_binding_claim": copy.deepcopy(dict(raw["actor_execution_binding"])),
            "actor_execution_binding": None,
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
    """Policy configuration bound to exact authoritative policy/rule evidence."""

    policy_ref: str
    allowed_source_classes: Mapping[str, tuple[str, ...]]
    required_trust_basis_prefixes: tuple[str, ...]
    policy_evidence_id: str
    policy_evidence_locator: str
    policy_evidence_version: str
    policy_authority_source: str
    governed_scopes: tuple[str, ...]
    governed_fact_classes: tuple[str, ...]
    policy_provenance: tuple[str, ...]
    policy_payload_digest: str
    policy_verified_state: str
    policy_currentness_state: str
    policy_conflict_state: str
    binding_id: str

    def config_payload(self) -> dict[str, Any]:
        return {
            "policy_ref": self.policy_ref,
            "allowed_source_classes": {k: sorted(v) for k, v in sorted(self.allowed_source_classes.items())},
            "required_trust_basis_prefixes": sorted(self.required_trust_basis_prefixes),
            "governed_scopes": sorted(self.governed_scopes),
            "governed_fact_classes": sorted(self.governed_fact_classes),
        }

    def binding_valid(self) -> bool:
        if not self.policy_evidence_id or not self.policy_evidence_locator or not self.policy_evidence_version:
            return False
        if not self.policy_authority_source or not self.policy_provenance:
            return False
        if self.policy_verified_state != "VERIFIED" or self.policy_currentness_state != "CURRENT" or self.policy_conflict_state != "NONE":
            return False
        if self.policy_payload_digest != digest(POLICY_BINDING_DOMAIN, self.config_payload()):
            return False
        expected_binding = digest(POLICY_BINDING_DOMAIN, {
            "policy_payload_digest": self.policy_payload_digest,
            "policy_evidence_id": self.policy_evidence_id,
            "policy_evidence_locator": self.policy_evidence_locator,
            "policy_evidence_version": self.policy_evidence_version,
            "policy_authority_source": self.policy_authority_source,
            "policy_verified_state": self.policy_verified_state,
            "policy_currentness_state": self.policy_currentness_state,
            "policy_conflict_state": self.policy_conflict_state,
            "policy_provenance": list(self.policy_provenance),
        })
        return self.binding_id == expected_binding

    def allows(self, item: Mapping[str, Any], requested_fact: Mapping[str, Any]) -> bool:
        if not self.binding_valid():
            return False
        fact_class = str(requested_fact["semantic_fact_class"])
        scope = str(requested_fact["exact_scope"])
        if fact_class not in set(self.governed_fact_classes):
            return False
        if "*" not in set(self.governed_scopes) and scope not in set(self.governed_scopes):
            return False
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


class TrustPolicyBindingResolver:
    """Binds policy configuration to exact verified/current authoritative rule evidence."""

    AUTHORITATIVE_POLICY_SOURCE_CLASSES = {"ACTIVE_PROJECT_SOURCE", "OPERATOR_DECISION"}
    REQUIRED_POLICY_EVIDENCE_FIELDS = {
        "evidence_id", "exact_immutable_locator", "exact_version_or_blob", "source_class",
        "verified_state", "currentness_state", "conflict_state", "provenance_chain",
        "semantic_fact_class", "semantic_value",
    }

    def bind(
        self,
        *,
        policy_ref: str,
        allowed_source_classes: Mapping[str, tuple[str, ...]],
        required_trust_basis_prefixes: tuple[str, ...],
        governed_scopes: tuple[str, ...],
        policy_evidence: Mapping[str, Any],
    ) -> TrustPolicy:
        missing = self.REQUIRED_POLICY_EVIDENCE_FIELDS - set(policy_evidence)
        if missing:
            raise RuntimeBoundaryError(f"trust_policy_evidence_missing:{sorted(missing)}")
        if policy_evidence["source_class"] not in self.AUTHORITATIVE_POLICY_SOURCE_CLASSES:
            raise RuntimeBoundaryError("trust_policy_authority_source_invalid")
        if policy_evidence["verified_state"] != "VERIFIED" or policy_evidence["currentness_state"] != "CURRENT":
            raise RuntimeBoundaryError("trust_policy_evidence_not_verified_current")
        if policy_evidence["conflict_state"] != "NONE":
            raise RuntimeBoundaryError("trust_policy_evidence_conflict")
        if not policy_evidence["exact_immutable_locator"] or not policy_evidence["exact_version_or_blob"]:
            raise RuntimeBoundaryError("trust_policy_evidence_identity_missing")
        if not policy_evidence["provenance_chain"]:
            raise RuntimeBoundaryError("trust_policy_provenance_missing")
        if policy_evidence["semantic_fact_class"] != "TRUST_POLICY_RULE":
            raise RuntimeBoundaryError("trust_policy_wrong_fact_class")

        config_payload = {
            "policy_ref": policy_ref,
            "allowed_source_classes": {k: sorted(v) for k, v in sorted(allowed_source_classes.items())},
            "required_trust_basis_prefixes": sorted(required_trust_basis_prefixes),
            "governed_scopes": sorted(governed_scopes),
            "governed_fact_classes": sorted(allowed_source_classes),
        }
        payload_digest = digest(POLICY_BINDING_DOMAIN, config_payload)
        semantic_value = policy_evidence["semantic_value"]
        if not isinstance(semantic_value, Mapping):
            raise RuntimeBoundaryError("trust_policy_semantic_value_invalid")
        if semantic_value.get("policy_ref") != policy_ref:
            raise RuntimeBoundaryError("trust_policy_ref_mismatch")
        if semantic_value.get("policy_payload_digest") != payload_digest:
            raise RuntimeBoundaryError("trust_policy_payload_mismatch")

        binding_id = digest(POLICY_BINDING_DOMAIN, {
            "policy_payload_digest": payload_digest,
            "policy_evidence_id": policy_evidence["evidence_id"],
            "policy_evidence_locator": policy_evidence["exact_immutable_locator"],
            "policy_evidence_version": policy_evidence["exact_version_or_blob"],
            "policy_authority_source": policy_evidence["source_class"],
            "policy_verified_state": policy_evidence["verified_state"],
            "policy_currentness_state": policy_evidence["currentness_state"],
            "policy_conflict_state": policy_evidence["conflict_state"],
            "policy_provenance": list(policy_evidence["provenance_chain"]),
        })
        return TrustPolicy(
            policy_ref=policy_ref,
            allowed_source_classes={k: tuple(v) for k, v in allowed_source_classes.items()},
            required_trust_basis_prefixes=tuple(required_trust_basis_prefixes),
            policy_evidence_id=str(policy_evidence["evidence_id"]),
            policy_evidence_locator=str(policy_evidence["exact_immutable_locator"]),
            policy_evidence_version=str(policy_evidence["exact_version_or_blob"]),
            policy_authority_source=str(policy_evidence["source_class"]),
            governed_scopes=tuple(governed_scopes),
            governed_fact_classes=tuple(sorted(allowed_source_classes)),
            policy_provenance=tuple(str(x) for x in policy_evidence["provenance_chain"]),
            policy_payload_digest=payload_digest,
            policy_verified_state=str(policy_evidence["verified_state"]),
            policy_currentness_state=str(policy_evidence["currentness_state"]),
            policy_conflict_state=str(policy_evidence["conflict_state"]),
            binding_id=binding_id,
        )


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
        if not policy.binding_valid():
            raise RuntimeBoundaryError("trust_policy_not_authoritatively_bound")
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
            "trust_policy_binding_id": policy.binding_id,
            "trust_policy_evidence_id": policy.policy_evidence_id,
            "trust_policy_dependency": {
                "evidence_id": policy.policy_evidence_id,
                "exact_immutable_locator": policy.policy_evidence_locator,
                "exact_version_or_blob": policy.policy_evidence_version,
                "binding_id": policy.binding_id,
                "verified_state": policy.policy_verified_state,
                "currentness_state": policy.policy_currentness_state,
                "conflict_state": policy.policy_conflict_state,
                "authority_source": policy.policy_authority_source,
                "provenance": list(policy.policy_provenance),
            },
        }
        actor_claim = envelope.get("actor_execution_binding_claim")
        actor_binding = None
        actor_refs: list[str] = []
        if actor_claim is not None:
            actor_binding = ActorExecutionBindingResolver().resolve(actor_claim, evidence)
            resolution["actor_execution_binding"] = actor_binding
            resolution["actor_execution_binding_id"] = actor_binding["binding_id"]
            resolution["actor_binding_evidence_versions"] = copy.deepcopy(actor_binding["supporting_evidence_versions"])
            resolution["actor_binding_evidence_refs"] = copy.deepcopy(actor_binding["supporting_evidence_refs"])
            actor_refs = list(actor_binding["supporting_evidence_refs"])
            if actor_binding["grounding_state"] == "CONFLICT":
                resolution["resolution_verdict"] = "CONFLICT"
            elif actor_binding["grounding_state"] != "RESOLVED" and resolution["resolution_verdict"] == "RESOLVED":
                resolution["resolution_verdict"] = "PARTIAL_UNKNOWN"
        resolution["input_evidence_ids"] = sorted(set(
            resolution["input_evidence_ids"]
            + [policy.policy_evidence_id]
            + actor_refs
        ))
        resolution["resolution_id"] = identity(RESOLUTION_DOMAIN, resolution, "resolution_id")
        return resolution


def normalize_actor_binding(binding: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "actor_instance_ref", "actor_role", "actor_execution_mode", "current_writer_ref",
        "current_writer_state", "writer_requirement", "authoritative_state_mutation_required",
        "effect_mutation_class", "worker_effect_authority_ref", "writer_authority_ref",
        "recovery_state_ref", "freeze_state", "handoff_state", "replacement_state",
        "recovery_evidence_refs", "binding_provenance", "grounding_state",
        "supporting_evidence_refs", "supporting_evidence_versions", "supporting_evidence_locators",
        "grounding_unknown_fields", "grounding_conflict_fields",
    }
    missing = required - set(binding)
    if missing:
        raise RuntimeBoundaryError(f"actor_binding_missing:{sorted(missing)}")
    out = copy.deepcopy(dict(binding))
    out["binding_id"] = identity(ACTOR_BINDING_DOMAIN, out, "binding_id")
    return out


class ActorExecutionBindingResolver:
    """Derives ACTOR_EXECUTION_BINDING from exact verified/current evidence."""

    FIELD_FACT_CLASS = {
        "actor_instance_ref": "ACTOR_INSTANCE_REF",
        "actor_role": "ACTOR_ROLE",
        "actor_execution_mode": "ACTOR_EXECUTION_MODE",
        "current_writer_ref": "CURRENT_WRITER_REF",
        "current_writer_state": "CURRENT_WRITER_STATE",
        "writer_requirement": "WRITER_REQUIREMENT",
        "authoritative_state_mutation_required": "AUTHORITATIVE_STATE_MUTATION_REQUIRED",
        "effect_mutation_class": "EFFECT_MUTATION_CLASS",
        "worker_effect_authority_ref": "WORKER_EFFECT_AUTHORITY_REF",
        "writer_authority_ref": "WRITER_AUTHORITY_REF",
        "recovery_state_ref": "RECOVERY_STATE_REF",
        "freeze_state": "FREEZE_STATE",
        "handoff_state": "HANDOFF_STATE",
        "replacement_state": "REPLACEMENT_STATE",
    }

    ALLOWED_SOURCES = {
        "ACTOR_INSTANCE_REF": {"TASK_CONVEYOR", "OPERATOR_DECISION", "CURRENT_WRITER", "RECOVERY"},
        "ACTOR_ROLE": {"TASK_CONVEYOR", "OPERATOR_DECISION", "CURRENT_WRITER", "RECOVERY"},
        "ACTOR_EXECUTION_MODE": {"TASK_CONVEYOR", "OPERATOR_DECISION", "CURRENT_WRITER", "RECOVERY"},
        "CURRENT_WRITER_REF": {"CURRENT_WRITER", "RECOVERY"},
        "CURRENT_WRITER_STATE": {"CURRENT_WRITER", "RECOVERY"},
        "WRITER_REQUIREMENT": {"TASK_CONVEYOR", "OPERATOR_DECISION", "ACTIVE_PROJECT_SOURCE"},
        "AUTHORITATIVE_STATE_MUTATION_REQUIRED": {"TASK_CONVEYOR", "OPERATOR_DECISION", "ACTIVE_PROJECT_SOURCE"},
        "EFFECT_MUTATION_CLASS": {"TASK_CONVEYOR", "OPERATOR_DECISION", "ACTIVE_PROJECT_SOURCE"},
        "WORKER_EFFECT_AUTHORITY_REF": {"TASK_CONVEYOR", "OPERATOR_DECISION"},
        "WRITER_AUTHORITY_REF": {"CURRENT_WRITER", "OPERATOR_DECISION", "RECOVERY"},
        "RECOVERY_STATE_REF": {"RECOVERY"},
        "FREEZE_STATE": {"RECOVERY"},
        "HANDOFF_STATE": {"RECOVERY"},
        "REPLACEMENT_STATE": {"RECOVERY"},
    }

    REQUIRED_EVIDENCE_FIELDS = {
        "evidence_id", "exact_immutable_locator", "exact_version_or_blob", "exact_scope",
        "source_class", "verified_state", "currentness_state", "conflict_state",
        "semantic_fact_class", "semantic_value", "provenance_chain",
    }

    def resolve(self, claim: Mapping[str, Any], evidence_items: list[Mapping[str, Any]]) -> dict[str, Any]:
        missing_claim = set(self.FIELD_FACT_CLASS) - set(claim)
        if missing_claim:
            raise RuntimeBoundaryError(f"actor_binding_claim_missing:{sorted(missing_claim)}")
        actor_scope = str(claim["actor_instance_ref"])
        supporting_refs: list[str] = []
        supporting_versions: dict[str, str] = {}
        supporting_locators: dict[str, str] = {}
        provenance: list[str] = []
        unknown_fields: list[str] = []
        conflict_fields: list[str] = []

        for field, fact_class in self.FIELD_FACT_CLASS.items():
            expected_value = claim[field]
            applicable = [
                e for e in evidence_items
                if e.get("semantic_fact_class") == fact_class
                and e.get("exact_scope") == actor_scope
            ]
            trusted_current = [
                e for e in applicable
                if not (self.REQUIRED_EVIDENCE_FIELDS - set(e))
                and e.get("source_class") in self.ALLOWED_SOURCES[fact_class]
                and e.get("verified_state") == "VERIFIED"
                and e.get("currentness_state") == "CURRENT"
                and e.get("conflict_state") == "NONE"
                and e.get("exact_immutable_locator")
                and e.get("exact_version_or_blob")
                and e.get("provenance_chain")
            ]
            values = {canonical_json(e.get("semantic_value")) for e in trusted_current}
            if len(values) > 1:
                conflict_fields.append(field)
                continue
            exact = [e for e in trusted_current if e.get("semantic_value") == expected_value]
            if len(exact) != 1:
                unknown_fields.append(field)
                continue
            item = exact[0]
            supporting_refs.append(str(item["evidence_id"]))
            supporting_versions[str(item["evidence_id"])] = str(item["exact_version_or_blob"])
            supporting_locators[str(item["evidence_id"])] = str(item["exact_immutable_locator"])
            provenance.extend(str(x) for x in item["provenance_chain"])

        grounding_state = "RESOLVED"
        if conflict_fields:
            grounding_state = "CONFLICT"
        elif unknown_fields:
            grounding_state = "UNKNOWN"

        derived = copy.deepcopy(dict(claim))
        derived["recovery_evidence_refs"] = sorted(
            ref for ref in supporting_refs
            if any(
                e.get("evidence_id") == ref
                and e.get("semantic_fact_class") in {"RECOVERY_STATE_REF", "FREEZE_STATE", "HANDOFF_STATE", "REPLACEMENT_STATE"}
                for e in evidence_items
            )
        )
        derived["binding_provenance"] = sorted(set(provenance))
        derived["grounding_state"] = grounding_state
        derived["supporting_evidence_refs"] = sorted(set(supporting_refs))
        derived["supporting_evidence_versions"] = dict(sorted(supporting_versions.items()))
        derived["supporting_evidence_locators"] = dict(sorted(supporting_locators.items()))
        derived["grounding_unknown_fields"] = sorted(set(unknown_fields))
        derived["grounding_conflict_fields"] = sorted(set(conflict_fields))
        derived["grounding_digest"] = digest(ACTOR_EVIDENCE_DOMAIN, {
            "claim": {k: claim[k] for k in sorted(self.FIELD_FACT_CLASS)},
            "supporting_evidence_versions": derived["supporting_evidence_versions"],
            "supporting_evidence_locators": derived["supporting_evidence_locators"],
            "grounding_state": grounding_state,
        })
        return normalize_actor_binding(derived)


def actor_binding_consistency(binding: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    if binding.get("grounding_state") != "RESOLVED":
        reasons.append("ACTOR_BINDING_NOT_EVIDENCE_RESOLVED")
    writer_req = binding["writer_requirement"]
    authoritative = binding["authoritative_state_mutation_required"]
    effect_class = binding["effect_mutation_class"]

    if effect_class == "AUTHORITATIVE_CURRENT_STATE_WRITE":
        if authoritative != "YES":
            reasons.append("AUTHORITATIVE_WRITE_REQUIRES_MUTATION_REQUIRED_YES")
        if writer_req != "REQUIRED":
            reasons.append("AUTHORITATIVE_WRITE_REQUIRES_WRITER_REQUIRED")
    if authoritative == "YES" and writer_req != "REQUIRED":
        reasons.append("AUTHORITATIVE_MUTATION_REQUIRES_WRITER_REQUIRED")
    if effect_class in ("READ_ONLY_ANALYSIS", "CANDIDATE_ARTIFACT_WRITE") and authoritative == "YES":
        reasons.append("NON_AUTHORITATIVE_EFFECT_CONTRADICTS_AUTHORITATIVE_MUTATION")
    if writer_req == "NOT_REQUIRED_FOR_TASK" and authoritative == "YES":
        reasons.append("WRITER_NOT_REQUIRED_CONTRADICTS_AUTHORITATIVE_MUTATION")
    return sorted(set(reasons))


def actor_effect_eligibility(binding: Mapping[str, Any], effect_class: str) -> tuple[bool, list[str]]:
    reasons: list[str] = actor_binding_consistency(binding)
    mode = binding["actor_execution_mode"]
    writer_req = binding["writer_requirement"]
    authoritative = binding["authoritative_state_mutation_required"]
    if effect_class != binding["effect_mutation_class"]:
        reasons.append("EFFECT_CLASS_BINDING_MISMATCH")
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
    return not reasons, sorted(set(reasons))


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
        resolved_actor = resolution.get("actor_execution_binding")
        if not isinstance(resolved_actor, Mapping):
            raise RuntimeBoundaryError("resolution_actor_binding_missing")
        if actor_binding.get("binding_id") != resolved_actor.get("binding_id"):
            raise RuntimeBoundaryError("actor_binding_not_resolution_bound")
        compiled["runtime_evidence_resolution_id"] = resolution["resolution_id"]
        compiled["trust_policy_dependency"] = copy.deepcopy(resolution["trust_policy_dependency"])
        compiled["actor_execution_binding"] = copy.deepcopy(dict(resolved_actor))
        compiled["actor_execution_binding_id"] = resolved_actor["binding_id"]
        compiled["actor_binding_evidence_versions"] = copy.deepcopy(resolved_actor["supporting_evidence_versions"])
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
        ec["trust_policy_dependency"] = copy.deepcopy(resolution["trust_policy_dependency"])
        ec["actor_execution_binding"] = copy.deepcopy(dict(actor_binding))
        ec["actor_binding_evidence_versions"] = copy.deepcopy(actor_binding["supporting_evidence_versions"])
        ec["context_id"] = core.digest(core.CONTEXT_DOMAIN, {k: v for k, v in ec.items() if k != "context_id"})
        projection = core.ExecutionContractProjector().project(ec, raw["action_intent"])
        contract = copy.deepcopy(projection.contract)
        contract["RUNTIME_EVIDENCE_RESOLUTION_REF"] = resolution["resolution_id"]
        contract["TRUST_POLICY_DEPENDENCY"] = copy.deepcopy(resolution["trust_policy_dependency"])
        contract["ACTOR_EXECUTION_BINDING"] = copy.deepcopy(dict(actor_binding))
        contract["ACTOR_BINDING_EVIDENCE_VERSIONS"] = copy.deepcopy(actor_binding["supporting_evidence_versions"])
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
        resolved_actor = resolution.get("actor_execution_binding")
        if not isinstance(resolved_actor, Mapping) or actor_binding.get("binding_id") != resolved_actor.get("binding_id"):
            return None
        if actor_binding.get("grounding_state") != "RESOLVED":
            return None
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
            "trust_policy_dependency": copy.deepcopy(resolution["trust_policy_dependency"]),
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
            "actor_binding_evidence_refs": copy.deepcopy(actor_binding["supporting_evidence_refs"]),
            "actor_binding_evidence_versions": copy.deepcopy(actor_binding["supporting_evidence_versions"]),
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
        current_trust_policy_dependency: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        reasons: list[str] = []
        expected_payload_digest = digest(INTENT_DOMAIN, {
            "action_id": intent["action_id"], "action_class": intent["action_class"],
            "scope": intent["selected_scope"], "target": intent["action_target_identity"],
            "parameters": intent["action_parameters"],
        })
        if intent.get("intent_payload_digest") != expected_payload_digest:
            reasons.append("INTENT_PAYLOAD_DIGEST_MISMATCH")
        if intent.get("intent_id") != identity(INTENT_DOMAIN, intent, "intent_id"):
            reasons.append("INTENT_ID_MISMATCH")
        if intent["contract_id"] != compiled["contract_id"]:
            reasons.append("CONTRACT_ID_MISMATCH")
        if intent["effective_context_id"] != compiled["effective_context_id"] or intent["effective_context_version"] != compiled["effective_context_version"]:
            reasons.append("EFFECTIVE_CONTEXT_MISMATCH")
        if intent["actor_execution_binding_id"] != actor_binding["binding_id"]:
            reasons.append("ACTOR_BINDING_CHANGED")
        if intent["effect_adapter_class"] != adapter_class:
            reasons.append("ADAPTER_CLASS_MISMATCH")
        policy_dep = intent.get("trust_policy_dependency")
        if not isinstance(policy_dep, Mapping):
            reasons.append("TRUST_POLICY_DEPENDENCY_MISSING")
        else:
            current_policy = current_trust_policy_dependency or {}
            required_policy_fields = {
                "evidence_id", "exact_immutable_locator", "exact_version_or_blob", "binding_id",
                "verified_state", "currentness_state", "conflict_state",
            }
            if required_policy_fields - set(current_policy):
                reasons.append("CURRENT_TRUST_POLICY_DEPENDENCY_MISSING")
            else:
                if current_policy.get("verified_state") != "VERIFIED" or current_policy.get("currentness_state") != "CURRENT":
                    reasons.append("TRUST_POLICY_NOT_CURRENT")
                if current_policy.get("conflict_state") != "NONE":
                    reasons.append("TRUST_POLICY_CONFLICT")
                for key in ("evidence_id","exact_immutable_locator","exact_version_or_blob","binding_id"):
                    if current_policy.get(key) != policy_dep.get(key):
                        reasons.append("TRUST_POLICY_DEPENDENCY_CHANGED:" + key)
        if prior_effect_state == "UNRESOLVED":
            reasons.append("UNRESOLVED_PRIOR_EFFECT")
        required_versions = dict(expected_evidence_versions)
        policy_dep_for_frontier = intent.get("trust_policy_dependency") or {}
        if policy_dep_for_frontier.get("evidence_id") and policy_dep_for_frontier.get("exact_version_or_blob"):
            required_versions[str(policy_dep_for_frontier["evidence_id"])] = str(policy_dep_for_frontier["exact_version_or_blob"])
        required_versions.update({str(k):str(v) for k,v in intent.get("actor_binding_evidence_versions", {}).items()})
        for ref, expected in required_versions.items():
            if current_evidence_versions.get(ref) != expected:
                reasons.append("EVIDENCE_FRONTIER_CHANGED:" + ref)
        if not adapter_authority:
            reasons.append("ADAPTER_AUTHORITY_MISSING")
        else:
            required_adapter_authority = {
                "authority_ref", "state", "adapter_class", "action_classes", "scopes",
                "exact_immutable_locator", "exact_version_or_blob", "verified_state", "conflict_state",
            }
            if required_adapter_authority - set(adapter_authority):
                reasons.append("ADAPTER_AUTHORITY_MALFORMED")
            if adapter_authority.get("state") != "CURRENT" or adapter_authority.get("verified_state") != "VERIFIED":
                reasons.append("ADAPTER_AUTHORITY_NOT_CURRENT")
            if adapter_authority.get("conflict_state") != "NONE":
                reasons.append("ADAPTER_AUTHORITY_CONFLICT")
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
            "actor_binding_evidence_refs": copy.deepcopy(actor_binding["supporting_evidence_refs"]),
            "actor_binding_evidence_versions": copy.deepcopy(actor_binding["supporting_evidence_versions"]),
            "trust_policy_dependency": copy.deepcopy(intent.get("trust_policy_dependency")),
            "prior_effect_state_refs": [prior_effect_state],
            "adapter_class": adapter_class,
            "adapter_authority_ref": None if not adapter_authority else adapter_authority.get("authority_ref"),
            "adapter_authority_snapshot_digest": None if not adapter_authority else digest(INVOCATION_BOUNDARY_DOMAIN, adapter_authority),
            "adapter_authority_version": None if not adapter_authority else adapter_authority.get("exact_version_or_blob"),
            "adapter_effect_class_scope": None if not adapter_authority else {
                "action_classes": sorted(adapter_authority.get("action_classes", [])),
                "scopes": sorted(adapter_authority.get("scopes", [])),
            },
            "expected_current_evidence_versions": copy.deepcopy(sorted(required_versions.items())),
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


class EffectBoundaryVerifier:
    """Re-checks the exact current invocation frontier immediately at adapter boundary."""

    def verify(
        self,
        intent: Mapping[str, Any],
        admission: Mapping[str, Any],
        invocation_evidence: Mapping[str, Any],
        adapter_class: str,
    ) -> tuple[bool, list[str]]:
        reasons: list[str] = []

        expected_payload_digest = digest(INTENT_DOMAIN, {
            "action_id": intent.get("action_id"), "action_class": intent.get("action_class"),
            "scope": intent.get("selected_scope"), "target": intent.get("action_target_identity"),
            "parameters": intent.get("action_parameters"),
        })
        if intent.get("intent_payload_digest") != expected_payload_digest:
            reasons.append("INTENT_PAYLOAD_DIGEST_MISMATCH_AT_INVOCATION")
        if intent.get("intent_id") != identity(INTENT_DOMAIN, intent, "intent_id"):
            reasons.append("INTENT_ID_MISMATCH_AT_INVOCATION")
        if admission.get("admission_id") != identity(ADMISSION_DOMAIN, admission, "admission_id"):
            reasons.append("ADMISSION_ID_MISMATCH_AT_INVOCATION")
        if admission.get("intent_id") != intent.get("intent_id"):
            reasons.append("INTENT_ADMISSION_MISMATCH")
        if admission.get("revalidation_verdict") != "ADMIT_EFFECT_NOW":
            reasons.append("ADMISSION_NOT_ADMIT_EFFECT_NOW")
        if admission.get("adapter_class") != adapter_class or intent.get("effect_adapter_class") != adapter_class:
            reasons.append("ADAPTER_CLASS_MISMATCH")

        current_versions = dict(invocation_evidence.get("current_evidence_versions", {}))
        expected_versions = dict(admission.get("expected_current_evidence_versions", []))
        if current_versions != expected_versions:
            reasons.append("INVOCATION_EVIDENCE_FRONTIER_CHANGED")

        admission_policy = admission.get("trust_policy_dependency")
        current_policy = invocation_evidence.get("trust_policy_dependency")
        if not isinstance(admission_policy, Mapping) or not isinstance(current_policy, Mapping):
            reasons.append("INVOCATION_TRUST_POLICY_DEPENDENCY_MISSING")
        else:
            if current_policy.get("verified_state") != "VERIFIED" or current_policy.get("currentness_state") != "CURRENT":
                reasons.append("INVOCATION_TRUST_POLICY_NOT_CURRENT")
            if current_policy.get("conflict_state") != "NONE":
                reasons.append("INVOCATION_TRUST_POLICY_CONFLICT")
            for key in ("evidence_id","exact_immutable_locator","exact_version_or_blob","binding_id"):
                if current_policy.get(key) != admission_policy.get(key):
                    reasons.append("INVOCATION_TRUST_POLICY_CHANGED:" + key)

        current_authority = invocation_evidence.get("adapter_authority")
        if not isinstance(current_authority, Mapping):
            reasons.append("INVOCATION_ADAPTER_AUTHORITY_MISSING")
        else:
            if current_authority.get("state") != "CURRENT" or current_authority.get("verified_state") != "VERIFIED":
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_NOT_CURRENT")
            if current_authority.get("conflict_state") != "NONE":
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_CONFLICT")
            if current_authority.get("adapter_class") != adapter_class:
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_CLASS_MISMATCH")
            if intent.get("action_class") not in set(current_authority.get("action_classes", [])):
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_ACTION_CLASS_MISMATCH")
            if intent.get("selected_scope") not in set(current_authority.get("scopes", [])):
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_SCOPE_MISMATCH")
            if admission.get("adapter_authority_snapshot_digest") != digest(INVOCATION_BOUNDARY_DOMAIN, current_authority):
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_CHANGED")
            if admission.get("adapter_authority_version") != current_authority.get("exact_version_or_blob"):
                reasons.append("INVOCATION_ADAPTER_AUTHORITY_VERSION_CHANGED")

        current_binding_raw = invocation_evidence.get("actor_execution_binding")
        if not isinstance(current_binding_raw, Mapping):
            reasons.append("INVOCATION_ACTOR_BINDING_MISSING")
        else:
            try:
                current_binding = normalize_actor_binding(current_binding_raw)
            except RuntimeBoundaryError:
                reasons.append("INVOCATION_ACTOR_BINDING_INVALID")
            else:
                if current_binding.get("binding_id") != admission.get("actor_execution_binding_id"):
                    reasons.append("INVOCATION_ACTOR_BINDING_CHANGED")
                if current_binding.get("supporting_evidence_versions") != admission.get("actor_binding_evidence_versions"):
                    reasons.append("INVOCATION_ACTOR_EVIDENCE_FRONTIER_CHANGED")
                for ref, version in current_binding.get("supporting_evidence_versions", {}).items():
                    if current_versions.get(ref) != version:
                        reasons.append("INVOCATION_ACTOR_EVIDENCE_VERSION_CHANGED:" + ref)
                eligible, actor_reasons = actor_effect_eligibility(current_binding, current_binding["effect_mutation_class"])
                if not eligible:
                    reasons.extend("INVOCATION_" + r for r in actor_reasons)

        current_prior_effect = invocation_evidence.get("prior_effect_state", "UNKNOWN")
        if current_prior_effect == "UNRESOLVED":
            reasons.append("INVOCATION_UNRESOLVED_PRIOR_EFFECT")
        if current_prior_effect != (admission.get("prior_effect_state_refs") or ["UNKNOWN"])[0]:
            reasons.append("INVOCATION_PRIOR_EFFECT_STATE_CHANGED")

        return not reasons, sorted(set(reasons))


class EffectAdapter(Protocol):
    def execute(
        self,
        intent: Mapping[str, Any],
        admission: Mapping[str, Any],
        invocation_evidence: Mapping[str, Any],
    ) -> Mapping[str, Any]: ...


class NonLiveEffectAdapter:
    """Default implementation boundary: verifies current frontier, then still performs no effect."""

    adapter_class = "NON_LIVE_EFFECT_ADAPTER"

    def execute(self, intent: Mapping[str, Any], admission: Mapping[str, Any], invocation_evidence: Mapping[str, Any]) -> Mapping[str, Any]:
        ok, reasons = EffectBoundaryVerifier().verify(intent, admission, invocation_evidence, self.adapter_class)
        if not ok:
            return {"adapter_status": "NOT_EXECUTED", "reason": reasons[0], "reasons": reasons, "effect_attempted": False}
        return {"adapter_status": "NOT_EXECUTED", "reason": "NON_LIVE_BOUNDARY", "reasons": [], "effect_attempted": False}


class MockEffectAdapter:
    """Test-only adapter. It verifies current frontier and returns synthetic observation, never I/O."""

    def __init__(self, adapter_class: str, observation: Mapping[str, Any]):
        self.adapter_class = adapter_class
        self.observation = copy.deepcopy(dict(observation))

    def execute(self, intent: Mapping[str, Any], admission: Mapping[str, Any], invocation_evidence: Mapping[str, Any]) -> Mapping[str, Any]:
        ok, reasons = EffectBoundaryVerifier().verify(intent, admission, invocation_evidence, self.adapter_class)
        if not ok:
            return {"adapter_status": "NOT_EXECUTED", "reason": reasons[0], "reasons": reasons, "effect_attempted": False}
        return {
            "adapter_status": "MOCK_OBSERVATION_AVAILABLE",
            "effect_attempted": False,
            "reasons": [],
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
