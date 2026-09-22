"""Content-free, immutable completion metadata. No provider/credential capability."""
from pathlib import Path
import hashlib
import json
import math
import os
import re
import stat
import uuid

SCHEMA = 'wb.openai.booster.failure_metadata.v1'
MAX_BYTES = 16384
MAX_INT = 2**53 - 1
STATES = {'value', 'absent', 'null', 'ancestor_null', 'ancestor_invalid', 'invalid', 'unsupported'}
STATUS = {'completed', 'failed', 'in_progress', 'cancelled', 'queued', 'incomplete'}
EFFORT = {'none', 'minimal', 'low', 'medium', 'high', 'xhigh', 'max', 'ultra'}
# Unknown strings never pass through, including error codes/types.
FIELDS = {
 'status': STATUS,
 'incomplete_details.reason': {'max_output_tokens', 'content_filter'},
 'error.code': {'server_error', 'rate_limit_exceeded', 'invalid_prompt', 'invalid_request_error',
                'context_length_exceeded', 'content_filter', 'insufficient_quota'},
 'error.type': {'server_error', 'rate_limit_error', 'invalid_request_error', 'api_error',
                'authentication_error', 'permission_error'},
 'max_output_tokens': 'count',
 'usage.input_tokens': 'count',
 'usage.output_tokens': 'count',
 'usage.total_tokens': 'count',
 'usage.input_tokens_details.cached_tokens': 'count',
 'usage.output_tokens_details.reasoning_tokens': 'count',
 'reasoning.effort': EFFORT,
}
IDENTITY_KEYS = {'request_sha256', 'plan_sha256', 'authority_sha256', 'attempt_key',
                 'response_sha256', 'native_body_sha256', 'shape_snapshot_sha256'}
KEYS = {'schema', 'execution_mode', 'identity', 'http_status', 'response_bytes', 'fields',
        'transport_latency_ms', 'latency_source', 'requester_review_required',
        'project_acceptance', 'project_state_mutation', 'snapshot_sha256'}

class MetadataError(ValueError): pass

def need(ok, code):
    if not ok: raise MetadataError(code)

def canon(obj):
    try: return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    except Exception: raise MetadataError('BLOCKED_METADATA_SERIALIZATION') from None

def sha(raw): return hashlib.sha256(raw).hexdigest()
def count(v): return type(v) is int and 0 <= v <= MAX_INT
def hex64(v): return type(v) is str and re.fullmatch('[0-9a-f]{64}', v) is not None

def typed(v, rule):
    if rule == 'count': return 'value' if count(v) else 'invalid'
    if type(v) is not str: return 'invalid'
    return 'value' if v in rule else 'unsupported'

def select(obj, dotted, rule):
    parts = dotted.split('.')
    parent = obj
    for i, key in enumerate(parts):
        if parent is None: return {'state': 'ancestor_null'}
        if type(parent) is not dict: return {'state': 'ancestor_invalid'}
        if key not in parent: return {'state': 'absent'}
        parent = parent[key]
        if i == len(parts)-1:
            if parent is None: return {'state': 'null'}
            state = typed(parent, rule)
            return {'state': state, 'value': parent} if state == 'value' else {'state': state}

def no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, 'BLOCKED_METADATA_DUPLICATE_JSON_KEY')
        out[key] = value
    return out

def parse(raw):
    try: return json.loads(raw.decode('utf-8'), object_pairs_hook=no_duplicates,
                           parse_constant=lambda _: (_ for _ in ()).throw(MetadataError('BLOCKED_METADATA_NONFINITE_JSON')))
    except MetadataError: raise
    except Exception: raise MetadataError('BLOCKED_METADATA_JSON') from None

def snapshot_identity(record):
    return sha(canon({k: v for k, v in record.items() if k != 'snapshot_sha256'}))

def build(*, body, identity, execution_mode, http_status, transport_latency_ms):
    need(type(body) is bytes and 0 < len(body) <= MAX_BYTES, 'BLOCKED_METADATA_BODY_BOUND')
    obj = parse(body)
    need(type(obj) is dict, 'BLOCKED_METADATA_RESPONSE_OBJECT')
    need(type(identity) is dict and set(identity) == IDENTITY_KEYS, 'BLOCKED_METADATA_IDENTITY_KEYS')
    need(identity['response_sha256'] == sha(body), 'BLOCKED_METADATA_RESPONSE_HASH')
    record = dict(schema=SCHEMA, execution_mode=execution_mode, identity=dict(identity),
                  http_status=http_status, response_bytes=len(body),
                  fields={path: select(obj, path, rule) for path, rule in FIELDS.items()},
                  transport_latency_ms=transport_latency_ms,
                  latency_source='transport_boundary_monotonic' if transport_latency_ms is not None else None,
                  requester_review_required=True, project_acceptance='NOT_GRANTED', project_state_mutation=False)
    record['snapshot_sha256'] = snapshot_identity(record)
    validate(record, expected_snapshot_sha256=record['snapshot_sha256'], expected_identity=identity,
             expected_mode=execution_mode)
    return record

