from __future__ import annotations
import hashlib,json
from pathlib import Path
import _representation_v01 as rep
from readback_assertions import evaluate
SCHEMA_VERSION=rep.SCHEMA_VERSION; REQ=rep.REQ; EXPECTED_BLOBS=rep.EXPECTED_BLOBS
ContractError=rep.ContractError; parse_fixture=rep.parse_fixture; validate_config=rep.validate_config
validate=rep.validate; classify=rep.classify; git_blob_sha=rep.git_blob_sha; digest=rep.digest
PHASE='post_build_readback'; LOCATOR='local-static://preview.html'
def sha256(b):return hashlib.sha256(b).hexdigest()
def render(fixtures):
    text,_ignored=rep.render(fixtures); out=[]
    for f in fixtures:
        m=f['metadata']; bucket,badge,mode=classify(m)
        out.append({'fixture':f['name'],'id':m['id'],'bucket':bucket,'badge':badge,
          'preview_ready':m['representation_state'] in {'preview_ready','preview_built','representation_ready'} and mode not in {'blocked','withdrawn','superseded'},
          'release_authorized':m['release_state']=='release_authorized','readback_confirmed':False,
          'readback_state':'unverified','expected_assertions':list(m['expected_readback_assertions']),
          'assertion_results':[],'failures':[],'phase':'build'})
    return text,out
def post_build_readback(path,fixtures,expected):
    raw=path.read_bytes(); observed={'git_blob_sha1':git_blob_sha(raw),'sha256':sha256(raw)}
    match=observed==expected; text=raw.decode(); rows=[]
    for f in fixtures:
        m=f['metadata']; bucket,badge,mode=classify(m); results=[]; failures=[]
        for name in m['expected_readback_assertions']:
            ok,detail=evaluate(name,f,text); results.append({'name':name,'result':'PASS' if ok else 'FAIL','failure_detail':None if ok else detail})
            if not ok:failures.append({'assertion':name,'detail':detail})
        if not match:failures.append({'assertion':'preview_identity','detail':'observed preview identity does not match build identity'})
        confirmed=match and not failures
        rows.append({'fixture':f['name'],'id':m['id'],'bucket':bucket,'badge':badge,
          'preview_ready':m['representation_state'] in {'preview_ready','preview_built','representation_ready'} and mode not in {'blocked','withdrawn','superseded'},
          'release_authorized':m['release_state']=='release_authorized','readback_confirmed':confirmed,
          'readback_state':'confirmed' if confirmed else 'failed','readback_locator':LOCATOR,'phase':PHASE,
          'assertion_results':results,'failures':failures})
    report={'schema_version':SCHEMA_VERSION,'phase':PHASE,'fixture_count':len(fixtures),
      'observed_preview':{'locator':LOCATOR,'expected_git_blob_sha1':expected['git_blob_sha1'],'observed_git_blob_sha1':observed['git_blob_sha1'],'expected_sha256':expected['sha256'],'observed_sha256':observed['sha256'],'identity_match':match},
      'fixture_results':rows,'preview_ready_count':sum(x['preview_ready'] for x in rows),'release_authorized_count':sum(x['release_authorized'] for x in rows),
      'readback_confirmed_count':sum(x['readback_confirmed'] for x in rows),'assertion_pass_count':sum(a['result']=='PASS' for x in rows for a in x['assertion_results']),
      'assertion_fail_count':sum(a['result']=='FAIL' for x in rows for a in x['assertion_results']),'readback_pass':match and all(x['readback_confirmed'] for x in rows),
      'deployment':False,'publication':False,'network_dependency':False}
    report['deterministic_identity']=digest(report);return report
def build(base:Path,strict_identity=True):
    validate_config({'mode':'local-static-v01','include_internal_quarantine':True})
    fx=[parse_fixture(p,strict_identity) for p in sorted((base/'fixtures').glob('*.md'))]
    text,pre=render(fx)
    if any(x['readback_confirmed'] for x in pre):raise ContractError('readback_must_be_unverified_before_write')
    raw=text.encode(); expected={'git_blob_sha1':git_blob_sha(raw),'sha256':sha256(raw)}; path=base/'preview.html'; path.write_bytes(raw)
    report=post_build_readback(path,fx,expected);(base/'readback-report.json').write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    return report
