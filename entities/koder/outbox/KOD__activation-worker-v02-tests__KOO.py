#!/usr/bin/env python3
import hashlib,json,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
WORKER=HERE/'KOD__activation-worker-v02__KOO.py'

def git(repo,*a):
 cp=subprocess.run(['git','-C',str(repo),*a],capture_output=True,text=True); assert cp.returncode==0,cp.stderr; return cp.stdout.strip()
def dump(p,o): p.write_text(json.dumps(o,sort_keys=True)+'\n',encoding='utf-8')
def fixture(td,recipient='koder',artifact_ref='entities/koordinator/outbox/FIX.md'):
 repo=td/'repo'; repo.mkdir(); git(repo,'init','-q'); git(repo,'config','user.email','fixture@example.invalid'); git(repo,'config','user.name','fixture')
 art='entities/koordinator/outbox/FIX.md'; inbox='entities/koder/inbox/FIX.md'; disp='routes/dispatch/FIX.md'
 for p in (repo/art,repo/inbox,repo/disp): p.parent.mkdir(parents=True,exist_ok=True)
 (repo/art).write_text('# fixture\n'); (repo/inbox).write_text('locator\n'); git(repo,'add','.'); git(repo,'commit','-q','-m','artifact')
 ac=git(repo,'rev-parse','HEAD'); blob=git(repo,'rev-parse',f'HEAD:{art}'); sha=hashlib.sha256((repo/art).read_bytes()).hexdigest()
 (repo/disp).write_text(f'sender: koordinator\nrecipient: {recipient}\nexchange_gate: v1\ninbox_path: `{inbox}`\nartifacts:\n- `{artifact_ref}` @ `{ac}`\n')
 git(repo,'add','.'); git(repo,'commit','-q','-m','dispatch'); dc=git(repo,'rev-parse','HEAD')
 loc={'artifact_path':art,'artifact_commit':ac,'artifact_blob':blob,'artifact_sha256':sha,'sender':'koordinator','recipient':'koder','exchange_gate':'v1','dispatch_path':disp,'dispatch_commit':dc,'inbox_path':inbox}
 rec={'entity':'koder','state':'verified','current_writer_state':'known_writer_unchanged','recovery_identity':'fixture-v2'}
 artcopy=td/'artifact.md'; artcopy.write_bytes((repo/art).read_bytes()); lp=td/'locator.json'; rp=td/'recovery.json'; dump(lp,loc); dump(rp,rec)
 handler=td/'handler.py'; handler.write_text("import os;from pathlib import Path;Path(os.environ['WB_RESULT_PATH']).write_text('ok\\n')\n")
 return repo,artcopy,lp,rp,loc,rec,handler

def run(td,repo,art,lp,rp,handler):
 ev=td/'e.json'; result=td/'r.txt'; cp=subprocess.run([sys.executable,str(WORKER),'--locator',str(lp),'--artifact',str(art),'--recovery',str(rp),'--git-repo',str(repo),'--state-dir',str(td/'state'),'--evidence',str(ev),'--result',str(result),'--handler',sys.executable,str(handler)],capture_output=True,text=True); return cp,json.loads(ev.read_text())

def case(name,mutate=None,expect=0,reason=None,recipient='koder',artifact_ref='entities/koordinator/outbox/FIX.md'):
 with tempfile.TemporaryDirectory() as x:
  td=Path(x); repo,art,lp,rp,loc,rec,h=fixture(td,recipient,artifact_ref)
  if mutate: mutate(td,repo,art,lp,rp,loc,rec)
  cp,ev=run(td,repo,art,lp,rp,h); assert cp.returncode==expect,(name,cp.stdout,cp.stderr); assert ev['state']!='processing_started' if expect else True
  if reason: assert ev.get('reason')==reason,(name,ev)
  print('PASS',name)

case('verified_immutable_chain')
case('fake_commit',lambda td,r,a,lp,rp,l,rc:(l.__setitem__('artifact_commit','a'*40),dump(lp,l)),21,'artifact_commit_not_found')
case('blob_mismatch',lambda td,r,a,lp,rp,l,rc:(l.__setitem__('artifact_blob','b'*40),dump(lp,l)),21,'artifact_blob_mismatch')
case('dispatch_recipient_mismatch',recipient='someoneelse',expect=21,reason='dispatch_recipient_mismatch')
case('dispatch_artifact_mismatch',artifact_ref='entities/koordinator/outbox/OTHER.md',expect=21,reason='dispatch_artifact_mismatch')
case('provider_unavailable',lambda td,r,a,lp,rp,l,rc:r.rename(td/'gone'),21,'provider_unavailable_or_unreadable')
case('local_sha_mismatch',lambda td,r,a,lp,rp,l,rc:a.write_text('tampered\n'),21,'artifact_sha256_mismatch')
case('unknown_writer_state',lambda td,r,a,lp,rp,l,rc:(rc.__setitem__('current_writer_state','unknown'),dump(rp,rc)),22,'current_writer_state_unknown_or_conflicting')
print('RESULT 8/8 PASS')
