# Contributing

Vertigo uses a spec-first workflow. The purpose is to make behavior and
boundaries explicit before agents produce code, not to create paperwork.

## Setup and verification

Install `uv`, then run:

```console
uv run --frozen vertigo hello
uv run --frozen poe check
```

`poe check` is the local and CI integration gate. The dependency audit is
network-dependent and intentionally separate:

```console
uv run --frozen poe audit
```

## Change tiers

| Tier | Use when | Required flow |
| --- | --- | --- |
| Trivial | No behavior changes | Implement, test if relevant, deterministic checks |
| Normal | Bounded behavior changes | Spec, plan, implementation tests, checks, correctness review, integration |
| High risk | Security boundaries, secrets, external input, persistence, code execution, or network scope | Normal flow plus adversarial spec and security reviews |

## Workflow

1. **Specify.** Write goals, non-goals, contracts, failure behavior, risks, and
   testable acceptance criteria under `docs/specs/`. Only an accepted spec can
   be implemented.
2. **Challenge.** For non-trivial work, use an independent reviewer to find
   ambiguity, unsafe assumptions, gaps, and unnecessary scope. Resolve findings
   before planning.
3. **Plan.** Record dependencies, ownership, validation, integration, and the
   fan-out decision under `docs/plans/`.
4. **Implement with tests.** The implementation owner writes meaningful tests
   before or alongside behavior.
5. **Verify deterministically.** Run `uv run --frozen poe check` before asking an
   LLM to review the change.
6. **Review independently.** Use correctness review for normal work. Add the test
   adversary for non-obvious behavior and the security reviewer for high-risk
   changes.
7. **Integrate.** One owner verifies the complete change against the accepted
   spec. Component completion claims are not evidence of integration.
8. **Learn.** Turn escaped gaps into the smallest useful regression test,
   deterministic rule, or documentation correction.

## Fan-out contracts

Do not fan out by default. Parallel tasks require all of the following:

- Stable input and output contracts.
- Independent acceptance criteria.
- Exclusive file or component ownership.
- No hidden sequencing dependency.
- A named integrator.

If merging parallel results is likely to cost more than sequential
implementation, keep the work with one owner.

## Testing policy

- Test public behavior, boundaries, regressions, and failure modes.
- Keep coverage of `src/vertigo` at or above 80%; the threshold is a tripwire,
  not the goal.
- Do not test framework wiring, trivial constants, or private implementation
  solely to increase coverage.
- If useful tests cannot preserve the threshold, simplify or delete dead code.
  Changing the threshold requires an accepted specification.
- Prefer small builders and local setup. Use shared fixtures only for stable,
  representative setup.
- Operational failures must not become successful or clean security verdicts.

## Review responsibilities

- **Implementation owner:** behavior and its tests.
- **Correctness reviewer:** specification conformance, logic, errors, and
  compatibility.
- **Test adversary:** missing cases, weak assertions, and false-positive tests.
- **Security reviewer:** concrete exploit paths in security-relevant changes.
- **Integrator:** cross-component behavior and final acceptance criteria.

Formatting, linting, typing, tests, coverage, and build belong to deterministic
automation, not LLM review.

## Definition of done

- Acceptance criteria are met.
- `uv run --frozen poe check` passes.
- Behavior changes have meaningful tests without coverage padding.
- Affected documentation and ADRs are updated.
- Required findings are resolved or rejected with a technical reason.
- The integrator verifies normal and high-risk changes against the accepted spec.

Review steps are conventions recorded in the pull request until GitHub branch
rules enforce them. See `README.md` for hosted settings not enforced by the
checkout.
