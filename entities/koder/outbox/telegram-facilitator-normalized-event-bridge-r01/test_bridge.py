#!/usr/bin/env python3
"""Локальные синтетические тесты. Python 3.10+, обычный пользователь.
python3 -I -B candidate/test_bridge.py --deps deps
Не создаёт БД, сеть, процессы, файлы или рабочие credentials.
"""
import argparse
import copy
from dataclasses import asdict, replace
import hashlib
import json
import os
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace
import unittest

parser=argparse.ArgumentParser()
parser.add_argument("--deps",type=Path,default=Path(__file__).resolve().parent.parent/"deps")
args=parser.parse_args()
BASE=Path(__file__).resolve().parent
DEPS=args.deps.resolve()
if hasattr(os,"geteuid") and os.geteuid()==0:
    raise SystemExit("BLOCKED_ROOT_EXECUTION")
counters={"network_attempts":0,"process_attempts":0,"write_attempts":0,
          "database_open_attempts":0,"denied_reads":0}
stdlib=Path(os.__file__).resolve().parent
allowed={BASE/"bridge.py",Path(__file__).resolve(),DEPS/"facilitator_core.py",DEPS/"phase1b_gateway.py"}
def audit(event, values):
    if event.startswith("socket."):
        counters["network_attempts"]+=1;raise RuntimeError("NETWORK_DENIED")
    if event.startswith("sqlite3.connect"):
        counters["database_open_attempts"]+=1;raise RuntimeError("DATABASE_DENIED")
    if event.startswith("subprocess.") or event in {"os.system","os.exec","os.fork","os.posix_spawn"}:
        counters["process_attempts"]+=1;raise RuntimeError("PROCESS_DENIED")
    if event in {"os.remove","os.rmdir","os.mkdir","os.rename","os.chmod","os.chown","os.link","os.symlink","os.truncate"}:
        counters["write_attempts"]+=1;raise RuntimeError("WRITE_DENIED")
    if event=="open":
        name,mode,flags=values
        if type(name) is int:return
        if ((type(mode) is str and any(x in mode for x in "wax+")) or
            (type(flags) is int and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))):
            counters["write_attempts"]+=1;raise RuntimeError("WRITE_DENIED")
        path=Path(name).resolve()
        if path not in allowed and not (path.is_relative_to(stdlib) and "site-packages" not in path.parts):
            counters["denied_reads"]+=1;raise RuntimeError("READ_DENIED")
sys.addaudithook(audit)

def load(name,path,expected_sha=None):
    data=path.read_bytes()
    if expected_sha is not None and hashlib.sha256(data).hexdigest()!=expected_sha:
        raise RuntimeError("DEPENDENCY_IDENTITY_MISMATCH")
    module=ModuleType(name);module.__file__=str(path);sys.modules[name]=module
    exec(compile(data,str(path),"exec"),module.__dict__)
    return module

b=load("_bridge_subject",BASE/"bridge.py")
phase=load("_phase1b_exact_producer",DEPS/"phase1b_gateway.py",
           "661300101b34ea52e90094b148319afa97e752c1f51fb980775eab3cdd8a38a9")

def fid(prefix,n):
    return prefix+"_"+format(n,"032x")

def receipt_from_real_method(comments=2,reactions=3,members=None):
    # Реальный неизменённый метод, но источник строки только синтетический.
    row={"publication_id":"pub-fixture-01","distribution_target":"target-fixture-01",
         "delivery_state":"delivered_verified","external_chat_id":-1003330000001,
         "external_message_id":123,"comments_count":comments,
         "reaction_total":reactions,"member_count":members}
    class StubDB:
        def execute(self,query,params):
            assert query.startswith("SELECT d.*,a.comments_count,a.reaction_total,a.member_count")
            assert params==(row["publication_id"],row["distribution_target"])
            return self
        def fetchone(self):return row
    obj=phase.Gateway.__new__(phase.Gateway)
    obj.db=StubDB();obj.config=SimpleNamespace(privacy_mode="aggregate_only")
    return obj.safe_receipt(row["publication_id"],row["distribution_target"])

TASK={"repository":"puev5691/wellbeing-hq",
      "path":"entities/koordinator/outbox/KOO__telegram-facilitator-normalized-event-bridge-r01__KOD.md",
      "commit":"8f79c66715b623ca287430c5b1b4b0d725ec57e5",
      "blob":"d09b1bba42d281b665b646a70747159ba4bf64aa"}
