#!/usr/bin/env python3
"""Render a Markdown RAG diagnostic report from structured JSON input.

Expected input shape:
{
  "title": "RAG Diagnostic Report",
  "symptoms": ["..."],
  "hypotheses": {
    "observed": ["..."],
    "inferred": ["..."],
    "unknown": ["..."]
  },
  "recommended_changes": {
    "now": ["..."],
    "next": ["..."],
    "later": ["..."]
  }
}
"""

import argparse
import json
import sys
from json import JSONDecodeError
from pathlib import Path


SECTIONS = [
    ("symptoms", "Symptom Summary"),
    ("hypotheses", "Working Hypotheses"),
    ("missing_evidence", "Missing Evidence"),
    ("investigation_order", "Investigation Order"),
    ("recommended_changes", "Recommended Changes"),
    ("evaluation_additions", "Evaluation Additions"),
    ("observability_additions", "Observability Additions"),
    ("risks", "Risks And Expected Impact"),
]

ORDER_PRIORITY = {
    "observed": 0,
    "inferred": 1,
    "unknown": 2,
    "now": 10,
    "next": 11,
    "later": 12,
}


def has_content(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return any(has_content(item) for item in value)
    if isinstance(value, dict):
        return any(has_content(item) for item in value.values())
    return bool(str(value).strip())


def ordered_items(value: dict) -> list[tuple[str, object]]:
    items = list(value.items())

    def sort_key(indexed_item: tuple[int, tuple[str, object]]) -> tuple[int, int]:
        index, (key, _) = indexed_item
        priority = ORDER_PRIORITY.get(str(key).strip().lower(), 999)
        return (priority, index)

    return [item for _, item in sorted(enumerate(items), key=sort_key)]


def format_heading_text(value) -> str:
    text = str(value).strip()
    return text or "Details"


def load_payload(input_path: str | None) -> dict:
    try:
        if input_path:
            raw = Path(input_path).read_text(encoding="utf-8")
            payload = json.loads(raw)
        else:
            payload = json.load(sys.stdin)
    except FileNotFoundError as exc:
        raise SystemExit(f"Input file not found: {exc.filename}") from exc
    except JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON input: {exc}") from exc

    if not isinstance(payload, dict):
        raise SystemExit("Expected a JSON object at the top level.")
    return payload


def render_value(value, heading_level: int = 3) -> list[str]:
    lines: list[str] = []
    if not has_content(value):
        return lines

    if isinstance(value, list):
        for item in value:
            if not has_content(item):
                continue
            if isinstance(item, (dict, list)):
                lines.extend(render_value(item, heading_level))
            else:
                lines.append(f"- {str(item).strip()}")
        return lines

    if isinstance(value, dict):
        for key, item in ordered_items(value):
            if not has_content(item):
                continue
            lines.append(f"{'#' * heading_level} {format_heading_text(key)}")
            child_lines = render_value(item, min(heading_level + 1, 6))
            if child_lines:
                lines.extend(child_lines)
        return lines

    lines.append(str(value).strip())
    return lines


def render_section(title: str, value) -> list[str]:
    body = render_value(value)
    if not body:
        return []
    return [f"## {title}", *body, ""]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a Markdown RAG diagnostic report from structured JSON input.",
        epilog='Example: echo {"title":"Diagnostic","symptoms":["..."]} | python render_rag_diagnostic.py',
    )
    parser.add_argument("--input", help="Path to a JSON payload. Defaults to stdin.")
    parser.add_argument("--output", help="Optional path to write the Markdown output.")
    args = parser.parse_args()

    payload = load_payload(args.input)
    title = format_heading_text(payload.get("title", "RAG Diagnostic Report"))

    lines = [f"# {title}", ""]
    for key, heading in SECTIONS:
        lines.extend(render_section(heading, payload.get(key)))

    content = "\n".join(lines).strip() + "\n"
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding="utf-8")
    else:
        sys.stdout.write(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
