import unittest
from policy import *

class PolicyTests(unittest.TestCase):
    def test_valid(self):
        g=PolicyGuard().evaluate(valid_synthetic_config())
        self.assertEqual(g.decision,"PASS_D0_SYNTHETIC_MOCK_ONLY")
        self.assertEqual(g.normalized["model"],MODEL)
        self.assertFalse(g.normalized["network_allowed"])

    def test_non_d0_rejected(self):
        c=valid_synthetic_config(); c["data_class"]="D1_PROJECT"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_wrong_model_rejected(self):
        c=valid_synthetic_config(); c["model"]="gpt-other"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_project_locator_rejected(self):
        c=valid_synthetic_config(); c["input_locator"]="https://github.com/puev5691/wellbeing-hq/x"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_project_text_rejected(self):
        c=valid_synthetic_config("read entities/koder/private")
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_credential_field_rejected(self):
        c=valid_synthetic_config(); c["api_key"]="x"
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_credential_value_rejected(self):
        c=valid_synthetic_config(("s"+"k-")+("a"*16))
        with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

    def test_restricted_flags_rejected(self):
        for field in ("tools_allowed","web_search_allowed","file_search_allowed","computer_use_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed"):
            c=valid_synthetic_config(); c[field]=True
            with self.subTest(field=field):
                with self.assertRaises(PolicyViolation): PolicyGuard().evaluate(c)

if __name__=="__main__": unittest.main(verbosity=2)