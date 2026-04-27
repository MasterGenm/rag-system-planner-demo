from __future__ import annotations

import io
from pathlib import Path

from scripts import check_freshness


def run_check(as_of: str) -> tuple[int, str]:
    stdout = io.StringIO()
    result = check_freshness.check_freshness(
        check_freshness.date.fromisoformat(as_of),
        stdout=stdout,
    )
    return result, stdout.getvalue()


def test_all_targets_are_fresh_on_validation_date():
    result, output = run_check("2026-04-27")

    assert result == 0
    assert output.count("status=ok") == 6
    assert "stale_files=0" in output


def test_180_day_targets_are_stale_in_2027():
    result, output = run_check("2027-04-27")

    assert result == 1
    assert "skills/rag-system-planner/SKILL.md" in output
    assert "cursor/rules/rag-system-planner.mdc" in output
    assert "docs/freshness-policy.md" in output
    assert "status=stale" in output


def test_365_day_targets_are_stale_by_end_of_2027():
    result, output = run_check("2027-12-31")

    assert result == 1
    assert "cases/CASE-0001-court-logic.md" in output
    assert "cases/CASE-0002-stackademic-rag-done-right.md" in output
    assert "cases/CASE-0003-lettria-graphrag.md" in output
    assert output.count("status=stale") == 6


def test_missing_frontmatter_file_is_silently_skipped(tmp_path, monkeypatch):
    fake_file = tmp_path / "no-frontmatter.md"
    fake_file.write_text("# no metadata\n", encoding="utf-8")
    monkeypatch.setattr(check_freshness, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(check_freshness, "TARGET_FILES", [Path("no-frontmatter.md")])

    result, output = run_check("2027-12-31")

    assert result == 0
    assert output == "stale_files=0\n"
