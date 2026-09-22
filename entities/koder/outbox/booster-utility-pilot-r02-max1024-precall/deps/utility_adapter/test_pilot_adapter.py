import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import pilot_adapter as a
from build_fixture import fixture

class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.case, raw = fixture()
        self.review = self.root / 'review.json'
        self.review.write_bytes(raw)
        self.card = self.root / 'card.json'

    def kw(self):
        return dict(request=self.case['request'], review_path=self.review,
                    expected_review_sha256=self.case['expected_review_sha256'],
                    observations=self.case['observations'], requester_review=self.case['requester_review'])

    def reject(self, action):
        with self.assertRaises(Exception):
            action()

    def replace_record(self, transform, trust_new_hash=True):
        obj = json.loads(self.review.read_bytes())
        transform(obj)
        raw = a.canonical(obj) + b'\n'
        self.review.write_bytes(raw)
        if trust_new_hash:
            self.case['expected_review_sha256'] = a.digest(raw)

    def test_pair_save_readback(self):
        sha = a.save_card(self.card, **self.kw())
        card = a.read_card(self.card, sha, **{k:v for k,v in self.kw().items() if k not in ('observations','requester_review')})
        self.assertEqual(card['comparison']['active_seconds_saved'], 25)
        self.assertEqual(card['comparison']['cycles_saved'], 1)
        self.assertEqual(card['comparison']['rework_count_saved'], 1)
        self.assertEqual(card['cost_summary']['estimated_cost_usd'], None)
        self.assertEqual(card['status'], 'SYNTHETIC_REVIEW_RECORDED')
        self.assertFalse(card['real_utility_demonstrated'])
        self.assertEqual(card['project_acceptance'], 'NOT_GRANTED')
        self.assertFalse(card['project_state_applied'])
        self.assertEqual(card['provider_calls'], 0)

    def test_deterministic_explicit_mapping(self):
        req = self.case['request']
        p = a.prepare(req)
        self.assertEqual(p, a.prepare(dict(reversed(list(req.items())))))
        self.assertNotEqual(p['identity']['request_sha256'], a.digest(req))
        changed = copy.deepcopy(req)
        changed['purpose'] += ' changed'
        p2 = a.prepare(changed)
        for k in ('request_sha256', 'plan_sha256', 'attempt_key', 'authority_sha256'):
            self.assertNotEqual(p['identity'][k], p2['identity'][k])

    def test_wrong_request_identity(self):
        self.replace_record(lambda r:r.update(request_sha256='0'*64))
        self.reject(lambda:a.make_card(**self.kw()))

    def test_wrong_attempt_identity(self):
        self.replace_record(lambda r:r.update(attempt_key='0'*64))
        self.reject(lambda:a.make_card(**self.kw()))

    def test_other_bindings(self):
        for k, v in [('task_blob','0'*40),('writer_blob','0'*40),('plan_sha256','0'*64),
                     ('authority_sha256','0'*64),('model','other')]:
            with self.subTest(k=k):
                case, raw = fixture()
                self.case = case
                self.review.write_bytes(raw)
                self.replace_record(lambda r:r.update({k:v}))
                self.reject(lambda:a.make_card(**self.kw()))

    def test_review_file_hash(self):
        self.review.write_bytes(self.review.read_bytes()+b' ')
        self.reject(lambda:a.make_card(**self.kw()))

    def test_review_internal_tamper(self):
        self.replace_record(lambda r:r['review_payload'].update(text='forged'))
        self.reject(lambda:a.make_card(**self.kw()))

    def test_pending_review(self):
        self.case['requester_review'] = None
        card = a.make_card(**self.kw())
        self.assertEqual(card['status'], 'PENDING_REQUESTER_REVIEW')
        self.assertIsNone(card['utility_verdict'])
        self.assertIsNone(card['comparison'])

    def test_all_requester_decisions(self):
        for d in ('accept_as_candidate','needs_rework','reject'):
            self.case['requester_review']['decision'] = d
            card = a.make_card(**self.kw())
            self.assertEqual(card['utility_verdict'], 'candidate_only:'+d)
            self.assertEqual(card['project_acceptance'], 'NOT_GRANTED')

    def test_missing_or_wrong_requester_evidence(self):
        original = copy.deepcopy(self.case['requester_review'])
        for k,v in [('entity_id','OTHER'),('reason',''),('evidence',[]),('decision','project_accepted')]:
            self.case['requester_review'] = dict(original, **{k:v})
            self.reject(lambda:a.make_card(**self.kw()))

    def test_unknown_cost_not_zero(self):
        c = a.make_card(**self.kw())
        self.assertIsNone(c['cost_summary']['estimated_cost_usd'])
        self.assertIsNone(c['cost_summary']['billed_cost_usd'])
        self.case['observations']['cost']['usage'] = dict(input_tokens=0, cached_input_tokens=0, output_tokens=0, total_tokens=0)
        self.reject(lambda:a.make_card(**self.kw()))

    def test_card_cannot_promote_unknown_cost_to_zero(self):
        a.save_card(self.card, **self.kw())
        card = json.loads(self.card.read_bytes())
        card['cost_summary']['estimated_cost_usd'] = 0
        self.card.write_bytes(a.canonical(card))
        kw = {k:v for k,v in self.kw().items() if k not in ('observations','requester_review')}
        self.reject(lambda:a.read_card(self.card,a.digest(self.card.read_bytes()),**kw))

    def test_known_synthetic_cost_reuses_estimator(self):
        cost = dict(kind='synthetic_estimate', usage=dict(input_tokens=1000,cached_input_tokens=100,output_tokens=500,total_tokens=1500),
                    price_snapshot=dict(snapshot_id='fixture:arithmetic-only',
                        models={'gpt-5.6-luna': dict(input=2,cached_input=1,output=4)},
                        estimator_scope=dict(max_input_tokens_inclusive=2000,over_limit='BLOCKED_PRICE_RULE_OUT_OF_SCOPE')),
                    evidence=['fixture://utility-r01/synthetic-usage'],provider_latency_ms=20)
        self.case['observations']['cost'] = cost
        card = a.make_card(**self.kw())
        self.assertEqual(card['cost_summary']['estimated_cost_usd'], .0039)
        self.assertIsNone(card['cost_summary']['billed_cost_usd'])
        cost['usage']['cached_input_tokens'] = None
        self.reject(lambda:a.make_card(**self.kw()))

    def test_metric_consistency_and_rubric(self):
        original = copy.deepcopy(self.case['observations'])
        for key,value in [('active_seconds',-1),('elapsed_seconds',1),('cycles',True),('rework_count',1.5),('rework_seconds',float('nan'))]:
            self.case['observations'] = copy.deepcopy(original)
            self.case['observations']['assisted'][key] = value
            self.reject(lambda:a.make_card(**self.kw()))
        self.case['observations'] = copy.deepcopy(original)
        self.case['observations']['assisted']['rubric'] = {'different':True}
        self.reject(lambda:a.make_card(**self.kw()))

    def test_request_privacy_scope_hash_and_forbidden_fields(self):
        original = copy.deepcopy(self.case['request'])
        for key,value in [('privacy_class','project_data'),('tools',['shell']),('source_sha256','0'*64),
                          ('task_blob','0'*40),('writer_blob','0'*40),('max_output_tokens',0),
                          ('live',True),('network',True),('credential','SYNTHETIC_FORBIDDEN'),
                          ('host','localhost'),('deployment',True)]:
            bad = dict(original, **{key:value})
            self.reject(lambda:a.prepare(bad))

    def test_disallowed_outputs_stay_fail_closed(self):
        store = a.dependency('review_result_store')
        identity = a.prepare(self.case['request'])['identity']
        for item in [{'type':'function_call'}, {'type':'unknown'},
                     {'type':'message','role':'system','content':[{'type':'output_text','text':'x'}]},
                     {'type':'message','role':'assistant','content':[{'type':'refusal','text':'x'}]}]:
            with self.subTest(item=item):
                self.reject(lambda:store.normalize_openai_result(body=a.canonical({'model':'gpt-5.6-luna','output':[item]}),
                    **identity,http_status=200,provider_calls=1,retries=0,fallback='none'))
        self.assertNotIn(b'SYNTHETIC_METADATA_NOT_REVIEW',self.review.read_bytes())

    def test_persisted_evidence_unknown_type_rejected(self):
        self.replace_record(lambda r:r['response_evidence']['output'].append({'type':'reasoning'}))
        self.reject(lambda:a.make_card(**self.kw()))

    def test_card_hash_and_semantic_tamper(self):
        sha = a.save_card(self.card, **self.kw())
        kw = {k:v for k,v in self.kw().items() if k not in ('observations','requester_review')}
        original = self.card.read_bytes()
        self.card.write_bytes(original+b' ')
        self.reject(lambda:a.read_card(self.card,sha,**kw))
        card = json.loads(original)
        card['project_acceptance'] = 'GRANTED'
        self.card.write_bytes(a.canonical(card))
        self.reject(lambda:a.read_card(self.card,a.digest(self.card.read_bytes()),**kw))

    def test_injected_readback_failure_cannot_pass(self):
        with patch.object(a,'read_card',side_effect=a.Blocked('INJECTED_READBACK_FAILURE')):
            self.reject(lambda:a.save_card(self.card,**self.kw()))

    def test_dependency_tamper(self):
        with patch.dict(a.PINS, {'review_result_store':'0'*64}):
            self.reject(lambda:a.make_card(**self.kw()))

    def test_duplicate_keys_rejected(self):
        p = self.root / 'duplicate.json'
        p.write_text('{"x":1,"x":2}')
        self.reject(lambda:a.load_json(p))

    def test_cli_only_offline(self):
        import contextlib
        import io
        path = self.root / 'case.json'
        path.write_bytes(a.canonical(self.case))
        args = ['pilot_adapter','--case',str(path),'--review',str(self.review),'--output',str(self.card)]
        with patch('sys.argv',args), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(a.main(),0)
        for option in ('--live','--network','--credential','--host','--deploy'):
            with patch('sys.argv',args+[option]), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as caught:
                    a.main()
                self.assertEqual(caught.exception.code,2)

if __name__ == '__main__':
    unittest.main()
