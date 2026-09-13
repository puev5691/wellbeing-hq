from __future__ import annotations
import hashlib, json
from pathlib import Path
from static_preview_core import *
import static_preview_core as _core

SCHEMA_VERSION="info-entry-static-preview-v0.2"

def render(fixtures):
    html_text,report=_core.render(fixtures)
    for item in report:
        item["readback_confirmed"]=False
        item["assertions"]=[]
        item["failures"]=[]
    return html_text,report

def build(base:Path,strict_identity=True):
    validate_config({"mode":"local-static-v01","include_internal_quarantine":True})
    fixtures=[parse_fixture(p,strict_identity) for p in sorted((base/"fixtures").glob("*.md"))]
    html_text,report=render(fixtures)
    data=html_text.encode("utf-8")
    state={"phase":"build","schema_version":SCHEMA_VERSION,"fixture_count":len(fixtures),"fixture_results":report,"preview_ready_count":sum(x["preview_ready"] for x in report),"release_authorized_count":sum(x["release_authorized"] for x in report),"readback_confirmed_count":0,"expected_preview_identity":{"git_blob":git_blob_sha(data),"sha256":hashlib.sha256(data).hexdigest(),"size":len(data)},"deployment":False,"publication":False,"network_dependency":False}
    state["deterministic_identity"]=digest(state)
    (base/"preview.html").write_bytes(data)
    (base/"build-state.json").write_text(json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    return state
