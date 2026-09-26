"""Operator-assisted fixed-IP route -> Commander device selection.

Pure local planner. No network, DNS, credentials, provider API or host execution.
The caller must independently verify route evidence, inventory and task authority.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any


PROFILE_SHA256 = "b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac"
PACKAGE_TREE = "fc1bb2751cc5d662037a037fdecf3ece69f07adb"
IPS = ("104.18.32.47", "172.64.155.209")
NODES = ("burzh", "mazhor", "erefia")
DEVICE_IDS = (
    "dd09a197-f716-4dd6-80bb-7f8e5d8260ff",
    "830038a0-232b-4d83-b52d-0e9973126165",
    "c55d5659-f2c8-416d-8b40-9bac8c80c30d",
)
HOSTS = ("ruvds-xnqc6", "p552203.kvmvps", "ruvds-ygo0w")
ACTION_ID = re.compile(r"^[A-Z][A-Z0-9_]{2,79}$")
EVIDENCE_ID = re.compile(r"^[0-9a-f]{40}$")


class State(str, Enum):
    ROUTE_NOT_HEALTHY = "ROUTE_NOT_HEALTHY"
    COMMANDER_DEVICE_UNKNOWN = "COMMANDER_DEVICE_UNKNOWN"
    COMMANDER_DEVICE_UNAVAILABLE = "COMMANDER_DEVICE_UNAVAILABLE"
    TASK_AUTHORITY_MISSING = "TASK_AUTHORITY_MISSING"
    CONTROL_PATH_READY = "CONTROL_PATH_READY"
    CONTROL_PATH_EXECUTION_BLOCKED = "CONTROL_PATH_EXECUTION_BLOCKED"


@dataclass(frozen=True)
class Device:
    node: str
    host: str
    device_id: str
    evidence_ref: str


def _unique_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("DUPLICATE_KEY")
        result[key] = value
    return result


def parse_mapping(raw: bytes, expected_sha256: str) -> tuple[Device, ...]:
    """Compare exact published mapping bytes to an independently supplied digest."""
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError("MAPPING_DIGEST_MISMATCH")
    obj = json.loads(raw, object_pairs_hook=_unique_pairs)
    if type(obj) is not dict or set(obj) != {"schema_version", "status", "router_package_tree", "router_profile_sha256", "node_priority", "ip_order", "devices"}:
        raise ValueError("MAPPING_SCHEMA")
    if obj["schema_version"] != "fixed-ip-commander-mapping-v1" or obj["status"] != "IDENTITY_FROM_PUBLISHED_EVIDENCE_CURRENT_AVAILABILITY_UNKNOWN":
        raise ValueError("MAPPING_STATUS")
    if obj["router_package_tree"] != PACKAGE_TREE or obj["router_profile_sha256"] != PROFILE_SHA256 or obj["node_priority"] != list(NODES) or obj["ip_order"] != list(IPS):
        raise ValueError("ROUTER_IDENTITY_MISMATCH")
    rows = obj["devices"]
    if type(rows) is not list or len(rows) != 3:
        raise ValueError("MAPPING_DEVICES")
    devices = []
    for i, row in enumerate(rows):
        if type(row) is not dict or set(row) != {"node", "host", "commander_device_id", "evidence_ref"}:
            raise ValueError("MAPPING_DEVICES")
        if (row["node"], row["host"], row["commander_device_id"]) != (NODES[i], HOSTS[i], DEVICE_IDS[i]):
            raise ValueError("COMMANDER_DEVICE_UNKNOWN")
        if type(row["evidence_ref"]) is not str or not row["evidence_ref"]:
            raise ValueError("MAPPING_EVIDENCE_MISSING")
        devices.append(Device(row["node"], row["host"], row["commander_device_id"], row["evidence_ref"]))
    return tuple(devices)


def _audit(state: State, *, node: str | None, device_id: str | None,
           ip: str | None, evidence_ref: str | None, manual_marker: str | None,
           action_id: str | None) -> dict[str, Any]:
    # Closed output; never include command content, token, URL, host response or credentials.
    return {"schema_version": "fixed-ip-commander-audit-v1", "outcome": state.value,
            "node": node, "commander_device_id": device_id, "selected_ip": ip,
            "health_evidence_ref": evidence_ref, "manual_selection_marker": manual_marker,
            "requested_action_id": action_id}


def select_control_path(devices: tuple[Device, ...], *, selected_node: str,
                        route_evidence: dict[str, Any], inventory: dict[str, Any],
                        manual_marker: str, action_id: str) -> dict[str, Any]:
    """Select exactly one device; no fallback and no Commander invocation.

    Inventory and route attestations must be verified by a future supervisor.
    This local function validates shape and consistency, not signatures/currentness.
    """
    if selected_node not in NODES:
        return _audit(State.COMMANDER_DEVICE_UNKNOWN, node=None, device_id=None, ip=None,
                      evidence_ref=None, manual_marker=None, action_id=None)
    if type(action_id) is not str or not ACTION_ID.fullmatch(action_id) or manual_marker != "OPERATOR_SELECTED:" + selected_node:
        return _audit(State.CONTROL_PATH_EXECUTION_BLOCKED, node=selected_node, device_id=None,
                      ip=None, evidence_ref=None, manual_marker=None, action_id=None)
    if type(route_evidence) is not dict or set(route_evidence) != {"router_package_tree", "profile_sha256", "selected_node", "selected_ip", "outcome", "http_status", "evidence_ref", "manual_node_selection", "trace"}:
        return _audit(State.ROUTE_NOT_HEALTHY, node=selected_node, device_id=None, ip=None,
                      evidence_ref=None, manual_marker=manual_marker, action_id=action_id)
    ref = route_evidence["evidence_ref"]
    ip = route_evidence["selected_ip"]
    if (route_evidence["router_package_tree"] != PACKAGE_TREE or route_evidence["profile_sha256"] != PROFILE_SHA256
            or route_evidence["selected_node"] != selected_node or ip not in IPS
            or route_evidence["outcome"] not in ("HEALTHY", "HTTP_APPLICATION_RESPONSE")
            or route_evidence["manual_node_selection"] is not True
            or type(ref) is not str or not EVIDENCE_ID.fullmatch(ref)):
        return _audit(State.ROUTE_NOT_HEALTHY, node=selected_node, device_id=None, ip=None,
                      evidence_ref=None, manual_marker=manual_marker, action_id=action_id)
    trace = route_evidence["trace"]
    status = route_evidence["http_status"]
    if route_evidence["outcome"] == "HTTP_APPLICATION_RESPONSE":
        if type(status) is not int or not 100 <= status <= 599:
            return _audit(State.ROUTE_NOT_HEALTHY, node=selected_node, device_id=None, ip=None,
                          evidence_ref=None, manual_marker=manual_marker, action_id=action_id)
        last = {"node": selected_node, "target_ip": ip, "outcome": route_evidence["outcome"], "http_status": status}
    else:
        if status is not None:
            return _audit(State.ROUTE_NOT_HEALTHY, node=selected_node, device_id=None, ip=None,
                          evidence_ref=None, manual_marker=manual_marker, action_id=action_id)
        last = {"node": selected_node, "target_ip": ip, "outcome": route_evidence["outcome"]}
    if (type(trace) is not list or len(trace) != (1 if ip == IPS[0] else 2)
            or any(type(item) is not dict for item in trace)
            or (ip == IPS[1] and trace[0] != {"node": selected_node, "target_ip": IPS[0], "outcome": "TARGET_IP_FAILURE"})
            or trace[-1] != last):
        return _audit(State.ROUTE_NOT_HEALTHY, node=selected_node, device_id=None, ip=None,
                      evidence_ref=None, manual_marker=manual_marker, action_id=action_id)
    if type(inventory) is not dict or set(inventory) != {"device_id", "host", "available", "evidence_ref"}:
        return _audit(State.COMMANDER_DEVICE_UNKNOWN, node=selected_node, device_id=None,
                      ip=ip, evidence_ref=ref, manual_marker=manual_marker, action_id=action_id)
    device = devices[NODES.index(selected_node)]
    if inventory["device_id"] != device.device_id or inventory["host"] != device.host or type(inventory["evidence_ref"]) is not str or not EVIDENCE_ID.fullmatch(inventory["evidence_ref"]):
        return _audit(State.COMMANDER_DEVICE_UNKNOWN, node=selected_node, device_id=None,
                      ip=ip, evidence_ref=ref, manual_marker=manual_marker, action_id=action_id)
    if inventory["available"] is not True:
        return _audit(State.COMMANDER_DEVICE_UNAVAILABLE, node=selected_node, device_id=device.device_id,
                      ip=ip, evidence_ref=ref, manual_marker=manual_marker, action_id=action_id)
    return _audit(State.CONTROL_PATH_READY, node=selected_node, device_id=device.device_id,
                  ip=ip, evidence_ref=ref, manual_marker=manual_marker, action_id=action_id)


def gate_action(selection: dict[str, Any], *, verified_task_authority: dict[str, Any] | None,
                operator_confirmation: bool) -> dict[str, Any]:
    """Separate task authority check. Returns a *selector*, never runs a command."""
    if selection.get("outcome") != State.CONTROL_PATH_READY.value:
        return {**selection, "outcome": State.CONTROL_PATH_EXECUTION_BLOCKED.value}
    if verified_task_authority is None:
        return {**selection, "outcome": State.TASK_AUTHORITY_MISSING.value}
    if (type(verified_task_authority) is not dict
            or set(verified_task_authority) != {"action_id", "node", "device_id", "authority_ref", "verified_by_supervisor"}
            or verified_task_authority["verified_by_supervisor"] is not True
            or verified_task_authority["action_id"] != selection["requested_action_id"]
            or verified_task_authority["node"] != selection["node"]
            or verified_task_authority["device_id"] != selection["commander_device_id"]
            or type(verified_task_authority["authority_ref"]) is not str
            or not EVIDENCE_ID.fullmatch(verified_task_authority["authority_ref"])
            or operator_confirmation is not True):
        return {**selection, "outcome": State.CONTROL_PATH_EXECUTION_BLOCKED.value}
    # Selection is ready for an independently authorized operator action.
    # No command payload or API invocation is generated here.
    return {**selection, "outcome": State.CONTROL_PATH_READY.value}


def offline_fixture_plan(mapping_path: Path, mapping_digest: str, fixture_path: Path) -> dict[str, Any]:
    devices = parse_mapping(mapping_path.read_bytes(), mapping_digest)
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"), object_pairs_hook=_unique_pairs)
    if type(fixture) is not dict or set(fixture) != {"selected_node", "route_evidence", "inventory", "manual_marker", "action_id", "verified_task_authority", "operator_confirmation"}:
        raise ValueError("INVALID_FIXTURE")
    selected = select_control_path(devices, selected_node=fixture["selected_node"],
                                   route_evidence=fixture["route_evidence"], inventory=fixture["inventory"],
                                   manual_marker=fixture["manual_marker"], action_id=fixture["action_id"])
    return gate_action(selected, verified_task_authority=fixture["verified_task_authority"],
                       operator_confirmation=fixture["operator_confirmation"])
