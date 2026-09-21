#!/usr/bin/env python3
"""Usage: python verify_delta.py BASE_V16 APPROVED_DELTA_DOC CANDIDATE_V17"""
import sys, pathlib, hashlib
base,proposal,candidate=[pathlib.Path(p).read_text() for p in sys.argv[1:4]]
assert hashlib.sha256(base.encode()).hexdigest()=='82e3117570a9ecd73be2dae1279ebb3e0a2d6125556de98d5c1ede14a9236ae5', 'wrong base'
assert hashlib.sha256(proposal.encode()).hexdigest()=='7105370e1f69dc6215fc7d3f5ed313c52f881b9e8aa3ee29fb967898bfb82ec4', 'wrong delta source'
heading='### Проверка физического экземпляра при замене чата\n'
delta=heading+proposal.split(heading,1)[1].split('\n## Проверка границ кандидата',1)[0]
delta=delta.rstrip()+'\n\n'
body,card=candidate.rsplit('## Служебная карточка\n',1)
old_body=base.rsplit('## Служебная карточка\n',1)[0]
assert body.count(delta)==1, 'delta altered or duplicated'
assert delta+'### Recovery task conveyor\n' in body, 'wrong insertion position'
restored=body.replace(delta,'',1)
restored=restored.replace(restored.split('\n',1)[0],old_body.split('\n',1)[0],1)
assert restored==old_body, 'unapproved body change'
assert candidate.split('\n',1)[0]=='# Канон сохранения состояния, инициации и восстановления Сущностей — v1.7 candidate'
for field in ['version: v1.7','status: candidate_for_controlled_source_review','effective: false','active_source_unchanged: entity-state-preservation-and-recovery-canon-v1_6-approved.md']:
 assert field in card, 'missing candidate boundary '+field
assert 'KOO instance-admission guard candidate' in card
print('PASS_EXACT_APPROVED_DELTA_ONLY')
print('PASS_BASE_BODY_BYTEWISE_RESTORED')
print('PASS_CANDIDATE_INACTIVE_METADATA')
print('candidate_sha256='+hashlib.sha256(candidate.encode()).hexdigest())
