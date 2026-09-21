#!/usr/bin/env python3
"""Run locally in a scratch checkout. No network, real credentials or deployment."""
import hashlib, io, json, os, socket, sys, unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
sys.path.insert(0,str(ROOT))
for key in ('OPENAI_API_KEY','CREDENTIALS_DIRECTORY','HTTP_PROXY','HTTPS_PROXY','ALL_PROXY'):
    os.environ.pop(key,None)
for key,name in {'LIVE_WORKER':'live_worker.py','DIAG_INTEGRATION':'diagnostic_reviewable_live_worker.py',
                 'RESULT_INTEGRATION':'reviewable_live_worker.py','RESULT_STORE':'review_result_store.py',
                 'SHAPE_STORE':'response_shape_store.py','INVOCATION':'SENTINEL-INVOCATION.example.json'}.items():
    os.environ[key]=str(ROOT/name)
assert hashlib.sha256((ROOT/'live_worker.py').read_bytes()).hexdigest()=='175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3'
suite=unittest.defaultTestLoader.discover(str(ROOT),pattern='test_*.py')
stream=io.StringIO()
with patch.object(socket.socket,'connect',side_effect=AssertionError('NETWORK_FORBIDDEN')), \
     patch('socket.create_connection',side_effect=AssertionError('NETWORK_FORBIDDEN')):
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
text=stream.getvalue()
# Remove duration, which is not deterministic evidence.
import re
text=re.sub(r'Ran (\d+) tests in [0-9.]+s',r'Ran \1 tests (duration omitted)',text)
(ROOT/'TEST-LOG.txt').write_text(text)
evidence={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
          'skipped':len(result.skipped),'provider_calls':0,'real_credential_value_reads':0,
          'host_systemd_mutation':0,'deployment':0,'retries':0,'fallback':'none','tools':'none',
          'project_acceptance':'NOT_GRANTED','production_acceptance':'NOT_GRANTED',
          'fixtures':'synthetic resolver/client only; socket connections forbidden',
          'success':result.wasSuccessful()}
(ROOT/'TEST-RESULTS.json').write_text(json.dumps(evidence,indent=2)+'\n')
print(text);print(json.dumps(evidence));sys.exit(0 if result.wasSuccessful() else 1)
