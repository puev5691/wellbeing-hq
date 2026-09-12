from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Any
import hashlib, json, sqlite3
PHASE0_SYNTHETIC_IDS={-1001000000001,-1002000000002}
class ConfigError(ValueError): pass
class ValidationError(ValueError): pass
class Transport(Protocol):
    def call(self, method:str, payload:dict[str,Any])->dict[str,Any]: ...
@dataclass(frozen=True)
class RuntimeConfig:
    environment:str; channel_key:str; channel_username:str|None; channel_chat_id:int; discussion_linked:bool; discussion_chat_id:int|None; bot_identity:str; webhook_endpoint:str|None; privacy_mode:str='discard_identity'
    @staticmethod
    def from_dict(raw):
        required=['environment','channel_key','channel_chat_id','discussion_linked','bot_identity']
        missing=[k for k in required if k not in raw]
        if missing: raise ConfigError('missing_config:'+','.join(missing))
        cid=raw['channel_chat_id']
        if not isinstance(cid,int): raise ConfigError('channel_chat_id_must_be_verified_integer')
        if cid in PHASE0_SYNTHETIC_IDS: raise ConfigError('synthetic_phase0_id_forbidden')
        linked=raw['discussion_linked']
        if linked not in (True,False): raise ConfigError('discussion_linked_must_be_boolean')
        did=raw.get('discussion_chat_id')
        if linked:
            if not isinstance(did,int): raise ConfigError('linked_discussion_requires_verified_integer_chat_id')
            if did in PHASE0_SYNTHETIC_IDS: raise ConfigError('synthetic_phase0_id_forbidden')
        elif did is not None: raise ConfigError('discussion_chat_id_requires_linked_true')
        if raw['environment'] not in {'sandbox','test'}: raise ConfigError('phase1a_nonproduction_environment_required')
        privacy=raw.get('privacy_mode','discard_identity')
        if privacy not in {'discard_identity','aggregate_only'}: raise ConfigError('privacy_mode_not_kan_approved')
        return RuntimeConfig(raw['environment'],str(raw['channel_key']),raw.get('channel_username'),cid,linked,did,str(raw['bot_identity']),raw.get('webhook_endpoint'),privacy)
class FakeTransport:
    def __init__(self): self.calls=[]; self.responses={}
    def queue(self,method,response): self.responses.setdefault(method,[]).append(response)
    def call(self,method,payload):
        self.calls.append((method,json.loads(json.dumps(payload))))
        if not self.responses.get(method): raise RuntimeError('no_fake_response:'+method)
        return self.responses[method].pop(0)
class TelegramBotAdapter:
    def __init__(self,config,transport):
        if transport is None: raise ConfigError('transport_injection_required')
        self.config=config; self.transport=transport
    def send(self,text): return self.transport.call('sendMessage',{'chat_id':self.config.channel_chat_id,'text':text})
    def edit(self,chat_id,message_id,text): return self.transport.call('editMessageText',{'chat_id':chat_id,'message_id':message_id,'text':text})
    def member_count(self,chat_id): return self.transport.call('getChatMemberCount',{'chat_id':chat_id})
    def validate_update(self,update):
        if not isinstance(update.get('update_id'),int): raise ValidationError('missing_update_id')
        return update['update_id']
