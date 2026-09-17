#!/usr/bin/env python3
"""Синтетические проверки ядра. Не требует Telegram, сети, ключей или БД."""
from types import ModuleType
import json
import sys
import unittest
import hashlib
from pathlib import Path
from dataclasses import replace, FrozenInstanceError, asdict

import os
require_uid=os.geteuid() if hasattr(os,"geteuid") else None
if require_uid==0:raise SystemExit("BLOCKED_ROOT_EXECUTION")
# Контроль операций, а не заявление о защите от злонамеренного Python-кода.
counters={"network_attempts":0,"process_attempts":0,"write_attempts":0,"denied_reads":0}
allowed={str(Path(__file__).resolve()),str(Path(__file__).with_name("facilitator_core.py").resolve())}
stdlib=Path(os.__file__).resolve().parent
def audit(event,args):
    if event.startswith("socket."):
        counters["network_attempts"]+=1;raise RuntimeError("NETWORK_DENIED")
    if event.startswith("subprocess.") or event in ("os.system","os.exec","os.fork","os.posix_spawn"):
        counters["process_attempts"]+=1;raise RuntimeError("PROCESS_DENIED")
    if event in ("os.remove","os.rmdir","os.mkdir","os.rename","os.chmod","os.chown","os.link","os.symlink","os.truncate"):
        counters["write_attempts"]+=1;raise RuntimeError("WRITE_DENIED")
    if event=="open":
        name,mode,flags=args
        if type(name) is int:return
        if (type(mode) is str and any(x in mode for x in "wax+")) or (type(flags) is int and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND)):
            counters["write_attempts"]+=1;raise RuntimeError("WRITE_DENIED")
        dest=Path(name).resolve()
        if str(dest) not in allowed and not dest.is_relative_to(stdlib):
            counters["denied_reads"]+=1;raise RuntimeError("READ_DENIED")
sys.addaudithook(audit)

