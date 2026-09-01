"""Command-line interface."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vertigo")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("hello", help="Print the bootstrap greeting")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the Vertigo CLI."""
    _parser().parse_args(argv)
    sys.stdout.buffer.write(b"Hello, Vertigo!\n")
    return 0