def validate(record, *, expected_snapshot_sha256, expected_identity, expected_mode):
    need(type(record) is dict and set(record) == KEYS, 'BLOCKED_METADATA_SCHEMA_KEYS')
    need(record['schema'] == SCHEMA, 'BLOCKED_METADATA_SCHEMA')
    need(expected_mode in ('REAL_PILOT', 'OFFLINE_TEST') and record['execution_mode'] == expected_mode,
         'BLOCKED_METADATA_MODE')
    ident = record['identity']
    need(type(ident) is dict and set(ident) == IDENTITY_KEYS and all(hex64(v) for v in ident.values()),
         'BLOCKED_METADATA_IDENTITY')
    need(type(expected_identity) is dict and set(expected_identity) == IDENTITY_KEYS and ident == expected_identity,
         'BLOCKED_METADATA_IDENTITY_MISMATCH')
    need(hex64(expected_snapshot_sha256) and record['snapshot_sha256'] == expected_snapshot_sha256
         and snapshot_identity(record) == expected_snapshot_sha256, 'BLOCKED_METADATA_HASH')
    need(type(record['http_status']) is int and 100 <= record['http_status'] <= 599, 'BLOCKED_METADATA_HTTP')
    need(type(record['response_bytes']) is int and 0 < record['response_bytes'] <= MAX_BYTES, 'BLOCKED_METADATA_BYTES')
    fields = record['fields']
    need(type(fields) is dict and set(fields) == set(FIELDS), 'BLOCKED_METADATA_FIELD_SET')
    for path, rule in FIELDS.items():
        leaf = fields[path]
        need(type(leaf) is dict and type(leaf.get('state')) is str and leaf['state'] in STATES,
             'BLOCKED_METADATA_FIELD_STATE')
        state = leaf['state']
        need(set(leaf) == ({'state', 'value'} if state == 'value' else {'state'}), 'BLOCKED_METADATA_FIELD_KEYS')
        if state == 'value': need(typed(leaf['value'], rule) == 'value', 'BLOCKED_METADATA_FIELD_VALUE')
        if state == 'unsupported': need(rule != 'count', 'BLOCKED_METADATA_FIELD_STATE')
        if state.startswith('ancestor_'): need('.' in path, 'BLOCKED_METADATA_FIELD_STATE')
    latency = record['transport_latency_ms']
    need(latency is None or (type(latency) in (int, float) and math.isfinite(latency) and 0 <= latency <= MAX_INT),
         'BLOCKED_METADATA_LATENCY')
    need(record['latency_source'] == ('transport_boundary_monotonic' if latency is not None else None),
         'BLOCKED_METADATA_LATENCY_SOURCE')
    need(record['requester_review_required'] is True and record['project_acceptance'] == 'NOT_GRANTED'
         and record['project_state_mutation'] is False, 'BLOCKED_METADATA_AUTHORITY')

def read_and_validate(path, *, expected_snapshot_sha256, expected_identity, expected_mode):
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, 'rb') as stream:
            need(stat.S_ISREG(os.fstat(stream.fileno()).st_mode), 'BLOCKED_METADATA_NOT_REGULAR')
            raw = stream.read(MAX_BYTES+1)
    except OSError: raise MetadataError('BLOCKED_METADATA_READ') from None
    need(0 < len(raw) <= MAX_BYTES, 'BLOCKED_METADATA_READ_BOUND')
    record = parse(raw)
    validate(record, expected_snapshot_sha256=expected_snapshot_sha256,
             expected_identity=expected_identity, expected_mode=expected_mode)
    need(raw == canon(record)+b'\n', 'BLOCKED_METADATA_NONCANONICAL')
    return record

def persist_and_readback(path, record):
    expected = dict(expected_snapshot_sha256=record.get('snapshot_sha256'),
                    expected_identity=record.get('identity'), expected_mode=record.get('execution_mode'))
    validate(record, **expected)
    raw = canon(record)+b'\n'
    need(len(raw) <= MAX_BYTES, 'BLOCKED_METADATA_WRITE_BOUND')
    path = Path(path)
    temp = path.parent / ('.'+path.name+'.tmp.'+uuid.uuid4().hex)
    fd = None
    try:
        path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        offset = 0
        while offset < len(raw):
            n = os.write(fd, raw[offset:]); need(n > 0, 'BLOCKED_METADATA_WRITE'); offset += n
        os.fsync(fd); os.close(fd); fd = None
        # Atomic create, never overwrite a prior artifact or a symlink.
        os.link(temp, path)
        dirfd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try: os.fsync(dirfd)
        finally: os.close(dirfd)
    except OSError: raise MetadataError('BLOCKED_METADATA_PERSISTENCE') from None
    finally:
        if fd is not None: os.close(fd)
        try: temp.unlink()
        except FileNotFoundError: pass
    read_and_validate(path, **expected)
    return expected['expected_snapshot_sha256']
