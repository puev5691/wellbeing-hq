from __future__ import annotations
import hashlib, html, json, re
from pathlib import Path
from static_preview import parse_fixture, git_blob_sha

PHASE="post_build_readback"
ARTICLE=re.compile(r"<article data-fixture='([^']+)' data-bucket='([^']+)'>(.*?)</article>",re.S)
def sha256(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def _observed(text):
    nav=text.split("</ul>",1)[0]
    cards={m.group(1):(m.group(2),m.group(3)) for m in ARTICLE.finditer(text)}
    return nav,cards
def _check(name,m,f,nav,cards,text):
    bucket,card=cards.get(m["id"],("","")); current=bucket=="current-public-ready"
    checks={
      "current_bucket_only":current and m["id"] in nav,
      "public_ready_badge_visible":m["expected_primary_badge"] in card,
      "provenance_visible":m["provenance_locator"] in card,
      "derivative_parent_visible":bool(m["derivative_of"]) and m["derivative_of"] in card,
      "safe_body_visible":html.escape(f["safe_body"]) in card,
      "internal_test_note_absent":"internal_test_note" not in text,
      "absent_from_public_navigation":m["id"] not in nav,
      "blocked_placeholder_only":"CONTENT SUPPRESSED — BLOCKED / QUARANTINE" in card and html.escape(f["safe_body"]) not in card,
      "blocking_reason_class_visible":bool(m["expected_blocking_reason"]) and html.escape(m["expected_blocking_reason"]) in card,
      "blocked_body_absent":"blocked_body" not in text,
      "no_canonical_public_url":m["canonical_public_url"] is None and "canonical_public_url" not in card,
      "absent_from_current_bucket":not current,
      "candidate_badge_persistent":"CANDIDATE / NOT CURRENT" in card,
      "no_public_ready_claim":"PUBLIC-READY" not in card,
      "release_unassessed_visible":"release_unassessed" in card,
      "reviewer_private_note_absent":"reviewer_private_note" not in text,
      "secret_block_badge_visible":"SECRET-LIKE / BLOCKED" in card,
      "secret_like_value_absent":"secret_like_value" not in text and "SYNTHETIC_SECRET_VALUE_DO_NOT_RENDER" not in text,
      "raw_detection_sample_absent":"raw_detection_sample" not in text,
      "SIS_review_required_visible":"SIS REVIEW REQUIRED" in card,
      "superseded_badge_visible":"SUPERSEDED" in card,
      "successor_locator_visible":bool(m["superseded_by"]) and all(x in card for x in m["superseded_by"]),
      "historical_bucket_only":bucket=="historical-superseded",
      "stale_warning_visible":"STALE — superseded by newer version" in card,
      "withdrawn_badge_visible":"WITHDRAWN" in card,
      "withdrawal_record_visible":"WITHDRAWAL RECORD" in card,
      "prior_body_not_presented_as_current":"prior body is not presented as current" in card and html.escape(f["safe_body"]) not in card,
      "release_withdrawn_visible":"release_withdrawn" in card}
    if name not in checks:return False,"unsupported assertion"
    return bool(checks[name]),None if checks[name] else "observed preview did not satisfy assertion"
def verify(base:Path,expected_preview_git_blob:str,expected_preview_sha256:str,strict_identity=True):
    p=base/"preview.html"; data=p.read_bytes(); observed_git=git_blob_sha(data); observed_sha=sha256(data)
    identity_ok=observed_git==expected_preview_git_blob and observed_sha==expected_preview_sha256
    text=data.decode("utf-8"); nav,cards=_observed(text)
    fixtures=[parse_fixture(x,strict_identity) for x in sorted((base/"fixtures").glob("*.md"))]
    results=[]; all_failures=[]
    for f in fixtures:
        m=f["metadata"]; evidence=[]; failures=[]
        for name in m["expected_readback_assertions"]:
            ok,detail=_check(name,m,f,nav,cards,text)
            evidence.append({"assertion_name":name,"assertion_result":"PASS" if ok else "FAIL","failure_detail":detail})
            if not ok:failures.append({"assertion_name":name,"failure_detail":detail})
        confirmed=identity_ok and not failures
        if not confirmed:all_failures.append({"fixture":f["name"],"failures":failures or [{"assertion_name":"preview_identity","failure_detail":"observed preview identity mismatch"}]})
        results.append({"fixture":f["name"],"id":m["id"],"readback_locator":"local-static://preview.html","readback_confirmed":confirmed,"assertion_evidence":evidence,"failures":failures})
    report={"phase":PHASE,"observed_preview_identity":{"git_blob":observed_git,"sha256":observed_sha,"size":len(data)},"expected_preview_identity":{"git_blob":expected_preview_git_blob,"sha256":expected_preview_sha256},"identity_match":identity_ok,"readback_locator":"local-static://preview.html","fixture_count":len(fixtures),"readback_confirmed_count":sum(x["readback_confirmed"] for x in results),"fixture_results":results,"failures":all_failures,"status":"PASS" if identity_ok and not all_failures else "FAIL","deployment":False,"publication":False,"network_dependency":False}
    (base/"readback-report.json").write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    return report
