"""Command-line interface for validation and batch annotation."""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path
from typing import Any

from .client import ClaudeClient, ClaudeClientConfig
from .pipeline import AnnotationPipeline, PipelineConfig
from .storage import read_jsonl
from .validation import validate_job


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sciarp-annotate")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser(
        "validate-input", help="validate JSONL without API calls"
    )
    validate.add_argument("input", type=Path)

    annotate = subparsers.add_parser(
        "annotate", help="run the three-stage annotation pipeline"
    )
    annotate.add_argument(
        "input", type=Path, help="canonical annotation jobs in JSONL format"
    )
    annotate.add_argument(
        "--output", type=Path, required=True, help="checkpoint/output directory"
    )
    annotate.add_argument("--model", default="claude-opus-5")
    annotate.add_argument("--concurrency", type=int, default=4)
    annotate.add_argument("--max-tokens", type=int, default=64_000)
    annotate.add_argument("--max-attempts", type=int, default=5)
    annotate.add_argument("--read-timeout", type=float, default=900.0)
    return parser


def main(argv: list[str] | None = None) -> None:
    args = _parser().parse_args(argv)
    try:
        if args.command == "validate-input":
            count = 0
            job_ids: set[str] = set()
            for line_number, job in read_jsonl(args.input):
                validate_job(job)
                if job["job_id"] in job_ids:
                    raise ValueError(
                        f"line {line_number}: duplicate job_id {job['job_id']}"
                    )
                job_ids.add(job["job_id"])
                count += 1
            print(f"validated {count} job(s)")
            return
        exit_code = asyncio.run(_annotate(args))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    raise SystemExit(exit_code)


async def _annotate(args: argparse.Namespace) -> int:
    if args.concurrency < 1:
        raise ValueError("--concurrency must be positive")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    config = ClaudeClientConfig(
        api_key=api_key,
        model=args.model,
        max_tokens=args.max_tokens,
        read_timeout_seconds=args.read_timeout,
        max_attempts=args.max_attempts,
    )
    jobs: list[dict[str, Any]] = []
    job_ids: set[str] = set()
    for line_number, job in read_jsonl(args.input):
        validate_job(job)
        if job["job_id"] in job_ids:
            raise ValueError(f"line {line_number}: duplicate job_id {job['job_id']}")
        job_ids.add(job["job_id"])
        jobs.append(job)

    semaphore = asyncio.Semaphore(args.concurrency)
    failures: list[tuple[str, str]] = []

    async with ClaudeClient(config) as client:
        pipeline = AnnotationPipeline(client, PipelineConfig(output_dir=args.output))

        async def run_one(job: dict[str, Any]) -> None:
            async with semaphore:
                try:
                    await pipeline.run_job(job)
                    print(f"complete\t{job['job_id']}", flush=True)
                except Exception as exc:  # one bad job must not stop independent jobs
                    failures.append((job["job_id"], str(exc)))
                    print(
                        f"failed\t{job['job_id']}\t{exc}", file=sys.stderr, flush=True
                    )

        await asyncio.gather(*(run_one(job) for job in jobs))

    print(f"summary\tcomplete={len(jobs) - len(failures)}\tfailed={len(failures)}")
    return 1 if failures else 0
