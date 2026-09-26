"""Offline/synthetic tests. No Commander, provider or host access."""

import hashlib
import json
import socket
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

from integration import (DEVICE_IDS, HOSTS, IPS, NODES, PROFILE_SHA256, State,
                         gate_action, parse_mapping, select_control_path)


ROOT = Path(__file__).parent
RAW = (ROOT / "mapping.current.json").read_bytes()
HASH = hashlib.sha256(RAW).hexdigest()
REF = "a" * 40


def route_evidence(node="burzh", ip=IPS[0], outcome="HEALTHY", status=None):
    trace = []
    if ip == IPS[1]:
        trace.append({"node": node, "target_ip": IPS[0], "outcome": "TARGET_IP_FAILURE"})
    last = {"node": node, "target_ip": ip, "outcome": outcome}
    if status is not None:
        last["http_status"] = status
    trace.append(last)
    return {"router_package_tree": "fc1bb2751cc5d662037a037fdecf3ece69f07adb",
            "profile_sha256": PROFILE_SHA256, "selected_node": node, "selected_ip": ip,
            "outcome": outcome, "http_status": status, "evidence_ref": REF,
            "manual_node_selection": True, "trace": trace}


def inventory(node="burzh", available=True):
    idx = NODES.index(node)
    return {"device_id": DEVICE_IDS[idx], "host": HOSTS[idx],
            "available": available, "evidence_ref": REF}


def select(node="burzh", **changes):
    params = {"selected_node": node, "route_evidence": route_evidence(node),
              "inventory": inventory(node), "manual_marker": "OPERATOR_SELECTED:" + node,
              "action_id": "READ_ONLY_ADMIN_CHECK_R01"}
    params.update(changes)
    return select_control_path(parse_mapping(RAW, HASH), **params)


class IntegrationTests(unittest.TestCase):
    def test_all_three_exact_mappings(self):
        for i, node in enumerate(NODES):
            with self.subTest(node=node):
                result = select(node)
                self.assertEqual((result["outcome"], result["commander_device_id"]),
                                 (State.CONTROL_PATH_READY.value, DEVICE_IDS[i]))

    def test_unknown_node_rejected(self):
        self.assertEqual(select_control_path(parse_mapping(RAW, HASH), selected_node="unknown",
                                             route_evidence={}, inventory={}, manual_marker="OPERATOR_SELECTED:unknown",
                                             action_id="READ_ONLY_ADMIN_CHECK_R01")["outcome"],
                         State.COMMANDER_DEVICE_UNKNOWN.value)

    def test_unknown_or_missing_commander_identity_rejected(self):
        inv = inventory()
        inv["device_id"] = "00000000-0000-0000-0000-000000000000"
        self.assertEqual(select(inventory=inv)["outcome"], State.COMMANDER_DEVICE_UNKNOWN.value)
        self.assertEqual(select(inventory={})["outcome"], State.COMMANDER_DEVICE_UNKNOWN.value)

    def test_unavailable_device_does_not_fallback(self):
        result = select(inventory=inventory(available=False))
        self.assertEqual((result["outcome"], result["node"]),
                         (State.COMMANDER_DEVICE_UNAVAILABLE.value, "burzh"))
        self.assertNotEqual(result["commander_device_id"], DEVICE_IDS[1])

    def test_unhealthy_route_blocks(self):
        r = route_evidence(outcome="TARGET_IP_FAILURE")
        self.assertEqual(select(route_evidence=r)["outcome"], State.ROUTE_NOT_HEALTHY.value)

    def test_certificate_failure_stops(self):
        r = route_evidence(outcome="TLS_CERTIFICATE_FAILURE")
        self.assertEqual(select(route_evidence=r)["outcome"], State.ROUTE_NOT_HEALTHY.value)

    def test_http_403_429_5xx_are_not_transport_failures(self):
        for status in (403, 429, 500, 503):
            with self.subTest(status=status):
                r = route_evidence(outcome="HTTP_APPLICATION_RESPONSE", status=status)
                self.assertEqual(select(route_evidence=r)["outcome"], State.CONTROL_PATH_READY.value)

    def test_second_ip_requires_explicit_first_ip_failure(self):
        r = route_evidence(ip=IPS[1])
        self.assertEqual(select(route_evidence=r)["outcome"], State.CONTROL_PATH_READY.value)
        r["trace"][0]["outcome"] = "HEALTHY"
        self.assertEqual(select(route_evidence=r)["outcome"], State.ROUTE_NOT_HEALTHY.value)

    def test_missing_task_authority_blocks_execution(self):
        result = gate_action(select(), verified_task_authority=None, operator_confirmation=True)
        self.assertEqual(result["outcome"], State.TASK_AUTHORITY_MISSING.value)

    def test_task_authority_must_match_device_action_and_operator_confirmation(self):
        authority = {"action_id": "READ_ONLY_ADMIN_CHECK_R01", "node": "burzh",
                     "device_id": DEVICE_IDS[0], "authority_ref": REF, "verified_by_supervisor": True}
        self.assertEqual(gate_action(select(), verified_task_authority=authority,
                                     operator_confirmation=False)["outcome"], State.CONTROL_PATH_EXECUTION_BLOCKED.value)
        self.assertEqual(gate_action(select(), verified_task_authority=authority,
                                     operator_confirmation=True)["outcome"], State.CONTROL_PATH_READY.value)
        authority["device_id"] = DEVICE_IDS[1]
        self.assertEqual(gate_action(select(), verified_task_authority=authority,
                                     operator_confirmation=True)["outcome"], State.CONTROL_PATH_EXECUTION_BLOCKED.value)

    def test_manual_override_is_explicit_and_auditable(self):
        result = select("mazhor")
        self.assertEqual((result["node"], result["manual_selection_marker"]),
                         ("mazhor", "OPERATOR_SELECTED:mazhor"))
        self.assertEqual(select("mazhor", manual_marker="auto")["outcome"],
                         State.CONTROL_PATH_EXECUTION_BLOCKED.value)
        r = route_evidence("mazhor")
        r["manual_node_selection"] = False
        self.assertEqual(select("mazhor", route_evidence=r)["outcome"], State.ROUTE_NOT_HEALTHY.value)

    def test_wrong_profile_or_mapping_digest_blocks(self):
        with self.assertRaisesRegex(ValueError, "MAPPING_DIGEST_MISMATCH"):
            parse_mapping(RAW, "0" * 64)
        r = route_evidence()
        r["profile_sha256"] = "0" * 64
        self.assertEqual(select(route_evidence=r)["outcome"], State.ROUTE_NOT_HEALTHY.value)

    def test_no_private_payload_in_audit(self):
        result = json.dumps(select())
        for forbidden in ("password", "Authorization", "Cookie", "https://", "command_payload"):
            self.assertNotIn(forbidden, result)

    @patch.object(socket, "create_connection")
    @patch.object(subprocess, "run")
    def test_no_network_or_subprocess(self, run, connect):
        select("erefia")
        run.assert_not_called()
        connect.assert_not_called()


if __name__ == "__main__":
    unittest.main()
