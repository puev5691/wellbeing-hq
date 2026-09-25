#!/usr/bin/env python3
import argparse, hashlib, json, os, re, subprocess, sys, uuid
from pathlib import Path

TERMINAL = {"result_dispatched", "processing_failed", "activation_failed"}

def jdump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def write_evidence(path, obj):
    Path(path).write_text(jdump(obj) + "\n", encoding="utf-8")

def fail(code, reason, evidence_path=None, extra=None):
    ev = {"state": "activation_failed", "reason": reason}
    if extra:
        ev.update(extra)
    if evidence_path:
        write_evidence(evidence_path, ev)
    print(jdump(ev))
    raise SystemExit(code)

class ProviderError(RuntimeError):
    pass

class GitProvider:
    """Read-only immutable identity provider over a local git repository."""
    def __init__(self, repo):
        self.repo = Path(repo)

    def _run(self, *args, text=False):
        try:
            cp = subprocess.run(["git", "-C", str(self.repo), *args], capture_output=True, text=text, check=False)
        except Exception as e:
            raise ProviderError("provider_unavailable") from e
        if cp.returncode != 0:
            raise ProviderError("provider_query_failed")
        return cp.stdout

    def commit_exists(self, commit):
        try:
            cp = subprocess.run(["git", "-C", str(self.repo), "cat-file", "-e", f"{commit}^{{commit}}"], capture_output=True, text=True, check=False)
        except Exception as e:
            raise ProviderError("provider_unavailable") from e
        if cp.returncode == 0:
            return True
        err = (cp.stderr or "").lower()
        missing_markers = ("not a valid object name", "not a valid object", "bad object", "invalid object name")
        if any(m in err for m in missing_markers):
            return False
        raise ProviderError("provider_query_failed")

    def blob_for_path(self, commit, path):
        out = self._run("ls-tree", commit, "--", path, text=True).strip()
        if not out:
            raise ProviderError("path_not_found_at_commit")
        left = out.split("\t", 1)[0].split()
        if len(left) < 3 or left[1] != "blob":
            raise ProviderError("path_not_blob")
        return left[2]

    def bytes_for_path(self, commit, path):
        return self._run("show", f"{commit}:{path}", text=False)

