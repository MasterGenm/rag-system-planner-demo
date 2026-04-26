"""Regression tests for the RAG plan renderer."""

import io
import json
import sys
from pathlib import Path

import pytest

import render_rag_plan


def invoke_plan(monkeypatch, capsys, args, stdin_text: str | None = None):
    monkeypatch.setattr(sys, "argv", ["render_rag_plan.py", *args])
    if stdin_text is not None:
        monkeypatch.setattr(sys, "stdin", io.StringIO(stdin_text))
    result = render_rag_plan.main()
    captured = capsys.readouterr()
    return result, captured


def test_full_payload_matches_expected(fixtures_dir, expected_dir, monkeypatch, capsys):
    result, captured = invoke_plan(
        monkeypatch,
        capsys,
        ["--input", str(fixtures_dir / "plan_full.json")],
    )

    assert result == 0
    assert captured.out == (expected_dir / "plan_full.md").read_text(encoding="utf-8")


def test_minimal_payload_renders_only_title(fixtures_dir, expected_dir, monkeypatch, capsys):
    result, captured = invoke_plan(
        monkeypatch,
        capsys,
        ["--input", str(fixtures_dir / "plan_minimal.json")],
    )

    assert result == 0
    assert captured.out == (expected_dir / "plan_minimal.md").read_text(encoding="utf-8")
    assert "## " not in captured.out


def test_missing_sections_do_not_render_empty_headings(monkeypatch, capsys):
    payload = {"title": "Partial Plan", "problem_summary": "Only one section."}

    result, captured = invoke_plan(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert "## Problem Summary" in captured.out
    assert "## Recommended Stack" not in captured.out
    assert "## Phased Rollout Plan" not in captured.out


def test_nested_dict_heading_level_never_exceeds_six(monkeypatch, capsys):
    payload = {
        "title": "Deep Plan",
        "rollout": {
            "Phase 1": {
                "A": {
                    "B": {
                        "C": {
                            "D": {
                                "E": ["done"],
                            }
                        }
                    }
                }
            }
        },
    }

    result, captured = invoke_plan(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert "###### E" in captured.out
    assert "#######" not in captured.out


def test_rollout_keys_are_ordered_by_priority(monkeypatch, capsys):
    payload = {
        "title": "Ordered Plan",
        "rollout": {
            "Phase 2": ["two"],
            "Phase 0": ["zero"],
            "Phase 1": ["one"],
        },
    }

    result, captured = invoke_plan(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert captured.out.index("### Phase 0") < captured.out.index("### Phase 1")
    assert captured.out.index("### Phase 1") < captured.out.index("### Phase 2")


def test_non_dict_top_level_raises_system_exit(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc_info:
        invoke_plan(monkeypatch, capsys, [], "[]")

    assert "Expected a JSON object" in str(exc_info.value)


def test_invalid_json_raises_system_exit(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc_info:
        invoke_plan(monkeypatch, capsys, [], "{")

    assert "Invalid JSON" in str(exc_info.value)


def test_missing_input_file_raises_system_exit(monkeypatch, capsys, tmp_path):
    missing = tmp_path / "missing.json"

    with pytest.raises(SystemExit) as exc_info:
        invoke_plan(monkeypatch, capsys, ["--input", str(missing)])

    assert "Input file not found" in str(exc_info.value)


def test_output_file_is_utf8_without_bom_and_single_trailing_newline(
    fixtures_dir,
    monkeypatch,
    capsys,
    tmp_path,
):
    output_path = tmp_path / "nested" / "plan.md"

    result, captured = invoke_plan(
        monkeypatch,
        capsys,
        ["--input", str(fixtures_dir / "plan_minimal.json"), "--output", str(output_path)],
    )

    data = output_path.read_bytes()
    assert result == 0
    assert captured.out == ""
    assert data == b"# Minimal Plan\n"
    assert not data.startswith(b"\xef\xbb\xbf")
    assert data.endswith(b"\n")
    assert not data.endswith(b"\n\n")
