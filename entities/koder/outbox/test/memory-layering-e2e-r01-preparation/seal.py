"""Deterministic payload manifest/checksum generator. No execution."""
import hashlib,json
from pathlib import Path
def encoded(x): return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def seal(root):
    root=Path(root); files=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.name in ('MANIFEST.json','SHA256SUMS.txt'): continue
        if '__pycache__' in p.parts: raise ValueError('unexpected bytecode artifact')
        b=p.read_bytes(); name=str(p.relative_to(root))
        files.append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'artifact_identity':'MLPREP-R01:'+name,'producer':'KOD-preparation','normative_status':'approved-source-copy' if name.startswith('sources/') else 'test-candidate','purpose':name.split('/')[0],'source_ref':'provenance/basis.json; source copies: recovery/mandatory-sources.json'})
    m={'schema':'MLPREP-MANIFEST-R01','scenario_id':'ML-E2E-DESIGN-R01','main_attempts':0,'root_identity':'external immutable Git commit + package subtree; supplied by publication result','files':files}
    b=encoded(m);(root/'MANIFEST.json').write_bytes(b)
    hashes={x['path']:x['sha256'] for x in files};hashes['MANIFEST.json']=hashlib.sha256(b).hexdigest()
    (root/'SHA256SUMS.txt').write_text(''.join(hashes[k]+'  '+k+'\n' for k in sorted(hashes)))
if __name__=='__main__': seal(Path(__file__).parent)
