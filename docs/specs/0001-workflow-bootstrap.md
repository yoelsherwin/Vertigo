# Milestone 0: Workflow Bootstrap

**Status:** Accepted  
**Reviewed:** 2026-09-01

## Goal

Create the smallest executable Python project that proves Vertigo's development
workflow and gives new developers and agents an unambiguous starting point.
Milestone 0 builds the delivery system, not the adversarial-testing product.

## Executable contract

The project uses Python 3.13, the standard-library `argparse` parser, a `src`
package layout, and `uv` for environment and dependency management.

`uv run --frozen vertigo hello` must:

- Write exactly `Hello, Vertigo!\n` to stdout.
- Write nothing to stderr.
- Exit with status `0`.

Running without a subcommand or with an unknown subcommand must show argparse
usage on stderr and exit with status `2`.

## Deliverables

### Project

- A `vertigo` Python package and console entry point.
- A committed `.python-version`, `pyproject.toml`, and `uv.lock`.
- Meaningful tests for the executable contract.
- A `.gitignore` for generated Python, test, environment, and build files.

### Onboarding

- `README.md`: purpose, prerequisites, setup, first command, verification command,
  and documentation map.
- `AGENTS.md`: the authoritative, concise instructions for coding agents.
- `CONTRIBUTING.md`: the authoritative development workflow and definition of
  done.
- `ARCHITECTURE.md`: only implemented boundaries and dependency direction.
- This specification, its implementation plan, and one concise ADR for the
  bootstrap toolchain.

`.github/copilot-instructions.md` points to `AGENTS.md`; it does not duplicate
agent rules. Other documents link to `CONTRIBUTING.md` rather than copying the
workflow.

### Agent roles

Repository custom-agent profiles under `.github/agents/` define:

- **Planner:** turns an accepted specification into a dependency-ordered plan.
- **Test adversary:** finds missing behavior and weak assertions without
  replacing implementation-owner testing.
- **Integrator:** verifies the assembled change against the accepted
  specification.
- **Security reviewer:** reviews security-relevant changes for concrete exploit
  paths.

These profiles make responsibilities repeatable but cannot prove that an agent
was invoked. Review use is recorded in the pull request.

### Repository automation

`uv run --frozen poe check` runs these local, deterministic checks:

1. Lockfile consistency.
2. Formatting.
3. Linting, including static security rules.
4. Type checking.
5. Tests and coverage.
6. Package build without build isolation.

CI runs that exact task on fresh Windows and Linux runners. Coverage measures
`src/vertigo` and must remain at least 80%. Meaningless coverage-padding tests
are forbidden and this rule takes precedence: simplify or remove dead code, test
real behavior, or change the policy through an accepted specification.

A separate scheduled job runs the network-dependent dependency vulnerability
audit. It is not described as deterministic and is not part of `poe check`.
Dependency update configuration and a pull-request template are committed.

CodeQL, GitHub secret scanning, Copilot automatic pull-request review, required
status checks, required reviews, and default-branch protection depend on the
eventual repository visibility, licensing, and GitHub settings. `README.md`
lists them as hosted setup, clearly marked **not enforced by this checkout**.
They are not milestone 0 acceptance gates. Static security linting remains
enforced locally and in CI.

## Development workflow

### Change tiers

- **Trivial:** no behavior change; implement and run deterministic checks.
- **Normal:** specify, plan, implement with tests, run deterministic checks,
  obtain independent correctness review, then integrate.
- **High risk:** add adversarial specification review and specialized security
  review.

Normal and high-risk changes use pull requests once a GitHub repository exists.
Trivial changes may use a pull request when review or CI evidence is useful.

### Sequence

1. Write the specification with goals, non-goals, acceptance criteria,
   contracts, risks, and failure behavior.
2. Independently challenge non-trivial specifications before planning.
3. Resolve findings and create a dependency-ordered implementation plan.
4. Fan out only tasks with stable contracts, exclusive ownership, explicit
   acceptance criteria, no hidden sequencing dependency, and a named integrator.
5. Implementation owners write meaningful tests with or before production code.
6. Run deterministic checks before LLM review.
7. Use independent correctness review and, when relevant, test-adversary and
   security review.
8. The integrator verifies the complete change against the specification.
9. Convert escaped gaps into the smallest useful regression test, deterministic
   rule, or documentation correction.

Steps involving reviewers and integrators are conventions recorded in the pull
request until hosted branch rules can enforce them. CI can enforce only the
deterministic checks.

## Definition of done

- Acceptance criteria are met.
- `uv run --frozen poe check` passes from a clean checkout.
- Behavior changes have meaningful tests.
- Coverage of `src/vertigo` remains at least 80% without padding.
- Affected documentation and decisions are updated.
- Required review findings are resolved or rejected with a technical reason.
- The integrator verifies the assembled result for normal and high-risk changes.

## Risks

- Process documents can become unreadable bureaucracy. Each topic therefore has
  one authoritative file and duplicated rules should be deleted.
- A green hello-world pipeline proves wiring, not product quality or security.
- Hosted controls may be unavailable until repository visibility and licensing
  are decided. Documentation must not present them as active.
- The advisory database changes over time. Dependency auditing is intentionally
  separated from deterministic validation.

## Non-goals

- Any adversarial-testing product logic.
- HTTP clients, LLM providers, attack scenarios, target adapters, or Docker.
- Designing future product architecture before product contracts exist.
- A web interface, service, database, plugin system, or deployment topology.
- Mandatory subagents for small or tightly coupled work.
- LLM review inside deterministic CI or as a required status check.
- CodeQL or other controls that depend on undecided GitHub hosting capabilities.
- Choosing repository visibility, licensing, or a production release model.

## Acceptance criteria

1. On a fresh CI runner, the README's documented commands install dependencies,
   run `uv run --frozen vertigo hello`, and run
   `uv run --frozen poe check` without undocumented steps.
2. The valid command matches the stdout, stderr, and exit-status contract.
3. Missing and unknown subcommands match the documented argparse failure
   behavior.
4. Local and CI deterministic verification use the same Poe task.
5. CI runs on Windows and Linux and enforces lockfile consistency, formatting,
   security-aware linting, type checking, source-package coverage of at least
   80%, tests, and build.
6. The dependency audit runs separately on a schedule and can also be dispatched
   manually.
7. `AGENTS.md`, Copilot instructions, custom agents, and the pull-request
   template agree with `CONTRIBUTING.md` without copying the full workflow.
8. `ARCHITECTURE.md` documents only code that exists.
9. The committed plan records why this small milestone is not fanned out.
10. The README distinguishes checkout-enforced controls from GitHub-hosted
    settings that still require manual configuration.
