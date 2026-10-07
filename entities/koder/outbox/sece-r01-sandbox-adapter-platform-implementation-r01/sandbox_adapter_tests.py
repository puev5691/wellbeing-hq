import copy, unittest
from sandbox_adapter import *

def platform(**kw):
    d={'profile_id':PLATFORM_ID,'profile_version':PLATFORM_VERSION,'verified_state':'VERIFIED','currentness_state':'CURRENT','conflict_state':'NONE','filename_encoding':'UTF-8','namespace_isolation_class':'PRIVATE_ATTEMPT_OWNED_TMPFS_MOUNT_NAMESPACE','root_identity_class':'DIRFD_STATX_DEV_INO_MNT_ID','created_object_identity_class':'RETAINED_FD_FSTAT_DEV_INO_MNT_ID','cleanup_binding_class':'DIRFD_UNLINKAT_PLUS_EXCLUSIVE_NAMESPACE_MUTATION_CONTROL','capabilities':dict(LinuxPosixProfileR01.required_caps),'supporting_evidence_versions':{'P1':'v1','P2':'v1'},'provenance':['P']}; d.update(kw); return d
def root(**kw):
    d={'sandbox_target_id':'TARGET-CLASS','environment_instance_id':'ENV-1','owner_attempt_id':'A1','explanatory_root_locator':'/not-security','stable_root_object_identity':{'dev':1,'ino':2,'mnt':3},'object_type':'DIRECTORY','ownership_evidence':['O'],'isolation_evidence':['I'],'expected_parent_identity':{'dev':1,'ino':1,'mnt':3},'currentness_evidence_version':'R1','platform_evidence_profile_id':PLATFORM_ID,'verified_state':'VERIFIED','currentness_state':'CURRENT','conflict_state':'NONE','supporting_evidence_versions':{'R1':'v1'}}; d.update(kw); return d
