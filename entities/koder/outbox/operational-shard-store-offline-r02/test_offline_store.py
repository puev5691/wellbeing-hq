#!/usr/bin/env python3
import concurrent.futures
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from offline_store import (OfflineStore, StoreError, SyntheticAdmission, canonical,
                           namespace, parse, sha, validate_record)

HERE = Path(__file__).resolve().parent
NS = ("KOD", "TASK-001", "repo@commit:path#blob", "main")


def admission(epoch=1, writer="writer-a", **changes):
    data = dict(zip(("entity_id", "task_id", "task_version", "stream_id"), NS))
    data.update(writer_id=writer, writer_epoch=epoch, authority_ref="synthetic-authority",
                trust_profile_ref="synthetic-profile", approved_sources_ref="synthetic-sources",
                admitted=True)
    data.update(changes)
    return SyntheticAdmission(**data)


def make_record(generation=1, parent=None, epoch=1, writer="writer-a", payload=b"step\n", **changes):
    obj = dict(schema="operational-record-v1", record_kind="STEP_EVIDENCE",
               entity_id=NS[0], task_id=NS[1], task_version=NS[2], stream_id=NS[3],
               writer_id=writer, writer_epoch=epoch, authority_ref="synthetic-authority",
               trust_profile_ref="synthetic-profile", approved_sources_ref="synthetic-sources",
               generation=generation, parent_digest=parent, payload_sha256=sha(payload),
               payload_bytes=len(payload), payload_media_type="text/plain",
               state_class="PROVISIONAL", source_refs=[], supersedes_refs=[],
               policy_ref="UNDECIDED", expiry_class="UNKNOWN")
    obj.update(changes)
    return canonical(obj), payload


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="operational-store-synthetic-")
        self.addCleanup(self.tmp.cleanup)
        self.sandbox = Path(self.tmp.name)
        (self.sandbox / ".offline-synthetic-root").write_bytes(b"OFFLINE_SYNTHETIC_ONLY\n")
        self.root = self.sandbox / "store"
        self.store = OfflineStore(self.root, self.sandbox)

    def first(self):
        raw, payload = make_record()
        put = self.store.put(raw, payload, "put-1", admission())
        cas = self.store.cas(NS, None, put["record_id"], "cas-1", admission())
        return raw, payload, put, cas

    def test_vector_canonical_identity_and_reparse(self):
        raw, payload = make_record()
        obj, record_id = validate_record(raw, payload)
        self.assertEqual(canonical(parse(raw)), raw)
        self.assertEqual(record_id, sha(raw))
        self.assertEqual(namespace(obj), NS)
        self.assertEqual(self.store.put(raw, payload, "put-1", admission())["record_id"], record_id)

    def test_published_deterministic_vector(self):
        vector = json.loads((HERE / "vectors.json").read_text(encoding="utf-8"))
        raw = vector["record_envelope_utf8"].encode("utf-8")
        payload = bytes.fromhex(vector["payload_hex"])
        obj, record_id = validate_record(raw, payload)
        self.assertEqual(namespace(obj), tuple(vector["namespace"]))
        self.assertEqual(record_id, vector["record_id"])
        put = self.store.put(raw, payload, vector["put_operation_id"], admission())
        self.assertEqual(put["request_digest"], vector["put_request_digest"])
        self.assertEqual(put["receipt_id"], vector["put_receipt_id"])
        cas = self.store.cas(NS, None, record_id, vector["cas_operation_id"], admission())
        self.assertEqual(cas["request_digest"], vector["cas_request_digest"])
        self.assertEqual(cas["receipt_id"], vector["cas_receipt_id"])
        self.assertEqual(cas["pointer"], vector["expected_pointer"])

    def test_noncanonical_duplicate_key_float_bom_and_payload(self):
        raw, payload = make_record()
        for altered in (raw.replace(b'"schema":', b' "schema":', 1),
                        raw.replace(b'"schema":', b'"schema":"x","schema":', 1),
                        raw.replace(b'"generation":1', b'"generation":1.0'),
                        b'\xef\xbb\xbf' + raw):
            with self.subTest(altered=altered[:35]), self.assertRaises(StoreError):
                validate_record(altered, payload)
        with self.assertRaisesRegex(StoreError, "PAYLOAD_MISMATCH"):
            validate_record(raw, b"changed")

    def test_record_namespace_and_path_reject(self):
        raw, payload = make_record(entity_id="../KOD")
        with self.assertRaisesRegex(StoreError, "BAD_ATOM"):
            self.store.put(raw, payload, "put-1", admission())
        raw, payload = make_record(task_id="OTHER")
        with self.assertRaisesRegex(StoreError, "ADMISSION_MISMATCH"):
            self.store.put(raw, payload, "put-1", admission())
        with self.assertRaisesRegex(StoreError, "BAD_STORE_ROOT"):
            OfflineStore(self.sandbox.parent / "outside", self.sandbox)
        with self.assertRaisesRegex(StoreError, "BAD_ATOM"):
            self.store.state(("../../", NS[1], NS[2], NS[3]))

    def test_put_idempotency_and_conflicting_bytes(self):
        raw, payload = make_record()
        a = self.store.put(raw, payload, "put-1", admission())
        self.assertEqual(a, self.store.put(raw, payload, "put-1", admission()))
        other_raw, other_payload = make_record(payload=b"changed\n")
        with self.assertRaisesRegex(StoreError, "IDEMPOTENCY_CONFLICT"):
            self.store.put(other_raw, other_payload, "put-1", admission())
        self.assertEqual(self.store.put(other_raw, other_payload, "put-2", admission())["status"], "APPLIED")

    def test_cas_exact_prior_generation_parent_and_ledger(self):
        _, _, put, cas = self.first()
        self.assertEqual(cas["status"], "APPLIED")
        self.assertEqual(self.store.state(NS)["status"], "VERIFIED_LOCAL_CANDIDATE")
        self.assertEqual(self.store.cas(NS, None, put["record_id"], "cas-1", admission()), cas)
        with self.assertRaisesRegex(StoreError, "IDEMPOTENCY_CONFLICT"):
            self.store.cas(NS, cas["pointer"], put["record_id"], "cas-1", admission())
        self.assertEqual(self.store.cas(NS, None, put["record_id"], "other-cas", admission())["status"], "CONFLICT")
        raw2, payload2 = make_record(generation=2, parent=put["record_id"])
        put2 = self.store.put(raw2, payload2, "put-2", admission())
        cas2 = self.store.cas(NS, cas["pointer"], put2["record_id"], "cas-2", admission())
        self.assertEqual(cas2["pointer"]["generation"], 2)
        self.assertEqual(self.store.resolve("CAS", NS, "cas-2", cas2["request_digest"]), cas2)
        self.assertEqual(self.store.resolve("CAS", NS, "cas-1", cas["request_digest"]), cas)
        self.assertEqual(self.store.resolve("CAS", NS, "cas-2", sha(b"wrong"))["status"], "CONFLICT")
        self.assertEqual(self.store.resolve("CAS", NS, "missing", sha(b"missing"))["status"], "NOT_APPLIED")

    def test_generation_parent_and_missing_object_block(self):
        _, _, put, cas = self.first()
        raw, payload = make_record(generation=2, parent=sha(b"wrong"))
        p = self.store.put(raw, payload, "put-2", admission())
        with self.assertRaisesRegex(StoreError, "GENERATION_PARENT_MISMATCH"):
            self.store.cas(NS, cas["pointer"], p["record_id"], "cas-2", admission())
        with self.assertRaisesRegex(StoreError, "OBJECT_MISSING"):
            self.store.cas(NS, cas["pointer"], sha(b"missing"), "cas-3", admission())

    def test_frozen_superseded_unadmitted_and_stale_fence(self):
        _, _, put, cas = self.first()
        raw, payload = make_record(generation=2, parent=put["record_id"])
        for flag in ({"frozen": True}, {"superseded": True}, {"admitted": False}):
            with self.subTest(flag=flag), self.assertRaisesRegex(StoreError, "ADMISSION_BLOCKED"):
                self.store.put(raw, payload, "other", admission(**flag))
            with self.assertRaisesRegex(StoreError, "ADMISSION_BLOCKED"):
                self.store.cas(NS, cas["pointer"], put["record_id"], "other", admission(**flag))
        raw2, payload2 = make_record(generation=2, parent=put["record_id"], epoch=2, writer="writer-b")
        p2 = self.store.put(raw2, payload2, "put-2", admission(2, "writer-b"))
        self.store.cas(NS, cas["pointer"], p2["record_id"], "cas-2", admission(2, "writer-b"))
        raw3, payload3 = make_record(generation=3, parent=p2["record_id"])
        with self.assertRaisesRegex(StoreError, "STALE_WRITER_FENCE"):
            self.store.put(raw3, payload3, "put-stale", admission())
        with self.assertRaisesRegex(StoreError, "STALE_WRITER_FENCE"):
            self.store.cas(NS, self.store.state(NS)["pointer"], put["record_id"], "cas-stale", admission())

    def test_orphan_pointer_missing_corrupt_and_anchor_mismatch(self):
        raw, payload = make_record()
        put = self.store.put(raw, payload, "put-1", admission())
        self.assertEqual(self.store.state(NS)["status"], "ABSENT")
        self.store.cas(NS, None, put["record_id"], "cas-1", admission())
        self.assertEqual(self.store.compare_anchor(NS, sha(b"other"))["status"], "BLOCKED_CANONICAL_MISMATCH")
        self.assertEqual(self.store.compare_anchor(NS, put["record_id"])["status"], "LOCAL_MATCH_ONLY")
        with self.store.connect() as c:
            c.execute("DELETE FROM objects WHERE record_id=?", (put["record_id"],))
        self.assertEqual(self.store.state(NS)["status"], "BLOCKED_INTEGRITY")
        with self.assertRaisesRegex(StoreError, "LEDGER_OBJECT_MISSING"):
            self.store.put(raw, payload, "put-1", admission())

    def test_durable_conflict_then_pointer_advances(self):
        _, _, put, first = self.first()
        conflict = self.store.cas(NS, None, put["record_id"], "cas-conflict", admission())
        self.assertEqual(conflict["status"], "CONFLICT")
        self.assertEqual(conflict["actual"], first["pointer"])
        self.assertEqual(self.store.resolve("CAS", NS, "cas-conflict", conflict["request_digest"]), conflict)
        raw2, payload2 = make_record(generation=2, parent=put["record_id"])
        rid2 = self.store.put(raw2, payload2, "put-2", admission())["record_id"]
        self.store.cas(NS, first["pointer"], rid2, "cas-2", admission())
        self.assertEqual(self.store.resolve("CAS", NS, "cas-conflict", conflict["request_digest"]), conflict)
        self.assertEqual(self.store.cas(NS, None, put["record_id"], "cas-conflict", admission()), conflict)

    def test_conflict_crash_before_and_after_outcome_commit(self):
        for stage, committed in (("after_conflict_ledger", False), ("after_conflict_commit", True)):
            with self.subTest(stage=stage):
                temp = tempfile.TemporaryDirectory(dir=self.sandbox)
                self.addCleanup(temp.cleanup)
                root = Path(temp.name)
                store = OfflineStore(root, self.sandbox)
                raw, payload = make_record()
                rid = store.put(raw, payload, "put-1", admission())["record_id"]
                first = store.cas(NS, None, rid, "cas-1", admission())
                proc = self.worker("cas", stage, "cas-conflict", raw, payload, root)
                self.assertEqual(proc.returncode, 77, proc.stderr.decode())
                request = sha(canonical(["COMMIT_CURRENT_CAS", store.key(NS), "cas-conflict", None,
                                         rid, "writer-a", 1, "synthetic-authority",
                                         "synthetic-profile", "synthetic-sources"]))
                result = store.resolve("CAS", NS, "cas-conflict", request)
                self.assertEqual(result["status"], "CONFLICT" if committed else "NOT_APPLIED")
                if committed:
                    self.assertEqual(result["actual"], first["pointer"])
                self.assertEqual(store.state(NS)["pointer"], first["pointer"])

    def test_closed_semantic_ledger_fail_closed(self):
        _, _, put, cas = self.first()
        cases = [("PUT", "put-1", put), ("CAS", "cas-1", cas)]
        for kind, op_id, original in cases:
            for mutation in (lambda o: o.update(op_id="wrong"),
                             lambda o: o.update(operation="OTHER"),
                             lambda o: o.update(namespace="OTHER"),
                             lambda o: o.update(receipt_id=sha(b"wrong")),
                             lambda o: o.update(extra="unadmitted")):
                with self.subTest(kind=kind, mutation=mutation):
                    altered = dict(original)
                    mutation(altered)
                    with self.store.connect() as c:
                        c.execute("UPDATE operations SET outcome=? WHERE kind=? AND namespace=? AND op_id=?",
                                  (canonical(altered).decode(), kind, self.store.key(NS), op_id))
                    self.assertEqual(self.store.resolve(kind, NS, op_id, original["request_digest"])["status"], "UNKNOWN")
                    with self.store.connect() as c:
                        with self.assertRaises(StoreError):
                            self.store.operation(c, kind, self.store.key(NS), op_id, original["request_digest"])
                        c.execute("UPDATE operations SET outcome=? WHERE kind=? AND namespace=? AND op_id=?",
                                  (canonical(original).decode(), kind, self.store.key(NS), op_id))
        for field, value in (("record_id", sha(b"wrong")), ("generation", 99),
                             ("parent_record_id", sha(b"wrong")),
                             ("operation_request_digest", sha(b"wrong"))):
            with self.subTest(pointer_field=field):
                altered = dict(cas)
                altered["pointer"] = dict(cas["pointer"])
                altered["pointer"][field] = value
                with self.store.connect() as c:
                    c.execute("UPDATE operations SET outcome=? WHERE kind='CAS' AND namespace=? AND op_id='cas-1'",
                              (canonical(altered).decode(), self.store.key(NS)))
                self.assertEqual(self.store.resolve("CAS", NS, "cas-1", cas["request_digest"])["status"], "UNKNOWN")
                self.assertEqual(self.store.state(NS)["status"], "BLOCKED_INTEGRITY")
                with self.store.connect() as c:
                    c.execute("UPDATE operations SET outcome=? WHERE kind='CAS' AND namespace=? AND op_id='cas-1'",
                              (canonical(cas).decode(), self.store.key(NS)))

    def test_concurrency_one_cas_winner(self):
        raw, payload = make_record()
        record_id = self.store.put(raw, payload, "put-1", admission())["record_id"]
        def go(i):
            s = OfflineStore(self.root, self.sandbox)
            return s.cas(NS, None, record_id, f"cas-{i}", admission())["status"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(go, range(8)))
        self.assertEqual(results.count("APPLIED"), 1)
        self.assertEqual(results.count("CONFLICT"), 7)
        self.assertEqual(self.store.state(NS)["pointer"]["generation"], 1)

    def test_crash_put_stages_and_reopen(self):
        for stage, applied in (("after_object", False), ("after_put_ledger", False),
                               ("after_put_commit", True)):
            with self.subTest(stage=stage):
                raw, payload = make_record(payload=stage.encode())
                op = "put-" + stage
                proc = self.worker("put", stage, op, raw, payload)
                self.assertEqual(proc.returncode, 77, proc.stderr.decode())
                s = OfflineStore(self.root, self.sandbox)
                request = sha(canonical(["PUT_IMMUTABLE", s.key(NS), op, sha(raw), sha(payload), len(payload)]))
                self.assertEqual(s.resolve("PUT", NS, op, request)["status"],
                                 "APPLIED" if applied else "NOT_APPLIED")
                with s.connect() as c:
                    exists = c.execute("SELECT COUNT(*) FROM objects WHERE record_id=?", (sha(raw),)).fetchone()[0]
                self.assertEqual(exists, int(applied))

    def test_crash_cas_atomic_tuple_and_lost_response(self):
        for stage in ("after_compare", "after_fence", "after_pointer", "after_cas_ledger",
                      "after_cas_commit"):
            with self.subTest(stage=stage):
                temp = tempfile.TemporaryDirectory(dir=self.sandbox)
                self.addCleanup(temp.cleanup)
                root = Path(temp.name)
                s = OfflineStore(root, self.sandbox)
                raw, payload = make_record(payload=stage.encode())
                record_id = s.put(raw, payload, "put-1", admission())["record_id"]
                proc = self.worker("cas", stage, "cas-crash", raw, payload, root)
                self.assertEqual(proc.returncode, 77, proc.stderr.decode())
                s = OfflineStore(root, self.sandbox)
                with s.connect() as c:
                    ptr = c.execute("SELECT value FROM pointers WHERE namespace=?", (s.key(NS),)).fetchone()
                    fence = c.execute("SELECT epoch,writer FROM fences WHERE namespace=?", (s.key(NS),)).fetchone()
                    ledger = c.execute("SELECT request_digest,outcome FROM operations WHERE kind='CAS' AND namespace=? AND op_id='cas-crash'", (s.key(NS),)).fetchone()
                committed = stage == "after_cas_commit"
                self.assertEqual((ptr is not None, fence is not None, ledger is not None),
                                 (committed, committed, committed))
                self.assertEqual(s.state(NS)["status"],
                                 "VERIFIED_LOCAL_CANDIDATE" if committed else "ABSENT")
                if committed:
                    self.assertEqual(json.loads(ptr[0])["record_id"], record_id)
                    self.assertEqual(fence, (1, "writer-a"))
                    self.assertEqual(s.resolve("CAS", NS, "cas-crash", ledger[0])["status"], "APPLIED")
                else:
                    self.assertEqual(s.resolve("CAS", NS, "cas-crash", sha(b"x"))["status"], "NOT_APPLIED")

    def test_crash_second_cas_writer_epoch_rollover(self):
        for stage in ("after_compare", "after_fence", "after_pointer", "after_cas_ledger",
                      "after_cas_commit"):
            with self.subTest(stage=stage):
                temp = tempfile.TemporaryDirectory(dir=self.sandbox)
                self.addCleanup(temp.cleanup)
                root = Path(temp.name)
                s = OfflineStore(root, self.sandbox)
                raw1, payload1 = make_record()
                rid1 = s.put(raw1, payload1, "put-1", admission())["record_id"]
                first = s.cas(NS, None, rid1, "cas-1", admission())
                raw2, payload2 = make_record(generation=2, parent=rid1, epoch=2,
                                             writer="writer-b", payload=b"successor\n")
                rid2 = s.put(raw2, payload2, "put-2", admission(2, "writer-b"))["record_id"]
                prior_hex = canonical(first["pointer"]).hex()
                proc = subprocess.run([sys.executable, "-B", str(HERE / "crash_worker.py"),
                                       str(self.sandbox), str(root), "cas-successor", stage,
                                       "cas-2", raw2.hex(), payload2.hex(), prior_hex],
                                      capture_output=True, check=False)
                self.assertEqual(proc.returncode, 77, proc.stderr.decode())
                s = OfflineStore(root, self.sandbox)
                state = s.state(NS)
                self.assertEqual(state["status"], "VERIFIED_LOCAL_CANDIDATE")
                committed = stage == "after_cas_commit"
                self.assertEqual(state["pointer"]["record_id"], rid2 if committed else rid1)
                self.assertEqual(state["fence"], (2, "writer-b") if committed else (1, "writer-a"))
                with s.connect() as c:
                    ledger = c.execute("SELECT request_digest FROM operations WHERE kind='CAS' AND namespace=? AND op_id='cas-2'", (s.key(NS),)).fetchone()
                self.assertEqual(ledger is not None, committed)
                if committed:
                    self.assertEqual(s.resolve("CAS", NS, "cas-2", ledger[0])["status"], "APPLIED")
                else:
                    self.assertEqual(s.resolve("CAS", NS, "cas-2", sha(b"x"))["status"], "NOT_APPLIED")

    def test_pointer_ledger_and_fence_divergence(self):
        _, _, put, cas = self.first()
        with self.store.connect() as c:
            c.execute("DELETE FROM operations WHERE kind='CAS' AND namespace=?", (self.store.key(NS),))
        self.assertEqual(self.store.state(NS)["status"], "BLOCKED_INTEGRITY")
        with self.store.connect() as c:
            c.execute("INSERT INTO operations VALUES (?,?,?,?,?)",
                      ("CAS", self.store.key(NS), "cas-1", cas["request_digest"],
                       canonical(cas).decode()))
            c.execute("UPDATE fences SET writer='forged' WHERE namespace=?", (self.store.key(NS),))
        self.assertEqual(self.store.state(NS)["status"], "BLOCKED_INTEGRITY")

    def test_corrupt_pointer_and_ledger_fail_closed(self):
        _, _, _, cas = self.first()
        with self.store.connect() as c:
            c.execute("UPDATE pointers SET value='not-json' WHERE namespace=?", (self.store.key(NS),))
        self.assertEqual(self.store.state(NS)["status"], "BLOCKED_INTEGRITY")
        with self.store.connect() as c:
            c.execute("UPDATE operations SET outcome='not-json' WHERE kind='CAS' AND namespace=?",
                      (self.store.key(NS),))
        self.assertEqual(self.store.resolve("CAS", NS, "cas-1", cas["request_digest"])["status"], "UNKNOWN")

    def test_unavailable_resolve_unknown_and_invalid_root(self):
        with patch.object(self.store, "connect", side_effect=sqlite3.OperationalError("offline")):
            self.assertEqual(self.store.resolve("CAS", NS, "cas-x", sha(b"x"))["status"], "UNKNOWN")
        (self.sandbox / ".offline-synthetic-root").unlink()
        with self.assertRaisesRegex(StoreError, "NOT_SYNTHETIC_ROOT"):
            OfflineStore(self.root, self.sandbox)

    def worker(self, kind, stage, op, raw, payload, root=None):
        return subprocess.run([sys.executable, "-B", str(HERE / "crash_worker.py"),
                               str(self.sandbox), str(root or self.root), kind, stage, op,
                               raw.hex(), payload.hex()], capture_output=True, check=False)


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(CandidateTests))
    print(json.dumps({"tests": result.testsRun, "failures": len(result.failures),
                      "errors": len(result.errors), "skipped": len(result.skipped),
                      "verdict": "PASS_OFFLINE_SYNTHETIC" if result.wasSuccessful() else "FAIL_OFFLINE_SYNTHETIC",
                      "live_calls": 0, "credentials": 0, "project_state_mutation": False}, sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)
