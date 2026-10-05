from __future__ import annotations

import copy
import inspect
import unittest

from runtime_integration import (
    ACTOR_EVIDENCE_DOMAIN,
    POLICY_BINDING_DOMAIN,
    ActorExecutionBindingResolver,
    ContractCompilerFacade,
    EffectIntentEmitter,
    EffectOutcomeRecorder,
    MockEffectAdapter,
    NonLiveEffectAdapter,
    PreEffectRevalidator,
    RuntimeBoundaryError,
    RuntimeEvidenceResolver,
    RuntimeHumanExplanationAdapter,
    RuntimeInputAdapter,
    RuntimeResultFixator,
    TrustPolicyBindingResolver,
    actor_binding_consistency,
    actor_effect_eligibility,
    digest,
)


def evidence(
    eid,
    fact_class,
    value,
    *,
    source="OPERATOR_DECISION",
    scope="S",
    current="CURRENT",
    verified="VERIFIED",
    conflict="NONE",
    version=None,
):
    return {
        "evidence_id": eid,
        "evidence_kind": "EXACT_TEST_EVIDENCE",
        "exact_immutable_locator": "repo@commit:path:" + eid,
        "exact_version_or_blob": version or ("blob-" + eid),
        "exact_scope": scope,
        "source_class": source,
        "trust_basis_ref": "POLICY:TEST:" + source,
        "verified_state": verified,
        "currentness_state": current,
        "semantic_fact_class": fact_class,
        "conflict_state": conflict,
        "selected_basis_relation": "SELECTED",
        "provenance_chain": ["repo@commit:path:" + eid],
        "derived_positive_fact_ids": [],
        "unknown_fields": [],
        "semantic_value": value,
    }


def actor_claim(
    mode="CURRENT_WRITER",
    writer_req="REQUIRED",
    effect_class="CANDIDATE_ARTIFACT_WRITE",
    authoritative="NO",
):
    return {
        "actor_instance_ref": "KOD-v0.7",
        "actor_role": "KOD",
        "actor_execution_mode": mode,
        "current_writer_ref": "WRITER-KOD-v07" if mode == "CURRENT_WRITER" else None,
        "current_writer_state": "CURRENT" if mode == "CURRENT_WRITER" else "ABSENT",
        "writer_requirement": writer_req,
        "authoritative_state_mutation_required": authoritative,
        "effect_mutation_class": effect_class,
        "worker_effect_authority_ref": "AUTH-WORKER" if mode == "WORKER_READ_ONLY" else None,
        "writer_authority_ref": "AUTH-WRITER" if mode == "CURRENT_WRITER" else None,
        "recovery_state_ref": "RECOVERY-CLEAR",
        "freeze_state": "CLEAR",
        "handoff_state": "NONE",
        "replacement_state": "NONE",
    }


SOURCE_BY_FACT = {
    "ACTOR_INSTANCE_REF": "TASK_CONVEYOR",
    "ACTOR_ROLE": "TASK_CONVEYOR",
    "ACTOR_EXECUTION_MODE": "TASK_CONVEYOR",
    "CURRENT_WRITER_REF": "CURRENT_WRITER",
    "CURRENT_WRITER_STATE": "CURRENT_WRITER",
    "WRITER_REQUIREMENT": "TASK_CONVEYOR",
    "AUTHORITATIVE_STATE_MUTATION_REQUIRED": "TASK_CONVEYOR",
    "EFFECT_MUTATION_CLASS": "TASK_CONVEYOR",
    "WORKER_EFFECT_AUTHORITY_REF": "OPERATOR_DECISION",
    "WRITER_AUTHORITY_REF": "CURRENT_WRITER",
    "RECOVERY_STATE_REF": "RECOVERY",
    "FREEZE_STATE": "RECOVERY",
    "HANDOFF_STATE": "RECOVERY",
    "REPLACEMENT_STATE": "RECOVERY",
}