def parse_scalar_fields(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"^\s*([A-Za-z0-9_.-]+)\s*:\s*(.*?)\s*$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2)
        v = v.strip()
        if len(v) >= 2 and v[0] == "`" and v[-1] == "`":
            v = v[1:-1]
        out[k] = v
    return out

def dispatch_mentions_artifact(text, artifact_path):
    if f"`{artifact_path}`" in text:
        return True
    fields = parse_scalar_fields(text)
    return artifact_path in fields.values()

def validate_locator_shape(locator):
    required = ["artifact_path", "artifact_commit", "artifact_blob", "artifact_sha256", "recipient", "sender", "exchange_gate", "dispatch_path", "dispatch_commit", "inbox_path"]
    missing = [k for k in required if not locator.get(k)]
    if missing:
        return False, "locator_missing_fields:" + ",".join(sorted(missing))
    if locator["exchange_gate"] != "v1":
        return False, "unsupported_exchange_gate"
    if not re.fullmatch(r"[0-9a-fA-F]{40}", locator["artifact_commit"]):
        return False, "artifact_commit_format_invalid"
    if not re.fullmatch(r"[0-9a-fA-F]{40}", locator["artifact_blob"]):
        return False, "artifact_blob_format_invalid"
    if not re.fullmatch(r"[0-9a-fA-F]{40}", locator["dispatch_commit"]):
        return False, "dispatch_commit_format_invalid"
    if not re.fullmatch(r"[0-9a-fA-F]{64}", locator["artifact_sha256"]):
        return False, "artifact_sha256_format_invalid"
    if not locator["inbox_path"].startswith("entities/") or "/inbox/" not in locator["inbox_path"]:
        return False, "invalid_inbox_path"
    if not locator["dispatch_path"].startswith("routes/dispatch/"):
        return False, "invalid_dispatch_path"
    return True, None

def verify_immutable_chain(provider, locator, artifact_bytes):
    try:
        if not provider.commit_exists(locator["artifact_commit"]):
            return False, "artifact_commit_not_found"
        actual_blob = provider.blob_for_path(locator["artifact_commit"], locator["artifact_path"])
        if actual_blob != locator["artifact_blob"]:
            return False, "artifact_blob_mismatch"
        provider_artifact = provider.bytes_for_path(locator["artifact_commit"], locator["artifact_path"])
        provider_sha = sha256_bytes(provider_artifact)
        local_sha = sha256_bytes(artifact_bytes)
        if provider_sha != locator["artifact_sha256"] or local_sha != locator["artifact_sha256"]:
            return False, "artifact_sha256_mismatch"
        if not provider.commit_exists(locator["dispatch_commit"]):
            return False, "dispatch_commit_not_found"
        dispatch_bytes = provider.bytes_for_path(locator["dispatch_commit"], locator["dispatch_path"])
        dispatch_text = dispatch_bytes.decode("utf-8")
        df = parse_scalar_fields(dispatch_text)
        if df.get("sender") != locator["sender"]:
            return False, "dispatch_sender_mismatch"
        if df.get("recipient") != locator["recipient"]:
            return False, "dispatch_recipient_mismatch"
        if df.get("exchange_gate") != locator["exchange_gate"]:
            return False, "dispatch_exchange_gate_mismatch"
        if not dispatch_mentions_artifact(dispatch_text, locator["artifact_path"]):
            return False, "dispatch_artifact_mismatch"
        if f"`{locator['inbox_path']}`" not in dispatch_text and df.get("inbox_path") != locator["inbox_path"]:
            return False, "dispatch_inbox_mismatch"
        return True, None
    except (ProviderError, UnicodeDecodeError):
        return False, "provider_unavailable_or_unreadable"

def validate_recovery(recovery, recipient):
    required = ["entity", "state", "current_writer_state", "recovery_identity"]
    missing = [k for k in required if not recovery.get(k)]
    if missing:
        return False, "recovery_missing_fields:" + ",".join(sorted(missing))
    if recovery["entity"] != recipient:
        return False, "recovery_entity_mismatch"
    if recovery["state"] != "verified":
        return False, "recovery_not_verified"
    if recovery["current_writer_state"] not in ("known_nonwriter", "known_writer_unchanged"):
        return False, "current_writer_state_unknown_or_conflicting"
    return True, None

# r0.3 is an isolated successor of the immutable v0.2 worker. The trust profile
# is supplied separately by the supervisor, not inferred from a Git filename.
def exact_ref(provider, supplied, trusted, label):
    if supplied != trusted or not isinstance(supplied, dict):
        return False, label + "_not_trusted"
    commit, path, blob = (supplied.get(k) for k in ("commit", "path", "blob"))
    if not all(isinstance(x, str) for x in (commit, path, blob)) or not re.fullmatch(r"[0-9a-f]{40}", commit) or not re.fullmatch(r"[0-9a-f]{40}", blob) or not path.startswith("fixtures/") or ":" in path:
        return False, label + "_invalid_ref"
    try:
        if not provider.commit_exists(commit) or provider.blob_for_path(commit, path) != blob:
            return False, label + "_identity_mismatch"
        return True, provider.bytes_for_path(commit, path)
    except ProviderError:
        return False, label + "_provider_unavailable"

def check_admission(provider, locator, envelope, admission, trust):
    required = ("event_id", "event_digest", "source_commit", "inbox_path", "inbox_blob", "recipient")
    if not all(isinstance(envelope.get(k), str) and envelope[k] for k in required):
        return False, "event_missing_fields", None
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,100}", envelope["event_id"]):
        return False, "event_id_invalid", None
    digest_payload = {k:envelope[k] for k in ("event_id", "source_commit", "inbox_path", "inbox_blob", "recipient")}
    digest_payload.update({k:locator[k] for k in ("artifact_path", "artifact_commit", "artifact_blob", "dispatch_path", "dispatch_commit")})
    digest = sha256_bytes(jdump(digest_payload).encode("utf-8"))
    if envelope["event_digest"] != digest:
        return False, "event_digest_mismatch", None
    if envelope["inbox_path"] != locator["inbox_path"] or envelope["recipient"] != locator["recipient"]:
        return False, "event_locator_mismatch", None
    try:
        if not provider.commit_exists(envelope["source_commit"]):
            return False, "event_commit_missing", None
        if provider.blob_for_path(envelope["source_commit"], envelope["inbox_path"]) != envelope["inbox_blob"]:
            return False, "event_inbox_blob_mismatch", None
        fields = parse_scalar_fields(provider.bytes_for_path(envelope["source_commit"], envelope["inbox_path"]).decode("utf-8"))
    except (ProviderError, UnicodeDecodeError):
        return False, "event_provider_unavailable_or_unreadable", None
    for name, value in (("recipient", locator["recipient"]), ("artifact_path", locator["artifact_path"]), ("artifact_commit", locator["artifact_commit"]), ("artifact_blob", locator["artifact_blob"]), ("dispatch_path", locator["dispatch_path"]), ("dispatch_commit", locator["dispatch_commit"])):
        if fields.get(name) != value:
            return False, "event_inbox_binding_mismatch:" + name, None
    if not isinstance(trust, dict) or trust.get("scope") != "ISOLATED_SYNTHETIC_R02" or trust.get("admission_version") != "r02":
        return False, "trusted_profile_missing_or_invalid", None
    if admission.get("task_id") != trust.get("task_id") or admission.get("source_set_id") != trust.get("source_set_id"):
        return False, "task_or_source_set_not_trusted", None
    for label in ("authority", "recovery", "writer"):
        ok, content = exact_ref(provider, admission.get(label), trust.get(label), label)
        if not ok:
            return False, content, None
        try:
            record = json.loads(content)
        except (UnicodeDecodeError, ValueError):
            return False, label + "_invalid_content", None
        if label == "authority":
            if record.get("status") != "AUTHORIZED" or record.get("task_id") != trust["task_id"] or record.get("recipient") != locator["recipient"] or record.get("source_set_id") != trust["source_set_id"] or record.get("superseded") is not False:
                return False, "authority_not_current_or_valid", None
        elif label == "recovery":
            if record.get("entity") != locator["recipient"] or record.get("state") != "verified" or record.get("recovery_identity") != admission.get("recovery_identity"):
                return False, "recovery_not_current_or_valid", None
        elif record.get("entity") != locator["recipient"] or record.get("status") != "CURRENT_WRITER_ESTABLISHED" or record.get("writer_id") != trust.get("writer_id") or record.get("superseded") is not False:
            return False, "writer_not_current_or_valid", None
    supplied = admission.get("sources")
    trusted = trust.get("sources")
    if not isinstance(supplied, list) or not supplied or supplied != trusted or len({x.get("path") for x in supplied if isinstance(x, dict)}) != len(supplied):
        return False, "approved_source_set_missing_or_untrusted", None
    for ref in supplied:
        ok, content = exact_ref(provider, ref, ref, "source")
        if not ok:
            return False, content, None
        # Approval comes from the supervisor trust profile, never from these bytes.
    return True, None, digest

