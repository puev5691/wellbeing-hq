#!/usr/bin/env python3
"""Offline synthetic detector-event to pinned activation-worker v0.2 probe.

This is a fixture, not a deployment adapter. It deliberately does not invent
authority or source validation that the worker does not implement.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

WORKER = Path(__file__).with_name("KOD__activation-worker-v02__KOO.py")
ARTIFACT = "entities/synthetic/outbox/SYN__task__TEST.md"
INBOX = "entities/synthetic/inbox/SYN__task__TEST.md"
DISPATCH = "routes/dispatch/SYN__task__TEST.md"

def cmd(*args, cwd=None, env=None):
    return subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True, check=True).stdout.strip()

def put(repo, path, data):
    p = repo / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(data, encoding="utf-8")

def commit(repo, msg):
    cmd("git", "add", ".", cwd=repo)
    cmd("git", "commit", "-qm", msg, cwd=repo, env={**os.environ, "GIT_AUTHOR_DATE":"2000-01-01T00:00:00+0000", "GIT_COMMITTER_DATE":"2000-01-01T00:00:00+0000"})
    return cmd("git", "rev-parse", "HEAD", cwd=repo)

def setup(base):
    repo = base / "mirror"
    repo.mkdir()
    cmd("git", "init", "-q", str(repo))
    cmd("git", "config", "user.name", "Synthetic Fixture", cwd=repo)
    cmd("git", "config", "user.email", "synthetic@example.invalid", cwd=repo)
    put(repo, ARTIFACT, "synthetic task only\n")
    a = commit(repo, "synthetic artifact")
    put(repo, DISPATCH, f"sender: synthetic\nrecipient: synthetic\nexchange_gate: v1\nartifact_path: `{ARTIFACT}`\ninbox_path: `{INBOX}`\n")
    d = commit(repo, "synthetic dispatch")
    put(repo, INBOX, "synthetic addressed inbox\n")
    e = commit(repo, "synthetic event")
    changed = cmd("git", "diff", "--name-only", d, e, cwd=repo).splitlines()
    assert changed == [INBOX], changed
    blob = cmd("git", "rev-parse", f"{a}:{ARTIFACT}", cwd=repo)
    payload = (repo / ARTIFACT).read_bytes()
    loc = dict(artifact_path=ARTIFACT, artifact_commit=a, artifact_blob=blob,
               artifact_sha256=hashlib.sha256(payload).hexdigest(), recipient="synthetic",
               sender="synthetic", exchange_gate="v1", dispatch_path=DISPATCH,
               dispatch_commit=d, inbox_path=INBOX)
    return repo, e, loc, payload

def run_case(base, repo, locator, payload, name, handler="ok", recovery=None, state=None):
    case = base / name
    case.mkdir()
    (case / "locator.json").write_text(json.dumps(locator))
    (case / "artifact.md").write_bytes(payload)
    (case / "recovery.json").write_text(json.dumps(recovery if recovery is not None else dict(entity="synthetic", state="verified", current_writer_state="known_nonwriter", recovery_identity="synthetic-recovery-v1")))
    state = state or case / "state"
    # Handler is a synthetic process with a local result artifact, never an Entity.
    handler_code = 'import os, pathlib, sys; pathlib.Path(os.environ["WB_RESULT_PATH"]).write_text("synthetic only\\n") if sys.argv[1] == "ok" else None; sys.exit(0 if sys.argv[1] == "ok" else 9)'
    proc = subprocess.run([sys.executable, str(WORKER), "--locator", str(case / "locator.json"), "--artifact", str(case / "artifact.md"), "--recovery", str(case / "recovery.json"), "--git-repo", str(repo), "--state-dir", str(state), "--evidence", str(case / "evidence.json"), "--result", str(case / "result.txt"), "--handler", sys.executable, "-c", handler_code, handler], capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE":"1"})
    evidence = json.loads((case / "evidence.json").read_text())
    return {"exit": proc.returncode, "state": evidence["state"], "reason": evidence.get("reason"), "handler_exit":evidence.get("handler_exit"), "marker":bool(list(state.glob("*.json"))), "synthetic_result":(case / "result.txt").is_file()}

def main():
    with tempfile.TemporaryDirectory(prefix="kod-detector-worker-r01-") as temp:
        base = Path(temp)
        repo, event_commit, good, payload = setup(base)
        # The model consumes exactly the changed inbox path at an immutable commit.
        event = {"source_event":"synthetic_github_push", "commit":event_commit,
                 "inbox_path":INBOX, "recipient":"synthetic", "digest":hashlib.sha256((event_commit+"|"+INBOX).encode()).hexdigest()}
        results = {}
        results["01_valid"] = run_case(base, repo, good, payload, "01")
        results["02_commit_blob_mismatch"] = run_case(base, repo, {**good, "artifact_blob":"0"*40}, payload, "02")
        results["03_wrong_recipient"] = run_case(base, repo, {**good, "recipient":"wrong"}, payload, "03")
        shared = base / "dedupe_state"
        results["04_duplicate_same_digest_initial"] = run_case(base, repo, good, payload, "04_initial", state=shared)
        results["04_duplicate_same_digest_repeat"] = run_case(base, repo, good, payload, "04_repeat", state=shared)
        # Same external ID, altered event digest: worker has no event ID/digest
        # input and therefore sees only its own immutable-item dedupe key.
        altered_event = {**event, "digest":"f"*64}
        results["05_duplicate_id_changed_digest_observed"] = run_case(base, repo, good, payload, "05_changed_digest", state=shared)
        results["07_missing_recovery_ref"] = run_case(base, repo, good, payload, "07", recovery={"entity":"synthetic", "state":"verified", "current_writer_state":"known_nonwriter"})
        results["08_provider_unavailable"] = run_case(base, base / "no_git_provider", good, payload, "08")
        results["09_handler_failure"] = run_case(base, repo, good, payload, "09", handler="fail")
        results["10_marker_no_entity"] = run_case(base, repo, good, payload, "10")
        # Differential demonstrations of unsupported contract fields. These are
        # NOT positive safety tests: acceptance despite absence is the blocker.
        results["06_missing_task_authority_observed"] = run_case(base, repo, good, payload, "06_no_authority")
        results["07_missing_approved_source_observed"] = run_case(base, repo, good, payload, "07_no_source")
        print(json.dumps({"event":event, "changed_digest_event":altered_event, "worker_git_blob":"c680878806fd2fb6d20df8b6e8938d3f3ead5053", "results":results}, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
