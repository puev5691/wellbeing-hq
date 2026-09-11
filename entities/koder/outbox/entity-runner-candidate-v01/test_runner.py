import contextlib,io,os,unittest
from unittest import mock
import runner
class T(unittest.TestCase):
    def test_budget(self):
        self.assertEqual(runner.validate_budget("25"),"25")
        for v in ("0","501","-1","x"):
            with self.assertRaises(runner.RunnerError): runner.validate_budget(v)
    def test_env(self):
        with mock.patch.dict(os.environ,{"X":"secret"},clear=False): self.assertEqual(runner.required_env("X"),"secret")
        with mock.patch.dict(os.environ,{},clear=True):
            with self.assertRaises(runner.RunnerError): runner.required_env("X")
    def test_event(self):
        out=io.StringIO()
        with contextlib.redirect_stdout(out): runner.safe_event("x",session_id="sess_test",status="running")
        self.assertIn('"session_id":"sess_test"',out.getvalue())
    def test_statuses(self):
        self.assertEqual(runner.KNOWN_STATUSES,{"idle","running","rescheduling","terminated"})
if __name__=="__main__": unittest.main(verbosity=2)