def reserve_event(state_dir, scope, event_id, digest, evidence_path):
    key = sha256_bytes((scope + "|" + event_id).encode("utf-8"))
    state_dir.mkdir(parents=True, exist_ok=True)
    reservation = state_dir / ("event-" + key + ".json")
    try:
        with reservation.open("x", encoding="utf-8") as f:
            f.write(jdump({"event_id":event_id, "event_digest":digest, "state":"reserved_unknown_until_reconciled"}) + "\n")
            f.flush(); os.fsync(f.fileno())
    except FileExistsError:
        prior = load_json(reservation)
        if prior.get("event_digest") != digest:
            fail(24, "event_id_digest_conflict", evidence_path)
        if prior.get("state") == "reserved_unknown_until_reconciled":
            fail(27, "event_state_unknown_requires_reconcile", evidence_path)
        fail(23, "duplicate_event_same_digest", evidence_path)
    return reservation

def finish_event(reservation, event_id, digest, state):
    # Atomic replacement in the same isolated state directory; interruption
    # before this step remains UNKNOWN and never triggers automatic replay.
    next_path = reservation.with_suffix(".next")
    with next_path.open("x", encoding="utf-8") as f:
        f.write(jdump({"event_id":event_id,"event_digest":digest,"state":state})+"\n")
        f.flush(); os.fsync(f.fileno())
    os.replace(next_path, reservation)

