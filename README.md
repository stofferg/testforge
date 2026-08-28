# TestForge

A small Python test automation project built with Playwright and pytest.

## Goals

- Learn modern UI test automation
- Practice pytest and Playwright
- Build toward a reusable test framework
- Add CI and reporting over time

## Current Features

- Playwright browser automation with Python
- pytest test runner and fixtures
- Playwright `expect()` assertions with automatic waiting
- Accessible locators such as `get_by_role()`
- Page Object Model structure for reusable UI behavior
- Page-to-page navigation using page objects
- Shared test setup in `conftest.py`
- Isolated tests that each start from a clean browser page
- Centralized project configuration with `pyproject.toml`
- Runtime base URL support via pytest's `--base-url` option
- Dependency tracking with `requirements.txt`
- Git/GitHub version control with small, incremental commits

## Project Structure

```text
testforge/
├── pages/              # Page objects and UI behavior
├── tests/              # Test cases and pytest fixtures
├── pyproject.toml      # pytest configuration
├── requirements.txt    # Python dependencies
└── README.md
```

## Running the Tests

Activate the virtual environment, then run:

```powershell
pytest
```

To run against a specific base URL:

```powershell
pytest --base-url https://example.com
```

To watch the browser while tests run:

```powershell
pytest --headed
```

## Concepts Practiced

The project is being built incrementally to practice framework design, maintainable selectors, reusable setup, test isolation, page objects, environment configuration, and reliable browser assertions.

## Next Steps

The planned learning path is:

1. **Environment configuration** — support cleaner dev/QA/staging-style configuration without changing test code.
2. **Better test data management** — separate reusable test data from page objects and tests.
3. **More realistic test scenarios** — move beyond example.com and automate a small public demo application with forms, navigation, and validation.
4. **Parameterized tests** — use pytest parameterization to run the same test logic with multiple data sets.
5. **Negative and boundary testing** — add tests for invalid inputs and failure paths, not just happy paths.
6. **Screenshots, traces, and diagnostics** — capture useful artifacts when a test fails and learn Playwright tracing.
7. **Test markers and suites** — organize tests into groups such as smoke, regression, and UI.
8. **Cross-browser execution** — run the suite against Chromium, Firefox, and WebKit.
9. **Parallel execution** — understand when and how to run tests concurrently.
10. **Reporting** — add readable test reports and useful failure information.
11. **GitHub Actions CI** — automatically install dependencies and run the test suite on every push or pull request.
12. **CI artifacts** — preserve reports, screenshots, and traces from failed CI runs.
13. **API testing** — add Playwright APIRequestContext or another Python HTTP client to cover API-level tests alongside UI tests.
14. **Secrets and authentication** — handle credentials safely and explore reusable authenticated browser state.
15. **Code quality** — add formatting, linting, type checking, and simple quality gates.
16. **Interview-ready architecture review** — be able to explain why the framework uses fixtures, page objects, configuration, assertions, test isolation, CI, and diagnostics.

The goal is not to add complexity for its own sake. Each step should introduce one practical automation-engineering concept and keep the framework understandable.