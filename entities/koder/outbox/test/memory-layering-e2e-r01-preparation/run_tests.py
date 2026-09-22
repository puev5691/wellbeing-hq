"""Guarded offline self-tests; never creates OLD/NEW processes."""
import sys,os,json,unittest,tempfile,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
scratch=tempfile.TemporaryDirectory(prefix='mlprep-tests-');tempfile.tempdir=scratch.name
# Test cleanup uses absolute paths so audit events can be resolved without
# silently treating dir_fd-relative opens as cwd-relative file access.
shutil._use_fd_functions=False
denied=[]
def audit(event,args):
    if event.startswith(('socket.','subprocess.','os.exec','os.spawn','os.fork','os.system')):
        denied.append(event);raise RuntimeError('OFFLINE_CAPABILITY_DENIED')
    if event=='open' and isinstance(args[0],(str,bytes)):
        p=Path(os.fsdecode(args[0])).resolve()
        allowed=[ROOT,Path(scratch.name),Path(sys.base_prefix)]
        if not any(p.is_relative_to(a) for a in allowed):
            denied.append('open-outside');raise RuntimeError('OFFLINE_FILE_DENIED')
sys.addaudithook(audit)
import test_preparation
suite=unittest.defaultTestLoader.loadTestsFromModule(test_preparation)
result=unittest.TestResult();suite.run(result)
report={'evidence_class':'OFFLINE_PREPARATION_SELF_TEST','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'forbidden_attempts':denied,'main_e2e_attempts':0,'old_new_processes_started':0,'provider_calls':0,'runtime_isolation_proven':False}
print(json.dumps(report,sort_keys=True))
if result.failures or result.errors:
    for _,msg in result.failures+result.errors:print(msg)
sys.exit(0 if result.wasSuccessful() and not denied else 1)
