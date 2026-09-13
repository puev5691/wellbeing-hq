from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from typing import Any, Mapping

PILOT_VERSION = "multi-model-gateway-mock-r01"
DATA_CLASS = "D0_SYNTHETIC"
AUTHOR_PROVIDER_MODEL = "mock-provider-a/mock-model-author-v1"
VERIFIER_PROVIDER_MODEL = "mock-provider-b/mock-model-verifier-v1"
KNOWN_PROVIDER_MODELS = frozenset({AUTHOR_PROVIDER_MODEL, VERIFIER_PROVIDER_MODEL})
AUTHOR_ADAPTER = "local-fake-author-adapter/r01"
VERIFIER_ADAPTER = "local-fake-verifier-adapter/r01"
POLICY_DECISION = "PASS_D0_LOCAL_SYNTHETIC_ONLY"


class PolicyViolation(ValueError):
    pass


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_text(canonical_json(value))


_CREDENTIAL_KEY = re.compile(
    r"(^|[_-])(api[_-]?key|token|secret|password|passwd|private[_-]?key|bearer|cookie|credential|session)([_-]|$)",
    re.IGNORECASE,
)
_CREDENTIAL_VALUE_PATTERNS = (
    re.compile(r"^sk-[A-Za-z0-9_-]{8,}$"),
    re.compile(r"^Bearer\s+\S+", re.IGNORECASE),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(?:api[_-]?key|token|secret|password)\s*[:=]\s*\S+"),
)
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_SAFE_TASK_ID = re.compile(r"^syn-[a-z0-9][a-z0-9._-]{2,63}$")


def _walk(value: Any, path: str = "$"):
    if isinstance(value, Mapping):
        for key, child in value.items():
            yield f"{path}.{key}", key
            yield from _walk(child, f"{path}.{key}")
    elif isinstance(value, (list, tuple)):
        for idx, child in enumerate(value):
            yield from _walk(child, f"{path}[{idx}]")
    else:
        yield path, value


def _reject_credential_like(value: Any) -> None:
    for path, item in _walk(value):
        if path.rsplit(".", 1)[-1] and isinstance(item, str):
            if path != "$" and _CREDENTIAL_KEY.search(path.rsplit(".", 1)[-1]):
                raise PolicyViolation("credential_like_field_forbidden")
            if any(pattern.search(item) for pattern in _CREDENTIAL_VALUE_PATTERNS):
                raise PolicyViolation("credential_like_value_forbidden")


def _require_exact_false(envelope: Mapping[str, Any], field: str) -> None:
    if envelope.get(field) is not False:
        raise PolicyViolation(f"{field}_must_be_false")


def _require_synthetic_locator(locator: Any) -> str:
    if not isinstance(locator, str) or not locator:
        raise PolicyViolation("invalid_input_locator")
    if not (locator.startswith("synthetic://") or locator.startswith("fixture://")):
        raise PolicyViolation("non_synthetic_locator_forbidden")
    lowered = locator.lower()
    if "github.com" in lowered or "http://" in lowered or "https://" in lowered or "file:///" in lowered:
        raise PolicyViolation("external_or_project_locator_forbidden")
    return locator


@dataclass(frozen=True)
class GuardDecision:
    decision: str
    normalized_envelope: dict[str, Any]


