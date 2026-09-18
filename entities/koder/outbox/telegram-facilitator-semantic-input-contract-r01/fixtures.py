#!/usr/bin/env python3
"""Учебные данные. Не сведения о людях и не действующие разрешения.
Функция возвращает 13 словарей в памяти, ничего не читает и не записывает.
"""
import hashlib
import json

def fid(prefix,n):
    return prefix+"_"+format(n,"032x")

def content_hash(content):
    return hashlib.sha256(json.dumps(content,ensure_ascii=False,sort_keys=True,
        separators=(",",":")).encode()).hexdigest()

TASK = {'repository': 'puev5691/wellbeing-hq', 'path': 'entities/koordinator/outbox/KOO__telegram-facilitator-semantic-input-contract-r01__KOD.md', 'commit': '517aab86ec383e6b4c9446eaf1863decb45ba2eb', 'blob': '8a2d1bcc4dd319fee8dfff9a5d8ea6e0d2e66b8f'}
WRITER = {'repository': 'puev5691/wellbeing-hq', 'path': 'entities/koder/current/KOD__replacement-current-writer-v03.md', 'commit': 'f6686de567b4fa1906ea7cecbc5b5963fcd4e587', 'blob': 'bfeff738de2759248307dd52433c77139624fb54'}
ANALYSIS = {'repository': 'synthetic-fixture/policy', 'path': 'declared-only.md', 'commit': '1111111111111111111111111111111111111111', 'blob': '2222222222222222222222222222222222222222'}
PRIVACY = {'repository': 'synthetic-fixture/privacy', 'path': 'admission-fixture.md', 'commit': '3333333333333333333333333333333333333333', 'blob': '4444444444444444444444444444444444444444'}
CATEGORIES = ['concept', 'criterion', 'disagreement', 'fact_claim', 'goal', 'open_question', 'option', 'position', 'preliminary_agreement', 'problem', 'procedure', 'topic']
THREAD = [('topic', 'Совместное использование учебного оборудования.'), ('problem', 'Непонятно, свободен ли общий учебный инструмент.'), ('concept', 'Нужно уточнить значение отметки «свободен».'), ('fact_claim', None), ('goal', 'Подготовить проверяемое предложение об учёте занятости.'), ('criterion', 'Макет различает два одновременных учебных запроса.'), ('option', 'Рассмотреть общую карточку состояния.'), ('procedure', 'Согласовать критерий, затем проверить учебный макет.'), ('position', 'Предложена ручная отметка.'), ('position', 'Предложена предварительная заявка.'), ('preliminary_agreement', 'Сообщён предварительный интерес, не согласие всей группы.'), ('open_question', 'Кто проверит результат учебного сценария?'), ('disagreement', 'Явно заявлено различие способов учёта.')]

def make_inputs():
    result=[]
    for n,(category,text) in enumerate(THREAD,1):
        content=({"kind":"excerpt","text":text} if text is not None else
            {"kind":"claim","subject":"Учебная карточка","predicate":"содержит",
             "object":"две синтетические записи"})
        policy={"privacy_class":"synthetic","retention_class":"synthetic_snapshot","expires_tick":100}
        source={"scope":fid("discussion",1),"source_id":fid("source",100+n),
            "version_sha256":content_hash(content),"kind":"synthetic_fixture","policy":dict(policy)}
        result.append({"schema_version":"semantic-input-r01","input_id":fid("semantic",10000+n),
            "content_class":"synthetic","purpose":"discussion_facilitation",
            "scope":{"discussion_id":fid("discussion",1),"event_id":fid("event",n),"sequence":n,"at_tick":n},
            "content":content,"category":category,
            "targets":[fid("event",9),fid("event",10)] if n==13 else [],
            "disagreement_level":"means" if n==13 else None,
            "participant":({"scope":fid("discussion",1),"pseudonym":fid("participant",n),
                "expires_tick":90,"scheme":"discussion_local_opaque"} if n in (9,10) else None),
            "content_source_id":source["source_id"],"sources":[source],"policy":policy,
            "analysis_policy":{"mode":"declared_only","source":dict(ANALYSIS),
                "allowed_categories":list(CATEGORIES),"max_text_bytes":512,"allow_participant":True},
            "authority":{"requester_id":"KOD","task":dict(TASK),"writer":dict(WRITER),
                "privacy_gate":dict(PRIVACY),"scope":"semantic_input_to_observe_only"}})
    return result
