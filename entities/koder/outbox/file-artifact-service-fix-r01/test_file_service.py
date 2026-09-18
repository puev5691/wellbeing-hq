#!/usr/bin/env python3
import hashlib
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType

P = Path(__file__).resolve().parent
m = ModuleType("_fas_fix")
m.__file__ = str(P / "file_service.py")
sys.modules[m.__name__] = m
exec(compile((P / "file_service.py").read_bytes(),
             m.__file__, "exec"), m.__dict__)

def h(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

class T(unittest.TestCase):
    def fixture(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        src = root / "src"
        out = root / "out"
        src.mkdir()
        out.mkdir()
        (src / "a.txt").write_bytes(b"alpha\n")
        (src / "z.bin").write_bytes(b"\x00\x01\x02")
        req = {
            "schema": "file-artifact-service-request-r01",
            "request_id": "req-1",
            "package_id": "pkg-1",
            "inputs": [
                {"source_id": "A", "source_path": "a.txt",
                 "target_path": "docs/a.txt",
                 "sha256": h(b"alpha\n"), "size": 6},
                {"source_id": "Z", "source_path": "z.bin",
                 "target_path": "bin/z.bin",
                 "sha256": h(b"\x00\x01\x02"), "size": 3}],
            "prior_manifest_path": None,
            "create_archive": True,
            "git_adapter_enabled": False}
        return root, src, out, req

    def execute_service(self, req, src, out):
        data = (json.dumps(req, sort_keys=True) + "\n").encode()
        return m.execute(data, src, out)

    def test_deterministic_package_and_archive(self):
        root, src, out, req = self.fixture()
        first = self.execute_service(req, src, out)
        archive = (out / "package.tar.gz").read_bytes()
        manifest = (out / "package/MANIFEST.json").read_bytes()
        out2 = root / "out2"
        out2.mkdir()
        second = self.execute_service(req, src, out2)
        self.assertEqual(archive, (out2 / "package.tar.gz").read_bytes())
        self.assertEqual(manifest,
                         (out2 / "package/MANIFEST.json").read_bytes())
        self.assertEqual(first, second)
    def test_manifest_inventory_exact(self):
        _, src, out, req = self.fixture()
        self.execute_service(req, src, out)
        man = json.loads((out / "package/MANIFEST.json").read_text())
        self.assertEqual([x["path"] for x in man["files"]],
                         ["bin/z.bin", "docs/a.txt"])
        self.assertEqual(man["authority_semantics"], "none")
        self.assertEqual(man["project_state_semantics"], "none")

    def test_readback(self):
        _, src, out, req = self.fixture()
        self.execute_service(req, src, out)
        rb = json.loads((out / "readback.json").read_text())
        for item in rb["files"]:
            data = (out / "package" / item["path"]).read_bytes()
            self.assertEqual((h(data), len(data)),
                             (item["sha256"], item["size"]))

    def test_hash_mismatch_fail_closed(self):
        _, src, out, req = self.fixture()
        req["inputs"][0]["sha256"] = "0" * 64
        with self.assertRaisesRegex(m.ServiceError,
                                    "^SOURCE_HASH_MISMATCH$"):
            self.execute_service(req, src, out)

    def test_size_mismatch_fail_closed(self):
        _, src, out, req = self.fixture()
        req["inputs"][0]["size"] = 7
        with self.assertRaisesRegex(m.ServiceError,
                                    "^SOURCE_SIZE_MISMATCH$"):
            self.execute_service(req, src, out)
    def test_missing_source(self):
        _, src, out, req = self.fixture()
        req["inputs"][0]["source_path"] = "missing"
        with self.assertRaisesRegex(m.ServiceError, "^SOURCE_MISSING$"):
            self.execute_service(req, src, out)

    def test_request_schema_closed(self):
        _, src, out, req = self.fixture()
        req["authority"] = "writer"
        with self.assertRaisesRegex(m.ServiceError, "^BAD_REQUEST_SCHEMA$"):
            self.execute_service(req, src, out)

    def test_git_adapter_disabled(self):
        _, src, out, req = self.fixture()
        req["git_adapter_enabled"] = True
        with self.assertRaisesRegex(m.ServiceError,
                                    "^GIT_ADAPTER_DISABLED$"):
            self.execute_service(req, src, out)
        with self.assertRaisesRegex(m.ServiceError,
                                    "^GIT_ADAPTER_DISABLED$"):
            m.GitAdapter().publish()

    def test_reserved_manifest_target_rejected_before_write(self):
        _, src, out, req = self.fixture()
        req["inputs"] = [dict(req["inputs"][0],
                              target_path="MANIFEST.json")]
        with self.assertRaisesRegex(m.ServiceError,
                                    "^RESERVED_TARGET_PATH$"):
            self.execute_service(req, src, out)
        self.assertFalse((out / "package").exists())

    def test_reserved_manifest_dot_alias_rejected(self):
        _, src, out, req = self.fixture()
        req["inputs"] = [dict(req["inputs"][0],
                              target_path="./MANIFEST.json")]
        with self.assertRaisesRegex(m.ServiceError, "^BAD_TARGET_PATH$"):
            self.execute_service(req, src, out)
    def test_prior_manifest_parent_escape_rejected(self):
        root, src, out, req = self.fixture()
        outside = root / "outside.json"
        outside.write_text("{}")
        req["prior_manifest_path"] = "../outside.json"
        with self.assertRaisesRegex(m.ServiceError,
                                    "^BAD_PRIOR_MANIFEST_PATH$"):
            self.execute_service(req, src, out)

    def test_prior_manifest_absolute_rejected(self):
        root, src, out, req = self.fixture()
        outside = root / "outside.json"
        outside.write_text("{}")
        req["prior_manifest_path"] = str(outside)
        with self.assertRaisesRegex(m.ServiceError,
                                    "^BAD_PRIOR_MANIFEST_PATH$"):
            self.execute_service(req, src, out)

    def test_prior_manifest_symlink_escape_rejected(self):
        root, src, out, req = self.fixture()
        outside = root / "outside.json"
        outside.write_text("{}")
        (src / "linked.json").symlink_to(outside)
        req["prior_manifest_path"] = "linked.json"
        with self.assertRaisesRegex(m.ServiceError,
                                    "^BAD_PRIOR_MANIFEST_PATH$"):
            self.execute_service(req, src, out)

    def test_prior_manifest_missing(self):
        _, src, out, req = self.fixture()
        req["prior_manifest_path"] = "missing.json"
        with self.assertRaisesRegex(m.ServiceError,
                                    "^PRIOR_MANIFEST_MISSING$"):
            self.execute_service(req, src, out)

    def test_prior_manifest_type_closed(self):
        for value in (0, False, [], {}, 1.5):
            with self.subTest(value=value):
                _, src, out, req = self.fixture()
                req["prior_manifest_path"] = value
                with self.assertRaisesRegex(
                        m.ServiceError,
                        "^BAD_PRIOR_MANIFEST_PATH_TYPE$"):
                    self.execute_service(req, src, out)
    def test_create_archive_type_closed(self):
        for value in ("false", 0, 1, None, [], {}):
            with self.subTest(value=value):
                _, src, out, req = self.fixture()
                req["create_archive"] = value
                with self.assertRaisesRegex(
                        m.ServiceError,
                        "^BAD_CREATE_ARCHIVE_TYPE$"):
                    self.execute_service(req, src, out)

    def test_create_archive_false_exact_bool(self):
        _, src, out, req = self.fixture()
        req["create_archive"] = False
        result = self.execute_service(req, src, out)
        self.assertIsNone(result["archive_sha256"])
        self.assertFalse((out / "package.tar.gz").exists())

    def test_diff(self):
        _, src, out, req = self.fixture()
        prior = {"schema": "file-artifact-manifest-r01",
                 "package_id": "old",
                 "files": [
                     {"path": "docs/a.txt", "sha256": h(b"alpha\n"),
                      "size": 6, "source_id": "A"},
                     {"path": "gone.txt", "sha256": h(b"x"),
                      "size": 1, "source_id": "X"}]}
        (src / "prior.json").write_text(json.dumps(prior))
        req["prior_manifest_path"] = "prior.json"
        result = self.execute_service(req, src, out)
        self.assertEqual(result["diff"]["unchanged"], ["docs/a.txt"])
        self.assertEqual(result["diff"]["added"], ["bin/z.bin"])
        self.assertEqual(result["diff"]["removed"], ["gone.txt"])
    def test_compact_result_no_paths_or_content(self):
        _, src, out, req = self.fixture()
        result = self.execute_service(req, src, out)
        raw = json.dumps(result)
        self.assertNotIn(str(src), raw)
        self.assertNotIn("alpha", raw)
        self.assertEqual(result["git_adapter"], "disabled")

    def test_zero_network(self):
        _, src, out, req = self.fixture()
        old = socket.socket
        def deny(*_args, **_kwargs):
            raise AssertionError("NETWORK")
        socket.socket = deny
        try:
            self.execute_service(req, src, out)
        finally:
            socket.socket = old

    def test_no_subprocess_needed(self):
        _, src, out, req = self.fixture()
        old = subprocess.Popen
        def deny(*_args, **_kwargs):
            raise AssertionError("PROCESS")
        subprocess.Popen = deny
        try:
            self.execute_service(req, src, out)
        finally:
            subprocess.Popen = old

if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(T))
    print(json.dumps({
        "verdict": m.PASS if result.wasSuccessful()
                   else "FAIL_FILE_ARTIFACT_SERVICE_FIX_TESTS",
        "tests": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "skipped": len(result.skipped),
        "network_calls": 0,
        "git_publications": 0,
        "credentials": 0,
        "authority_semantics": "none",
        "project_state_semantics": "none"}, sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)