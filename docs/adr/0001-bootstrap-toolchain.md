# ADR 0001: Bootstrap Toolchain

**Status:** Accepted  
**Date:** 2026-09-01

## Context

The empty repository needs a reproducible, cross-platform Python workflow without
introducing product architecture or runtime dependencies.

## Decision

- Use Python 3.13 and a `src` package layout.
- Use `uv` for Python installation, dependency locking, and command execution.
- Use standard-library `argparse` for the bootstrap CLI.
- Use Ruff, mypy, pytest/coverage, and build as deterministic checks.
- Use Poe only to expose one cross-platform task shared by developers and CI.
- Run `pip-audit` separately because its advisory data changes over time.

## Consequences

The lockfile and one command make local and CI behavior consistent. Poe adds one
development dependency, but avoids platform-specific shell scripts. Future
runtime dependencies require a product need and an accepted design decision.
