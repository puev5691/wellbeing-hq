"""Deterministic in-memory protocol tests; no OS sockets or MAIN process."""
import hashlib, json, tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
PACKAGE=HERE.parent/'mlprep'
OLD=HERE/'frozen/broker.py'
NEW=HERE/'successor/broker.py'
CFG=HERE/'frozen/broker-config.json'
NEEDED=['recovery/'+x+'.json' for x in ('task-v2','promotion','checkpoint','input','task-v1','experience','raw-failure')]

class Exhausted(Exception):pass
def require(ok,why):
    if not ok:raise AssertionError(why)
class Conn:
    def __init__(self,loc):self.loc=loc;self.reply=None
    def recv(self,_):return json.dumps({'op':'read','locator':self.loc},separators=(',',':')).encode()
    def sendall(self,raw):self.reply=json.loads(raw)
    def close(self):pass
class Server:
    def __init__(self,queue):self.queue=list(queue);self.closed=False
    def bind(self,path):Path(path).touch()
    def listen(self,_):pass
    def accept(self):
        if not self.queue:raise Exhausted()
        return self.queue.pop(0),None
    def close(self):self.closed=True

def run(locators,cap=None):
    with tempfile.TemporaryDirectory(prefix='ml-broker-offline-') as d:
        base=Path(d)
        for folder in ('supervisor/package','broker-runtime','evidence'):(base/folder).mkdir(parents=True)
        cfg=json.loads(CFG.read_bytes())
        if cap is not None:cfg['max_bytes']=cap
        (base/'supervisor/broker-config.json').write_text(json.dumps(cfg,sort_keys=True)+'\n')
        for item in cfg['allowlist']:
            data=(PACKAGE/item['path']).read_bytes()
            require(hashlib.sha256(data).hexdigest()==item['sha256'] and len(data)==item['bytes'],'fixture mismatch')
            p=base/'supervisor/package'/item['path'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
        conns=[Conn(loc) for loc in locators];server=Server(conns)
        class FakeSocket:
            AF_UNIX=1;SOCK_STREAM=1
            @staticmethod
            def socket(family,kind):
                require((family,kind)==(1,1),'unexpected socket family')
                return server
        source=NEW.read_text()
        code=source.replace('import json, os, socket, sys','import json, os, sys\nsocket=FakeSocket')
        code=code.replace('BASE=Path("/home/shd/ml-e2e-r01-admission")',f'BASE=Path({str(base)!r})')
        require(code!=source and 'socket=FakeSocket' in code,'test transport patch failed')
        try:exec(compile(code,'<same-successor-code-in-memory-transport>','exec'),{'FakeSocket':FakeSocket})
        except Exhausted:pass
        log=base/'evidence/broker-readiness-log.json'
        return [c.reply for c in conns],json.loads(log.read_text()) if log.exists() else None,cfg,server.closed

def main():
    old=OLD.read_bytes();new=NEW.read_bytes();config=CFG.read_bytes()
    require(hashlib.sha256(old).hexdigest()=='e087c602ede9ce6ef74422be2add1e77f073d7713097344b582d9dfaae8c1b86','old code identity')
    require(hashlib.sha256(config).hexdigest()=='0037645f9f43487246b838b7f590a9c42b71a3542dd2a35dcca6798093d10974','old config identity')
    expected=old.decode().replace('while len(events) < cfg["sentinel_request_budget"]:',
        '# Serve the entire admitted read budget, then process one explicit DENY_READ_LIMIT.\n'
        '# The old sentinel_request_budget=4 remains historical config evidence only.\n'
        'while reads <= max_reads:')
    require(new.decode()==expected,'only loop must differ')
    cfg=json.loads(config)
    require(cfg['max_reads']==32 and cfg['max_bytes']==262144 and cfg['sentinel_request_budget']==4 and len(cfg['allowlist'])==11,'contract changed')
    require(sum(x['bytes'] for x in cfg['allowlist'] if x['path'] in NEEDED)==3531,'seven-read size changed')
    r,_,c,closed=run(NEEDED)
    require(len(r)==7 and all(x['status']=='OK' and x['reads']==i+1 for i,x in enumerate(r)) and r[-1]['semantic_bytes']==3531 and not closed,'seven sequential reads')
    r,log,c2,closed=run([NEEDED[0]]*33)
    require(all(x['status']=='OK' and x['reads']==i+1 for i,x in enumerate(r[:32])),'32 reads')
    require(r[32]['reason']=='READ_LIMIT' and r[32]['reads']==33 and closed and log['events'][-1]['decision']=='DENY_READ_LIMIT','33rd denial')
    r,_,c3,_=run([NEEDED[0]]*2,cap=600)
    require(r[0]['status']=='OK' and r[1]['reason']=='BYTE_LIMIT' and r[1]['semantic_bytes']==562,'byte bound')
    r,_,c4,_=run(['unknown','full-corpus','verifier-private/oracle.json','recovery/raw-noise.json',NEEDED[0]])
    require([x['reason'] for x in r[:4]]==['UNKNOWN_LOCATOR','FORBIDDEN_LOCATOR','FORBIDDEN_LOCATOR','FORBIDDEN_LOCATOR'] and r[4]['status']=='OK' and r[4]['reads']==5,'denied cases')
    require(all(x['allowlist']==cfg['allowlist'] for x in (c,c2,c3,c4)),'allowlist mutated')
    print(json.dumps({'evidence_class':'OFFLINE_SYNTHETIC_IN_MEMORY_BROKER_PROTOCOL','tests':6,'passed':6,'required_sequential_reads':7,'required_bytes':3531,'allowed_reads':32,'denied_read':33,'max_bytes':262144,'byte_limit_denied':True,'unknown_full_corpus_oracle_denied':True,'allowlist_unchanged':True,'provider_calls':0,'worker_network_calls':0,'main_attempts_by_test':0,'host_mutations':0,'runtime_socket_tested':False},sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
