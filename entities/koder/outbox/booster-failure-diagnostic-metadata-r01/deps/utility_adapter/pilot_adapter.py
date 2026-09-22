"""Offline D0 requester adapter. No transport, resolver, or live entrypoint."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import math
import sys

ROOT = Path(__file__).resolve().parent
PINS = {
    'booster_runtime': 'c0b64fd44879c6c2395c02f66ee79c641a36c768372513ed35d149289ff2d941',
    'review_result_store': '72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba',
    'benchmark_harness': 'becf19820c6ef125d89b121f1b1a2242e315462531e64183ae6e5e6218abc944',
}
SCHEMA = 'wb.booster.utility_pilot.offline.v1'
TASK = '507aaf662da4a6b3c7704d712eea9dd5b71ee160'
TASK_BLOB = 'b3e9d22aada30c628a71971f08e1d0f25d49a7e0'
WRITER = 'cf1c84f9df7c90509703e4885844d0cf871ff412'
FLAGS = dict(evidence_class='D0_SYNTHETIC_FIXTURE', provider_calls=0,
             network_calls=0, credential_value_reads=0,
             live_authority='NOT_GRANTED', standing_authority='NOT_GRANTED',
             project_acceptance='NOT_GRANTED', project_state_applied=False)

class Blocked(ValueError):
    pass

def need(ok, code):
    if not ok:
        raise Blocked(code)

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')

def digest(obj):
    return hashlib.sha256(obj if type(obj) is bytes else canonical(obj)).hexdigest()

def dependency(name):
    path = ROOT / 'deps' / (name + '.py')
    need(digest(path.read_bytes()) == PINS[name], 'BLOCKED_DEPENDENCY_IDENTITY')
    spec = importlib.util.spec_from_file_location('_utility_' + name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def keys(obj, expected):
    need(type(obj) is dict and set(obj) == set(expected.split()), 'BLOCKED_SCHEMA')

def text(value):
    need(type(value) is str and 0 < len(value.encode()) <= 4096 and value.strip(), 'BLOCKED_TEXT')

def number(value):
    need(type(value) in (int, float) and math.isfinite(value) and value >= 0, 'BLOCKED_METRIC')

def integer(value):
    need(type(value) is int and value >= 0, 'BLOCKED_METRIC')

def evidence(value):
    need(type(value) is list and 0 < len(value) <= 16, 'BLOCKED_EVIDENCE')
    for v in value:
        text(v)
        need(v.startswith('fixture://'), 'BLOCKED_NON_SYNTHETIC_EVIDENCE')

def load_json(path):
    raw = Path(path).read_bytes()
    need(0 < len(raw) <= 32768, 'BLOCKED_INPUT_SIZE')
    def pairs(items):
        obj = {}
        for k, v in items:
            need(k not in obj, 'BLOCKED_DUPLICATE_KEY')
            obj[k] = v
        return obj
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(Blocked('BLOCKED_NONFINITE')))

def prepare(request):
    """Input is a trusted caller-owned request, never taken from model output."""
    b = dependency('booster_runtime')
    need(type(request) is dict and set(request) == set(b.BoosterRequest.__dataclass_fields__), 'BLOCKED_REQUEST_SCHEMA')
    need(type(request['tools']) is list and request['tools'] == [], 'BLOCKED_TOOLS')
    need(request['task_path'] == 'entities/koordinator/outbox/KOO__booster-utility-pilot-adapter-r01__KOD.md'
         and request['task_commit'] == TASK and request['task_blob'] == TASK_BLOB
         and request['writer_blob'] == WRITER
         and request['writer_path'] == 'entities/koder/current/KOD__replacement-current-writer-v05.md'
         and request['writer_commit'] == 'df92a8bfcce29294332f6e4de3391a3e7966adfd'
         and request['entity_id'] == 'KOD' and request['role'] == 'koder', 'BLOCKED_TASK_WRITER_SCOPE')
    need(request['provider'] == 'openai' and request['model'] == 'gpt-5.6-luna', 'BLOCKED_PROVIDER_MODEL')
    need(request['source_locator'].startswith('fixture://utility-r01/'), 'BLOCKED_SOURCE')
    need(request['source_sha256'] == digest(request['payload'].encode()), 'BLOCKED_SOURCE_HASH')
    text(request['purpose'])
    obj = dict(request, tools=())
    req = b.BoosterRequest(**obj)
    auth = b.Authority('utility-r01-offline', 'REPLAY_ONLY', req.entity_id,
                       req.task_commit, req.writer_blob, req.provider, req.model,
                       req.privacy_class, (), False)
    b.validate_request(req, auth)
    # New domain-separated mapping; no equality with legacy request hashes implied.
    rh = digest({'domain': SCHEMA + '/request', 'request': request})
    plan = {'domain': SCHEMA + '/plan', 'request_sha256': rh, 'mode': 'OFFLINE_FIXTURE',
            'provider': req.provider, 'model': req.model, 'max_output_tokens': req.max_output_tokens,
            'source_sha256': req.source_sha256, 'tools': [], 'provider_calls': 0}
    ph = digest(plan)
    ah = digest({'domain': SCHEMA + '/fixture-authority', 'task_commit': TASK,
                 'task_blob': TASK_BLOB, 'writer_blob': WRITER,
                 'request_sha256': rh, 'plan_sha256': ph, 'live_authority': 'NOT_GRANTED'})
    attempt = digest({'domain': SCHEMA + '/fixture-attempt', 'request_sha256': rh,
                      'plan_sha256': ph, 'authority_sha256': ah})
    identity = dict(attempt_key=attempt, request_sha256=rh, task_commit=TASK,
                    task_blob=TASK_BLOB, writer_blob=WRITER, plan_sha256=ph,
                    authority_sha256=ah, provider=req.provider, model=req.model)
    return {'schema': SCHEMA + '/prepared', 'identity': identity, 'plan': plan, **FLAGS}

def verify_review(path, request, expected_file_sha256):
    """Expected file hash comes from trusted fixture manifest/producer receipt."""
    prepared = prepare(request)
    raw = Path(path).read_bytes()
    need(len(raw) <= 32768 and digest(raw) == expected_file_sha256, 'BLOCKED_REVIEW_FILE_HASH')
    # Existing corrected validator is the authority for review-result v2 semantics.
    record = dependency('review_result_store').read_and_validate(path, **prepared['identity'])
    return prepared, record

def metrics(obj):
    keys(obj, 'active_seconds elapsed_seconds cycles rework_count rework_seconds phases rubric evidence')
    for k in ('active_seconds', 'elapsed_seconds', 'rework_seconds'):
        number(obj[k])
    for k in ('cycles', 'rework_count'):
        integer(obj[k])
    need(obj['cycles'] >= 1 and obj['elapsed_seconds'] >= obj['active_seconds']
         and obj['rework_seconds'] <= obj['active_seconds'], 'BLOCKED_METRIC_RELATION')
    keys(obj['phases'], 'preparation_seconds work_seconds review_seconds rework_seconds')
    for v in obj['phases'].values():
        number(v)
    need(math.isclose(sum(obj['phases'].values()), obj['active_seconds'], abs_tol=1e-9)
         and obj['phases']['rework_seconds'] == obj['rework_seconds'], 'BLOCKED_PHASE_TOTAL')
    need(type(obj['rubric']) is dict and 0 < len(obj['rubric']) <= 16, 'BLOCKED_RUBRIC')
    for k, v in obj['rubric'].items():
        text(k)
        need(type(v) is bool, 'BLOCKED_RUBRIC')
    evidence(obj['evidence'])

def cost_card(cost, model):
    keys(cost, 'kind usage price_snapshot evidence provider_latency_ms')
    if cost['provider_latency_ms'] is not None:
        number(cost['provider_latency_ms'])
    need(cost['kind'] in ('unknown', 'synthetic_estimate'), 'BLOCKED_COST_KIND')
    if cost['kind'] == 'unknown':
        need(cost['usage'] is None and cost['price_snapshot'] is None
             and cost['evidence'] is None and cost['provider_latency_ms'] is None, 'BLOCKED_UNKNOWN_COST')
        return {'kind': 'unknown', 'estimated_cost_usd': None, 'billed_cost_usd': None}
    evidence(cost['evidence'])
    u = cost['usage']
    keys(u, 'input_tokens cached_input_tokens output_tokens total_tokens')
    for v in u.values():
        integer(v)
    need(u['cached_input_tokens'] <= u['input_tokens'] and
         u['total_tokens'] == u['input_tokens'] + u['output_tokens'], 'BLOCKED_USAGE')
    p = cost['price_snapshot']
    keys(p, 'snapshot_id models estimator_scope')
    text(p['snapshot_id'])
    need(p['snapshot_id'].startswith('fixture:'), 'BLOCKED_PRICE_PROVENANCE')
    need(type(p['models']) is dict and set(p['models']) == {model}, 'BLOCKED_PRICE_MODEL')
    keys(p['models'][model], 'input cached_input output')
    for v in p['models'][model].values():
        number(v)
    keys(p['estimator_scope'], 'max_input_tokens_inclusive over_limit')
    integer(p['estimator_scope']['max_input_tokens_inclusive'])
    need(p['estimator_scope']['over_limit'] == 'BLOCKED_PRICE_RULE_OUT_OF_SCOPE', 'BLOCKED_PRICE_SCOPE')
    b = dependency('benchmark_harness')
    amount = b.estimate_cost(model, b.Usage(**u), p)
    return {'kind': 'synthetic_estimate', 'estimated_cost_usd': amount, 'billed_cost_usd': None}

def make_card(request, review_path, expected_review_sha256, observations, requester_review):
    prepared, record = verify_review(review_path, request, expected_review_sha256)
    keys(observations, 'comparison_mode baseline assisted cost')
    need(observations['comparison_mode'] == 'synthetic_matched_pair', 'BLOCKED_COMPARISON_MODE')
    for side in ('baseline', 'assisted'):
        metrics(observations[side])
    base, assisted = observations['baseline'], observations['assisted']
    need(set(base['rubric']) == set(assisted['rubric']), 'BLOCKED_RUBRIC_MISMATCH')
    cost = cost_card(observations['cost'], request['model'])
    if requester_review is not None:
        keys(requester_review, 'entity_id decision reason evidence')
        need(requester_review['entity_id'] == request['entity_id'], 'BLOCKED_REQUESTER')
        need(requester_review['decision'] in ('accept_as_candidate', 'needs_rework', 'reject'), 'BLOCKED_REVIEW_DECISION')
        text(requester_review['reason'])
        evidence(requester_review['evidence'])
    complete = requester_review is not None
    return {'schema': SCHEMA + '/card', **FLAGS, 'identity': prepared['identity'],
            'review_result_sha256': expected_review_sha256,
            'review_payload_sha256': record['review_payload']['sha256'],
            'observations': observations, 'cost_summary': cost,
            'requester_review': requester_review, 'requester_review_required': True,
            'status': 'SYNTHETIC_REVIEW_RECORDED' if complete else 'PENDING_REQUESTER_REVIEW',
            'utility_verdict': ('candidate_only:' + requester_review['decision']) if complete else None,
            'real_utility_demonstrated': False,
            'comparison': {k + '_saved': base[k] - assisted[k] for k in
                           ('active_seconds', 'elapsed_seconds', 'cycles', 'rework_count', 'rework_seconds')}
                          if complete else None}

def read_card(path, expected_card_sha256, *, request, review_path, expected_review_sha256):
    raw = Path(path).read_bytes()
    need(len(raw) <= 32768 and digest(raw) == expected_card_sha256, 'BLOCKED_CARD_HASH')
    obj = load_json(path)
    need(type(obj) is dict and 'observations' in obj and 'requester_review' in obj, 'BLOCKED_CARD_SCHEMA')
    expected = make_card(request, review_path, expected_review_sha256,
                         obj['observations'], obj['requester_review'])
    need(canonical(obj) == canonical(expected), 'BLOCKED_CARD_READBACK')
    return obj

def save_card(path, *, request, review_path, expected_review_sha256, observations, requester_review):
    card = make_card(request, review_path, expected_review_sha256, observations, requester_review)
    # Reuse atomic local persistence, not a new storage service.
    dependency('review_result_store').persist_atomic(Path(path), card)
    expected = digest(canonical(card) + b'\n')
    read_card(path, expected, request=request, review_path=review_path,
              expected_review_sha256=expected_review_sha256)
    return expected

def main():
    ap = argparse.ArgumentParser(description='D0 offline fixture adapter; no live mode')
    ap.add_argument('--case', required=True)
    ap.add_argument('--review', required=True)
    ap.add_argument('--output', required=True)
    ns = ap.parse_args()
    try:
        case = load_json(ns.case)
        keys(case, 'request expected_review_sha256 observations requester_review')
        sha = save_card(ns.output, request=case['request'], review_path=ns.review,
                        expected_review_sha256=case['expected_review_sha256'],
                        observations=case['observations'], requester_review=case['requester_review'])
        print(json.dumps({'status': 'OFFLINE_CARD_READBACK_PASS', 'card_sha256': sha, **FLAGS}))
        return 0
    except Exception as exc:
        print(json.dumps({'status': 'BLOCKED', 'reason': str(exc) if isinstance(exc, (Blocked, ValueError)) else type(exc).__name__, **FLAGS}))
        return 20

if __name__ == '__main__':
    raise SystemExit(main())
