import unittest
from policy import *

class PolicyTests(unittest.TestCase):
    def test_valid(self):
        g=PolicyGuard().evaluate(valid_synthetic_config("gpt-5.6-luna"))
        self.assertEqual(g.decision,"PASS_D0_SYNTHETIC_MOCK_ONLY")
        self.assertEqual(g.normalized["model"],"gpt-5.6-luna")
        self.assertFalse(g.normalized["network_allowed"])


    def test_exact_four_model_allowlist(self):
        self.assertEqual(MODELS,frozenset({"gpt-5.6-luna","gpt-5.6-terra","gpt-5.6-sol","gpt-6-astra"}))
        for model in sorted(MODELS):
            with self.subTest(model=model):
                g=PolicyGuard().evaluate(valid_synthetic_config(model))
                self.assertEqual(g.normalized["model"],model)

    def test_non_d0_rejected(self):
        c=valid_synthetic_config("gpt-5.6-luna"); c["data_class"]="D1_PROJECT"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_wrong_model_rejected(self):
        c=valid_synthetic_config("gpt-5.6-luna"); c["model"]="gpt-other"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_project_locator_rejected(self):
        c=valid_synthetic_config("gpt-5.6-luna"); c["input_locator"]="https://github.com/puev5691/wellbeing-hq/x"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_project_text_rejected(self):
        c=valid_synthetic_config("gpt-5.6-luna","read entities/koder/private")
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_credential_field_rejected(self):
        c=valid_synthetic_config("gpt-5.6-luna"); c["api_key"]="x"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_credential_value_rejected(self):
        c=valid_synthetic_config("gpt-5.6-luna",("s"+"k-")+("a"*16))
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_restricted_flags_rejected(self):
        for field in ("tools_allowed","web_search_allowed","file_search_allowed","computer_use_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed"):
            c=valid_synthetic_config("gpt-5.6-luna"); c[field]=True
            with self.subTest(field=field):
                with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

if __name__=="__main__": unittest.main(verbosity=2)
