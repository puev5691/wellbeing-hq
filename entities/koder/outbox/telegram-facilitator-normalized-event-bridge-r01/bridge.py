#!/usr/bin/env python3
"""Изолированное преобразование safe_receipt Phase 1B в NormalizedEvent.

Python 3.10+, без сети, БД, секретов и изменений runtime.
Вход содержит агрегатную квитанцию и отдельный проверяемый контекст.
Только fact_claim об учтённых счётчиках, не анализ содержания обсуждения.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from pathlib import Path
from types import ModuleType
from typing import Callable
import hashlib
import json
import re
import sys

SCHEMA = "phase1b-safe-receipt-bridge-r01"
SCOPE = "convert_aggregate_receipt_to_fact_claim"
CORE_BLOB = "ad980b0de8a00c1d134823cebc49059a0811f3fa"
CORE_SHA256 = "33f280e9cc56534996d0706de7e3605c0247ff1af8b71ea985fdd7613d47b64a"
PRODUCER_BLOB = "c870616f119fa3198a50db31898ad9ba4ad4bafc"
POLICY_MARKER = "KAN:d201f1cc2a8d151fa0358c2c0db26fd1d217e409|KOO:14df7edd91954e92c96e593b4432fd6441f3833a|aggregate_only-v1"
MAX_INPUT = 16384
MAX_COUNT = 10**9
MAX_TICK = 2**53 - 1
TOP_FIELDS = frozenset({"schema_version", "producer_blob", "receipt", "receipt_source_id",
                       "event_context", "data_class", "policy", "sources", "authority"})
RECEIPT_FIELDS = frozenset({"publication_id", "distribution_target", "delivery_state",
    "external_chat_id", "external_message_id", "comments_count", "reaction_total",
    "member_count", "personal_data_exported", "raw_comment_exported",
    "production_publication", "privacy_mode", "privacy_policy_marker"})

class BridgeError(ValueError):
    """Только фиксированный код: неизвестные поля и содержимое не отражаются в ошибке."""

def require(ok, code="BLOCKED_BRIDGE_SCHEMA"):
    if not ok:
        raise BridgeError(code)

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def integer(value, low=0, high=MAX_TICK):
    return type(value) is int and low <= value <= high

def matches(value, pattern):
    return type(value) is str and re.fullmatch(pattern, value) is not None

def closed(value, names, code="BLOCKED_BRIDGE_SCHEMA"):
    require(type(value) is dict and set(value) == set(names), code)

def strict_json(data):
    require(type(data) is bytes and 0 < len(data) <= MAX_INPUT, "BLOCKED_BRIDGE_INPUT_SIZE")
    def pairs(items):
        obj = {}
        for key, value in items:
            require(key not in obj, "BLOCKED_BRIDGE_DUPLICATE_KEY")
            obj[key] = value
        return obj
    def nonfinite(_):
        raise BridgeError("BLOCKED_BRIDGE_SCHEMA")
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite)
        canonical(value)  # Проверить Unicode, включая одиночные суррогаты.
        return value
    except BridgeError:
        raise
    except (ValueError, UnicodeError, RecursionError, TypeError):
        raise BridgeError("BLOCKED_BRIDGE_SCHEMA") from None

@dataclass(frozen=True)
class ArtifactRef:
    repository: str
    path: str
    commit: str
    blob: str
    def __post_init__(self):
        require(matches(self.repository, r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"),
                "BLOCKED_BRIDGE_IDENTITY")
        require(matches(self.path, r"[A-Za-z0-9_./-]{1,256}") and
                all(p not in ("", ".", "..") for p in self.path.split("/")),
                "BLOCKED_BRIDGE_IDENTITY")
        require(matches(self.commit, r"[0-9a-f]{40}") and matches(self.blob, r"[0-9a-f]{40}"),
                "BLOCKED_BRIDGE_IDENTITY")

@dataclass(frozen=True)
class Authority:
    requester_id: str
    task: ArtifactRef
    writer: ArtifactRef
    decision: ArtifactRef
    scope: str
    def __post_init__(self):
        require(matches(self.requester_id, r"[A-Z][A-Z0-9]{1,15}"), "BLOCKED_BRIDGE_IDENTITY")
        require(all(type(v) is ArtifactRef for v in (self.task, self.writer, self.decision)),
                "BLOCKED_BRIDGE_IDENTITY")
        require(self.scope == SCOPE, "BLOCKED_BRIDGE_AUTHORITY")

@dataclass(frozen=True)
class AdmissionRequest:
    request_sha256: str
    authority: Authority
    discussion_id: str
    receipt_sha256: str
    data_class: str
    at_tick: int
    expires_tick: int

@dataclass(frozen=True)
class Grant:
    """Возвращается внешним доверенным verifier, не читается из входного JSON."""
    request_sha256: str
    authority_sha256: str
    data_class: str
    not_before_tick: int
    valid_until_tick: int
    retention_limit_tick: int

@dataclass(frozen=True)
class BridgeResult:
    event: object = field(repr=False)
    request_sha256: str
    receipt_sha256: str
    authority: Authority
    input_data_class: str
    receipt_source_id: str
    boundary: str = field(default="Phase1B.Gateway.safe_receipt", init=False)
    status: str = field(default="converted_input_not_project_acceptance", init=False)
    dispatch_performed: bool = field(default=False, init=False)
    executable_task_created: bool = field(default=False, init=False)
    candidate_task_approved: bool = field(default=False, init=False)

def load_core(path: Path) -> ModuleType:
    try:
        data = path.read_bytes()
    except OSError:
        raise BridgeError("BLOCKED_BRIDGE_CORE_UNAVAILABLE") from None
    require(git_blob(data) == CORE_BLOB and sha(data) == CORE_SHA256, "BLOCKED_BRIDGE_CORE_IDENTITY")
    module = ModuleType("_normalized_bridge_core_" + CORE_BLOB)
    module.__file__ = str(path)
    sys.modules[module.__name__] = module
    exec(compile(data, str(path), "exec"), module.__dict__)
    return module

class Bridge:
    def __init__(self, core_path: Path):
        self.core = load_core(core_path)

    def convert(self, data: bytes,
                verifier: Callable[[AdmissionRequest], Grant | None] | None = None) -> BridgeResult:
        obj = strict_json(data)
        closed(obj, TOP_FIELDS)
        require(obj["schema_version"] == SCHEMA, "BLOCKED_BRIDGE_SCHEMA_VERSION")
        require(obj["producer_blob"] == PRODUCER_BLOB, "BLOCKED_BRIDGE_PRODUCER_IDENTITY")
        receipt = obj["receipt"]
        closed(receipt, RECEIPT_FIELDS)
        for name in ("publication_id", "distribution_target"):
            require(matches(receipt[name], r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}"),
                    "BLOCKED_BRIDGE_IDENTITY")
        require(integer(receipt["external_chat_id"], -MAX_TICK) and receipt["external_chat_id"] != 0
                and integer(receipt["external_message_id"], 1), "BLOCKED_BRIDGE_IDENTITY")
        require(receipt["delivery_state"] == "delivered_verified", "BLOCKED_BRIDGE_DELIVERY_STATE")
        require(receipt["privacy_mode"] == "aggregate_only" and
                receipt["privacy_policy_marker"] == POLICY_MARKER, "BLOCKED_BRIDGE_PRIVACY")
        require(all(receipt[k] is False for k in
                ("personal_data_exported", "raw_comment_exported", "production_publication")),
                "BLOCKED_BRIDGE_PRIVACY")
        require(integer(receipt["comments_count"], high=MAX_COUNT) and
                integer(receipt["reaction_total"], high=MAX_COUNT) and
                (receipt["member_count"] is None or integer(receipt["member_count"], high=MAX_COUNT)),
                "BLOCKED_BRIDGE_COUNTS")

        ctx = obj["event_context"]
        closed(ctx, {"discussion_id", "event_id", "sequence", "at_tick"})
        require(matches(ctx["discussion_id"], r"discussion_[0-9a-f]{32}") and
                matches(ctx["event_id"], r"event_[0-9a-f]{32}"), "BLOCKED_BRIDGE_IDENTITY")
        require(integer(ctx["sequence"], 1) and integer(ctx["at_tick"]), "BLOCKED_BRIDGE_IDENTITY")
        require(type(obj["data_class"]) is str and obj["data_class"] in
                ("synthetic", "phase1b_aggregate_minimized"), "BLOCKED_BRIDGE_DATA_CLASS")
        policy = obj["policy"]
        closed(policy, {"privacy_class", "retention_class", "expires_tick"})
        privacy, source_kind = (("synthetic", "synthetic_fixture") if obj["data_class"] == "synthetic"
                                else ("minimized_derived", "normalized_projection"))
        require(policy["privacy_class"] == privacy, "BLOCKED_BRIDGE_PRIVACY")
        require(type(policy["retention_class"]) is str and
                policy["retention_class"] in ("memory_only", "synthetic_snapshot") and
                (privacy == "synthetic" or policy["retention_class"] == "memory_only"),
                "BLOCKED_BRIDGE_RETENTION")
        require(integer(policy["expires_tick"]) and policy["expires_tick"] > ctx["at_tick"],
                "BLOCKED_BRIDGE_EXPIRED")
        sources = obj["sources"]
        require(type(sources) is list and 1 <= len(sources) <= 8, "BLOCKED_BRIDGE_SOURCE")
        receipt_sha = sha(canonical(receipt))
        selected = []
        source_ids = set()
        for source in sources:
            closed(source, {"scope", "source_id", "version_sha256", "kind"}, "BLOCKED_BRIDGE_SOURCE")
            require(source["scope"] == ctx["discussion_id"] and
                    matches(source["source_id"], r"source_[0-9a-f]{32}") and
                    matches(source["version_sha256"], r"[0-9a-f]{64}") and
                    source["kind"] == source_kind, "BLOCKED_BRIDGE_SOURCE")
            require(source["source_id"] not in source_ids, "BLOCKED_BRIDGE_SOURCE")
            source_ids.add(source["source_id"])
            if source["source_id"] == obj["receipt_source_id"]:
                selected.append(source)
        require(matches(obj["receipt_source_id"], r"source_[0-9a-f]{32}") and len(selected) == 1
                and selected[0]["version_sha256"] == receipt_sha, "BLOCKED_BRIDGE_SOURCE_IDENTITY")

        raw_auth = obj["authority"]
        closed(raw_auth, {"requester_id", "task", "writer", "decision", "scope"},
               "BLOCKED_BRIDGE_AUTHORITY")
        refs = {}
        for name in ("task", "writer", "decision"):
            closed(raw_auth[name], {"repository", "path", "commit", "blob"}, "BLOCKED_BRIDGE_IDENTITY")
            refs[name] = ArtifactRef(**raw_auth[name])
        auth = Authority(raw_auth["requester_id"], refs["task"], refs["writer"],
                         refs["decision"], raw_auth["scope"])
        request_sha = sha(canonical(obj))
        check = AdmissionRequest(request_sha, auth, ctx["discussion_id"], receipt_sha,
                                 obj["data_class"], ctx["at_tick"], policy["expires_tick"])
        require(callable(verifier), "BLOCKED_BRIDGE_AUTHORITY")
        try:
            grant = verifier(check)
        except Exception:
            raise BridgeError("BLOCKED_BRIDGE_AUTHORITY") from None
        require(type(grant) is Grant, "BLOCKED_BRIDGE_AUTHORITY")
        require(grant.request_sha256 == request_sha and
                grant.authority_sha256 == sha(canonical(asdict(auth))) and
                grant.data_class == obj["data_class"], "BLOCKED_BRIDGE_AUTHORITY")
        require(all(integer(t) for t in (grant.not_before_tick, grant.valid_until_tick,
                                        grant.retention_limit_tick)), "BLOCKED_BRIDGE_AUTHORITY")
        require(grant.not_before_tick <= ctx["at_tick"] < grant.valid_until_tick,
                "BLOCKED_BRIDGE_AUTHORITY_EXPIRED")
        require(policy["expires_tick"] <= grant.retention_limit_tick, "BLOCKED_BRIDGE_RETENTION")
        # Никаких выводов о теме, позиции, согласии или фактическом числе участников.
        members = "неизвестно" if receipt["member_count"] is None else str(receipt["member_count"])
        derived = ("Квитанция Phase 1B: учтено комментариев=" + str(receipt["comments_count"]) +
                   "; агрегат реакций=" + str(receipt["reaction_total"]) +
                   "; member_count=" + members + ". Содержание обсуждения не представлено.")
        try:
            event = self.core.NormalizedEvent(
                ctx["discussion_id"], ctx["event_id"], ctx["sequence"], ctx["at_tick"],
                "observe", "fact_claim", derived, (), None,
                tuple(self.core.SourceRef(**s) for s in sources),
                self.core.RetentionPrivacy(**policy))
        except (self.core.CoreError, TypeError, ValueError):
            raise BridgeError("FAIL_BRIDGE_CORE_CONTRACT") from None
        return BridgeResult(event, request_sha, receipt_sha, auth,
                            obj["data_class"], obj["receipt_source_id"])
