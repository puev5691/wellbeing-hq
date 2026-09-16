from __future__ import annotations
import json, os, tempfile, unittest
from pathlib import Path
from verify_candidate import VerificationError, verify

BASE = Path(__file__).resolve().parent
UPSTREAM = Path(os.environ.get("TERA2_UPSTREAM_DIR", str(BASE.parent / "upstream"))).resolve()
PROFILE = json.loads((BASE / "root-profile.json").read_text())

class CandidateTests(unittest.TestCase):
    def test_positive_full_verifier(self):
        checks = verify(BASE, UPSTREAM)
        self.assertIn("mode_selector_fail_closed", checks)
        self.assertIn("full_policy_source_assignments", checks)
        self.assertIn("pinned_source_identities", checks)
        self.assertIn("declared_postpatch_identities", checks)
        self.assertIn("full_genesis_accounts_0_15", checks)

    def test_negative_fixture_mode_run_mismatch_fails_closed(self):
        with self.assertRaisesRegex(VerificationError, "node_local_common_selector_forbidden"):
            verify(BASE, UPSTREAM, node_local_file="fixtures/negative-node-mode-mismatch.json")

    def test_negative_fixture_consensus_mismatch_fails_closed(self):
        with self.assertRaisesRegex(VerificationError, "assignment_mismatch:temporal_identity.CONSENSUS_PERIOD_TIME"):
            verify(BASE, UPSTREAM, profile_file="fixtures/negative-profile-consensus-mismatch.json")

    def _mutated_profile_fails(self, mutate, expected_code):
        profile = json.loads(json.dumps(PROFILE))
        mutate(profile)
        with tempfile.TemporaryDirectory(prefix="tera2-r03-test-") as td:
            path = Path(td) / "profile.json"
            path.write_text(json.dumps(profile, indent=2) + "\n")
            with self.assertRaisesRegex(VerificationError, expected_code):
                verify(BASE, UPSTREAM, profile_file=path)

    def test_genesis_allocation_drift_fails_closed(self):
        self._mutated_profile_fails(
            lambda p: p["genesis_public_config"]["allocation"].__setitem__("accounts_1_through_15", 1),
            "genesis_zero_range_profile_mismatch",
        )

    def test_reward_policy_drift_fails_closed(self):
        self._mutated_profile_fails(
            lambda p: p["reward_mining_policy"].__setitem__("START_MINING", 17),
            "assignment_mismatch:reward_mining_policy.START_MINING",
        )

    def test_explicit_non_goals_unchanged(self):
        self.assertEqual(PROFILE["chain_identity"]["NETWORK_ID"], "WELLBEING.ROOT")
        self.assertEqual(PROFILE["temporal_identity"]["START_NETWORK_DATE"], 1800000000000)
        self.assertEqual(PROFILE["genesis_public_config"]["allocation"], {"system_account_0":1000000000,"accounts_1_through_15":0})
        self.assertEqual(PROFILE["genesis_public_config"]["smart_genesis"], "retain exact upstream built-in GenesisSmartCreate at pinned commit")
        self.assertEqual(PROFILE["reward_mining_policy"]["NEW_FORMULA_KTERA"], 3)
        self.assertEqual(PROFILE["reward_mining_policy"]["NEW_FORMULA_JINN_KTERA"], 3)

    def test_node_local_has_no_free_mode_selector(self):
        local = json.loads((BASE / "node-local.example.json").read_text())
        self.assertNotIn("MODE_RUN", local)
        self.assertEqual(local["common_profile_selector_ref"], "root-profile.json#mode_run")
        self.assertTrue(local["required_preflight"]["mode_run_from_common_profile"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
