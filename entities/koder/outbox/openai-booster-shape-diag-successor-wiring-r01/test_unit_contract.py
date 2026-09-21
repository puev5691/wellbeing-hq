import shlex,unittest
from pathlib import Path

UNIT=Path(__file__).with_name("wellbeing-openai-booster-shape-diag-successor.service.candidate")
RUNTIME="/opt/wellbeing/openai-booster-shape-diag-successor-r01"
STATE="/var/lib/wellbeing/openai-booster-live-child-r01"

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text=UNIT.read_text()
        cls.lines=[x.strip() for x in cls.text.splitlines() if x.strip() and not x.startswith("#")]

    def test_oneshot_disabled_by_default_contract(self):
        self.assertIn("Type=oneshot",self.lines)
        self.assertIn("WantedBy=multi-user.target",self.lines)
        self.assertNotIn("Restart=always",self.lines)
        self.assertNotIn("Restart=on-failure",self.lines)

    def test_exact_credential_mapping_and_write_boundary(self):
        self.assertIn("LoadCredentialEncrypted=openai-wellbeing-entity-boosters-restricted:/etc/credstore.encrypted/openai-wellbeing-entity-boosters-restricted.cred",self.lines)
        self.assertIn("ReadWritePaths="+STATE,self.lines)

    def test_execstart_exact_successor_wiring(self):
        line=next(x for x in self.lines if x.startswith("ExecStart="))
        argv=shlex.split(line[len("ExecStart="):])
        expected=[
          "/usr/bin/python3","-I","-B",RUNTIME+"/shape_diag_successor_runner.py",
          "--worker","/opt/wellbeing/openai-booster-live-child-r01/live_worker.py",
          "--diag-integration",RUNTIME+"/diagnostic_reviewable_live_worker.py",
          "--result-integration",RUNTIME+"/reviewable_live_worker.py",
          "--result-store",RUNTIME+"/review_result_store.py",
          "--shape-store",RUNTIME+"/response_shape_store.py",
          "--invocation",STATE+"/invocation.json",
          "--ledger",STATE+"/ledger.sqlite",
          "--shape-dir",STATE+"/response-shapes",
          "--result-dir",STATE+"/review-results"
        ]
        self.assertEqual(argv,expected)

    def test_no_listener_or_credential_environment(self):
        low=self.text.lower()
        self.assertNotIn("listenstream=",low)
        self.assertNotIn("socket",low)
        self.assertNotIn("environment=openai",low)
        self.assertNotIn("environmentfile=",low)

if __name__=="__main__": unittest.main(verbosity=2)
