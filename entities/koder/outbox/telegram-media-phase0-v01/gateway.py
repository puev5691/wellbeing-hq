import json,re,sqlite3,hashlib
PUB_RE=re.compile(r"^[a-z0-9][a-z0-9-]{2,127}$")
class GatewayError(RuntimeError): pass
class FakeTelegramAdapter:
    def __init__(self,fail_send=False,fail_edit=False): self.fail_send=fail_send;self.fail_edit=fail_edit;self.send_calls=0;self.edit_calls=0
    def send(self,p):
        self.send_calls+=1
        if self.fail_send: raise GatewayError("adapter_send_failure")
        return {"ok":True,"result":{"message_id":1001,"chat":{"id":-1001000000001,"type":"channel"},"date":1,"text":p["text"]}}
    def edit(self,mid,text):
        self.edit_calls+=1
        if self.fail_edit: raise GatewayError("adapter_edit_failure")
        return {"ok":True,"result":{"message_id":mid,"text":text}}
    def member_counts(self): return {-1001000000001:10,-1002000000002:5}
class Gateway:
    def __init__(self,db_path,adapter=None):
        self.db=sqlite3.connect(db_path);self.db.row_factory=sqlite3.Row;self.adapter=adapter or FakeTelegramAdapter()
        self.db.executescript("""CREATE TABLE IF NOT EXISTS publications(publication_id TEXT,target_channel TEXT,environment TEXT,synthetic INTEGER,state TEXT,channel_message_id INTEGER,revision INTEGER DEFAULT 1,payload_hash TEXT,previous_payload_hash TEXT,comments_count INTEGER DEFAULT 0,reaction_total INTEGER DEFAULT 0,channel_member_count INTEGER,discussion_member_count INTEGER,PRIMARY KEY(publication_id,target_channel));CREATE TABLE IF NOT EXISTS discussion_map(publication_id TEXT PRIMARY KEY,channel_message_id INTEGER UNIQUE,discussion_chat_id INTEGER,discussion_root_message_id INTEGER UNIQUE);CREATE TABLE IF NOT EXISTS processed_updates(update_id INTEGER PRIMARY KEY);CREATE TABLE IF NOT EXISTS comments(update_id INTEGER PRIMARY KEY,publication_id TEXT,user_id INTEGER,first_name TEXT,raw_text TEXT);CREATE TABLE IF NOT EXISTS reactions(publication_id TEXT PRIMARY KEY,reaction_json TEXT,total INTEGER);CREATE TABLE IF NOT EXISTS member_snapshots(chat_id INTEGER,synthetic_tick INTEGER,count INTEGER,PRIMARY KEY(chat_id,synthetic_tick));""")
        self.db.execute("UPDATE publications SET state='prepared' WHERE state='dispatching'");self.db.commit()
    def validate_publication(self,p):
        pid=p.get("publication_id","");t=p.get("target");d=p.get("derivative")
        if not PUB_RE.match(pid): raise GatewayError("malformed_publication_id")
        if not isinstance(t,dict) or t.get("platform")!="telegram" or not t.get("channel_key"): raise GatewayError("missing_target")
        if not isinstance(d,dict) or not d.get("text"): raise GatewayError("missing_derivative")
        return pid,t["channel_key"],d["text"]
    def publish(self,p):
        pid,target,text=self.validate_publication(p);h=hashlib.sha256(text.encode()).hexdigest()
        try:
            r=self.db.execute("select * from publications where publication_id=? and target_channel=?",(pid,target)).fetchone()
            if r:return {"status":"duplicate_noop","channel_message_id":r["channel_message_id"]}
            self.db.execute("insert into publications(publication_id,target_channel,environment,synthetic,state,payload_hash) values(?,?,?,?,?,?)",(pid,target,p.get("environment",""),int(bool(p.get("synthetic"))),"prepared",h));self.db.execute("update publications set state='dispatching' where publication_id=?",(pid,));self.db.commit()
            mid=self.adapter.send({"text":text})["result"]["message_id"]
            self.db.execute("update publications set state='delivered_unverified',channel_message_id=? where publication_id=?",(mid,pid));self.db.commit();return {"status":"sent","channel_message_id":mid}
        except GatewayError:
            self.db.execute("update publications set state='failed' where publication_id=?",(pid,));self.db.commit();raise
        except sqlite3.DatabaseError:
            self.db.rollback();raise GatewayError("db_write_failure")
    def verify_echo(self,pid): self.db.execute("update publications set state='delivered_verified' where publication_id=?",(pid,));self.db.commit()
    def handle_update(self,u):
        uid=u.get("update_id")
        if not isinstance(uid,int): raise GatewayError("missing_update_id")
        if self.db.execute("select 1 from processed_updates where update_id=?",(uid,)).fetchone():return {"status":"duplicate_update_noop"}
        try:
            m=u.get("message")
            if isinstance(m,dict) and m.get("is_automatic_forward"):
                cmid=(m.get("forward_origin") or {}).get("message_id");p=self.db.execute("select publication_id from publications where channel_message_id=?",(cmid,)).fetchone()
                if not p:raise GatewayError("unknown_auto_forward_source")
                self.db.execute("insert into discussion_map values(?,?,?,?)",(p["publication_id"],cmid,m["chat"]["id"],m["message_id"]))
            elif isinstance(m,dict):
                root=(m.get("reply_to_message") or {}).get("message_id") or m.get("message_thread_id");d=self.db.execute("select publication_id from discussion_map where discussion_root_message_id=?",(root,)).fetchone()
                if not d:raise GatewayError("unknown_discussion_root")
                f=m.get("from") or {};pid=d["publication_id"];self.db.execute("insert into comments values(?,?,?,?,?)",(uid,pid,f.get("id"),f.get("first_name"),m.get("text")));self.db.execute("update publications set comments_count=comments_count+1 where publication_id=?",(pid,))
            elif "message_reaction_count" in u:
                r=u["message_reaction_count"];p=self.db.execute("select publication_id from publications where channel_message_id=?",(r.get("message_id"),)).fetchone()
                if not p:raise GatewayError("unknown_reaction_publication")
                c={}
                for x in r.get("reactions",[]):
                    emoji=(x.get("type") or {}).get("emoji")
                    if emoji:c[emoji]=int(x.get("total_count",0))
                total=sum(c.values());pid=p["publication_id"]
                self.db.execute("insert or replace into reactions values(?,?,?)",(pid,json.dumps(c,ensure_ascii=False),total));self.db.execute("update publications set reaction_total=? where publication_id=?",(total,pid))
            else:raise GatewayError("unsupported_update")
            self.db.execute("insert into processed_updates values(?)",(uid,));self.db.commit();return {"status":"processed"}
        except GatewayError:self.db.rollback();raise
        except sqlite3.DatabaseError:self.db.rollback();raise GatewayError("db_write_failure")
    def snapshot_members(self,tick=1):
        c=self.adapter.member_counts()
        for k,v in c.items():self.db.execute("insert or replace into member_snapshots values(?,?,?)",(k,tick,v))
        self.db.execute("update publications set channel_member_count=?,discussion_member_count=?",(c[-1001000000001],c[-1002000000002]));self.db.commit()
    def correct(self,c):
        pid=c.get("publication_id");r=self.db.execute("select * from publications where publication_id=?",(pid,)).fetchone();text=(c.get("derivative") or {}).get("text");rev=c.get("revision")
        if not r:raise GatewayError("unknown_publication")
        if not isinstance(rev,int) or rev<=r["revision"] or not text:raise GatewayError("invalid_correction")
        self.adapter.edit(r["channel_message_id"],text);h=hashlib.sha256(text.encode()).hexdigest();self.db.execute("update publications set revision=?,previous_payload_hash=payload_hash,payload_hash=? where publication_id=?",(rev,h,pid));self.db.commit();return {"status":"corrected","channel_message_id":r["channel_message_id"],"revision":rev}
    def safe_receipt(self,pid,include_identity=False):
        if include_identity: raise GatewayError("raw_identity_export_blocked")
        r=self.db.execute("select * from publications where publication_id=?",(pid,)).fetchone();d=self.db.execute("select discussion_root_message_id from discussion_map where publication_id=?",(pid,)).fetchone()
        if not r:raise GatewayError("unknown_publication")
        return {"publication_id":pid,"environment":r["environment"],"delivery_state":r["state"],"channel_message_id":r["channel_message_id"],"discussion_root_message_id":d["discussion_root_message_id"] if d else None,"comments_count":r["comments_count"],"reaction_total":r["reaction_total"],"channel_member_count":r["channel_member_count"],"discussion_member_count":r["discussion_member_count"],"synthetic":bool(r["synthetic"]),"personal_data_exported":False,"production_publication":False}
