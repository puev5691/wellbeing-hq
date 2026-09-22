"""Reproducible synthetic fixture construction, never provider execution."""
from pathlib import Path
import json
import pilot_adapter as a

def fixture():
    payload = 'Synthetic code review: def first(xs): return xs[0]. Explain the empty-list defect and propose one bounded test. Do not execute code.'
    request = dict(request_id='utility-r01-fixture', entity_id='KOD', role='koder',
        task_path='entities/koordinator/outbox/KOO__booster-utility-pilot-adapter-r01__KOD.md',
        task_commit=a.TASK, task_blob=a.TASK_BLOB,
        writer_path='entities/koder/current/KOD__replacement-current-writer-v05.md',
        writer_commit='df92a8bfcce29294332f6e4de3391a3e7966adfd', writer_blob=a.WRITER,
        purpose='Synthetic bounded code review comparison', provider='openai', model='gpt-5.6-luna',
        privacy_class='synthetic_only', tools=[], payload=payload,
        source_locator='fixture://utility-r01/first-function', source_sha256=a.digest(payload.encode()),
        max_output_tokens=128)
    prepared = a.prepare(request)
    body = a.canonical({'model': request['model'], 'output': [
        {'type': 'reasoning', 'summary': 'SYNTHETIC_METADATA_NOT_REVIEW'},
        {'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text',
          'text': 'An empty list raises IndexError at xs[0]. Add an empty-list test expecting IndexError under the stated current contract.'}]}]})
    # v2 requires provider_calls=1 as a protocol field. This record is synthetic,
    # not a record of an actual call. The adapter card always records actual calls=0.
    record = a.dependency('review_result_store').normalize_openai_result(
        body=body, **prepared['identity'], http_status=200, provider_calls=1, retries=0, fallback='none')
    def metrics(active, elapsed, cycles, count, rework, phases, rubric, label):
        return dict(active_seconds=active, elapsed_seconds=elapsed, cycles=cycles,
                    rework_count=count, rework_seconds=rework, phases=phases, rubric=rubric,
                    evidence=['fixture://utility-r01/' + label])
    observations = dict(comparison_mode='synthetic_matched_pair',
        baseline=metrics(120, 120, 2, 1, 30,
            dict(preparation_seconds=10, work_seconds=50, review_seconds=30, rework_seconds=30),
            {'identifies_empty_list': True, 'proposes_bounded_test': True}, 'baseline-trace'),
        assisted=metrics(95, 105, 1, 0, 0,
            dict(preparation_seconds=25, work_seconds=30, review_seconds=40, rework_seconds=0),
            {'identifies_empty_list': True, 'proposes_bounded_test': True}, 'assisted-trace'),
        cost=dict(kind='unknown', usage=None, price_snapshot=None, evidence=None, provider_latency_ms=None))
    review = dict(entity_id='KOD', decision='accept_as_candidate',
                  reason='Synthetic fixture assertion: both explicit rubric criteria satisfied; no project application.',
                  evidence=['fixture://utility-r01/requester-check'])
    raw = a.canonical(record) + b'\n'
    return dict(request=request, expected_review_sha256=a.digest(raw),
                observations=observations, requester_review=review), raw

if __name__ == '__main__':
    case, raw = fixture()
    dest = Path(__file__).resolve().parent / 'fixtures'
    dest.mkdir(exist_ok=True)
    (dest / 'case.json').write_bytes(a.canonical(case) + b'\n')
    (dest / 'review.synthetic.json').write_bytes(raw)
