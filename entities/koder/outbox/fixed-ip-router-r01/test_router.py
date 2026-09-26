"""Deterministic offline/synthetic tests; no network or provider calls."""

import hashlib
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from router import AdmissionError, Observation, Outcome, admit, load_profile, route
from node_probe import probe_fixed_ip


ROOT = Path(__file__).parent
CURRENT = json.loads((ROOT / "profile.current.json").read_text(encoding="utf-8"))
IPS = CURRENT["ip_set"]
NODES = ("burzh", "mazhor", "erefia")


def profile_data(**changes):
    obj = dict(CURRENT)
    obj.update({"status": "ADMITTED", **changes})
    return json.dumps(obj, sort_keys=True).encode("utf-8")


def admitted(raw=None, **overrides):
    raw = raw or profile_data()
    p = load_profile(raw)
    claims = dict(admitted_digest=hashlib.sha256(raw).hexdigest(), admitted_id=p.profile_id,
                  admitted_revision=p.revision, current_generation=1, profile_generation=1)
    claims.update(overrides)
    admit(p, **claims)
    return p


def observations(default=Outcome.TARGET_IP_FAILURE):
    return {(n, ip): Observation(default) for n in NODES for ip in IPS}


class PlannerTests(unittest.TestCase):
    def test_current_fixture_is_not_operationally_admitted(self):
        p = load_profile((ROOT / "profile.current.json").read_bytes())
        with self.assertRaisesRegex(AdmissionError, "UNADMITTED_PROFILE"):
            admit(p, admitted_digest=p.digest, admitted_id=p.profile_id,
                  admitted_revision=p.revision, current_generation=1, profile_generation=1)

    def test_healthy_first_ip(self):
        obs = observations()
        obs[(NODES[0], IPS[0])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs)
        self.assertEqual((r["selected_node"], r["selected_ip"], len(r["trace"])), ("burzh", IPS[0], 1))

    def test_first_ip_fails_second_healthy_same_node(self):
        obs = observations()
        obs[(NODES[0], IPS[1])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs)
        self.assertEqual((r["selected_node"], r["selected_ip"], len(r["trace"])), ("burzh", IPS[1], 2))

    def test_both_ips_fail_then_secondary(self):
        obs = observations()
        obs[(NODES[1], IPS[0])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs)
        self.assertEqual((r["selected_node"], len(r["trace"])), ("mazhor", 3))

    def test_primary_node_unavailable_then_secondary(self):
        obs = observations()
        obs[(NODES[0], IPS[0])] = Observation(Outcome.NODE_FAILURE)
        obs[(NODES[1], IPS[0])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs)
        self.assertEqual((r["selected_node"], len(r["trace"])), ("mazhor", 2))

    def test_secondary_fails_then_tertiary(self):
        obs = observations()
        obs[(NODES[2], IPS[0])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs)
        self.assertEqual((r["selected_node"], len(r["trace"])), ("erefia", 5))

    def test_certificate_mismatch_stops_without_downgrade(self):
        obs = observations()
        obs[(NODES[0], IPS[0])] = Observation(Outcome.TLS_CERTIFICATE_FAILURE)
        obs[(NODES[0], IPS[1])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs)
        self.assertEqual((r["outcome"], r["selected_ip"], len(r["trace"])),
                         ("TLS_CERTIFICATE_FAILURE", IPS[0], 1))

    def test_http_statuses_are_application_responses(self):
        for code in (403, 429, 500, 503):
            with self.subTest(code=code):
                obs = observations()
                obs[(NODES[0], IPS[0])] = Observation(Outcome.HTTP_APPLICATION_RESPONSE, code)
                r = route(admitted(), obs)
                self.assertEqual((r["outcome"], r["trace"][0]["http_status"], len(r["trace"])),
                                 ("HTTP_APPLICATION_RESPONSE", code, 1))

    def test_stale_profile_and_generation(self):
        for state in ("STALE", "SUPERSEDED"):
            with self.subTest(state=state):
                p = load_profile(profile_data(status=state))
                with self.assertRaisesRegex(AdmissionError, "UNADMITTED_PROFILE"):
                    admit(p, admitted_digest=p.digest, admitted_id=p.profile_id,
                          admitted_revision=p.revision, current_generation=1, profile_generation=1)
        with self.assertRaisesRegex(AdmissionError, "STALE_PROFILE"):
            admitted(current_generation=2)

    def test_unadmitted_successor_even_if_tls_ip_looks_valid(self):
        raw = profile_data(profile_id="SUCCESSOR", revision=2, status="CANDIDATE",
                           ip_set=[IPS[1], "192.0.2.1"], supersedes=CURRENT["profile_id"])
        p = load_profile(raw)
        with self.assertRaisesRegex(AdmissionError, "UNADMITTED_PROFILE"):
            admit(p, admitted_digest=p.digest, admitted_id="SUCCESSOR",
                  admitted_revision=2, current_generation=2, profile_generation=2)

    def test_all_nodes_all_ips_exhausted(self):
        r = route(admitted(), observations())
        self.assertEqual((r["outcome"], r["selected_node"], len(r["trace"])),
                         ("FIXED_IP_SET_EXHAUSTED", None, 6))

    def test_manual_failover_is_explicit_and_constrained(self):
        obs = observations()
        obs[(NODES[1], IPS[0])] = Observation(Outcome.HEALTHY)
        r = route(admitted(), obs, manual_node="mazhor")
        self.assertEqual((r["selected_node"], len(r["trace"])), ("mazhor", 1))
        with self.assertRaisesRegex(AdmissionError, "UNADMITTED_MANUAL_NODE"):
            route(admitted(), obs, manual_node="unknown")

    def test_missing_observation_cannot_be_assumed_healthy(self):
        with self.assertRaisesRegex(AdmissionError, "MISSING_OBSERVATION"):
            route(admitted(), {})

    def test_identity_override_duplicate_key_and_digest_mismatch(self):
        with self.assertRaisesRegex(AdmissionError, "TLS_IDENTITY_MISMATCH"):
            load_profile(profile_data(tls_sni="192.0.2.1"))
        with self.assertRaisesRegex(AdmissionError, "INVALID_PROFILE_JSON"):
            load_profile(b'{"schema_version":"x","schema_version":"y"}')
        with self.assertRaisesRegex(AdmissionError, "UNADMITTED_PROFILE"):
            admitted(admitted_digest="0" * 64)

    def test_audit_contains_no_private_request_material(self):
        obs = observations()
        obs[(NODES[0], IPS[0])] = Observation(Outcome.HTTP_APPLICATION_RESPONSE, 403)
        result = json.dumps(route(admitted(), obs))
        for forbidden in ("Authorization", "Cookie", "body", "https://", "password"):
            self.assertNotIn(forbidden, result)


