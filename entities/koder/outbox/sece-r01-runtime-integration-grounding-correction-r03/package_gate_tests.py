from __future__ import annotations
import hashlib
import importlib
from pathlib import Path

EXPECTED_CORE_SHA256 = "7f254b1df1f0160680caf13e9dd99f0cc7ed93e9944cd4d4ec9d584f7e6c1fed"
REQUIRED_CORE_SYMBOLS = [
    "SemanticAtomLoader", "ContextComposer", "CollisionDetector", "ContextCorrectionEngine",
    "DependencyScopeResolver", "EffectiveContextBuilder", "ExecutionContractProjector",
    "ActionAuthorizationValidator", "CausalEventValidator", "CurrentStateEvidenceResolver",
    "StaticValidator", "MultiOutcomeAggregator", "ResultClassifier", "ContextDeltaBuilder",
    "SuccessorContextBuilder", "NextGateResolver", "HumanCausalRenderer", "TraceRecorder",
    "digest", "contract_id", "CONTEXT_DOMAIN",
]

def main() -> int:
    root = Path(__file__).resolve().parent
    core_path = root / "sece_simulator.py"
    got = hashlib.sha256(core_path.read_bytes()).hexdigest()
    assert got == EXPECTED_CORE_SHA256, (got, EXPECTED_CORE_SHA256)
    core = importlib.import_module("sece_simulator")
    missing = [name for name in REQUIRED_CORE_SYMBOLS if not hasattr(core, name)]
    assert not missing, missing
    from runtime_integration import ReviewedSeceCoreAdapter
    adapter = ReviewedSeceCoreAdapter(core)
    assert adapter.core is core
    print("BASELINE_CORE_SHA256_MATCH=YES")
    print("REVIEWED_CORE_INTERFACE_BINDING_PASS=YES")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
