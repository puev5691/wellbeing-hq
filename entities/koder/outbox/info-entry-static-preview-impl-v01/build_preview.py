from pathlib import Path
from static_preview import build
if __name__=='__main__': print(build(Path(__file__).resolve().parent,True)['deterministic_identity'])
