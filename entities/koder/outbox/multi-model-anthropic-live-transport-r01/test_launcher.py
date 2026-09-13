import json, os, tempfile, unittest
from unittest.mock import patch
import urllib.request

import launcher
from policy import valid_synthetic_config

class TestLauncher(unittest.TestCase):
    def setUp(self):
        self.urlopen_patch=patch.object(urllib.request,"urlopen",side_effect=AssertionError("network forbidden in tests"));self.urlopen_patch.start()
    def tearDown(self): self.urlopen_patch.stop()
    def test_default_summary_is_network_denied(self):
        plan=launcher.prepare_plan(valid_synthetic_config())
        s=launcher.default_denied_summary(plan)
        self.assertEqual(s["status"],"LIVE_DISABLED_DEFAULT_DENY");self.assertFalse(s["credential_read"]);self.assertFalse(s["external_network_used"])
    def test_prepare_plan_keeps_accepted_mock_blueprint(self):
        p=launcher.prepare_plan(valid_synthetic_config())
        self.assertFalse(p["network_execution_enabled"]);self.assertEqual(p["transport_mode"],"mock_only")
    def test_main_without_live_does_not_need_secret_or_switch(self):
        with tempfile.NamedTemporaryFile("w",encoding="utf-8",delete=False) as f:
            json.dump(valid_synthetic_config(),f); path=f.name
        try:
            with patch.dict(os.environ,{"ANTHROPIC_API_KEY":"","ANTHROPIC_LIVE_D0":""},clear=False):
                self.assertEqual(launcher.main(["--config",path]),0)
        finally: os.unlink(path)

if __name__=="__main__": unittest.main()
