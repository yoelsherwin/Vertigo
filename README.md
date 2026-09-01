# Vertigo

Vertigo will be an adversarial testing framework for stateful, tool-wielding LLM
agents. The repository currently contains only a hello-world CLI and the
development workflow that future product milestones must use.

## Prerequisite

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/). Vertigo
uses the Python version and locked dependencies declared in this repository.

## First run

```console
uv run --frozen vertigo hello
```

Expected output:

```text
Hello, Vertigo!
```

Run the same deterministic checks used by CI:

```console
uv run --frozen poe check
```

Run the network-dependent dependency audit separately:

```console
uv run --frozen poe audit
```

## Development

- [`CONTRIBUTING.md`](CONTRIBUTING.md): authoritative development workflow.
- [`AGENTS.md`](AGENTS.md): authoritative instructions for coding agents.
- [`ARCHITECTURE.md`](ARCHITECTURE.md): implemented system boundaries.
- [`docs/specs`](docs/specs): accepted behavior and milestone contracts.
- [`docs/plans`](docs/plans): dependency-ordered implementation plans.
- [`docs/adr`](docs/adr): durable architectural decisions.

## GitHub-hosted setup

The checkout cannot enforce repository settings. After the repository is hosted,
configure these controls explicitly:

1. Protect the default branch and require the cross-platform `Checks` jobs.
2. Require pull requests and an independent approval for normal and high-risk
   changes.
3. Enable Copilot automatic pull-request review if the repository's plan
   supports it.
4. Enable secret scanning and push protection if repository visibility and
   licensing support them.
5. Enable CodeQL default setup when available.

These hosted controls are **not enforced by this checkout**. Local and CI static
security linting is enforced by `poe check`.
