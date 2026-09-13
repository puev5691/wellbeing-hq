import json, re, sys
from pathlib import Path

SECRET_RE = re.compile(r"(api[_-]?key|token|secret|password)\s*[:=]\s*[A-Za-z0-9_\-]{8,}", re.I)

STRING_FIELDS = {
    "id", "title", "immutable_identity", "semantic_status", "editorial_status",
    "public_legal_outcome", "security_state", "representation_state", "release_state",
}
BOOLEAN_FIELDS = {"secret_dependency", "public_legal_conditions_satisfied"}
NULL_OR_STRING_FIELDS = {"superseded_by"}

def load_schema(base):
    return json.loads((base / "schema.json").read_text(encoding="utf-8"))

def validate_object(obj, schema):
    errors = []
    if not isinstance(obj, dict):
        return {"public_ready": False, "errors": ["invalid_type:root"]}

    required = set(schema["required"])
    allowed = set(schema["allowed_properties"])

    for k in schema["required"]:
        if k not in obj:
            errors.append(f"missing:{k}")

    for k in obj:
        if k not in allowed:
            errors.append(f"unknown_key:{k}")

    for k in STRING_FIELDS:
        if k in obj and not isinstance(obj[k], str):
            errors.append(f"invalid_type:{k}")
    for k in BOOLEAN_FIELDS:
        if k in obj and type(obj[k]) is not bool:
            errors.append(f"invalid_type:{k}")
    for k in NULL_OR_STRING_FIELDS:
        if k in obj and obj[k] is not None and not isinstance(obj[k], str):
            errors.append(f"invalid_type:{k}")

    # Type validation is a hard prerequisite. Semantic gates are not evaluated
    # against malformed values because Python truthiness/equality can hide type errors.
    if any(e.startswith("invalid_type:") or e.startswith("unknown_key:") or e.startswith("missing:") for e in errors):
        return {"public_ready": False, "errors": errors}

    for k, vals in schema["enums"].items():
        if k in obj and obj[k] not in vals:
            errors.append(f"invalid:{k}:{obj[k]}")

    serialized = json.dumps(obj, ensure_ascii=False)
    if SECRET_RE.search(serialized):
        errors.append("secret_like_material")
    if obj.get("secret_dependency") is True:
        errors.append("secret_dependency")
    if obj.get("security_state") in {"blocked_secret", "requires_SIS_review", "unknown"}:
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
    if obj.get("semantic_status") not in {"current", "accepted"}:
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
