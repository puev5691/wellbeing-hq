from __future__ import annotations

import copy
import inspect
import unittest

from runtime_integration import (
    ActorExecutionBindingResolver,
    ContractCompilerFacade,
    EffectIntentEmitter,
    MockEffectAdapter,
    NonLiveEffectAdapter,
    POLICY_BINDING_DOMAIN,
    PreEffectRevalidator,
    RuntimeBoundaryError,
    RuntimeEvidenceResolver,
    RuntimeInputAdapter,
    TaskExecutionBindingResolver,
    TrustPolicyBindingResolver,
    actor_effect_eligibility,
    digest,
    task_binding_eligibility,
)


def evidence(eid, fact_class, value, *, source, scope, version=None, current="CURRENT", verified="VERIFIED", conflict="NONE"):
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


def actor_claim():
    return {
        "actor_instance_ref": "KOD-v0.7",
        "actor_role": "KOD",
        "actor_execution_mode": "CURRENT_WRITER",
        "current_writer_ref": "WRITER-KOD-v07",
        "current_writer_state": "CURRENT",
        "writer_requirement": "REQUIRED",
        "authoritative_state_mutation_required": "NO",
        "effect_mutation_class": "CANDIDATE_ARTIFACT_WRITE",
        "worker_effect_authority_ref": None,
        "writer_authority_ref": "AUTH-WRITER",
        "recovery_state_ref": "RECOVERY-CLEAR",
        "freeze_state": "CLEAR",
        "handoff_state": "NONE",
        "replacement_state": "NONE",
    }


