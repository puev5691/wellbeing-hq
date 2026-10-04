from __future__ import annotations
from copy import deepcopy
from sece_simulator import ClosedSchemaValidator, SchemaError

def run_schema_minimum_tests(fixture_schema: dict) -> dict:
    assertion_schema = fixture_schema["$defs"]["Assertion"]
    base = {
        "assertion_type": "SECONDARY_REASONS_COUNT",
        "subject_ref": None,
        "scope": None,
        "expected_state": None,
        "expected_ref": None,
        "expected_bool": None,
        "expected_count": 0,
    }
    v = ClosedSchemaValidator(fixture_schema)
    v.validate(base, assertion_schema)
    below = deepcopy(base)
    below["expected_count"] = -1
    rejected = False
    try:
        v.validate(below, assertion_schema)
    except SchemaError as exc:
        rejected = ":minimum" in str(exc)
    return {
        "below_minimum_rejected": rejected,
        "exact_minimum_accepted": True,
        "REVIEWED_SCHEMA_MINIMUM_SUPPORT_FIXED": rejected,
    }
