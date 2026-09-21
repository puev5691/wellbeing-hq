import copy, json, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import review_result_store as store
import shape_diag_successor_runner as runner
import diagnostic_reviewable_live_worker as diag
from test_successor_wiring import MSG, REASON, Resolver, Client, body

ROOT=Path(__file__).resolve().parent
IDENTITY=dict(attempt_key='1'*64,request_sha256='2'*64,task_commit=runner.TASK_COMMIT,
              task_blob=runner.TASK_BLOB,writer_blob=runner.WRITER_BLOB,plan_sha256='3'*64,
              authority_sha256='4'*64,provider='openai',model=runner.MODEL)

class Policy(unittest.TestCase):
    def normalize(self,items):
        return store.normalize_openai_result(body=body(items),http_status=200,
                  provider_calls=1,retries=0,fallback='none',**IDENTITY)

    def test_reasoning_before_between_after_is_not_result(self):
        reason=dict(REASON,summary=[{'type':'summary_text','text':'PRIVATE_REASON_MARKER'}],
                    encrypted_content='OPAQUE_MARKER',content=[{'type':'output_text','text':'NOT_REVIEW'}])
        for items in ([reason,MSG],[MSG,reason],[reason,MSG,reason]):
            with self.subTest(items=len(items)):
                rec=self.normalize(items)
                self.assertEqual(rec['review_payload']['text'],'SYNTHETIC_OK')
                self.assertEqual(len(rec['response_evidence']['output']),1)
                for marker in ('PRIVATE_REASON_MARKER','OPAQUE_MARKER','NOT_REVIEW','reasoning'):
                    self.assertNotIn(marker,json.dumps(rec))
                store.validate_record(rec,**IDENTITY)

    def test_reasoning_only_does_not_produce_result(self):
        with self.assertRaises(store.PersistenceError):self.normalize([REASON])

    def test_tools_actions_unknown_and_metadata_aliases_stay_blocked(self):
        for typ in ('function_call','tool_call','computer_call','web_search_call','file_search_call',
                    'function_call_output','tool_call_output','unknown','metadata','reasoning_summary','Reasoning'):
            for items in ([REASON,{'type':typ},MSG],[MSG,REASON,{'type':typ}]):
                with self.subTest(type=typ,position=items[0]['type']):
                    with self.assertRaisesRegex(store.PersistenceError,'BLOCKED_UNEXPECTED_PROVIDER_ACTION'):
                        self.normalize(items)

    def test_nonassistant_roles_stay_blocked(self):
        for role in ('user','system','tool',None):
            with self.subTest(role=role):
                with self.assertRaisesRegex(store.PersistenceError,'BLOCKED_UNEXPECTED_PROVIDER_ACTION'):
                    self.normalize([REASON,dict(MSG,role=role)])

    def test_disallowed_message_content_stays_blocked(self):
        for typ in ('reasoning_text','summary_text','refusal','function_call','tool_call','image','unknown'):
            with self.subTest(type=typ):
                with self.assertRaisesRegex(store.PersistenceError,'BLOCKED_UNEXPECTED_PROVIDER_ACTION'):
                    self.normalize([REASON,dict(MSG,content=[{'type':typ,'text':'NOT_ALLOWED'}])])

    def test_no_valid_prefix_acceptance_with_later_invalid_message(self):
        with self.assertRaises(store.PersistenceError):self.normalize([MSG,REASON,dict(MSG,content=[])])

    def test_plain_assistant_and_existing_multiple_text_semantics(self):
        self.assertEqual(self.normalize([MSG])['review_payload']['text'],'SYNTHETIC_OK')
        # Existing contract concatenates text messages; this policy does not broaden it.
        self.assertEqual(self.normalize([MSG,REASON,MSG])['review_payload']['text'],'SYNTHETIC_OK\nSYNTHETIC_OK')

    def test_review_readback_rejects_reasoning_in_evidence(self):
        rec=self.normalize([REASON,MSG]);rec['response_evidence']['output'].insert(0,REASON)
        with self.assertRaises(store.PersistenceError):store.validate_record(rec,**IDENTITY)

    def test_review_readback_detects_tampered_text(self):
        rec=self.normalize([REASON,MSG]);rec['review_payload']['text']='TAMPERED'
        with self.assertRaisesRegex(store.PersistenceError,'BLOCKED_REVIEW_PAYLOAD'):
            store.validate_record(rec,**IDENTITY)