WRITER={"repository":"puev5691/wellbeing-hq",
        "path":"entities/koder/current/KOD__replacement-current-writer-v03.md",
        "commit":"f6686de567b4fa1906ea7cecbc5b5963fcd4e587",
        "blob":"bfeff738de2759248307dd52433c77139624fb54"}

def fixture(data_class="synthetic",comments=2,reactions=3,members=None):
    receipt=receipt_from_real_method(comments,reactions,members)
    synthetic=data_class=="synthetic"
    return {"schema_version":b.SCHEMA,"producer_blob":b.PRODUCER_BLOB,
        "receipt":receipt,"receipt_source_id":fid("source",999),
        "event_context":{"discussion_id":fid("discussion",1),"event_id":fid("event",1),
                         "sequence":1,"at_tick":1},
        "data_class":data_class,
        "policy":{"privacy_class":"synthetic" if synthetic else "minimized_derived",
                  "retention_class":"synthetic_snapshot" if synthetic else "memory_only","expires_tick":100},
        "sources":[{"scope":fid("discussion",1),"source_id":fid("source",999),
                    "version_sha256":b.sha(b.canonical(receipt)),
                    "kind":"synthetic_fixture" if synthetic else "normalized_projection"}],
        "authority":{"requester_id":"KOD","task":copy.deepcopy(TASK),"writer":copy.deepcopy(WRITER),
                     "decision":copy.deepcopy(TASK),"scope":b.SCOPE}}

def approve_exact(obj,**changes):
    expected=b.sha(b.canonical(obj))
    def verifier(check):
        if check.request_sha256!=expected:return None
        grant=b.Grant(expected,b.sha(b.canonical(asdict(check.authority))),
                      check.data_class,0,100,100)
        return replace(grant,**changes)
    return verifier

