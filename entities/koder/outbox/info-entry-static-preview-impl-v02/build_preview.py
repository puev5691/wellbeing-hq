from pathlib import Path
from static_preview import build
from post_build_readback import verify
if __name__=="__main__":
    base=Path(__file__).resolve().parent
    state=build(base,True)
    ident=state["expected_preview_identity"]
    report=verify(base,ident["git_blob"],ident["sha256"],True)
    if report["status"]!="PASS":raise SystemExit(2)
    print(report["observed_preview_identity"]["git_blob"])
