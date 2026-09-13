#!/usr/bin/env python3
"""A dependency-free session timer and monitor.

This utility measures the time for which it is running. It does not keep a
remote server alive, reconnect SSH, or bypass provider limits.
"""

from __future__ import annotations

import argparse
import logging
import signal
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


VERSION = "1.0.0"
DEFAULT_INTERVAL = 1.0


@dataclass
class Session:
    """State for one timer session."""

    started_at: datetime
    started_monotonic: float
    stopped_at: Optional[datetime] = None
    stopped_monotonic: Optional[float] = None

    @property
    def elapsed_seconds(self) -> float:
        """Return elapsed seconds using a monotonic clock."""
        end = self.stopped_monotonic or time.monotonic()
        return max(0.0, end - self.started_monotonic)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Display and optionally log the elapsed time of a local session. "
            "This does not keep remote servers alive."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=DEFAULT_INTERVAL,
        metavar="SECONDS",
        help="How often to refresh the timer.",
    )
    parser.add_argument(
        "--log",
        type=Path,
        metavar="FILE",
        help="Append session start and stop events to FILE.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        metavar="HOURS",
        help="Stop automatically after the specified number of hours.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Do not refresh the terminal; print only the final summary.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"session_timer {VERSION}",
    )
    return parser


def validate_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> None:
    if args.interval <= 0:
        parser.error("--interval must be greater than 0")
    if args.hours is not None and args.hours <= 0:
        parser.error("--hours must be greater than 0")


def format_duration(seconds: float) -> str:
    """Format seconds as HH:MM:SS, preserving days when necessary."""
    total_seconds = max(0, int(seconds))
    days, remainder = divmod(total_seconds, 86_400)
    hours, remainder = divmod(remainder, 3_600)
    minutes, secs = divmod(remainder, 60)
    if days:
        return f"{days}d {hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def utc_timestamp(value: datetime) -> str:
    """Return an ISO 8601 timestamp in UTC."""
    return value.astimezone(timezone.utc).isoformat(timespec="seconds")


def append_log(path: Optional[Path], message: str) -> None:
    if path is None:
        return
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as logfile:
            logfile.write(f"{message}\n")
    except OSError as exc:
        logging.error("Could not write log file %s: %s", path, exc)


def install_signal_handlers(stop: dict[str, bool]) -> None:
    def request_stop(signum: int, _frame: object) -> None:
        stop["requested"] = True
        if signum == signal.SIGINT:
            print("\nStopping session timer...", file=sys.stderr)

    signal.signal(signal.SIGINT, request_stop)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, request_stop)


def display_progress(session: Session, quiet: bool) -> None:
    if quiet:
        return
    message = f"Elapsed: {format_duration(session.elapsed_seconds)}"
    print(message.ljust(32), end="\r", flush=True)


def run(args: argparse.Namespace) -> int:
    session = Session(
        started_at=datetime.now(timezone.utc),
        started_monotonic=time.monotonic(),
    )
    stop = {"requested": False}
    install_signal_handlers(stop)

    started_message = f"Session started: {utc_timestamp(session.started_at)}"
    append_log(args.log, started_message)

    if not args.quiet:
        print(started_message)
        print("Press Ctrl+C to stop.")

    try:
        while not stop["requested"]:
            display_progress(session, args.quiet)
            if args.hours is not None and session.elapsed_seconds >= args.hours * 3_600:
                break
            time.sleep(args.interval)
    except KeyboardInterrupt:
        stop["requested"] = True
    finally:
        session.stopped_at = datetime.now(timezone.utc)
        session.stopped_monotonic = time.monotonic()

    stopped_message = f"Session stopped: {utc_timestamp(session.stopped_at)}"
    duration = format_duration(session.elapsed_seconds)
    append_log(args.log, f"{stopped_message} | Duration: {duration}")

    if not args.quiet:
        print(" " * 32, end="\r")
    print(f"{stopped_message}")
    print(f"Total duration: {duration}")
    if args.log:
        print(f"Log file: {args.log}")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    validate_args(args, parser)
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
