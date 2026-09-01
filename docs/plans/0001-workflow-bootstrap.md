# Plan 0001: Workflow Bootstrap

**Specification:** `docs/specs/0001-workflow-bootstrap.md`  
**Integrator:** milestone implementation owner

## Fan-out decision

Do not fan out implementation. The executable is a few lines, while the
toolchain, documentation, and CI all reference the same commands and policies.
Parallel ownership would cost more coordination than it saves and would make
inconsistency more likely. Independent agents are still used for adversarial
specification, correctness, test-gap, and security reviews at their defined
gates.

## Implementation order

1. **Toolchain contract**
   - Add Python 3.13 and `uv` configuration.
   - Configure Ruff, mypy, pytest/coverage, Poe, build, and dependency audit.
   - Record the toolchain decision in an ADR.
   - Generate and commit `uv.lock`.
2. **Executable contract using TDD**
   - Add failing tests for valid, missing, and unknown commands.
   - Implement the `vertigo` package and `argparse` CLI.
   - Keep production dependencies empty.
3. **Authoritative onboarding**
   - Add `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `ARCHITECTURE.md`.
   - Make `CONTRIBUTING.md` the workflow authority and `AGENTS.md` the
     agent-instruction authority.
   - Link rather than duplicate rules.
4. **Agent and pull-request infrastructure**
   - Add repository Copilot instructions and planner, test-adversary, integrator,
     and security-reviewer profiles.
   - Add a pull-request template that records tier, specification, deterministic
     checks, and required reviews.
5. **Automation**
   - Add cross-platform pull-request CI using the local Poe task.
   - Add a separate scheduled/manual dependency audit.
   - Add dependency update configuration.
6. **Integration**
   - Run the hello command and deterministic verification from the locked
     environment.
   - Run an independent correctness review.
   - Run test-adversary review.
   - Security-review only the workflow's executable and automation surfaces;
     product security review remains out of scope.
   - Resolve findings and verify every acceptance criterion.

## Ownership

The implementation owner may modify all milestone files. Review agents are
read-only and return findings to the implementation owner. This avoids
concurrent edits and leaves one integrator accountable for consistency.

## Expected files

```text
.github/
  agents/
  workflows/
  copilot-instructions.md
  dependabot.yml
  pull_request_template.md
docs/
  adr/0001-bootstrap-toolchain.md
  plans/0001-workflow-bootstrap.md
  specs/0001-workflow-bootstrap.md
src/vertigo/
tests/
.gitignore
.python-version
AGENTS.md
ARCHITECTURE.md
CONTRIBUTING.md
README.md
pyproject.toml
uv.lock
```

## Validation

The integration gate is:

```text
uv run --frozen vertigo hello
uv run --frozen poe check
```

The first command must satisfy the exact CLI contract. The second must be the
same deterministic task invoked by CI.

## Integration record

| Acceptance criterion | Evidence |
| --- | --- |
| Fresh-run onboarding | CI uses the README commands on fresh Windows and Linux runners |
| Exact valid command | Unit and installed-script tests assert exit status and raw stdout/stderr |
| Invalid commands | Parameterized tests assert argparse usage and exit status `2` |
| Shared verification | Developers and CI run `uv run --frozen poe check` |
| Deterministic gates | Lock, format, lint/security, typing, tests/coverage, and build pass |
| Dependency audit | Scheduled/manual workflow exists; local audit found no known vulnerabilities |
| Consistent guidance | Agent profiles and Copilot instructions link to the authoritative files |
| Current architecture only | `ARCHITECTURE.md` documents only the implemented CLI boundary |
| Fan-out decision | This plan records why implementation remained with one owner |
| Hosted controls | README clearly labels settings that the checkout cannot enforce |

Adversarial specification, correctness, test-adversary, and security reviews
were completed. All reported findings were resolved before integration.