class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.bridge=b.Bridge(DEPS/"facilitator_core.py")
        self.obj=fixture()
    def convert(self,obj=None,verifier=None):
        obj=self.obj if obj is None else obj
        return self.bridge.convert(b.canonical(obj),approve_exact(obj) if verifier is None else verifier)
    def blocked(self,obj,code=None,verifier=None):
        with self.assertRaises(b.BridgeError) as context:
            self.bridge.convert(b.canonical(obj),approve_exact(obj) if verifier is None else verifier)
        if code:self.assertEqual(str(context.exception),code)
        self.assertNotIn("PRIVATE_SENTINEL",str(context.exception))
    def test_exact_producer_method_and_fields(self):
        self.assertEqual(phase.PRIVACY_POLICY_MARKER,b.POLICY_MARKER)
        self.assertEqual(set(receipt_from_real_method()),b.RECEIPT_FIELDS)
        self.assertEqual(b.git_blob((DEPS/"phase1b_gateway.py").read_bytes()),b.PRODUCER_BLOB)
        self.assertEqual(b.git_blob((DEPS/"facilitator_core.py").read_bytes()),b.CORE_BLOB)
    def test_real_core_normalized_type_and_mapping(self):
        result=self.convert();event=result.event
        self.assertIs(type(event),self.bridge.core.NormalizedEvent)
        self.assertEqual((event.action,event.category),("observe","fact_claim"))
        self.assertIn("комментариев=2",event.derived_text)
        self.assertIn("реакций=3",event.derived_text)
        self.assertIn("member_count=неизвестно",event.derived_text)
        self.assertFalse(event.targets)
        self.assertIsNone(event.disagreement_level)
    def test_null_is_not_zero_and_numeric_zero_preserved(self):
        for members in (None,0,1,b.MAX_COUNT):
            obj=fixture(comments=0,reactions=0,members=members);text=self.convert(obj).event.derived_text
            self.assertIn("комментариев=0",text)
            self.assertIn("member_count="+("неизвестно" if members is None else str(members)),text)
    def test_provenance_preserved_without_technical_id_export(self):
        obj=self.obj
        obj["sources"].append({"scope":fid("discussion",1),"source_id":fid("source",998),
                              "version_sha256":"1"*64,"kind":"synthetic_fixture"})
        result=self.convert(obj)
        self.assertEqual([asdict(x) for x in result.event.sources],obj["sources"])
        serialized=b.canonical(asdict(result)).decode()
        for value in ("-1003330000001","pub-fixture-01","target-fixture-01"):
            self.assertNotIn(value,serialized)
        self.assertEqual(result.receipt_sha256,b.sha(b.canonical(obj["receipt"])))
    def test_caller_authority_retained_separately(self):
        result=self.convert()
        self.assertEqual(asdict(result.authority),self.obj["authority"])
        self.assertFalse(result.dispatch_performed or result.executable_task_created or result.candidate_task_approved)
        self.assertEqual(result.status,"converted_input_not_project_acceptance")
    def test_synthetic_retention_exact(self):
        event=self.convert().event
        self.assertEqual(asdict(event.policy),self.obj["policy"])
    def test_minimized_data_memory_only_and_export_closed(self):
        obj=fixture("phase1b_aggregate_minimized");result=self.convert(obj)
        self.assertEqual(result.event.policy.privacy_class,"minimized_derived")
        self.assertEqual(result.event.policy.retention_class,"memory_only")
        core=self.bridge.core;state=core.apply_event(core.DiscussionState(fid("discussion",1)),result.event)
        with self.assertRaises(core.CoreError):core.snapshot(state)
    def test_default_closed_authority(self):
        with self.assertRaisesRegex(b.BridgeError,"^BLOCKED_BRIDGE_AUTHORITY$"):
            self.bridge.convert(b.canonical(self.obj))
    def test_bad_verifier_values_and_exception(self):
        def broken(_):raise RuntimeError("PRIVATE_SENTINEL")
        for verifier in (lambda _:True,lambda _:1,lambda _:None,broken):
            self.blocked(self.obj,"BLOCKED_BRIDGE_AUTHORITY",verifier)
    def test_grant_bound_to_task_writer_decision_and_all_input(self):
        saved=approve_exact(self.obj)
        for ref in ("task","writer","decision"):
            obj=copy.deepcopy(self.obj);obj["authority"][ref]["blob"]="1"*40
            self.blocked(obj,"BLOCKED_BRIDGE_AUTHORITY",saved)
        obj=copy.deepcopy(self.obj);obj["event_context"]["discussion_id"]=fid("discussion",2)
        obj["sources"][0]["scope"]=fid("discussion",2)
        self.blocked(obj,"BLOCKED_BRIDGE_AUTHORITY",saved)
    def test_grant_forged_digest_authority_class(self):
        for changes in ({"request_sha256":"1"*64},{"authority_sha256":"1"*64},{"data_class":"unknown"}):
            self.blocked(self.obj,"BLOCKED_BRIDGE_AUTHORITY",approve_exact(self.obj,**changes))
    def test_authority_time_bounds(self):
        for changes in ({"not_before_tick":2},{"valid_until_tick":1}):
            self.blocked(self.obj,"BLOCKED_BRIDGE_AUTHORITY_EXPIRED",approve_exact(self.obj,**changes))
        self.blocked(self.obj,"BLOCKED_BRIDGE_AUTHORITY",approve_exact(self.obj,valid_until_tick=True))
    def test_retention_cap_and_expired_input(self):
        self.blocked(self.obj,"BLOCKED_BRIDGE_RETENTION",approve_exact(self.obj,retention_limit_tick=99))
        obj=copy.deepcopy(self.obj);obj["policy"]["expires_tick"]=1
        self.blocked(obj,"BLOCKED_BRIDGE_EXPIRED")
    def test_schema_missing_fields_all_levels(self):
        nested=("receipt","event_context","policy","authority")
        for key in b.TOP_FIELDS:
            obj=copy.deepcopy(self.obj);del obj[key];self.blocked(obj)
        for parent in nested:
            for key in self.obj[parent]:
                obj=copy.deepcopy(self.obj);del obj[parent][key];self.blocked(obj)
        for key in ("repository","path","commit","blob"):
            obj=copy.deepcopy(self.obj);del obj["authority"]["writer"][key];self.blocked(obj)
    def test_unknown_raw_identity_tool_fields_closed(self):
        for field in ("raw_update","raw_text","user_id","username","token","dispatch","approved","execute"):
            for parent in (None,"receipt","authority","policy","event_context"):
                obj=copy.deepcopy(self.obj)
                target=obj if parent is None else obj[parent]
                target[field]="PRIVATE_SENTINEL";self.blocked(obj)
        obj=copy.deepcopy(self.obj);obj["sources"][0]["user_id"]="PRIVATE_SENTINEL";self.blocked(obj)
    def test_unsupported_schema_producer_scope(self):
        obj=copy.deepcopy(self.obj);obj["schema_version"]="future";self.blocked(obj,"BLOCKED_BRIDGE_SCHEMA_VERSION")
        obj=copy.deepcopy(self.obj);obj["producer_blob"]="1"*40;self.blocked(obj,"BLOCKED_BRIDGE_PRODUCER_IDENTITY")
        obj=copy.deepcopy(self.obj);obj["authority"]["scope"]="execute_task";self.blocked(obj,"BLOCKED_BRIDGE_AUTHORITY")
    def test_data_class_unknown_null_list(self):
        for value in ("unknown",None,[],{}):
            obj=copy.deepcopy(self.obj);obj["data_class"]=value;self.blocked(obj,"BLOCKED_BRIDGE_DATA_CLASS")
    def test_privacy_flags_and_mode(self):
        for key in ("personal_data_exported","raw_comment_exported","production_publication"):
            for value in (True,0,None,"false"):
                obj=copy.deepcopy(self.obj);obj["receipt"][key]=value;self.blocked(obj,"BLOCKED_BRIDGE_PRIVACY")
        for key in ("privacy_mode","privacy_policy_marker"):
            obj=copy.deepcopy(self.obj);obj["receipt"][key]="unknown";self.blocked(obj,"BLOCKED_BRIDGE_PRIVACY")
    def test_no_privacy_or_retention_downgrade(self):
        obj=fixture("phase1b_aggregate_minimized");obj["policy"]["privacy_class"]="synthetic"
        self.blocked(obj,"BLOCKED_BRIDGE_PRIVACY")
        obj=fixture("phase1b_aggregate_minimized");obj["policy"]["retention_class"]="synthetic_snapshot"
        self.blocked(obj,"BLOCKED_BRIDGE_RETENTION")
        obj=copy.deepcopy(self.obj);obj["policy"]["retention_class"]="forever"
        self.blocked(obj,"BLOCKED_BRIDGE_RETENTION")
    def test_source_refs_required_and_exact(self):
        variants=([],[None],[dict(self.obj["sources"][0],version_sha256="0"*64)],
                  [dict(self.obj["sources"][0],scope=fid("discussion",2))],
                  [dict(self.obj["sources"][0],kind="raw_telegram")],
                  self.obj["sources"]*2)
        for sources in variants:
            obj=copy.deepcopy(self.obj);obj["sources"]=sources;self.blocked(obj)
        obj=copy.deepcopy(self.obj);obj["receipt_source_id"]=fid("source",123);self.blocked(obj)
    def test_snapshot_mutation_invalidates_source(self):
        obj=copy.deepcopy(self.obj);obj["receipt"]["reaction_total"]=4
        self.blocked(obj,"BLOCKED_BRIDGE_SOURCE_IDENTITY")
    def test_no_missing_or_bool_identity(self):
        for name,value in (("external_chat_id",True),("external_chat_id",0),
                           ("external_message_id",None),("publication_id","../private"),
                           ("distribution_target","PRIVATE_SENTINEL\n")):
            obj=copy.deepcopy(self.obj);obj["receipt"][name]=value
            self.blocked(obj,"BLOCKED_BRIDGE_IDENTITY")
        for name,value in (("sequence",True),("at_tick",-1),("event_id","unknown")):
            obj=copy.deepcopy(self.obj);obj["event_context"][name]=value
            self.blocked(obj,"BLOCKED_BRIDGE_IDENTITY")
    def test_delivery_is_not_authorization(self):
        obj=copy.deepcopy(self.obj);obj["receipt"]["delivery_state"]="delivered_unverified"
        self.blocked(obj,"BLOCKED_BRIDGE_DELIVERY_STATE")
        self.blocked(self.obj,"BLOCKED_BRIDGE_AUTHORITY",lambda _:None)
    def test_bounded_counts_no_coercion(self):
        for name in ("comments_count","reaction_total","member_count"):
            for value in (-1,True,"2",2.5,b.MAX_COUNT+1):
                obj=copy.deepcopy(self.obj);obj["receipt"][name]=value
                self.blocked(obj,"BLOCKED_BRIDGE_COUNTS")
    def test_authority_shape_paths_and_versions(self):
        for change in ({"path":"../credentials"},{"commit":"main"},{"blob":"123"}):
            obj=copy.deepcopy(self.obj);obj["authority"]["task"].update(change)
            self.blocked(obj,"BLOCKED_BRIDGE_IDENTITY")
        obj=copy.deepcopy(self.obj);obj["authority"]["requester_id"]=""
        self.blocked(obj,"BLOCKED_BRIDGE_IDENTITY")
    def test_bad_json_no_echo(self):
        for data in (b"",b" "*16385,b"PRIVATE_SENTINEL",b"\xff",b"[]",b"null",
                     b'{"a":1,"a":2}',b'{"a":NaN}',b'{"a":"\\ud800"}'):
            with self.assertRaises(b.BridgeError) as error:self.bridge.convert(data)
            self.assertNotIn("PRIVATE_SENTINEL",str(error.exception))
    def test_determinism_and_no_input_mutation(self):
        original=b.canonical(self.obj)
        first=self.convert();second=self.convert()
        self.assertEqual(asdict(first),asdict(second))
        self.assertEqual(b.canonical(self.obj),original)
    def test_bridge_never_calls_state_or_dispatch_functions(self):
        def denied(*_,**__):raise AssertionError("CORE_STATE_MUTATION_NOT_ALLOWED")
        self.bridge.core.apply_event=denied
        self.bridge.core.record_decision=denied
        self.bridge.core.synthesize=denied
        result=self.convert();self.assertFalse(result.executable_task_created)
        self.assertFalse(hasattr(self.bridge,"dispatch"))
    def test_aggregate_alone_cannot_create_task_or_agreement(self):
        core=self.bridge.core;event=self.convert().event
        state=core.apply_event(core.DiscussionState(fid("discussion",1)),event)
        state=core.apply_event(state,core.fixture_event(2,action="synthesize"))
        self.assertFalse(state.tasks)
        self.assertEqual(state.summaries[0].group_consensus,"not_established")
        self.assertEqual(state.items[0].epistemic_status,"reported_claim_not_verified_fact")
    def test_downstream_candidate_still_not_executable(self):
        core=self.bridge.core
        events=(core.fixture_event(1,"problem","Синтетическая проблема."),
                core.fixture_event(2,"goal","Синтетический проверяемый результат."),
                core.fixture_event(3,"criterion","Синтетический критерий."))
        state=core.replay(fid("discussion",1),events)
        obj=copy.deepcopy(self.obj);obj["event_context"].update(event_id=fid("event",4),sequence=4,at_tick=4)
        state=core.apply_event(state,self.convert(obj).event)
        state=core.apply_event(state,core.fixture_event(5,action="synthesize"))
        self.assertEqual(len(state.tasks),1)
        task=state.tasks[0]
        self.assertFalse(task.executable or task.approved_for_execution)
        state=core.record_decision(state,core.fixture_decision(state),lambda _:True)
        self.assertEqual(state.tasks[0].status,"candidate_only")
        self.assertFalse(state.tasks[0].executable or state.tasks[0].approved_for_execution)
    def test_source_expiry_and_dedup_in_core(self):
        core=self.bridge.core;event=self.convert().event
        state=core.apply_event(core.DiscussionState(fid("discussion",1)),event)
        self.assertEqual(core.apply_event(state,event),state)
        self.assertFalse(core.expire(state,100).items)
        self.assertEqual(event.policy.expires_tick,100)
    def test_dependency_tamper_before_execution(self):
        class FakeFile:
            def read_bytes(self):return b'raise AssertionError("must_not_execute")'
        with self.assertRaisesRegex(b.BridgeError,"^BLOCKED_BRIDGE_CORE_IDENTITY$"):
            b.load_core(FakeFile())
    def test_operation_guard_counters(self):
        self.assertFalse(any(counters.values()))

if __name__=="__main__":
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BridgeTests))
    good=result.wasSuccessful() and not any(counters.values())
    proof={"verdict":"PASS_TELEGRAM_FACILITATOR_NORMALIZED_EVENT_BRIDGE_R01_READY_FOR_INDEPENDENT_VERIFY" if good else "FAIL_BRIDGE_TESTS",
        "test_methods":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),
        "skipped":len(result.skipped),"operation_counters":counters,"uid":os.geteuid(),
        "live_telegram_calls":0,"live_provider_calls":0,"credentials_read":False,
        "scope":"synthetic producer method with in-memory row stub; no real DB or runtime"}
    print(json.dumps(proof,sort_keys=True))
    raise SystemExit(0 if good else 1)
