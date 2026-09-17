#!/usr/bin/env python3
"""Изолированное ядро обсуждений r0.1. Python 3.10+, только стандартная библиотека.

python3 -I -B facilitator_core.py --self-test
python3 -I -B facilitator_core.py --demo

Вход уже нормализован и минимизирован внешним privacy gate. Здесь нет NLP,
Telegram, провайдера, хранилища, часов, сети, публикации или диспетчера задач.
Типы NormalizedEvent/DiscussionState/CandidateTask/DecisionRecord являются
машинным контрактом normalized_event/discussion_state/candidate_task/decision_record.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict, replace
from typing import Callable
import hashlib
import json
import re

VERSION = "facilitator-r01"
PASS = "PASS_TELEGRAM_FACILITATOR_CORE_R01_READY_FOR_INDEPENDENT_VERIFY"
CATEGORIES = frozenset({"topic", "problem", "concept", "fact_claim", "goal", "criterion",
    "option", "procedure", "position", "preliminary_agreement", "open_question", "disagreement"})
LEVELS = frozenset({"facts", "concepts", "goals", "criteria", "means", "procedure", "other"})
MAX_ITEMS = 128
MAX_SEEN = 512
MAX_DECISIONS = 64
MAX_TEXT = 512

class CoreError(ValueError):
    """Только фиксированный код: отклонённый payload не попадает в диагностику."""

def require(ok, code="BLOCKED_SCHEMA"):
    if not ok:
        raise CoreError(code)

def integer(value):
    return type(value) is int and 0 <= value <= 2**53-1

def token(value, prefix):
    return type(value) is str and re.fullmatch(prefix + r"_[0-9a-f]{32}", value) is not None

def digest(value):
    return type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None

def text(value):
    if type(value) is not str or not value.strip():
        return False
    try:
        return len(value.encode("utf-8")) <= MAX_TEXT and all(ord(c) >= 32 for c in value)
    except UnicodeError:
        return False

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")

def fingerprint(value):
    return hashlib.sha256(canonical(asdict(value))).hexdigest()

@dataclass(frozen=True)
class SourceRef:
    scope: str
    source_id: str
    version_sha256: str
    kind: str
    def __post_init__(self):
        require(token(self.scope,"discussion") and token(self.source_id,"source")
                and digest(self.version_sha256)
                and self.kind in ("synthetic_fixture","normalized_projection"))

@dataclass(frozen=True)
class RetentionPrivacy:
    privacy_class: str
    retention_class: str
    expires_tick: int
    def __post_init__(self):
        require(type(self.privacy_class) is str and self.privacy_class in ("synthetic","minimized_derived"))
        require(type(self.retention_class) is str and self.retention_class in ("memory_only","synthetic_snapshot"))
        require(integer(self.expires_tick))
        require(self.privacy_class == "synthetic" or self.retention_class == "memory_only",
                "BLOCKED_PERSISTENCE_GATE_REQUIRED")

@dataclass(frozen=True)
class Provenance:
    sources: tuple[SourceRef, ...]
    event_ids: tuple[str, ...]
    rule: str
    def __post_init__(self):
        require(type(self.sources) is tuple and 1 <= len(self.sources) <= MAX_SEEN)
        require(all(type(x) is SourceRef for x in self.sources))
        require(len(set(self.sources)) == len(self.sources))
        require(len({x.scope for x in self.sources}) == 1, "BLOCKED_CROSS_DISCUSSION")
        require(type(self.event_ids) is tuple and 1 <= len(self.event_ids) <= MAX_SEEN)
        require(all(token(x,"event") for x in self.event_ids) and len(set(self.event_ids)) == len(self.event_ids))
        require(self.rule in ("normalized_input", "synthesis_r01", "explicit_human_gate"))

@dataclass(frozen=True)
class NormalizedEvent:
    discussion_id: str
    event_id: str
    sequence: int
    at_tick: int
    action: str
    category: str | None
    derived_text: str | None = field(repr=False)
    targets: tuple[str, ...]
    disagreement_level: str | None
    sources: tuple[SourceRef, ...]
    policy: RetentionPrivacy
    def __post_init__(self):
        require(token(self.discussion_id,"discussion") and token(self.event_id,"event"))
        require(integer(self.sequence) and self.sequence > 0 and integer(self.at_tick))
        require(type(self.policy) is RetentionPrivacy and self.policy.expires_tick > self.at_tick,
                "BLOCKED_EXPIRED_INPUT")
        require(type(self.action) is str and self.action in ("observe","synthesize","retract"))
        Provenance(self.sources,(self.event_id,),"normalized_input")
        require(all(s.scope == self.discussion_id for s in self.sources),"BLOCKED_CROSS_DISCUSSION")
        if self.policy.privacy_class == "synthetic":
            require(all(s.kind == "synthetic_fixture" for s in self.sources),"BLOCKED_PRIVACY_DOWNGRADE")
        require(type(self.targets) is tuple and len(self.targets) <= MAX_ITEMS)
        require(all(token(x,"event") for x in self.targets) and len(set(self.targets)) == len(self.targets))
        if self.action == "observe":
            require(type(self.category) is str and self.category in CATEGORIES and text(self.derived_text))
            if self.category == "disagreement":
                require(type(self.disagreement_level) is str and self.disagreement_level in LEVELS
                        and len(self.targets) >= 2,"BLOCKED_DISAGREEMENT_SHAPE")
            else:
                require(self.disagreement_level is None and not self.targets)
        else:
            require(self.category is None and self.derived_text is None and self.disagreement_level is None)
            require(len(self.targets) == (1 if self.action == "retract" else 0))

@dataclass(frozen=True)
class DiscussionItem:
    item_id: str
    category: str
    derived_text: str = field(repr=False)
    targets: tuple[str, ...]
    disagreement_level: str | None
    provenance: Provenance
    policy: RetentionPrivacy
    @property
    def epistemic_status(self):
        if self.category == "fact_claim": return "reported_claim_not_verified_fact"
        if self.category == "preliminary_agreement": return "reported_preliminary_not_group_consensus"
        return "reported_or_proposed_not_decided"

@dataclass(frozen=True)
class CandidateQuestion:
    candidate_id: str
    basis_revision: int
    question: str = field(repr=False)
    basis_ids: tuple[str, ...]
    provenance: Provenance
    policy: RetentionPrivacy
    status: str = field(default="candidate_only", init=False)
    executable: bool = field(default=False, init=False)

@dataclass(frozen=True)
class CandidateSummary:
    candidate_id: str
    basis_revision: int
    sections: tuple[tuple[str, tuple[str, ...]], ...]
    provenance: Provenance
    policy: RetentionPrivacy
    status: str = field(default="candidate_only", init=False)
    group_consensus: str = field(default="not_established", init=False)
    executable: bool = field(default=False, init=False)

@dataclass(frozen=True)
class CandidateTask:
    candidate_id: str
    basis_revision: int
    problem_ids: tuple[str, ...]
    title: str = field(repr=False)
    basis_ids: tuple[str, ...]
    expected_result: str = field(repr=False)
    criterion_ids: tuple[str, ...]
    option_ids: tuple[str, ...]
    procedure_ids: tuple[str, ...]
    unresolved_question_ids: tuple[str, ...]
    provenance: Provenance
    policy: RetentionPrivacy
    suggested_recipient: str = field(default="group_review_not_assigned", init=False)
    status: str = field(default="candidate_only", init=False)
    executable: bool = field(default=False, init=False)
    approved_for_execution: bool = field(default=False, init=False)

@dataclass(frozen=True)
class DecisionRecord:
    decision_id: str
    target_id: str
    target_sha256: str
    basis_revision: int
    at_tick: int
    action: str
    authority_role: str
    verification_ref: SourceRef
    provenance: Provenance
    policy: RetentionPrivacy
    scope: str = field(default="candidate_review_only", init=False)
    execution_authority: bool = field(default=False, init=False)
    def __post_init__(self):
        require(token(self.decision_id,"decision") and token(self.target_id,"candidate")
                and digest(self.target_sha256) and integer(self.basis_revision) and integer(self.at_tick))
        require(type(self.action) is str and self.action in ("approve","reject","defer"))
        require(type(self.authority_role) is str and self.authority_role in ("moderator","operator"))
        require(type(self.verification_ref) is SourceRef and type(self.provenance) is Provenance
                and self.provenance.rule == "explicit_human_gate" and type(self.policy) is RetentionPrivacy)
        require(self.policy.expires_tick > self.at_tick,"BLOCKED_EXPIRED_INPUT")
        require(self.verification_ref in self.provenance.sources,"BLOCKED_MISSING_DECISION_PROVENANCE")
        if self.policy.privacy_class == "synthetic":
            require(all(s.kind == "synthetic_fixture" for s in self.provenance.sources),"BLOCKED_PRIVACY_DOWNGRADE")

@dataclass(frozen=True)
class SeenEvent:
    event_id: str
    fingerprint: str
    policy: RetentionPrivacy

@dataclass(frozen=True)
class DiscussionState:
    discussion_id: str
    logical_tick: int = 0
    last_sequence: int = 0
    revision: int = 0
    items: tuple[DiscussionItem, ...] = ()
    questions: tuple[CandidateQuestion, ...] = ()
    summaries: tuple[CandidateSummary, ...] = ()
    tasks: tuple[CandidateTask, ...] = ()
    decisions: tuple[DecisionRecord, ...] = ()
    seen: tuple[SeenEvent, ...] = ()
    def __post_init__(self):
        require(token(self.discussion_id,"discussion"))
        require(all(integer(x) for x in (self.logical_tick,self.last_sequence,self.revision)))
        for value,cls in ((self.items,DiscussionItem),(self.questions,CandidateQuestion),
                          (self.summaries,CandidateSummary),(self.tasks,CandidateTask),
                          (self.decisions,DecisionRecord),(self.seen,SeenEvent)):
            require(type(value) is tuple and all(type(x) is cls for x in value))
        require(len(self.items) <= MAX_ITEMS and len(self.seen) <= MAX_SEEN
                and len(self.decisions) <= MAX_DECISIONS,"BLOCKED_CAPACITY")

# Не импортировать произвольные JSON snapshot как доверенное состояние.
# Состояние создаётся пустым и воспроизводится только через проверенные переходы.
def normalized_event(data: bytes) -> NormalizedEvent:
    require(type(data) is bytes and len(data) <= 8192,"BLOCKED_INPUT_SIZE")
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result,"BLOCKED_DUPLICATE_KEY")
            result[k]=v
        return result
    try:
        obj=json.loads(data.decode("utf-8"),object_pairs_hook=pairs,
                       parse_constant=lambda _: (_ for _ in ()).throw(CoreError("BLOCKED_SCHEMA")))
        require(type(obj) is dict and set(obj) == {
            "discussion_id","event_id","sequence","at_tick","action","category","derived_text",
            "targets","disagreement_level","sources","policy"})
        require(type(obj["sources"]) is list and type(obj["targets"]) is list and type(obj["policy"]) is dict)
        require(set(obj["policy"]) == {"privacy_class","retention_class","expires_tick"})
        sources=[]
        for source in obj["sources"]:
            require(type(source) is dict and set(source)=={"scope","source_id","version_sha256","kind"})
            sources.append(SourceRef(**source))
        obj["sources"]=tuple(sources);obj["targets"]=tuple(obj["targets"])
        obj["policy"]=RetentionPrivacy(**obj["policy"])
        return NormalizedEvent(**obj)
    except CoreError:
        raise
    except (TypeError,ValueError,KeyError,UnicodeError,RecursionError):
        raise CoreError("BLOCKED_SCHEMA") from None

def combine_policy(policies):
    values=tuple(policies);require(bool(values))
    privacy="minimized_derived" if any(p.privacy_class == "minimized_derived" for p in values) else "synthetic"
    retention="synthetic_snapshot" if all(p.retention_class == "synthetic_snapshot" for p in values) else "memory_only"
    return RetentionPrivacy(privacy,retention,min(p.expires_tick for p in values))

def provenance(items, event):
    sources=set(event.sources);event_ids={event.event_id}
    for item in items:
        sources.update(item.provenance.sources);event_ids.update(item.provenance.event_ids)
    return Provenance(tuple(sorted(sources,key=lambda s:canonical(asdict(s)))),tuple(sorted(event_ids)),"synthesis_r01")

def candidate_id(kind, state, prov):
    b=canonical({"rule":VERSION,"kind":kind,"discussion":state.discussion_id,
                 "revision":state.revision,"sources":asdict(prov)})
    return "candidate_"+hashlib.sha256(b).hexdigest()[:32]

def expire(state: DiscussionState, tick: int) -> DiscussionState:
    """Чистая новая проекция; не удаляет файлы, не перезаписывает переданный объект."""
    require(type(state) is DiscussionState and integer(tick) and tick >= state.logical_tick,"BLOCKED_TIME_ORDER")
    items=tuple(i for i in state.items if i.policy.expires_tick > tick)
    live={i.item_id for i in items}
    items=tuple(i for i in items if not i.targets or set(i.targets) <= live)
    changed=items != state.items
    questions=() if changed else tuple(c for c in state.questions if c.policy.expires_tick > tick)
    summaries=() if changed else tuple(c for c in state.summaries if c.policy.expires_tick > tick)
    tasks=() if changed else tuple(c for c in state.tasks if c.policy.expires_tick > tick)
    targets={c.candidate_id for c in (*questions,*summaries,*tasks)}
    return replace(state,logical_tick=tick,revision=state.revision+int(changed),items=items,
        questions=questions,summaries=summaries,tasks=tasks,
        decisions=tuple(d for d in state.decisions if d.policy.expires_tick > tick and d.target_id in targets),
        seen=tuple(s for s in state.seen if s.policy.expires_tick > tick))

def synthesize(state,event):
    require(bool(state.items),"BLOCKED_INSUFFICIENT_DISCUSSION")
    prov=provenance(state.items,event)
    policy=combine_policy([event.policy,*[i.policy for i in state.items]])
    by={k:tuple(i.item_id for i in state.items if i.category==k) for k in sorted(CATEGORIES)}
    question_specs=[]
    for item in state.items:
        if item.category == "open_question": question_specs.append((item.derived_text,(item.item_id,)))
        if item.category == "disagreement":
            question_specs.append(("Какие данные или критерии нужны для рассмотрения разногласия уровня "+item.disagreement_level+"?",(item.item_id,*item.targets)))
    if not by["problem"]: question_specs.append(("Какую проблему требуется решить?",tuple(i.item_id for i in state.items)))
    if not by["goal"]: question_specs.append(("Какой результат требуется получить?",tuple(i.item_id for i in state.items)))
    if not by["criterion"]: question_specs.append(("По какому критерию проверить результат?",tuple(i.item_id for i in state.items)))
    questions=tuple(CandidateQuestion(candidate_id("question:"+str(n),state,prov),state.revision,q,b,prov,policy)
                    for n,(q,b) in enumerate(question_specs))
    summary=CandidateSummary(candidate_id("summary",state,prov),state.revision,tuple(by.items()),prov,policy)
    tasks=()
    if by["problem"] and by["goal"]:
        first_problem=next(i for i in state.items if i.category=="problem")
        first_goal=next(i for i in state.items if i.category=="goal")
        tasks=(CandidateTask(candidate_id("task",state,prov),state.revision,by["problem"],
            "Рассмотреть: "+first_problem.derived_text,tuple(i.item_id for i in state.items),
            first_goal.derived_text,by["criterion"],by["option"],by["procedure"],
            tuple(q.candidate_id for q in questions),prov,policy),)
    return replace(state,questions=questions,summaries=(summary,),tasks=tasks,decisions=())

def apply_event(state: DiscussionState, event: NormalizedEvent) -> DiscussionState:
    require(type(state) is DiscussionState and type(event) is NormalizedEvent)
    require(state.discussion_id == event.discussion_id,"BLOCKED_CROSS_DISCUSSION")
    fp=fingerprint(event)
    previous=next((s for s in state.seen if s.event_id==event.event_id),None)
    if previous is not None:
        require(previous.fingerprint==fp,"BLOCKED_EVENT_ID_CONFLICT")
        return state  # Идемпотентный повтор не продлевает срок хранения.
    require(event.sequence == state.last_sequence+1,"BLOCKED_SEQUENCE")
    state=expire(state,event.at_tick)
    require(len(state.seen)<MAX_SEEN,"BLOCKED_CAPACITY")
    if event.action == "observe":
        require(len(state.items)<MAX_ITEMS,"BLOCKED_CAPACITY")
        current={i.item_id:i for i in state.items}
        require(all(t in current for t in event.targets),"BLOCKED_DANGLING_REFERENCE")
        if event.category == "disagreement":
            require(all(current[t].category!="disagreement" for t in event.targets),"BLOCKED_NESTED_DISAGREEMENT")
        pol=combine_policy([event.policy,*[current[t].policy for t in event.targets]])
        item=DiscussionItem(event.event_id,event.category,event.derived_text,event.targets,event.disagreement_level,
            provenance(tuple(current[t] for t in event.targets),event) if event.targets else
            Provenance(event.sources,(event.event_id,),"normalized_input"),pol)
        state=replace(state,items=(*state.items,item),revision=state.revision+1,
                      questions=(),summaries=(),tasks=(),decisions=())
    elif event.action == "retract":
        target=event.targets[0]
        require(any(i.item_id==target for i in state.items),"BLOCKED_DANGLING_REFERENCE")
        remaining=tuple(i for i in state.items if i.item_id!=target and target not in i.targets)
        state=replace(state,items=remaining,revision=state.revision+1,questions=(),summaries=(),tasks=(),decisions=())
    else:
        state=synthesize(state,event)
    return replace(state,last_sequence=event.sequence,
                   seen=(*state.seen,SeenEvent(event.event_id,fp,event.policy)))

def record_decision(state: DiscussionState, record: DecisionRecord,
                    verifier: Callable[[DecisionRecord],bool] | None = None) -> DiscussionState:
    """Внешняя доверенная проверка человеческого решения обязательна. Не исполнитель."""
    require(type(state) is DiscussionState and type(record) is DecisionRecord)
    require(all(s.scope==state.discussion_id for s in record.provenance.sources),"BLOCKED_CROSS_DISCUSSION")
    old=next((d for d in state.decisions if d.decision_id==record.decision_id),None)
    if old is not None:
        require(old==record,"BLOCKED_DECISION_ID_CONFLICT")
        return state
    state=expire(state,record.at_tick)
    candidates=(*state.questions,*state.summaries,*state.tasks)
    target=next((c for c in candidates if c.candidate_id==record.target_id),None)
    require(target is not None,"BLOCKED_STALE_CANDIDATE")
    require(record.basis_revision==state.revision==target.basis_revision
            and record.target_sha256==fingerprint(target),"BLOCKED_STALE_CANDIDATE")
    require(combine_policy([record.policy,target.policy])==record.policy,"BLOCKED_DECISION_RETENTION")
    require(len(state.decisions)<MAX_DECISIONS,"BLOCKED_CAPACITY")
    require(callable(verifier),"BLOCKED_HUMAN_VERIFICATION_REQUIRED")
    try:
        verified=verifier(record)
    except Exception:
        raise CoreError("BLOCKED_HUMAN_VERIFICATION_REQUIRED") from None
    require(verified is True,"BLOCKED_HUMAN_VERIFICATION_REQUIRED")
    return replace(state,decisions=(*state.decisions,record))

def snapshot(state: DiscussionState) -> bytes:
    """Только явный экспорт синтетической проекции; сама функция ничего не записывает."""
    require(type(state) is DiscussionState)
    all_objects=(*state.items,*state.questions,*state.summaries,*state.tasks,*state.decisions,*state.seen)
    require(all(x.policy.privacy_class=="synthetic" and x.policy.retention_class=="synthetic_snapshot"
                for x in all_objects),"BLOCKED_PERSISTENCE_GATE_REQUIRED")
    data=asdict(state)
    for item,data_item in zip(state.items,data["items"]):
        data_item["epistemic_status"]=item.epistemic_status
    return canonical({"schema_version":VERSION,"authority":"candidate_only",
                      "group_consensus":"not_established","discussion_state":data})

def replay(discussion_id, events):
    state=DiscussionState(discussion_id)
    for event in events: state=apply_event(state,event)
    return state

# Синтетические данные. Идентификаторы не выведены из Telegram audience identity.
def fixture_id(prefix,number): return prefix+"_"+format(number,"032x")
DEMO_DISCUSSION=fixture_id("discussion",1)

def fixture_event(number,category=None,derived_text=None,*,action="observe",targets=(),level=None,
                  privacy="synthetic",retention="synthetic_snapshot",expires=100,scope=DEMO_DISCUSSION):
    source=SourceRef(scope,fixture_id("source",number),hashlib.sha256(("fixture:"+str(number)).encode()).hexdigest(),
                     "synthetic_fixture" if privacy=="synthetic" else "normalized_projection")
    return NormalizedEvent(scope,fixture_id("event",number),number,number,action,category,derived_text,
        targets,level,(source,),RetentionPrivacy(privacy,retention,expires))

def discussion_fixture():
    content=[("topic","Порядок использования общего инструмента."),
        ("problem","Участники не знают, свободен ли общий инструмент."),
        ("concept","Нужно уточнить, что считается завершённым использованием."),
        ("fact_claim","Сообщается о двух накладках; подтверждение ещё требуется."),
        ("goal","Подготовить проверяемое предложение по учёту занятости."),
        ("criterion","В пробном сценарии два одновременных запроса различаются."),
        ("option","Рассмотреть общую карточку состояния."),
        ("procedure","Сначала согласовать критерий и затем проверить макет."),
        ("position","Предложена ручная отметка занятости."),
        ("position","Предложена предварительная заявка на использование."),
        ("preliminary_agreement","Сообщено о предварительном интересе; согласие группы не установлено."),
        ("open_question","Кто проверит результат пробного сценария?")]
    events=[fixture_event(n,c,t) for n,(c,t) in enumerate(content,1)]
    events.append(fixture_event(13,"disagreement","Различаются способы учёта занятости.",
        targets=(fixture_id("event",9),fixture_id("event",10)),level="means"))
    events.append(fixture_event(14,action="synthesize"))
    return tuple(events)

def fixture_decision(state,action="approve",number=1):
    target=state.tasks[0];source=SourceRef(state.discussion_id,fixture_id("source",100+number),
        hashlib.sha256(("synthetic-decision:"+str(number)).encode()).hexdigest(),"synthetic_fixture")
    return DecisionRecord(fixture_id("decision",number),target.candidate_id,fingerprint(target),state.revision,
        state.logical_tick+number,action,"moderator",source,
        Provenance((source,),(fixture_id("event",100+number),),"explicit_human_gate"),target.policy)

if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["--demo"]:
        print(snapshot(replay(DEMO_DISCUSSION,discussion_fixture())).decode())
    elif sys.argv[1:] == ["--self-test"]:
        from pathlib import Path
        import runpy
        runpy.run_path(str(Path(__file__).with_name("test_facilitator.py")),run_name="__main__")
    else:
        print(__doc__)