def bind(): return build_binding(leaf='payload-01.bin',root=root(),platform=platform(),adapter_blob='B-ADAPTER',platform_blob='B-PLATFORM')
def created(b): return EphemeralFileSandboxEffectAdapterR01().created_identity({'operation_key':'OP1','attempt_id':'A1','stable_object_identity':{'dev':1,'ino':9,'mnt':3},'open_reference_class':'RETAINED_FD','no_symlink_reparse_evidence':['N'],'ownership_evidence':['A1'],'creation_evidence':['O_EXCL'],'payload_digest':'abc','expected_length':3,'maximum_length':100,'hardlink_replacement_evidence':['NLINK1','EXCLUSIVE']},b)
def cstate(b,c): return {'terminal_effect_evidence_durable':True,'effect_outcome':'EVIDENCED_SUCCESS','root_identity_id':b['root_identity_id'],'parent_identity_unchanged':True,'current_leaf_identity':c['stable_object_identity'],'operation_key':c['operation_key'],'owner_attempt_id':c['attempt_id'],'leaf_regular_file':True,'no_symlink_reparse_substitution':True,'cleanup_scope_separately_bound':True,'confinement_version':'R02','post_mutation_identity_ambiguity':False}
class T(unittest.TestCase):
    def test_name_accept(self): self.assertTrue(leaf_verdict('payload-01.bin')[0])
    def test_name_reject(self):
        for x in ('','.','..','../x','/x',r'a\b','a:b','é.txt','a\x00b'): self.assertFalse(leaf_verdict(x)[0])
    def test_platform_pass(self): self.assertEqual(LinuxPosixProfileR01().validate(platform())['verdict'],'PASS')
    def test_platform_block_openat2(self):
        p=platform(); p['capabilities']['openat2_relative']=False; self.assertEqual(LinuxPosixProfileR01().validate(p)['verdict'],'BLOCKED')
    def test_platform_block_isolation(self): self.assertEqual(LinuxPosixProfileR01().validate(platform(namespace_isolation_class='SHARED'))['verdict'],'BLOCKED')
    def test_binding(self): self.assertEqual(bind()['confinement_id'],CONFINEMENT_ID)
    def test_binding_block_root(self):
        with self.assertRaises(SandboxError): build_binding(leaf='a',root=root(ownership_evidence=[]),platform=platform(),adapter_blob='A',platform_blob='P')
    def test_runtime_binding_pass(self):
        b=bind(); self.assertTrue(runtime_binding_verdict(b,copy.deepcopy(b),b['supporting_evidence_versions'])[0])
    def test_runtime_profile_drift(self):
        b=bind(); c=copy.deepcopy(b); c['platform_version']='R02'; self.assertFalse(runtime_binding_verdict(b,c,b['supporting_evidence_versions'])[0])
    def test_runtime_root_drift(self):
        b=bind(); c=copy.deepcopy(b); c['root_identity_id']='X'; self.assertFalse(runtime_binding_verdict(b,c,b['supporting_evidence_versions'])[0])
    def test_runtime_evidence_drift(self):
        b=bind(); f=dict(b['supporting_evidence_versions']); f['R1']='v2'; self.assertFalse(runtime_binding_verdict(b,b,f)[0])
    def test_pre_effect(self):
        b=bind(); self.assertEqual(EphemeralFileSandboxEffectAdapterR01().pre_effect(b,b,b['supporting_evidence_versions'])['classification'],'READY_FOR_PRIMITIVE_INVOCATION')
    def test_prior_unresolved(self):
        b=bind(); self.assertEqual(EphemeralFileSandboxEffectAdapterR01().pre_effect(b,b,b['supporting_evidence_versions'],'UNRESOLVED')['classification'],'NOT_EXECUTED')
    def test_plan_openat2(self): self.assertTrue(any('openat2' in s['primitive'] for s in EphemeralFileSandboxEffectAdapterR01().plan(bind())))
    def test_outcome_success(self):
        o={k:True for k in ('created_identity_proven','same_object_write','same_object_stat','same_object_readback','same_object_hash','regular_file_proven','no_symlink_reparse_proven','non_replacement_proven','payload_digest_match','length_match')}; o.update(effect_attempted=True,mutation_possible=True); self.assertEqual(EphemeralFileSandboxEffectAdapterR01().classify(o),'EVIDENCED_SUCCESS')
    def test_outcome_unresolved_identity(self): self.assertEqual(EphemeralFileSandboxEffectAdapterR01().classify({'effect_attempted':True,'mutation_possible':True,'created_identity_proven':False}),'UNRESOLVED')
    def test_not_executed(self): self.assertEqual(EphemeralFileSandboxEffectAdapterR01().classify({'effect_attempted':False,'mutation_possible':False}),'NOT_EXECUTED')
    def test_cleanup_eligible(self):
        b=bind(); c=created(b); self.assertEqual(ObjectBoundCleanupR02().eligibility(binding=b,created=c,state=cstate(b,c),platform=platform())['classification'],'ELIGIBLE')
    def test_cleanup_identity_block(self):
        b=bind(); c=created(b); s=cstate(b,c); s['current_leaf_identity']={'ino':99}; self.assertEqual(ObjectBoundCleanupR02().eligibility(binding=b,created=c,state=s,platform=platform())['classification'],'BLOCKED')
    def test_cleanup_exclusive_block(self):
        b=bind(); c=created(b); p=platform(); p['capabilities']['exclusive_namespace_mutation_control']=False; self.assertEqual(ObjectBoundCleanupR02().eligibility(binding=b,created=c,state=cstate(b,c),platform=p)['classification'],'BLOCKED')
    def test_cleanup_unresolved(self):
        b=bind(); c=created(b); s=cstate(b,c); s['post_mutation_identity_ambiguity']=True; self.assertEqual(ObjectBoundCleanupR02().eligibility(binding=b,created=c,state=s,platform=platform())['classification'],'UNRESOLVED')
    def test_post_cleanup(self): self.assertEqual(ObjectBoundCleanupR02().post_cleanup({'exact_leaf_absent':True,'root_identity_unchanged':True,'parent_identity_unchanged':True,'no_unexpected_sibling_parent_mutation':True}),'PASS')
if __name__=='__main__': unittest.main(verbosity=2)
