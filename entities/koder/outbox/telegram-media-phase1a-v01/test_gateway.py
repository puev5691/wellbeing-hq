import os,tempfile,unittest
from gateway import *
CHANNEL=-1007770001111; DISCUSSION=-1007770002222
def cfg(**o):
 r={'environment':'sandbox','channel_key':'wbnp-experimental','channel_username':'wbnp_pev5691_15042026','channel_chat_id':CHANNEL,'discussion_linked':True,'discussion_chat_id':DISCUSSION,'bot_identity':'publisher-bot-metadata-only','webhook_endpoint':'https://example.invalid/telegram/webhook'}; r.update(o); return RuntimeConfig.from_dict(r)
def pub(pid='p1',target='telegram:wbnp-experimental',text='synthetic phase1a test'): return {'publication_id':pid,'distribution_target':target,'text':text}
class T(unittest.TestCase):
 def make(self):
  td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup); tr=FakeTransport(); gw=Gateway(os.path.join(td.name,'g.db'),cfg(),TelegramBotAdapter(cfg(),tr)); return gw,tr
 def sendq(self,tr,mid=101,chat=CHANNEL): tr.queue('sendMessage',{'ok':True,'result':{'message_id':mid,'chat':{'id':chat}}})
 def test_missing_chat_id(self):
  with self.assertRaises(ConfigError): RuntimeConfig.from_dict({'environment':'sandbox','channel_key':'x','discussion_linked':False,'bot_identity':'x'})
 def test_unknown_chat_id(self):
  with self.assertRaises(ConfigError): cfg(channel_chat_id='UNKNOWN')
 def test_phase0_id_rejected(self):
  with self.assertRaises(ConfigError): cfg(channel_chat_id=-1001000000001)
 def test_same_mid_two_chats_no_collision(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); other=CHANNEL+999; gw.db.execute("INSERT INTO publications VALUES ('p2',1,'x')"); gw.db.execute("INSERT INTO deliveries VALUES ('p2','t2',?,101,'delivered_unverified','x')",(other,)); gw.db.commit(); self.assertEqual(gw.db.execute('SELECT count(*) FROM deliveries WHERE external_message_id=101').fetchone()[0],2)
 def test_wrong_forward_chat(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); u={'update_id':1,'message':{'message_id':201,'chat':{'id':DISCUSSION},'is_automatic_forward':True,'forward_origin':{'type':'channel','chat':{'id':CHANNEL+1},'message_id':101}}}; self.assertRaises(ValidationError,gw.ingest_update,u)
 def test_wrong_forward_message(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); u={'update_id':2,'message':{'message_id':201,'chat':{'id':DISCUSSION},'is_automatic_forward':True,'forward_origin':{'type':'channel','chat':{'id':CHANNEL},'message_id':999}}}; self.assertRaises(ValidationError,gw.ingest_update,u)
 def test_verify_composite(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); self.assertFalse(gw.verify_delivery('p1','telegram:wbnp-experimental',{'chat_id':CHANNEL,'message_id':999})); self.assertTrue(gw.verify_delivery('p1','telegram:wbnp-experimental',{'chat_id':CHANNEL,'message_id':101}))
 def test_multi_target(self):
  gw,tr=self.make(); self.sendq(tr,101); self.sendq(tr,102); gw.publish(pub('p1','a','a')); gw.publish(pub('p1','b','b')); self.assertEqual(gw.db.execute('SELECT count(*) FROM deliveries').fetchone()[0],2)
 def test_fake_transport_only(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); self.assertEqual([x[0] for x in tr.calls],['sendMessage'])
 def test_privacy_default(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); gw.ingest_update({'update_id':3,'message':{'message_id':201,'chat':{'id':DISCUSSION},'is_automatic_forward':True,'forward_origin':{'type':'channel','chat':{'id':CHANNEL},'message_id':101}}}); out=gw.ingest_update({'update_id':4,'message':{'message_id':202,'message_thread_id':201,'chat':{'id':DISCUSSION},'from':{'id':424242,'first_name':'Test User'},'text':'raw'}}); self.assertFalse(out['identity_stored']); self.assertFalse(out['raw_text_stored']); r=gw.safe_receipt('p1','telegram:wbnp-experimental'); self.assertFalse(r['personal_data_exported'])
 def test_update_dedupe(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); u={'update_id':5,'message':{'message_id':201,'chat':{'id':DISCUSSION},'is_automatic_forward':True,'forward_origin':{'type':'channel','chat':{'id':CHANNEL},'message_id':101}}}; gw.ingest_update(u); self.assertTrue(gw.ingest_update(u)['duplicate_update'])
 def test_correction_no_resend(self):
  gw,tr=self.make(); self.sendq(tr); gw.publish(pub()); tr.queue('editMessageText',{'ok':True,'result':{'message_id':101,'chat':{'id':CHANNEL}}}); o=gw.correct('p1','telegram:wbnp-experimental',2,'corrected'); self.assertFalse(o['new_send']); self.assertEqual([m for m,_ in tr.calls].count('sendMessage'),1)
 def test_restart(self):
  td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup); path=os.path.join(td.name,'g.db'); tr=FakeTransport(); gw=Gateway(path,cfg(),TelegramBotAdapter(cfg(),tr)); self.sendq(tr); gw.publish(pub()); gw.verify_delivery('p1','telegram:wbnp-experimental',{'chat_id':CHANNEL,'message_id':101}); gw.db.close(); gw2=Gateway(path,cfg(),TelegramBotAdapter(cfg(),FakeTransport())); self.assertEqual(gw2.safe_receipt('p1','telegram:wbnp-experimental')['delivery_state'],'delivered_verified')
 def test_phase0_compatible(self):
  gw,tr=self.make(); self.sendq(tr,1001); gw.publish(pub('tg-sandbox-fixture-001','telegram:sandbox-channel','SANDBOX TEST: wellbeing media-gateway fixture. No public project content.')); u={'update_id':5001,'message':{'message_id':2001,'chat':{'id':DISCUSSION},'is_automatic_forward':True,'forward_origin':{'type':'channel','chat':{'id':CHANNEL},'message_id':1001}}}; self.assertTrue(gw.ingest_update(u)['mapped'])
 def test_wrong_send_chat(self):
  gw,tr=self.make(); self.sendq(tr,101,CHANNEL+99); self.assertRaises(ValidationError,gw.publish,pub())
 def test_unapproved_privacy_mode(self):
  with self.assertRaises(ConfigError): cfg(privacy_mode='store_raw_identity')
if __name__=='__main__': unittest.main(verbosity=2)