path=Path(__file__).with_name("facilitator_core.py")
c=ModuleType("facilitator_test_subject");c.__file__=str(path);sys.modules[c.__name__]=c
exec(compile(path.read_bytes(),str(path),"exec"),c.__dict__)

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.events=c.discussion_fixture()
        self.state=c.replay(c.DEMO_DISCUSSION,self.events)
    def fails(self,code,fn):
        with self.assertRaises(c.CoreError) as cm: fn()
        self.assertEqual(str(cm.exception),code)
    def test_required_types_and_all_categories(self):
        self.assertEqual({i.category for i in self.state.items},c.CATEGORIES)
        self.assertIsInstance(self.events[0],c.NormalizedEvent)
        self.assertIsInstance(self.state,c.DiscussionState)
        self.assertIsInstance(self.state.tasks[0],c.CandidateTask)
        self.assertIsInstance(c.fixture_decision(self.state),c.DecisionRecord)
    def test_deterministic_replay_and_no_wall_clock(self):
        self.assertEqual(c.snapshot(self.state),c.snapshot(c.replay(c.DEMO_DISCUSSION,self.events)))
        self.assertEqual(c.snapshot(self.state),c.snapshot(c.replay(c.DEMO_DISCUSSION,tuple(self.events))))
    def test_json_roundtrip_all_events(self):
        events=tuple(c.normalized_event(c.canonical(asdict(e))) for e in self.events)
        self.assertEqual(events,self.events)
        self.assertEqual(c.replay(c.DEMO_DISCUSSION,events),self.state)
    def test_candidate_task_content(self):
        task=self.state.tasks[0]
        self.assertTrue(task.problem_ids and task.expected_result and task.criterion_ids)
        self.assertTrue(task.option_ids and task.procedure_ids and task.unresolved_question_ids)
        self.assertEqual(task.suggested_recipient,"group_review_not_assigned")
        self.assertEqual(task.status,"candidate_only")
        self.assertFalse(task.executable or task.approved_for_execution)
    def test_claims_never_truth_or_consensus(self):
        for item in self.state.items:
            if item.category=="fact_claim":self.assertEqual(item.epistemic_status,"reported_claim_not_verified_fact")
            if item.category=="preliminary_agreement":self.assertEqual(item.epistemic_status,"reported_preliminary_not_group_consensus")
        self.assertEqual(self.state.summaries[0].group_consensus,"not_established")
        self.assertEqual(json.loads(c.snapshot(self.state))["group_consensus"],"not_established")
    def test_missing_goal_problem_criterion(self):
        events=(c.fixture_event(1,"concept","Нужно уточнить понятие."),c.fixture_event(2,action="synthesize"))
        state=c.replay(c.DEMO_DISCUSSION,events)
        self.assertFalse(state.tasks)
        self.assertEqual(len(state.questions),3)
    def test_summary_and_disagreement_question(self):
        summary=dict(self.state.summaries[0].sections)
        self.assertEqual(len(summary["position"]),2)
        self.assertEqual(len(summary["disagreement"]),1)
        self.assertEqual(len(self.state.questions),2)
        self.assertTrue(any("means" in q.question for q in self.state.questions))
    def test_provenance_complete_scoped(self):
        for candidate in (*self.state.tasks,*self.state.questions,*self.state.summaries):
            self.assertEqual(len(candidate.provenance.event_ids),14)
            self.assertEqual({s.scope for s in candidate.provenance.sources},{c.DEMO_DISCUSSION})
            self.assertTrue(all(c.digest(s.version_sha256) for s in candidate.provenance.sources))
    def test_duplicate_noop_no_ttl_extension(self):
        self.assertEqual(c.apply_event(self.state,self.events[0]),self.state)
        self.assertEqual(c.apply_event(self.state,self.events[-1]),self.state)
    def test_conflicting_event_id(self):
        changed=replace(self.events[0],derived_text="Другая тема.")
        self.fails("BLOCKED_EVENT_ID_CONFLICT",lambda:c.apply_event(self.state,changed))
    def test_out_of_order_event_and_clock(self):
        self.fails("BLOCKED_SEQUENCE",lambda:c.apply_event(c.DiscussionState(c.DEMO_DISCUSSION),self.events[1]))
        e=c.fixture_event(15,"option","Ещё один вариант.")
        self.fails("BLOCKED_TIME_ORDER",lambda:c.apply_event(self.state,replace(e,at_tick=13)))
        self.fails("BLOCKED_TIME_ORDER",lambda:c.expire(self.state,True))
    def test_cross_discussion(self):
        other=c.fixture_event(15,"goal","Другая группа.",scope=c.fixture_id("discussion",2))
        self.fails("BLOCKED_CROSS_DISCUSSION",lambda:c.apply_event(self.state,other))
        self.fails("BLOCKED_CROSS_DISCUSSION",lambda:replace(other,discussion_id=c.DEMO_DISCUSSION))
    def test_retraction_invalidates_derived_and_original_unchanged(self):
        original=c.snapshot(self.state)
        state=c.apply_event(self.state,c.fixture_event(15,action="retract",targets=(c.fixture_id("event",9),)))
        self.assertFalse(state.tasks or state.questions or state.summaries or state.decisions)
        self.assertFalse(any(i.category=="disagreement" for i in state.items))
        self.assertEqual(c.snapshot(self.state),original)
    def test_dangling_and_nested_disagreement(self):
        bad=c.fixture_event(15,"disagreement","Различие.",targets=(c.fixture_id("event",1),c.fixture_id("event",98)),level="facts")
        self.fails("BLOCKED_DANGLING_REFERENCE",lambda:c.apply_event(self.state,bad))
        nested=replace(bad,targets=(c.fixture_id("event",1),c.fixture_id("event",13)))
        self.fails("BLOCKED_NESTED_DISAGREEMENT",lambda:c.apply_event(self.state,nested))
    def test_each_disagreement_level(self):
        for level in c.LEVELS:
            with self.subTest(level=level):
                e=c.fixture_event(15,"disagreement","Явно отмеченное различие.",targets=(c.fixture_id("event",9),c.fixture_id("event",10)),level=level)
                self.assertEqual(c.apply_event(self.state,e).items[-1].disagreement_level,level)
    def test_expiry_pure_projection(self):
        state=c.expire(self.state,100)
        self.assertFalse(state.items or state.tasks or state.questions or state.summaries or state.seen or state.decisions)
        self.assertTrue(self.state.items)
        self.assertNotIn("Участники",c.snapshot(state).decode())
        self.assertEqual(state.last_sequence,14)
        self.fails("BLOCKED_SEQUENCE",lambda:c.apply_event(state,self.events[0]))
    def test_short_lived_source_limits_all_derived(self):
        events=list(self.events);events[0]=replace(events[0],policy=c.RetentionPrivacy("synthetic","synthetic_snapshot",20))
        state=c.replay(c.DEMO_DISCUSSION,events)
        self.assertTrue(all(x.policy.expires_tick==20 for x in (*state.tasks,*state.questions,*state.summaries)))
        self.assertFalse(c.expire(state,20).tasks)
    def test_private_input_forbids_snapshot(self):
        events=list(self.events)
        events[0]=c.fixture_event(1,"topic","Минимизированная синтетическая проекция.",privacy="minimized_derived",retention="memory_only")
        state=c.replay(c.DEMO_DISCUSSION,events)
        self.assertEqual(state.tasks[0].policy.privacy_class,"minimized_derived")
        self.assertEqual(state.tasks[0].policy.retention_class,"memory_only")
        self.fails("BLOCKED_PERSISTENCE_GATE_REQUIRED",lambda:c.snapshot(state))
    def test_no_privacy_downgrade_or_unbounded_retention(self):
        self.fails("BLOCKED_PERSISTENCE_GATE_REQUIRED",lambda:c.RetentionPrivacy("minimized_derived","synthetic_snapshot",100))
        p=c.fixture_event(1,"topic","Проекция.",privacy="minimized_derived",retention="memory_only")
        self.fails("BLOCKED_PRIVACY_DOWNGRADE",lambda:replace(p,policy=c.RetentionPrivacy("synthetic","synthetic_snapshot",100)))
        self.fails("BLOCKED_SCHEMA",lambda:c.RetentionPrivacy("synthetic","forever",100))
        self.fails("BLOCKED_EXPIRED_INPUT",lambda:c.fixture_event(1,"topic","Тема.",expires=1))
    def test_approve_reject_defer_do_not_create_authority(self):
        for action in ("approve","reject","defer"):
            with self.subTest(action=action):
                record=c.fixture_decision(self.state,action)
                state=c.record_decision(self.state,record,lambda d:d==record)
                self.assertEqual(state.decisions[0].action,action)
                self.assertFalse(state.tasks[0].approved_for_execution or state.tasks[0].executable)
                self.assertEqual(state.tasks[0].status,"candidate_only")
                self.assertFalse(state.decisions[0].execution_authority)
                self.assertEqual(state.summaries[0].group_consensus,"not_established")
    def test_default_false_nonbool_and_exception_verifier_denied(self):
        record=c.fixture_decision(self.state)
        def broken(_):raise RuntimeError("SECRET_LIKE_TEST_MARKER")
        for verifier in (None,lambda _:False,lambda _:1,broken):
            with self.subTest(verifier=verifier):
                self.fails("BLOCKED_HUMAN_VERIFICATION_REQUIRED",lambda:c.record_decision(self.state,record,verifier))
    def test_decision_exact_version_and_scope(self):
        record=c.fixture_decision(self.state)
        for bad in (replace(record,target_sha256="0"*64),replace(record,basis_revision=0)):
            self.fails("BLOCKED_STALE_CANDIDATE",lambda:c.record_decision(self.state,bad,lambda _:True))
        self.fails("BLOCKED_SCHEMA",lambda:replace(record,authority_role="model"))
    def test_stale_decision_on_changed_discussion(self):
        record=c.fixture_decision(self.state)
        state=c.apply_event(self.state,c.fixture_event(15,"goal","Другой ожидаемый результат."))
        self.fails("BLOCKED_STALE_CANDIDATE",lambda:c.record_decision(state,record,lambda _:True))
    def test_decision_dedup_and_conflict(self):
        record=c.fixture_decision(self.state)
        state=c.record_decision(self.state,record,lambda _:True)
        self.assertEqual(c.record_decision(state,record),state)
        self.fails("BLOCKED_DECISION_ID_CONFLICT",lambda:c.record_decision(state,replace(record,action="reject"),lambda _:True))
    def test_decision_retention_and_expiry(self):
        record=c.fixture_decision(self.state)
        bad=replace(record,policy=c.RetentionPrivacy("synthetic","synthetic_snapshot",101))
        self.fails("BLOCKED_DECISION_RETENTION",lambda:c.record_decision(self.state,bad,lambda _:True))
        state=c.record_decision(self.state,record,lambda _:True)
        self.assertFalse(c.expire(state,100).decisions)
    def test_frozen_objects(self):
        with self.assertRaises(FrozenInstanceError):self.state.tasks[0].executable=True
        with self.assertRaises(FrozenInstanceError):self.state.items[0].derived_text="changed"
    def test_json_unknown_raw_identity_and_authority_fields(self):
        for field in ("raw_text","raw_update","user_id","username","token","approved","execute","group_consensus"):
            with self.subTest(field=field):
                obj=asdict(self.events[0]);obj[field]="SECRET_LIKE_TEST_MARKER"
                self.fails("BLOCKED_SCHEMA",lambda:c.normalized_event(c.canonical(obj)))
        obj=asdict(self.events[0]);obj["sources"][0]["user_id"]=123
        self.fails("BLOCKED_SCHEMA",lambda:c.normalized_event(c.canonical(obj)))
    def test_bad_json_does_not_leak_input(self):
        for payload in (b"invalid SECRET_LIKE_TEST_MARKER",b"null",b"[]",b"\xff",b'{"a":1,"a":2}',b'{"a":NaN}'):
            with self.subTest(payload=payload):
                with self.assertRaises(c.CoreError) as cm:c.normalized_event(payload)
                self.assertNotIn("SECRET_LIKE_TEST_MARKER",str(cm.exception))
        self.fails("BLOCKED_INPUT_SIZE",lambda:c.normalized_event(b" "*8193))
    def test_bad_scalar_and_unicode_input(self):
        for key,value in (("sequence",True),("at_tick",-1),("category","execute"),("derived_text",""),("derived_text","x"*513),
                          ("derived_text","\ud800"),("derived_text","bad\ntext"),("discussion_id","username_test")):
            with self.subTest(key=key):
                with self.assertRaises(c.CoreError):replace(self.events[0],**{key:value})
    def test_empty_synthesis_and_capacity(self):
        self.fails("BLOCKED_INSUFFICIENT_DISCUSSION",lambda:c.apply_event(c.DiscussionState(c.DEMO_DISCUSSION),c.fixture_event(1,action="synthesize")))
        state=c.DiscussionState(c.DEMO_DISCUSSION)
        for number in range(1,c.MAX_ITEMS+1):
            state=c.apply_event(state,c.fixture_event(number,"fact_claim","Синтетическое утверждение.",expires=1000))
        self.fails("BLOCKED_CAPACITY",lambda:c.apply_event(state,c.fixture_event(129,"fact_claim","Лишнее.",expires=1000)))
    def test_replay_properties_across_40_sequences(self):
        for length in range(1,41):
            with self.subTest(length=length):
                events=tuple(c.fixture_event(n,"position","Синтетическая позиция.",expires=200) for n in range(1,length+1))
                state=c.replay(c.DEMO_DISCUSSION,events)
                state2=c.replay(c.DEMO_DISCUSSION,events+events)
                self.assertEqual(c.snapshot(state),c.snapshot(state2))
                self.assertEqual(len(state.items),length)
                self.assertFalse(state.tasks or state.decisions)

if __name__=="__main__":
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(CoreTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    proof={"verdict":c.PASS if result.wasSuccessful() else "FAIL_TELEGRAM_FACILITATOR_CORE_R01_TESTS",
           "tests_run":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),
           "skipped":len(result.skipped),"operation_counters":counters,"uid":require_uid,
           "api_calls":0,"credentials_read":False,"independent_review":"pending"}
    print(json.dumps(proof,ensure_ascii=False,sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() and not any(counters.values()) else 1)
