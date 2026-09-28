"""Only supervisor oracle self-tests with invented observations; NO backend test."""
import copy
import tempfile
import unittest
from pathlib import Path

from oracle import (canonical, evaluate, expected, identity, strict_load,
                    validate_fixture, validate_projection)

HERE = Path(__file__).resolve().parent


def synthetic_observation(f, case, state, response):
    events = []
    def add(kind, actor, barrier):
        core = {"kind": kind, "actor": actor, "barrier": barrier}
        events.append({**core, "event_identity": identity("STPC-EVIDENCE-R01",
                                                       {"ordinal": len(events), **core})})
    race = next((b for b in case["barriers"] if b.endswith("-RACE")), None)
    if race:
        add("ARRIVE", "P1", race); add("ARRIVE", "P2", race)
    if case["test_id"] == "T04":
        add("PAUSE", "P1", "B-T04-OLD-PAUSED")
    if case["test_id"] == "T10":
        add("HEALTHY_AUTH_READ", "SUPERVISOR", "B-T10-HEALTH")
    for b in case["release_order"]:
        if b == "B-T04-F2-COMMIT":
            add("AUTHORITATIVE_F2", "SUPERVISOR", b)
        add("RELEASE", "SUPERVISOR", b)
    return {"schema": "STPC_OBSERVATION_V1", "test_id": case["test_id"],
            "case_id": case["case_id"], "run_id": "SELFTEST-SYNTHETIC-ONLY",
            "initial_state_identity": identity("STPC-STATE-R01", f["states"][case["initial_state"]]),
            "schedule_identity": identity("STPC-FIXTURE-R01", case),
            "actor_actions": case["actions"], "barrier_events": events,
            "fault_proof": {"point": case["fault_point"],
                            "supervisor_event_identity": identity("STPC-EVIDENCE-R01", events)},
            "observed_responses": response, "authoritative_readback": state,
            "readback_provenance": {"authoritative": True, "healthy": True,
                                    "fault_injected": False,
                                    "readback_identity": identity("STPC-STATE-R01", state)},
            "transition_history": state["transition_history"], "integrity_status": "PASS",
            "overlap_proof": ({"barrier_id": race, "participants": ["P1", "P2"]}
                              if race else None)}


class OracleSelfTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = strict_load(HERE / "FIXTURES.json")
        cls.schedule = strict_load(HERE / "SCHEDULE.json")["cases"]
        cls.vectors = strict_load(HERE / "VECTORS.json")["vectors"]

    def test_frozen_fixture_and_vectors_match_independent_derivation(self):
        self.assertTrue(validate_fixture(self.fixture))
        self.assertEqual(len(self.schedule), 8)
        for case, vector in zip(self.schedule, self.vectors):
            states, allowed, forbidden = expected(self.fixture, case)
            self.assertEqual(vector["initial_projection"], self.fixture["states"][case["initial_state"]])
            self.assertEqual(vector["allowed_state_identities"],
                             [identity("STPC-STATE-R01", s) for s in states])
            self.assertEqual(vector["allowed_client_classifications"], sorted(allowed))
            self.assertEqual(vector["forbidden_outcomes"], sorted(forbidden))

    def test_all_synthetic_positive_oracle_paths(self):
        for case in self.schedule:
            with self.subTest(case=case["case_id"]):
                states, allowed, _ = expected(self.fixture, case)
                obs = synthetic_observation(self.fixture, case, states[0], sorted(allowed)[0])
                self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "PASS")

    def test_missing_evidence_is_unknown(self):
        case = self.schedule[0]; state, allowed, _ = expected(self.fixture, case)
        obs = synthetic_observation(self.fixture, case, state[0], sorted(allowed)[0])
        del obs["authoritative_readback"]
        self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "UNKNOWN")

    def test_unavailable_never_absent(self):
        case = next(c for c in self.schedule if c["test_id"] == "T10")
        state, _, _ = expected(self.fixture, case)
        obs = synthetic_observation(self.fixture, case, state[0], "NOT_APPLIED")
        obs["readback_provenance"]["authoritative"] = False
        self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "UNKNOWN")

    def test_t10_fault_or_unhealthy_is_unknown(self):
        case = next(c for c in self.schedule if c["test_id"] == "T10")
        state, _, _ = expected(self.fixture, case)
        obs = synthetic_observation(self.fixture, case, state[0], "NOT_APPLIED")
        obs["readback_provenance"]["fault_injected"] = True
        self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "UNKNOWN")

    def test_race_without_overlap_is_unknown(self):
        case = next(c for c in self.schedule if c["test_id"] == "T02")
        state, allowed, _ = expected(self.fixture, case)
        obs = synthetic_observation(self.fixture, case, state[0], sorted(allowed)[0])
        obs["overlap_proof"] = None
        self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "UNKNOWN")

    def test_t04_wrong_stale_order_is_unknown(self):
        case = next(c for c in self.schedule if c["test_id"] == "T04")
        state, allowed, _ = expected(self.fixture, case)
        obs = synthetic_observation(self.fixture, case, state[0], sorted(allowed)[0])
        obs["barrier_events"] = [x for x in obs["barrier_events"] if x["kind"] != "AUTHORITATIVE_F2"]
        self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "UNKNOWN")

    def test_wrong_projection_is_fail(self):
        case = self.schedule[1]; state, allowed, _ = expected(self.fixture, case)
        obs = synthetic_observation(self.fixture, case, state[0], sorted(allowed)[0])
        obs["authoritative_readback"] = self.fixture["states"]["S0"]
        obs["readback_provenance"]["readback_identity"] = identity("STPC-STATE-R01", obs["authoritative_readback"])
        obs["transition_history"] = obs["authoritative_readback"]["transition_history"]
        self.assertEqual(evaluate(self.fixture, case, obs)["classification"], "FAIL")

    def test_unknown_projection_field_rejected(self):
        s = copy.deepcopy(self.fixture["states"]["S1"]); s["extra"] = True
        with self.assertRaisesRegex(ValueError, "CLOSED_SCHEMA"):
            validate_projection(s)

    def test_noncanonical_and_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.json"
            p.write_bytes(b'{"a":1,"a":2}\n')
            with self.assertRaisesRegex(ValueError, "DUPLICATE_KEY"):
                strict_load(p)
            p.write_bytes(b'{ "a":1}\n')
            with self.assertRaisesRegex(ValueError, "NON_CANONICAL_BYTES"):
                strict_load(p)


if __name__ == "__main__":
    unittest.main()
