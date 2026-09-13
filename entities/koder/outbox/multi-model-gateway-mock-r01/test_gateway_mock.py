import ast
import copy
import hashlib
import json
from pathlib import Path
import unittest

from gateway_mock import (
    AUTHOR_PROVIDER_MODEL,
    VERIFIER_PROVIDER_MODEL,
    MultiModelGatewayMock,
    PolicyViolation,
    canonical_json,
    sha256_json,
    valid_synthetic_envelope,
)

FIXTURE_PAYLOAD = "D0_SYNTHETIC fixture alpha r01\n"
FIXTURE_HASH = hashlib.sha256(FIXTURE_PAYLOAD.encode("utf-8")).hexdigest()


def envelope():
    return valid_synthetic_envelope(FIXTURE_HASH)


class GatewayMockTests(unittest.TestCase):
    def test_01_valid_d0_author_verifier_pass(self):
        result = MultiModelGatewayMock().run(envelope())
        self.assertTrue(result["verifier_result"]["agreement"])
        self.assertEqual(result["reconciliation"]["final_candidate_status"], "VERIFIED_CANDIDATE_REQUIRES_KOO")
        self.assertEqual(result["reconciliation"]["project_acceptance"], "NOT_GRANTED")

    def test_02_disagreement_retained_not_overwritten(self):
        result = MultiModelGatewayMock(verifier_mode="disagree").run(envelope())
        self.assertFalse(result["verifier_result"]["agreement"])
        self.assertEqual(result["reconciliation"]["final_candidate_status"], "DISAGREEMENT_REQUIRES_KOO")
        self.assertFalse(result["reconciliation"]["automatic_merge"])
        self.assertEqual(result["provenance"]["final_candidate_status"], "DISAGREEMENT_REQUIRES_KOO")

    def test_03_d2_d5_d6_d7_fail_closed(self):
        for data_class in ("D2_INTERNAL_LOW", "D5_PERSONAL", "D6_SECURITY_SENSITIVE", "D7_SECRETS"):
            with self.subTest(data_class=data_class):
                e = envelope(); e["data_class"] = data_class
                with self.assertRaisesRegex(PolicyViolation, "data_class_must_be_D0_SYNTHETIC"):
                    MultiModelGatewayMock().run(e)

    def test_04_other_non_d0_classes_fail_closed_too(self):
        for data_class in ("D1_PUBLIC", "D3_UNRELEASED_GOV", "D4_PROPRIETARY_TECH", "D8_THIRD_PARTY_RESTRICTED", "D9_RAW_LOGS_USER_CONTENT"):
            e = envelope(); e["data_class"] = data_class
            with self.assertRaises(PolicyViolation): MultiModelGatewayMock().run(e)

    def test_05_credential_like_field_fails_closed(self):
        e = envelope(); e["api_key"] = "synthetic-placeholder"
        with self.assertRaisesRegex(PolicyViolation, "credential_like_field_forbidden"):
            MultiModelGatewayMock().run(e)

    def test_06_credential_like_value_fails_closed(self):
        e = envelope(); e["task_id"] = "sk-THISLOOKSLIKEACREDENTIAL123"
        with self.assertRaisesRegex(PolicyViolation, "credential_like_value_forbidden"):
            MultiModelGatewayMock().run(e)

    def test_07_unknown_provider_or_model_fails_closed(self):
        e = envelope(); e["author_provider_model"] = "unknown-provider/unknown-model"
        with self.assertRaisesRegex(PolicyViolation, "unknown_author_provider_model"):
            MultiModelGatewayMock().run(e)
        e = envelope(); e["allowed_provider_models"] = [AUTHOR_PROVIDER_MODEL, "unknown-provider/model"]
        with self.assertRaisesRegex(PolicyViolation, "unknown_or_incomplete_provider_model_allowlist"):
            MultiModelGatewayMock().run(e)

    def test_08_fallback_fails_closed(self):
        e = envelope(); e["fallback_allowed"] = True
        with self.assertRaisesRegex(PolicyViolation, "fallback_allowed_must_be_false"):
            MultiModelGatewayMock().run(e)

    def test_09_external_tools_and_network_fail_closed(self):
        for field in ("external_tools_allowed", "network_allowed"):
            with self.subTest(field=field):
                e = envelope(); e[field] = True
                with self.assertRaises(PolicyViolation): MultiModelGatewayMock().run(e)

    def test_10_project_mutation_fails_closed(self):
        e = envelope(); e["project_mutation_allowed"] = True
        with self.assertRaisesRegex(PolicyViolation, "project_mutation_allowed_must_be_false"):
            MultiModelGatewayMock().run(e)

    def test_11_non_synthetic_locator_fails_closed(self):
        e = envelope(); e["input_locators"] = ["https://github.com/puev5691/wellbeing-hq"]
        with self.assertRaises(PolicyViolation): MultiModelGatewayMock().run(e)

    def test_12_nonzero_cost_fails_closed(self):
        e = envelope(); e["max_cost_usd"] = 0.01
        with self.assertRaisesRegex(PolicyViolation, "max_cost_usd_must_be_zero"):
            MultiModelGatewayMock().run(e)

    def test_13_provenance_complete_and_hash_valid(self):
        result = MultiModelGatewayMock().run(envelope())
        p = result["provenance"]
        required = {
            "gateway_run_id", "task_id", "task_class", "data_sensitivity_class", "input_locators",
            "synthetic_payload_hash", "policy_decision", "gateway_implementation_version", "author", "verifier",
            "reconciliation_hash", "verifier_agreement", "final_candidate_status", "cost_usd",
            "external_network_used", "external_tools_used", "fallback_used", "project_mutation_performed", "project_acceptance"
        }
        self.assertEqual(set(p), required)
        self.assertEqual(result["provenance_hash"], sha256_json(p))
        copy_result = copy.deepcopy(result); identity = copy_result.pop("result_identity")
        self.assertEqual(identity, sha256_json(copy_result))

    def test_14_outputs_cannot_self_accept_or_be_current_canon(self):
        result = MultiModelGatewayMock().run(envelope())
        text = canonical_json(result).lower()
        forbidden_values = ('"project_acceptance":"accepted"', '"candidate_status":"current"', '"candidate_status":"canon"')
        for marker in forbidden_values: self.assertNotIn(marker, text)
        self.assertEqual(result["reconciliation"]["project_acceptance"], "NOT_GRANTED")
        self.assertFalse(result["reconciliation"]["project_mutation_performed"])

    def test_15_reproducible_identity_same_input_same_adapter_version(self):
        first = MultiModelGatewayMock().run(envelope())
        second = MultiModelGatewayMock().run(envelope())
        self.assertEqual(first["gateway_run_id"], second["gateway_run_id"])
        self.assertEqual(first["result_identity"], second["result_identity"])
        self.assertEqual(first, second)

    def test_16_author_and_verifier_are_independent_fake_providers(self):
        result = MultiModelGatewayMock().run(envelope())
        author = result["provenance"]["author"]["provider_model"]
        verifier = result["provenance"]["verifier"]["provider_model"]
        self.assertEqual(author, AUTHOR_PROVIDER_MODEL)
        self.assertEqual(verifier, VERIFIER_PROVIDER_MODEL)
        self.assertNotEqual(author.split("/", 1)[0], verifier.split("/", 1)[0])

    def test_17_no_network_provider_sdk_or_connector_imports(self):
        source = Path(__file__).with_name("gateway_mock.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import): imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom): imported.add(node.module or "")
        forbidden = {
            "socket", "requests", "urllib", "urllib.request", "http", "http.client", "aiohttp", "httpx",
            "openai", "anthropic", "google", "boto3", "botocore", "litellm", "mcp"
        }
        self.assertTrue(imported.isdisjoint(forbidden), imported & forbidden)

    def test_18_synthetic_payload_hash_roundtrip(self):
        payload = FIXTURE_PAYLOAD
        e = envelope()
        self.assertEqual(hashlib.sha256(payload.encode("utf-8")).hexdigest(), e["synthetic_payload_hash"])
        result = MultiModelGatewayMock().run(e)
        self.assertEqual(result["provenance"]["data_sensitivity_class"], "D0_SYNTHETIC")



if __name__ == "__main__":
    unittest.main(verbosity=2)
