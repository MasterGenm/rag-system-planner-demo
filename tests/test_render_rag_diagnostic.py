"""Regression tests for the RAG diagnostic renderer."""

import io
import json
import sys

import pytest

import render_rag_diagnostic


def invoke_diagnostic(monkeypatch, capsys, args, stdin_text: str | None = None):
    monkeypatch.setattr(sys, "argv", ["render_rag_diagnostic.py", *args])
    if stdin_text is not None:
        monkeypatch.setattr(sys, "stdin", io.StringIO(stdin_text))
    result = render_rag_diagnostic.main()
    captured = capsys.readouterr()
    return result, captured


def test_full_payload_matches_expected(fixtures_dir, expected_dir, monkeypatch, capsys):
    result, captured = invoke_diagnostic(
        monkeypatch,
        capsys,
        ["--input", str(fixtures_dir / "diagnostic_full.json")],
    )

    assert result == 0
    assert captured.out == (expected_dir / "diagnostic_full.md").read_text(encoding="utf-8")


def test_minimal_payload_renders_only_title(fixtures_dir, expected_dir, monkeypatch, capsys):
    result, captured = invoke_diagnostic(
        monkeypatch,
        capsys,
        ["--input", str(fixtures_dir / "diagnostic_minimal.json")],
    )

    assert result == 0
    assert captured.out == (expected_dir / "diagnostic_minimal.md").read_text(encoding="utf-8")
    assert "## " not in captured.out


def test_missing_sections_do_not_render_empty_headings(monkeypatch, capsys):
    payload = {"title": "Partial Diagnostic", "symptoms": ["Only symptoms."]}

    result, captured = invoke_diagnostic(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert "## Symptom Summary" in captured.out
    assert "## Recommended Changes" not in captured.out
    assert "## Missing Evidence" not in captured.out


def test_hypotheses_are_ordered_by_priority(monkeypatch, capsys):
    payload = {
        "title": "Ordered Diagnostic",
        "hypotheses": {
            "unknown": ["unknown item"],
            "observed": ["observed item"],
            "inferred": ["inferred item"],
        },
    }

    result, captured = invoke_diagnostic(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert captured.out.index("### observed") < captured.out.index("### inferred")
    assert captured.out.index("### inferred") < captured.out.index("### unknown")


def test_recommended_changes_are_ordered_by_priority(monkeypatch, capsys):
    payload = {
        "title": "Ordered Changes",
        "recommended_changes": {
            "later": ["later item"],
            "now": ["now item"],
            "next": ["next item"],
        },
    }

    result, captured = invoke_diagnostic(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert captured.out.index("### now") < captured.out.index("### next")
    assert captured.out.index("### next") < captured.out.index("### later")


def test_nested_dict_heading_level_never_exceeds_six(monkeypatch, capsys):
    payload = {
        "title": "Deep Diagnostic",
        "risks": {
            "A": {
                "B": {
                    "C": {
                        "D": {
                            "E": {
                                "F": ["done"],
                            }
                        }
                    }
                }
            }
        },
    }

    result, captured = invoke_diagnostic(monkeypatch, capsys, [], json.dumps(payload))

    assert result == 0
    assert "###### F" in captured.out
    assert "#######" not in captured.out


def test_non_dict_top_level_raises_system_exit(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc_info:
        invoke_diagnostic(monkeypatch, capsys, [], '"x"')

    assert "Expected a JSON object" in str(exc_info.value)


def test_invalid_json_raises_system_exit(monkeypatch, capsys):
    with pytest.raises(SystemExit) as exc_info:
        invoke_diagnostic(monkeypatch, capsys, [], "{")

    assert "Invalid JSON" in str(exc_info.value)


def test_missing_input_file_raises_system_exit(monkeypatch, capsys, tmp_path):
    missing = tmp_path / "missing.json"

    with pytest.raises(SystemExit) as exc_info:
        invoke_diagnostic(monkeypatch, capsys, ["--input", str(missing)])

    assert "Input file not found" in str(exc_info.value)


def test_output_file_is_utf8_without_bom_and_single_trailing_newline(
    fixtures_dir,
    monkeypatch,
    capsys,
    tmp_path,
):
    output_path = tmp_path / "nested" / "diagnostic.md"

    result, captured = invoke_diagnostic(
        monkeypatch,
        capsys,
        ["--input", str(fixtures_dir / "diagnostic_minimal.json"), "--output", str(output_path)],
    )

    data = output_path.read_bytes()
    assert result == 0
    assert captured.out == ""
    assert data == b"# Minimal Diagnostic\n"
    assert not data.startswith(b"\xef\xbb\xbf")
    assert data.endswith(b"\n")
    assert not data.endswith(b"\n\n")
