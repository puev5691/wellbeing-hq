#!/usr/bin/env python3
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
WORKER=HERE/'KOD__activation-worker-v01__KOO.py'
HANDLER=HERE/'KOD__activation-worker-v01-fixture__KOO.py'
def dump(p,o): p.write_text(json.dumps(o,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
def base(td):
    art=td/'artifact.md'; art.write_text('# fixture\n',encoding='utf-8'); sha=hashlib.sha256(art.read_bytes()).hexdigest()
    loc={'artifact_path':'entities/koordinator/outbox/FIX.md','artifact_commit':'a'*40,'artifact_blob':'b'*40,'artifact_sha256':sha,'recipient':'koder','exchange_gate':'v1','dispatch_path':'routes/dispatch/FIX.md','inbox_path':'entities/koder/inbox/FIX.md'}
    rec={'entity':'koder','state':'verified','current_writer_state':'known_writer_unchanged','recovery_identity':'fixture-recovery-v1'}
    lp=td/'locator.json'; rp=td/'recovery.json'; dump(lp,loc); dump(rp,rec); return art,lp,rp,loc,rec
def invoke(td,lp,rp,art,ev,res,state):
    return subprocess.run([sys.executable,str(WORKER),'--locator',str(lp),'--artifact',str(art),'--recovery',str(rp),'--state-dir',str(state),'--evidence',str(ev),'--result',str(res),'--handler',sys.executable,str(HANDLER)],capture_output=True,text=True)
def chk(v,m):
    if not v: raise AssertionError(m)
T=[]
def t(n):
    def d(f): T.append((n,f)); return f
    return d
@t('happy_path_processing_started_to_result')
def _():
    with tempfile.TemporaryDirectory() as x:
        td=Path(x); art,lp,rp,_,_=base(td); ev=td/'e'; res=td/'r'; state=td/'s'; cp=invoke(td,lp,rp,art,ev,res,state); chk(cp.returncode==0,cp.stdout+cp.stderr); d=json.loads(ev.read_text()); chk(d['state']=='result_dispatched',d); chk(d['current_writer_claimed'] is False,d)
@t('sha_mismatch_fails_closed')
def _():
    with tempfile.TemporaryDirectory() as x:
        td=Path(x); art,lp,rp,loc,_=base(td); loc['artifact_sha256']='0'*64; dump(lp,loc); cp=invoke(td,lp,rp,art,td/'e',td/'r',td/'s'); chk(cp.returncode==21,cp.stdout)
@t('unknown_writer_state_fails_closed')
def _():
    with tempfile.TemporaryDirectory() as x:
        td=Path(x); art,lp,rp,_,rec=base(td); rec['current_writer_state']='unknown'; dump(rp,rec); cp=invoke(td,lp,rp,art,td/'e',td/'r',td/'s'); chk(cp.returncode==22,cp.stdout)
@t('idempotency_requires_explicit_retry')
def _():
    with tempfile.TemporaryDirectory() as x:
        td=Path(x); art,lp,rp,_,_=base(td); state=td/'s'; cp=invoke(td,lp,rp,art,td/'e1',td/'r1',state); chk(cp.returncode==0,cp.stdout); cp2=invoke(td,lp,rp,art,td/'e2',td/'r2',state); chk(cp2.returncode==23,cp2.stdout)
@t('recipient_mismatch_fails_closed')
def _():
    with tempfile.TemporaryDirectory() as x:
        td=Path(x); art,lp,rp,_,rec=base(td); rec['entity']='koordinator'; dump(rp,rec); cp=invoke(td,lp,rp,art,td/'e',td/'r',td/'s'); chk(cp.returncode==22,cp.stdout)
f=0
for n,fn in T:
    try: fn(); print('PASS',n)
    except Exception as e: f+=1; print('FAIL',n,repr(e))
print(f'RESULT {len(T)-f}/{len(T)} PASS'); raise SystemExit(1 if f else 0)
