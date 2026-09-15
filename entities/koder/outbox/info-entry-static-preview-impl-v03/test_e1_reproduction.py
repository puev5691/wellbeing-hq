from __future__ import annotations
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class TestE1ReportReproduction(unittest.TestCase):
    def test_committed_report_reproduces_byte_for_byte(self):
        source = Path(__file__).resolve().parent
        committed = (source / "readback-report.json").read_bytes()

        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            for name in (
                "static_preview_core.py",
                "static_preview.py",
                "post_build_readback.py",
                "schema-v01.json",
            ):
                shutil.copy2(source / name, base / name)
            shutil.copytree(source / "fixtures", base / "fixtures")

            code = (
                "from pathlib import Path; "
                "from static_preview import build; "
                "from post_build_readback import verify; "
                "b=Path('.').resolve(); "
                "s=build(b,True); i=s['expected_preview_identity']; "
                "verify(b,i['git_blob'],i['sha256'],True)"
            )
            subprocess.run(
                [sys.executable, "-c", code],
                cwd=base,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            reproduced = (base / "readback-report.json").read_bytes()
            self.assertEqual(reproduced, committed)


if __name__ == "__main__":
    unittest.main()