def actor_support(claim, *, omit=(), conflict_field=None, version_overrides=None):
    version_overrides = version_overrides or {}
    out = []
    for field, fact_class in ActorExecutionBindingResolver.FIELD_FACT_CLASS.items():
        if field in set(omit):
            continue
        eid = "ACT-" + field.upper()
        out.append(
            evidence(
                eid,
                fact_class,
                claim[field],
                source=SOURCE_BY_FACT[fact_class],
                scope=claim["actor_instance_ref"],
                version=version_overrides.get(field),
            )
        )
        if field == conflict_field:
            out.append(
                evidence(
                    eid + "-CONFLICT",
                    fact_class,
                    "CONFLICTING-VALUE",
                    source=SOURCE_BY_FACT[fact_class],
                    scope=claim["actor_instance_ref"],
                )
            )
    return out


def policy(*, current="CURRENT", conflict="NONE", version="blob-POLICY-E1"):
    allowed = {
        "AUTHORITY": ("OPERATOR_DECISION",),
        "TASK_CURRENTNESS": ("TASK_CONVEYOR",),
        "WRITER": ("CURRENT_WRITER",),
        "OUTCOME": ("VERIFIED_RESULT",),
    }
    prefixes = ("POLICY:TEST:",)
    scopes = ("*",)
    config = {
        "policy_ref": "POLICY:TEST",
        "allowed_source_classes": {k: sorted(v) for k, v in sorted(allowed.items())},
        "required_trust_basis_prefixes": sorted(prefixes),
        "governed_scopes": sorted(scopes),
        "governed_fact_classes": sorted(allowed),
    }
    pe = {
        "evidence_id": "POLICY-E1",
        "exact_immutable_locator": "repo@commit:path:POLICY-E1",
        "exact_version_or_blob": version,
        "source_class": "ACTIVE_PROJECT_SOURCE",
        "verified_state": "VERIFIED",
        "currentness_state": current,
        "conflict_state": conflict,
        "provenance_chain": ["repo@commit:path:POLICY-E1"],
        "semantic_fact_class": "TRUST_POLICY_RULE",
        "semantic_value": {
            "policy_ref": "POLICY:TEST",
            "policy_payload_digest": digest(POLICY_BINDING_DOMAIN, config),
        },
    }
    return TrustPolicyBindingResolver().bind(
        policy_ref="POLICY:TEST",
        allowed_source_classes=allowed,
        required_trust_basis_prefixes=prefixes,
        governed_scopes=scopes,
        policy_evidence=pe,
    )


def policy_dependency(p):
    return {
        "evidence_id": p.policy_evidence_id,
        "exact_immutable_locator": p.policy_evidence_locator,
        "exact_version_or_blob": p.policy_evidence_version,
        "binding_id": p.binding_id,
        "verified_state": p.policy_verified_state,
        "currentness_state": p.policy_currentness_state,
        "conflict_state": p.policy_conflict_state,
        "authority_source": p.policy_authority_source,
        "provenance": list(p.policy_provenance),
    }


def raw_input(extra_evidence, requested_facts, claim=None, actor_evidence=None):
    claim = claim or actor_claim()
    actor_evidence = actor_support(claim) if actor_evidence is None else list(actor_evidence)
    return {
        "entity_ref": "KOD",
        "instance_ref": "KOD-v0.7",
        "role": "KOD",
        "active_source_refs": ["SRC-SET-R07"],
        "evidence_items": list(extra_evidence) + actor_evidence,
        "requested_facts": requested_facts,
        "actor_execution_binding": claim,
        "immutable_inputs": [{"input_id": "I1", "version": "blob-I1"}],
        "profile": {"profile_id": "KOD"},
        "capabilities": ["OFFLINE_CODE"],
        "experience": [{"ref": "EXP-1", "advisory_only": True}],
        "causal_events": [],
        "human_input": [],
        "unknowns": [],
        "conflicts": [],
        "proposed_action": {
            "action_id": "A1",
            "action_class": "WRITE_CANDIDATE",
            "selected_scope": "S",
            "transition_type": "MUTATE",
            "target_ref": "candidate",
            "parameters": {"mode": "OFFLINE"},
        },
    }


