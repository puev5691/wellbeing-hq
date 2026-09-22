"""Run offline tests with audited filesystem and denied external capabilities."""
from pathlib import Path
import io
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import test_bridge

attempts = []
def forbidden(*args, **kwargs):
    attempts.append('forbidden_capability')
    raise RuntimeError('FORBIDDEN_EXTERNAL_CAPABILITY')

class NoEnvironment(dict):
    # Fixed non-secret locale/terminal values for argparse; never read real env.
    SAFE = {'LANGUAGE':'C','LC_ALL':'C','LC_MESSAGES':'C','LANG':'C','COLUMNS':'80','LINES':'24'}
    def get(self, key, default=None):
        if key in self.SAFE:
            return self.SAFE[key]
        return forbidden()
    def __getitem__(self, key):
        if key in self.SAFE:
            return self.SAFE[key]
        return forbidden()

original_open = os.open
def resolved_open(path, flags, mode=0o777, *, dir_fd=None):
    # Python audit open events omit dir_fd. Resolve safe relative rmtree opens
    # against the actual directory descriptor before the audit hook sees them.
    if dir_fd is not None and not os.path.isabs(path):
        path = str(Path(os.readlink('/proc/self/fd/'+str(dir_fd))) / os.fsdecode(path))
        dir_fd = None
    return original_open(path, flags, mode, dir_fd=dir_fd)

with tempfile.TemporaryDirectory(prefix='utility-bridge-tests-') as scratch:
    tempfile.tempdir = scratch
    roots = (ROOT, Path(scratch))
    def audit(event, args):
        if event.startswith(('socket.', 'subprocess.')) or event in ('os.system','os.exec','os.posix_spawn'):
            forbidden()
        if event == 'open' and isinstance(args[0], (str, bytes)):
            p = Path(os.fsdecode(args[0])).resolve()
            if not any(p.is_relative_to(r) for r in roots):
                # Read-only imports from the interpreter library are allowed.
                mode, flags = args[1], args[2]
                writing = (isinstance(mode,str) and any(x in mode for x in 'wa+')) or flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT)
                if writing or not p.is_relative_to(Path(sys.base_prefix)):
                    forbidden()
    sys.addaudithook(audit)
    with patch.object(os,'open',resolved_open), patch.object(os,'environ',NoEnvironment()), patch.object(os,'getenv',forbidden), \
         patch.object(socket,'create_connection',forbidden), patch.object(socket.socket,'connect',forbidden), \
         patch.object(subprocess,'Popen',forbidden), patch.object(os,'system',forbidden):
        suite = unittest.defaultTestLoader.loadTestsFromModule(test_bridge)
        stream = io.StringIO()
        result = unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    # Tests catching errors cannot silently hide attempted network/credential I/O.
    report = dict(tests=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                  skipped=len(result.skipped), forbidden_attempts=len(attempts),
                  real_provider_calls=0, evidence_class='OFFLINE_TEST_ONLY', real_authority_consumption=0)
    log = '\n'.join(line for line in stream.getvalue().splitlines() if not line.startswith('Ran '))+'\n'
    (ROOT/'TEST-LOG.txt').write_text(log)
    (ROOT/'TEST-RESULTS.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(log)
    print(json.dumps(report,sort_keys=True))
    if not result.wasSuccessful() or attempts:
        raise SystemExit(1)
