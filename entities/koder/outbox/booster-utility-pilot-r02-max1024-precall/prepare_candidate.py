"""Non-live deterministic preparation; never calls execute/resolver/transport."""
from pathlib import Path
import copy
import json
import bridge as b

ROOT=Path(__file__).resolve().parent
def read(name):return json.loads((ROOT/name).read_bytes())
def build():
    old=read('basis/request-r01.json');prior=read('basis/admission-r01.json')
    r=copy.deepcopy(old);r['max_output_tokens']=1024
    a=copy.deepcopy(prior);a['authority_id']=b.AUTHORITY;a['max_output_tokens']=1024
    a['request_sha256']=b.request_hash(r)
    # Logical verification ticks only, no installed LIVE_GATE/admission.
    p=b.prepare(r,a,now_tick=1,trusted_authority_sha256=b.sha(a),
                verify_ref=lambda ref:ref in (old['task'],old['writer']))
    body=p['native']['body']
    changes=[k for k in old if old[k]!=r[k]]
    assert changes==['max_output_tokens']
    assert r['payload']==read('basis/task.json')['specification']
    ids=dict(p['identity'],native_body_sha256=b.sha(b.canon(body)),
             named_authority_reservation=b.sha({'domain':b.DOMAIN+'/use-once','authority_id':b.AUTHORITY}))
    return {'request.json':r,'admission.candidate.json':a,'native-body.json':body,
            'identities.json':ids,'comparison.json':dict(request_changed_keys=changes,
             authority_changed_keys=sorted(k for k in prior if prior[k]!=a[k]),
             baseline_elapsed_seconds=read('basis/baseline-measurements.json')['baseline_elapsed_seconds'],
             baseline_sha256=r['baseline_sha256'],reasoning_effort_added='reasoning' in body,
             verification_now_tick=1,valid_until_tick=a['valid_until_tick'],provider_calls=0,
             host_installed=False,live_admission=False)}

if __name__=='__main__':
    for name,obj in build().items():(ROOT/name).write_bytes(b.canon(obj)+b'\n')
