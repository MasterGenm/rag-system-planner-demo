"""Check freshness metadata in long-lived project documents."""

from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import TextIO


REPO_ROOT = Path(__file__).resolve().parents[1]

TARGET_FILES = [
    Path("skills/rag-system-planner/SKILL.md"),
    Path("cursor/rules/rag-system-planner.mdc"),
    Path("docs/freshness-policy.md"),
    Path("cases/CASE-0001-court-logic.md"),
    Path("cases/CASE-0002-stackademic-rag-done-right.md"),
    Path("cases/CASE-0003-lettria-graphrag.md"),
]


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return None

    if not lines or lines[0] != "---":
        return None

    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return None

    metadata: dict[str, str] = {}
    for line in lines[1:end_index]:
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata


def freshness_status(metadata: dict[str, str], as_of: date) -> tuple[date, str]:
    last_validated = date.fromisoformat(metadata["last_validated_at"])
    stale_after_days = int(metadata["stale_after_days"])
    due = last_validated + timedelta(days=stale_after_days)
    status = "stale" if due < as_of else "ok"
    return due, status


def check_freshness(as_of: date, stdout: TextIO) -> int:
    stale_files = 0
    for relative_path in TARGET_FILES:
        path = REPO_ROOT / relative_path
        metadata = parse_frontmatter(path)
        if metadata is None:
            continue

        due, status = freshness_status(metadata, as_of)
        if status == "stale":
            stale_files += 1

        print(
            f"{relative_path.as_posix()}: "
            f"last_validated={metadata['last_validated_at']} "
            f"stale_after={metadata['stale_after_days']}d "
            f"due={due.isoformat()} "
            f"status={status}",
            file=stdout,
        )

    print(f"stale_files={stale_files}", file=stdout)
    return 1 if stale_files else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check freshness metadata.")
    parser.add_argument("--as-of", required=True, help="Date in YYYY-MM-DD format.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return check_freshness(date.fromisoformat(args.as_of), stdout=sys.stdout)


if __name__ == "__main__":
    raise SystemExit(main())
