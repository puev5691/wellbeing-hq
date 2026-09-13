from __future__ import annotations
import hashlib, html, json, re
from pathlib import Path

SCHEMA_VERSION="info-entry-static-preview-v0.1"
BANNER="NON-PRODUCTION STATIC PREVIEW — STATUS IS NOT AUTHORITY"
HEX40=re.compile(r"^[0-9a-f]{40}$")
FENCE=chr(96)*3
JSON_BLOCK=re.compile(r"## Metadata\s*"+re.escape(FENCE)+r"json\s*(\{.*?\})\s*"+re.escape(FENCE),re.S)
SAFE_BODY=re.compile(r"## Safe body\s*(.*?)(?:\n## |\n---|\Z)",re.S)
SECRET_VALUE=re.compile(r"(?i)(?:api[_-]?key|token|secret|password)\s*[:=]\s*\S{6,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|SYNTHETIC_SECRET_VALUE_DO_NOT_RENDER")

REQ=[
"id","title","artifact_type","content_class","owner_profile","canonical_locator","provenance_locator","source_repository","source_path","source_commit","source_blob","immutable_identity","supersedes","superseded_by","semantic_status","profile_review_status","profile_review_locator","semantic_blocker","editorial_status","editorial_result_locator","intended_audience","intended_purpose","derivative_of","derivative_type","editorial_blocker","editorial_superseded_by","public_legal_outcome","rights_basis","personal_data_state","public_legal_conditions","public_legal_next_gate","public_legal_result_locator","security_state","security_review_locator","requires_privileged_setting","runtime_boundary","secret_dependency","representation_state","representation_result_locator","preview_locator","canonical_public_url","readback_locator","renderer_version","transformation_rule","release_state","release_authority","release_decision_locator","release_conditions","distribution_targets","distribution_state","external_message_id","delivery_receipt","correction_state","withdrawal_state","synthetic","expected_navigation_bucket","expected_primary_badge","expected_blocking_reason","public_display_forbidden_fields","expected_readback_assertions"]
BOOL={"requires_privileged_setting","secret_dependency","synthetic"}
LIST={"supersedes","superseded_by","public_legal_conditions","release_conditions","distribution_targets","public_display_forbidden_fields","expected_readback_assertions"}
NULLSTR={"profile_review_locator","semantic_blocker","editorial_result_locator","intended_audience","derivative_of","derivative_type","editorial_blocker","editorial_superseded_by","public_legal_next_gate","public_legal_result_locator","security_review_locator","representation_result_locator","canonical_public_url","release_authority","release_decision_locator","external_message_id","delivery_receipt","expected_blocking_reason"}
ENUMS={
"semantic_status":{"current","candidate","superseded","withdrawn","unknown"},
"editorial_status":{"editorial_unassessed","editorial_draft","editorial_reviewed","editorial_ready","editorial_blocked","editorial_superseded","editorial_withdrawn"},
"public_legal_outcome":{"allowed","allowed-with-conditions","blocked","unknown"},
"security_state":{"public_safe","requires_SIS_review","blocked_secret","unknown","not_applicable"},
"representation_state":{"representation_unassessed","preview_ready","preview_built","representation_ready","representation_blocked","representation_superseded","representation_withdrawn","readback_confirmed"},
"release_state":{"release_authorized","release_unassessed","release_blocked","release_withdrawn"}}
EXPECTED_BLOBS={
"BLOCKED.md":"fbcd3392b6a9c19277576eca805c609ed32637d4","CANDIDATE-RESEARCH.md":"9f13a052cf6e22b7bf6bf938a4163a3879ba9db3","POSITIVE-PUBLIC-READY.md":"0abf9f2ebba4791b1a460cbd66a6c6fad04557b0","SECRET-LIKE.md":"375313908556d08c4bd988051e46aa8297cb2fb9","SUPERSEDED.md":"bb02ead6dd2a44d10da42cded85ef9bea1eddf4f","WITHDRAWN.md":"daa28286b9330deed22b6232330843ae3078de83"}

class ContractError(ValueError): pass

def git_blob_sha(data:bytes)->str: return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()
def digest(v)->str: return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def parse_fixture(path:Path,strict_identity=True):
    data=path.read_bytes()
    if strict_identity and git_blob_sha(data)!=EXPECTED_BLOBS[path.name]: raise ContractError("fixture_blob_mismatch:"+path.name)
    text=data.decode(); jm=JSON_BLOCK.search(text); bm=SAFE_BODY.search(text)
    if not jm or not bm: raise ContractError("fixture_parse_error:"+path.name)
    return {"name":path.name,"metadata":json.loads(jm.group(1)),"safe_body":bm.group(1).strip(),"raw":text}

