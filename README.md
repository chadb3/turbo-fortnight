# math-ci-demo

[![Test Status:](https://github.com/chadb3/turbo-fortnight/actions/workflows/tests.yml/badge.svg)](https://github.com/chadb3/turbo-fortnight/actions/workflows/tests.yml)

A tiny Python project meant to demonstrate how GitHub automatically tests
your code every time you push. Repository name was the "random" one GitHub provided. There's nothing fancy here on purpose: a
handful of math functions, a pytest test suite for them, and a GitHub
Actions workflow that runs that suite on every push.

## Project layout

```
math-ci-demo/
├── mathops.py                  # the functions being tested
├── tests/
│   └── test_mathops.py         # pytest tests for mathops.py
├── conftest.py                 # lets pytest find mathops.py from tests/
├── requirements.txt            # just pytest
└── .github/
    └── workflows/
        └── tests.yml           # the CI workflow GitHub runs automatically
```

## The math functions

`mathops.py` has six small functions: `add`, `subtract`, `multiply`,
`divide` (raises `ValueError` on divide-by-zero), `is_prime`, and
`factorial` (raises `ValueError` on negative input). Each is simple enough
that it's obvious what "correct" looks like, which makes them easy to test.

## Running the tests yourself

```bash
pip install -r requirements.txt
pytest -v
```

You should see all tests pass.

## How GitHub's automatic testing works

This is the part you asked about. GitHub itself doesn't run your tests —
it runs whatever workflow you define using **GitHub Actions**, a free CI
(continuous integration) system built into every GitHub repository.

1. **You define a workflow file** in `.github/workflows/`. This repo's is
   `tests.yml`. GitHub looks for YAML files in that exact folder and treats
   each one as a workflow.
2. **The `on:` section says when it runs.** Here it's `push` and
   `pull_request` on the `main` branch — so every time you push a commit,
   or open/update a pull request, GitHub kicks the workflow off
   automatically. No one has to click a button.
3. **GitHub spins up a fresh virtual machine** (`ubuntu-latest` here) that
   has nothing on it but a bare OS.
4. **The `steps:` run in order** on that machine: check out your code
   (`actions/checkout`), install Python (`actions/setup-python`), install
   dependencies (`pip install -r requirements.txt`), then run `pytest -v`.
5. **The result shows up right in GitHub** — a green check or red X next
   to your commit, on the pull request, and under the repo's "Actions" tab.
   If any test fails, the whole run is marked failed, which is exactly the
   signal you want before merging broken code.

This workflow also uses a **matrix** to run the same tests against Python
3.10, 3.11, and 3.12 in parallel, so you'd notice immediately if a change
only breaks on one version.