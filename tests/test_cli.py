"""Tests for the thin rag-planner CLI runner."""

from __future__ import annotations

import io
import json
import sys

from cli import rag_planner


def run_cli(monkeypatch, capsys, argv, stdin_text: str | None = None):
    if stdin_text is not None:
        monkeypatch.setattr(sys, "stdin", io.StringIO(stdin_text))
    result = rag_planner.main(argv)
    captured = capsys.readouterr()
    return result, captured


def test_plan_renders_markdown_from_stdin(monkeypatch, capsys):
    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["plan", "--input", "-"],
        '{"title":"x"}',
    )

    assert result == 0
    assert captured.out == "# x\n"
    assert captured.err == ""


def test_diagnose_renders_markdown_from_file(fixtures_dir, monkeypatch, capsys):
    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["diagnose", "--input", str(fixtures_dir / "diagnostic_minimal.json")],
    )

    assert result == 0
    assert captured.out == "# Minimal Diagnostic\n"
    assert captured.err == ""


def test_validate_success_is_silent(monkeypatch, capsys):
    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["validate", "--input", "-", "--mode", "plan"],
        '{"title":"x"}',
    )

    assert result == 0
    assert captured.out == ""
    assert captured.err == ""


def test_validate_schema_error_returns_two_and_path(monkeypatch, capsys):
    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["validate", "--input", "-", "--mode", "plan"],
        '{"title":"x","unknown_key":1}',
    )

    assert result == 2
    assert captured.out == ""
    assert "$:" in captured.err
    assert "unknown_key" in captured.err


def test_plan_schema_error_does_not_render(monkeypatch, capsys):
    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["plan", "--input", "-"],
        '{"title":"x","unknown_key":1}',
    )

    assert result == 2
    assert captured.out == ""
    assert "unknown_key" in captured.err


def test_output_file_suppresses_stdout(monkeypatch, capsys, tmp_path):
    output_path = tmp_path / "nested" / "plan.md"

    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["plan", "--input", "-", "--output", str(output_path)],
        '{"title":"x"}',
    )

    assert result == 0
    assert captured.out == ""
    assert output_path.read_bytes() == b"# x\n"


def test_run_log_appends_t7_fields(monkeypatch, capsys, tmp_path):
    log_path = tmp_path / "runs" / "r.jsonl"

    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["plan", "--input", "-", "--run-log", str(log_path)],
        '{"title":"x"}',
    )

    assert result == 0
    assert captured.out == "# x\n"
    records = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
    assert len(records) == 1
    record = records[0]
    assert set(record) == {
        "run_id",
        "timestamp",
        "mode",
        "input_sha256",
        "input_path",
        "output_sha256",
        "output_path",
        "schema_version",
        "cli_version",
    }
    assert record["mode"] == "plan"
    assert record["input_path"] == "stdin"
    assert record["output_path"] == "stdout"
    assert record["schema_version"] == "1"
    assert record["cli_version"] == "0.0.0"


def test_invalid_json_returns_two(monkeypatch, capsys):
    result, captured = run_cli(
        monkeypatch,
        capsys,
        ["validate", "--input", "-", "--mode", "plan"],
        "{",
    )

    assert result == 2
    assert captured.out == ""
    assert "Invalid JSON" in captured.err
