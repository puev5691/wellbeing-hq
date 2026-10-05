from __future__ import annotations

import copy
import inspect
import unittest

from runtime_integration import (
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
    TrustPolicy,
    TrustPolicyBindingResolver,
    POLICY_BINDING_DOMAIN,
    actor_binding_consistency,
    actor_effect_eligibility,
    digest,
    normalize_actor_binding,
)


def evidence(eid, fact_class, value, *, source="OPERATOR_DECISION", scope="S", current="CURRENT", verified="VERIFIED", conflict="NONE"):
    return {
        "evidence_id": eid,
        "evidence_kind": "EXACT_TEST_EVIDENCE",
        "exact_immutable_locator": "repo@commit:path:" + eid,
        "exact_version_or_blob": "blob-" + eid,
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


def actor(mode="CURRENT_WRITER", writer_req="REQUIRED", effect_class="CANDIDATE_ARTIFACT_WRITE"):
    return normalize_actor_binding({
        "actor_instance_ref": "KOD-v0.7",
        "actor_role": "KOD",
        "actor_execution_mode": mode,
        "current_writer_ref": "WRITER-KOD-v07" if mode == "CURRENT_WRITER" else None,
        "current_writer_state": "CURRENT" if mode == "CURRENT_WRITER" else "ABSENT",
        "writer_requirement": writer_req,
        "authoritative_state_mutation_required": "NO",
        "effect_mutation_class": effect_class,
        "worker_effect_authority_ref": "AUTH-WORKER" if mode == "WORKER_READ_ONLY" else None,
        "writer_authority_ref": "AUTH-WRITER" if mode == "CURRENT_WRITER" else None,
        "recovery_state_ref": "RECOVERY-CLEAR",
        "freeze_state": "CLEAR",
        "handoff_state": "NONE",
        "replacement_state": "NONE",
        "recovery_evidence_refs": ["RECOVERY-E1"],
        "binding_provenance": ["WRITER-E1", "RECOVERY-E1"],
    })


def policy(*, evidence_current="CURRENT", evidence_source="ACTIVE_PROJECT_SOURCE", payload_override=None):
    allowed = {
        "AUTHORITY": ("OPERATOR_DECISION",),
        "TASK_CURRENTNESS": ("TASK_CONVEYOR",),
        "WRITER": ("CURRENT_WRITER",),
        "OUTCOME": ("VERIFIED_RESULT",),
    }
    prefixes = ("POLICY:TEST:",)
    scopes = ("*",)
    payload = {
        "policy_ref": "POLICY:TEST",
        "allowed_source_classes": {k: sorted(v) for k, v in sorted(allowed.items())},
        "required_trust_basis_prefixes": sorted(prefixes),
        "governed_scopes": sorted(scopes),
        "governed_fact_classes": sorted(allowed),
    }
    pe = {
        "evidence_id": "POLICY-E1",
        "exact_immutable_locator": "repo@commit:path:POLICY-E1",
        "exact_version_or_blob": "blob-POLICY-E1",
        "source_class": evidence_source,
        "verified_state": "VERIFIED",
        "currentness_state": evidence_current,
        "conflict_state": "NONE",
        "provenance_chain": ["repo@commit:path:POLICY-E1"],
        "semantic_fact_class": "TRUST_POLICY_RULE",
        "semantic_value": {
            "policy_ref": "POLICY:TEST",
            "policy_payload_digest": payload_override or digest(POLICY_BINDING_DOMAIN, payload),
        },
    }
    return TrustPolicyBindingResolver().bind(
        policy_ref="POLICY:TEST",
        allowed_source_classes=allowed,
        required_trust_basis_prefixes=prefixes,
        governed_scopes=scopes,
        policy_evidence=pe,
    )


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


def invocation(binding, authority, versions=None, prior_effect_state="NONE"):
    return {
        "current_evidence_versions": dict(versions or {"E1": "v1"}),
        "adapter_authority": copy.deepcopy(authority),
        "actor_execution_binding": copy.deepcopy(binding),
        "prior_effect_state": prior_effect_state,
    }


def raw_input(evidence_items, requested_facts, binding=None):
    return {
        "entity_ref": "KOD",
        "instance_ref": "KOD-v0.7",
        "role": "KOD",
        "active_source_refs": ["SRC-SET-R07"],
        "evidence_items": evidence_items,
        "requested_facts": requested_facts,
        "actor_execution_binding": binding or actor(),
        "immutable_inputs": [{"input_id": "I1", "version": "blob-I1"}],
        "profile": {"profile_id": "KOD"},
        "capabilities": ["OFFLINE_CODE"],
        "experience": [{"ref": "EXP-1", "advisory_only": True}],
        "causal_events": [],
        "human_input": [],
        "unknowns": [],
        "conflicts": [],
        "proposed_action": {"action_id": "A1", "action_class": "WRITE_CANDIDATE", "selected_scope": "S", "transition_type": "MUTATE", "target_ref": "candidate", "parameters": {"mode": "OFFLINE"}},
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


class RuntimeIntegrationTests(unittest.TestCase):
    def test_adapter_cannot_assert_positive_fact(self):
        item = evidence("E1", "AUTHORITY", "ALLOW")
        item["derived_positive_fact_ids"] = ["FORGED"]
        with self.assertRaises(RuntimeBoundaryError):
            RuntimeInputAdapter().normalize(raw_input([item], []))

    def test_exact_authority_resolves_only_under_authoritatively_bound_policy(self):
        req = {"fact_id": "F-A", "semantic_fact_class": "AUTHORITY", "semantic_value": "ALLOW", "exact_scope": "S", "required_currentness": "CURRENT"}
        env = RuntimeInputAdapter().normalize(raw_input([evidence("E1", "AUTHORITY", "ALLOW")], [req]))
        p = policy()
        self.assertTrue(p.binding_valid())
        r = RuntimeEvidenceResolver().resolve(env, p)
        self.assertEqual(r["resolution_verdict"], "RESOLVED")
        self.assertEqual(r["selected_fact_bindings"][0]["evidence_id"], "E1")
        self.assertEqual(r["trust_policy_binding_id"], p.binding_id)

    def test_policy_binding_rejects_stale_or_payload_mismatch(self):
        with self.assertRaises(RuntimeBoundaryError):
            policy(evidence_current="STALE")
        with self.assertRaises(RuntimeBoundaryError):
            policy(payload_override="0" * 64)

    def test_profile_human_or_model_source_cannot_become_authority(self):
        req = {"fact_id": "F-A", "semantic_fact_class": "AUTHORITY", "semantic_value": "ALLOW", "exact_scope": "S", "required_currentness": "CURRENT"}
        env = RuntimeInputAdapter().normalize(raw_input([evidence("E1", "AUTHORITY", "ALLOW", source="OTHER_EXPLICIT")], [req]))
        r = RuntimeEvidenceResolver().resolve(env, policy())
        self.assertEqual(r["resolution_verdict"], "PARTIAL_UNKNOWN")
        self.assertFalse(r["selected_fact_bindings"])

    def test_unverified_support_stays_unknown(self):
        req = {"fact_id": "F-A", "semantic_fact_class": "AUTHORITY", "semantic_value": "ALLOW", "exact_scope": "S", "required_currentness": "CURRENT"}
        env = RuntimeInputAdapter().normalize(raw_input([evidence("E1", "AUTHORITY", "ALLOW", verified="UNVERIFIED")], [req]))
        r = RuntimeEvidenceResolver().resolve(env, policy())
        self.assertEqual(r["resolution_verdict"], "PARTIAL_UNKNOWN")
        self.assertEqual(r["unknown_fact_bindings"][0]["state"], "UNKNOWN")

    def test_conflict_is_not_winner_by_order(self):
        req = {"fact_id": "F-A", "semantic_fact_class": "AUTHORITY", "semantic_value": "ALLOW", "exact_scope": "S", "required_currentness": "CURRENT"}
        a = evidence("E-A", "AUTHORITY", "ALLOW")
        b = evidence("E-B", "AUTHORITY", "DENY")
        env1 = RuntimeInputAdapter().normalize(raw_input([a, b], [req]))
        env2 = RuntimeInputAdapter().normalize(raw_input([b, a], [req]))
        r1 = RuntimeEvidenceResolver().resolve(env1, policy())
        r2 = RuntimeEvidenceResolver().resolve(env2, policy())
        self.assertEqual(r1["resolution_verdict"], "CONFLICT")
        self.assertEqual(r2["resolution_verdict"], "CONFLICT")

    def test_worker_writer_recovery_semantics(self):
        b = actor(mode="WORKER_READ_ONLY", writer_req="REQUIRED", effect_class="AUTHORITATIVE_CURRENT_STATE_WRITE")
        ok, reasons = actor_effect_eligibility(b, b["effect_mutation_class"])
        self.assertFalse(ok)
        self.assertIn("WORKER_CANNOT_SATISFY_WRITER_REQUIRED", reasons)
        self.assertIn("WORKER_CANNOT_AUTHORITATIVE_STATE_WRITE", reasons)
        b2 = actor(mode="WORKER_READ_ONLY", writer_req="NOT_REQUIRED_FOR_TASK", effect_class="READ_ONLY_ANALYSIS")
        self.assertIsNone(b2["current_writer_ref"])
        ok2, _ = actor_effect_eligibility(b2, b2["effect_mutation_class"])
        self.assertTrue(ok2)

    def _resolved(self):
        req = {"fact_id": "F-A", "semantic_fact_class": "AUTHORITY", "semantic_value": "ALLOW", "exact_scope": "S", "required_currentness": "CURRENT"}
        env = RuntimeInputAdapter().normalize(raw_input([evidence("E1", "AUTHORITY", "ALLOW")], [req]))
        binding = normalize_actor_binding(env["actor_execution_binding"])
        r = RuntimeEvidenceResolver().resolve(env, policy())
        return env, binding, r

    def test_contract_facade_propagates_resolution_and_actor_binding(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        self.assertEqual(c["runtime_evidence_resolution_id"], r["resolution_id"])
        self.assertEqual(c["actor_execution_binding_id"], binding["binding_id"])

    def test_intent_requires_resolved_and_admit(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        self.assertIsNotNone(intent)
        self.assertEqual(intent["intent_state"], "PRE_EFFECT_INTENT")
        self.assertEqual(intent["authority_evidence_refs"], ["E1"])
        self.assertEqual(intent["actor_execution_binding_id"], binding["binding_id"])
        self.assertEqual(intent["input_version_refs"], [("I1", "blob-I1")])
        c2 = ContractCompilerFacade(FakeCore("NO_EFFECT")).compile(env, r, binding)
        self.assertIsNone(EffectIntentEmitter().emit(env, r, c2, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT"))

    def test_pre_effect_admission_invalidates_on_frontier_change(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        reval = PreEffectRevalidator()
        good = reval.revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        self.assertEqual(good["revalidation_verdict"], "ADMIT_EFFECT_NOW")
        stale = reval.revalidate(intent, c, binding, current_evidence_versions={"E1": "v2"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        self.assertNotEqual(stale["revalidation_verdict"], "ADMIT_EFFECT_NOW")

    def test_pre_effect_admission_invalidates_on_actor_binding_change(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        changed = copy.deepcopy(binding)
        changed["freeze_state"] = "FROZEN"
        changed = normalize_actor_binding(changed)
        admission = PreEffectRevalidator().revalidate(intent, c, changed, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        self.assertNotEqual(admission["revalidation_verdict"], "ADMIT_EFFECT_NOW")
        self.assertIn("ACTOR_BINDING_CHANGED", admission["revalidation_reason_ids"])

    def test_unresolved_prior_effect_blocks_overlap(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="UNRESOLVED")
        self.assertNotEqual(admission["revalidation_verdict"], "ADMIT_EFFECT_NOW")
        self.assertIn("UNRESOLVED_PRIOR_EFFECT", admission["revalidation_reason_ids"])

    def test_non_live_adapter_never_effects_world(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="NON_LIVE_EFFECT_ADAPTER", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("NON_LIVE_EFFECT_ADAPTER")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="NON_LIVE_EFFECT_ADAPTER", adapter_authority=authority, prior_effect_state="NONE")
        out = NonLiveEffectAdapter().execute(intent, admission, invocation(binding, authority))
        self.assertFalse(out["effect_attempted"])
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")

    def test_intent_or_mock_observation_cannot_fabricate_outcome(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        adapter_result = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(intent, admission, invocation(binding, authority))
        rec = EffectOutcomeRecorder()
        unresolved = rec.record(intent, admission, adapter_result, outcome_evidence=[], policy=policy())
        self.assertEqual(unresolved["outcome_state"], "UNRESOLVED")
        ev = evidence("OUT-E1", "OUTCOME", "SUCCESS", source="VERIFIED_RESULT")
        resolved = rec.record(intent, admission, adapter_result, outcome_evidence=[ev], policy=policy())
        self.assertEqual(resolved["outcome_state"], "EVIDENCED_SUCCESS")
        self.assertFalse(resolved["effect_attempted"])

    def test_invocation_boundary_rejects_frontier_change_after_admission(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(intent, admission, invocation(binding, authority, {"E1": "v2"}))
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertIn("INVOCATION_EVIDENCE_FRONTIER_CHANGED", out["reasons"])

    def test_invocation_boundary_rejects_mutated_intent_or_admission(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        mutated_intent = copy.deepcopy(intent)
        mutated_intent["action_parameters"]["mode"] = "MUTATED"
        out1 = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(mutated_intent, admission, invocation(binding, authority))
        self.assertEqual(out1["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("INTENT_" in r for r in out1["reasons"]))
        mutated_admission = copy.deepcopy(admission)
        mutated_admission["revalidation_reason_ids"] = ["TAMPERED"]
        out2 = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(intent, mutated_admission, invocation(binding, authority))
        self.assertEqual(out2["adapter_status"], "NOT_EXECUTED")
        self.assertIn("ADMISSION_ID_MISMATCH_AT_INVOCATION", out2["reasons"])

    def test_invocation_boundary_rejects_authority_or_recovery_change(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        changed_authority = adapter_authority("MOCK", version="AUTH-V2")
        out1 = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(intent, admission, invocation(binding, changed_authority))
        self.assertEqual(out1["adapter_status"], "NOT_EXECUTED")
        self.assertIn("INVOCATION_ADAPTER_AUTHORITY_CHANGED", out1["reasons"])
        changed_binding = copy.deepcopy(binding)
        changed_binding["freeze_state"] = "FROZEN"
        changed_binding = normalize_actor_binding(changed_binding)
        out2 = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(intent, admission, invocation(changed_binding, authority))
        self.assertEqual(out2["adapter_status"], "NOT_EXECUTED")
        self.assertTrue(any("ACTOR_BINDING" in r or "RECOVERY" in r for r in out2["reasons"]))

    def test_c3_rejects_contradictory_writer_mutation_binding(self):
        bad = copy.deepcopy(actor())
        bad["effect_mutation_class"] = "AUTHORITATIVE_CURRENT_STATE_WRITE"
        bad["authoritative_state_mutation_required"] = "YES"
        bad["writer_requirement"] = "NOT_REQUIRED_FOR_TASK"
        bad = normalize_actor_binding(bad)
        reasons = actor_binding_consistency(bad)
        self.assertIn("AUTHORITATIVE_WRITE_REQUIRES_WRITER_REQUIRED", reasons)
        ok, eligible_reasons = actor_effect_eligibility(bad, bad["effect_mutation_class"])
        self.assertFalse(ok)
        self.assertIn("WRITER_NOT_REQUIRED_CONTRADICTS_AUTHORITATIVE_MUTATION", eligible_reasons)

    def test_invocation_boundary_rejects_prior_effect_change(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        intent = EffectIntentEmitter().emit(env, r, c, binding, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
        authority = adapter_authority("MOCK")
        admission = PreEffectRevalidator().revalidate(intent, c, binding, current_evidence_versions={"E1": "v1"}, expected_evidence_versions={"E1": "v1"}, adapter_class="MOCK", adapter_authority=authority, prior_effect_state="NONE")
        out = MockEffectAdapter("MOCK", {"outcome": "SUCCESS"}).execute(intent, admission, invocation(binding, authority, prior_effect_state="UNRESOLVED"))
        self.assertEqual(out["adapter_status"], "NOT_EXECUTED")
        self.assertIn("INVOCATION_UNRESOLVED_PRIOR_EFFECT", out["reasons"])

    def test_result_and_human_explanation_share_truth_path(self):
        env, binding, r = self._resolved()
        c = ContractCompilerFacade(FakeCore()).compile(env, r, binding)
        result = RuntimeResultFixator().fix(env, r, c, None, None, None, next_gate_candidate={"recipient": "KOO", "task_ref": "T-NEXT"})
        view = RuntimeHumanExplanationAdapter().render(result)
        self.assertEqual(view["effect_outcome"], result["outcome_state"])
        self.assertEqual(view["next_gate_candidate"], result["next_gate_candidate"])
        self.assertTrue(view["next_gate_requires_external_authority"])

    def test_identity_determinism(self):
        raw = raw_input([], [], actor())
        a = RuntimeInputAdapter().normalize(raw)
        b = RuntimeInputAdapter().normalize(copy.deepcopy(raw))
        self.assertEqual(a["envelope_id"], b["envelope_id"])

    def test_no_forbidden_io_imports(self):
        src = inspect.getsource(__import__("runtime_integration"))
        for forbidden in ("socket", "requests", "urllib", "subprocess", "ftplib", "telnetlib"):
            self.assertNotIn("import " + forbidden, src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
