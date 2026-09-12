import json, re, sys
from pathlib import Path

SECRET_RE = re.compile(r"(api[_-]?key|token|secret|password)\s*[:=]\s*[A-Za-z0-9_\-]{8,}", re.I)

def load_schema(base):
    return json.loads((base / "schema.json").read_text(encoding="utf-8"))

def validate_object(obj, schema):
    errors = []
    for k in schema["required"]:
        if k not in obj:
            errors.append(f"missing:{k}")
    for k, vals in schema["enums"].items():
        if k in obj and obj[k] not in vals:
            errors.append(f"invalid:{k}:{obj[k]}")
    serialized = json.dumps(obj, ensure_ascii=False)
    if SECRET_RE.search(serialized):
        errors.append("secret_like_material")
    if obj.get("secret_dependency") is True:
        errors.append("secret_dependency")
    if obj.get("security_state") in {"blocked_secret","requires_SIS_review","unknown"}:
        errors.append(f"security_gate:{obj.get('security_state')}")
    legal = obj.get("public_legal_outcome")
    cond_ok = obj.get("public_legal_conditions_satisfied")
    if legal == "allowed":
        pass
    elif legal == "allowed-with-conditions":
        if cond_ok is not True:
            errors.append("legal_conditions_not_satisfied")
    else:
        errors.append(f"legal_gate:{legal}")
    if obj.get("editorial_status") != "editorial_ready":
        errors.append(f"editorial_gate:{obj.get('editorial_status')}")
    if obj.get("representation_state") != "representation_ready":
        errors.append(f"representation_gate:{obj.get('representation_state')}")
    if obj.get("release_state") != "release_authorized":
        errors.append(f"release_gate:{obj.get('release_state')}")
    if obj.get("semantic_status") not in {"current","accepted"}:
        errors.append(f"semantic_gate:{obj.get('semantic_status')}")
    if obj.get("superseded_by"):
        errors.append("superseded")
    if not obj.get("immutable_identity"):
        errors.append("immutable_identity_missing")
    return {"public_ready": not errors, "errors": errors}

def main():
    base = Path(__file__).resolve().parent
    schema = load_schema(base)
    obj = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    result = validate_object(obj, schema)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(0 if result["public_ready"] else 2)

if __name__ == "__main__":
    main()
