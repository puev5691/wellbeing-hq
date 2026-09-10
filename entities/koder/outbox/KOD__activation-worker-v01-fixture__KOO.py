#!/usr/bin/env python3
import json, os
from pathlib import Path
artifact = Path(os.environ["WB_ARTIFACT_PATH"]).read_text(encoding="utf-8")
result = {
    "activation_id": os.environ["WB_ACTIVATION_ID"],
    "processing_instance_id": os.environ["WB_PROCESSING_INSTANCE_ID"],
    "recipient": os.environ["WB_RECIPIENT"],
    "artifact_seen": bool(artifact),
    "status": "fixture_processed"
}
Path(os.environ["WB_RESULT_PATH"]).write_text(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
