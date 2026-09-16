import json, unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PROFILE = json.loads((BASE / "root-profile.json").read_text())
PATCH = (BASE / "WBN_ROOT_PROFILE.patch").read_text()


class CandidateTests(unittest.TestCase):
    def test_root_identity(self):
        c = PROFILE["chain_identity"]
        self.assertEqual(c["NETWORK_ID"], "WELLBEING.ROOT")
        self.assertFalse(c["DATA_shard_js_required"])

    def test_fixed_temporal_identity(self):
        t = PROFILE["temporal_identity"]
        self.assertEqual(t["START_NETWORK_DATE"], 1800000000000)
        self.assertEqual(t["CONSENSUS_PERIOD_TIME"], 3000)

    def test_genesis_allocation(self):
        g = PROFILE["genesis_public_config"]
        self.assertEqual(g["TOTAL_SUPPLY_TERA"], 1000000000)
        self.assertEqual(g["allocation"]["system_account_0"], 1000000000)
        self.assertEqual(g["preallocated_founder_balance"], 0)
        self.assertEqual(g["preallocated_developer_balance"], 0)

    def test_reward_starts_after_genesis_blocks(self):
        self.assertEqual(PROFILE["reward_mining_policy"]["START_MINING"], 16)
        self.assertIn("global.START_MINING = 16", PATCH)

    def test_runtime_boundaries(self):
        b = PROFILE["candidate_boundaries"]
        self.assertFalse(b["runtime_launch"])
        self.assertFalse(b["node_start"])
        self.assertFalse(b["genesis_execution"])
        self.assertFalse(b["existing_DATA_DB_mutation"])
        self.assertFalse(b["credentials"])

    def test_no_shard_profile_or_runtime_mining_enable(self):
        self.assertNotIn("DATA/shard.js", PATCH)
        self.assertNotIn("global.USE_MINING = 1", PATCH)


if __name__ == "__main__":
    unittest.main(verbosity=2)