class PolicyGuard:
    required_fields = frozenset({
        "task_id",
        "task_class",
        "data_class",
        "input_locators",
        "synthetic_payload_hash",
        "requested_role",
        "allowed_provider_models",
        "author_provider_model",
        "verifier_provider_model",
        "max_cost_usd",
        "external_tools_allowed",
        "network_allowed",
        "project_mutation_allowed",
        "fallback_allowed",
    })

    def evaluate(self, envelope: Mapping[str, Any]) -> GuardDecision:
        if not isinstance(envelope, Mapping):
            raise PolicyViolation("task_envelope_must_be_object")
        _reject_credential_like(envelope)
        unknown_fields = set(envelope) - self.required_fields
        missing_fields = self.required_fields - set(envelope)
        if missing_fields:
            raise PolicyViolation("missing_fields:" + ",".join(sorted(missing_fields)))
        if unknown_fields:
            raise PolicyViolation("unknown_fields:" + ",".join(sorted(unknown_fields)))

        task_id = envelope["task_id"]
        if not isinstance(task_id, str) or not _SAFE_TASK_ID.fullmatch(task_id):
            raise PolicyViolation("synthetic_task_id_required")
        if envelope["task_class"] not in {"L", "M"}:
            raise PolicyViolation("pilot_task_class_must_be_L_or_M")
        if envelope["data_class"] != DATA_CLASS:
            raise PolicyViolation("data_class_must_be_D0_SYNTHETIC")
        if envelope["requested_role"] != "author":
            raise PolicyViolation("pipeline_entry_role_must_be_author")

        locators = envelope["input_locators"]
        if not isinstance(locators, list) or not locators:
            raise PolicyViolation("input_locators_nonempty_list_required")
        normalized_locators = [_require_synthetic_locator(x) for x in locators]

        payload_hash = envelope["synthetic_payload_hash"]
        if not isinstance(payload_hash, str) or not _HEX64.fullmatch(payload_hash):
            raise PolicyViolation("synthetic_payload_hash_sha256_required")

        allowed = envelope["allowed_provider_models"]
        if not isinstance(allowed, list) or len(allowed) != 2 or len(set(allowed)) != 2:
            raise PolicyViolation("exact_two_provider_models_required")
        if set(allowed) != KNOWN_PROVIDER_MODELS:
            raise PolicyViolation("unknown_or_incomplete_provider_model_allowlist")

        author = envelope["author_provider_model"]
        verifier = envelope["verifier_provider_model"]
        if author != AUTHOR_PROVIDER_MODEL:
            raise PolicyViolation("unknown_author_provider_model")
        if verifier != VERIFIER_PROVIDER_MODEL:
            raise PolicyViolation("unknown_verifier_provider_model")
        if author == verifier or author.split("/", 1)[0] == verifier.split("/", 1)[0]:
            raise PolicyViolation("author_verifier_provider_independence_required")

        if envelope["max_cost_usd"] != 0:
            raise PolicyViolation("max_cost_usd_must_be_zero")
        _require_exact_false(envelope, "external_tools_allowed")
        _require_exact_false(envelope, "network_allowed")
        _require_exact_false(envelope, "project_mutation_allowed")
        _require_exact_false(envelope, "fallback_allowed")

        normalized = {
            "task_id": task_id,
            "task_class": envelope["task_class"],
            "data_class": DATA_CLASS,
            "input_locators": normalized_locators,
            "synthetic_payload_hash": payload_hash,
            "requested_role": "author",
            "allowed_provider_models": sorted(allowed),
            "author_provider_model": AUTHOR_PROVIDER_MODEL,
            "verifier_provider_model": VERIFIER_PROVIDER_MODEL,
            "max_cost_usd": 0,
            "external_tools_allowed": False,
            "network_allowed": False,
            "project_mutation_allowed": False,
            "fallback_allowed": False,
        }
        return GuardDecision(POLICY_DECISION, normalized)


class FakeAuthorProvider:
    provider_model = AUTHOR_PROVIDER_MODEL
    adapter_identity = AUTHOR_ADAPTER
    role = "author"

    def run(self, envelope: Mapping[str, Any]) -> dict[str, Any]:
        payload_hash = envelope["synthetic_payload_hash"]
        result = {
            "result_type": "local_mock_candidate_result",
            "role": self.role,
            "provider_model": self.provider_model,
            "adapter_identity": self.adapter_identity,
            "task_id": envelope["task_id"],
            "candidate_status": "CANDIDATE_REQUIRES_KOO_REVIEW",
            "structured_candidate": {
                "synthetic_digest_prefix": payload_hash[:16],
                "task_class": envelope["task_class"],
                "transformation": "deterministic-local-author-r01",
            },
            "cost_usd": 0,
            "external_network_used": False,
        }
        result["output_hash"] = sha256_json(result)
        return result


class FakeVerifierProvider:
    provider_model = VERIFIER_PROVIDER_MODEL
    role = "verifier"

    def __init__(self, mode: str = "agree"):
        if mode not in {"agree", "disagree"}:
            raise ValueError("verifier_mode_must_be_agree_or_disagree")
        self.mode = mode
        self.adapter_identity = f"{VERIFIER_ADAPTER}:{mode}"

    def verify(self, envelope: Mapping[str, Any], author_result: Mapping[str, Any]) -> dict[str, Any]:
        expected_prefix = envelope["synthetic_payload_hash"][:16]
        author_prefix = author_result["structured_candidate"]["synthetic_digest_prefix"]
        deterministic_match = author_prefix == expected_prefix
        agreement = deterministic_match and self.mode == "agree"
        result = {
            "result_type": "local_mock_verifier_result",
            "role": self.role,
            "provider_model": self.provider_model,
            "adapter_identity": self.adapter_identity,
            "task_id": envelope["task_id"],
            "agreement": agreement,
            "reason_code": "MATCHED_SYNTHETIC_RUBRIC" if agreement else "SYNTHETIC_DISAGREEMENT_RETAINED",
            "author_output_hash": author_result["output_hash"],
            "cost_usd": 0,
            "external_network_used": False,
        }
        result["output_hash"] = sha256_json(result)
        return result