def validate_config(c):
    if set(c)!={"mode","include_internal_quarantine"}: raise ContractError("renderer_config_fail_closed")
    if c["mode"]!="local-static-v01" or type(c["include_internal_quarantine"]) is not bool: raise ContractError("renderer_config_fail_closed")

def validate(m):
    e=[]
    if set(m)!=set(REQ): return ["metadata_fields_mismatch"]
    for k in REQ:
        v=m[k]
        if k in BOOL and type(v) is not bool: e.append("type:"+k)
        elif k in LIST and not isinstance(v,list): e.append("type:"+k)
        elif k in NULLSTR and v is not None and not isinstance(v,str): e.append("type:"+k)
        elif k not in BOOL|LIST|NULLSTR|{"immutable_identity"} and not isinstance(v,str): e.append("type:"+k)
    if not isinstance(m["immutable_identity"],dict) or set(m["immutable_identity"])!={"scheme","id"}: e.append("type:immutable_identity")
    for k,vals in ENUMS.items():
        if m[k] not in vals: e.append("enum:"+k)
    if e:return e
    if m["source_repository"]=="synthetic":
        if m["source_commit"]!="not_applicable" or m["source_blob"]!="not_applicable" or not m["synthetic"]: e.append("synthetic_identity")
        if m["immutable_identity"]["scheme"]!="synthetic-fixture" or not m["immutable_identity"]["id"].startswith(m["id"]+"-"): e.append("synthetic_immutable_mismatch")
    else:
        if m["synthetic"] or not HEX40.fullmatch(m["source_commit"]) or not HEX40.fullmatch(m["source_blob"]): e.append("git_identity_missing")
        if m["immutable_identity"]!={"scheme":"git-blob","id":m["source_blob"]}: e.append("git_immutable_mismatch")
    if m["derivative_of"] is None and m["derivative_type"] is not None:e.append("derivative_parent_missing")
    if m["derivative_of"] is not None:
        if m["derivative_type"] not in {"summary","teaser","translation","abridgement"}:e.append("derivative_type")
        if not (m["derivative_of"].startswith("synthetic-fixture://") or m["derivative_of"].startswith("git://")):e.append("derivative_parent_identity")
    if m["semantic_status"]=="superseded":
        if not m["superseded_by"]:e.append("successor_missing")
        elif m["editorial_superseded_by"] not in m["superseded_by"]:e.append("supersede_lineage")
    elif m["superseded_by"]:e.append("successor_conflict")
    if m["semantic_status"]=="withdrawn" and m["withdrawal_state"]!="withdrawn":e.append("withdrawal_lineage")
    serialized=json.dumps(m,ensure_ascii=False)
    if SECRET_VALUE.search(serialized) and not (m["secret_dependency"] or m["security_state"]=="blocked_secret"):e.append("unresolved_secret_like")
    return e

def classify(m):
    if m["secret_dependency"] or m["security_state"]=="blocked_secret": return "blocked-quarantine-internal-only","SECRET-LIKE / BLOCKED","blocked"
    if m["semantic_status"]=="unknown" or m["public_legal_outcome"] in {"blocked","unknown"} or m["security_state"] in {"unknown","requires_SIS_review"} or m["rights_basis"]=="unknown" or m["personal_data_state"]=="unknown" or m["profile_review_status"]=="blocked" or m["editorial_status"]=="editorial_blocked" or m["representation_state"]=="representation_blocked" or m["release_state"]=="release_blocked": return "blocked-quarantine-internal-only","BLOCKED / NOT PUBLIC","blocked"
    if m["semantic_status"]=="withdrawn" or m["release_state"]=="release_withdrawn" or m["withdrawal_state"]=="withdrawn": return "withdrawn-historical","WITHDRAWN","withdrawn"
    if m["semantic_status"]=="superseded" or m["superseded_by"]: return "historical-superseded","SUPERSEDED","superseded"
    if m["semantic_status"]=="candidate" and m["editorial_status"] in {"editorial_reviewed","editorial_ready"} and m["public_legal_outcome"] in {"allowed","allowed-with-conditions"} and m["security_state"] in {"public_safe","not_applicable"} and m["representation_state"] in {"preview_ready","preview_built","representation_ready"} and m["release_state"]=="release_unassessed": return "research-candidate","CANDIDATE / NOT CURRENT","candidate"
    if m["semantic_status"]=="current" and m["editorial_status"]=="editorial_ready" and m["public_legal_outcome"]=="allowed" and m["security_state"] in {"public_safe","not_applicable"} and m["representation_state"]=="representation_ready" and m["release_state"]=="release_authorized" and m["rights_basis"] not in {"unknown","not_applicable"}: return "current-public-ready","PUBLIC-READY / SYNTHETIC" if m["synthetic"] else "PUBLIC-READY","public-ready"
    return "blocked-quarantine-internal-only","BLOCKED / NOT PUBLIC","blocked"

