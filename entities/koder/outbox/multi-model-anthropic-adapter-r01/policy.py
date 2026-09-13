from __future__ import annotations
from dataclasses import dataclass
import hashlib, json, re
from typing import Any, Mapping

ADAPTER_VERSION="anthropic-direct-adapter-r01"
PROVIDER="anthropic"
MODEL="claude-sonnet-5"
DATA_CLASS="D0_SYNTHETIC"
ENDPOINT="https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION="2023-06-01"
CREDENTIAL_ENV="ANTHROPIC_API_KEY"
MAX_PILOT_TOKENS=1024

class PolicyViolation(ValueError): pass

def canonical_json(v:Any)->str:
    return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))
def sha256_json(v:Any)->str:
    return hashlib.sha256(canonical_json(v).encode()).hexdigest()
def sha256_text(v:str)->str:
    return hashlib.sha256(v.encode()).hexdigest()

_CK=re.compile(r"(^|[_-])(api[_-]?key|token|secret|password|passwd|private[_-]?key|bearer|cookie|credential|session)([_-]|$)",re.I)
_CV=(re.compile(r"^sk-[A-Za-z0-9_-]{8,}$"),re.compile(r"^Bearer\s+\S+",re.I),re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),re.compile(r"(?i)(?:api[_-]?key|token|secret|password)\s*[:=]\s*\S+"))
_PRIVATE=("github.com/puev5691/wellbeing-hq","entities/","routes/","registry/","/data/wellbeing","/storage/emulated/0/documents/obs","file://")
_SAFE_TASK=re.compile(r"^syn-[a-z0-9][a-z0-9._-]{2,63}$")

def _walk(v:Any,path:str="$"):
    if isinstance(v,Mapping):
        for k,c in v.items():
            yield f"{path}.{k}",k
            yield from _walk(c,f"{path}.{k}")
    elif isinstance(v,(list,tuple)):
        for i,c in enumerate(v): yield from _walk(c,f"{path}[{i}]")
    else: yield path,v

def _reject_credentials(v:Any)->None:
    for path,item in _walk(v):
        leaf=path.rsplit(".",1)[-1]
        if path!="$" and _CK.search(leaf): raise PolicyViolation("credential_like_field_forbidden")
        if isinstance(item,str) and any(p.search(item) for p in _CV): raise PolicyViolation("credential_like_value_forbidden")

def _false(c:Mapping[str,Any],field:str)->None:
    if c.get(field) is not False: raise PolicyViolation(f"{field}_must_be_false")
def _locator(v:Any)->str:
    if not isinstance(v,str) or not v: raise PolicyViolation("synthetic_locator_required")
    if not (v.startswith("synthetic://") or v.startswith("fixture://")): raise PolicyViolation("project_or_private_locator_forbidden")
    lo=v.lower()
    if any(x in lo for x in _PRIVATE) or "http://" in lo or "https://" in lo: raise PolicyViolation("project_or_private_locator_forbidden")
    return v

def credential_contract()->dict[str,Any]:
    return {"kind":"environment_secret_injection","environment_variable":CREDENTIAL_ENV,"secret_value_stored":False,"secret_value_logged":False,"secret_value_in_provenance":False}

@dataclass(frozen=True)
class GuardDecision:
    decision:str
    normalized:dict[str,Any]

class PolicyGuard:
    required=frozenset({"task_id","data_class","input_locator","synthetic_text","provider","model","max_tokens","tools_allowed","search_allowed","files_allowed","caching_allowed","mcp_allowed","managed_agents_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed"})
    def evaluate(self,c:Mapping[str,Any])->GuardDecision:
        if not isinstance(c,Mapping): raise PolicyViolation("config_must_be_object")
        _reject_credentials(c)
        missing=self.required-set(c); unknown=set(c)-self.required
        if missing: raise PolicyViolation("missing_fields:"+",".join(sorted(missing)))
        if unknown: raise PolicyViolation("unknown_fields:"+",".join(sorted(unknown)))
        if not isinstance(c["task_id"],str) or not _SAFE_TASK.fullmatch(c["task_id"]): raise PolicyViolation("synthetic_task_id_required")
        if c["data_class"]!=DATA_CLASS: raise PolicyViolation("data_class_must_be_D0_SYNTHETIC")
        if c["provider"]!=PROVIDER: raise PolicyViolation("unknown_provider")
        if c["model"]!=MODEL: raise PolicyViolation("unknown_model")
        locator=_locator(c["input_locator"]); text=c["synthetic_text"]
        if not isinstance(text,str) or not text or len(text.encode())>32768: raise PolicyViolation("bounded_synthetic_text_required")
        lo=text.lower()
        if any(x in lo for x in _PRIVATE): raise PolicyViolation("project_or_private_data_forbidden")
        mt=c["max_tokens"]
        if not isinstance(mt,int) or isinstance(mt,bool) or not 1<=mt<=MAX_PILOT_TOKENS: raise PolicyViolation("max_tokens_out_of_D0_pilot_bounds")
        flags=("tools_allowed","search_allowed","files_allowed","caching_allowed","mcp_allowed","managed_agents_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed")
        for f in flags:_false(c,f)
        n={"task_id":c["task_id"],"data_class":DATA_CLASS,"input_locator":locator,"synthetic_text":text,"synthetic_text_sha256":sha256_text(text),"provider":PROVIDER,"model":MODEL,"max_tokens":mt}
        n.update({f:False for f in flags})
        return GuardDecision("PASS_D0_SYNTHETIC_MOCK_ONLY",n)

def valid_synthetic_config(text:str="Return exactly the word SYNTHETIC.")->dict[str,Any]:
    c={"task_id":"syn-anthropic-001","data_class":DATA_CLASS,"input_locator":"fixture://anthropic-d0-r01","synthetic_text":text,"provider":PROVIDER,"model":MODEL,"max_tokens":64}
    for f in ("tools_allowed","search_allowed","files_allowed","caching_allowed","mcp_allowed","managed_agents_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed"):c[f]=False
    return c
