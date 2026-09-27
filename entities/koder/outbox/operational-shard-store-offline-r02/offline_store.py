#!/usr/bin/env python3
"""Offline synthetic operational-store candidate. No project authority or live adapter."""
from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

SCHEMA = "operational-record-v1"
FIELDS = frozenset({
    "schema", "record_kind", "entity_id", "task_id", "task_version", "stream_id",
    "writer_id", "writer_epoch", "authority_ref", "trust_profile_ref",
    "approved_sources_ref", "generation", "parent_digest", "payload_sha256",
    "payload_bytes", "payload_media_type", "state_class", "source_refs",
    "supersedes_refs", "policy_ref", "expiry_class",
})
KINDS = frozenset({"WORKING_NOTE", "STEP_EVIDENCE", "CHECKPOINT_CANDIDATE",
                   "PROMOTION_RECEIPT", "CONFLICT_EVIDENCE"})
STATES = frozenset({"PROVISIONAL", "SEALED_CANDIDATE", "PROMOTION_EVIDENCE"})
ATOM = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}\Z")
DIGEST = re.compile(r"sha256:[0-9a-f]{64}\Z")


POINTER_FIELDS = frozenset({"generation", "record_id", "parent_record_id",
                            "writer_epoch", "writer_id", "authority_ref",
                            "trust_profile_ref", "operation_id",
                            "operation_request_digest", "receipt_id"})
PUT_OUTCOME_FIELDS = frozenset({"status", "operation", "namespace", "op_id",
                                "record_id", "request_digest", "receipt_id"})
CAS_APPLIED_FIELDS = frozenset({"status", "operation", "namespace", "op_id",
                                "pointer", "expected_pointer", "approved_sources_ref",
                                "request_digest", "receipt_id"})
CAS_CONFLICT_FIELDS = frozenset({"status", "operation", "namespace", "op_id",
                                 "reason", "actual", "expected_pointer", "requested_record_id",
                                 "writer_id", "writer_epoch", "authority_ref",
                                 "trust_profile_ref", "approved_sources_ref",
                                 "request_digest", "receipt_id"})


class StoreError(RuntimeError):
    pass


def check(condition: bool, code: str) -> None:
    if not condition:
        raise StoreError(code)