def adapter_authority(adapter_class="MOCK", version="AUTH-V1", state="CURRENT", verified="VERIFIED", conflict="NONE"):
    return {
        "authority_ref": "ADAPTER-AUTH",
        "state": state,
        "adapter_class": adapter_class,
        "action_classes": ["WRITE_CANDIDATE"],
        "scopes": ["S"],
        "exact_immutable_locator": "repo@commit:path:ADAPTER-AUTH",
        "exact_version_or_blob": version,
        "verified_state": verified,
        "conflict_state": conflict,
    }


class FakeCore:
    def __init__(self, decision="ADMIT"):
        self.decision = decision

    def compile(self, envelope, resolution, actor_binding):
        return {
            "effective_context_id": "CTX-1",
            "effective_context_version": 1,
            "contract_id": "CONTRACT-1",
            "projection_valid": True,
            "aggregation": {"effect_decision": self.decision, "next_gate_class": "NONE"},
        }


def resolved_bundle(*, claim=None, actor_evidence=None):
    claim = claim or actor_claim()
    req = {
        "fact_id": "F-A",
        "semantic_fact_class": "AUTHORITY",
        "semantic_value": "ALLOW",
        "exact_scope": "S",
        "required_currentness": "CURRENT",
    }
    auth = evidence("E1", "AUTHORITY", "ALLOW")
    env = RuntimeInputAdapter().normalize(raw_input([auth], [req], claim=claim, actor_evidence=actor_evidence))
    p = policy()
    resolution = RuntimeEvidenceResolver().resolve(env, p)
    binding = resolution.get("actor_execution_binding")
    frontier = {
        item["evidence_id"]: item["exact_version_or_blob"]
        for item in env["evidence_items"]
    }
    dep = policy_dependency(p)
    frontier[dep["evidence_id"]] = dep["exact_version_or_blob"]
    return env, p, resolution, binding, frontier


def admission_bundle(adapter_class="MOCK"):
    env, p, resolution, binding, frontier = resolved_bundle()
    compiled = ContractCompilerFacade(FakeCore()).compile(env, resolution, binding)
    intent = EffectIntentEmitter().emit(
        env,
        resolution,
        compiled,
        binding,
        adapter_class=adapter_class,
        required_outcome_evidence_mode="EXACT_RESULT",
    )
    authority = adapter_authority(adapter_class)
    dep = policy_dependency(p)
    admission = PreEffectRevalidator().revalidate(
        intent,
        compiled,
        binding,
        current_evidence_versions=frontier,
        expected_evidence_versions={"E1": "blob-E1"},
        adapter_class=adapter_class,
        adapter_authority=authority,
        prior_effect_state="NONE",
        current_trust_policy_dependency=dep,
    )
    return env, p, resolution, binding, frontier, compiled, intent, authority, dep, admission


def invocation(binding, authority, frontier, dep, prior_effect_state="NONE"):
    return {
        "current_evidence_versions": dict(frontier),
        "adapter_authority": copy.deepcopy(authority),
        "actor_execution_binding": copy.deepcopy(binding),
        "trust_policy_dependency": copy.deepcopy(dep),
        "prior_effect_state": prior_effect_state,
    }