class FakeTLS:
    def __init__(self):
        self.written = None
        self.data = iter(b"HTTP/1.1 403 Forbidden\r\n")

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def sendall(self, payload):
        self.written = payload

    def recv(self, _length):
        return bytes((next(self.data),))


class FakeContext:
    def __init__(self, tls):
        self.tls = tls
        self.check_hostname = False
        self.verify_mode = None
        self.sni = None

    def wrap_socket(self, _raw, server_hostname):
        self.sni = server_hostname
        return self.tls


class ProbeContractTests(unittest.TestCase):
    @patch("node_probe.socket.create_connection")
    def test_hostname_cannot_trigger_dns(self, connect):
        self.assertEqual(probe_fixed_ip("chatgpt.com").outcome, Outcome.TARGET_IP_FAILURE)
        connect.assert_not_called()

    @patch("node_probe.ssl.create_default_context")
    @patch("node_probe.socket.create_connection")
    def test_node_local_probe_preserves_sni_host_certificate_check_and_ip(self, connect, make_context):
        tls = FakeTLS()
        ctx = FakeContext(tls)
        make_context.return_value = ctx
        result = probe_fixed_ip(IPS[0])
        self.assertEqual((result.outcome, result.http_status), (Outcome.HTTP_APPLICATION_RESPONSE, 403))
        self.assertEqual(connect.call_args.args[0], (IPS[0], 443))
        self.assertEqual(ctx.sni, "chatgpt.com")
        self.assertTrue(ctx.check_hostname)
        self.assertEqual(ctx.verify_mode, __import__("ssl").CERT_REQUIRED)
        self.assertIn(b"Host: chatgpt.com\r\n", tls.written)


if __name__ == "__main__":
    unittest.main()
