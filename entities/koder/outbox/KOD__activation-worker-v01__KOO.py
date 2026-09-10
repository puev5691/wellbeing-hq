#!/usr/bin/env python3
import argparse, hashlib, json, os, subprocess, sys, uuid
from pathlib import Path

TERMINAL = {"result_dispatched", "processing_failed", "activation_failed"}

def jdump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def fail(code, reason, evidence_path=None, extra=None):
    ev = {"state": "activation_failed", "reason": reason}
    if extra: ev.update(extra)
    if evidence_path: Path(evidence_path).write_text(jdump(ev) + "\n", encoding="utf-8")
    print(jdump(ev)); raise SystemExit(code)

def validate_locator(locator):
    required=["artifact_path","artifact_commit","artifact_blob","artifact_sha256","recipient","exchange_gate","dispatch_path","inbox_path"]
    missing=[k for k in required if not locator.get(k)]
    if missing: return False,"locator_missing_fields:"+",".join(sorted(missing))
    if locator["exchange_gate"]!="v1": return False,"unsupported_exchange_gate"
    if not locator["inbox_path"].startswith("entities/") or "/inbox/" not in locator["inbox_path"]: return False,"invalid_inbox_path"
    if not locator["dispatch_path"].startswith("routes/dispatch/"): return False,"invalid_dispatch_path"
    return True,None

def validate_recovery(recovery, recipient):
    required=["entity","state","current_writer_state","recovery_identity"]
    missing=[k for k in required if not recovery.get(k)]
    if missing: return False,"recovery_missing_fields:"+",".join(sorted(missing))
    if recovery["entity"]!=recipient: return False,"recovery_entity_mismatch"
    if recovery["state"]!="verified": return False,"recovery_not_verified"
    if recovery["current_writer_state"] not in ("known_nonwriter","known_writer_unchanged"): return False,"current_writer_state_unknown_or_conflicting"
    return True,None

def main():
    ap=argparse.ArgumentParser(description="Fail-closed activation-worker prototype")
    ap.add_argument("--locator",required=True); ap.add_argument("--artifact",required=True); ap.add_argument("--recovery",required=True)
    ap.add_argument("--state-dir",required=True); ap.add_argument("--evidence",required=True); ap.add_argument("--result",required=True)
    ap.add_argument("--handler",nargs=argparse.REMAINDER,required=True); ap.add_argument("--retry",action="store_true"); ns=ap.parse_args()
    locator=load_json(ns.locator); ok,reason=validate_locator(locator)
    if not ok: fail(20,reason,ns.evidence)
    actual_sha=sha256_bytes(Path(ns.artifact).read_bytes())
    if actual_sha!=locator["artifact_sha256"]: fail(21,"artifact_sha256_mismatch",ns.evidence,{"expected":locator["artifact_sha256"],"actual":actual_sha})
    recovery=load_json(ns.recovery); ok,reason=validate_recovery(recovery,locator["recipient"])
    if not ok: fail(22,reason,ns.evidence)
    material="|".join([locator["artifact_path"],locator["artifact_commit"],locator["artifact_blob"],locator["artifact_sha256"],locator["recipient"],recovery["recovery_identity"]])
    activation_id=hashlib.sha256(material.encode()).hexdigest(); state_dir=Path(ns.state_dir); state_dir.mkdir(parents=True,exist_ok=True); marker=state_dir/(activation_id+".json")
    if marker.exists() and not ns.retry:
        prior=load_json(marker)
        if prior.get("state") in TERMINAL or prior.get("state")=="processing_started": fail(23,"immutable_item_already_processed_explicit_retry_required",ns.evidence,{"activation_id":activation_id,"prior_state":prior.get("state")})
    instance_id="proc:"+str(uuid.uuid4())
    started={"state":"processing_started","activation_id":activation_id,"processing_instance_id":instance_id,"recipient":locator["recipient"],"current_writer_claimed":False,"authority_expanded":False,"writer_grant_expanded":False,"artifact_sha256":actual_sha,"recovery_identity":recovery["recovery_identity"]}
    marker.write_text(jdump(started)+"\n",encoding="utf-8"); Path(ns.evidence).write_text(jdump(started)+"\n",encoding="utf-8")
    if not ns.handler: fail(24,"handler_missing",ns.evidence,{"activation_id":activation_id})
    env=os.environ.copy(); env.update({"WB_ACTIVATION_ID":activation_id,"WB_PROCESSING_INSTANCE_ID":instance_id,"WB_RECIPIENT":locator["recipient"],"WB_ARTIFACT_PATH":str(Path(ns.artifact).resolve()),"WB_RESULT_PATH":str(Path(ns.result).resolve())})
    cp=subprocess.run(ns.handler,env=env,text=True,capture_output=True)
    if cp.returncode!=0:
        ev=dict(started); ev.update({"state":"processing_failed","handler_exit":cp.returncode}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); Path(ns.evidence).write_text(jdump(ev)+"\n",encoding="utf-8"); print(jdump(ev)); return 30
    if not Path(ns.result).is_file():
        ev=dict(started); ev.update({"state":"processing_failed","reason":"handler_no_result_artifact"}); marker.write_text(jdump(ev)+"\n",encoding="utf-8"); Path(ns.evidence).write_text(jdump(ev)+"\n",encoding="utf-8"); print(jdump(ev)); return 31
    ev=dict(started); ev.update({"state":"result_dispatched","result_path":str(Path(ns.result)),"result_sha256":sha256_bytes(Path(ns.result).read_bytes()),"dispatch_evidence":{"required":True,"status":"prototype_local_evidence_only"}})
    marker.write_text(jdump(ev)+"\n",encoding="utf-8"); Path(ns.evidence).write_text(jdump(ev)+"\n",encoding="utf-8"); print(jdump(ev)); return 0

if __name__=="__main__": main()