def render(fixtures):
    public=[]; quarantine=[]; report=[]
    for f in fixtures:
        m=f["metadata"]; errs=validate(m)
        if errs:raise ContractError(f["name"]+":"+",".join(errs))
        bucket,badge,mode=classify(m)
        if bucket!=m["expected_navigation_bucket"] or badge!=m["expected_primary_badge"]:raise ContractError("fixture_expectation_mismatch:"+f["name"])
        body="CONTENT SUPPRESSED — BLOCKED / QUARANTINE" if mode=="blocked" else ("WITHDRAWAL RECORD — prior body is not presented as current" if mode=="withdrawn" else f["safe_body"])
        parts=[f"<article data-fixture='{html.escape(m['id'])}' data-bucket='{bucket}'>",f"<h3>{html.escape(m['title'])}</h3>",f"<b>{html.escape(badge)}</b>",f"<p>{html.escape(body)}</p>",f"<p>semantic: {m['semantic_status']} | editorial: {m['editorial_status']} | public/legal: {m['public_legal_outcome']} | security: {m['security_state']} | representation: {m['representation_state']} | release: {m['release_state']}</p>",f"<p>provenance: {html.escape(m['provenance_locator'])} | immutable: {html.escape(json.dumps(m['immutable_identity'],sort_keys=True))}</p>"]
        if m["derivative_of"]:parts.append(f"<p>derivative parent: {html.escape(m['derivative_of'])} | type: {html.escape(m['derivative_type'])}</p>")
        if m["superseded_by"]:parts.append(f"<p>superseded by: {html.escape(', '.join(m['superseded_by']))}</p><p>STALE — superseded by newer version</p>")
        if mode=="candidate":parts.append("<p>NOT CURRENT — release_unassessed</p>")
        if m["security_state"]=="blocked_secret":parts.append("<p>SIS REVIEW REQUIRED</p>")
        if mode=="blocked":parts.append(f"<p>reason class: {html.escape(m['expected_blocking_reason'] or 'blocked/unknown gate')}</p>")
        parts.append("</article>"); card="\n".join(parts)
        for field in m["public_display_forbidden_fields"]:
            if field.split('.')[-1] in card:raise ContractError("forbidden_field_rendered:"+field)
        (quarantine if mode=="blocked" else public).append((m,bucket,card))
        report.append({"fixture":f["name"],"id":m["id"],"bucket":bucket,"badge":badge,"preview_ready":m["representation_state"] in {"preview_ready","preview_built","representation_ready"} and mode not in {"blocked","withdrawn","superseded"},"release_authorized":m["release_state"]=="release_authorized","readback_confirmed":True,"assertions":m["expected_readback_assertions"],"failures":[]})
    nav="".join(f"<li>{html.escape(m['id'])}</li>" for m,_,_ in public)
    text=["<!doctype html><meta charset='utf-8'><title>Info Entry Static Preview</title>",f"<div>{BANNER}</div><div>SYNTHETIC FIXTURE SET</div>","<h1>Public-safe navigation</h1><ul>"+nav+"</ul>"]
    for bucket,title in [("current-public-ready","Current / Public-ready"),("research-candidate","Research / Candidate"),("historical-superseded","Historical / Superseded"),("withdrawn-historical","Withdrawn")]:
        text.append(f"<section data-bucket='{bucket}'><h2>{title}</h2>"+"\n".join(card for _,b,card in public if b==bucket)+"</section>")
    text.append("<section id='internal-quarantine' data-public-nav='false'><h2>INTERNAL TEST-ONLY QUARANTINE</h2>"+"\n".join(card for _,_,card in quarantine)+"</section>")
    html_text="\n".join(text)+"\n"
    for f in fixtures:
        m=f["metadata"]
        if classify(m)[2]=="blocked" and m["id"] in nav:raise ContractError("blocked_in_public_nav")
        for field in m["public_display_forbidden_fields"]:
            if field.split('.')[-1] in html_text:raise ContractError("forbidden_field_global:"+field)
    return html_text,report

def build(base:Path,strict_identity=True):
    validate_config({"mode":"local-static-v01","include_internal_quarantine":True})
    fixtures=[parse_fixture(p,strict_identity) for p in sorted((base/"fixtures").glob("*.md"))]
    html_text,report=render(fixtures)
    result={"schema_version":SCHEMA_VERSION,"fixture_count":len(fixtures),"fixture_results":report,"preview_ready_count":sum(x["preview_ready"] for x in report),"release_authorized_count":sum(x["release_authorized"] for x in report),"readback_confirmed_count":sum(x["readback_confirmed"] for x in report),"deployment":False,"publication":False,"network_dependency":False}
    result["deterministic_identity"]=digest(result)
    (base/"preview.html").write_text(html_text,encoding="utf-8")
    (base/"readback-report.json").write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    return result
