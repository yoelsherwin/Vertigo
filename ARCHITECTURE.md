# Architecture

## Implemented boundary

Vertigo is currently a local Python console application:

```text
console entry point -> vertigo.cli.main -> Python standard library
```

`src/vertigo/cli.py` owns argument parsing and the hello-world behavior.
`tests/` verifies the public CLI contract. Packaging maps the `vertigo` command
to `vertigo.cli:main`.

Production code has no third-party runtime dependencies. Development tools are
locked separately in `uv.lock`.

## Dependency direction

- Production modules may depend on the Python standard library.
- Tests may depend on production modules and development-only test tools.
- Production modules must not import from tests, documentation, automation, or
  future adapters.

## Not designed yet

There is no product architecture for targets, attacker models, orchestration,
scenarios, persistence, reporting, or deployment. Those boundaries must follow
accepted product specifications rather than being invented during bootstrap.