class MultiModelGatewayMock:
    def __init__(self, verifier_mode: str = "agree"):
        self.guard = PolicyGuard()
        self.author = FakeAuthorProvider()
        self.verifier = FakeVerifierProvider(verifier_mode)

    def run(self, envelope: Mapping[str, Any]) -> dict[str, Any]:
        guard = self.guard.evaluate(envelope)
        normalized = guard.normalized_envelope
        author_result = self.author.run(normalized)
        verifier_result = self.verifier.verify(normalized, author_result)
        final_status = (
            "VERIFIED_CANDIDATE_REQUIRES_KOO"
            if verifier_result["agreement"]
            else "DISAGREEMENT_REQUIRES_KOO"
        )
        reconciliation = {
            "author_output_hash": author_result["output_hash"],
            "verifier_output_hash": verifier_result["output_hash"],
            "verifier_agreement": verifier_result["agreement"],
            "final_candidate_status": final_status,
            "project_acceptance": "NOT_GRANTED",
            "automatic_merge": False,
            "project_mutation_performed": False,
        }
        reconciliation_hash = sha256_json(reconciliation)
        run_seed = {
            "pilot_version": PILOT_VERSION,
            "envelope": normalized,
            "author_adapter": self.author.adapter_identity,
            "verifier_adapter": self.verifier.adapter_identity,
        }
        gateway_run_id = "mmg-r01-" + sha256_json(run_seed)[:24]
        provenance = {
            "gateway_run_id": gateway_run_id,
            "task_id": normalized["task_id"],
            "task_class": normalized["task_class"],
            "data_sensitivity_class": normalized["data_class"],
            "input_locators": normalized["input_locators"],
            "synthetic_payload_hash": normalized["synthetic_payload_hash"],
            "policy_decision": guard.decision,
            "gateway_implementation_version": PILOT_VERSION,
            "author": {
                "provider_model": self.author.provider_model,
                "adapter_identity": self.author.adapter_identity,
                "role": self.author.role,
                "output_hash": author_result["output_hash"],
            },
            "verifier": {
                "provider_model": self.verifier.provider_model,
                "adapter_identity": self.verifier.adapter_identity,
                "role": self.verifier.role,
                "output_hash": verifier_result["output_hash"],
                "agreement": verifier_result["agreement"],
            },
            "reconciliation_hash": reconciliation_hash,
            "verifier_agreement": verifier_result["agreement"],
            "final_candidate_status": final_status,
            "cost_usd": 0,
            "external_network_used": False,
            "external_tools_used": False,
            "fallback_used": False,
            "project_mutation_performed": False,
            "project_acceptance": "NOT_GRANTED",
        }
        provenance_hash = sha256_json(provenance)
        result = {
            "gateway_run_id": gateway_run_id,
            "author_result": author_result,
            "verifier_result": verifier_result,
            "reconciliation": reconciliation,
            "provenance": provenance,
            "provenance_hash": provenance_hash,
        }
        result["result_identity"] = sha256_json(result)
        return result


def valid_synthetic_envelope(payload_hash: str) -> dict[str, Any]:
    return {
        "task_id": "syn-demo-001",
        "task_class": "L",
        "data_class": "D0_SYNTHETIC",
        "input_locators": ["fixture://synthetic-payload-v1"],
        "synthetic_payload_hash": payload_hash,
        "requested_role": "author",
        "allowed_provider_models": [AUTHOR_PROVIDER_MODEL, VERIFIER_PROVIDER_MODEL],
        "author_provider_model": AUTHOR_PROVIDER_MODEL,
        "verifier_provider_model": VERIFIER_PROVIDER_MODEL,
        "max_cost_usd": 0,
        "external_tools_allowed": False,
        "network_allowed": False,
        "project_mutation_allowed": False,
        "fallback_allowed": False,
    }
