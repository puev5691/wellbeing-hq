import tempfile, unittest
from pathlib import Path
from cleanup_sandbox import cleanup_db, CONFIRMATION

class CleanupTests(unittest.TestCase):
    def test_cleanup_exact_path_only(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'gateway.sqlite3'; p.write_bytes(b'test')
            self.assertTrue(cleanup_db(str(p),CONFIRMATION,allowed_path=p))
            self.assertFalse(p.exists())
    def test_cleanup_requires_confirmation(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'gateway.sqlite3'; p.write_bytes(b'test')
            with self.assertRaises(ValueError): cleanup_db(str(p),'NO',allowed_path=p)
            self.assertTrue(p.exists())
    def test_cleanup_rejects_other_path(self):
        with tempfile.TemporaryDirectory() as td:
            allowed=Path(td)/'gateway.sqlite3'; other=Path(td)/'other.sqlite3'; other.write_bytes(b'test')
            with self.assertRaises(ValueError): cleanup_db(str(other),CONFIRMATION,allowed_path=allowed)
            self.assertTrue(other.exists())

if __name__=='__main__':
    unittest.main(verbosity=2)
