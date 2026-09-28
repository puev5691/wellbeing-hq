"""STP-C first-tranche supervisor oracle. Pure stdlib; no backend/adapter access.

Self-tests of this module do not execute T01-T20 against a candidate.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

LABELS = frozenset({"STPC-REQUEST-R01", "STPC-FIXTURE-R01", "STPC-STATE-R01",
                    "STPC-TRANSITION-R01", "STPC-EVIDENCE-R01", "STPC-CORPUS-R01"})
TESTS = frozenset({"T01", "T02", "T03", "T04", "T10", "T12"})


def canonical(value):
    if type(value) not in (dict, list, str, int, bool, type(None)):
        raise ValueError("NON_CANONICAL_TYPE")
    def walk(x):
        if type(x) is dict:
            if any(type(k) is not str for k in x):
                raise ValueError("BAD_KEY")
            for v in x.values():
                walk(v)
        elif type(x) is list:
            for v in x:
                walk(v)
        elif type(x) not in (str, int, bool, type(None)):
            raise ValueError("NON_CANONICAL_TYPE")
    walk(value)
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def identity(label, value):
    if label not in LABELS:
        raise ValueError("UNKNOWN_DOMAIN")
    payload = value if type(value) is bytes else canonical(value)
    return hashlib.sha256(label.encode("ascii") + b"\x00" + payload).hexdigest()


def strict_load(path):
    raw = Path(path).read_bytes()
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise ValueError("DUPLICATE_KEY")
            out[k] = v
        return out
    obj = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                     parse_float=lambda _: (_ for _ in ()).throw(ValueError("FLOAT")))
    if canonical(obj) != raw:
        raise ValueError("NON_CANONICAL_BYTES")
    return obj


def closed(obj, keys):
    if type(obj) is not dict or set(obj) != set(keys):
        raise ValueError("CLOSED_SCHEMA_MISMATCH")


def validate_fixture(f):
    closed(f, ("schema", "namespace", "requests", "states", "transition_inputs", "absence"))
    if f["schema"] != "STPC_FIXTURE_R01" or type(f["namespace"]) is not str:
        raise ValueError("BAD_FIXTURE")
    if set(f["requests"]) != {"R1", "R2"} or set(f["states"]) != {"S0", "S1"}:
        raise ValueError("BAD_FIXTURE_SET")
    for name, req in f["requests"].items():
        closed(req, ("request_id", "request_digest", "operation_id", "nonce_identity",
                     "intended_effect_identity", "idempotency_key", "process_fence"))
        if name != req["request_id"] or any(type(v) is not str or not v for v in req.values()):
            raise ValueError("BAD_REQUEST")
        core = {k: v for k, v in req.items() if k != "request_digest"}
        if req["request_digest"] != identity("STPC-REQUEST-R01", core):
            raise ValueError("BAD_REQUEST_DIGEST")
    for state in f["states"].values():
        validate_projection(state)
    for state in f["transition_inputs"].values():
        validate_projection(state)
        if state["namespace"] != f["namespace"]:
            raise ValueError("CROSS_NAMESPACE_STATE")
    if f["states"]["S0"]["requests"] or len(f["states"]["S1"]["requests"]) != 1:
        raise ValueError("BAD_INITIAL_STATE")
    closed(f["absence"], ("namespace", "read_mode", "fault_injected", "initial_state_identity"))
    if f["absence"]["read_mode"] != "AUTHORITATIVE" or f["absence"]["fault_injected"] is not False:
        raise ValueError("ABSENCE_NOT_AUTHORITATIVE")
    return True


def validate_projection(p):
    closed(p, ("schema", "namespace", "requests", "operations", "nonces",
               "transition_history", "current_state", "state_revision", "process_fence",
               "transition_identity", "evidence_identity", "collision_classification",
               "authoritative_absence_classification"))
    if p["schema"] != "STPC_LEDGER_V1" or type(p["namespace"]) is not str or not p["namespace"]:
        raise ValueError("BAD_PROJECTION")
    for k in ("requests", "operations", "nonces", "transition_history"):
        if type(p[k]) is not list:
            raise ValueError("BAD_COLLECTION")
    if type(p["state_revision"]) is not int or p["state_revision"] < 0:
        raise ValueError("BAD_REVISION")
    if p["current_state"] not in {"NEW", "RESERVED", "ADMITTED", "SIGNED", "VERIFIED",
                                 "QUORUM_VALID", "QUORUM_BLOCKED", "PRE_EFFECT_VALID",
                                 "AUTHORIZED", "CLAIMED", "COMMITTED", "OUTCOME_UNKNOWN",
                                 "REJECTED", "CONFLICT", "STALE", "PENDING_RECONCILIATION"}:
        raise ValueError("BAD_STATE")
    if p["collision_classification"] not in {"NONE", "REQUEST_ID_COLLISION",
                                             "OPERATION_ID_COLLISION", "NONCE_REPLAY", "LEDGER_CONFLICT"}:
        raise ValueError("BAD_COLLISION")
    if p["authoritative_absence_classification"] not in {"NOT_APPLICABLE", "NOT_APPLIED",
                                                          "UNKNOWN", "LEDGER_UNAVAILABLE"}:
        raise ValueError("BAD_ABSENCE")
    for key in ("process_fence", "transition_identity", "evidence_identity"):
        if p[key] is not None and (type(p[key]) is not str or not p[key]):
            raise ValueError("BAD_IDENTITY")
    for req in p["requests"]:
        closed(req, ("request_id", "request_digest", "operation_id", "nonce_identity"))
    for op in p["operations"]:
        closed(op, ("operation_id", "request_id", "intended_effect_identity",
                    "idempotency_key", "current_state", "state_revision", "process_fence",
                    "transition_identity", "evidence_identity", "effect_claim",
                    "terminal_result", "outcome_unknown_evidence", "reconciliation_evidence"))
        if type(op["state_revision"]) is not int or type(op["effect_claim"]) is not bool:
            raise ValueError("BAD_OPERATION")
    for item in p["transition_history"]:
        closed(item, ("revision", "from_state", "to_state", "process_fence",
                      "transition_identity", "evidence_identity", "prior_transition_identity"))
    if p["current_state"] == "NEW" and (p["requests"] or p["operations"] or p["nonces"] or p["transition_history"]):
        raise ValueError("NEW_WITH_RECORDS")
    if p["current_state"] == "NEW" and (p["state_revision"] != 0 or
            any(p[k] is not None for k in ("process_fence", "transition_identity", "evidence_identity")) or
            p["authoritative_absence_classification"] != "NOT_APPLIED"):
        raise ValueError("BAD_EMPTY_PROJECTION")
    if p["current_state"] != "NEW":
        if (len(p["requests"]) != 1 or len(p["operations"]) != 1 or len(p["nonces"]) != 1 or
                len(p["transition_history"]) != p["state_revision"] or
                p["authoritative_absence_classification"] != "NOT_APPLICABLE"):
            raise ValueError("BROKEN_LEDGER_LINKAGE")
        req, op, hist = p["requests"][0], p["operations"][0], p["transition_history"]
        if (req["request_id"] != op["request_id"] or req["operation_id"] != op["operation_id"] or
                req["nonce_identity"] != p["nonces"][0] or
                any(x["revision"] != i + 1 or x["prior_transition_identity"] !=
                    (None if i == 0 else hist[i-1]["transition_identity"]) or
                    x["from_state"] != ("NEW" if i == 0 else hist[i-1]["to_state"])
                    for i, x in enumerate(hist)) or
                hist[-1]["to_state"] != p["current_state"] or
                any(op[k] != p[k] for k in ("current_state", "state_revision", "process_fence",
                                              "transition_identity", "evidence_identity")) or
                any(hist[-1][k] != p[k] for k in ("process_fence", "transition_identity", "evidence_identity"))):
            raise ValueError("BROKEN_LEDGER_LINKAGE")
    return True


def validate_schedule(case):
    closed(case, ("test_id", "case_id", "initial_state", "seed_ref", "actors", "actions",
                  "barriers", "release_order", "fault_point", "overlap_required",
                  "healthy_authoritative_read"))
    if case["test_id"] not in TESTS or type(case["actions"]) is not list:
        raise ValueError("BAD_SCHEDULE")
    if len(case["actors"]) != len(set(case["actors"])) or len(case["barriers"]) != len(set(case["barriers"])):
        raise ValueError("BAD_SCHEDULE_DUPLICATE")
    if set(case["release_order"]) != set(case["barriers"]):
        raise ValueError("BAD_RELEASE_ORDER")
    if case["test_id"] in {"T02", "T03", "T12"} and not case["overlap_required"]:
        raise ValueError("RACE_OVERLAP_REQUIRED")
    if case["test_id"] == "T10" and (not case["healthy_authoritative_read"] or case["fault_point"] != "NONE"):
        raise ValueError("T10_READ_PATH")
    return True


def expected(f, case):
    """Generate allowed projections from frozen inputs only, never candidate output."""
    validate_fixture(f)
    validate_schedule(case)
    tid, cid = case["test_id"], case["case_id"]
    s0, s1 = f["states"]["S0"], f["states"]["S1"]
    if tid == "T01":
        if cid == "abort_before_commit":
            return [s0], {"NOT_APPLIED"}, {"PARTIAL_RESERVATION", "APPLIED"}
        if cid == "complete_commit":
            return [s1], {"RESERVED"}, {"PARTIAL_RESERVATION", "NOT_APPLIED"}
    if tid == "T02":
        if cid == "request_collision":
            return [s1, f["transition_inputs"]["T02_request_R2_wins"]], {
                "RESERVED|REQUEST_ID_COLLISION"}, {"TWO_WINNERS", "OVERWRITE"}
        if cid == "operation_collision":
            return [s1, f["transition_inputs"]["T02_operation_R2_wins"]], {
                "RESERVED|OPERATION_ID_COLLISION"}, {"TWO_WINNERS", "OVERWRITE"}
    if tid == "T03":
        return [f["transition_inputs"]["T03_P1_wins"], f["transition_inputs"]["T03_P2_wins"]], {
            "ONE_APPLIED_ONE_LEDGER_CONFLICT"}, {"TWO_APPLIED", "REVISION_REGRESSION"}
    if tid == "T04":
        return [f["transition_inputs"]["F2_authoritative"]], {"F2_APPLIED_F1_STALE"}, {
            "F1_APPLIED", "FENCE_ROLLBACK"}
    if tid == "T10":
        return [s0], {"NOT_APPLIED"}, {"LEDGER_UNAVAILABLE_AS_ABSENT", "STALE_READ"}
    if tid == "T12":
        return [f["transition_inputs"]["T12_P1_wins"], f["transition_inputs"]["T12_P2_wins"]], {
            "ONE_APPLIED_ONE_LEDGER_CONFLICT"}, {"TWO_APPLIED", "FORKED_HISTORY"}
    raise ValueError("UNKNOWN_CASE")


EVIDENCE_KEYS = frozenset({"schema", "test_id", "case_id", "run_id", "initial_state_identity",
                           "schedule_identity", "actor_actions", "barrier_events", "fault_proof",
                           "observed_responses", "authoritative_readback", "readback_provenance",
                           "transition_history", "integrity_status", "overlap_proof"})


def evaluate(f, case, observed):
    """Return PASS/FAIL/UNKNOWN; observed data never defines expected state."""
    allowed_states, allowed_classifications, forbidden = expected(f, case)
    if type(observed) is not dict or not EVIDENCE_KEYS.issubset(observed):
        return {"classification": "UNKNOWN", "reason": "MISSING_EVIDENCE"}
    if set(observed) != EVIDENCE_KEYS:
        return {"classification": "FAIL", "reason": "UNKNOWN_EVIDENCE_FIELD"}
    if observed["schema"] != "STPC_OBSERVATION_V1" or observed["test_id"] != case["test_id"] or observed["case_id"] != case["case_id"]:
        return {"classification": "FAIL", "reason": "WRONG_TEST_IDENTITY"}
    if observed["initial_state_identity"] != identity("STPC-STATE-R01", f["states"][case["initial_state"]]) or observed["schedule_identity"] != identity("STPC-FIXTURE-R01", case):
        return {"classification": "FAIL", "reason": "WRONG_INPUT_IDENTITY"}
    fp = observed["fault_proof"]
    if (not observed["run_id"] or observed["actor_actions"] != case["actions"] or
            type(fp) is not dict or set(fp) != {"point", "supervisor_event_identity"} or
            fp["point"] != case["fault_point"] or
            type(fp["supervisor_event_identity"]) is not str or not fp["supervisor_event_identity"]):
        return {"classification": "UNKNOWN", "reason": "SCHEDULE_OR_FAULT_NOT_PROVEN"}
    if not valid_barriers(case, observed["barrier_events"]):
        return {"classification": "UNKNOWN", "reason": "BARRIER_ORDER_NOT_PROVEN"}
    if observed["integrity_status"] != "PASS":
        return {"classification": "UNKNOWN" if observed["integrity_status"] in ("UNAVAILABLE", "UNKNOWN") else "FAIL", "reason": "INTEGRITY_NOT_PASS"}
    p = observed["readback_provenance"]
    if (type(p) is not dict or set(p) != {"authoritative", "healthy", "fault_injected", "readback_identity"} or
            any(type(p[k]) is not bool for k in ("authoritative", "healthy", "fault_injected")) or
            type(p["readback_identity"]) is not str or not p["authoritative"]):
        return {"classification": "UNKNOWN", "reason": "READBACK_NOT_AUTHORITATIVE"}
    if case["test_id"] == "T10" and (not p["healthy"] or p["fault_injected"]):
        return {"classification": "UNKNOWN", "reason": "T10_PATH_NOT_HEALTHY"}
    if case["overlap_required"] and not valid_overlap(case, observed["barrier_events"], observed["overlap_proof"]):
        return {"classification": "UNKNOWN", "reason": "RACE_OVERLAP_NOT_PROVEN"}
    if case["test_id"] == "T04" and not valid_stale_barrier(observed["barrier_events"]):
        return {"classification": "UNKNOWN", "reason": "STALE_ORDER_NOT_PROVEN"}
    state = observed["authoritative_readback"]
    if state is None:
        return {"classification": "UNKNOWN", "reason": "READBACK_UNAVAILABLE"}
    try:
        validate_projection(state)
    except ValueError:
        return {"classification": "FAIL", "reason": "LEDGER_CORRUPT"}
    if p["readback_identity"] != identity("STPC-STATE-R01", state):
        return {"classification": "FAIL", "reason": "READBACK_IDENTITY_MISMATCH"}
    if observed["transition_history"] != state["transition_history"]:
        return {"classification": "FAIL", "reason": "HISTORY_MISMATCH"}
    responses = observed["observed_responses"]
    if type(responses) is not str:
        return {"classification": "UNKNOWN", "reason": "RESPONSE_MISSING"}
    if responses in forbidden:
        return {"classification": "FAIL", "reason": "FORBIDDEN_OUTCOME"}
    if state not in allowed_states or responses not in allowed_classifications:
        return {"classification": "FAIL", "reason": "ORACLE_MISMATCH"}
    return {"classification": "PASS", "reason": "EXACT_ORACLE_MATCH"}


def valid_overlap(case, events, proof):
    # Supervisor event sequence, not wall-clock timestamps. Both actors must
    # arrive before release; neither protected attempt may finish first.
    if type(events) is not list or type(proof) is not dict or set(proof) != {"barrier_id", "participants"}:
        return False
    try:
        barrier = next(b for b in case["barriers"] if b.endswith("-RACE"))
        if proof != {"barrier_id": barrier, "participants": ["P1", "P2"]}:
            return False
        seq = [(e["kind"], e["actor"], e["barrier"]) for e in events]
        a1 = seq.index(("ARRIVE", "P1", barrier))
        a2 = seq.index(("ARRIVE", "P2", barrier))
        rel = seq.index(("RELEASE", "SUPERVISOR", barrier))
        return a1 < rel and a2 < rel and not any(x[0] == "FINISH" for x in seq[:rel])
    except (StopIteration, ValueError, KeyError, TypeError):
        return False


def valid_barriers(case, events):
    if type(events) is not list:
        return False
    try:
        for i, event in enumerate(events):
            closed(event, ("kind", "actor", "barrier", "event_identity"))
            core = {k: event[k] for k in ("kind", "actor", "barrier")}
            if event["event_identity"] != identity("STPC-EVIDENCE-R01", {"ordinal": i, **core}):
                return False
        releases = [e["barrier"] for e in events if e["kind"] == "RELEASE"]
        if releases != case["release_order"]:
            return False
        if case["test_id"] == "T10" and not any(e["kind"] == "HEALTHY_AUTH_READ" and
                                                  e["actor"] == "SUPERVISOR" for e in events):
            return False
        return True
    except (KeyError, TypeError, ValueError):
        return False
def valid_stale_barrier(events):
    if type(events) is not list:
        return False
    try:
        seq = [(e["kind"], e["actor"], e["barrier"]) for e in events]
        return (seq.index(("PAUSE", "P1", "B-T04-OLD-PAUSED")) <
                seq.index(("AUTHORITATIVE_F2", "SUPERVISOR", "B-T04-F2-COMMIT")) <
                seq.index(("RELEASE", "SUPERVISOR", "B-T04-OLD-RELEASE")))
    except (ValueError, KeyError, TypeError):
        return False


def corpus_identity(root, names):
    # Identity of exact file bytes, including README/self-test files, excluding
    # only recursive MANIFEST and SHA256SUMS. Sorted paths are mandatory.
    entries = [{"path": n, "bytes": (Path(root) / n).stat().st_size,
                "sha256": hashlib.sha256((Path(root) / n).read_bytes()).hexdigest()}
               for n in sorted(names)]
    return identity("STPC-CORPUS-R01", entries)
