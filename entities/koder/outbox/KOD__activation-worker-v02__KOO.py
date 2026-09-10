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
        self._run("cat-file", "-e", f"{commit}^{{commit}}")
        return True

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

def main():
    ap = argparse.ArgumentParser(description="Fail-closed activation-worker prototype v0.2")
    ap.add_argument("--locator", required=True)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--recovery", required=True)
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
    identity_material = "|".join([locator["artifact_path"], locator["artifact_commit"], locator["artifact_blob"], locator["artifact_sha256"], locator["dispatch_path"], locator["dispatch_commit"], locator["recipient"], recovery["recovery_identity"]])
    activation_id = hashlib.sha256(identity_material.encode()).hexdigest()
    state_dir = Path(ns.state_dir); state_dir.mkdir(parents=True, exist_ok=True)
    marker = state_dir / (activation_id + ".json")
    if marker.exists() and not ns.retry:
        prior = load_json(marker)
        if prior.get("state") in TERMINAL or prior.get("state") == "processing_started":
            fail(23, "immutable_item_already_processed_explicit_retry_required", ns.evidence, {"activation_id": activation_id, "prior_state": prior.get("state")})
    instance_id = "proc:" + str(uuid.uuid4())
    started = {"state":"processing_started","activation_id":activation_id,"processing_instance_id":instance_id,"recipient":locator["recipient"],"current_writer_claimed":False,"authority_expanded":False,"writer_grant_expanded":False,"artifact_sha256":locator["artifact_sha256"],"artifact_commit":locator["artifact_commit"],"artifact_blob":locator["artifact_blob"],"dispatch_commit":locator["dispatch_commit"],"recovery_identity":recovery["recovery_identity"]}
    marker.write_text(jdump(started)+"\n",encoding="utf-8"); write_evidence(ns.evidence,started)
    env=os.environ.copy(); env["WB_ACTIVATION_ID"]=activation_id; env["WB_PROCESSING_INSTANCE_ID"]=instance_id; env["WB_RECIPIENT"]=locator["recipient"]; env["WB_ARTIFACT_PATH"]=str(Path(ns.artifact).resolve()); env["WB_RESULT_PATH"]=str(Path(ns.result).resolve())
    cp=subprocess.run(ns.handler,env=env,text=True,capture_output=True)
    if cp.returncode != 0:
        ev=dict(started); ev.update({"state":"processing_failed","handler_exit":cp.returncode}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); write_evidence(ns.evidence,ev); print(jdump(ev)); return 30
    if not Path(ns.result).is_file():
        ev=dict(started); ev.update({"state":"processing_failed","reason":"handler_no_result_artifact"}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); write_evidence(ns.evidence,ev); print(jdump(ev)); return 31
    ev=dict(started); ev.update({"state":"result_dispatched","result_path":str(Path(ns.result)),"result_sha256":sha256_bytes(Path(ns.result).read_bytes()),"dispatch_evidence":{"required":True,"status":"prototype_local_evidence_only"}}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); write_evidence(ns.evidence,ev); print(jdump(ev)); return 0

if __name__ == "__main__":
    main()
