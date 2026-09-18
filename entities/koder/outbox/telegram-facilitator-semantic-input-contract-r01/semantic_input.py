#!/usr/bin/env python3
"""Локальная библиотека смыслового входа r0.1. Python 3.10+, обычный пользователь.
Только явно допущенная минимизированная проекция, не Telegram/NLP/LLM/хранилище.
Проверка: python3 -I -B candidate/test_semantic.py --core deps/facilitator_core.py
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from pathlib import Path
from types import ModuleType
from typing import Callable
import hashlib
import json
import re
import sys

SCHEMA = "semantic-input-r01"
PURPOSE = "discussion_facilitation"
SCOPE = "semantic_input_to_observe_only"
PASS = "PASS_TELEGRAM_FACILITATOR_SEMANTIC_INPUT_CONTRACT_R01_READY_FOR_INDEPENDENT_VERIFY"
CORE_BLOB = "ad980b0de8a00c1d134823cebc49059a0811f3fa"
CORE_SHA256 = "33f280e9cc56534996d0706de7e3605c0247ff1af8b71ea985fdd7613d47b64a"
MAX_INPUT = 16384
MAX_TEXT = 512
MAX_TICK = 2**53-1
CATEGORIES = frozenset({"topic","problem","concept","fact_claim","goal","criterion","option",
    "procedure","position","preliminary_agreement","open_question","disagreement"})
LEVELS = frozenset({"facts","concepts","goals","criteria","means","procedure","other"})

class SemanticError(ValueError):
    """Фиксированный код, без копирования отвергнутого содержимого."""

def require(ok, code="BLOCKED_SEMANTIC_SCHEMA"):
    if not ok:
        raise SemanticError(code)

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",",":"), allow_nan=False).encode("utf-8")

def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()

def git_blob(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def matches(value, pattern):
    return type(value) is str and re.fullmatch(pattern,value) is not None

def ident(value, prefix):
    return matches(value,prefix+r"_[0-9a-f]{32}")

def tick(value):
    return type(value) is int and 0 <= value <= MAX_TICK

def closed(value, names):
    require(type(value) is dict and set(value)==set(names))

def bounded_text(value, limit):
    require(type(value) is str and bool(value.strip()) and
            len(value.encode("utf-8")) <= limit and all(ord(c)>=32 for c in value),
            "BLOCKED_SEMANTIC_TEXT")

@dataclass(frozen=True, slots=True)
class ArtifactRef:
    repository: str
    path: str
    commit: str
    blob: str

@dataclass(frozen=True, slots=True)
class Policy:
    privacy_class: str
    retention_class: str
    expires_tick: int

@dataclass(frozen=True, slots=True)
class Source:
    scope: str
    source_id: str
    version_sha256: str
    kind: str
    policy: Policy

@dataclass(frozen=True, slots=True)
class ParticipantRef:
    scope: str
    pseudonym: str
    expires_tick: int
    scheme: str

@dataclass(frozen=True, slots=True)
class Content:
    kind: str
    text: str | None = field(repr=False)
    claim: tuple[str,str,str] | None = field(repr=False)
    def render(self):
        return self.text if self.kind=="excerpt" else " | ".join(self.claim)
    def projection(self):
        if self.kind=="excerpt":
            return {"kind":"excerpt","text":self.text}
        return {"kind":"claim","subject":self.claim[0],
                "predicate":self.claim[1],"object":self.claim[2]}

@dataclass(frozen=True, slots=True)
class EventScope:
    discussion_id: str
    event_id: str
    sequence: int
    at_tick: int

@dataclass(frozen=True, slots=True)
class AnalysisPolicy:
    mode: str
    source: ArtifactRef
    allowed_categories: tuple[str,...]
    max_text_bytes: int
    allow_participant: bool

@dataclass(frozen=True, slots=True)
class Authority:
    requester_id: str
    task: ArtifactRef
    writer: ArtifactRef
    privacy_gate: ArtifactRef
    scope: str

@dataclass(frozen=True, slots=True)
class SemanticInput:
    schema_version: str
    input_id: str
    content_class: str
    purpose: str
    scope: EventScope
    content: Content = field(repr=False)
    category: str
    targets: tuple[str,...]
    disagreement_level: str | None
    participant: ParticipantRef | None = field(repr=False)
    content_source_id: str
    sources: tuple[Source,...]
    policy: Policy
    analysis_policy: AnalysisPolicy
    authority: Authority
    @property
    def identity(self):
        return digest(asdict(self))

@dataclass(frozen=True, slots=True)
class AdmissionCheck:
    input_sha256: str
    authority: Authority
    analysis_sha256: str
    content_sha256: str
    sources_sha256: str
    participant_sha256: str
    discussion_id: str
    purpose: str
    category: str
    content_class: str
    effective_policy: Policy

@dataclass(frozen=True, slots=True)
class AdmissionProof:
    check_sha256: str
    source: ArtifactRef
    valid_from_tick: int
    valid_until_tick: int
    retention_limit_tick: int
    minimization_confirmed: bool
    participant_scoped_confirmed: bool
    scope: str

@dataclass(frozen=True, slots=True)
class SemanticResult:
    event: object = field(repr=False)
    input_sha256: str
    check_sha256: str
    admission_sha256: str
    authority: Authority
    proof_source: ArtifactRef
    analysis_policy: AnalysisPolicy
    input_content_class: str
    normalized_event_sha256: str
    status: str = field(default="admitted_input_not_accepted_decision",init=False)
    project_acceptance: str = field(default="NOT_GRANTED",init=False)
    dispatch_performed: bool = field(default=False,init=False)
    executable_task_created: bool = field(default=False,init=False)
    def redacted(self):
        return {"input_sha256":self.input_sha256,"check_sha256":self.check_sha256,
                "admission_sha256":self.admission_sha256,
                "normalized_event_sha256":self.normalized_event_sha256,
                "status":self.status,"project_acceptance":self.project_acceptance,
                "dispatch_performed":False,"executable_task_created":False}

def artifact(obj):
    closed(obj,{"repository","path","commit","blob"})
    require(matches(obj["repository"],r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+") and
            matches(obj["path"],r"[A-Za-z0-9_./-]{1,256}") and
            all(s not in ("",".","..") for s in obj["path"].split("/")) and
            matches(obj["commit"],r"[0-9a-f]{40}") and matches(obj["blob"],r"[0-9a-f]{40}"),
            "BLOCKED_SEMANTIC_IDENTITY")
    return ArtifactRef(**obj)

def policy(obj):
    closed(obj,{"privacy_class","retention_class","expires_tick"})
    require(type(obj["privacy_class"]) is str and
            obj["privacy_class"] in ("synthetic","minimized_derived") and
            type(obj["retention_class"]) is str and
            obj["retention_class"] in ("memory_only","synthetic_snapshot") and
            (obj["privacy_class"]=="synthetic" or obj["retention_class"]=="memory_only"),
            "BLOCKED_SEMANTIC_PRIVACY")
    require(tick(obj["expires_tick"]),"BLOCKED_SEMANTIC_EXPIRY")
    return Policy(**obj)

def parse(data: bytes) -> SemanticInput:
    require(type(data) is bytes and 0 < len(data) <= MAX_INPUT,"BLOCKED_SEMANTIC_SIZE")
    def pairs(items):
        out={}
        for k,v in items:
            require(k not in out,"BLOCKED_SEMANTIC_DUPLICATE_KEY")
            out[k]=v
        return out
    def bad_constant(_):
        raise SemanticError("BLOCKED_SEMANTIC_SCHEMA")
    try:
        obj=json.loads(data.decode("utf-8"),object_pairs_hook=pairs,parse_constant=bad_constant)
        canonical(obj)
        return _parse(obj)
    except SemanticError:
        raise
    except (ValueError,TypeError,UnicodeError,KeyError,RecursionError):
        raise SemanticError("BLOCKED_SEMANTIC_SCHEMA") from None

def _parse(o):
    closed(o,{"schema_version","input_id","content_class","purpose","scope","content","category",
              "targets","disagreement_level","participant","content_source_id","sources","policy",
              "analysis_policy","authority"})
    require(o["schema_version"]==SCHEMA,"BLOCKED_SEMANTIC_VERSION")
    require(ident(o["input_id"],"semantic"),"BLOCKED_SEMANTIC_IDENTITY")
    require(o["purpose"]==PURPOSE,"BLOCKED_SEMANTIC_PURPOSE")
    require(type(o["content_class"]) is str and o["content_class"] in
            ("synthetic","admitted_minimized"),"BLOCKED_SEMANTIC_CONTENT_CLASS")
    sc=o["scope"]
    closed(sc,{"discussion_id","event_id","sequence","at_tick"})
    require(ident(sc["discussion_id"],"discussion") and ident(sc["event_id"],"event") and
            tick(sc["sequence"]) and sc["sequence"]>0 and tick(sc["at_tick"]),
            "BLOCKED_SEMANTIC_IDENTITY")
    a=o["analysis_policy"]
    closed(a,{"mode","source","allowed_categories","max_text_bytes","allow_participant"})
    require(a["mode"]=="declared_only","BLOCKED_SEMANTIC_ANALYSIS_UNSUPPORTED")
    require(type(a["allowed_categories"]) is list and 1<=len(a["allowed_categories"])<=len(CATEGORIES)
            and all(type(c) is str and c in CATEGORIES for c in a["allowed_categories"])
            and len(set(a["allowed_categories"]))==len(a["allowed_categories"])
            and type(a["max_text_bytes"]) is int and 1<=a["max_text_bytes"]<=MAX_TEXT
            and type(a["allow_participant"]) is bool,"BLOCKED_SEMANTIC_ANALYSIS_POLICY")
    analysis=AnalysisPolicy(a["mode"],artifact(a["source"]),tuple(a["allowed_categories"]),
                            a["max_text_bytes"],a["allow_participant"])
    require(type(o["category"]) is str and o["category"] in analysis.allowed_categories,
            "BLOCKED_SEMANTIC_CATEGORY")
    c=o["content"]
    require(type(c) is dict and type(c.get("kind")) is str)
    if c["kind"]=="excerpt":
        closed(c,{"kind","text"});bounded_text(c["text"],analysis.max_text_bytes)
        content=Content("excerpt",c["text"],None)
    elif c["kind"]=="claim":
        closed(c,{"kind","subject","predicate","object"})
        values=tuple(c[k] for k in ("subject","predicate","object"))
        for v in values: bounded_text(v,160)
        content=Content("claim",None,values)
        bounded_text(content.render(),analysis.max_text_bytes)
    else:
        raise SemanticError("BLOCKED_SEMANTIC_CONTENT_KIND")
    require(type(o["targets"]) is list and len(o["targets"])<=16 and
            all(ident(t,"event") and t!=sc["event_id"] for t in o["targets"])
            and len(set(o["targets"]))==len(o["targets"]),"BLOCKED_SEMANTIC_TARGETS")
    if o["category"]=="disagreement":
        require(len(o["targets"])>=2 and type(o["disagreement_level"]) is str and
                o["disagreement_level"] in LEVELS,"BLOCKED_SEMANTIC_TARGETS")
    else:
        require(not o["targets"] and o["disagreement_level"] is None,"BLOCKED_SEMANTIC_TARGETS")
    p=policy(o["policy"]);sources=[]
    require(type(o["sources"]) is list and 1<=len(o["sources"])<=8,"BLOCKED_SEMANTIC_SOURCE")
    for s in o["sources"]:
        closed(s,{"scope","source_id","version_sha256","kind","policy"})
        require(s["scope"]==sc["discussion_id"] and ident(s["source_id"],"source") and
                matches(s["version_sha256"],r"[0-9a-f]{64}"),"BLOCKED_SEMANTIC_SOURCE")
        sp=policy(s["policy"])
        require(s["kind"]==("synthetic_fixture" if sp.privacy_class=="synthetic"
                           else "normalized_projection"),"BLOCKED_SEMANTIC_SOURCE")
        sources.append(Source(s["scope"],s["source_id"],s["version_sha256"],s["kind"],sp))
    require(len({s.source_id for s in sources})==len(sources),"BLOCKED_SEMANTIC_SOURCE")
    require(ident(o["content_source_id"],"source"),"BLOCKED_SEMANTIC_SOURCE")
    chosen=[s for s in sources if s.source_id==o["content_source_id"]]
    require(len(chosen)==1 and chosen[0].version_sha256==digest(content.projection()),
            "BLOCKED_SEMANTIC_CONTENT_IDENTITY")
    if o["content_class"]=="synthetic":
        require(all(x.privacy_class=="synthetic" for x in (p,*[s.policy for s in sources])),
                "BLOCKED_SEMANTIC_PRIVACY_DOWNGRADE")
    else:
        require(p.privacy_class=="minimized_derived" and
                chosen[0].policy.privacy_class=="minimized_derived","BLOCKED_SEMANTIC_PRIVACY_DOWNGRADE")
    participant=None
    if o["participant"] is not None:
        d=o["participant"]
        closed(d,{"scope","pseudonym","expires_tick","scheme"})
        require(analysis.allow_participant and d["scope"]==sc["discussion_id"] and
                ident(d["pseudonym"],"participant") and tick(d["expires_tick"]) and
                d["scheme"]=="discussion_local_opaque","BLOCKED_SEMANTIC_PARTICIPANT")
        participant=ParticipantRef(**d)
    auth=o["authority"]
    closed(auth,{"requester_id","task","writer","privacy_gate","scope"})
    require(matches(auth["requester_id"],r"[A-Z][A-Z0-9]{1,15}") and auth["scope"]==SCOPE,
            "BLOCKED_SEMANTIC_AUTHORITY")
    authority=Authority(auth["requester_id"],artifact(auth["task"]),artifact(auth["writer"]),
                        artifact(auth["privacy_gate"]),auth["scope"])
    return SemanticInput(SCHEMA,o["input_id"],o["content_class"],PURPOSE,EventScope(**sc),content,
        o["category"],tuple(o["targets"]),o["disagreement_level"],participant,o["content_source_id"],
        tuple(sources),p,analysis,authority)

def load_core(path: Path):
    try:
        raw=path.read_bytes()
    except OSError:
        raise SemanticError("BLOCKED_SEMANTIC_CORE_UNAVAILABLE") from None
    require(git_blob(raw)==CORE_BLOB and hashlib.sha256(raw).hexdigest()==CORE_SHA256,
            "BLOCKED_SEMANTIC_CORE_IDENTITY")
    mod=ModuleType("_semantic_core_"+CORE_BLOB);mod.__file__=str(path)
    sys.modules[mod.__name__]=mod
    exec(compile(raw,str(path),"exec"),mod.__dict__)
    return mod

class SemanticAdapter:
    def __init__(self, core_path: Path):
        self.core=load_core(core_path)

    def convert(self, data: bytes, *, now_tick: int,
                verifier: Callable[[AdmissionCheck],AdmissionProof|None]|None=None) -> SemanticResult:
        item=parse(data)
        require(tick(now_tick) and item.scope.at_tick<=now_tick,"BLOCKED_SEMANTIC_TIME")
        policies=(item.policy,*[s.policy for s in item.sources])
        expiry=min(p.expires_tick for p in policies)
        if item.participant:
            expiry=min(expiry,item.participant.expires_tick)
        require(now_tick<expiry,"BLOCKED_SEMANTIC_EXPIRED")
        privacy=("minimized_derived" if any(p.privacy_class=="minimized_derived" for p in policies)
                 else "synthetic")
        retention=("synthetic_snapshot" if all(p.retention_class=="synthetic_snapshot" for p in policies)
                   else "memory_only")
        effective=Policy(privacy,retention,expiry)
        check=AdmissionCheck(item.identity,item.authority,digest(asdict(item.analysis_policy)),
            digest(item.content.projection()),digest([asdict(s) for s in item.sources]),
            digest(asdict(item.participant) if item.participant else None),item.scope.discussion_id,
            item.purpose,item.category,item.content_class,effective)
        check_hash=digest(asdict(check))
        require(callable(verifier),"BLOCKED_SEMANTIC_AUTHORITY")
        try:
            proof=verifier(check)
        except Exception:
            raise SemanticError("BLOCKED_SEMANTIC_AUTHORITY") from None
        require(type(proof) is AdmissionProof and proof.check_sha256==check_hash and
                proof.scope==SCOPE and type(proof.source) is ArtifactRef and
                proof.minimization_confirmed is True and
                type(proof.participant_scoped_confirmed) is bool and
                (item.participant is None or proof.participant_scoped_confirmed is True),
                "BLOCKED_SEMANTIC_AUTHORITY")
        artifact(asdict(proof.source))
        require(tick(proof.valid_from_tick) and tick(proof.valid_until_tick) and
                proof.valid_from_tick<=now_tick<proof.valid_until_tick,
                "BLOCKED_SEMANTIC_AUTHORITY_EXPIRED")
        require(tick(proof.retention_limit_tick) and expiry<=proof.retention_limit_tick,
                "BLOCKED_SEMANTIC_RETENTION")
        require(digest(asdict(check))==check_hash and parse(data).identity==item.identity,
                "BLOCKED_SEMANTIC_CONTEXT_CHANGED")
        semantic_source_id="source_"+item.input_id.split("_",1)[1]
        require(all(s.source_id!=semantic_source_id for s in item.sources),"BLOCKED_SEMANTIC_SOURCE_COLLISION")
        core_sources=[self.core.SourceRef(s.scope,s.source_id,s.version_sha256,s.kind) for s in item.sources]
        core_sources.append(self.core.SourceRef(item.scope.discussion_id,semantic_source_id,item.identity,
            "synthetic_fixture" if privacy=="synthetic" else "normalized_projection"))
        try:
            event=self.core.NormalizedEvent(item.scope.discussion_id,item.scope.event_id,
                item.scope.sequence,item.scope.at_tick,"observe",item.category,item.content.render(),
                item.targets,item.disagreement_level,tuple(core_sources),
                self.core.RetentionPrivacy(**asdict(effective)))
        except self.core.CoreError:
            raise SemanticError("FAIL_SEMANTIC_CORE_CONTRACT") from None
        return SemanticResult(event,item.identity,check_hash,digest(asdict(proof)),item.authority,
            proof.source,item.analysis_policy,item.content_class,digest(asdict(event)))