def main():
    ap = argparse.ArgumentParser(description="Fail-closed activation-worker prototype v0.2")
    ap.add_argument("--locator", required=True)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--recovery", required=True)
    ap.add_argument("--event", required=True)
    ap.add_argument("--admission", required=True)
    ap.add_argument("--admission-trust", required=True)
    ap.add_argument("--git-repo", required=True)
    ap.add_argument("--state-dir", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--result", required=True)
    ap.add_argument("--retry", action="store_true")
    ap.add_argument("--handler", nargs=argparse.REMAINDER, required=True)
    ns = ap.parse_args()
    locator = load_json(ns.locator)
    ok, reason = validate_locator_shape(locator)
    if not ok:
        fail(20, reason, ns.evidence)
    artifact_bytes = Path(ns.artifact).read_bytes()
    provider = GitProvider(ns.git_repo)
    ok, reason = verify_immutable_chain(provider, locator, artifact_bytes)
    if not ok:
        fail(21, reason, ns.evidence)
    recovery = load_json(ns.recovery)
    ok, reason = validate_recovery(recovery, locator["recipient"])
    if not ok:
        fail(22, reason, ns.evidence)
    envelope, admission, trust = (load_json(p) for p in (ns.event, ns.admission, ns.admission_trust))
    ok, reason, event_digest = check_admission(provider, locator, envelope, admission, trust)
    if not ok:
        fail(25, reason, ns.evidence)
    state_dir = Path(ns.state_dir)
    if ns.retry:
        fail(26, "automatic_retry_not_allowed_in_isolated_successor", ns.evidence)
    reservation = reserve_event(state_dir, trust["task_id"], envelope["event_id"], event_digest, ns.evidence)
    identity_material = "|".join([locator["artifact_path"], locator["artifact_commit"], locator["artifact_blob"], locator["artifact_sha256"], locator["dispatch_path"], locator["dispatch_commit"], locator["recipient"], recovery["recovery_identity"]])
    activation_id = hashlib.sha256(identity_material.encode()).hexdigest()
    state_dir.mkdir(parents=True, exist_ok=True)
    marker = state_dir / (activation_id + ".json")
    if marker.exists() and not ns.retry:
        prior = load_json(marker)
        if prior.get("state") in TERMINAL or prior.get("state") == "processing_started":
            fail(23, "immutable_item_already_processed_explicit_retry_required", ns.evidence, {"activation_id": activation_id, "prior_state": prior.get("state")})
    instance_id = "proc:" + str(uuid.uuid4())
    started = {"state":"worker_handler_invoked_synthetic","activation_id":activation_id,"processing_instance_id":instance_id,"recipient":locator["recipient"],"current_writer_claimed":False,"authority_expanded":False,"writer_grant_expanded":False,"artifact_sha256":locator["artifact_sha256"],"artifact_commit":locator["artifact_commit"],"artifact_blob":locator["artifact_blob"],"dispatch_commit":locator["dispatch_commit"],"recovery_identity":recovery["recovery_identity"],"event_id":envelope["event_id"],"event_digest":event_digest,"real_entity_processing_started":False}
    marker.write_text(jdump(started)+"\n",encoding="utf-8"); write_evidence(ns.evidence,started)
    env=os.environ.copy(); env["WB_ACTIVATION_ID"]=activation_id; env["WB_PROCESSING_INSTANCE_ID"]=instance_id; env["WB_RECIPIENT"]=locator["recipient"]; env["WB_ARTIFACT_PATH"]=str(Path(ns.artifact).resolve()); env["WB_RESULT_PATH"]=str(Path(ns.result).resolve())
    cp=subprocess.run(ns.handler,env=env,text=True,capture_output=True)
    if cp.returncode != 0:
        ev=dict(started); ev.update({"state":"processing_failed","handler_exit":cp.returncode}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); write_evidence(ns.evidence,ev); finish_event(reservation,envelope["event_id"],event_digest,"processing_failed"); print(jdump(ev)); return 30
    if not Path(ns.result).is_file():
        ev=dict(started); ev.update({"state":"processing_failed","reason":"handler_no_result_artifact"}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); write_evidence(ns.evidence,ev); finish_event(reservation,envelope["event_id"],event_digest,"processing_failed"); print(jdump(ev)); return 31
    ev=dict(started); ev.update({"state":"result_dispatched","result_path":str(Path(ns.result)),"result_sha256":sha256_bytes(Path(ns.result).read_bytes()),"dispatch_evidence":{"required":True,"status":"prototype_local_evidence_only"}}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); write_evidence(ns.evidence,ev); finish_event(reservation,envelope["event_id"],event_digest,"result_dispatched"); print(jdump(ev)); return 0

if __name__ == "__main__":
    sys.exit(main())