class RuntimeGroundingCorrectionR03Tests(unittest.TestCase):
    def test_adapter_does_not_create_actor_binding(self):
        claim = actor_claim()
        env = RuntimeInputAdapter().normalize(raw_input([], [], claim=claim))
        self.assertIsNone(env["actor_execution_binding"])
        self.assertEqual(env["actor_execution_binding_claim"], claim)

    def test_policy_binding_is_authoritative_and_current(self):
        p = policy()
        self.assertTrue(p.binding_valid())
        self.assertEqual(p.policy_currentness_state, "CURRENT")
        self.assertEqual(p.policy_conflict_state, "NONE")

    def test_stale_or_conflicted_policy_cannot_bind(self):
        with self.assertRaises(RuntimeBoundaryError):
            policy(current="STALE")
        with self.assertRaises(RuntimeBoundaryError):
            policy(conflict="CONFLICT")

    def test_resolution_carries_full_policy_dependency(self):
        _, p, resolution, _, _ = resolved_bundle()
        dep = resolution["trust_policy_dependency"]
        self.assertEqual(dep["evidence_id"], p.policy_evidence_id)
        self.assertEqual(dep["exact_version_or_blob"], p.policy_evidence_version)
        self.assertEqual(dep["binding_id"], p.binding_id)
        self.assertEqual(dep["currentness_state"], "CURRENT")
        self.assertEqual(dep["conflict_state"], "NONE")

    def test_actor_binding_is_evidence_derived(self):
        _, _, resolution, binding, _ = resolved_bundle()
        self.assertEqual(resolution["resolution_verdict"], "RESOLVED")
        self.assertEqual(binding["grounding_state"], "RESOLVED")
        self.assertGreaterEqual(len(binding["supporting_evidence_refs"]), 10)
        self.assertEqual(resolution["actor_execution_binding_id"], binding["binding_id"])

    def test_missing_actor_support_is_ineligible(self):
        claim = actor_claim()
        support = actor_support(claim, omit={"CURRENT_WRITER_STATE"})
        _, _, resolution, binding, _ = resolved_bundle(claim=claim, actor_evidence=support)
        self.assertEqual(resolution["resolution_verdict"], "PARTIAL_UNKNOWN")
        self.assertEqual(binding["grounding_state"], "UNKNOWN")
        ok, reasons = actor_effect_eligibility(binding, binding["effect_mutation_class"])
        self.assertFalse(ok)
        self.assertIn("ACTOR_BINDING_NOT_EVIDENCE_RESOLVED", reasons)

    def test_conflicting_actor_support_is_ineligible(self):
        claim = actor_claim()
        support = actor_support(claim, conflict_field="FREEZE_STATE")
        _, _, resolution, binding, _ = resolved_bundle(claim=claim, actor_evidence=support)
        self.assertEqual(resolution["resolution_verdict"], "CONFLICT")
        self.assertEqual(binding["grounding_state"], "CONFLICT")
        self.assertIn("freeze_state", binding["grounding_conflict_fields"])

    def test_contract_facade_requires_resolution_actor_binding(self):
        env, _, resolution, binding, _ = resolved_bundle()
        compiled = ContractCompilerFacade(FakeCore()).compile(env, resolution, binding)
        self.assertEqual(compiled["actor_execution_binding_id"], binding["binding_id"])
        self.assertEqual(compiled["trust_policy_dependency"], resolution["trust_policy_dependency"])
        forged = copy.deepcopy(binding)
        forged["actor_execution_mode"] = "WORKER_READ_ONLY"
        forged["binding_id"] = "FORGED"
        with self.assertRaises(RuntimeBoundaryError):
            ContractCompilerFacade(FakeCore()).compile(env, resolution, forged)

    def test_intent_carries_policy_and_actor_evidence_dependencies(self):
        _, _, resolution, binding, _, _, intent, _, _, _ = admission_bundle()
        self.assertEqual(intent["trust_policy_dependency"], resolution["trust_policy_dependency"])
        self.assertEqual(intent["actor_execution_binding_id"], binding["binding_id"])
        self.assertEqual(intent["actor_binding_evidence_versions"], binding["supporting_evidence_versions"])
        self.assertIn(resolution["trust_policy_evidence_id"], intent["required_evidence_ids"])

    def test_admission_frontier_includes_policy_and_actor_versions(self):
        _, _, _, binding, _, _, _, _, dep, admission = admission_bundle()
        expected = dict(admission["expected_current_evidence_versions"])
        self.assertEqual(expected[dep["evidence_id"]], dep["exact_version_or_blob"])
        for ref, version in binding["supporting_evidence_versions"].items():
            self.assertEqual(expected[ref], version)
        self.assertEqual(admission["trust_policy_dependency"], dep)

    def test_policy_change_before_revalidation_blocks_admission(self):
        env, _, resolution, binding, frontier = resolved_bundle()
        compiled = ContractCompilerFacade(FakeCore()).compile(env, resolution, binding)
        intent = EffectIntentEmitter().emit(env, resolution, compiled, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        current_dep = copy.deepcopy(resolution["trust_policy_dependency"])
        current_dep["exact_version_or_blob"] = "blob-POLICY-E2"
        frontier2 = dict(frontier)
        frontier2[current_dep["evidence_id"]] = "blob-POLICY-E2"
        admission = PreEffectRevalidator().revalidate(
            intent,
            compiled,
            binding,
            current_evidence_versions=frontier2,
            expected_evidence_versions={"E1": "blob-E1"},
            adapter_class="MOCK",
            adapter_authority=adapter_authority("MOCK"),
            prior_effect_state="NONE",
            current_trust_policy_dependency=current_dep,
        )
        self.assertNotEqual(admission["revalidation_verdict"], "ADMIT_EFFECT_NOW")
        self.assertTrue(any("TRUST_POLICY" in r for r in admission["revalidation_reason_ids"]))

    def test_policy_change_after_admission_blocks_invocation(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        changed = copy.deepcopy(dep)
        changed["exact_version_or_blob"] = "blob-POLICY-E2"
        frontier2 = dict(frontier)
        frontier2[dep["evidence_id"]] = "blob-POLICY-E2"
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(binding, authority, frontier2, changed)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("TRUST_POLICY" in r for r in out["reasons"]))

    def test_policy_conflict_after_admission_blocks_invocation(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        changed = copy.deepcopy(dep)
        changed["conflict_state"] = "CONFLICT"
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(binding, authority, frontier, changed)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertIn("INVOCATION_TRUST_POLICY_CONFLICT", out["reasons"])

    def test_actor_evidence_version_change_after_admission_blocks_invocation(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        claim = actor_claim()
        changed_support = actor_support(claim, version_overrides={"FREEZE_STATE": "blob-ACT-FREEZE-STATE-V2"})
        changed_binding = ActorExecutionBindingResolver().resolve(claim, changed_support)
        frontier2 = dict(frontier)
        for ref, version in changed_binding["supporting_evidence_versions"].items():
            frontier2[ref] = version
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(changed_binding, authority, frontier2, dep)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("ACTOR" in r or "EVIDENCE_FRONTIER" in r for r in out["reasons"]))

    def test_recovery_state_change_after_admission_blocks_invocation(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        claim = actor_claim()
        changed_claim = copy.deepcopy(claim)
        changed_claim["freeze_state"] = "FROZEN"
        changed_support = actor_support(changed_claim)
        changed_binding = ActorExecutionBindingResolver().resolve(changed_claim, changed_support)
        frontier2 = dict(frontier)
        for ref, version in changed_binding["supporting_evidence_versions"].items():
            frontier2[ref] = version
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(changed_binding, authority, frontier2, dep)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("ACTOR" in r or "RECOVERY" in r for r in out["reasons"]))

    def test_c2_frontier_change_after_admission_still_blocks(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        frontier2 = dict(frontier)
        frontier2["E1"] = "blob-E1-v2"
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(binding, authority, frontier2, dep)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertIn("INVOCATION_EVIDENCE_FRONTIER_CHANGED", out["reasons"])

    def test_c2_mutated_intent_still_blocks(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        mutated = copy.deepcopy(intent)
        mutated["action_parameters"]["mode"] = "MUTATED"
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            mutated, admission, invocation(binding, authority, frontier, dep)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("INTENT_" in r for r in out["reasons"]))

    def test_c2_mutated_admission_still_blocks(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        mutated = copy.deepcopy(admission)
        mutated["revalidation_reason_ids"] = ["TAMPERED"]
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, mutated, invocation(binding, authority, frontier, dep)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertIn("ADMISSION_ID_MISMATCH_AT_INVOCATION", out["reasons"])

    def test_c2_adapter_authority_change_still_blocks(self):
        _, _, _, binding, frontier, _, intent, _, dep, admission = admission_bundle()
        changed = adapter_authority("MOCK", version="AUTH-V2")
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(binding, changed, frontier, dep)
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("ADAPTER_AUTHORITY" in r for r in out["reasons"]))

    def test_c2_unresolved_prior_effect_still_blocks(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(binding, authority, frontier, dep, prior_effect_state="UNRESOLVED")
        )
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertIn("INVOCATION_UNRESOLVED_PRIOR_EFFECT", out["reasons"])

    def test_contradictory_authoritative_writer_binding_is_ineligible(self):
        claim = actor_claim(
            writer_req="NOT_REQUIRED_FOR_TASK",
            effect_class="AUTHORITATIVE_CURRENT_STATE_WRITE",
            authoritative="YES",
        )
        support = actor_support(claim)
        binding = ActorExecutionBindingResolver().resolve(claim, support)
        reasons = actor_binding_consistency(binding)
        self.assertIn("AUTHORITATIVE_WRITE_REQUIRES_WRITER_REQUIRED", reasons)
        ok, reasons2 = actor_effect_eligibility(binding, binding["effect_mutation_class"])
        self.assertFalse(ok)
        self.assertIn("WRITER_NOT_REQUIRED_CONTRADICTS_AUTHORITATIVE_MUTATION", reasons2)

    def test_worker_cannot_gain_current_writer_by_claim(self):
        claim = actor_claim(mode="WORKER_READ_ONLY", writer_req="REQUIRED", effect_class="AUTHORITATIVE_CURRENT_STATE_WRITE", authoritative="YES")
        support = actor_support(claim)
        binding = ActorExecutionBindingResolver().resolve(claim, support)
        ok, reasons = actor_effect_eligibility(binding, binding["effect_mutation_class"])
        self.assertFalse(ok)
        self.assertIn("WORKER_CANNOT_SATISFY_WRITER_REQUIRED", reasons)
        self.assertIn("WORKER_CANNOT_AUTHORITATIVE_STATE_WRITE", reasons)

    def test_non_live_adapter_still_never_effects_world(self):
        _, _, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle("NON_LIVE_EFFECT_ADAPTER")
        out = NonLiveEffectAdapter().execute(intent, admission, invocation(binding, authority, frontier, dep))
        self.assertFalse(out["effect_attempted"])
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertEqual(out["reason"], "NON_LIVE_BOUNDARY")

    def test_mock_observation_cannot_fabricate_outcome(self):
        _, p, _, binding, frontier, _, intent, authority, dep, admission = admission_bundle()
        adapter_result = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(
            intent, admission, invocation(binding, authority, frontier, dep)
        )
        recorder = EffectOutcomeRecorder()
        unresolved = recorder.record(intent, admission, adapter_result, outcome_evidence=[], policy=p)
        self.assertEqual(unresolved["outcome_state"], "UNRESOLVED")
        ev = evidence("OUT-E1", "OUTCOME", "SUCCESS", source="VERIFIED_RESULT")
        resolved = recorder.record(intent, admission, adapter_result, outcome_evidence=[ev], policy=p)
        self.assertEqual(resolved["outcome_state"], "EVIDENCED_SUCCESS")
        self.assertFalse(resolved["effect_attempted"])

    def test_result_and_human_explanation_share_truth_path(self):
        env, _, resolution, binding, _ = resolved_bundle()
        compiled = ContractCompilerFacade(FakeCore()).compile(env, resolution, binding)
        result = RuntimeResultFixator().fix(
            env, resolution, compiled, None, None, None,
            next_gate_candidate={"recipient": "KOO", "task_ref": "T-NEXT"},
        )
        view = RuntimeHumanExplanationAdapter().render(result)
        self.assertEqual(view["effect_outcome"], result["outcome_state"])
        self.assertEqual(view["next_gate_candidate"], result["next_gate_candidate"])
        self.assertTrue(view["next_gate_requires_external_authority"])

    def test_actor_binding_identity_changes_with_evidence_version(self):
        claim = actor_claim()
        b1 = ActorExecutionBindingResolver().resolve(claim, actor_support(claim))
        b2 = ActorExecutionBindingResolver().resolve(
            claim, actor_support(claim, version_overrides={"FREEZE_STATE": "blob-ACT-FREEZE-STATE-V2"})
        )
        self.assertNotEqual(b1["binding_id"], b2["binding_id"])
        self.assertNotEqual(b1["grounding_digest"], b2["grounding_digest"])

    def test_no_forbidden_io_imports(self):
        src = inspect.getsource(__import__("runtime_integration"))
        for forbidden in ("socket", "requests", "urllib", "subprocess", "ftplib", "telnetlib"):
            self.assertNotIn("import " + forbidden, src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
