from __future__ import annotations

import ast
import inspect
import textwrap

import sece_simulator as mod
from sece_simulator import source_anti_cheat_checks

def run_anti_cheat_regression_tests(source_text: str, fixtures: list[dict]) -> dict:
    base=source_anti_cheat_checks(source_text)

    fixture_binding_ids=set()
    for f in fixtures:
        bd=f["semantic_input"].get("binding_derivation_input")
        if not bd:
            continue
        st=bd["initial_state"]
        fixture_binding_ids.update(b["binding_id"] for b in st["initial_derived_bindings"])
        fixture_binding_ids.update(r["output_binding_id"] for r in st["recomputation_rules"])
    hardcoded=sorted(x for x in fixture_binding_ids if x in source_text)

    core_classes=[
        mod.ContextCorrectionEngine,
        mod.EffectiveContextBuilder,
        mod.ExecutionContractProjector,
        mod.ActionAuthorizationValidator,
        mod.RuntimeStepGuardSimulator,
        mod.ResultClassifier,
        mod.NextGateResolver,
    ]
    transformation_proxy=any("transformation_type" in inspect.getsource(cls) for cls in core_classes)

    run_source=inspect.getsource(mod.Simulator.run_fixture)
    pre_oracle=run_source.split("self.oracle.compare",1)[0]
    description_drives_execution='"description"' in pre_oracle or "['description']" in pre_oracle

    run_source=textwrap.dedent(inspect.getsource(mod.Simulator.run_fixture))
    run_tree=ast.parse(run_source)
    hidden_fixture_branches=[]
    for node in ast.walk(run_tree):
        if isinstance(node,ast.If):
            test=ast.get_source_segment(run_source,node.test) or ""
            if "fixture_id" in test:
                hidden_fixture_branches.append(test)

    return {
        "ORACLE_SEPARATION_TEST_PASS":base["ORACLE_SEPARATION_TEST_PASS"],
        "NO_FIXTURE_ID_BRANCHING_TEST_PASS":base["NO_FIXTURE_ID_BRANCHING_TEST_PASS"] and not hidden_fixture_branches,
        "NO_HIDDEN_BINDING_MAPPING_TEST_PASS":base["NO_HIDDEN_BINDING_MAPPING_TEST_PASS"] and not hardcoded,
        "NO_FIXTURE_TRANSFORMATION_PROXY_FOR_CORE_INVARIANTS":not transformation_proxy,
        "NO_PROSE_DRIVEN_EXECUTION":not description_drives_execution,
        "hardcoded_fixture_binding_ids":hardcoded,
        "fixture_id_branches":hidden_fixture_branches,
    }