class Ordering(unittest.TestCase):
    def setUp(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup);self.root=Path(td.name)
        self.events=[]
        self.worker=runner.load_pinned(ROOT/'live_worker.py',runner.WORKER_SHA256,'_test_final_worker')
        o=json.loads((ROOT/'SENTINEL-INVOCATION.example.json').read_text())
        o.update(mode='LIVE',authority_id='SYNTHETIC_OFFLINE_ORDERING_ONLY')
        self.plan=runner.make_plan(self.worker,o)
        self.client=Client(body([REASON,MSG]));self.resolver=Resolver()
        self.rw=diag.DiagnosticReviewableLiveWorker(worker_path=ROOT/'live_worker.py',
            result_integration_path=ROOT/'reviewable_live_worker.py',result_store_path=ROOT/'review_result_store.py',
            shape_store_path=ROOT/'response_shape_store.py',ledger_path=self.root/'ledger.sqlite',
            shape_dir=self.root/'shape',result_dir=self.root/'review',resolver=self.resolver,client=self.client)
        self.identity=diag.Identity(runner.TASK_COMMIT,runner.TASK_BLOB,runner.WRITER_BLOB)

    def invoke(self,fail=None):
        from contextlib import ExitStack
        with ExitStack() as stack:
            def wrap(obj,name,label,error=None):
                original=getattr(obj,name)
                def hooked(*a,**kw):
                    self.events.append(label)
                    if fail==label:raise error('SYNTHETIC_READBACK_FAILURE')
                    return original(*a,**kw)
                stack.enter_context(patch.object(obj,name,hooked))
            wrap(self.rw.worker.DurableOneShotLedger,'claim','claim')
            wrap(self.resolver,'resolve','synthetic_resolver')
            wrap(self.client,'request','synthetic_transport')
            wrap(self.rw.shape_store,'persist_atomic','shape_persist')
            wrap(self.rw.shape_store,'read_and_validate','shape_readback',self.rw.shape_store.DiagnosticError)
            wrap(self.rw.result_store,'normalize_openai_result','normalize')
            wrap(self.rw.result_store,'persist_atomic','review_persist')
            wrap(self.rw.result_store,'read_and_validate','review_readback',self.rw.result_store.PersistenceError)
            return self.rw.invoke_once_persist_shape_then_normalize(self.plan,self.identity,now_tick=1)

    def test_persistence_and_strict_readback_order(self):
        out=self.invoke()
        self.assertEqual(self.events,['claim','synthetic_resolver','synthetic_transport','shape_persist',
                                    'shape_readback','normalize','review_persist','review_readback'])
        self.assertEqual(out['status'],'PASS_AFTER_SHAPE_AND_REVIEW_PERSISTENCE')
        self.assertEqual((self.client.calls,self.resolver.calls),(1,1))
        self.assertEqual((out['retries'],out['fallback']),(0,'none'))
        self.assertEqual(out['project_acceptance'],'NOT_GRANTED')
        self.assertFalse(out['project_state_mutation'])

    def test_shape_readback_failure_blocks_normalization(self):
        with self.assertRaisesRegex(diag.ShapeIntegrationError,'BLOCKED_SHAPE_DIAGNOSTIC_PERSISTENCE'):
            self.invoke('shape_readback')
        self.assertNotIn('normalize',self.events)
        self.assertFalse((self.root/'review').exists())

    def test_review_readback_failure_blocks_terminal_pass(self):
        with self.assertRaisesRegex(diag.ShapeIntegrationError,'BLOCKED_REVIEW_RESULT_PERSISTENCE_AFTER_SHAPE_SAVED'):
            self.invoke('review_readback')
        self.assertEqual(self.events[-1],'review_readback')

    def test_tool_action_keeps_shape_but_never_review(self):
        self.client.body=body([REASON,MSG,{'type':'function_call','name':'forbidden'}])
        with self.assertRaisesRegex(diag.ShapeIntegrationError,'BLOCKED_UNEXPECTED_PROVIDER_ACTION'):self.invoke()
        self.assertIn('shape_readback',self.events)
        self.assertNotIn('review_persist',self.events)

    def test_replay_rejected_before_second_transport(self):
        self.invoke()
        with self.assertRaises(diag.ShapeIntegrationError):self.invoke()
        self.assertEqual(self.client.calls,1)

    def test_reasoning_payload_not_in_persisted_artifacts(self):
        self.client.body=body([dict(REASON,summary=[{'type':'summary_text','text':'REASON_SECRET_MARKER'}],
                                  encrypted_content='OPAQUE_REASON_MARKER'),MSG])
        out=self.invoke()
        raw=Path(out['shape_path']).read_text()+Path(out['result_path']).read_text()
        for marker in ('REASON_SECRET_MARKER','OPAQUE_REASON_MARKER','synthetic-not-real'):
            self.assertNotIn(marker,raw)

if __name__=='__main__':unittest.main()
