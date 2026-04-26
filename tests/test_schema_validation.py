"""JSON Schema validation tests for renderer inputs."""

import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
FIXTURE_DIR = ROOT / "tests" / "fixtures"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def plan_schema():
    return load_json(SCHEMA_DIR / "plan_input.schema.json")


@pytest.fixture(scope="module")
def diagnostic_schema():
    return load_json(SCHEMA_DIR / "diagnostic_input.schema.json")


def test_schemas_are_valid_draft_2020_12(plan_schema, diagnostic_schema):
    jsonschema.Draft202012Validator.check_schema(plan_schema)
    jsonschema.Draft202012Validator.check_schema(diagnostic_schema)


@pytest.mark.parametrize(
    ("fixture_name", "schema_fixture"),
    [
        ("plan_minimal.json", "plan_schema"),
        ("plan_full.json", "plan_schema"),
        ("diagnostic_minimal.json", "diagnostic_schema"),
        ("diagnostic_full.json", "diagnostic_schema"),
    ],
)
def test_t1_fixtures_validate_against_schema(fixture_name, schema_fixture, request):
    schema = request.getfixturevalue(schema_fixture)
    payload = load_json(FIXTURE_DIR / fixture_name)

    jsonschema.Draft202012Validator(schema).validate(payload)


@pytest.mark.parametrize(
    "payload",
    [
        {"title": "x", "unknown_key": 1},
        {"title": "x", "assumptions": "should be an array"},
        {"title": "x", "rollout": {"Phase 9": ["invalid phase"]}},
    ],
)
def test_plan_schema_rejects_invalid_payloads(plan_schema, payload):
    validator = jsonschema.Draft202012Validator(plan_schema)

    with pytest.raises(jsonschema.ValidationError):
        validator.validate(payload)


@pytest.mark.parametrize(
    "payload",
    [
        {"title": "x", "unknown_key": 1},
        {"title": "x", "symptoms": "should be an array"},
        {"title": "x", "hypotheses": {"guessed": ["invalid label"]}},
        {"title": "x", "recommended_changes": {"soon": ["invalid priority"]}},
    ],
)
def test_diagnostic_schema_rejects_invalid_payloads(diagnostic_schema, payload):
    validator = jsonschema.Draft202012Validator(diagnostic_schema)

    with pytest.raises(jsonschema.ValidationError):
        validator.validate(payload)