ACTOR_SOURCE = {
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


def actor_support(claim=None):
    claim = claim or actor_claim()
    out = []
    for field, fact_class in ActorExecutionBindingResolver.FIELD_FACT_CLASS.items():
        out.append(evidence(
            "ACT-" + field.upper(),
            fact_class,
            claim[field],
            source=ACTOR_SOURCE[fact_class],
            scope=claim["actor_instance_ref"],
        ))
    return out


def task_claim(*, task_ref="TASK-R04", authority_state="AUTHORIZED", currentness="CURRENT", supersession="NOT_SUPERSEDED"):
    return {
        "task_ref": task_ref,
        "task_authority_basis_ref": "AUTH-R04",
        "task_authority_state": authority_state,
        "task_currentness": currentness,
        "task_supersession_state": supersession,
    }


TASK_SOURCE = {
    "TASK_IDENTITY_REF": "TASK_CONVEYOR",
    "TASK_AUTHORITY_BASIS_REF": "OPERATOR_DECISION",
    "TASK_AUTHORITY_STATE": "OPERATOR_DECISION",
    "TASK_CURRENTNESS": "TASK_CONVEYOR",
    "TASK_SUPERSESSION_STATE": "TASK_CONVEYOR",
}


def task_support(claim=None, *, omit=(), conflict_field=None, version_overrides=None, scope_override=None):
    claim = claim or task_claim()
    version_overrides = version_overrides or {}
    out = []
    for field, fact_class in TaskExecutionBindingResolver.FIELD_FACT_CLASS.items():
        if field in set(omit):
            continue
        eid = "TASK-" + field.upper()
        out.append(evidence(
            eid,
            fact_class,
            claim[field],
            source=TASK_SOURCE[fact_class],
            scope=scope_override or claim["task_ref"],
            version=version_overrides.get(field),
        ))
        if field == conflict_field:
            out.append(evidence(
                eid + "-CONFLICT",
                fact_class,
                "CONFLICTING-VALUE",
                source=TASK_SOURCE[fact_class],
                scope=scope_override or claim["task_ref"],
            ))
    return out


def policy():
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
        "exact_version_or_blob": "blob-POLICY-E1",
        "source_class": "ACTIVE_PROJECT_SOURCE",
        "verified_state": "VERIFIED",
        "currentness_state": "CURRENT",
        "conflict_state": "NONE",
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


def raw_input(*, aclaim=None, tclaim=None, aevidence=None, tevidence=None, extra=None):
    aclaim = aclaim or actor_claim()
    tclaim = tclaim or task_claim()
    return {
        "entity_ref": "KOD",
        "instance_ref": "KOD-v0.7",
        "role": "KOD",
        "active_source_refs": ["SRC-SET-R07"],
        "evidence_items": list(extra or []) + list(aevidence if aevidence is not None else actor_support(aclaim)) + list(tevidence if tevidence is not None else task_support(tclaim)),
        "requested_facts": [],
        "actor_execution_binding": aclaim,
        "task_execution_binding": tclaim,
        "immutable_inputs": [{"input_id": "I1", "version": "blob-I1"}],
        "profile": {"profile_id": "KOD"},
        "capabilities": ["OFFLINE_CODE"],
        "experience": [],
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


class FakeCore:
    def compile(self, envelope, resolution, actor_binding):
        return {
            "effective_context_id": "CTX-1",
            "effective_context_version": 1,
            "contract_id": "CONTRACT-1",
            "projection_valid": True,
            "aggregation": {"effect_decision": "ADMIT", "next_gate_class": "NONE"},
        }


def adapter_authority(version="AUTH-V1"):
    return {
        "authority_ref": "ADAPTER-AUTH",
        "state": "CURRENT",
        "adapter_class": "MOCK",
        "action_classes": ["WRITE_CANDIDATE"],
        "scopes": ["S"],
        "exact_immutable_locator": "repo@commit:path:ADAPTER-AUTH",
        "exact_version_or_blob": version,
        "verified_state": "VERIFIED",
        "conflict_state": "NONE",
    }


def bundle(*, tclaim=None, tevidence=None, aclaim=None, aevidence=None):
    env = RuntimeInputAdapter().normalize(raw_input(aclaim=aclaim, tclaim=tclaim, aevidence=aevidence, tevidence=tevidence))
    p = policy()
    resolution = RuntimeEvidenceResolver().resolve(env, p)
    actor = resolution.get("actor_execution_binding")
    task = resolution.get("task_execution_binding")
    frontier = {e["evidence_id"]: e["exact_version_or_blob"] for e in env["evidence_items"]}
    pdep = policy_dependency(p)
    frontier[pdep["evidence_id"]] = pdep["exact_version_or_blob"]
    return env, p, resolution, actor, task, frontier, pdep


def eligible_bundle():
    env, p, resolution, actor, task, frontier, pdep = bundle()
    compiled = ContractCompilerFacade(FakeCore()).compile(env, resolution, actor)
    intent = EffectIntentEmitter().emit(env, resolution, compiled, actor, adapter_class="MOCK", required_outcome_evidence_mode="EXACT_RESULT")
    authority = adapter_authority()
    admission = PreEffectRevalidator().revalidate(
        intent,
        compiled,
        actor,
        current_evidence_versions=frontier,
        expected_evidence_versions={},
        adapter_class="MOCK",
        adapter_authority=authority,
        prior_effect_state="NONE",
        current_trust_policy_dependency=pdep,
        current_task_execution_binding=task,
    )
    return env,p,resolution,actor,task,frontier,pdep,compiled,intent,authority,admission


def invocation(actor, task, frontier, pdep, authority=None, prior="NONE"):
    return {
        "current_evidence_versions": dict(frontier),
        "adapter_authority": copy.deepcopy(authority or adapter_authority()),
        "actor_execution_binding": copy.deepcopy(actor),
        "task_execution_binding": copy.deepcopy(task),
        "trust_policy_dependency": copy.deepcopy(pdep),
        "prior_effect_state": prior,
    }


class TaskGroundingR04Tests(unittest.TestCase):
    # Mandatory task proof failures.
    def test_missing_task_authority_support_blocks(self):
        claim = task_claim()
        env,p,resolution,actor,task,_,_ = bundle(tclaim=claim, tevidence=task_support(claim, omit={"task_authority_state"}))
        self.assertEqual(task["grounding_state"], "UNKNOWN")
        self.assertEqual(resolution["resolution_verdict"], "PARTIAL_UNKNOWN")
        self.assertIsNone(EffectIntentEmitter().emit(env, resolution, {"aggregation":{"effect_decision":"ADMIT"},"projection_valid":True}, actor, adapter_class="MOCK", required_outcome_evidence_mode="X"))

    def test_missing_task_currentness_support_blocks(self):
        claim = task_claim()
        _,_,resolution,_,task,_,_ = bundle(tclaim=claim, tevidence=task_support(claim, omit={"task_currentness"}))
        self.assertEqual(task["grounding_state"], "UNKNOWN")
        self.assertEqual(resolution["resolution_verdict"], "PARTIAL_UNKNOWN")

    def test_task_currentness_unknown_blocks(self):
        claim = task_claim(currentness="UNKNOWN")
        _,_,resolution,_,task,_,_ = bundle(tclaim=claim, tevidence=task_support(claim))
        ok,reasons = task_binding_eligibility(task)
        self.assertFalse(ok)
        self.assertIn("TASK_NOT_CURRENT", reasons)

    def test_task_conflict_blocks(self):
        claim = task_claim()
        _,_,resolution,_,task,_,_ = bundle(tclaim=claim, tevidence=task_support(claim, conflict_field="task_authority_basis_ref"))
        self.assertEqual(task["grounding_state"], "CONFLICT")
        self.assertEqual(resolution["resolution_verdict"], "CONFLICT")

    def test_task_superseded_blocks(self):
        claim = task_claim(supersession="SUPERSEDED")
        _,_,_,_,task,_,_ = bundle(tclaim=claim, tevidence=task_support(claim))
        ok,reasons = task_binding_eligibility(task)
        self.assertFalse(ok)
        self.assertIn("TASK_SUPERSEDED_OR_UNKNOWN", reasons)

    def test_wrong_task_identity_blocks(self):
        claim = task_claim(task_ref="TASK-WRONG")
        evidence_for_real = task_support(task_claim(task_ref="TASK-R04"))
        _,_,resolution,_,task,_,_ = bundle(tclaim=claim, tevidence=evidence_for_real)
        self.assertEqual(task["grounding_state"], "UNKNOWN")
        self.assertIn("task_ref", task["grounding_unknown_fields"])

    def test_unverified_task_authority_blocks(self):
        claim = task_claim()
        te = task_support(claim)
        for item in te:
            if item["semantic_fact_class"] == "TASK_AUTHORITY_STATE":
                item["verified_state"] = "UNVERIFIED"
        _,_,resolution,_,task,_,_ = bundle(tclaim=claim, tevidence=te)
        self.assertEqual(task["grounding_state"], "UNKNOWN")
        self.assertEqual(resolution["resolution_verdict"], "PARTIAL_UNKNOWN")

    # Valid path.
    def test_valid_exact_current_task_path(self):
        env,p,resolution,actor,task,frontier,pdep,compiled,intent,authority,admission = eligible_bundle()
        self.assertEqual(resolution["resolution_verdict"], "RESOLVED")
        self.assertEqual(task["grounding_state"], "RESOLVED")
        self.assertTrue(task_binding_eligibility(task)[0])
        self.assertIsNotNone(intent)
        self.assertEqual(admission["revalidation_verdict"], "ADMIT_EFFECT_NOW")
        out = MockEffectAdapter("MOCK", {"outcome":"SUCCESS"}).execute(intent, admission, invocation(actor,task,frontier,pdep,authority))
        self.assertEqual(out["adapter_status"], "MOCK_OBSERVATION_AVAILABLE")
        self.assertFalse(out["effect_attempted"])

    # End-to-end binding.
    def test_task_binding_flows_resolution_contract_intent_admission(self):
        env,p,resolution,actor,task,frontier,pdep,compiled,intent,authority,admission = eligible_bundle()
        self.assertEqual(compiled["task_execution_binding_id"], task["binding_id"])
        self.assertEqual(intent["task_execution_binding_id"], task["binding_id"])
        self.assertEqual(admission["task_execution_binding_id"], task["binding_id"])
        self.assertEqual(intent["task_binding_evidence_versions"], task["supporting_evidence_versions"])
        self.assertEqual(admission["task_binding_evidence_versions"], task["supporting_evidence_versions"])

    # Drift before admission.
    def test_task_authority_version_drift_before_admission_blocks(self):
        env,p,resolution,actor,task,frontier,pdep = bundle()
        compiled = ContractCompilerFacade(FakeCore()).compile(env,resolution,actor)
        intent = EffectIntentEmitter().emit(env,resolution,compiled,actor,adapter_class="MOCK",required_outcome_evidence_mode="X")
        changed_claim = task_claim()
        changed_task = TaskExecutionBindingResolver().resolve(changed_claim, task_support(changed_claim, version_overrides={"task_authority_state":"AUTH-V2"}))
        frontier2=dict(frontier)
        frontier2.update(changed_task["supporting_evidence_versions"])
        admission = PreEffectRevalidator().revalidate(
            intent,compiled,actor,current_evidence_versions=frontier2,expected_evidence_versions={},
            adapter_class="MOCK",adapter_authority=adapter_authority(),prior_effect_state="NONE",
            current_trust_policy_dependency=pdep,current_task_execution_binding=changed_task
        )
        self.assertNotEqual(admission["revalidation_verdict"], "ADMIT_EFFECT_NOW")
        self.assertTrue(any("TASK" in r or "EVIDENCE_FRONTIER" in r for r in admission["revalidation_reason_ids"]))

    # Drift after admission.
    def test_task_currentness_drift_after_admission_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        changed_claim=task_claim(currentness="UNKNOWN")
        changed_task=TaskExecutionBindingResolver().resolve(changed_claim,task_support(changed_claim))
        frontier2=dict(frontier); frontier2.update(changed_task["supporting_evidence_versions"])
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(actor,changed_task,frontier2,pdep,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("TASK" in r for r in out["reasons"]))

    def test_task_supersession_drift_after_admission_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        changed_claim=task_claim(supersession="SUPERSEDED")
        changed_task=TaskExecutionBindingResolver().resolve(changed_claim,task_support(changed_claim))
        frontier2=dict(frontier); frontier2.update(changed_task["supporting_evidence_versions"])
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(actor,changed_task,frontier2,pdep,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("TASK" in r for r in out["reasons"]))

    def test_task_evidence_version_drift_after_admission_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        claim=task_claim()
        changed_task=TaskExecutionBindingResolver().resolve(claim,task_support(claim,version_overrides={"task_currentness":"TASK-CURR-V2"}))
        frontier2=dict(frontier); frontier2.update(changed_task["supporting_evidence_versions"])
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(actor,changed_task,frontier2,pdep,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("TASK" in r or "EVIDENCE_FRONTIER" in r for r in out["reasons"]))

    # Preserve C1.
    def test_c1_policy_drift_still_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        changed=copy.deepcopy(pdep); changed["exact_version_or_blob"]="POLICY-V2"
        frontier2=dict(frontier); frontier2[pdep["evidence_id"]]="POLICY-V2"
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(actor,task,frontier2,changed,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("TRUST_POLICY" in r for r in out["reasons"]))

    # Preserve C2.
    def test_c2_mutated_intent_still_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        mutated=copy.deepcopy(intent); mutated["action_parameters"]["mode"]="MUTATED"
        out=MockEffectAdapter("MOCK",{}).execute(mutated,admission,invocation(actor,task,frontier,pdep,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("INTENT_" in r for r in out["reasons"]))

    def test_c2_mutated_admission_still_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        mutated=copy.deepcopy(admission); mutated["revalidation_reason_ids"]=["TAMPERED"]
        out=MockEffectAdapter("MOCK",{}).execute(intent,mutated,invocation(actor,task,frontier,pdep,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertIn("ADMISSION_ID_MISMATCH_AT_INVOCATION",out["reasons"])

    def test_c2_adapter_authority_drift_still_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,_,admission=eligible_bundle()
        changed=adapter_authority("AUTH-V2")
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(actor,task,frontier,pdep,changed))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("ADAPTER_AUTHORITY" in r for r in out["reasons"]))

    def test_c2_unresolved_prior_effect_still_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(actor,task,frontier,pdep,authority,prior="UNRESOLVED"))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertIn("INVOCATION_UNRESOLVED_PRIOR_EFFECT",out["reasons"])

    # Preserve actor/Recovery grounding.
    def test_actor_missing_support_still_blocks(self):
        claim=actor_claim()
        support=actor_support(claim)
        support=[e for e in support if e["semantic_fact_class"]!="CURRENT_WRITER_STATE"]
        env=RuntimeInputAdapter().normalize(raw_input(aclaim=claim,aevidence=support))
        resolution=RuntimeEvidenceResolver().resolve(env,policy())
        actor=resolution["actor_execution_binding"]
        self.assertEqual(actor["grounding_state"],"UNKNOWN")
        self.assertFalse(actor_effect_eligibility(actor,actor["effect_mutation_class"])[0])

    def test_actor_recovery_drift_still_blocks(self):
        _,_,_,actor,task,frontier,pdep,_,intent,authority,admission=eligible_bundle()
        changed_claim=actor_claim(); changed_claim["freeze_state"]="FROZEN"
        changed_actor=ActorExecutionBindingResolver().resolve(changed_claim,actor_support(changed_claim))
        frontier2=dict(frontier); frontier2.update(changed_actor["supporting_evidence_versions"])
        out=MockEffectAdapter("MOCK",{}).execute(intent,admission,invocation(changed_actor,task,frontier2,pdep,authority))
        self.assertEqual(out["adapter_status"],"NOT_EXECUTED")
        self.assertTrue(any("ACTOR" in r or "RECOVERY" in r for r in out["reasons"]))

    def test_non_live_boundary_still_no_effect(self):
        env,p,resolution,actor,task,frontier,pdep=bundle()
        compiled=ContractCompilerFacade(FakeCore()).compile(env,resolution,actor)
        intent=EffectIntentEmitter().emit(env,resolution,compiled,actor,adapter_class="NON_LIVE_EFFECT_ADAPTER",required_outcome_evidence_mode="X")
        authority=adapter_authority(); authority["adapter_class"]="NON_LIVE_EFFECT_ADAPTER"
        admission=PreEffectRevalidator().revalidate(
            intent,compiled,actor,current_evidence_versions=frontier,expected_evidence_versions={},
            adapter_class="NON_LIVE_EFFECT_ADAPTER",adapter_authority=authority,prior_effect_state="NONE",
            current_trust_policy_dependency=pdep,current_task_execution_binding=task)
        out=NonLiveEffectAdapter().execute(intent,admission,invocation(actor,task,frontier,pdep,authority))
        self.assertFalse(out["effect_attempted"])
        self.assertEqual(out["reason"],"NON_LIVE_BOUNDARY")

    def test_no_forbidden_io_imports(self):
        src=inspect.getsource(__import__("runtime_integration"))
        for forbidden in ("socket","requests","urllib","subprocess","ftplib","telnetlib"):
            self.assertNotIn("import "+forbidden,src)


if __name__ == "__main__":
    unittest.main(verbosity=2)
