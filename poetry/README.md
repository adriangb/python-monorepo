# Poetry monorepo

This is a Cargo-like monorepo where there are several subprojects in `workspaces/` and a top-level virtual project that has a `pyproject.toml` and `poetry.lock` file.
Each workspace gets it's own dependency group so if you want to install a single workspace (e.g. to run unit tests in CI) you can run `poetry install --only cli` which will install `cli` and `lib` (because `cli` depends on it).
If you run `poetry install` you get all groups which is probably what you want for local development.

## Usage

1. Install [pipx].
2. Run `make init`.
3. To test a single package run `make test-lib`. To test all packages run `make tests`.

[pipx]: https://pypa.github.io/pipx/

## Test dependencies

Since each subproject is treated as an arbitrary Python package dependency groups do not leak through.
So instead of Poetry dependency groups test / dev / benchmark dependencies are handled with extras: `poetry install --only cli-test`.
