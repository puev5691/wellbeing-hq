import os,tempfile,unittest
from gateway import *
PUB={"publication_id":"tg-sandbox-fixture-001","environment":"sandbox","synthetic":True,"content_layer":"system-test","source_identity":{"scheme":"synthetic","id":"tg-phase0-fixture-001"},"canonical":{"url":"https://example.invalid/wellbeing/tg-phase0-fixture-001","readback_state":"synthetic_pass"},"release":{"state":"synthetic_authorized_for_test_only"},"target":{"platform":"telegram","channel_key":"sandbox-channel"},"derivative":{"type":"telegram-test-message","text":"SANDBOX TEST: wellbeing media-gateway fixture. No public project content."}}
AUTO={"update_id":5001,"message":{"message_id":2001,"chat":{"id":-1002000000002,"type":"supergroup"},"date":2,"is_automatic_forward":True,"forward_origin":{"type":"channel","date":1,"chat":{"id":-1001000000001,"type":"channel"},"message_id":1001}}}
COMMENT={"update_id":5002,"message":{"message_id":2002,"message_thread_id":2001,"chat":{"id":-1002000000002,"type":"supergroup"},"from":{"id":424242,"is_bot":False,"first_name":"Test User"},"date":3,"reply_to_message":{"message_id":2001,"chat":{"id":-1002000000002,"type":"supergroup"}},"text":"Тестовый комментарий."}}
REACT={"update_id":5003,"message_reaction_count":{"chat":{"id":-1001000000001,"type":"channel"},"message_id":1001,"date":4,"reactions":[{"type":{"type":"emoji","emoji":"👍"},"total_count":2},{"type":{"type":"emoji","emoji":"❤"},"total_count":1}]}}
CORR={"publication_id":"tg-sandbox-fixture-001","action":"correct","revision":2,"derivative":{"text":"SANDBOX TEST v2: corrected test message. No public project content."}}
class T(unittest.TestCase):
 def setUp(self): self.t=tempfile.TemporaryDirectory();self.db=os.path.join(self.t.name,"g.db");self.a=FakeTelegramAdapter();self.g=Gateway(self.db,self.a)
 def tearDown(self):
  try:self.g.db.close()
  except:pass
  self.t.cleanup()
 def seed(self): self.g.publish(PUB);self.g.verify_echo(PUB["publication_id"]);self.g.handle_update(AUTO);self.g.handle_update(COMMENT);self.g.handle_update(REACT);self.g.snapshot_members()
 def test_positive_restart_duplicate(self):
  self.seed();self.g.correct(CORR);r=self.g.safe_receipt(PUB["publication_id"]);self.assertEqual((r["channel_message_id"],r["discussion_root_message_id"],r["comments_count"],r["reaction_total"],r["channel_member_count"],r["discussion_member_count"]),(1001,2001,1,3,10,5));self.assertFalse(r["personal_data_exported"]);self.g.db.close();self.g=Gateway(self.db,self.a);self.assertEqual(self.g.publish(PUB)["status"],"duplicate_noop");self.assertEqual(self.a.send_calls,1)
 def test_duplicate_update(self): self.g.publish(PUB);self.g.handle_update(AUTO);self.g.handle_update(COMMENT);self.assertEqual(self.g.handle_update(COMMENT)["status"],"duplicate_update_noop");self.assertEqual(self.g.safe_receipt(PUB["publication_id"])["comments_count"],1)
 def test_malformed(self):
  x=dict(PUB);x["publication_id"]="BAD"
  with self.assertRaisesRegex(GatewayError,"malformed"):self.g.publish(x)
 def test_missing_target(self):
  x=dict(PUB);x.pop("target")
  with self.assertRaisesRegex(GatewayError,"missing_target"):self.g.publish(x)
 def test_missing_derivative(self):
  x=dict(PUB);x.pop("derivative")
  with self.assertRaisesRegex(GatewayError,"missing_derivative"):self.g.publish(x)
 def test_unknown_auto(self):
  x={**AUTO,"update_id":5101,"message":{**AUTO["message"],"forward_origin":{**AUTO["message"]["forward_origin"],"message_id":9999}}}
  with self.assertRaisesRegex(GatewayError,"unknown_auto"):self.g.handle_update(x)
 def test_unknown_discussion(self):
  x={**COMMENT,"update_id":5102,"message":{**COMMENT["message"],"message_thread_id":9999,"reply_to_message":{"message_id":9999}}}
  with self.assertRaisesRegex(GatewayError,"unknown_discussion"):self.g.handle_update(x)
 def test_unknown_reaction(self):
  x={**REACT,"update_id":5103,"message_reaction_count":{**REACT["message_reaction_count"],"message_id":9999}}
  with self.assertRaisesRegex(GatewayError,"unknown_reaction"):self.g.handle_update(x)
 def test_send_failure(self):
  g=Gateway(os.path.join(self.t.name,"s.db"),FakeTelegramAdapter(fail_send=True))
  with self.assertRaisesRegex(GatewayError,"adapter_send"):g.publish(PUB)
  self.assertEqual(g.db.execute("select state from publications").fetchone()[0],"failed")
 def test_edit_failure(self):
  self.g.publish(PUB);self.g.adapter.fail_edit=True
  with self.assertRaisesRegex(GatewayError,"adapter_edit"):self.g.correct(CORR)
 def test_restart_dispatching(self): self.g.publish(PUB);self.g.db.execute("update publications set state='dispatching'");self.g.db.commit();self.g.db.close();self.g=Gateway(self.db,self.a);self.assertEqual(self.g.db.execute("select state from publications").fetchone()[0],"prepared")
 def test_safe_receipt(self): self.seed();s=str(self.g.safe_receipt(PUB["publication_id"]));self.assertNotIn("424242",s);self.assertNotIn("Test User",s);self.assertNotIn("Тестовый комментарий.",s)
 def test_db_write_failure(self): self.g.db.execute("drop table publications");self.g.db.commit();self.assertRaisesRegex(GatewayError,"db_write_failure",self.g.publish,PUB)
 def test_attempt_raw_identity_export(self): self.seed();self.assertRaisesRegex(GatewayError,"raw_identity_export_blocked",self.g.safe_receipt,PUB["publication_id"],True)
if __name__=="__main__":unittest.main(verbosity=2)