class Gateway:
    def __init__(self,db_path,config,adapter): self.config=config; self.adapter=adapter; self.db=sqlite3.connect(db_path); self.db.row_factory=sqlite3.Row; self._init()
    def _init(self):
        self.db.executescript('''PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS publications(publication_id TEXT PRIMARY KEY, revision INTEGER NOT NULL DEFAULT 1, content_hash TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS deliveries(publication_id TEXT NOT NULL, distribution_target TEXT NOT NULL, external_chat_id INTEGER, external_message_id INTEGER, delivery_state TEXT NOT NULL, content_hash TEXT NOT NULL, PRIMARY KEY(publication_id,distribution_target), UNIQUE(external_chat_id,external_message_id));
CREATE TABLE IF NOT EXISTS discussion_threads(publication_id TEXT NOT NULL, distribution_target TEXT NOT NULL, discussion_chat_id INTEGER NOT NULL, discussion_root_message_id INTEGER NOT NULL, origin_channel_chat_id INTEGER NOT NULL, origin_channel_message_id INTEGER NOT NULL, PRIMARY KEY(publication_id,distribution_target,discussion_chat_id), UNIQUE(discussion_chat_id,discussion_root_message_id));
CREATE TABLE IF NOT EXISTS processed_updates(update_id INTEGER PRIMARY KEY);
CREATE TABLE IF NOT EXISTS aggregates(publication_id TEXT NOT NULL, distribution_target TEXT NOT NULL, comments_count INTEGER NOT NULL DEFAULT 0, reaction_total INTEGER NOT NULL DEFAULT 0, member_count INTEGER, PRIMARY KEY(publication_id,distribution_target));'''); self.db.commit()
    def _hash(self,t): return hashlib.sha256(t.encode()).hexdigest()
    def publish(self,p):
        pid,target,text=p.get('publication_id'),p.get('distribution_target'),p.get('text')
        if not isinstance(pid,str) or not pid.strip(): raise ValidationError('invalid_publication_id')
        if not isinstance(target,str) or not target.strip(): raise ValidationError('missing_distribution_target')
        if not isinstance(text,str) or not text.strip(): raise ValidationError('missing_text')
        row=self.db.execute('SELECT * FROM deliveries WHERE publication_id=? AND distribution_target=?',(pid,target)).fetchone()
        if row: return {'duplicate':True,'state':row['delivery_state'],'external_chat_id':row['external_chat_id'],'external_message_id':row['external_message_id']}
        h=self._hash(text); self.db.execute('INSERT OR IGNORE INTO publications(publication_id,content_hash) VALUES (?,?)',(pid,h)); self.db.execute('INSERT INTO deliveries(publication_id,distribution_target,delivery_state,content_hash) VALUES (?,?,?,?)',(pid,target,'dispatching',h)); self.db.execute('INSERT OR IGNORE INTO aggregates(publication_id,distribution_target) VALUES (?,?)',(pid,target)); self.db.commit()
        resp=self.adapter.send(text); msg=resp.get('result',{}); cid=(msg.get('chat') or {}).get('id'); mid=msg.get('message_id')
        if resp.get('ok') is not True or not isinstance(cid,int) or not isinstance(mid,int): raise ValidationError('send_response_missing_identity')
        if cid!=self.config.channel_chat_id: self.db.execute("UPDATE deliveries SET delivery_state='send_identity_mismatch' WHERE publication_id=? AND distribution_target=?",(pid,target)); self.db.commit(); raise ValidationError('send_response_wrong_chat')
        self.db.execute("UPDATE deliveries SET external_chat_id=?,external_message_id=?,delivery_state='delivered_unverified' WHERE publication_id=? AND distribution_target=?",(cid,mid,pid,target)); self.db.commit(); return {'duplicate':False,'state':'delivered_unverified','external_chat_id':cid,'external_message_id':mid}
    def verify_delivery(self,pid,target,evidence):
        row=self.db.execute('SELECT * FROM deliveries WHERE publication_id=? AND distribution_target=?',(pid,target)).fetchone()
        if not row: raise ValidationError('unknown_delivery')
        if evidence.get('chat_id')!=row['external_chat_id'] or evidence.get('message_id')!=row['external_message_id'] or evidence.get('chat_id')!=self.config.channel_chat_id: return False
        self.db.execute("UPDATE deliveries SET delivery_state='delivered_verified' WHERE publication_id=? AND distribution_target=?",(pid,target)); self.db.commit(); return True
    def ingest_update(self,u):
        uid=self.adapter.validate_update(u)
        if self.db.execute('SELECT 1 FROM processed_updates WHERE update_id=?',(uid,)).fetchone(): return {'duplicate_update':True}
        msg=u.get('message') or {}
        if msg.get('is_automatic_forward'): out=self._forward(msg)
        elif 'message_reaction_count' in u: out=self._reaction(u['message_reaction_count'])
        elif msg: out=self._comment(msg)
        else: out={'ignored':True}
        self.db.execute('INSERT INTO processed_updates(update_id) VALUES (?)',(uid,)); self.db.commit(); return out
    def _forward(self,msg):
        o=msg.get('forward_origin') or {}
        if o.get('type')!='channel': raise ValidationError('auto_forward_origin_not_channel')
        oc=((o.get('chat') or {}).get('id')); om=o.get('message_id')
        if oc!=self.config.channel_chat_id: raise ValidationError('auto_forward_wrong_origin_chat')
        row=self.db.execute('SELECT * FROM deliveries WHERE external_chat_id=? AND external_message_id=?',(oc,om)).fetchone()
        if not row: raise ValidationError('auto_forward_unknown_origin_message')
        dc=((msg.get('chat') or {}).get('id')); root=msg.get('message_id')
        if not self.config.discussion_linked: raise ValidationError('discussion_not_configured')
        if dc!=self.config.discussion_chat_id: raise ValidationError('auto_forward_wrong_discussion_chat')
        self.db.execute('INSERT OR IGNORE INTO discussion_threads VALUES (?,?,?,?,?,?)',(row['publication_id'],row['distribution_target'],dc,root,oc,om)); return {'mapped':True,'publication_id':row['publication_id'],'distribution_target':row['distribution_target']}
    def _comment(self,msg):
        cid=((msg.get('chat') or {}).get('id')); root=msg.get('message_thread_id') or ((msg.get('reply_to_message') or {}).get('message_id'))
        row=self.db.execute('SELECT * FROM discussion_threads WHERE discussion_chat_id=? AND discussion_root_message_id=?',(cid,root)).fetchone()
        if not row: raise ValidationError('comment_unknown_thread')
        self.db.execute('UPDATE aggregates SET comments_count=comments_count+1 WHERE publication_id=? AND distribution_target=?',(row['publication_id'],row['distribution_target'])); return {'comment_counted':True,'identity_stored':False,'raw_text_stored':False}
    def _reaction(self,r):
        cid=((r.get('chat') or {}).get('id')); mid=r.get('message_id'); row=self.db.execute('SELECT * FROM deliveries WHERE external_chat_id=? AND external_message_id=?',(cid,mid)).fetchone()
        if not row: raise ValidationError('reaction_unknown_delivery')
        total=sum(int(x.get('total_count',0)) for x in r.get('reactions',[])); self.db.execute('UPDATE aggregates SET reaction_total=? WHERE publication_id=? AND distribution_target=?',(total,row['publication_id'],row['distribution_target'])); return {'reaction_total':total}
    def correct(self,pid,target,revision,text):
        row=self.db.execute('SELECT * FROM deliveries WHERE publication_id=? AND distribution_target=?',(pid,target)).fetchone()
        if not row or row['external_chat_id'] is None: raise ValidationError('unknown_delivery')
        resp=self.adapter.edit(row['external_chat_id'],row['external_message_id'],text)
        if resp.get('ok') is not True: raise ValidationError('edit_failed')
        h=self._hash(text); self.db.execute('UPDATE publications SET revision=?,content_hash=? WHERE publication_id=?',(revision,h,pid)); self.db.execute('UPDATE deliveries SET content_hash=? WHERE publication_id=? AND distribution_target=?',(h,pid,target)); self.db.commit(); return {'corrected':True,'new_send':False,'message_id':row['external_message_id']}
    def safe_receipt(self,pid,target):
        row=self.db.execute('SELECT d.*,a.comments_count,a.reaction_total,a.member_count FROM deliveries d JOIN aggregates a USING(publication_id,distribution_target) WHERE publication_id=? AND distribution_target=?',(pid,target)).fetchone()
        if not row: raise ValidationError('unknown_delivery')
        return {'publication_id':row['publication_id'],'distribution_target':row['distribution_target'],'delivery_state':row['delivery_state'],'external_chat_id':row['external_chat_id'],'external_message_id':row['external_message_id'],'comments_count':row['comments_count'],'reaction_total':row['reaction_total'],'member_count':row['member_count'],'personal_data_exported':False,'raw_comment_exported':False,'production_publication':False,'privacy_policy':'fail_closed_pending_KAN'}