def sha(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def pairs(items):
    obj = {}
    for key, value in items:
        check(key not in obj, "DUPLICATE_JSON_KEY")
        obj[key] = value
    return obj


def reject_number(value):
    raise StoreError("NON_INTEGER_NUMBER")


def parse(raw: bytes):
    check(type(raw) is bytes and not raw.startswith(b"\xef\xbb\xbf"), "BAD_BYTES")
    try:
        return json.loads(raw.decode("utf-8", "strict"), object_pairs_hook=pairs,
                          parse_float=reject_number, parse_constant=reject_number)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise StoreError("BAD_JSON") from exc


def _safe_text(value):
    check(type(value) is str and not any(0xD800 <= ord(c) <= 0xDFFF for c in value),
          "BAD_TEXT")
    return value


def _walk(value):
    if type(value) is str:
        _safe_text(value)
    elif type(value) is int or value is None or type(value) is bool:
        pass
    elif type(value) is list:
        for x in value:
            _walk(x)
    elif type(value) is dict:
        for key, x in value.items():
            _safe_text(key)
            _walk(x)
    else:
        raise StoreError("BAD_JSON_TYPE")


def canonical(obj) -> bytes:
    _walk(obj)
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def atom(value):
    check(type(value) is str and ATOM.fullmatch(value) is not None, "BAD_ATOM")
    return value


def namespace(record):
    return tuple(record[key] for key in ("entity_id", "task_id", "task_version", "stream_id"))


def validate_record(raw: bytes, payload: bytes):
    obj = parse(raw)
    check(type(obj) is dict and set(obj) == FIELDS and canonical(obj) == raw,
          "BAD_RECORD_CANONICAL")
    check(obj["schema"] == SCHEMA and obj["record_kind"] in KINDS and
          obj["state_class"] in STATES, "BAD_RECORD_SCHEMA")
    for key in ("entity_id", "task_id", "stream_id", "writer_id"):
        atom(obj[key])
    for key in ("task_version", "authority_ref", "trust_profile_ref",
                "approved_sources_ref", "payload_media_type", "policy_ref", "expiry_class"):
        check(type(obj[key]) is str and 0 < len(obj[key]) <= 512, "BAD_RECORD_REF")
        _safe_text(obj[key])
    check(type(obj["writer_epoch"]) is int and obj["writer_epoch"] > 0 and
          type(obj["generation"]) is int and obj["generation"] > 0,
          "BAD_RECORD_GENERATION")
    check(type(payload) is bytes and type(obj["payload_bytes"]) is int and
          obj["payload_bytes"] == len(payload) and obj["payload_sha256"] == sha(payload),
          "PAYLOAD_MISMATCH")
    parent = obj["parent_digest"]
    check((obj["generation"] == 1 and parent is None) or
          (obj["generation"] > 1 and type(parent) is str and DIGEST.fullmatch(parent)),
          "BAD_PARENT")
    for key in ("source_refs", "supersedes_refs"):
        check(type(obj[key]) is list and all(type(x) is str and x for x in obj[key]),
              "BAD_RECORD_REF")
    return obj, sha(raw)


@dataclass(frozen=True)
class SyntheticAdmission:
    """Fixture only: represents a supervisor verdict; it is NOT trust verification."""
    entity_id: str
    task_id: str
    task_version: str
    stream_id: str
    writer_id: str
    writer_epoch: int
    authority_ref: str
    trust_profile_ref: str
    approved_sources_ref: str
    admitted: bool = False
    frozen: bool = False
    superseded: bool = False

    def verify(self, record):
        check(self.admitted and not self.frozen and not self.superseded,
              "ADMISSION_BLOCKED")
        for key in ("entity_id", "task_id", "task_version", "stream_id",
                    "writer_id", "writer_epoch", "authority_ref", "trust_profile_ref",
                    "approved_sources_ref"):
            check(getattr(self, key) == record[key], "ADMISSION_MISMATCH")


def receipt(status, **values):
    return {"status": status, **values}


class OfflineStore:
    def __init__(self, root: Path, sandbox_root: Path):
        sandbox_root = Path(sandbox_root).resolve(strict=True)
        marker = sandbox_root / ".offline-synthetic-root"
        check(marker.is_file() and marker.read_bytes() == b"OFFLINE_SYNTHETIC_ONLY\n",
              "NOT_SYNTHETIC_ROOT")
        root = Path(root)
        check(not root.is_symlink() and root.resolve().is_relative_to(sandbox_root) and
              root.resolve() != sandbox_root, "BAD_STORE_ROOT")
        root.mkdir(parents=True, exist_ok=True)
        self.db = root / "candidate.sqlite3"
        with self.connect() as c:
            c.executescript("""
                CREATE TABLE IF NOT EXISTS objects (
                    namespace TEXT NOT NULL, record_id TEXT PRIMARY KEY,
                    envelope BLOB NOT NULL, payload BLOB NOT NULL);
                CREATE TABLE IF NOT EXISTS pointers (
                    namespace TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS fences (
                    namespace TEXT PRIMARY KEY, epoch INTEGER NOT NULL, writer TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS operations (
                    kind TEXT NOT NULL, namespace TEXT NOT NULL, op_id TEXT NOT NULL,
                    request_digest TEXT NOT NULL, outcome TEXT NOT NULL,
                    PRIMARY KEY(kind, namespace, op_id));
            """)

    def connect(self):
        c = sqlite3.connect(self.db, timeout=10.0, isolation_level=None)
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA synchronous=FULL")
        c.execute("PRAGMA busy_timeout=10000")
        return c

    @staticmethod
    def key(ns):
        check(type(ns) is tuple and len(ns) == 4 and all(type(x) is str for x in ns),
              "BAD_NAMESPACE")
        for x in (ns[0], ns[1], ns[3]):
            atom(x)
        check(0 < len(ns[2]) <= 512, "BAD_NAMESPACE")
        return canonical(list(ns)).decode("utf-8")

    @staticmethod
    def fault(stage, injection):
        if stage == injection:
            os._exit(77)  # test subprocess only; abrupt process loss

    @staticmethod
    def pointer_object(c, key, pointer):
        check(type(pointer) is dict and set(pointer) == POINTER_FIELDS,
              "BAD_POINTER_SCHEMA")
        check(type(pointer["generation"]) is int and pointer["generation"] > 0 and
              type(pointer["writer_epoch"]) is int and pointer["writer_epoch"] > 0 and
              type(pointer["record_id"]) is str and DIGEST.fullmatch(pointer["record_id"]) and
              type(pointer["operation_request_digest"]) is str and
              DIGEST.fullmatch(pointer["operation_request_digest"]) and
              type(pointer["receipt_id"]) is str and DIGEST.fullmatch(pointer["receipt_id"]),
              "BAD_POINTER_TYPE")
        atom(pointer["writer_id"]); atom(pointer["operation_id"])
        for name in ("authority_ref", "trust_profile_ref"):
            check(type(pointer[name]) is str and bool(pointer[name]), "BAD_POINTER_TYPE")
        parent = pointer["parent_record_id"]
        check((pointer["generation"] == 1 and parent is None) or
              (pointer["generation"] > 1 and type(parent) is str and DIGEST.fullmatch(parent)),
              "BAD_POINTER_PARENT")
        core = {k: v for k, v in pointer.items() if k != "receipt_id"}
        expected_receipt = sha(canonical(["CAS_RECEIPT", key, pointer["operation_id"],
                                          pointer["operation_request_digest"], core]))
        check(pointer["receipt_id"] == expected_receipt, "BAD_POINTER_RECEIPT")
        row = c.execute("SELECT namespace,envelope,payload FROM objects WHERE record_id=?",
                        (pointer["record_id"],)).fetchone()
        check(row is not None and row[0] == key, "LEDGER_OBJECT_MISSING")
        obj, derived = validate_record(row[1], row[2])
        check(derived == pointer["record_id"] and OfflineStore.key(namespace(obj)) == key and
              obj["generation"] == pointer["generation"] and
              obj["parent_digest"] == parent and
              obj["writer_id"] == pointer["writer_id"] and
              obj["writer_epoch"] == pointer["writer_epoch"] and
              obj["authority_ref"] == pointer["authority_ref"] and
              obj["trust_profile_ref"] == pointer["trust_profile_ref"],
              "LEDGER_OBJECT_MISMATCH")
        return obj

    @staticmethod
    def validate_ledger(c, kind, key, op_id, request_digest, raw):
        check(type(raw) is str, "BAD_OPERATION_LEDGER")
        out = parse(raw.encode("utf-8"))
        check(type(out) is dict and canonical(out) == raw.encode("utf-8") and
              out.get("operation") == kind and out.get("namespace") == key and
              out.get("op_id") == op_id and out.get("request_digest") == request_digest and
              type(out.get("receipt_id")) is str and DIGEST.fullmatch(out["receipt_id"]),
              "BAD_OPERATION_LEDGER")
        if kind == "PUT":
            check(set(out) == PUT_OUTCOME_FIELDS and out.get("status") == "APPLIED" and
                  type(out.get("record_id")) is str and DIGEST.fullmatch(out["record_id"]),
                  "BAD_PUT_OUTCOME")
            rid = out["record_id"]
            row = c.execute("SELECT namespace,envelope,payload FROM objects WHERE record_id=?",
                            (rid,)).fetchone()
            check(row is not None and row[0] == key, "LEDGER_OBJECT_MISSING")
            obj, derived = validate_record(row[1], row[2])
            check(derived == rid and OfflineStore.key(namespace(obj)) == key and
                  request_digest == sha(canonical(["PUT_IMMUTABLE", key, op_id, rid,
                                                   sha(row[2]), len(row[2])])) and
                  out["receipt_id"] == sha(canonical(["PUT_RECEIPT", key, op_id,
                                                       request_digest, rid])), "BAD_PUT_OUTCOME")
        elif kind == "CAS" and out.get("status") == "APPLIED":
            check(set(out) == CAS_APPLIED_FIELDS and
                  type(out.get("approved_sources_ref")) is str and out["approved_sources_ref"],
                  "BAD_CAS_OUTCOME")
            pointer = out["pointer"]
            obj = OfflineStore.pointer_object(c, key, pointer)
            prior = out["expected_pointer"]
            if prior is not None:
                OfflineStore.pointer_object(c, key, prior)
            check(pointer["operation_id"] == op_id and
                  pointer["operation_request_digest"] == request_digest and
                  pointer["receipt_id"] == out["receipt_id"] and
                  pointer["generation"] == (1 if prior is None else prior["generation"] + 1) and
                  pointer["parent_record_id"] == (None if prior is None else prior["record_id"]) and
                  obj["approved_sources_ref"] == out["approved_sources_ref"],
                  "BAD_CAS_OUTCOME")
            derived_request = sha(canonical(["COMMIT_CURRENT_CAS", key, op_id, prior,
                                             pointer["record_id"], pointer["writer_id"],
                                             pointer["writer_epoch"], pointer["authority_ref"],
                                             pointer["trust_profile_ref"], out["approved_sources_ref"]]))
            check(derived_request == request_digest, "BAD_CAS_REQUEST_BINDING")
        elif kind == "CAS" and out.get("status") == "CONFLICT":
            check(set(out) == CAS_CONFLICT_FIELDS and out.get("reason") == "CAS_CONFLICT" and
                  type(out.get("requested_record_id")) is str and
                  DIGEST.fullmatch(out["requested_record_id"]) and
                  type(out.get("writer_epoch")) is int and out["writer_epoch"] > 0,
                  "BAD_CONFLICT_OUTCOME")
            atom(out["writer_id"])
            for name in ("authority_ref", "trust_profile_ref", "approved_sources_ref"):
                check(type(out[name]) is str and bool(out[name]), "BAD_CONFLICT_OUTCOME")
            actual, prior = out["actual"], out["expected_pointer"]
            if actual is not None:
                OfflineStore.pointer_object(c, key, actual)
            # A conflicting caller may supply an unknown expected pointer.
            # The request digest binds its exact bytes without trusting it.
            check(prior is None or type(prior) is dict, "BAD_CONFLICT_OUTCOME")
            check(actual != prior, "BAD_CONFLICT_OUTCOME")
            derived_request = sha(canonical(["COMMIT_CURRENT_CAS", key, op_id, prior,
                                             out["requested_record_id"], out["writer_id"],
                                             out["writer_epoch"], out["authority_ref"],
                                             out["trust_profile_ref"], out["approved_sources_ref"]]))
            derived_receipt = sha(canonical(["CAS_CONFLICT_RECEIPT", key, op_id,
                                             request_digest, actual]))
            check(derived_request == request_digest and derived_receipt == out["receipt_id"],
                  "BAD_CONFLICT_BINDING")
        else:
            raise StoreError("BAD_OPERATION_LEDGER")
        return out

    @staticmethod
    def operation(c, kind, key, op_id, request_digest):
        row = c.execute("SELECT request_digest,outcome FROM operations WHERE kind=? AND namespace=? AND op_id=?",
                        (kind, key, op_id)).fetchone()
        if row:
            check(row[0] == request_digest, "IDEMPOTENCY_CONFLICT")
            return OfflineStore.validate_ledger(c, kind, key, op_id, row[0], row[1])
        return None

    def put(self, envelope: bytes, payload: bytes, op_id: str,
            admission: SyntheticAdmission, injection=None):
        atom(op_id)
        obj, record_id = validate_record(envelope, payload)
        admission.verify(obj)
        key = self.key(namespace(obj))
        request_digest = sha(canonical(["PUT_IMMUTABLE", key, op_id, record_id,
                                        sha(payload), len(payload)]))
        with self.connect() as c:
            c.execute("BEGIN IMMEDIATE")
            old = self.operation(c, "PUT", key, op_id, request_digest)
            if old is not None:
                present = c.execute("SELECT namespace,envelope,payload FROM objects WHERE record_id=?",
                                    (record_id,)).fetchone()
                check(present == (key, envelope, payload), "OBJECT_CORRUPT")
                c.commit(); return old
            fence_row = c.execute("SELECT epoch,writer FROM fences WHERE namespace=?", (key,)).fetchone()
            if fence_row:
                check(admission.writer_epoch >= fence_row[0], "STALE_WRITER_FENCE")
                check(admission.writer_epoch != fence_row[0] or admission.writer_id == fence_row[1],
                      "FENCE_WRITER_CONFLICT")
            existing = c.execute("SELECT envelope,payload FROM objects WHERE record_id=?",
                                 (record_id,)).fetchone()
            check(existing is None or existing == (envelope, payload), "OBJECT_ID_CONFLICT")
            if existing is None:
                c.execute("INSERT INTO objects VALUES (?,?,?,?)", (key, record_id, envelope, payload))
            self.fault("after_object", injection)
            out = receipt("APPLIED", operation="PUT", op_id=op_id, record_id=record_id,
                          request_digest=request_digest, namespace=key,
                          receipt_id=sha(canonical(["PUT_RECEIPT", key, op_id,
                                                     request_digest, record_id])))
            c.execute("INSERT INTO operations VALUES (?,?,?,?,?)",
                      ("PUT", key, op_id, request_digest, canonical(out).decode()))
            self.fault("after_put_ledger", injection)
            c.commit()
        self.fault("after_put_commit", injection)
        return out

    def cas(self, ns: tuple[str, str, str, str], expected: dict | None,
            record_id: str, op_id: str, admission: SyntheticAdmission, injection=None):
        atom(op_id)
        check(type(record_id) is str and DIGEST.fullmatch(record_id), "BAD_RECORD_ID")
        key = self.key(ns)
        check(tuple(getattr(admission, k) for k in
                    ("entity_id", "task_id", "task_version", "stream_id")) == ns and
              admission.admitted and not admission.frozen and not admission.superseded,
              "ADMISSION_BLOCKED")
        check(expected is None or type(expected) is dict, "BAD_EXPECTED_POINTER")
        request_digest = sha(canonical(["COMMIT_CURRENT_CAS", key, op_id, expected,
                                        record_id, admission.writer_id,
                                        admission.writer_epoch, admission.authority_ref,
                                        admission.trust_profile_ref, admission.approved_sources_ref]))
        with self.connect() as c:
            c.execute("BEGIN IMMEDIATE")
            old = self.operation(c, "CAS", key, op_id, request_digest)
            if old is not None:
                c.commit(); return old
            row = c.execute("SELECT value FROM pointers WHERE namespace=?", (key,)).fetchone()
            actual = json.loads(row[0]) if row else None
            if actual != expected:
                out = receipt("CONFLICT", operation="CAS", op_id=op_id,
                              reason="CAS_CONFLICT", actual=actual,
                              expected_pointer=expected, requested_record_id=record_id,
                              writer_id=admission.writer_id,
                              writer_epoch=admission.writer_epoch,
                              authority_ref=admission.authority_ref,
                              trust_profile_ref=admission.trust_profile_ref,
                              approved_sources_ref=admission.approved_sources_ref,
                              request_digest=request_digest, namespace=key,
                              receipt_id=sha(canonical(["CAS_CONFLICT_RECEIPT", key, op_id,
                                                         request_digest, actual])))
                c.execute("INSERT INTO operations VALUES (?,?,?,?,?)",
                          ("CAS", key, op_id, request_digest, canonical(out).decode()))
                self.fault("after_conflict_ledger", injection)
                c.commit()
                self.fault("after_conflict_commit", injection)
                return out
            self.fault("after_compare", injection)
            obj_row = c.execute("SELECT namespace,envelope,payload FROM objects WHERE record_id=?",
                                (record_id,)).fetchone()
            check(obj_row is not None, "OBJECT_MISSING")
            check(obj_row[0] == key, "NAMESPACE_MISMATCH")
            obj, derived = validate_record(obj_row[1], obj_row[2])
            check(derived == record_id, "OBJECT_CORRUPT")
            admission.verify(obj)
            fence_row = c.execute("SELECT epoch,writer FROM fences WHERE namespace=?", (key,)).fetchone()
            if fence_row:
                check(admission.writer_epoch >= fence_row[0], "STALE_WRITER_FENCE")
                check(admission.writer_epoch != fence_row[0] or admission.writer_id == fence_row[1],
                      "FENCE_WRITER_CONFLICT")
            if actual is not None:
                check(admission.writer_epoch >= actual["writer_epoch"], "STALE_WRITER_FENCE")
            generation = 1 if actual is None else actual["generation"] + 1
            check(obj["generation"] == generation and
                  obj["parent_digest"] == (None if actual is None else actual["record_id"]),
                  "GENERATION_PARENT_MISMATCH")
            c.execute("INSERT INTO fences VALUES (?,?,?) ON CONFLICT(namespace) DO UPDATE SET epoch=excluded.epoch,writer=excluded.writer",
                      (key, admission.writer_epoch, admission.writer_id))
            self.fault("after_fence", injection)
            new = {"generation": generation, "record_id": record_id,
                   "parent_record_id": obj["parent_digest"],
                   "writer_epoch": admission.writer_epoch, "writer_id": admission.writer_id,
                   "authority_ref": admission.authority_ref,
                   "trust_profile_ref": admission.trust_profile_ref,
                   "operation_id": op_id, "operation_request_digest": request_digest}
            receipt_id = sha(canonical(["CAS_RECEIPT", key, op_id, request_digest, new]))
            new["receipt_id"] = receipt_id
            c.execute("INSERT INTO pointers VALUES (?,?) ON CONFLICT(namespace) DO UPDATE SET value=excluded.value",
                      (key, canonical(new).decode()))
            self.fault("after_pointer", injection)
            out = receipt("APPLIED", operation="CAS", op_id=op_id, pointer=new,
                          expected_pointer=expected,
                          approved_sources_ref=admission.approved_sources_ref,
                          request_digest=request_digest, namespace=key,
                          receipt_id=receipt_id)
            c.execute("INSERT INTO operations VALUES (?,?,?,?,?)",
                      ("CAS", key, op_id, request_digest, canonical(out).decode()))
            self.fault("after_cas_ledger", injection)
            c.commit()  # one recoverable linearization point for pointer + fence + outcome
        self.fault("after_cas_commit", injection)
        return out

    def resolve(self, kind, ns, op_id, request_digest):
        atom(op_id)
        check(kind in ("PUT", "CAS") and type(request_digest) is str and
              DIGEST.fullmatch(request_digest), "BAD_RESOLVE_REQUEST")
        key = self.key(ns)
        try:
            with self.connect() as c:
                row = c.execute("SELECT request_digest,outcome FROM operations WHERE kind=? AND namespace=? AND op_id=?",
                                (kind, key, op_id)).fetchone()
                if row is None:
                    return receipt("NOT_APPLIED")
                if row[0] != request_digest:
                    return receipt("CONFLICT", reason="REQUEST_DIGEST_MISMATCH")
                try:
                    return self.validate_ledger(c, kind, key, op_id, row[0], row[1])
                except (ValueError, TypeError, KeyError, StoreError):
                    return receipt("UNKNOWN", reason="LEDGER_CORRUPT")
        except sqlite3.Error:
            return receipt("UNKNOWN")

    def state(self, ns):
        key = self.key(ns)
        try:
            with self.connect() as c:
                row = c.execute("SELECT value FROM pointers WHERE namespace=?", (key,)).fetchone()
                fence = c.execute("SELECT epoch,writer FROM fences WHERE namespace=?", (key,)).fetchone()
                if row is None:
                    return receipt("ABSENT", fence=fence)
                try:
                    pointer = json.loads(row[0])
                    check(type(pointer) is dict and set(pointer) == {
                        "generation", "record_id", "parent_record_id", "writer_epoch",
                        "writer_id", "authority_ref", "trust_profile_ref", "operation_id",
                        "operation_request_digest", "receipt_id"} and
                        type(pointer["record_id"]) is str and
                        type(pointer["generation"]) is int and
                        type(pointer["writer_epoch"]) is int and
                        type(pointer["writer_id"]) is str,
                          "POINTER_CORRUPT")
                except (ValueError, TypeError, KeyError, StoreError):
                    return receipt("BLOCKED_INTEGRITY", reason="POINTER_CORRUPT")
                obj = c.execute("SELECT envelope,payload FROM objects WHERE record_id=?",
                                (pointer["record_id"],)).fetchone()
                if obj is None:
                    return receipt("BLOCKED_INTEGRITY", reason="POINTER_WITHOUT_OBJECT")
                try:
                    record, derived = validate_record(obj[0], obj[1])
                    check(derived == pointer["record_id"] and namespace(record) == ns and
                          record["generation"] == pointer["generation"] and
                          record["parent_digest"] == pointer["parent_record_id"], "OBJECT_CORRUPT")
                except (StoreError, KeyError, TypeError):
                    return receipt("BLOCKED_INTEGRITY", reason="POINTER_OBJECT_DIVERGENCE")
                if fence is None or fence != (pointer["writer_epoch"], pointer["writer_id"]):
                    return receipt("BLOCKED_INTEGRITY", reason="FENCE_POINTER_DIVERGENCE")
                op = c.execute("SELECT request_digest,outcome FROM operations WHERE kind='CAS' AND namespace=? AND op_id=?",
                               (key, pointer.get("operation_id"))).fetchone()
                if op is None or op[0] != pointer.get("operation_request_digest"):
                    return receipt("BLOCKED_INTEGRITY", reason="POINTER_LEDGER_DIVERGENCE")
                try:
                    outcome = self.validate_ledger(c, "CAS", key, pointer["operation_id"], op[0], op[1])
                    if (outcome.get("status") != "APPLIED" or outcome.get("pointer") != pointer or
                            outcome.get("receipt_id") != pointer["receipt_id"]):
                        return receipt("BLOCKED_INTEGRITY", reason="POINTER_LEDGER_DIVERGENCE")
                except (ValueError, TypeError, KeyError, StoreError):
                    return receipt("BLOCKED_INTEGRITY", reason="POINTER_LEDGER_DIVERGENCE")
                return receipt("VERIFIED_LOCAL_CANDIDATE", pointer=pointer, fence=fence)
        except sqlite3.Error:
            return receipt("UNKNOWN")

    def compare_anchor(self, ns, expected_record_id):
        state = self.state(ns)
        if state["status"] != "VERIFIED_LOCAL_CANDIDATE":
            return state
        if state["pointer"]["record_id"] != expected_record_id:
            return receipt("BLOCKED_CANONICAL_MISMATCH")
        return receipt("LOCAL_MATCH_ONLY")  # synthetic input, never a real Git readback
