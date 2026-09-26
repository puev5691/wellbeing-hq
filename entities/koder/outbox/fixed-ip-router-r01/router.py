"""Fixed-IP administration route planner r0.1.

No provider request is made by this module. Observations come from a separately
authorized node-local probe. The caller must establish profile and node
admission independently; this planner is not a security authority.
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Mapping, Sequence


TARGET = "chatgpt.com"
NODE_ORDER = ("burzh", "mazhor", "erefia")
NODE_HOSTS = ("ruvds-xnqc6", "p552203.kvmvps", "ruvds-ygo0w")


class Outcome(str, Enum):
    HEALTHY = "HEALTHY"
    TARGET_IP_FAILURE = "TARGET_IP_FAILURE"
    NODE_FAILURE = "NODE_FAILURE"
    TLS_CERTIFICATE_FAILURE = "TLS_CERTIFICATE_FAILURE"
    HTTP_APPLICATION_RESPONSE = "HTTP_APPLICATION_RESPONSE"
    FIXED_IP_SET_EXHAUSTED = "FIXED_IP_SET_EXHAUSTED"


class AdmissionError(ValueError):
    pass


@dataclass(frozen=True)
class Observation:
    outcome: Outcome
    http_status: int | None = None

    def __post_init__(self) -> None:
        if self.outcome is Outcome.HTTP_APPLICATION_RESPONSE:
            if type(self.http_status) is not int or not 100 <= self.http_status <= 599:
                raise ValueError("HTTP response requires valid status")
        elif self.http_status is not None:
            raise ValueError("HTTP status is only valid for application response")


@dataclass(frozen=True)
class Profile:
    profile_id: str
    revision: int
    status: str
    ip_set: tuple[str, ...]
    node_order: tuple[str, ...]
    node_hosts: tuple[str, ...]
    digest: str


def load_profile(raw: bytes) -> Profile:
    """Validate exact versioned bytes; do not resolve DNS or discover IPs."""
    digest = hashlib.sha256(raw).hexdigest()
    try:
        obj = json.loads(raw, object_pairs_hook=_unique_pairs)
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise AdmissionError("INVALID_PROFILE_JSON") from exc
    required = {"schema_version", "profile_id", "revision", "status", "logical_target",
                "tls_sni", "http_host", "certificate_name", "ip_set", "nodes",
                "source_evidence_refs", "validation_evidence_refs", "supersedes"}
    if type(obj) is not dict or set(obj) != required:
        raise AdmissionError("INVALID_PROFILE_SCHEMA")
    if obj["schema_version"] != "fixed-ip-router-profile-v1":
        raise AdmissionError("INVALID_PROFILE_VERSION")
    if any(obj[k] != TARGET for k in ("logical_target", "tls_sni", "http_host", "certificate_name")):
        raise AdmissionError("TLS_IDENTITY_MISMATCH")
    if type(obj["profile_id"]) is not str or not obj["profile_id"] or type(obj["revision"]) is not int or obj["revision"] < 1:
        raise AdmissionError("INVALID_PROFILE_IDENTITY")
    if obj["status"] not in ("DOCUMENTED_CURRENT_MEASURED_SET", "CANDIDATE", "ADMITTED", "STALE", "SUPERSEDED"):
        raise AdmissionError("INVALID_PROFILE_STATUS")
    ips = obj["ip_set"]
    if type(ips) is not list or len(ips) != 2 or any(type(ip) is not str for ip in ips) or len(set(ips)) != 2:
        raise AdmissionError("INVALID_IP_SET")
    try:
        if any(type(ip) is not str or str(ipaddress.IPv4Address(ip)) != ip for ip in ips):
            raise ValueError("noncanonical IPv4")
    except (ipaddress.AddressValueError, ValueError) as exc:
        raise AdmissionError("INVALID_IP_SET") from exc
    nodes = obj["nodes"]
    if type(nodes) is not list or len(nodes) != 3 or any(type(n) is not dict or set(n) != {"name", "host_identity"} for n in nodes):
        raise AdmissionError("INVALID_NODES")
    names = tuple(n["name"] for n in nodes)
    hosts = tuple(n["host_identity"] for n in nodes)
    if names != NODE_ORDER or hosts != NODE_HOSTS:
        raise AdmissionError("NODE_IDENTITY_MISMATCH")
    if any(type(obj[k]) is not list or not obj[k] or any(type(v) is not str or not v for v in obj[k]) for k in ("source_evidence_refs", "validation_evidence_refs")):
        raise AdmissionError("MISSING_EVIDENCE_REFS")
    if obj["supersedes"] is not None and (type(obj["supersedes"]) is not str or not obj["supersedes"]):
        raise AdmissionError("INVALID_SUPERSESSION")
    return Profile(obj["profile_id"], obj["revision"], obj["status"], tuple(ips), names, hosts, digest)


def _unique_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def admit(profile: Profile, *, admitted_digest: str, admitted_id: str,
          admitted_revision: int, current_generation: int, profile_generation: int) -> None:
    """Compare against independently verified admission facts supplied by supervisor.

    This function does NOT validate signatures or create operational authority.
    """
    if profile.status != "ADMITTED" or profile.digest != admitted_digest or profile.profile_id != admitted_id or profile.revision != admitted_revision:
        raise AdmissionError("UNADMITTED_PROFILE")
    if type(current_generation) is not int or type(profile_generation) is not int or current_generation != profile_generation:
        raise AdmissionError("STALE_PROFILE")


def route(profile: Profile, observations: Mapping[tuple[str, str], Observation], *,
          manual_node: str | None = None) -> dict[str, object]:
    """Deterministic node/IP order. Called only after independent admission."""
    if manual_node is not None and manual_node not in profile.node_order:
        raise AdmissionError("UNADMITTED_MANUAL_NODE")
    if manual_node is None:
        nodes: Sequence[str] = profile.node_order
    else:
        # Manual skip is explicit and auditable; no automatic priority mutation.
        nodes = profile.node_order[profile.node_order.index(manual_node):]
    trace: list[dict[str, str | int]] = []
    for node in nodes:
        for ip in profile.ip_set:
            item = observations.get((node, ip))
            if item is None:
                raise AdmissionError("MISSING_OBSERVATION")
            trace.append(_entry(node, ip, item))
            if item.outcome is Outcome.TLS_CERTIFICATE_FAILURE:
                return _result(profile, Outcome.TLS_CERTIFICATE_FAILURE, node, ip, trace)
            if item.outcome is Outcome.NODE_FAILURE:
                break  # node unavailable; the other IP cannot repair its execution path
            if item.outcome in (Outcome.HEALTHY, Outcome.HTTP_APPLICATION_RESPONSE):
                return _result(profile, item.outcome, node, ip, trace)
            if item.outcome is not Outcome.TARGET_IP_FAILURE:
                raise AdmissionError("INVALID_OBSERVATION")
        # Both admitted IPs failed (or the whole node failed); only then next node.
    return _result(profile, Outcome.FIXED_IP_SET_EXHAUSTED, None, None, trace)


def _entry(node: str, ip: str, item: Observation) -> dict[str, str | int]:
    entry: dict[str, str | int] = {"node": node, "target_ip": ip, "outcome": item.outcome.value}
    if item.http_status is not None:
        entry["http_status"] = item.http_status
    return entry


def _result(profile: Profile, outcome: Outcome, node: str | None,
            ip: str | None, trace: list[dict[str, str | int]]) -> dict[str, object]:
    # Closed audit: no headers, URLs, tokens, cookies, private request or body.
    return {"schema_version": "fixed-ip-router-audit-v1", "profile_id": profile.profile_id,
            "profile_revision": profile.revision, "profile_sha256": profile.digest,
            "selected_node": node, "selected_ip": ip, "outcome": outcome.value,
            "trace": trace}


def offline_plan(profile_path: Path, admission_path: Path, observation_path: Path,
                 manual_node: str | None = None) -> dict[str, object]:
    profile = load_profile(profile_path.read_bytes())
    admission = json.loads(admission_path.read_text(encoding="utf-8"), object_pairs_hook=_unique_pairs)
    if type(admission) is not dict or set(admission) != {"admitted_digest", "admitted_id", "admitted_revision", "current_generation", "profile_generation"}:
        raise AdmissionError("INVALID_ADMISSION_RECORD")
    admit(profile, **admission)
    raw = json.loads(observation_path.read_text(encoding="utf-8"), object_pairs_hook=_unique_pairs)
    if type(raw) is not list:
        raise AdmissionError("INVALID_OBSERVATIONS")
    observations: dict[tuple[str, str], Observation] = {}
    for row in raw:
        if type(row) is not dict or set(row) != {"node", "ip", "outcome", "http_status"}:
            raise AdmissionError("INVALID_OBSERVATIONS")
        key = (row["node"], row["ip"])
        if key in observations or key[0] not in profile.node_order or key[1] not in profile.ip_set:
            raise AdmissionError("INVALID_OBSERVATIONS")
        observations[key] = Observation(Outcome(row["outcome"]), row["http_status"])
    return route(profile, observations, manual_node=manual_node)
