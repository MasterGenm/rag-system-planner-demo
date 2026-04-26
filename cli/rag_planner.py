"""Thin CLI runner for validating and rendering RAG planner payloads."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
import hashlib
import json
from json import JSONDecodeError
from pathlib import Path
import sys
from uuid import uuid4

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
SCRIPTS_DIR = ROOT / "skills" / "rag-system-planner" / "scripts"
SCHEMA_VERSION = "1"
CLI_VERSION = "0.0.0"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import render_rag_diagnostic  # noqa: E402
import render_rag_plan  # noqa: E402


class CliError(Exception):
    def __init__(self, message: str, exit_code: int = 2) -> None:
        super().__init__(message)
        self.exit_code = exit_code


def load_schema(mode: str) -> dict:
    schema_name = "plan_input.schema.json" if mode == "plan" else "diagnostic_input.schema.json"
    return json.loads((SCHEMA_DIR / schema_name).read_text(encoding="utf-8"))


def read_input(input_arg: str) -> tuple[str, str]:
    if input_arg == "-":
        return sys.stdin.read(), "stdin"

    path = Path(input_arg)
    try:
        return path.read_text(encoding="utf-8"), str(path)
    except FileNotFoundError as exc:
        raise CliError(f"$: Input file not found: {exc.filename}") from exc


def parse_payload(raw: str) -> dict:
    try:
        payload = json.loads(raw)
    except JSONDecodeError as exc:
        raise CliError(f"$: Invalid JSON: {exc}") from exc

    if not isinstance(payload, dict):
        raise CliError("$: Expected a JSON object at the top level.")
    return payload


def error_path(error: jsonschema.ValidationError) -> str:
    if not error.absolute_path:
        return "$"
    return "$." + ".".join(str(part) for part in error.absolute_path)


def validate_payload(payload: dict, mode: str) -> list[str]:
    validator = jsonschema.Draft202012Validator(load_schema(mode))
    errors = sorted(validator.iter_errors(payload), key=lambda err: list(err.absolute_path))
    return [f"{error_path(error)}: {error.message}" for error in errors]


def render_payload(payload: dict, mode: str) -> str:
    if mode == "plan":
        title = render_rag_plan.format_heading_text(payload.get("title", "RAG Solution Package"))
        lines = [f"# {title}", ""]
        for key, heading in render_rag_plan.SECTIONS:
            lines.extend(render_rag_plan.render_section(heading, payload.get(key)))
        return "\n".join(lines).strip() + "\n"

    title = render_rag_diagnostic.format_heading_text(payload.get("title", "RAG Diagnostic Report"))
    lines = [f"# {title}", ""]
    for key, heading in render_rag_diagnostic.SECTIONS:
        lines.extend(render_rag_diagnostic.render_section(heading, payload.get(key)))
    return "\n".join(lines).strip() + "\n"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def append_run_log(
    path: str,
    *,
    mode: str,
    raw_input: str,
    input_path: str,
    output: str,
    output_path: str,
) -> None:
    record = {
        "run_id": str(uuid4()),
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "mode": mode,
        "input_sha256": sha256_text(raw_input),
        "input_path": input_path,
        "output_sha256": sha256_text(output),
        "output_path": output_path,
        "schema_version": SCHEMA_VERSION,
        "cli_version": CLI_VERSION,
    }
    log_path = Path(path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def handle_validate(input_arg: str, mode: str) -> int:
    raw, _ = read_input(input_arg)
    payload = parse_payload(raw)
    errors = validate_payload(payload, mode)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 2
    return 0


def handle_render(args: argparse.Namespace, mode: str) -> int:
    raw, input_path = read_input(args.input)
    payload = parse_payload(raw)
    errors = validate_payload(payload, mode)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 2

    output = render_payload(payload, mode)
    output_path = "stdout"
    if args.output:
        output_path = args.output
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(output, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(output)

    if args.run_log:
        append_run_log(
            args.run_log,
            mode=mode,
            raw_input=raw,
            input_path=input_path,
            output=output,
            output_path=output_path,
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rag-planner")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("plan", "diagnose"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--input", required=True, help="Input JSON file, or '-' for stdin.")
        subparser.add_argument("--output", help="Optional Markdown output file.")
        subparser.add_argument("--run-log", help="Optional JSONL run log path.")

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--input", required=True, help="Input JSON file, or '-' for stdin.")
    validate_parser.add_argument("--mode", required=True, choices=["plan", "diagnose"])

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "validate":
            return handle_validate(args.input, args.mode)
        if args.command == "plan":
            return handle_render(args, "plan")
        if args.command == "diagnose":
            return handle_render(args, "diagnose")
    except CliError as exc:
        print(exc, file=sys.stderr)
        return exc.exit_code
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
