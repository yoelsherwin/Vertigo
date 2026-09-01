# Agent Instructions

Before changing code, read the accepted specification, its plan,
[`CONTRIBUTING.md`](CONTRIBUTING.md), and
[`ARCHITECTURE.md`](ARCHITECTURE.md).

## Non-negotiable rules

- Do not implement a draft specification.
- Do not invent future architecture, extension points, or dependencies.
- Treat subagents as optional. Fan out only independent work with stable
  contracts, exclusive ownership, explicit acceptance criteria, and a named
  integrator.
- The implementation owner writes meaningful tests with or before behavior.
  Test specialists look for gaps; they do not replace implementation testing.
- Prefer small builders and local setup over large shared fixtures.
- Keep project coverage at or above 80%, but never add a test only to increase
  coverage.
- Run `uv run --frozen poe check` before LLM review.
- Use correctness review for normal changes and add test-adversary and security
  review when the change risk requires them.
- Update only authoritative documentation. Link instead of copying rules.
- Never place secrets in code, configuration, tests, logs, or reports.

The complete workflow and definition of done live in
[`CONTRIBUTING.md`](CONTRIBUTING.md).
